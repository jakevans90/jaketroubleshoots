# Site Quality Audit Triage

## Scope and conclusion

This review validated the 5,150 findings in the original audit rather than assuming that a fired rule represented a defect. The auditor was corrected where repository evidence demonstrated duplication or false-positive behavior, and the audit was regenerated.

- Original audit: 5,150 findings (1 Critical, 2,841 High, 2,308 Medium).
- Regenerated audit: 2,826 findings (1 Critical, 2,765 High, 60 Medium).
- Net reduction from rule-quality corrections: 2,324 findings.
- Guide HTML files: 2,817.
- Registered guide records: 2,816.
- All 2,686 guides with a High finding lack a meta description. The sole Critical guide is one of those 2,686, so 2,686 guides have at least one Critical, High, or Medium finding.

No guide content, catalog, sitemap, taxonomy, CSS, or JavaScript was changed.

## Critical finding

### `html_without_json_record`

- Exact file: `guides/teleflex-autocat-drive-system-pneumatic-failure.html`
- Exact URL: `https://jaketroubleshoots.com/guides/teleflex-autocat-drive-system-pneumatic-failure.html`
- Validity: genuine.
- Evidence:
  - The HTML file exists and has that exact canonical URL.
  - The exact URL occurs once in `sitemap.xml`.
  - No record with that URL exists in any of the 91 shards registered by `data/guides.json`.
  - `data/guides-teleflex.json` contains other AutoCAT, AutoCAT 2, and AutoCAT 2 WAVE records, but not this guide.
  - The site guide listing and related-guide code load registered shards through `data/guides.json`; `related-guides.js` cannot identify the current guide when its record is absent.
- User-facing/discovery impact: the page remains directly reachable and indexable through its sitemap URL, but it is absent from JSON-driven guide listings, search/filter results, model/manufacturer discovery, and related-guide resolution. On the page itself, the related-guides component logs that the guide is not found and does not render related AutoCAT guides.
- Minimum safe correction: add one record for the existing URL to `data/guides-teleflex.json`, using manufacturer `Teleflex`, model `AutoCAT`, the existing HTML title/description, and a reviewed structural transcription of the page's steps, CCR documentation, and helpful details. Do not create another HTML page or change the canonical URL. Because the record contains substantive guide fields, a human should validate the transcription before publication.

## Current counts by exact rule ID and issue type

In this auditor, the exact rule ID is the `issue_type`.

| Rule ID / issue type | Severity | Findings | Unique affected guide files |
|---|---:|---:|---:|
| `missing_meta_description` | High | 2,686 | 2,686 |
| `title_mismatch_html_json` | High | 79 | 79 |
| `missing_required_section` | Medium | 44 | 32 |
| `missing_expected_outcome_statement` | Medium | 10 | 10 |
| `duplicate_section_heading` | Medium | 6 | 2 |
| `html_without_json_record` | Critical | 1 | 1 |
| **Total** |  | **2,826** | **2,686 guides with any Critical/High/Medium** |

Counts of guide files by severity are 1 Critical, 2,686 High, and 43 Medium. These categories overlap.

Only six finding types remain, so the “20 most frequent” list is exhausted by the six rows above.

## Representative examples

Up to ten examples are shown for every remaining rule.

### `missing_meta_description`

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

All ten have zero usable `<meta name="description">` elements. This rule is reliable and the same direct check was confirmed across the population.

### `title_mismatch_html_json`

1. `guides/3m-bair-hugger-775-series-hose-connection-damage.html` — JSON adds “to Blanket.”
2. `guides/3m-ranger-245-temperature-sensor-malfunction.html` — JSON adds “Causing Inaccurate Warming.”
3. `guides/abbott-i-stat-1-analyzer-lockout-or-qc-failures.html` — JSON uses “Blood Gas Analyzer.”
4. `guides/beckman-coulter-gem-premier-4000-5000-series-lis-network-communication-failures.html` — JSON adds “for Result Transmission.”
5. `guides/cardinal-health-kendall-scd-express-display-keypad-startup-failure.html` — HTML includes the abbreviation “(SCD).”
6. `guides/conmed-system-2450-5000-series-internal-cooling-fan-failure.html` — JSON adds “Causing Thermal Shutdown.”
7. `guides/drager-evita-v300-flow-sensor-error.html` — JSON repeats “Ventilator” in the issue phrase.
8. `guides/drager-perseus-bellows-not-cycling.html` — HTML adds “Troubleshooting Guide.”
9. `guides/enthermics-dc-series-display-control-panel.html` — JSON repeats “Blanket Warmer.”
10. `guides/enthermics-dc-series-overheat.html` — JSON repeats “Blanket Warmer.”

