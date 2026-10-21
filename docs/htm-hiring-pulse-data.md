# HTM Hiring Pulse data foundation

HTM Hiring Pulse keeps its authoritative collection data separate from the
public jobs page. The page reads only the generated, privacy-minimized snapshot
at `data/htm-hiring-pulse-public.json`.

## Data location and versioning

The authoritative files live in `data/htm-hiring-pulse/`:

- `employers.json`
- `postings.json`
- `observations.json`
- `role-taxonomy.json`

Every file is a versioned JSON object. Employers, observations, and taxonomy
currently use schema version 1; postings use version 2, which added the optional
posted date. Any further breaking field or meaning change requires a new schema
version and a migration. Timestamps are UTC ISO-8601 strings. Nullable fields
are present with `null`; they are not silently omitted. IDs are deterministic
SHA-256-derived identifiers, so the same normalized entity receives the same ID
across runs.

## Stable schemas

### employers.json

The root contains `schemaVersion`, `updatedAt`, and `records`. Each employer has:

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | string | Stable `emp_` identifier derived from normalized name |
| `name` / `normalized_name` | string | Display and matching forms |
| `aliases` / `normalized_aliases` | string[] | Alternate employer names |
| `employer_type` | enum | `health-system`, `hospital`, `oem`, `iso`, `vendor`, `dialysis`, `government`, `education`, or `other` |
| `career_url` / `website_url` | string or null | Canonicalized URLs |
| `headquarters_location` | location or null | Optional structured location |
| `active` | boolean | Whether the employer remains in scope |
| `created_at` / `updated_at` | timestamp | Audit timestamps |

### postings.json

The root contains `schemaVersion`, `updatedAt`, and `records`. Each posting has:

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | string | Stable `job_` identifier |
| `employer_id` | string | Foreign key into employers |
| `title` / `normalized_title` | string | Display and matching forms |
| `role_category_id` | string | Foreign key into role taxonomy |
| `location` | location | `text`, `city`, `state`, `country`, and `remote` |
| `canonical_url` | string | URL after fragment and tracking-parameter removal |
| `source` | string | Name of the checked source |
| `source_posting_id` | string or null | Source-native job identifier |
| `employment_type`, `experience_level`, `salary_text`, `description_snippet` | string or null | Optional discovery metadata |
| `posted_date` | `YYYY-MM-DD` or null | Employer-provided posting date when available |
| `dedupe_key` | string | Hash of employer, title, location, and canonical URL |
| `first_seen` / `last_seen` | timestamp | Discovery window |
| `status` | enum | `active` or `closed` |
| `closed_at` | timestamp or null | Closure time |
| `created_at` / `updated_at` | timestamp | Audit timestamps |

Matching first uses source plus `source_posting_id`, then canonical URL, then the
full employer/title/location/URL dedupe key. URL canonicalization removes common
tracking parameters and fragments before matching.

### observations.json

The root contains `schemaVersion`, `updatedAt`, `checks`, and `records`.

Each check records its stable ID, source, `checked_at`, whether the snapshot was
complete, observed count, and counts for new, updated, unchanged, reopened, and
closed jobs. Each observation contains an ID, `check_id`, `posting_id`, source,
`observed_at`, status (`seen`, `reopened`, or `closed`), raw URL, and note.

A missing posting is closed only during `sync --complete`. Partial checks and
one-off upserts never close absent postings.

### role-taxonomy.json

The root contains `schemaVersion`, `updatedAt`, and `categories`. Each category
has `id`, `label`, `description`, and ordered `titlePatterns`. The first matching
pattern classifies a title; unmatched titles use `other-htm`. Explicit
`roleCategoryId` input always takes precedence.

## Commands

Validate all schemas, unique keys, timestamps, enums, and cross-file references:

```sh
python tools/htm_hiring_pulse.py validate
```

Add or update postings without closing anything absent from the input:

```sh
python tools/htm_hiring_pulse.py upsert --source employer-careers --input tmp/jobs.json
```

Apply a complete source snapshot and close previously active postings from that
same source when they are absent:

```sh
python tools/htm_hiring_pulse.py sync --source employer-careers --input tmp/jobs.json --complete
```

Patch one posting by stable ID:

```sh
python tools/htm_hiring_pulse.py update --id job_1234 --input tmp/posting-patch.json
```

Generate summary statistics. Output defaults to stdout; `--output` writes JSON:

