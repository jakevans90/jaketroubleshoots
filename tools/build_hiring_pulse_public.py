#!/usr/bin/env python3
"""Build the small public HTM Hiring Pulse snapshot and static page summary."""

from __future__ import annotations

import argparse
import html
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import htm_hiring_pulse as pulse  # noqa: E402


PUBLIC_PATH = Path("data/htm-hiring-pulse-public.json")
PAGE_PATH = Path("biomed-jobs.html")
START_MARKER = "    <!-- hiring-pulse-static:start -->"
END_MARKER = "    <!-- hiring-pulse-static:end -->"
EMPLOYER_TYPE_LABELS = {
    "health-system": "Hospital / Health System",
    "hospital": "Hospital / Health System",
    "oem": "OEM / Manufacturer",
    "iso": "ISO / HTM Provider",
    "dialysis": "Dialysis",
    "government": "Government",
    "vendor": "Vendor",
    "education": "Education",
    "other": "Other",
}


def _valid_public_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlsplit(value)
    return parsed.scheme == "https" and bool(parsed.netloc) and not parsed.username and not parsed.password


def _last_updated(store: dict[str, dict[str, Any]]) -> str | None:
    values = [
        store[name].get("updatedAt")
        for name in ("employers", "postings", "observations")
        if store[name].get("updatedAt")
    ]
    return max(values) if values else None


def build_public_snapshot(store: dict[str, dict[str, Any]]) -> dict[str, Any]:
    errors = pulse.validate_store(store)
    if errors:
        raise ValueError("Cannot build a public snapshot from invalid data:\n" + "\n".join(errors))

    employers = {item["id"]: item for item in store["employers"]["records"]}
    roles = {item["id"]: item for item in store["taxonomy"]["categories"]}
    active = [item for item in store["postings"]["records"] if item["status"] == "active"]
    public_postings: list[dict[str, Any]] = []
    ids: set[str] = set()
    urls: set[str] = set()

    for item in active:
        employer = employers.get(item["employer_id"])
        role = roles.get(item["role_category_id"])
        url = item.get("canonical_url")
        if employer is None or role is None:
            raise ValueError(f"Posting {item['id']} has an unresolved employer or role category")
        if not _valid_public_url(url):
            raise ValueError(f"Posting {item['id']} has an invalid public canonical URL")
        if item["id"] in ids or url in urls:
            raise ValueError(f"Duplicate active posting id or canonical URL: {item['id']}")
        ids.add(item["id"])
        urls.add(url)
        location = item.get("location") or {}
        public_postings.append({
            "id": item["id"],
            "title": item["title"],
            "employer": employer["name"],
            "employerId": employer["id"],
            "employerType": employer["employer_type"],
            "employerTypeLabel": EMPLOYER_TYPE_LABELS.get(employer["employer_type"], employer["employer_type"]),
            "location": location.get("text") or "Location not listed",
            "state": location.get("state"),
            "remote": bool(location.get("remote")),
            "roleCategory": role["label"],
            "roleCategoryId": role["id"],
            "salary": item.get("salary_text"),
            "postedDate": item.get("posted_date"),
            "firstObserved": item.get("first_seen"),
            "url": url,
        })

    public_postings.sort(key=lambda item: (
        item["employer"].casefold(), item["title"].casefold(), item["location"].casefold(), item["url"]
    ))
    employer_counts = Counter(item["employer"] for item in public_postings)
    employer_type_counts = Counter((item["employerType"], item["employerTypeLabel"]) for item in public_postings)
    role_counts = Counter((item["roleCategoryId"], item["roleCategory"]) for item in public_postings)
    state_counts = Counter(item["state"] for item in public_postings if item["state"])

    return {
        "schemaVersion": 1,
        "lastUpdated": _last_updated(store),
        "availability": "available" if public_postings else "unavailable",
        "methodology": {
            "label": "Observed sample",
            "description": "Current openings observed on the tracked employer career sources; not the entire HTM job market.",
        },
        "summary": {
            "activePostings": len(public_postings),
            "employersRepresented": len(employer_counts),
            "statesRepresented": len(state_counts),
            "roleCategoriesRepresented": len(role_counts),
        } if public_postings else None,
        "coverage": {
            "employers": sorted(employer_counts, key=str.casefold),
        },
        "breakdowns": {
            "roles": [
                {"id": key[0], "label": key[1], "activePostings": count}
                for key, count in sorted(role_counts.items(), key=lambda value: (-value[1], value[0][1].casefold()))
            ],
            "states": [
                {"state": state, "activePostings": count}
                for state, count in sorted(state_counts.items(), key=lambda value: (-value[1], value[0]))
            ],
            "employers": [
                {"employer": employer, "activePostings": count}
                for employer, count in sorted(employer_counts.items(), key=lambda value: (-value[1], value[0].casefold()))
            ],
            "employerTypes": [
                {"id": key[0], "label": key[1], "activePostings": count}
                for key, count in sorted(employer_type_counts.items(), key=lambda value: (-value[1], value[0][1].casefold()))
            ],
        },
        "postings": public_postings,
    }


