# HTM Hiring Pulse data foundation

HTM Hiring Pulse is intentionally separate from the public jobs page. Nothing in
`biomed-jobs.html` reads these files yet.

## Data location and versioning

The authoritative files live in `data/htm-hiring-pulse/`:

- `employers.json`
- `postings.json`
- `observations.json`
- `role-taxonomy.json`

Every file is a JSON object with `schemaVersion: 1`. Any breaking field or
meaning change requires a new schema version and a migration. Timestamps are
UTC ISO-8601 strings. Nullable fields are present with `null`; they are not
silently omitted. IDs are deterministic SHA-256-derived identifiers, so the
same normalized entity receives the same ID across runs.

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
      "descriptionSnippet": "Supports inspection, maintenance, and repair."
    }
  ]
}
```

Use the same stable source name for every check of a source. Only pass
`--complete` when the input is known to represent the source's complete current
result set.