```sh
python tools/htm_hiring_pulse.py summary --since-days 7
python tools/htm_hiring_pulse.py summary --since-days 7 --output reports/htm-hiring-pulse-summary.json
```

Mutation commands and summary output support `--dry-run`. A dry run performs the
full transformation and validation but writes no files.

## Operator workflow

The operator commands maintain one local source check at a time. The temporary
session is ignored by Git and does not change the four authoritative datasets
until the check is finalized.

### Partial check

Use a partial check when entering one or several jobs but not reviewing every
currently listed job from that source:

```sh
python tools/htm_hiring_pulse.py operator begin --source example-health-careers
python tools/htm_hiring_pulse.py operator add
python tools/htm_hiring_pulse.py operator status
python tools/htm_hiring_pulse.py operator finish --dry-run
python tools/htm_hiring_pulse.py operator finish
```

`operator add` displays known employers for selection and prompts for employer,
job URL, title, location, remote status, salary, and posted date. Optional values
may be left blank. It immediately reports whether the entry is new, matches an
existing posting, or replaces a duplicate already staged in the current check.
URLs, locations, role categories, and dates are normalized before staging.

Run `operator add` once per job. `operator status` can be used at any point to
review the current source and staged jobs. A dry-run performs the exact final
deduplication, observation, and validation steps without writing or clearing the
session.

### Complete source check

Only use a complete check after reviewing the entire current result set from a
single source. Begin it explicitly:

```sh
python tools/htm_hiring_pulse.py operator begin --source example-health-careers --complete-source-check
python tools/htm_hiring_pulse.py operator add
python tools/htm_hiring_pulse.py operator status
python tools/htm_hiring_pulse.py operator finish --dry-run --confirm-close-missing
python tools/htm_hiring_pulse.py operator finish --confirm-close-missing
```

Complete checks require the closure flag again at finish. Only then are active
postings from that same source marked closed when absent from the staged list.
Partial checks never close missing jobs. The finish command validates the entire
cross-linked store before any write occurs.

To abandon a staged check without changing authoritative data:

```sh
python tools/htm_hiring_pulse.py operator cancel --confirm
```

## Employer collectors

`tools/collect_htm_hiring_pulse.py` collects relevant United States HTM jobs
from enabled public employer career sites. Current coverage includes TRIMEDX,
Agiliti, GE HealthCare, DaVita, Fresenius Medical Care, Cleveland Clinic, and
Mass General Brigham. The versioned source configuration is stored in
`data/htm-hiring-pulse/collection-sources.json`. The collector uses official
public Workday feeds and supported structured Phenom results. It honors each site's
`robots.txt`, paginates every configured query, validates declared result
counts, filters by explicit HTM title patterns, and deduplicates requisitions
before using the existing Hiring Pulse ingest logic.

List the configured sources:

```sh
python tools/collect_htm_hiring_pulse.py list-sources
```

Preview every enabled source without changing authoritative data:

```sh
python tools/collect_htm_hiring_pulse.py collect
```

Preview one or more sources:

```sh
python tools/collect_htm_hiring_pulse.py collect --source trimedx-careers
python tools/collect_htm_hiring_pulse.py collect --source davita-careers --source fresenius-medical-care-careers
```

After reviewing a successful preview, write the observations without closing
any missing jobs:

```sh
python tools/collect_htm_hiring_pulse.py collect --apply
```

Only after a later run has retrieved and verified every page for each selected
source should missing jobs be eligible for closure. Closure requires a separate
explicit flag:

```sh
python tools/collect_htm_hiring_pulse.py collect --apply --confirm-close-missing
```

The command aborts before writing if any selected source is unavailable,
disallowed by `robots.txt`, malformed, exceeds its configured safety cap, or
unexpectedly produces zero relevant United States jobs. If a live source's
declared result count changes during pagination, the retrieved jobs remain
eligible for a partial update but that source is automatically marked
incomplete and cannot close missing jobs. Repeated requisitions across pages
also make a snapshot incomplete, protecting against shifting or unstable sort
orders.

Each source records its employer type, adapter, first tracked date, last
successful check, last successful posting count, automation status, and a short
limitation note. Disable a broken source by setting `enabled` to `false` and
`metadata.collectionStatus` to `disabled`; do not delete it while postings or
observations still refer to its source ID.

## Scheduled automation