def _list_items(items: list[dict[str, Any]], name_key: str, limit: int | None = None) -> str:
    selected = items if limit is None else items[:limit]
    return "\n".join(
        f"          <li><span>{html.escape(str(item[name_key]))}</span><strong>{item['activePostings']}</strong></li>"
        for item in selected
    )


def render_static_summary(snapshot: dict[str, Any]) -> str:
    if snapshot["availability"] != "available" or not snapshot.get("summary"):
        return "\n".join([
            START_MARKER,
            '    <div class="jobs-pulse-unavailable" role="status">',
            "      <h3>Hiring Pulse data is temporarily unavailable</h3>",
            "      <p>The job search tools, employer directory, and career resources below are still available.</p>",
            "    </div>",
            END_MARKER,
        ])

    summary = snapshot["summary"]
    employers = ", ".join(html.escape(name) for name in snapshot["coverage"]["employers"])
    last_updated = snapshot["lastUpdated"].replace("T", " ").replace("Z", " UTC") if snapshot.get("lastUpdated") else "Not available"
    role_items = _list_items(snapshot["breakdowns"]["roles"], "label")
    state_items = _list_items(snapshot["breakdowns"]["states"], "state", 10)
    employer_items = _list_items(snapshot["breakdowns"]["employers"], "employer")
    return "\n".join([
        START_MARKER,
        '    <p class="jobs-pulse-status">Live observed sample · Updated ' + html.escape(last_updated) + "</p>",
        "    <p>Explore current HTM-related openings collected from a defined set of employer career sites. Counts describe only this observed sample, not the entire HTM labor market.</p>",
        '    <div class="jobs-pulse-summary" aria-label="Hiring Pulse summary">',
        f'      <div><strong>{summary["activePostings"]}</strong><span>Active postings</span></div>',
        f'      <div><strong>{summary["employersRepresented"]}</strong><span>Employers represented</span></div>',
        f'      <div><strong>{summary["statesRepresented"]}</strong><span>States represented</span></div>',
        f'      <div><strong>{summary["roleCategoriesRepresented"]}</strong><span>Role categories</span></div>',
        "    </div>",
        '    <div class="jobs-pulse-coverage">',
        "      <h3>Current coverage</h3>",
        f"      <p><strong>Tracked employers:</strong> {employers}.</p>",
        "      <p>Openings are collected from these employer career sources, normalized, and deduplicated. Coverage is expanding across employer types and regions. A posting remains active until a complete check of its source confirms it is absent. First-observed dates are not employer-posted dates.</p>",
        "    </div>",
        '    <div class="jobs-breakdown-grid">',
        '      <section aria-labelledby="pulse-role-breakdown"><h3 id="pulse-role-breakdown">Roles in this sample</h3><ul class="jobs-count-list">',
        role_items,
        "        </ul></section>",
        '      <section aria-labelledby="pulse-state-breakdown"><h3 id="pulse-state-breakdown">Top states in this sample</h3><ul class="jobs-count-list">',
        state_items,
        "        </ul></section>",
        '      <section aria-labelledby="pulse-employer-breakdown"><h3 id="pulse-employer-breakdown">Employers in this sample</h3><ul class="jobs-count-list">',
        employer_items,
        "        </ul></section>",
        "    </div>",
        '    <p class="jobs-help">Counts reflect the current tracked sample. Coverage varies by employer, role, and geography, so these totals should not be read as market share or labor-market trends.</p>',
        END_MARKER,
    ])


def replace_static_block(page: str, rendered: str) -> str:
    start = page.find(START_MARKER)
    end = page.find(END_MARKER)
    if start < 0 or end < 0 or end < start:
        raise ValueError("Hiring Pulse static markers are missing or out of order")
    end += len(END_MARKER)
    return page[:start] + rendered + page[end:]


def render_json(value: dict[str, Any]) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def build(root: Path, check: bool = False) -> bool:
    store = pulse.load_store(root)
    snapshot = build_public_snapshot(store)
    public_path = root / PUBLIC_PATH
    page_path = root / PAGE_PATH
    page = page_path.read_text(encoding="utf-8")
    updated_page = replace_static_block(page, render_static_summary(snapshot))
    expected = {public_path: render_json(snapshot), page_path: updated_page.encode("utf-8")}
    changed = [path for path, content in expected.items() if not path.exists() or path.read_bytes() != content]
    if check:
        if changed:
            print("Out of date: " + ", ".join(str(path.relative_to(root)) for path in changed), file=sys.stderr)
            return False
        return True
    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_bytes() != content:
            path.write_bytes(content)
    print(f"Published {len(snapshot['postings'])} active Hiring Pulse postings.")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true", help="Fail when generated files are not current")
    args = parser.parse_args()
    try:
        return 0 if build(args.root.resolve(), args.check) else 1
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
