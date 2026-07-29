# High-Severity Repair Plan

## Scope and evidence

This is a report-only triage of the remaining High-severity findings in:

- `reports/site-quality-audit.json`
- `reports/site-quality-audit.md`
- `reports/site-quality-audit-triage.md`

No guide HTML, guide JSON, taxonomy, sitemap, CSS, JavaScript, or other site content was changed. In this auditor, the exact rule ID is the `issue_type`. Only two High-severity rule IDs remain, so the requested top-10 ranking is exhausted by the two rows below. A High severity identifies the potential impact of a finding; it does not establish that an automatic repair is safe.

## High-severity inventory and ranking

Ranked by unique affected files:

| Rank | Exact rule ID | Issue type | Findings | Unique affected files | Repair classification |
|---:|---|---|---:|---:|---|
| 1 | `missing_meta_description` | Missing HTML meta description | 2,686 | 2,686 | mechanically safe to repair, but safe only with strict validation at this scale |
| 2 | `title_mismatch_html_json` | HTML/JSON title mismatch | 79 | 79 | requires human review |
|  | **Total** |  | **2,765** | **2,686 across both rules** |  |

All 79 title-mismatch files are also among the 2,686 files missing a meta description. Therefore, the finding count must not be used as a file-touch estimate.

## Ranked rule details

### 1. `missing_meta_description`

**Evidence and status:** confirmed defect. Each of the 2,686 affected HTML files has zero usable `<meta name="description">` elements. Each has a registered JSON guide record with an existing non-empty `description` field. The deterministic repair is to copy that existing field verbatim, with HTML-attribute escaping, into exactly one meta-description element in the corresponding HTML `<head>`. It does not require generating or rewriting troubleshooting text.

**Representative examples (10):**

1. `guides/3m-bair-hugger-775-series-blower-fails-to-start.html`
2. `guides/3m-bair-hugger-775-series-control-panel-or-keypad-failure.html`
3. `guides/3m-bair-hugger-775-series-error-fc-001-internal-sensor-1-over-temperature-hose-occlusion-fault.html`
4. `guides/3m-bair-hugger-775-series-error-fc-002-hose-end-sensor-2-over-temperature-condition.html`
5. `guides/3m-bair-hugger-775-series-error-fc-003-hose-end-sensor-3-over-temperature-condition.html`
6. `guides/3m-bair-hugger-775-series-error-fc-004-internal-sensor-1-shorted.html`
7. `guides/3m-bair-hugger-775-series-error-fc-005-hose-end-sensor-2-shorted.html`
8. `guides/3m-bair-hugger-775-series-error-fc-006-hose-end-sensor-3-shorted.html`
9. `guides/3m-bair-hugger-775-series-error-fc-007-hose-end-sensor-2-open-hose-connection-fault.html`
10. `guides/3m-bair-hugger-775-series-error-fc-008-heater-blower-thermostat-failure.html`

**Impact:** the visible guide body is unaffected, but search engines have no page-supplied summary and may synthesize an inferior or misleading snippet. This weakens search-result clarity, click-through relevance, and consistent discovery messaging. At 2,686 pages, it is also a large maintenance inconsistency and makes later metadata validation less trustworthy.

**Classification:** `mechanically safe to repair` when the repair only copies the matched record's existing description. Because this is a 2,686-file change and attribute escaping or URL-to-record matching errors could propagate widely, execution is also `safe only with strict validation`. The classification does not authorize invented descriptions.

**Estimated unique guide files touched by this family:** 2,686 for the complete family. A safer first batch is the 37 affected 3M guides selected by registered JSON records whose `manufacturer` is exactly `3M` and whose corresponding HTML fires `missing_meta_description`.

### 2. `title_mismatch_html_json`

**Evidence and status:** reliable literal mismatch detection, but noisy or ambiguous defect classification. The 79 comparisons are real inequalities. Thirty-five are normalized containment variants, and many differences are device-class expansions, discovery wording, punctuation, or a `Troubleshooting Guide` suffix. Some are confirmed or likely defects, including three generic HTML titles (`Jake Troubleshoots`) and four CARESCAPE R850/R860 conflicts. The rule does not prove whether HTML or JSON is authoritative.

**Representative examples (10):**

1. `guides/3m-bair-hugger-775-series-hose-connection-damage.html` — JSON adds “to Blanket.”
2. `guides/3m-ranger-245-temperature-sensor-malfunction.html` — JSON adds “Causing Inaccurate Warming.”
3. `guides/abbott-i-stat-1-analyzer-lockout-or-qc-failures.html` — JSON expands the device class to “Blood Gas Analyzer.”
4. `guides/beckman-coulter-gem-premier-4000-5000-series-lis-network-communication-failures.html` — JSON adds discovery wording about result transmission.
5. `guides/cardinal-health-kendall-scd-express-display-keypad-startup-failure.html` — HTML adds the abbreviation `(SCD)`.
6. `guides/drager-perseus-bellows-not-cycling.html` — HTML adds `Troubleshooting Guide`.
7. `guides/enthermics-dc-series-display-control-panel.html` — JSON repeats `Blanket Warmer`.
8. `guides/ge-b450-power.html` — HTML title is the generic `Jake Troubleshoots`.
9. `guides/ge-r860-flow-sensor-error.html` — HTML names R850 while the filename and JSON record name R860.
10. `guides/stryker-s3-bed-exit-alarm.html` — HTML contains `Hopital`; JSON uses `Hospital` and a different title structure.

