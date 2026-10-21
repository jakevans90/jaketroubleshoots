#!/usr/bin/env python3
"""Collect a guarded HTM Hiring Pulse pilot from public employer career pages.

Collection is a dry run unless --apply is supplied. Missing postings are only
closed when every selected source produced a verified complete snapshot and the
operator also supplies --confirm-close-missing.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import timedelta
from pathlib import Path
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, unquote, urlsplit
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser

sys.path.insert(0, str(Path(__file__).resolve().parent))
import htm_hiring_pulse as pulse


CONFIG_PATH = Path("data/htm-hiring-pulse/collection-sources.json")
USER_AGENT = "JakeTroubleshoots-HTM-Hiring-Pulse/1.0"
ADAPTERS = {"workday", "phenom"}
US_STATES = {
    "alabama": "AL", "alaska": "AK", "arizona": "AZ", "arkansas": "AR", "california": "CA",
    "colorado": "CO", "connecticut": "CT", "delaware": "DE", "district of columbia": "DC",
    "florida": "FL", "georgia": "GA", "hawaii": "HI", "idaho": "ID", "illinois": "IL",
    "indiana": "IN", "iowa": "IA", "kansas": "KS", "kentucky": "KY", "louisiana": "LA",
    "maine": "ME", "maryland": "MD", "massachusetts": "MA", "michigan": "MI", "minnesota": "MN",
    "mississippi": "MS", "missouri": "MO", "montana": "MT", "nebraska": "NE", "nevada": "NV",
    "new hampshire": "NH", "new jersey": "NJ", "new mexico": "NM", "new york": "NY",
    "north carolina": "NC", "north dakota": "ND", "ohio": "OH", "oklahoma": "OK", "oregon": "OR",
    "pennsylvania": "PA", "rhode island": "RI", "south carolina": "SC", "south dakota": "SD",
    "tennessee": "TN", "texas": "TX", "utah": "UT", "vermont": "VT", "virginia": "VA",
    "washington": "WA", "west virginia": "WV", "wisconsin": "WI", "wyoming": "WY",
}
STATE_CODES = set(US_STATES.values())


class CollectionError(ValueError):
    pass


@dataclass
class CollectionResult:
    source_id: str
    postings: list[dict[str, Any]]
    scanned: int
    complete: bool
    query_totals: dict[str, int]


def load_config(root: Path) -> dict[str, Any]:
    config = pulse.load_json(root / CONFIG_PATH)
    errors = validate_config(config)
    if errors:
        raise CollectionError("Invalid collection source configuration:\n" + "\n".join(errors))
    return config


def validate_config(config: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if set(config) != {"schemaVersion", "sources"}:
        errors.append("root must contain exactly schemaVersion and sources")
    if config.get("schemaVersion") != 2:
        errors.append("schemaVersion must be 2")
    sources = config.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("sources must be a non-empty array")
        return errors
    ids: set[str] = set()
    expected = {"id", "enabled", "employer", "adapter", "queries", "relevancePatterns", "excludePatterns", "roleOverrides", "adapterConfig", "metadata"}
    employer_fields = {"name", "employerType", "careerUrl", "websiteUrl"}
    for index, source in enumerate(sources):
        where = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{where} must be an object")
            continue
        if set(source) != expected:
            errors.append(f"{where} must contain exactly {', '.join(sorted(expected))}")
        source_id = source.get("id")
        if not isinstance(source_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", source_id):
            errors.append(f"{where}.id must be lowercase hyphenated text")
        elif source_id in ids:
            errors.append(f"{where}.id duplicates {source_id}")
        ids.add(source_id)
        if not isinstance(source.get("enabled"), bool):
            errors.append(f"{where}.enabled must be a boolean")
        employer = source.get("employer")
        if not isinstance(employer, dict) or set(employer) != employer_fields:
            errors.append(f"{where}.employer must contain exactly {', '.join(sorted(employer_fields))}")
        elif employer.get("employerType") not in pulse.EMPLOYER_TYPES:
            errors.append(f"{where}.employer.employerType is invalid")
        if source.get("adapter") not in ADAPTERS:
            errors.append(f"{where}.adapter must be workday or phenom")
        for field in ("queries", "relevancePatterns"):
            values = source.get(field)
            if not isinstance(values, list) or not values or not all(isinstance(value, str) and value.strip() for value in values):
                errors.append(f"{where}.{field} must be a non-empty array of strings")
        for pattern in source.get("relevancePatterns", []):
            try:
                re.compile(pattern, re.IGNORECASE)
            except re.error as exc:
                errors.append(f"{where}.relevancePatterns contains invalid regex: {exc}")
        exclusions = source.get("excludePatterns")
        if not isinstance(exclusions, list) or not all(isinstance(value, str) and value.strip() for value in exclusions):
            errors.append(f"{where}.excludePatterns must be an array of strings")
        for pattern in exclusions or []:
            try:
                re.compile(pattern, re.IGNORECASE)
            except re.error as exc:
                errors.append(f"{where}.excludePatterns contains invalid regex: {exc}")
        overrides = source.get("roleOverrides")
        if not isinstance(overrides, list):
            errors.append(f"{where}.roleOverrides must be an array")
        else:
            for override in overrides:
                if not isinstance(override, dict) or set(override) != {"pattern", "roleCategoryId"}:
                    errors.append(f"{where}.roleOverrides entries need pattern and roleCategoryId")
                    continue
                try:
                    re.compile(override["pattern"], re.IGNORECASE)
                except (re.error, TypeError) as exc:
                    errors.append(f"{where}.roleOverrides contains invalid regex: {exc}")
        adapter_config = source.get("adapterConfig")
        if not isinstance(adapter_config, dict):
            errors.append(f"{where}.adapterConfig must be an object")
            continue
        common = {"publicBaseUrl", "publicSitePath", "robotsUrl", "pageSize", "maxResultsPerQuery"}
        specific = {"apiUrl"} if source.get("adapter") == "workday" else {"searchUrl", "jobIdentifierField", "queryParameter"}
        allowed_config = common | specific | ({"allowUnknownUsLocation"} if source.get("adapter") == "workday" else set())
        config_fields = set(adapter_config)
        if config_fields != common | specific and config_fields != allowed_config:
            errors.append(f"{where}.adapterConfig fields do not match the selected adapter")
        for field in (common | specific) - {"jobIdentifierField", "queryParameter", "pageSize", "maxResultsPerQuery", "publicSitePath"}:
            if field in adapter_config and not pulse.is_web_url(adapter_config.get(field)):
                errors.append(f"{where}.adapterConfig.{field} must be an HTTP(S) URL")
        for field in ("pageSize", "maxResultsPerQuery"):
            if not isinstance(adapter_config.get(field), int) or adapter_config.get(field, 0) <= 0:
                errors.append(f"{where}.adapterConfig.{field} must be a positive integer")
        if "allowUnknownUsLocation" in adapter_config and not isinstance(adapter_config.get("allowUnknownUsLocation"), bool):
            errors.append(f"{where}.adapterConfig.allowUnknownUsLocation must be a boolean")
        if source.get("adapter") == "phenom" and adapter_config.get("queryParameter") is not None:
            if not isinstance(adapter_config.get("queryParameter"), str) or not adapter_config["queryParameter"].strip():
                errors.append(f"{where}.adapterConfig.queryParameter must be null or non-empty text")
        metadata = source.get("metadata")
        metadata_fields = {"firstTracked", "lastSuccessfulCheck", "lastSuccessfulPostingCount", "collectionStatus", "fullyAutomated", "notes"}
        if not isinstance(metadata, dict) or set(metadata) != metadata_fields:
            errors.append(f"{where}.metadata must contain exactly {', '.join(sorted(metadata_fields))}")
        else:
            try:
                if not isinstance(metadata.get("firstTracked"), str) or pulse.normalize_date(metadata["firstTracked"]) != metadata["firstTracked"]:
                    raise ValueError
            except ValueError:
                errors.append(f"{where}.metadata.firstTracked must use YYYY-MM-DD")
            if metadata.get("lastSuccessfulCheck") is not None:
                try:
                    pulse.parse_timestamp(metadata["lastSuccessfulCheck"])
                except (TypeError, ValueError):
                    errors.append(f"{where}.metadata.lastSuccessfulCheck must be null or a timestamp")
            if metadata.get("lastSuccessfulPostingCount") is not None and (not isinstance(metadata.get("lastSuccessfulPostingCount"), int) or metadata["lastSuccessfulPostingCount"] < 0):
                errors.append(f"{where}.metadata.lastSuccessfulPostingCount must be null or a non-negative integer")
            if metadata.get("collectionStatus") not in {"active", "partial", "failed", "not-started", "disabled"}:
                errors.append(f"{where}.metadata.collectionStatus is invalid")
            if not isinstance(metadata.get("fullyAutomated"), bool):
                errors.append(f"{where}.metadata.fullyAutomated must be a boolean")
            if not isinstance(metadata.get("notes"), str):
                errors.append(f"{where}.metadata.notes must be text")
    return errors


def request_bytes(url: str, timeout: int, body: dict[str, Any] | None = None, attempts: int = 3) -> bytes:
    data = None if body is None else json.dumps(body).encode("utf-8")
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json, text/html;q=0.9"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            with urlopen(Request(url, data=data, headers=headers), timeout=timeout) as response:
                status = getattr(response, "status", 200)
                if status != 200:
                    raise CollectionError(f"Unexpected HTTP {status} from {url}")
                return response.read()
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_error = exc
            if attempt + 1 < attempts:
                time.sleep(attempt + 1)
    raise CollectionError(f"Request failed after {attempts} attempts: {url}: {last_error}")


def get_text(url: str, timeout: int) -> str:
    return request_bytes(url, timeout).decode("utf-8", errors="replace")


def post_json(url: str, payload: dict[str, Any], timeout: int) -> dict[str, Any]:
    try:
        value = json.loads(request_bytes(url, timeout, payload).decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise CollectionError(f"Invalid JSON returned by {url}: {exc}") from exc
    if not isinstance(value, dict):
        raise CollectionError(f"Expected a JSON object from {url}")
    return value


def ensure_robots_allowed(source: dict[str, Any], timeout: int) -> None:
    adapter = source["adapterConfig"]
    robots_text = get_text(adapter["robotsUrl"], timeout)
    parser = RobotFileParser()
    parser.set_url(adapter["robotsUrl"])
    parser.parse(robots_text.splitlines())
    target = adapter.get("apiUrl") or adapter.get("searchUrl")
    if not parser.can_fetch(USER_AGENT, target):
        raise CollectionError(f"robots.txt does not permit collection for {source['id']}: {target}")


def parse_phenom_ddo(html: str) -> dict[str, Any]:
    marker = "phApp.ddo ="
    start = html.find(marker)
    if start < 0:
        raise CollectionError("Phenom page did not contain phApp.ddo data")
    raw = html[start + len(marker):].lstrip()
    try:
        value, _ = json.JSONDecoder().raw_decode(raw)
    except json.JSONDecodeError as exc:
        raise CollectionError(f"Could not decode Phenom job data: {exc}") from exc
    if not isinstance(value, dict):
        raise CollectionError("Phenom phApp.ddo value was not an object")
    return value


def phenom_page_data(html: str) -> tuple[list[dict[str, Any]], int, int]:
    root = parse_phenom_ddo(html)
    result = root.get("eagerLoadRefineSearch")
    if not isinstance(result, dict) or result.get("status") != 200:
        raise CollectionError("Phenom search data was missing or unsuccessful")
    jobs = result.get("data", {}).get("jobs")
    hits, total = result.get("hits"), result.get("totalHits")
    if not isinstance(jobs, list) or not isinstance(hits, int) or not isinstance(total, int):
        raise CollectionError("Phenom search response did not include jobs, hits, and totalHits")
    if hits != len(jobs):
        raise CollectionError(f"Phenom hit count mismatch: declared {hits}, received {len(jobs)}")
    return jobs, hits, total


def slugify(value: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", pulse.normalize_text(value))).strip("-")


def parse_posted_date(value: Any, checked_at: str) -> str | None:
    cleaned = pulse.clean_optional(value)
    if not cleaned:
        return None
    iso = re.match(r"^(\d{4}-\d{2}-\d{2})", cleaned)
    if iso:
        return iso.group(1)
    checked = pulse.parse_timestamp(checked_at).date()
    normalized = cleaned.casefold()
    if "today" in normalized:
        return checked.isoformat()
    if "yesterday" in normalized:
        return (checked - timedelta(days=1)).isoformat()
    days = re.search(r"posted\s+(\d+)\s+days?\s+ago", normalized)
    if days and "+" not in normalized:
        return (checked - timedelta(days=int(days.group(1)))).isoformat()
    return None


def state_from_text(value: str) -> str | None:
    text = value or ""
    for match in re.finditer(r"(?:^|[,\s-])([A-Z]{2})(?=\s*(?:\d{5}(?:-\d{4})?)?(?:,|$))", text):
        if match.group(1) in STATE_CODES:
            return match.group(1)
    normalized = pulse.normalize_text(text)
    for name, code in US_STATES.items():
        if re.search(rf"\b{re.escape(name)}\b", normalized):
            return code
    return None


def location_payload(text: Any, country: Any = "US", fallback: str | None = None) -> dict[str, Any]:
    display = pulse.clean_optional(text) or pulse.clean_optional(fallback) or "Location not listed"
    remote = "remote" in display.casefold() or "anywhere" in display.casefold()
    state = state_from_text(display)
    city = None
    parts = [part.strip() for part in display.split(",") if part.strip()]
    if parts and not remote:
        candidate = re.sub(r"\s+\d{5}(?:-\d{4})?$", "", parts[0 if len(parts) == 2 else max(0, len(parts) - 2)]).strip()
        if candidate and pulse.normalize_text(candidate) not in US_STATES:
            city = candidate
    country_text = pulse.clean_optional(country) or "US"
    country_code = "US" if pulse.normalize_text(country_text) in {"us", "usa", "united states", "united states of america"} else country_text.upper()
    return {"text": display, "city": city, "state": state, "country": country_code, "remote": remote}


def is_us_job(location: dict[str, Any], allow_unknown_location: bool = False) -> bool:
    return location.get("country") == "US" and bool(location.get("state") or location.get("remote") or allow_unknown_location)


def relevant_title(source: dict[str, Any], title: str) -> bool:
    included = any(re.search(pattern, title, re.IGNORECASE) for pattern in source["relevancePatterns"])
    excluded = any(re.search(pattern, title, re.IGNORECASE) for pattern in source.get("excludePatterns", []))
    return included and not excluded


def role_override(source: dict[str, Any], title: str) -> str | None:
    for override in source["roleOverrides"]:
        if re.search(override["pattern"], title, re.IGNORECASE):
            return override["roleCategoryId"]
    return None


def make_common_record(source: dict[str, Any], title: str, location: dict[str, Any], url: str, source_id: str,
                       posted_date: str | None = None, employment_type: Any = None,
                       salary: Any = None, description: Any = None) -> dict[str, Any]:
    record = {
        "employer": source["employer"],
        "title": " ".join(title.split()),
        "location": location,
        "url": url,
        "sourcePostingId": source_id,
        "employmentType": pulse.clean_optional(employment_type),
        "experienceLevel": None,
        "salaryText": pulse.clean_optional(salary),
        "postedDate": posted_date,
        "descriptionSnippet": pulse.clean_optional(description),
    }
    override = role_override(source, title)
    if override:
        record["roleCategoryId"] = override
    return record


def workday_record(source: dict[str, Any], job: dict[str, Any], checked_at: str) -> dict[str, Any] | None:
    title = pulse.clean_optional(job.get("title"))
    external_path = pulse.clean_optional(job.get("externalPath"))
    if not title or not external_path or not relevant_title(source, title):
        return None
    location_text = pulse.clean_optional(job.get("locationsText")) or "Location not listed"
    fallback = None
    path_match = re.match(r"/job/([^/]+)/", external_path)
    if path_match:
        fallback = unquote(path_match.group(1)).replace("-", " ")
    location = location_payload(location_text, "US", fallback)
    if not location.get("state") and fallback:
        fallback_state = state_from_text(fallback)
        if fallback_state:
            location["state"] = fallback_state
            location["remote"] = location["remote"] or "anywhere" in fallback.casefold()
    if not is_us_job(location, bool(source["adapterConfig"].get("allowUnknownUsLocation"))):
        return None
    requisition = re.search(r"_([A-Za-z]+\d+)$", external_path)
    source_id = requisition.group(1) if requisition else external_path.rstrip("/").split("_")[-1]
    adapter = source["adapterConfig"]
    url = adapter["publicBaseUrl"].rstrip("/") + adapter["publicSitePath"] + external_path
    bullet_fields = job.get("bulletFields")
    description = " · ".join(str(item) for item in bullet_fields) if isinstance(bullet_fields, list) else None
    return make_common_record(
        source, title, location, url, source_id,
        parse_posted_date(job.get("postedOn"), checked_at), job.get("timeType"), None, description,
    )


def phenom_record(source: dict[str, Any], job: dict[str, Any], checked_at: str) -> dict[str, Any] | None:
    title = pulse.clean_optional(job.get("title"))
    job_id = pulse.clean_optional(job.get("jobId"))
    if not title or not job_id or not relevant_title(source, title):
        return None
    country = job.get("country") or "US"
    location = location_payload(job.get("cityState") or job.get("location"), country)
    if not is_us_job(location):
        return None
    adapter = source["adapterConfig"]
    identifier = pulse.clean_optional(job.get(adapter["jobIdentifierField"])) or job_id
    url = (
        adapter["publicBaseUrl"].rstrip("/") + adapter["publicSitePath"]
        + "/job/" + quote(identifier, safe="") + "/" + slugify(title)
    )
    description = (
        job.get("descriptionTeaser_first200") or job.get("descriptionTeaser_keyword")
        or job.get("descriptionTeaser") or job.get("descriptionTeaser_ats")
    )
    salary = job.get("salary") or job.get("payRange") or job.get("salaryText")
    employment_type = job.get("type") or job.get("jobType")
    return make_common_record(
        source, title, location, url, job_id,
        parse_posted_date(job.get("postedDate") or job.get("dateCreated"), checked_at),
        employment_type, salary, description,
    )


def collect_workday(source: dict[str, Any], checked_at: str, timeout: int,
                    post: Callable[[str, dict[str, Any], int], dict[str, Any]] = post_json) -> CollectionResult:
    adapter = source["adapterConfig"]
    page_size = adapter["pageSize"]
    scanned = 0
    totals: dict[str, int] = {}
    by_id: dict[str, dict[str, Any]] = {}
    complete = True
    for query in source["queries"]:
        offset = 0
        retrieved = 0
        total = None
        maximum_total = 0
        query_stable = True
        page_fingerprints: set[tuple[str, ...]] = set()
        while total is None or offset < maximum_total:
            response = post(adapter["apiUrl"], {"appliedFacets": {}, "limit": page_size, "offset": offset, "searchText": query}, timeout)
            jobs = response.get("jobPostings")
            declared_total = response.get("total")
            if not isinstance(jobs, list) or not isinstance(declared_total, int):
                raise CollectionError(f"{source['id']} Workday response lacked jobPostings or total")
            if declared_total > adapter["maxResultsPerQuery"]:
                raise CollectionError(f"{source['id']} query '{query}' unexpectedly returned {declared_total} jobs")
            if total is None:
                total = declared_total
                maximum_total = declared_total
            elif total != declared_total:
                query_stable = False
                complete = False
                total = declared_total
                maximum_total = max(maximum_total, declared_total)
            totals[query] = maximum_total
            if declared_total and not jobs and offset < declared_total:
                raise CollectionError(f"{source['id']} returned an empty Workday page before completion")
            retrieved += len(jobs)
            scanned += len(jobs)
            page_ids = tuple(
                pulse.clean_optional(job.get("externalPath")) or f"missing-{index}"
                for index, job in enumerate(jobs) if isinstance(job, dict)
            )
            if page_ids and page_ids in page_fingerprints:
                complete = False
            page_fingerprints.add(page_ids)
            for job in jobs:
                if isinstance(job, dict):
                    record = workday_record(source, job, checked_at)
                    if record:
                        by_id[record["sourcePostingId"]] = record
            offset += len(jobs)
            if not jobs:
                break
        if query_stable and retrieved != (total or 0):
            raise CollectionError(f"{source['id']} retrieved {retrieved} of {total} Workday jobs for '{query}'")
    if not by_id:
        raise CollectionError(f"{source['id']} returned zero relevant US jobs; refusing to create a snapshot")
    return CollectionResult(source["id"], sorted(by_id.values(), key=lambda item: (item["title"].casefold(), item["sourcePostingId"])), scanned, complete, totals)


def collect_phenom(source: dict[str, Any], checked_at: str, timeout: int,
                   get: Callable[[str, int], str] = get_text) -> CollectionResult:
    adapter = source["adapterConfig"]
    scanned = 0
    totals: dict[str, int] = {}
    by_id: dict[str, dict[str, Any]] = {}
    complete = True
    for query in source["queries"]:
        offset = 0
        retrieved = 0
        total = None
        maximum_total = 0
        query_stable = True
        page_fingerprints: set[tuple[str, ...]] = set()
        while total is None or offset < maximum_total:
            parameters: dict[str, Any] = {"from": offset, "s": 1}
            if adapter.get("queryParameter"):
                parameters[adapter["queryParameter"]] = query
            params = urlencode(parameters)
            jobs, hits, declared_total = phenom_page_data(get(adapter["searchUrl"] + "?" + params, timeout))
            if declared_total > adapter["maxResultsPerQuery"]:
                raise CollectionError(f"{source['id']} query '{query}' unexpectedly returned {declared_total} jobs")
            if total is None:
                total = declared_total
                maximum_total = declared_total
            elif total != declared_total:
                query_stable = False
                complete = False
                total = declared_total
                maximum_total = max(maximum_total, declared_total)
            totals[query] = maximum_total
            if declared_total and not jobs and offset < declared_total:
                raise CollectionError(f"{source['id']} returned an empty Phenom page before completion")
            retrieved += hits
            scanned += hits
            page_ids = tuple(
                pulse.clean_optional(job.get("jobId")) or f"missing-{index}"
                for index, job in enumerate(jobs) if isinstance(job, dict)
            )
            if page_ids and page_ids in page_fingerprints:
                complete = False
            page_fingerprints.add(page_ids)
            for job in jobs:
                if isinstance(job, dict):
                    record = phenom_record(source, job, checked_at)
                    if record:
                        by_id[record["sourcePostingId"]] = record
            offset += hits
            if not hits:
                break
        if query_stable and retrieved != (total or 0):
            raise CollectionError(f"{source['id']} retrieved {retrieved} of {total} Phenom jobs for '{query}'")
    if not by_id:
        raise CollectionError(f"{source['id']} returned zero relevant US jobs; refusing to create a snapshot")
    return CollectionResult(source["id"], sorted(by_id.values(), key=lambda item: (item["title"].casefold(), item["sourcePostingId"])), scanned, complete, totals)


def selected_sources(config: dict[str, Any], requested: list[str] | None) -> list[dict[str, Any]]:
    available = {source["id"]: source for source in config["sources"] if source["enabled"]}
    if not requested:
        return list(available.values())
    unknown = sorted(set(requested) - set(available))
    if unknown:
        raise CollectionError("Unknown or disabled source(s): " + ", ".join(unknown))
    return [available[source_id] for source_id in requested]


def reclassify_configured_postings(store: dict[str, dict[str, Any]], config: dict[str, Any], timestamp: str) -> int:
    sources = {source["id"]: source for source in config["sources"]}
    changed = 0
    for posting in store["postings"]["records"]:
        source = sources.get(posting.get("source"))
        if not source:
            continue
        role_id = role_override(source, posting["title"]) or pulse.classify_role(posting["title"], store["taxonomy"])
        if posting.get("role_category_id") == role_id:
            continue
        posting["role_category_id"] = role_id
        posting["updated_at"] = timestamp
        changed += 1
    return changed


def command_list(args: argparse.Namespace) -> int:
    config = load_config(args.root)
    for source in config["sources"]:
        status = "enabled" if source["enabled"] else "disabled"
        print(f"{source['id']}\t{source['adapter']}\t{status}\t{source['employer']['name']}")
    return 0


def command_collect(args: argparse.Namespace) -> int:
    config = load_config(args.root)
    sources = selected_sources(config, args.source)
    checked_at = pulse.normalize_timestamp(args.checked_at)
    results: list[CollectionResult] = []
    for source in sources:
        ensure_robots_allowed(source, args.timeout)
        collector = collect_workday if source["adapter"] == "workday" else collect_phenom
        results.append(collector(source, checked_at, args.timeout))
    if args.confirm_close_missing and not all(result.complete for result in results):
        raise CollectionError("Closure requested, but at least one selected source was not a complete snapshot")

    store = copy.deepcopy(pulse.load_store(args.root))
    checks = []
    reports = []
    for result in results:
        complete = bool(args.confirm_close_missing and result.complete)
        check = pulse.upsert_records(store, result.postings, result.source_id, checked_at, complete)
        checks.append(check)
        reports.append({
            "source": result.source_id,
            "queries": result.query_totals,
            "recordsScanned": result.scanned,
            "relevantUniquePostings": len(result.postings),
            "snapshotVerifiedComplete": result.complete,
            "missingJobsMayClose": complete,
            "check": check,
        })
    reclassified = reclassify_configured_postings(store, config, checked_at)
    changed = {"employers", "postings", "observations"}
    pulse.stamp_changed(store, changed, checked_at)
    errors = pulse.validate_store(store)
    if errors:
        raise CollectionError("Validation failed after collection:\n" + "\n".join(errors))
    report = {
        "schemaVersion": 1,
        "checkedAt": checked_at,
        "dryRun": not args.apply,
        "sources": reports,
        "reclassifiedPostings": reclassified,
        "summary": pulse.build_summary(store, checked_at, args.since_days),
    }
    rendered = pulse.render_json(report)
    sys.stdout.buffer.write(rendered)
    if args.report:
        report_path = args.report if args.report.is_absolute() else args.root / args.report
        if args.apply:
            pulse.atomic_write(report_path, rendered)
            print(f"wrote {report_path}", file=sys.stderr)
        else:
            print("DRY RUN: report output not written", file=sys.stderr)
    pulse.save_store(args.root, store, changed, dry_run=not args.apply)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=pulse.ROOT, help="Repository root")
    commands = parser.add_subparsers(dest="command", required=True)
    listing = commands.add_parser("list-sources", help="List configured pilot sources")
    listing.set_defaults(func=command_list)
    collect = commands.add_parser("collect", help="Collect and validate pilot postings; dry-run by default")
    collect.add_argument("--source", action="append", help="Source id to collect; repeat as needed; defaults to all enabled")
    collect.add_argument("--checked-at", help="UTC ISO-8601 observation time; defaults to now")
    collect.add_argument("--timeout", type=int, default=30, help="Per-request timeout in seconds")
    collect.add_argument("--since-days", type=int, default=7, help="New-posting window used in the preview summary")
    collect.add_argument("--apply", action="store_true", help="Write validated employer, posting, and observation data")
    collect.add_argument("--confirm-close-missing", action="store_true", help="Treat verified snapshots as complete and close absent jobs")
    collect.add_argument("--report", type=Path, help="Optional JSON report path; only written with --apply")
    collect.set_defaults(func=command_collect)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if getattr(args, "timeout", 1) <= 0:
        parser.error("--timeout must be positive")
    if getattr(args, "since_days", 1) <= 0:
        parser.error("--since-days must be positive")
    try:
        return args.func(args)
    except (CollectionError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
