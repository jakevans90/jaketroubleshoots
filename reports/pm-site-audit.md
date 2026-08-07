# Preventive Maintenance Site Audit

Audit date: 2026-08-07  
Branch audited: `codex-edits` (tracking `origin/codex-edits`)  
Starting worktree: clean

## Inventory

- PM HTML pages found: **69**
- PM records in `data/preventive-maintenance.json`: **70** (**69 unique URLs**)
- PM procedure URLs indexed in `sitemap.xml`: **66** (**66 unique URLs**)
- PM pages discoverable through normal PM navigation: **69**
- PM pages with title tags: **69 of 69**
- PM pages with meta descriptions: **69 of 69**
- PM pages with standard `header`, `nav`, and `footer` elements: **69 of 69**
- PM pages with the shared `hub-links.js`, `feedback.js`, and `guide-icons.js` scripts: **69 of 69**

The PM hub loads `data/preventive-maintenance.json` and renders every unique PM page as a card. The hub also provides PM-specific text search and electrical-safety filtering.

## Confirmed Defects

### Missing sitemap entries

The following existing PM pages have no corresponding sitemap URL:

- `preventive-maintenance/tuttnauer-2540-preventive-maintenance-procedure.html`
- `preventive-maintenance/tuttnauer-3870-preventive-maintenance-procedure.html`
- `preventive-maintenance/verathon-bladderscan-i10-preventive-maintenance-procedure.html`

Recommended fix: add exactly one sitemap entry for each page.

### Duplicate PM record

`data/preventive-maintenance.json` contains two records for:

- `preventive-maintenance/philips-avalon-fm30-preventive-maintenance-procedure.html`

This makes the PM hub render the same destination twice and report 70 procedures when only 69 PM pages exist.

Recommended fix: retain the current, most recently added record and remove the older duplicate record without changing either the HTML procedure or its technical wording.

### Incorrect canonical URLs

Two page canonicals omit `-procedure` from the actual filename:

- `preventive-maintenance/ge-healthcare-mac-5-preventive-maintenance-procedure.html`
- `preventive-maintenance/ge-healthcare-mac-vu360-preventive-maintenance-procedure.html`

Recommended fix: make each canonical exactly match its published HTML URL.

### Broken relative asset links

Eight PM pages reference favicon or web-manifest files that do not exist. The repository's available standard icon is `images/favicon.ico`.

- `preventive-maintenance/ge-healthcare-mac-5500-hd-preventive-maintenance-procedure.html`
- `preventive-maintenance/mortara-eli-250-eli-210-preventive-maintenance-procedure.html`
- `preventive-maintenance/philips-avalon-fm30-preventive-maintenance-procedure.html`
- `preventive-maintenance/stryker-intouch-preventive-maintenance-procedure.html`
- `preventive-maintenance/stryker-procuity-preventive-maintenance-procedure.html`
- `preventive-maintenance/tuttnauer-2540-preventive-maintenance-procedure.html`
- `preventive-maintenance/tuttnauer-3870-preventive-maintenance-procedure.html`
- `preventive-maintenance/verathon-bladderscan-i10-preventive-maintenance-procedure.html`

Recommended fix: replace broken icon references with the existing `../images/favicon.ico` reference and remove links to the nonexistent web manifest.

## Duplicate and Orphan Checks

- Duplicate PM sitemap URLs: none
- Sitemap PM URLs without matching HTML files: none
- PM HTML pages absent from PM data/navigation: none
- PM data URLs without matching HTML files: none
- Duplicate PM records: one (Philips Avalon FM30, listed above)

## Intentional Differences

- `search.html` is explicitly a troubleshooting-guide search surface and loads troubleshooting guide shards only. PM discovery is provided by the dedicated searchable `preventive-maintenance.html` hub, so PM records are not being added to the troubleshooting search in this repair.
- PM pages consistently use the three shared discovery/navigation scripts required by their template. They do not use `related-guides.js`; the PM template uses `hub-links.js` for related hub navigation instead.
- The Siemens Healthineers CLINITEK Status+ filename spells `plus` rather than preserving the `+` character. This is a valid URL-safe slug and matches its JSON URL, canonical, and sitemap entry.
- One PM page uses an alternate valid Google advertising script URL. This does not affect PM discovery or local navigation and is outside the deterministic repair scope.

## Items Needing Review

- The two Philips Avalon FM30 records contain different approved summaries, dates, and interval phrasing. Structural repair should remove the older duplicate and retain the newer 2026-08-06 record; no interval or procedure wording should be merged or rewritten.
- Several PM pages contain visibly mis-decoded punctuation characters inherited from existing content. Because the task forbids rewriting approved PM content and technical wording, these are not changed by this structural repair.

## Recommended Repairs

1. Remove the older duplicate Philips Avalon FM30 JSON record.
2. Regenerate or update `sitemap.xml` so all 69 PM pages appear exactly once.
3. Correct the two canonical URLs to match their filenames.
4. Repair the broken favicon references and remove nonexistent manifest references on the affected PM pages.
5. Run the full tests, Python compilation, `git diff --check`, sitemap validation, and the site audit; then verify the changed-file scope before committing.

## Repair Validation Results

- Full test suite: **passed** (`60` tests)
- Python compilation checks: **passed**
- `git diff --check`: **passed**
- PM sitemap validation: **passed** (`69` pages, `69` unique PM sitemap URLs, no missing or orphan URLs, no duplicates)
- PM data/navigation validation: **passed** (`69` records, `69` unique URLs, all targets present)
- PM local-link validation: **passed** (no broken local links)
- Sitemap semantic diff: only the three missing PM URLs were added; no URLs were removed
- Repository site audit: completed; its `139` findings are pre-existing troubleshooting-guide findings outside this PM repair
- Legacy `scripts/validate_site.py`: completed but reports pre-existing Windows default-encoding failures while reading troubleshooting JSON shards; it also identified the final Mortara icon link, which was repaired before the clean PM-specific validation

No PM procedure steps, maintenance intervals, manufacturer instructions, or other technical content were changed.