**Impact:** material mismatches can show an incorrect model or generic browser/search title, harm search relevance, confuse users about which device the guide covers, and cause inconsistent labels between a guide page and JSON-driven listings. Minor variants generally have negligible user impact and may be intentional SEO or readability choices. Blind synchronization could replace a good title with a redundant or less accurate one.

**Classification:** `requires human review`. A reviewed subset can become `safe only with strict validation` after an authoritative title is established from filename, canonical URL, manufacturer/model fields, page heading, guide content, and surrounding records. Containment, punctuation, device-class expansion, and suffix-only variants are `likely intentional or not worth repairing` unless a repository title convention is explicitly adopted.

**Estimated unique guide files touched by this family:** at most 79 guide HTML files, but the actual repair count should be lower after review. If JSON is authoritative for a confirmed case, only HTML `<title>` would normally change; if HTML is authoritative, the owning manufacturer shard's `title` field would change instead. Never change both merely to silence the rule.

## Shared underlying defects and rule-family touch estimates

| Rule family | Exact rule IDs | Underlying defect | Unique guide files potentially touched |
|---|---|---|---:|
| Missing page metadata | `missing_meta_description` | HTML head lacks a standard metadata element even though the matched JSON record supplies its value | 2,686 |
| Title consistency | `title_mismatch_html_json` | Two title sources differ; causes range from typos/wrong models to intentional presentation variants | up to 79 after review |
| Combined High-severity work | both rules | The 79 title files also lack meta descriptions | 2,686, not 2,765 |

The two rules do not normally fire on the same underlying defect: a missing description and a title inequality are independent. They do fire on the same 79 files, so batching by file can reduce operational overhead, but combining the repairs would mix a deterministic metadata insertion with judgment-heavy title editing. They should remain separate repair families.

## Defect-confidence separation

### Confirmed defects

- All 2,686 `missing_meta_description` findings.
- The three `title_mismatch_html_json` files whose HTML title is `Jake Troubleshoots`: `guides/ge-b450-pdm-not-recognized.html`, `guides/ge-b450-power.html`, and `guides/ge-b450-touchscreen.html`.
- The title text inequality in every mismatch finding. Whether every inequality warrants repair is a separate question.

### Likely defects

- CARESCAPE files under `ge-r860-...` whose JSON and filename name R860 but whose HTML title names R850: `guides/ge-r860-exhalation-valve-failure.html`, `guides/ge-r860-flow-sensor-error.html`, `guides/ge-r860-internal-battery-failure.html`, and `guides/ge-r860-touchscreen-freezes.html`. Confirm against the body and source material before changing a model identifier.
- Clear spelling or accidental repetition cases such as `Hopital` and repeated device-class wording. These still need a human-selected authoritative title.

### Noisy or ambiguous findings

- Added explanatory phrases such as “to Blanket,” “Causing Inaccurate Warming,” or “for Result Transmission.”
- Device-class expansions such as `Analyzer` versus `Blood Gas Analyzer`.
- Punctuation, quote-style, slash-spacing, manufacturer-prefix, and `Troubleshooting Guide` suffix differences.
- All other title mismatches until the device identity and preferred display title are reviewed.

### Known intentional repository conventions

- HTML and JSON descriptions may be complementary rather than literally identical; the former exact-description equality rule was intentionally removed.
- Concise and expanded title forms occur in the repository. Literal title mismatch is retained as a review queue, not as proof that one side should automatically overwrite the other.
- Historical taxonomy aliases and the registered `data/guides-senko.json` shard are accepted conventions and are unrelated to these High findings.
- The phrase `[Insert code]` can be an intentional work-order example. Phrase similarity and placeholder-like wording are not evidence for automatic rewriting.

## Safest first repair batch

Use a bounded pilot of the `missing_meta_description` family for the 37 affected 3M guide files. Select files from the audit, not from a filename glob alone:

1. finding severity is `High`;
2. rule ID is exactly `missing_meta_description`;
3. the file has exactly one registered JSON record by exact relative `url`;
4. that record's `manufacturer` is exactly `3M`;
5. its `description` is a non-empty string; and
6. the HTML currently has zero usable meta-description elements.

This pilot is preferable to mixing in any title repair. Once its diff and validation are clean, the same deterministic operation can be repeated shard-by-shard across the remaining 2,648 files.

