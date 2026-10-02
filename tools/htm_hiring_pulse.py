#!/usr/bin/env python3
"""Maintain the private data foundation for HTM Hiring Pulse.

The public jobs page does not consume these files yet. This CLI deliberately
uses only the Python standard library so it works with the site's existing
maintenance environment.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import unicodedata
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = Path("data/htm-hiring-pulse")
FILES = {
    "employers": "employers.json",
    "postings": "postings.json",
    "observations": "observations.json",
    "taxonomy": "role-taxonomy.json",
}
TRACKING_QUERY_KEYS = {
    "fbclid", "gclid", "mc_cid", "mc_eid", "ref", "referrer", "source",
}
EMPLOYER_TYPES = {"health-system", "hospital", "oem", "iso", "vendor", "dialysis", "government", "education", "other"}
POSTING_STATUSES = {"active", "closed"}
OBSERVATION_STATUSES = {"seen", "reopened", "closed"}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_timestamp(value: str) -> datetime:
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value or ""):
        value += "T00:00:00Z"
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def normalize_timestamp(value: str | None) -> str:
    if not value:
        return utc_now()
    return parse_timestamp(value).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def normalize_text(value: str) -> str:
    text = unicodedata.normalize("NFKD", value or "").encode("ascii", "ignore").decode("ascii")
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text.casefold()).split())


def stable_id(prefix: str, *parts: str) -> str:
    payload = "\x1f".join(parts).encode("utf-8")
    return f"{prefix}_{hashlib.sha256(payload).hexdigest()[:16]}"


def canonicalize_url(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    parsed = urlsplit(raw)
    if parsed.scheme and parsed.scheme.casefold() not in {"http", "https"}:
        return raw
    scheme = parsed.scheme.casefold() or "https"
    host = parsed.netloc.casefold()
    if not host and parsed.path:
        parsed = urlsplit("https://" + raw)
        scheme, host = "https", parsed.netloc.casefold()
    if scheme == "http" and host.endswith(":80"):
        host = host[:-3]
    if scheme == "https" and host.endswith(":443"):
        host = host[:-4]
    path = re.sub(r"/{2,}", "/", parsed.path or "/")
    if path != "/":
        path = path.rstrip("/")
    query = []
    for key, item in parse_qsl(parsed.query, keep_blank_values=True):
        lowered = key.casefold()
        if lowered.startswith("utm_") or lowered in TRACKING_QUERY_KEYS:
            continue
        query.append((key, item))
    return urlunsplit((scheme, host, path, urlencode(sorted(query)), ""))


def is_web_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlsplit(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def normalize_location(value: Any) -> dict[str, Any]:
    if isinstance(value, str):
        text = " ".join(value.split())
        return {"text": text, "city": None, "state": None, "country": "US", "remote": "remote" in text.casefold()}
    if not isinstance(value, dict):
        raise ValueError("location must be a string or object")
    city = clean_optional(value.get("city"))
    state = clean_optional(value.get("state"))
    country = clean_optional(value.get("country")) or "US"
    remote = bool(value.get("remote", False))
    text = clean_optional(value.get("text"))
    if not text:
        text = ", ".join(item for item in (city, state, country) if item)
        if remote:
            text = (text + " — Remote").strip(" —")
    return {"text": text, "city": city, "state": state.upper() if state else None, "country": country.upper(), "remote": remote}


def clean_optional(value: Any) -> str | None:
    if value is None:
        return None
    cleaned = " ".join(str(value).split())
    return cleaned or None


def location_key(location: dict[str, Any]) -> str:
    return "|".join([
        normalize_text(location.get("text") or ""),
        normalize_text(location.get("city") or ""),
        normalize_text(location.get("state") or ""),
        normalize_text(location.get("country") or ""),
        "remote" if location.get("remote") else "onsite",
    ])


def dedupe_key(employer_id: str, title: str, location: dict[str, Any], url: str) -> str:
    return stable_id("dedupe", employer_id, normalize_text(title), location_key(location), canonicalize_url(url))


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Missing data file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def load_store(root: Path) -> dict[str, dict[str, Any]]:
    base = root / DATA_DIR
    return {name: load_json(base / filename) for name, filename in FILES.items()}


def render_json(value: Any) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def atomic_write(path: Path, contents: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(handle, "wb") as stream:
            stream.write(contents)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def save_store(root: Path, store: dict[str, dict[str, Any]], changed: set[str], dry_run: bool) -> None:
    if dry_run:
        print("DRY RUN: no files written")
        return
    base = root / DATA_DIR
    for name in sorted(changed):
        atomic_write(base / FILES[name], render_json(store[name]))
        print(f"updated {DATA_DIR.as_posix()}/{FILES[name]}")


def read_input(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read input {path}: {exc}") from exc


def taxonomy_ids(store: dict[str, dict[str, Any]]) -> set[str]:
    return {item["id"] for item in store["taxonomy"].get("categories", []) if isinstance(item, dict) and isinstance(item.get("id"), str)}


def classify_role(title: str, taxonomy: dict[str, Any]) -> str:
    normalized = normalize_text(title)
    for category in taxonomy.get("categories", []):
        if category.get("id") == "other-htm":
            continue
        for pattern in category.get("titlePatterns", []):
            if normalize_text(pattern) in normalized:
                return category["id"]
    return "other-htm"


def find_or_create_employer(
    store: dict[str, dict[str, Any]], value: str | dict[str, Any], timestamp: str
) -> tuple[dict[str, Any], bool, bool]:
    payload = {"name": value} if isinstance(value, str) else dict(value)
    name = clean_optional(payload.get("name"))
    if not name:
        raise ValueError("Every posting needs a non-empty employer name")
    normalized = normalize_text(name)
    records = store["employers"]["records"]
    existing = next((item for item in records if item["normalized_name"] == normalized or normalized in item.get("normalized_aliases", [])), None)
    if existing:
        changed = False
        for input_key, record_key in (("careerUrl", "career_url"), ("websiteUrl", "website_url"), ("employerType", "employer_type")):
            if payload.get(input_key) is not None:
                new_value = clean_optional(payload[input_key])
                if record_key.endswith("_url") and new_value:
                    new_value = canonicalize_url(new_value)
                if existing.get(record_key) != new_value:
                    existing[record_key] = new_value
                    changed = True
        aliases = sorted({*existing.get("aliases", []), *(payload.get("aliases") or [])}, key=str.casefold)
        normalized_aliases = sorted({normalize_text(item) for item in aliases if clean_optional(item)})
        if aliases != existing.get("aliases") or normalized_aliases != existing.get("normalized_aliases"):
            existing["aliases"], existing["normalized_aliases"] = aliases, normalized_aliases
            changed = True
        if changed:
            existing["updated_at"] = timestamp
        return existing, False, changed
    employer_type = payload.get("employerType") or "other"
    if employer_type not in EMPLOYER_TYPES:
        raise ValueError(f"Unknown employerType: {employer_type}")
    aliases = sorted({clean_optional(item) for item in payload.get("aliases", []) if clean_optional(item)}, key=str.casefold)
    record = {
        "id": stable_id("emp", normalized),
        "name": name,
        "normalized_name": normalized,
        "aliases": aliases,
        "normalized_aliases": sorted({normalize_text(item) for item in aliases}),
        "employer_type": employer_type,
        "career_url": canonicalize_url(payload.get("careerUrl", "")) or None,
        "website_url": canonicalize_url(payload.get("websiteUrl", "")) or None,
        "headquarters_location": normalize_location(payload["headquartersLocation"]) if payload.get("headquartersLocation") else None,
        "active": True,
        "created_at": timestamp,
        "updated_at": timestamp,
    }
    records.append(record)
    return record, True, True


def make_posting_payload(raw: dict[str, Any], source: str, timestamp: str, store: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], bool, bool]:
    if not isinstance(raw, dict):
        raise ValueError("Each posting must be an object")
    title = clean_optional(raw.get("title"))
    url = canonicalize_url(raw.get("url", ""))
    if not title or not url:
        raise ValueError("Every posting needs non-empty title and url values")
    if not is_web_url(url):
        raise ValueError(f"Posting url must be an absolute HTTP(S) URL: {raw.get('url', '')}")
    employer, employer_created, employer_changed = find_or_create_employer(store, raw.get("employer", ""), timestamp)
    location = normalize_location(raw.get("location", ""))
    role_id = raw.get("roleCategoryId") or classify_role(title, store["taxonomy"])
    if role_id not in taxonomy_ids(store):
        raise ValueError(f"Unknown roleCategoryId: {role_id}")
    source_posting_id = clean_optional(raw.get("sourcePostingId"))
    key = dedupe_key(employer["id"], title, location, url)
    records = store["postings"]["records"]
    existing = None
    if source_posting_id:
        existing = next((item for item in records if item["source"] == source and item.get("source_posting_id") == source_posting_id), None)
    if not existing:
        existing = next((item for item in records if item["canonical_url"] == url), None)
    if not existing:
        existing = next((item for item in records if item["dedupe_key"] == key), None)
    fields = {
        "employer_id": employer["id"],
        "title": title,
        "normalized_title": normalize_text(title),
        "role_category_id": role_id,
        "location": location,
        "canonical_url": url,
        "source": source,
        "source_posting_id": source_posting_id,
        "employment_type": clean_optional(raw.get("employmentType")),
        "experience_level": clean_optional(raw.get("experienceLevel")),
        "salary_text": clean_optional(raw.get("salaryText")),
        "description_snippet": clean_optional(raw.get("descriptionSnippet")),
    }
    if existing:
        changed = any(existing.get(name) != value for name, value in fields.items()) or existing.get("status") != "active"
        existing.update(fields)
        existing["dedupe_key"] = key
        existing["last_seen"] = timestamp
        existing["status"] = "active"
        existing["closed_at"] = None
        if changed:
            existing["updated_at"] = timestamp
        return existing, False, changed or employer_changed
    record = {
        "id": stable_id("job", key),
        **fields,
        "dedupe_key": key,
        "first_seen": timestamp,
        "last_seen": timestamp,
        "status": "active",
        "closed_at": None,
        "created_at": timestamp,
        "updated_at": timestamp,
    }
    records.append(record)
    return record, True, True


def append_observation(store: dict[str, dict[str, Any]], posting: dict[str, Any], check_id: str, timestamp: str, status: str, raw_url: str | None = None, note: str | None = None) -> None:
    sequence = len(store["observations"]["records"])
    record = {
        "id": stable_id("obs", check_id, posting["id"], status, str(sequence)),
        "check_id": check_id,
        "posting_id": posting["id"],
        "source": posting["source"],
        "observed_at": timestamp,
        "status": status,
        "raw_url": clean_optional(raw_url),
        "note": clean_optional(note),
    }
    store["observations"]["records"].append(record)


def new_check_id(source: str, timestamp: str) -> str:
    return stable_id("check", normalize_text(source), timestamp)


def upsert_records(store: dict[str, dict[str, Any]], raw_records: list[Any], source: str, timestamp: str, complete: bool) -> dict[str, Any]:
    check_id = new_check_id(source, timestamp)
    seen_ids: set[str] = set()
    counts = Counter()
    for raw in raw_records:
        previous = None
        source_posting_id = clean_optional(raw.get("sourcePostingId")) if isinstance(raw, dict) else None
        canonical_url = canonicalize_url(raw.get("url", "")) if isinstance(raw, dict) else ""
        if source_posting_id:
            previous = next((item for item in store["postings"]["records"] if item["source"] == source and item.get("source_posting_id") == source_posting_id), None)
        if not previous and canonical_url:
            previous = next((item for item in store["postings"]["records"] if item["canonical_url"] == canonical_url), None)
        was_closed = bool(previous and previous.get("status") == "closed")
        posting, created, changed = make_posting_payload(raw, source, timestamp, store)
        seen_ids.add(posting["id"])
        if created:
            counts["new"] += 1
            observation_status = "seen"
        elif was_closed:
            counts["reopened"] += 1
            observation_status = "reopened"
        else:
            counts["updated" if changed else "unchanged"] += 1
            observation_status = "seen"
        append_observation(store, posting, check_id, timestamp, observation_status, raw.get("url"))
    if complete:
        for posting in store["postings"]["records"]:
            if posting["source"] != source or posting["status"] != "active" or posting["id"] in seen_ids:
                continue
            posting["status"] = "closed"
            posting["closed_at"] = timestamp
            posting["updated_at"] = timestamp
            counts["closed"] += 1
            append_observation(store, posting, check_id, timestamp, "closed", note="Absent from complete source check")
    check = {
        "id": check_id,
        "source": source,
        "checked_at": timestamp,
        "complete": complete,
        "observed_count": len(raw_records),
        "new_count": counts["new"],
        "updated_count": counts["updated"],
        "unchanged_count": counts["unchanged"],
        "reopened_count": counts["reopened"],
        "closed_count": counts["closed"],
    }
    store["observations"]["checks"].append(check)
    return check


def validate_store(store: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    root_fields = {
        "employers": {"schemaVersion", "updatedAt", "records"},
        "postings": {"schemaVersion", "updatedAt", "records"},
        "observations": {"schemaVersion", "updatedAt", "checks", "records"},
        "taxonomy": {"schemaVersion", "updatedAt", "categories"},
    }
    for name in FILES:
        value = store.get(name)
        if not isinstance(value, dict):
            errors.append(f"{name}: root must be an object")
            continue
        missing = root_fields[name] - set(value)
        extra = set(value) - root_fields[name]
        if missing:
            errors.append(f"{name}: missing root fields {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"{name}: unexpected root fields {', '.join(sorted(extra))}")
        if value.get("schemaVersion") != 1:
            errors.append(f"{name}: schemaVersion must be 1")
        if value.get("updatedAt") is not None:
            validate_timestamps(value, ("updatedAt",), name, errors)
    employers = store.get("employers", {}).get("records")
    postings = store.get("postings", {}).get("records")
    observations = store.get("observations", {}).get("records")
    checks = store.get("observations", {}).get("checks")
    categories = store.get("taxonomy", {}).get("categories")
    for label, records in (("employers", employers), ("postings", postings), ("observations.records", observations), ("observations.checks", checks), ("taxonomy.categories", categories)):
        if not isinstance(records, list):
            errors.append(f"{label} must be an array")
    if errors:
        return errors
    employer_ids = set()
    employer_names = set()
    for index, item in enumerate(employers):
        where = f"employers.records[{index}]"
        required = {"id", "name", "normalized_name", "aliases", "normalized_aliases", "employer_type", "career_url", "website_url", "headquarters_location", "active", "created_at", "updated_at"}
        check_required(item, required, where, errors)
        if not isinstance(item, dict):
            continue
        if item.get("id") in employer_ids:
            errors.append(f"{where}: duplicate id {item.get('id')}")
        employer_ids.add(item.get("id"))
        if item.get("normalized_name") in employer_names:
            errors.append(f"{where}: duplicate normalized_name {item.get('normalized_name')}")
        employer_names.add(item.get("normalized_name"))
        if item.get("employer_type") not in EMPLOYER_TYPES:
            errors.append(f"{where}: invalid employer_type")
        if not isinstance(item.get("active"), bool):
            errors.append(f"{where}.active must be a boolean")
        if not isinstance(item.get("aliases"), list) or not all(isinstance(alias, str) for alias in item.get("aliases", [])):
            errors.append(f"{where}.aliases must be an array of strings")
        if not isinstance(item.get("normalized_aliases"), list) or not all(isinstance(alias, str) for alias in item.get("normalized_aliases", [])):
            errors.append(f"{where}.normalized_aliases must be an array of strings")
        for field in ("career_url", "website_url"):
            if item.get(field) is not None and not is_web_url(item.get(field)):
                errors.append(f"{where}.{field} must be null or an absolute HTTP(S) URL")
        validate_timestamps(item, ("created_at", "updated_at"), where, errors)
    category_ids = set()
    for index, item in enumerate(categories):
        where = f"role-taxonomy.categories[{index}]"
        check_required(item, {"id", "label", "description", "titlePatterns"}, where, errors)
        if not isinstance(item, dict):
            continue
        if item.get("id") in category_ids:
            errors.append(f"{where}: duplicate id {item.get('id')}")
        category_ids.add(item.get("id"))
        if not isinstance(item.get("titlePatterns"), list):
            errors.append(f"{where}.titlePatterns must be an array")
        elif not all(isinstance(pattern, str) and pattern.strip() for pattern in item["titlePatterns"]):
            errors.append(f"{where}.titlePatterns must contain non-empty strings")
    posting_ids, posting_urls, posting_keys = set(), set(), set()
    for index, item in enumerate(postings):
        where = f"postings.records[{index}]"
        required = {"id", "employer_id", "title", "normalized_title", "role_category_id", "location", "canonical_url", "source", "source_posting_id", "employment_type", "experience_level", "salary_text", "description_snippet", "dedupe_key", "first_seen", "last_seen", "status", "closed_at", "created_at", "updated_at"}
        check_required(item, required, where, errors)
        if not isinstance(item, dict):
            continue
        posting_id = item.get("id")
        if posting_id in posting_ids:
            errors.append(f"{where}: duplicate id {posting_id}")
        posting_ids.add(posting_id)
        if item.get("canonical_url") in posting_urls:
            errors.append(f"{where}: duplicate canonical_url {item.get('canonical_url')}")
        posting_urls.add(item.get("canonical_url"))
        if item.get("dedupe_key") in posting_keys:
            errors.append(f"{where}: duplicate dedupe_key {item.get('dedupe_key')}")
        posting_keys.add(item.get("dedupe_key"))
        if item.get("employer_id") not in employer_ids:
            errors.append(f"{where}: unknown employer_id {item.get('employer_id')}")
        if item.get("role_category_id") not in category_ids:
            errors.append(f"{where}: unknown role_category_id {item.get('role_category_id')}")
        if item.get("status") not in POSTING_STATUSES:
            errors.append(f"{where}: invalid status")
        if not is_web_url(item.get("canonical_url")):
            errors.append(f"{where}.canonical_url must be an absolute HTTP(S) URL")
        if item.get("status") == "active" and item.get("closed_at") is not None:
            errors.append(f"{where}: active posting cannot have closed_at")
        if item.get("status") == "closed" and not item.get("closed_at"):
            errors.append(f"{where}: closed posting needs closed_at")
        if not isinstance(item.get("location"), dict):
            errors.append(f"{where}.location must be an object")
        else:
            location = item["location"]
            expected_location_fields = {"text", "city", "state", "country", "remote"}
            if set(location) != expected_location_fields:
                errors.append(f"{where}.location must contain exactly text, city, state, country, and remote")
            if not isinstance(location.get("text"), str) or not location.get("text").strip():
                errors.append(f"{where}.location.text must be a non-empty string")
            if not isinstance(location.get("remote"), bool):
                errors.append(f"{where}.location.remote must be a boolean")
        validate_timestamps(item, ("first_seen", "last_seen", "created_at", "updated_at"), where, errors)
        if item.get("closed_at"):
            validate_timestamps(item, ("closed_at",), where, errors)
        validate_timestamp_order(item, where, errors)
    check_ids = set()
    for index, item in enumerate(checks):
        where = f"observations.checks[{index}]"
        check_required(item, {"id", "source", "checked_at", "complete", "observed_count", "new_count", "updated_count", "unchanged_count", "reopened_count", "closed_count"}, where, errors)
        if not isinstance(item, dict):
            continue
        if item.get("id") in check_ids:
            errors.append(f"{where}: duplicate id {item.get('id')}")
        check_ids.add(item.get("id"))
        if not isinstance(item.get("complete"), bool):
            errors.append(f"{where}.complete must be a boolean")
        for field in ("observed_count", "new_count", "updated_count", "unchanged_count", "reopened_count", "closed_count"):
            if not isinstance(item.get(field), int) or isinstance(item.get(field), bool) or item.get(field, -1) < 0:
                errors.append(f"{where}.{field} must be a non-negative integer")
        validate_timestamps(item, ("checked_at",), where, errors)
    observation_ids = set()
    for index, item in enumerate(observations):
        where = f"observations.records[{index}]"
        check_required(item, {"id", "check_id", "posting_id", "source", "observed_at", "status", "raw_url", "note"}, where, errors)
        if not isinstance(item, dict):
            continue
        if item.get("id") in observation_ids:
            errors.append(f"{where}: duplicate id {item.get('id')}")
        observation_ids.add(item.get("id"))
        if item.get("check_id") not in check_ids:
            errors.append(f"{where}: unknown check_id {item.get('check_id')}")
        if item.get("posting_id") not in posting_ids:
            errors.append(f"{where}: unknown posting_id {item.get('posting_id')}")
        if item.get("status") not in OBSERVATION_STATUSES:
            errors.append(f"{where}: invalid status")
        validate_timestamps(item, ("observed_at",), where, errors)
    return errors


def check_required(item: Any, required: set[str], where: str, errors: list[str]) -> None:
    if not isinstance(item, dict):
        errors.append(f"{where} must be an object")
        return
    missing = required - set(item)
    extra = set(item) - required
    if missing:
        errors.append(f"{where}: missing fields {', '.join(sorted(missing))}")
    if extra:
        errors.append(f"{where}: unexpected fields {', '.join(sorted(extra))}")


def validate_timestamps(item: dict[str, Any], fields: tuple[str, ...], where: str, errors: list[str]) -> None:
    for field in fields:
        try:
            parse_timestamp(item[field])
        except (KeyError, TypeError, ValueError):
            errors.append(f"{where}.{field} must be an ISO-8601 timestamp")


def validate_timestamp_order(item: dict[str, Any], where: str, errors: list[str]) -> None:
    try:
        first_seen = parse_timestamp(item["first_seen"])
        last_seen = parse_timestamp(item["last_seen"])
        created_at = parse_timestamp(item["created_at"])
        updated_at = parse_timestamp(item["updated_at"])
        if first_seen > last_seen:
            errors.append(f"{where}: first_seen cannot be after last_seen")
        if created_at > updated_at:
            errors.append(f"{where}: created_at cannot be after updated_at")
        if item.get("closed_at") and parse_timestamp(item["closed_at"]) < last_seen:
            errors.append(f"{where}: closed_at cannot be before last_seen")
    except (KeyError, TypeError, ValueError):
        pass


def stamp_changed(store: dict[str, dict[str, Any]], changed: set[str], timestamp: str) -> None:
    for name in changed:
        store[name]["updatedAt"] = timestamp


def print_check(check: dict[str, Any]) -> None:
    print(json.dumps(check, indent=2, ensure_ascii=False))


def command_validate(args: argparse.Namespace) -> int:
    errors = validate_store(load_store(args.root))
    if errors:
        for error in errors:
            print("ERROR:", error)
        print(f"Validation failed: {len(errors)} error(s)")
        return 1
    print("HTM Hiring Pulse data is valid")
    return 0


def command_upsert(args: argparse.Namespace) -> int:
    store = load_store(args.root)
    timestamp = normalize_timestamp(args.observed_at)
    payload = read_input(args.input)
    raw_records = payload.get("postings") if isinstance(payload, dict) and "postings" in payload else payload
    if isinstance(raw_records, dict):
        raw_records = [raw_records]
    if not isinstance(raw_records, list):
        raise ValueError("Input must be a posting object, an array, or an object with a postings array")
    check = upsert_records(store, raw_records, args.source, timestamp, complete=False)
    changed = {"employers", "postings", "observations"}
    stamp_changed(store, changed, timestamp)
    errors = validate_store(store)
    if errors:
        raise ValueError("Validation failed after upsert:\n" + "\n".join(errors))
    print_check(check)
    save_store(args.root, store, changed, args.dry_run)
    return 0


def command_sync(args: argparse.Namespace) -> int:
    store = load_store(args.root)
    timestamp = normalize_timestamp(args.checked_at)
    payload = read_input(args.input)
    raw_records = payload.get("postings") if isinstance(payload, dict) and "postings" in payload else payload
    if not isinstance(raw_records, list):
        raise ValueError("Sync input must be an array or an object with a postings array")
    check = upsert_records(store, raw_records, args.source, timestamp, complete=args.complete)
    changed = {"employers", "postings", "observations"}
    stamp_changed(store, changed, timestamp)
    errors = validate_store(store)
    if errors:
        raise ValueError("Validation failed after sync:\n" + "\n".join(errors))
    print_check(check)
    save_store(args.root, store, changed, args.dry_run)
    return 0


def command_update(args: argparse.Namespace) -> int:
    store = load_store(args.root)
    timestamp = normalize_timestamp(args.updated_at)
    patch = read_input(args.input)
    if not isinstance(patch, dict):
        raise ValueError("Update input must be an object")
    posting = next((item for item in store["postings"]["records"] if item["id"] == args.id), None)
    if not posting:
        raise ValueError(f"Unknown posting id: {args.id}")
    allowed = {"title", "roleCategoryId", "location", "url", "employmentType", "experienceLevel", "salaryText", "descriptionSnippet"}
    unknown = set(patch) - allowed
    if unknown:
        raise ValueError("Unsupported update fields: " + ", ".join(sorted(unknown)))
    if "title" in patch:
        posting["title"] = clean_optional(patch["title"])
        if not posting["title"]:
            raise ValueError("title cannot be empty")
        posting["normalized_title"] = normalize_text(posting["title"])
    if "roleCategoryId" in patch:
        if patch["roleCategoryId"] not in taxonomy_ids(store):
            raise ValueError(f"Unknown roleCategoryId: {patch['roleCategoryId']}")
        posting["role_category_id"] = patch["roleCategoryId"]
    if "location" in patch:
        posting["location"] = normalize_location(patch["location"])
    if "url" in patch:
        posting["canonical_url"] = canonicalize_url(patch["url"])
        if not is_web_url(posting["canonical_url"]):
            raise ValueError("url must be an absolute HTTP(S) URL")
    for input_key, record_key in (("employmentType", "employment_type"), ("experienceLevel", "experience_level"), ("salaryText", "salary_text"), ("descriptionSnippet", "description_snippet")):
        if input_key in patch:
            posting[record_key] = clean_optional(patch[input_key])
    posting["dedupe_key"] = dedupe_key(posting["employer_id"], posting["title"], posting["location"], posting["canonical_url"])
    posting["updated_at"] = timestamp
    store["postings"]["updatedAt"] = timestamp
    errors = validate_store(store)
    if errors:
        raise ValueError("Validation failed after update:\n" + "\n".join(errors))
    print(json.dumps(posting, indent=2, ensure_ascii=False))
    save_store(args.root, store, {"postings"}, args.dry_run)
    return 0


def build_summary(store: dict[str, dict[str, Any]], as_of: str, since_days: int) -> dict[str, Any]:
    as_of_dt = parse_timestamp(as_of)
    window_start = as_of_dt - timedelta(days=since_days)
    active = [item for item in store["postings"]["records"] if item["status"] == "active" and parse_timestamp(item["first_seen"]) <= as_of_dt]
    employers = {item["employer_id"] for item in active}
    newly_observed = [item for item in store["postings"]["records"] if window_start <= parse_timestamp(item["first_seen"]) <= as_of_dt]
    states = sorted({item["location"].get("state") for item in active if item.get("location", {}).get("state")})
    role_counts = Counter(item["role_category_id"] for item in active)
    labels = {item["id"]: item["label"] for item in store["taxonomy"]["categories"]}
    return {
        "schemaVersion": 1,
        "generatedAt": utc_now(),
        "asOf": as_of,
        "newWindowStart": window_start.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "activePostings": len(active),
        "employersRepresented": len(employers),
        "newlyObservedJobs": len(newly_observed),
        "statesRepresented": {"count": len(states), "states": states},
        "roleCategories": [
            {"id": role_id, "label": labels.get(role_id, role_id), "activePostings": count}
            for role_id, count in sorted(role_counts.items(), key=lambda item: (-item[1], item[0]))
        ],
    }


def command_summary(args: argparse.Namespace) -> int:
    store = load_store(args.root)
    errors = validate_store(store)
    if errors:
        raise ValueError("Cannot summarize invalid data:\n" + "\n".join(errors))
    as_of = normalize_timestamp(args.as_of)
    summary = build_summary(store, as_of, args.since_days)
    rendered = render_json(summary)
    sys.stdout.buffer.write(rendered)
    if args.output:
        if args.dry_run:
            print("DRY RUN: summary output not written", file=sys.stderr)
        else:
            output = args.output if args.output.is_absolute() else args.root / args.output
            atomic_write(output, rendered)
            print(f"wrote {output}", file=sys.stderr)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="Validate all four data files and cross-file references")
    validate.set_defaults(func=command_validate)

    upsert = subparsers.add_parser("upsert", help="Add or update one or more postings without closing absent jobs")
    upsert.add_argument("--input", type=Path, required=True)
    upsert.add_argument("--source", required=True)
    upsert.add_argument("--observed-at")
    upsert.add_argument("--dry-run", action="store_true")
    upsert.set_defaults(func=command_upsert)

    sync = subparsers.add_parser("sync", help="Apply a source snapshot; --complete closes active jobs absent from that snapshot")
    sync.add_argument("--input", type=Path, required=True)
    sync.add_argument("--source", required=True)
    sync.add_argument("--checked-at")
    sync.add_argument("--complete", action="store_true")
    sync.add_argument("--dry-run", action="store_true")
    sync.set_defaults(func=command_sync)

    update = subparsers.add_parser("update", help="Patch a posting by stable posting id")
    update.add_argument("--id", required=True)
    update.add_argument("--input", type=Path, required=True)
    update.add_argument("--updated-at")
    update.add_argument("--dry-run", action="store_true")
    update.set_defaults(func=command_update)

    summary = subparsers.add_parser("summary", help="Generate current Hiring Pulse summary statistics")
    summary.add_argument("--as-of")
    summary.add_argument("--since-days", type=int, default=7)
    summary.add_argument("--output", type=Path)
    summary.add_argument("--dry-run", action="store_true")
    summary.set_defaults(func=command_summary)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if getattr(args, "since_days", 0) < 0:
        parser.error("--since-days must be zero or greater")
    try:
        return args.func(args)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