`.github/workflows/htm-hiring-pulse.yml` runs at 07:17 UTC on every third
calendar day and supports manual `workflow_dispatch`. Scheduled workflows only
run after the workflow exists on GitHub's default branch; until `codex-edits`
is merged there, run the process locally.

The workflow checks out and fast-forwards `codex-edits`, runs collector and
snapshot tests, executes `tools/automate_htm_hiring_pulse.py`, rebuilds the
public snapshot, runs the full Python/JavaScript suites, rejects unexpected
changed paths, and only then commits and pushes a narrowly scoped data update.
No third-party packages or secrets are required for the current adapters.

Safety thresholds live in `data/htm-hiring-pulse/automation-config.json`. They
protect against source count collapse, implausible expansion, excessive source
closures, excessive total decline, and too few successful sources. A failed
source cannot close anything. Zero results, HTTP errors, robots denial,
malformed responses, unstable pagination, and repeated page identities produce
a failed or partial source. Successful sources may refresh while failed sources
retain their prior active postings.

Scheduled runs deliberately pass `--confirm-close-missing`, preserving the
explicit closure gate used by manual collection. Even then, jobs close only for
a complete source snapshot that passes the configured closure limit. Manual
workflow runs default to no closures unless the operator selects confirmation.

Every run uploads `reports/htm-hiring-pulse-automation.json` as a 30-day GitHub
Actions artifact. It summarizes active postings, employers, states, new jobs,
successful/partial/failed sources, closures, warnings, and per-source results.
The report is diagnostic and is not committed or exposed publicly.

Run locally without writing production data:

```sh
python tools/automate_htm_hiring_pulse.py --report reports/htm-hiring-pulse-automation.json
```

Write a validated update, then rebuild the public snapshot:

```sh
python tools/automate_htm_hiring_pulse.py --apply --report reports/htm-hiring-pulse-automation.json
python tools/build_hiring_pulse_public.py
```

Add `--confirm-close-missing` only when guarded closures are intended.

## Adding another employer adapter

Prefer an official structured feed. Confirm `robots.txt`, access constraints,
pagination, stable posting IDs, canonical URLs, location semantics, and
zero-result behavior before enabling a source. Use strict source-specific title
patterns and exclusions; generic words such as `equipment`, `engineering`, and
`technician` are not sufficient. Extend the existing taxonomy rather than
creating a second classification system.

The hospital-source review enabled Cleveland Clinic and Mass General Brigham
through allowed official Workday endpoints. Other prioritized sources remain
unconfigured for now:

- CommonSpirit, Mayo Clinic, and Kaiser Permanente disallow their search paths
  in `robots.txt`.
- HCA Healthcare returned blocked/upgrade-state access and zero public results.
- Ascension was transitioning between Phenom and Oracle career experiences;
  no stable adapter was validated.
- UPMC exposes a custom search implementation that needs a dedicated adapter.
- Johns Hopkins Medicine is crawlable but splits relevant roles across broad
  categories and has no validated structured adapter yet.
- MedStar Health uses a JavaScript/Jibe search experience that still needs a
  stable endpoint and pagination contract.
- VA/USAJobs has relevant roles, but automated API use requires approved API
  access and should not be added without that credential path.

Hospital systems often use titles such as `CE Technician` and `Clinical
Engineering Technician`. Their source rules accept those specific titles while
rejecting research, facilities, patient-care, pharmacy, and unrelated generic
technician roles. Facility-only locations remain unknown rather than inferred.

## Ingest format

Input may be an array or an object with a `postings` array:

```json
{
  "postings": [
    {
      "employer": {
        "name": "Example Health",
        "employerType": "health-system",
        "careerUrl": "https://example.org/careers"
      },
      "title": "Biomedical Equipment Technician II",
      "location": {
        "text": "Pittsburgh, PA",
        "city": "Pittsburgh",
        "state": "PA",
        "country": "US",
        "remote": false
      },
      "url": "https://example.org/jobs/123?utm_source=feed",
      "sourcePostingId": "123",
      "employmentType": "Full-time",
      "experienceLevel": "Mid-level",
      "salaryText": null,
      "postedDate": "2026-10-01",
      "descriptionSnippet": "Supports inspection, maintenance, and repair."
    }
  ]
}
```

Use the same stable source name for every check of a source. Only pass
`--complete` when the input is known to represent the source's complete current
result set.
