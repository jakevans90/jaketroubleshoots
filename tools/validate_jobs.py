"""Validate the static jobs dataset and, optionally, its append-only history.

No third-party packages are needed. The structural checker implements only the
JSON Schema keywords used in data/jobs.schema.json; it is not a general engine.
"""
from __future__ import annotations

import argparse
from datetime import date, datetime
import json
import math
from pathlib import Path
import re
from urllib.parse import urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON property: {key}")
        result[key] = value
    return result


def load_json(path):
    def reject_constant(value):
        raise ValueError(f"Non-finite JSON number: {value}")
    return json.loads(Path(path).read_text(encoding="utf-8"),
                      object_pairs_hook=_unique_object,
                      parse_constant=reject_constant)


def _structure(value, rule, schema, path="dataset"):
    if "$ref" in rule:
        return _structure(value, schema["$defs"][rule["$ref"].split("/")[-1]], schema, path)
    if "anyOf" in rule:
        choices = [_structure(value, branch, schema, path) for branch in rule["anyOf"]]
        if any(not errors for errors in choices):
            return []
        return [f"{path}: does not match an allowed value ({'; '.join(choices[0])})"]
    errors = []
    kind = rule.get("type")
    matches = {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value),
        "null": value is None,
    }
    if kind and not matches[kind]:
        return [f"{path}: expected {kind}"]
    if "enum" in rule and value not in rule["enum"]:
        errors.append(f"{path}: expected one of {rule['enum']}")
    if "const" in rule and value != rule["const"]:
        errors.append(f"{path}: expected {rule['const']}")
    if isinstance(value, dict):
        for key in rule.get("required", []):
            if key not in value:
                errors.append(f"{path}.{key}: required")
        props = rule.get("properties", {})
        for key, child in value.items():
            if key in props:
                errors.extend(_structure(child, props[key], schema, f"{path}.{key}"))
            elif rule.get("additionalProperties") is False:
                errors.append(f"{path}.{key}: unexpected property")
    if isinstance(value, list) and "items" in rule:
        for index, child in enumerate(value):
            errors.extend(_structure(child, rule["items"], schema, f"{path}[{index}]"))
    if isinstance(value, str):
        if len(value) < rule.get("minLength", 0):
            errors.append(f"{path}: must not be empty")
        if "pattern" in rule and not re.search(rule["pattern"], value):
            errors.append(f"{path}: invalid format")
        try:
            if rule.get("format") == "date":
                date.fromisoformat(value)
            elif rule.get("format") == "date-time":
                datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
            elif rule.get("format") == "uri":
                parsed = urlsplit(value)
                if (parsed.scheme != "https" or not parsed.hostname or parsed.username or
                        parsed.password or "\\" in value or any(ord(c) < 33 for c in value)):
                    raise ValueError("Expected absolute HTTPS URL without credentials")
                _ = parsed.port
        except ValueError:
            errors.append(f"{path}: invalid {rule.get('format')}")
    if kind in {"integer", "number"} and "minimum" in rule and value < rule["minimum"]:
        errors.append(f"{path}: must be at least {rule['minimum']}")
    return errors


def _canonical_url(url):
    parts = urlsplit(url)
    host = parts.hostname.lower()
    if parts.port and parts.port != 443:
        host += f":{parts.port}"
    return urlunsplit(("https", host, parts.path.rstrip("/") or "/", parts.query, ""))


