# HTM jobs: staged static data

The jobs hub stays at `biomed-jobs.html`. It uses the shared theme plus isolated
`jobs.css` and `jobs.js`. No database, API keys, scheduled collector, account, or
new production dependency is required.

## What is live in this stage

The page provides role/location searches, a filterable employer directory,
career guidance, and an explicitly unmeasured Hiring Pulse. Direct links and
the Indeed GET form work without JavaScript. JavaScript adds LinkedIn/Google
query building, employer filtering, and disclosure expansion for old anchors.
The existing analytics, advertising, social links, canonical URL, and original
20 search shortcuts are preserved.

`data/job-sources.json` records 15 employer portals and 20 existing board/search
shortcuts. Employer categories describe where to search, not verified openings.
Role tags and search terms are editorial suggestions, not evidence of vacancies.
`last_reviewed` is a source-link review date, never a posting date. The audit on
2026-09-29 confirmed official career content, not counts or individual jobs.
Search-board results could not be verified and remain `unverified`.

Edit sources in JSON, then run `python tools/build_job_sources.py --write`.
The generated employer cards and search shortcuts remain in the HTML so the directory does not
depend on a network fetch or JavaScript. Run `--check` before publishing.
When expanding employer categories, extend generator labels and page filters
together. The initial coverage omits hospitals, government, and recruiters;
the page states this explicitly.
Search-shortcut IDs use `indeed-search-`, `linkedin-search-`, or `google-search-`
prefixes to select the generated group. Extend the generator and page markup
together before introducing another board. Avoid hand-editing generated HTML.

## Individual postings, when collection begins

`data/jobs.json` intentionally starts with `coverage_status: "not_started"`,
`updated_at: null`, and empty `jobs` and `observations` arrays. It is not loaded
by the page yet. Empty here means not measured, not zero market vacancies.
Do not seed it with demonstration jobs or infer records from career links.

`data/jobs.schema.json` documents the version 1 contract:

- Stable job ID, source ID and optional employer requisition ID.
- Employer ID/name/type, exact title, normalized role and level.
- City, state, country, workplace type, and original HTTPS posting URL.
- Employer posting date if given; immutable first-seen and latest-observed UTC
  timestamps; active, closed, or unknown status.
- Optional salary range with explicit currency and period. Unknown values are
  null. Do not infer salaries, dates, remote eligibility, or locations.

Use ISO dates (`YYYY-MM-DD`) and UTC timestamps (`YYYY-MM-DDTHH:MM:SSZ`). A job
with multiple locations needs a deliberate schema extension before geographic
counts are introduced; do not silently duplicate one requisition into many jobs.
The source ID refers to an entry in `job-sources.json`. Keep source entries
after collection stops so historic references continue to resolve.

## Preserve history from the first observation

For each successful observation, append `{job_id, observed_at, snapshot}`;
`snapshot` is the full job record at that time and its `last_seen` equals the
observation time. Append in chronological order. Update the corresponding
current job record to match its latest snapshot. Keep the original `first_seen`.
Here `last_seen` means last successfully observed status, including an explicit
closure notice; it does not necessarily mean last seen open.

Retain closed jobs and old snapshots. A timeout, bot challenge, missing search
result, or failed request is not evidence of closure: do not update last_seen
or change the job to closed from that event. Record operational failures outside
this public dataset. Before importing updates, save the previous data and run:

```sh
python tools/validate_jobs.py --previous path/to/previous-jobs.json
```

The validator rejects removal or rewriting of prior history, moved first-seen
dates, unknown sources, impossible dates, reversed salary ranges, inconsistent
snapshots, duplicate IDs, exact normalized posting URLs, and repeated source
requisition IDs. It cannot identify every cross-site duplicate automatically.
Review requisition IDs, canonical URLs, and employer/location/title matches
before counting a posting. Keep one stable record for a known duplicate.

## Before publishing metrics

Add source coverage, collection freshness and known gaps, then collect and
review real postings. Define active-posting freshness rules and cross-source
deduplication first. Newly observed means first seen in a stated seven-day
window, not necessarily newly posted. Unique employers and states come from
verified current postings, not the source directory. Explain unknown/multiple
locations and staffing-company versus hiring-employer attribution.

Only publish trends after a comparable history exists (start with 30–60 days).
State the date range, included sources, coverage changes, and limitations.
Never describe this convenience sample as the entire HTM labor market.

## Verification and later migration

```sh
python tools/build_job_sources.py --check
python tools/validate_jobs.py
python -m unittest discover -s tests -p test_jobs_data.py
node --test tests/test_jobs_ui.js
```

The IDs and separate sources/jobs/observations map directly to future database
tables. Keep IDs and historical snapshots during migration; switch the read
layer after the data is trustworthy. No database choice is required now.
