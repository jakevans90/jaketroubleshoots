#!/usr/bin/env python3
"""Record one reproducible Hiring Pulse summary per UTC ISO week.

The current week's entry is updated as checks arrive. Earlier weeks are frozen;
no historical values are inferred from today's postings.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import timedelta
from pathlib import Path

import build_hiring_pulse_public as public

ROOT = Path(__file__).resolve().parents[1]
HISTORY_PATH = Path("data/htm-hiring-pulse/weekly-history.json")


def week_start(timestamp: str) -> str:
    parsed = public._parse_timestamp(timestamp)
    if parsed is None:
        raise ValueError(f"Invalid weekly timestamp: {timestamp}")
    return (parsed.date() - timedelta(days=parsed.weekday())).isoformat()


def summarize(snapshot: dict, store: dict) -> dict:
    timestamp = snapshot.get("lastUpdated")
    if not timestamp or snapshot.get("availability") != "available":
        raise ValueError("A validated, available public snapshot is required")
    week = week_start(timestamp)
    postings = snapshot["postings"]
    # Count first observations even when an opening closed later in the week.
    new = [item for item in store["postings"]["records"] if item.get("first_seen") and week_start(item["first_seen"]) == week]
    employers = Counter(item["employerId"] for item in postings)
    new_employers = Counter(item["employer_id"] for item in new)
    states = Counter(item["state"] for item in postings if item.get("state"))
    roles = Counter(item["roleCategoryId"] for item in postings)
    return {
        "weekStart": week,
        "observedAt": timestamp,
        "trackedPostings": len(postings),
        "recentlyObservedPostings": sum(item["freshness"] == "recent" for item in postings),
        "agingPostings": sum(item["freshness"] == "aging" for item in postings),
        "newlyObservedPostings": len(new),
        "employersRepresented": len(employers),
        "statesRepresented": len(states),
        "employers": {key: {"tracked": employers[key], "new": new_employers[key]} for key in sorted(employers.keys() | new_employers.keys())},
        "states": dict(sorted(states.items())),
        "roles": dict(sorted(roles.items())),
    }


def update_history(history: dict, entry: dict) -> dict:
    if set(history) != {"schemaVersion", "weeks"} or history["schemaVersion"] != 1 or not isinstance(history["weeks"], list):
        raise ValueError("Invalid weekly history schema")
    weeks = history["weeks"]
    if any(not isinstance(item, dict) or item.get("weekStart") != week_start(item.get("observedAt", "")) for item in weeks):
        raise ValueError("Invalid weekly history entry")
    dates = [item["weekStart"] for item in weeks]
    if dates != sorted(set(dates)):
        raise ValueError("Weekly history must have unique, ordered weeks")
    if weeks and entry["weekStart"] < weeks[-1]["weekStart"]:
        raise ValueError("Cannot write a past week after a newer snapshot")
    if weeks and entry["weekStart"] == weeks[-1]["weekStart"]:
        if public._parse_timestamp(entry["observedAt"]) < public._parse_timestamp(weeks[-1]["observedAt"]):
            raise ValueError("Cannot replace a weekly snapshot with older data")
        weeks[-1] = entry
    else:
        weeks.append(entry)
    return history


def build(root: Path, check: bool = False) -> bool:
    snapshot = public.pulse.load_json(root / public.PUBLIC_PATH)
    store = public.pulse.load_store(root)
    if public.pulse.validate_store(store):
        raise ValueError("Hiring Pulse source records are invalid")
    entry = summarize(snapshot, store)
    path = root / HISTORY_PATH
    history = public.pulse.load_json(path) if path.exists() else {"schemaVersion": 1, "weeks": []}
    result = update_history(history, entry)
    expected = public.render_json(result)
    if check:
        return path.exists() and path.read_bytes() == expected
    if not path.exists() or path.read_bytes() != expected:
        public.pulse.atomic_write(path, expected)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        if not build(args.root.resolve(), args.check):
            print("Weekly Hiring Pulse history is out of date")
            return 1
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