def validate_dataset(dataset, sources, previous=None, schema=None):
    """Return all validation errors; never modify dataset, sources, or history."""
    schema = schema or load_json(ROOT / "data" / "jobs.schema.json")
    errors = _structure(dataset, schema, schema)
    if errors:
        return errors
    source_records = sources.get("sources") if isinstance(sources, dict) else sources
    if not isinstance(source_records, list) or any(not isinstance(s, dict) or
            not isinstance(s.get("id"), str) for s in source_records):
        return ["sources: expected source objects with stable id fields"]
    source_ids = {source["id"] for source in source_records}
    if len(source_ids) != len(source_records):
        errors.append("sources: duplicate source IDs")
    jobs, observations = dataset["jobs"], dataset["observations"]
    updated = dataset["updated_at"]
    if dataset["coverage_status"] == "not_started":
        if jobs or observations or updated is not None:
            errors.append("not_started requires empty jobs/history and updated_at:null")
    elif updated is None:
        errors.append("collecting/paused requires updated_at")

    def check_job(job, where):
        if job["source_id"] not in source_ids:
            errors.append(f"{where}.source_id: unknown source {job['source_id']}")
        if job["first_seen"] > job["last_seen"]:
            errors.append(f"{where}: first_seen must not follow last_seen")
        if updated and job["last_seen"] > updated:
            errors.append(f"{where}: last_seen must not follow updated_at")
        if job["posted_at"] and job["posted_at"] > job["last_seen"][:10]:
            errors.append(f"{where}: posted_at must not follow last_seen")
        salary = job["salary"]
        if salary is not None:
            low, high = salary["min"], salary["max"]
            if low is None and high is None:
                errors.append(f"{where}.salary: at least one amount is required")
            if low is not None and high is not None and low > high:
                errors.append(f"{where}.salary: min must not exceed max")

    job_ids, urls, source_keys, employers = {}, {}, {}, {}
    for index, job in enumerate(jobs):
        where = f"jobs[{index}]"
        check_job(job, where)
        if job["id"] in job_ids:
            errors.append(f"{where}: duplicate job ID {job['id']}")
        job_ids[job["id"]] = job
        url = _canonical_url(job["url"])
        if url in urls:
            errors.append(f"{where}: duplicate job URL (also {urls[url]})")
        urls[url] = job["id"]
        if job["source_job_id"]:
            key = (job["source_id"], job["source_job_id"])
            if key in source_keys:
                errors.append(f"{where}: duplicate source/job identifier (also {source_keys[key]})")
            source_keys[key] = job["id"]
        employer = job["employer"]
        if employer["id"] in employers and employers[employer["id"]] != employer:
            errors.append(f"{where}: inconsistent employer fields for {employer['id']}")
        employers[employer["id"]] = employer

    seen, first, latest, prior_time = set(), {}, {}, None
    for index, observation in enumerate(observations):
        where = f"observations[{index}]"
        job_id, observed = observation["job_id"], observation["observed_at"]
        snapshot = observation["snapshot"]
        check_job(snapshot, f"{where}.snapshot")
        if job_id not in job_ids:
            errors.append(f"{where}: unknown job_id {job_id}")
        if snapshot["id"] != job_id:
            errors.append(f"{where}: snapshot.id must match job_id")
        if snapshot["last_seen"] != observed:
            errors.append(f"{where}: snapshot.last_seen must match observed_at")
        if prior_time and observed < prior_time:
            errors.append(f"{where}: observations must be chronological")
        if (job_id, observed) in seen:
            errors.append(f"{where}: duplicate observation")
        seen.add((job_id, observed))
        first.setdefault(job_id, observed)
        if snapshot["first_seen"] != first[job_id]:
            errors.append(f"{where}: first_seen must match the first observation")
        latest[job_id] = snapshot
        prior_time = observed
    for job_id, job in job_ids.items():
        if job_id not in latest:
            errors.append(f"jobs.{job_id}: at least one observation is required")
        elif latest[job_id] != job:
            errors.append(f"jobs.{job_id}: must match its latest observation snapshot")

    if previous is not None:
        old_errors = validate_dataset(previous, sources, schema=schema)
        if old_errors:
            errors.extend(f"previous: {error}" for error in old_errors)
        else:
            old_history = previous["observations"]
            if observations[:len(old_history)] != old_history:
                errors.append("history: prior observations must be retained unchanged and in order")
            if previous["updated_at"] and (not updated or updated < previous["updated_at"]):
                errors.append("updated_at must not move backward")
            if previous["coverage_status"] != "not_started" and dataset["coverage_status"] == "not_started":
                errors.append("coverage_status must not reset to not_started")
            for old in previous["jobs"]:
                current = job_ids.get(old["id"])
                if current is None:
                    errors.append(f"history: retain job {old['id']}, including closed jobs")
                elif current["first_seen"] != old["first_seen"]:
                    errors.append(f"history: preserve first_seen for {old['id']}")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--previous", type=Path, help="Previous jobs.json to enforce history retention")
    args = parser.parse_args(argv)
    try:
        dataset = load_json(args.root / "data" / "jobs.json")
        sources = load_json(args.root / "data" / "job-sources.json")
        schema = load_json(args.root / "data" / "jobs.schema.json")
        previous = load_json(args.previous) if args.previous else None
        errors = validate_dataset(dataset, sources, previous, schema)
    except (OSError, ValueError) as error:
        errors = [str(error)]
    if errors:
        print("Jobs validation failed:\n" + "\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Jobs data valid: {len(dataset['jobs'])} records, "
          f"{len(dataset['observations'])} observations; coverage={dataset['coverage_status']}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