### Repair contract: 3M missing meta descriptions

- **Exact rule IDs:** `missing_meta_description` only.
- **Exact files or selection criteria:** the 37 audit-listed guide HTML files meeting all six criteria above. The source records are in `data/guides-3m.json`, but that JSON file is read-only input and must not be edited.
- **Fields or markup that would change:** insert exactly one `<meta name="description" content="...">` in each selected HTML `<head>`, using the exact matched JSON `description` after correct HTML-attribute escaping. Preserve the repository's local head ordering and indentation.
- **Files that must not change:** all JSON files, all non-selected guide HTML, `data/guides.json`, taxonomy/hub files, `sitemap.xml`, CSS, JavaScript, auditor code, tests, and reports except regenerated audit outputs when deliberately requested after the content repair. No title, canonical URL, heading, body, steps, CCR, safety, escalation, or return-to-service text may change.
- **Required validation checks:** assert one-to-one exact URL matching; assert the source description is non-empty; parse each changed HTML and assert exactly one usable meta description; decode the HTML attribute and assert exact equality with the JSON value; assert title, canonical URL, visible text, scripts, and all other markup are unchanged; run the site auditor and require the selected 37 findings to disappear with no new findings; run the full test suite, Python compilation checks, the repository site validator, and `git diff --check`; inspect a representative diff containing quotes, ampersands, and non-ASCII punctuation if present.
- **Rollback risks:** a broad or incorrect selector could edit unrelated pages; faulty escaping could truncate or corrupt metadata; insertion at the wrong location could produce invalid head markup; a URL mismatch could attach one guide's description to another. Keep the pilot in one isolated commit so it can be reverted atomically.
- **Could technical or safety wording be affected?** The source description may summarize technical or safety-relevant subject matter, but copying it verbatim does not author or alter that wording. Validation must prove that no visible troubleshooting, safety, escalation, CCR, or return-to-service wording changed.

## Deferred title repair protocol

Do not include `title_mismatch_html_json` in the first automatic batch. Review one file at a time and record the authoritative source.

- **Exact rule ID:** `title_mismatch_html_json`.
- **Files:** only an explicitly reviewed subset of the 79 audit-listed files; start with the three generic `Jake Troubleshoots` titles. Treat the four R850/R860 cases as a separate technical-review batch.
- **Markup or fields:** change only the confirmed incorrect HTML `<title>` or only the confirmed incorrect JSON `title`. A visible `<h1>`, model field, URL, or body change requires separate evidence and scope.
- **Files that must not change:** canonical URLs, filenames, sitemap, taxonomy, manufacturer shard placement, descriptions, steps, safety/escalation/CCR/return-to-service wording, shared assets, and unrelated records.
- **Validation:** require agreement among filename/URL, manufacturer/model fields, visible heading, body context, and authoritative device identity; rerun the auditor and site validator; prove no URL or visible-body changes; review search-result wording manually.
- **Rollback risks:** choosing the wrong side can publish the wrong device model, reduce useful discovery wording, or spread an accidental title into JSON-driven listings.
- **Could technical or safety wording be affected?** Yes. Model identifiers and issue qualifiers are technical wording. R850/R860 and similar conflicts require human confirmation; no automatic rewrite is justified.

## Higher-risk findings outside this plan

Do not expand this High-severity repair effort into phrase-similarity cleanup, paragraph/list conversion, expected-outcome additions, section-content judgments, or edits to troubleshooting, safety, escalation, CCR, or return-to-service language. Those are not supported by the two remaining High rules and require separate human-reviewed work.

## Final recommendation

The single safest repair family to do next is `missing_meta_description`: deterministic insertion of the exact registered JSON `description` into the corresponding HTML head. The complete family affects an estimated **2,686 guide files**. Begin with the **37-file 3M pilot** defined above, validate it, and then proceed shard-by-shard.

### Proposed Codex repair prompt

> Work on the existing `codex-edits` branch. Before changing anything, confirm the branch, a clean worktree, and configured `origin`. Repair only `missing_meta_description` findings for audit-listed guide files whose exact registered JSON record has `manufacturer` equal to `3M` (expected: 37 files). For each file, insert exactly one HTML meta-description element in the `<head>` using the matched `data/guides-3m.json` record's existing non-empty `description`, with correct HTML-attribute escaping and repository-consistent formatting. Do not generate or rewrite wording. Do not change JSON, titles, canonical URLs, filenames, headings, visible body content, steps, CCR, safety, escalation, return-to-service text, taxonomy, sitemap, CSS, JavaScript, or unrelated files. Validate exact URL-to-record matching, exactly one usable meta description per changed page, decoded equality to the JSON description, and no other semantic or visible changes. Run the site auditor, repository site validator, full test suite, Python compilation checks, and `git diff --check`. Commit and attempt to push only the 37 intended HTML files and any regenerated audit reports explicitly required by the task; do not merge to `main`.