The rule reliably reports literal inequality but is noisy as a defect classifier. Thirty-five of the original 79 pairs are normalized containment variants, and many others differ only by device-class expansion, issue-specific discovery wording, punctuation, or a “Troubleshooting Guide” suffix. However, some findings expose material mistakes, including generic `Jake Troubleshoots` titles and CARESCAPE R850/R860 conflicts. Keep the rule as a human-review queue; do not mechanically force either side to win.

### `missing_required_section`

1. `guides/bd-alaris-air-in-line.html` — missing `Helpful Details to Include`.
2. `guides/drager-apollo-decoupling-valve-faults.html` — missing `Helpful Details to Include`.
3. `guides/exergen-tat-5000s-series-hi-lo-hi-a-or-lo-a-temperature-ambient-range-messages.html` — missing `Helpful Details to Include`.
4. `guides/ge-aisys-gas-or-agent-delivery-errors.html` — missing `Helpful Details to Include`.
5. `guides/ge-b450-pdm-not-recognized.html` — missing `What This Guide Helps With`.
6. `guides/ge-b450-pdm-not-recognized.html` — missing `Step-by-Step Troubleshooting`.
7. `guides/ge-b450-power.html` — missing `What This Guide Helps With`.
8. `guides/ge-b450-power.html` — missing `Step-by-Step Troubleshooting`.
9. `guides/ge-b450-touchscreen.html` — missing `What This Guide Helps With`.
10. `guides/ge-b450-touchscreen.html` — missing `Step-by-Step Troubleshooting`.

After accepting the established `Helpful Details to Include (If Known)` convention, this rule fell from 2,292 findings on 2,261 guides to 44 findings on 32 guides. The remaining checks are reliable as exact structural-presence checks, although a human should decide whether older page layouts are intentionally exempt.

### `missing_expected_outcome_statement`

1. `guides/3m-bair-paws-875-control-interface-or-power-switch-failure.html`
2. `guides/abbott-precision-xceed-pro-display-or-keypad-malfunction.html`
3. `guides/conmed-system-2450-5000-series-internal-cooling-fan-failure.html`
4. `guides/fujifilm-sonosite-edge-ii-probe-connector-damage-or-not-recognized.html`
5. `guides/ge-logiq-e-series-battery-not-charging.html`
6. `guides/hamilton-c1-battery.html`
7. `guides/masimo-rad-5-sensor-not-detected-low-perfusion-errors.html`
8. `guides/physio-control-lifepak-15-touchscreen.html`
9. `guides/smiths-medical-medfusion-4000-drug-library-or-configuration-corruption.html`
10. `guides/verathon-prime-plus-probe.html`

This heuristic is useful but human-review-only. The records contain instructions and often “Reason,” “Why,” observable behavior, or isolation logic, but no recognized explicit expected/verification marker. Deciding whether that is sufficient requires editorial and technical judgment; adding wording mechanically could change meaning.

### `duplicate_section_heading`

1. `guides/medtronic-valleylab-force-fx-no-output.html` — `Complaint` appears twice.
2. `guides/medtronic-valleylab-force-fx-no-output.html` — `Cause` appears twice.
3. `guides/medtronic-valleylab-force-fx-no-output.html` — `Resolution` appears twice.
4. `guides/nonin-onyx-ii-9590-display-or-button-failure.html` — `Complaint` appears twice.
5. `guides/nonin-onyx-ii-9590-display-or-button-failure.html` — `Cause` appears twice.
6. `guides/nonin-onyx-ii-9590-display-or-button-failure.html` — `Resolution` appears twice.

The counts are correct, but each guide contains two complete CCR examples, so three rule findings describe one repeated CCR block pattern per guide. This is not an auditor duplicate: the three distinct headings are each repeated. Human review should determine whether two examples are intentional before any removal.

### `html_without_json_record`

1. `guides/teleflex-autocat-drive-system-pneumatic-failure.html`

This is the genuine Critical described above.

## Rules removed or corrected after validation

