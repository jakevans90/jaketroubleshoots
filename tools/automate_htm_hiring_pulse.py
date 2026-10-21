#!/usr/bin/env python3
"""Run guarded multi-source HTM Hiring Pulse collection for automation."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))
import collect_htm_hiring_pulse as collector
import htm_hiring_pulse as pulse


THRESHOLDS_PATH = Path("data/htm-hiring-pulse/automation-config.json")


def load_thresholds(root: Path) -> dict[str, Any]:
    value = pulse.load_json(root / THRESHOLDS_PATH)
    expected = {
        "schemaVersion", "minimumBaselinePostings", "minimumSourceRetentionRatio",
        "maximumSourceGrowthMultiplier", "maximumTotalDropRatio",
        "maximumTotalGrowthMultiplier", "maximumSourceClosureRatio", "minimumSuccessfulSources",
    }
    if set(value) != expected or value.get("schemaVersion") != 1:
        raise collector.CollectionError("Invalid automation threshold configuration")
    for key in ("minimumSourceRetentionRatio", "maximumTotalDropRatio", "maximumSourceClosureRatio"):
        if not isinstance(value[key], (int, float)) or not 0 <= value[key] <= 1:
            raise collector.CollectionError(f"{key} must be between 0 and 1")
    for key in ("maximumSourceGrowthMultiplier", "maximumTotalGrowthMultiplier"):
        if not isinstance(value[key], (int, float)) or value[key] < 1:
            raise collector.CollectionError(f"{key} must be at least 1")
    for key in ("minimumBaselinePostings", "minimumSuccessfulSources"):
        if not isinstance(value[key], int) or value[key] < 1:
            raise collector.CollectionError(f"{key} must be a positive integer")
    return value


def active_by_source(store: dict[str, dict[str, Any]]) -> Counter[str]:
    return Counter(item["source"] for item in store["postings"]["records"] if item["status"] == "active")


def collect_source(source: dict[str, Any], checked_at: str, timeout: int) -> collector.CollectionResult:
    collector.ensure_robots_allowed(source, timeout)
    adapter = collector.collect_workday if source["adapter"] == "workday" else collector.collect_phenom
    return adapter(source, checked_at, timeout)


def _write_report(path: Path | None, report: dict[str, Any]) -> None:
    if path is not None:
        pulse.atomic_write(path, pulse.render_json(report))


def run_automation(
    root: Path,
    requested_sources: list[str] | None,
    checked_at: str,
    timeout: int,
    apply: bool,
    confirm_close_missing: bool,
    report_path: Path | None,
    collect: Callable[[dict[str, Any], str, int], collector.CollectionResult] = collect_source,
) -> dict[str, Any]:
    config = collector.load_config(root)
    thresholds = load_thresholds(root)
    sources = collector.selected_sources(config, requested_sources)
    original = pulse.load_store(root)
    store = copy.deepcopy(original)
    existing_counts = active_by_source(original)
    original_total = sum(existing_counts.values())
    warnings: list[str] = []
    reports: list[dict[str, Any]] = []
    successful = partial = failed = new_total = closed_total = 0
    metadata_by_id = {source["id"]: source["metadata"] for source in config["sources"]}

    for source in sources:
        source_id = source["id"]
        before_count = existing_counts[source_id]
        try:
            result = collect(source, checked_at, timeout)
        except (collector.CollectionError, ValueError, OSError) as exc:
            failed += 1
            metadata_by_id[source_id]["collectionStatus"] = "failed"
            warning = f"{source_id}: collection failed: {exc}"
            warnings.append(warning)
            reports.append({
                "source": source_id, "employer": source["employer"]["name"], "retrievedCount": 0,
                "relevantHtmCount": 0, "existingJobsRefreshed": 0, "newJobsAdded": 0,
                "jobsPotentiallyMissing": before_count, "jobsClosed": 0, "sourceStatus": "failed",
                "snapshotComplete": False, "warning": str(exc),
            })
            continue

        relevant_count = len(result.postings)
        source_status = "complete" if result.complete else "partial"
        source_warnings: list[str] = []
        baseline = thresholds["minimumBaselinePostings"]
        if before_count >= baseline and relevant_count < before_count * thresholds["minimumSourceRetentionRatio"]:
            source_status = "partial"
            source_warnings.append(f"count collapsed from {before_count} to {relevant_count}")
        if before_count >= baseline and relevant_count > before_count * thresholds["maximumSourceGrowthMultiplier"]:
            source_status = "failed"
            source_warnings.append(f"count expanded from {before_count} to {relevant_count}")

        preview = copy.deepcopy(store)
        preview_check = pulse.upsert_records(preview, result.postings, source_id, checked_at, True)
        potentially_missing = preview_check["closed_count"]
        closure_ratio = potentially_missing / before_count if before_count else 0
        if potentially_missing and closure_ratio > thresholds["maximumSourceClosureRatio"]:
            source_status = "partial"
            source_warnings.append(
                f"{potentially_missing} potential closures exceed the configured {thresholds['maximumSourceClosureRatio']:.0%} source limit"
            )

        if source_status == "failed":
            failed += 1
            metadata_by_id[source_id]["collectionStatus"] = "failed"
            warnings.extend(f"{source_id}: {message}" for message in source_warnings)
            reports.append({
                "source": source_id, "employer": source["employer"]["name"], "retrievedCount": result.scanned,
                "relevantHtmCount": relevant_count, "existingJobsRefreshed": 0, "newJobsAdded": 0,
                "jobsPotentiallyMissing": potentially_missing, "jobsClosed": 0, "sourceStatus": "failed",
                "snapshotComplete": result.complete, "warning": "; ".join(source_warnings),
            })
            continue

        may_close = bool(confirm_close_missing and result.complete and source_status == "complete")
        check = pulse.upsert_records(store, result.postings, source_id, checked_at, may_close)
        new_total += check["new_count"]
        closed_total += check["closed_count"]
        existing_refreshed = check["observed_count"] - check["new_count"] - check["reopened_count"]
        if source_status == "complete":
            successful += 1
            metadata_by_id[source_id].update({
                "lastSuccessfulCheck": checked_at,
                "lastSuccessfulPostingCount": relevant_count,
                "collectionStatus": "active",
            })
        else:
            partial += 1
            metadata_by_id[source_id]["collectionStatus"] = "partial"
            if not result.complete:
                source_warnings.append("pagination or result identity was not stable; closures disabled")
        warnings.extend(f"{source_id}: {message}" for message in source_warnings)
        reports.append({
            "source": source_id, "employer": source["employer"]["name"], "retrievedCount": result.scanned,
            "relevantHtmCount": relevant_count, "existingJobsRefreshed": existing_refreshed,
            "newJobsAdded": check["new_count"], "jobsPotentiallyMissing": potentially_missing,
            "jobsClosed": check["closed_count"], "sourceStatus": source_status,
            "snapshotComplete": result.complete, "warning": "; ".join(source_warnings) or None,
        })

    new_active_counts = active_by_source(store)
    active_total = sum(new_active_counts.values())
    global_errors: list[str] = []
    if successful + partial < thresholds["minimumSuccessfulSources"]:
        global_errors.append("too few sources completed sufficiently to publish an automated update")
    if original_total and active_total < original_total * (1 - thresholds["maximumTotalDropRatio"]):
        global_errors.append(f"active postings dropped from {original_total} to {active_total}")
    if original_total and active_total > original_total * thresholds["maximumTotalGrowthMultiplier"]:
        global_errors.append(f"active postings expanded from {original_total} to {active_total}")
    validation_errors = pulse.validate_store(store)
    global_errors.extend(validation_errors)
    employers = {item["employer_id"] for item in store["postings"]["records"] if item["status"] == "active"}
    states = {item["location"].get("state") for item in store["postings"]["records"] if item["status"] == "active" and item["location"].get("state")}
    report = {
        "schemaVersion": 1,
        "timestamp": checked_at,
        "dryRun": not apply,
        "status": "failed" if global_errors else ("warning" if warnings or failed or partial else "healthy"),
        "summary": {
            "activePostings": active_total,
            "trackedEmployers": len(employers),
            "statesRepresented": len(states),
            "newPostingsDiscovered": new_total,
            "sourcesSuccessfullyChecked": successful,
            "sourcesPartiallyChecked": partial,
            "sourcesFailed": failed,
            "postingsClosed": closed_total,
        },
        "sources": reports,
        "warnings": warnings,
        "errors": global_errors,
    }
    _write_report(report_path, report)
    if global_errors:
        raise collector.CollectionError("Automated collection failed validation:\n" + "\n".join(global_errors))

    collector.reclassify_configured_postings(store, config, checked_at)
    changed = {"employers", "postings", "observations"}
    pulse.stamp_changed(store, changed, checked_at)
    if apply:
        pulse.save_store(root, store, changed, dry_run=False)
        config_path = root / collector.CONFIG_PATH
        pulse.atomic_write(config_path, pulse.render_json(config))
    return report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=pulse.ROOT)
    parser.add_argument("--source", action="append", help="Enabled source id; repeat to limit the run")
    parser.add_argument("--checked-at", help="UTC ISO-8601 time; defaults to now")
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--apply", action="store_true", help="Write only after every global validation passes")
    parser.add_argument("--confirm-close-missing", action="store_true", help="Permit safe closures only for complete source snapshots")
    parser.add_argument("--report", type=Path, help="Health report path; written even for a dry run")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.timeout <= 0:
        raise SystemExit("--timeout must be positive")
    root = args.root.resolve()
    report = args.report
    if report is not None and not report.is_absolute():
        report = root / report
    try:
        result = run_automation(
            root, args.source, pulse.normalize_timestamp(args.checked_at), args.timeout,
            args.apply, args.confirm_close_missing, report,
        )
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (collector.CollectionError, ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
