#!/usr/bin/env python3
"""Build a deliberately small set of crawlable HTM job landing pages."""

from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

import build_hiring_pulse_public as public

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import generate_sitemap
BASE = "https://jaketroubleshoots.com/"
DIRECTORY = Path("htm-jobs")
MIN_LISTINGS = 8
# Explicit editorial selection prevents combinatorial/thin page generation.
PAGES = (
    ("state-texas", "HTM Jobs in Texas", {"state": "TX"}),
    ("role-imaging-service", "Imaging Service Jobs", {"roleCategoryId": "imaging-service"}),
    ("bmet-jobs-texas", "BMET Jobs in Texas", {"state": "TX", "roleCategoryId": "bmet"}),
    ("employer-trimedx", "TRIMEDX HTM Openings", {"employer": "TRIMEDX"}),
)


def matching(postings: list[dict], criteria: dict[str, str]) -> list[dict]:
    return sorted(
        (item for item in postings if item["freshness"] == "recent" and all(item.get(key) == value for key, value in criteria.items())),
        key=lambda item: (item["lastObserved"], item["title"], item["url"]),
        reverse=True,
    )


def render_page(slug: str, title: str, listings: list[dict], observed_at: str) -> bytes:
    eligible = len(listings) >= MIN_LISTINGS
    heading = html.escape(title)
    canonical = BASE + f"htm-jobs/{slug}.html"
    robots = "" if eligible else '  <meta name="robots" content="noindex,follow">\n'
    cards = "\n".join(
        '<article class="jobs-employer-card">'
        f'<span class="jobs-card-type">{html.escape(item["employer"])} · {html.escape(item["roleCategory"])}</span>'
        f'<h3><a href="{html.escape(item["url"], quote=True)}" rel="noopener">{html.escape(item["title"])}</a></h3>'
        f'<p>{html.escape(item["location"])} · Last observed {html.escape(item["lastObserved"][:10])}</p>'
        '</article>' for item in listings
    ) if eligible else '<p>There are not enough recently observed openings to make a useful listing here right now. Browse the full Hiring Pulse instead.</p>'
    description = f"Explore {title.lower()} recently observed in Jake Troubleshoots' tracked employer sample. Verify each opening on the employer career site."
    content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{heading} | Jake Troubleshoots</title>
  <meta name="description" content="{html.escape(description, quote=True)}">
{robots}  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="../style.css?v=20260920-2">
  <link rel="stylesheet" href="../jobs.css?v=20261123">
  <link rel="icon" href="../images/favicon.ico">
</head>
<body class="jobs-page">
<a class="skip-link" href="#page-heading">Skip to content</a>
<header><a href="../index.html" class="site-logo"><img src="../images/logo.png" alt="" class="site-icon"><span class="logo-text">Jake Troubleshoots</span></a>
<nav class="site-primary-nav" aria-label="Primary navigation"><a href="../guides.html">Guides</a><a href="../preventive-maintenance.html">PMs</a><a href="../biomed-basics.html">Basics</a><a href="../search.html">Search</a><a href="../biomed-jobs.html">Jobs</a></nav></header>
<main class="career-hub-main jobs-main">
  <nav class="jobs-section-nav" aria-label="Job navigation"><a href="../biomed-jobs.html">Hiring Pulse</a><a href="index.html">Browse selected job pages</a></nav>
  <section class="content-box jobs-pulse" aria-labelledby="page-heading">
    <p class="section-kicker">HTM Hiring Pulse · Observed employer sample</p>
    <h1 id="page-heading">{heading}</h1>
    <p>These are openings recently observed on tracked employer career pages, not a complete view of the job market. Confirm availability and application details with the employer.</p>
    <p class="jobs-help">Snapshot refreshed {html.escape(observed_at.replace("T", " ").replace("Z", " UTC"))}. {len(listings)} matches observed within seven days. Last observed is not the employer's posted date.</p>
    <h2>Recently observed openings</h2>
    <div class="jobs-employer-grid">{cards}</div>
  </section>
</main>
<footer><p><a href="../biomed-jobs.html">HTM Jobs &amp; Hiring Trends</a> · <a href="../privacy-policy.html">Privacy Policy</a></p><p>Guides intended for trained personnel only.</p></footer>
</body>
</html>
'''
    return content.encode("utf-8")


def render_index(links: list[tuple[str, str, int]], observed_at: str) -> bytes:
    items = "\n".join(
        f'<li><a href="{html.escape(slug)}.html">{html.escape(title)}</a> ({count} recently observed)</li>'
        for slug, title, count in links
    )
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Browse HTM Job Openings | Jake Troubleshoots</title><meta name="description" content="Selected state, role, and employer HTM job pages based on recently observed openings."><link rel="canonical" href="{BASE}htm-jobs/"><link rel="stylesheet" href="../style.css?v=20260920-2"><link rel="icon" href="../images/favicon.ico"></head><body class="jobs-page"><a class="skip-link" href="#page-heading">Skip to content</a><header><a href="../index.html" class="site-logo"><img src="../images/logo.png" alt="" class="site-icon"><span class="logo-text">Jake Troubleshoots</span></a></header><main class="career-hub-main jobs-main"><nav class="jobs-section-nav"><a href="../biomed-jobs.html">Hiring Pulse</a></nav><section class="content-box jobs-pulse"><h1 id="page-heading">Browse HTM Job Openings</h1><p>Selected pages from our observed employer sample. Counts reflect the {html.escape(observed_at[:10])} snapshot, not the entire HTM job market.</p><ul>{items}</ul><p><a href="../biomed-jobs.html">Search all tracked openings</a></p></section></main></body></html>\n'''.encode("utf-8")


def sitemap_bytes(root: Path, eligible: list[str]) -> bytes:
    return generate_sitemap.render_sitemap(root).encode("utf-8")


def build(root: Path, check: bool = False) -> bool:
    snapshot = public.pulse.load_json(root / public.PUBLIC_PATH)
    postings = snapshot["postings"]
    if snapshot.get("availability") != "available" or not all(public._valid_public_url(item.get("url")) for item in postings):
        raise ValueError("Cannot build job pages from an unavailable or invalid public snapshot")
    expected = {}
    links = []
    for slug, title, criteria in PAGES:
        matches = matching(postings, criteria)
        expected[root / DIRECTORY / f"{slug}.html"] = render_page(slug, title, matches, snapshot["lastUpdated"])
        if len(matches) >= MIN_LISTINGS:
            links.append((slug, title, len(matches)))
    expected[root / DIRECTORY / "index.html"] = render_index(links, snapshot["lastUpdated"])
    # The sitemap generator reads generated files, so write pages before it.
    if not check:
        for path, contents in expected.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            if not path.exists() or path.read_bytes() != contents:
                path.write_bytes(contents)
    expected[root / "sitemap.xml"] = sitemap_bytes(root, [slug for slug, _, _ in links])
    changed = [path for path, contents in expected.items() if not path.exists() or path.read_bytes() != contents]
    if check:
        return not changed
    for path in changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(expected[path])
    print(f"Published {len(links)} selected HTM job pages.")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        sys.exit(0 if build(args.root.resolve(), args.check) else 1)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