| Original rule | Original count | Finding |
|---|---:|---|
| `missing_required_section` | 2,292 | 2,248 guides used the intentional heading `Helpful Details to Include (If Known)`. Alias-aware heading validation removed those false positives. |
| `meta_description_mismatch` | 47 | HTML and JSON descriptions used legitimate, complementary issue-specific wording. Exact equality was not a valid structural requirement, so the rule was removed. |
| `duplicate_manufacturer_model_issue` | 6 | Its key included the normalized title, so all six findings duplicated `duplicate_title`. The redundant rule was removed. |
| `duplicate_title` | 6 | Punctuation stripping collapsed distinct Dräger alarm priorities such as `!!` and `!!!`. Duplicate comparison now preserves punctuation; no duplicates remain. |
| `unrelated_metadata_wording` | 1 | `ED-Flow` was falsely found across the word boundary in “failed flow.” Term matching now respects alphanumeric boundaries; the narrower stale-model check remains available. |
| `placeholder_or_template_instruction` | 2 | Both hits were intentional work-order examples using `[Insert code]`, not unfinished page templates. That convention is now allowed while other explicit placeholders still fire. |
| `model_noncanonical_taxonomy_link` | 9 | The model hub contains historical/formal aliases: `Hamilton Medical`/`Hamilton`, `Dräger`/`Drager`, `VYAIRE`/`Vyaire`, `Fluoroscopy System`/`Fluoroscopy / Interventional System`, `Hemodialysis Machine`/`Hemodialysis (HD) Machine`, and `SPECT/CT System`/`SPECT / CT System`. Explicit aliases now prevent false findings without weakening unknown-value checks. |
| `wrong_manufacturer_shard` | 5 | `Senko Medical` intentionally uses the registered historical shard `data/guides-senko.json` rather than the current hub slug `senko-medical`. The explicit legacy mapping is now accepted. |

## Requested validation questions

- One guide counted multiple times for one defect: yes. The original Dräger duplicate records were reported by both `duplicate_title` and `duplicate_manufacturer_model_issue`; the second rule was wholly redundant and removed. Separately, `missing_required_section` can correctly emit multiple findings for different absent sections on one guide.
- Metadata checks comparing legitimate issue-specific wording: yes. All 47 exact meta-description mismatches were legitimate device-naming versus cause-focused variants; that exact-equality rule was removed.
- Stale-template detection on common troubleshooting language: yes. The stale-model heuristic joined normalized words and found `ED-Flow` inside “failed flow.” Boundary-aware matching fixes it. `[Insert code]` is also an intentional work-order convention.
- Intentional title formats: many are intentional expansions or concise variants. The rule remains because it also catches wrong models and generic titles, but every hit requires human review.
- Historical taxonomy names: the original check did not account for them. Explicit, reviewed aliases now cover all nine original findings.
- Paragraph-list false positives: none were emitted. A second scan using the intended `-`, `*`, `•`, and numbered-prefix patterns also found zero guides with two or more paragraph-based list markers. The current report therefore provides no evidence that this rule is producing false positives.

## Repair classification

### Mechanical without changing guide wording

- Add missing meta-description elements by copying each guide record's existing JSON `description` verbatim into the HTML head, with correct HTML escaping. This changes metadata markup but does not invent or alter wording. A scripted change should verify exactly one meta description afterward.
- Add a truly absent standard section heading only when the section content already exists immediately below an older/unlabeled container. This is safe only for the subset where no prose must be created or moved.
- Normalize purely structural markup around a confirmed duplicate heading only if the visible wording and reading order remain unchanged.

These are candidate repairs for a later content task; none were performed here.

### Human review required

- Create and validate the missing Teleflex JSON record.
- Decide which title is authoritative for each of the 79 HTML/JSON title pairs, especially generic titles and R850/R860 conflicts.
- Determine whether the 44 remaining missing sections are defects or intentional legacy layouts.
- Decide whether the ten outcome findings need new explicit outcome language.
- Decide whether the two guides with repeated CCR heading sets intentionally provide multiple examples.

## Reliability assessment

- Reliable: `html_without_json_record`, `missing_meta_description`, and the corrected required-section presence check.
- Reliable observation, noisy interpretation: `title_mismatch_html_json` and `duplicate_section_heading`.
- Heuristic/human-review-only: `missing_expected_outcome_statement`.
- Duplicative and removed: `duplicate_manufacturer_model_issue`.
- False-positive prone and corrected/removed: exact meta-description equality, punctuation-stripping title duplicates, cross-word stale-model matching, unqualified placeholder matching, exact taxonomy-link naming, legacy shard derivation, and exact-only required-heading matching.
