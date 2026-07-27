# Publishing one troubleshooting guide

This document describes the repository's **current** guide-publishing pipeline. It is deliberately limited to troubleshooting guides (not preventive-maintenance articles, Biomed Basics, vendors, or a general site audit).

## What was traced

### Recent guide using existing taxonomy: Fresenius Kabi Agilia air-in-line alarm

The most recent commit at the time of this analysis (`50377fd`, 2026-07-27) added `guides/fresenius-kabi-agilia-air-in-line-alarm-or-air-detector-false-alarm.html`. Its discovery record is in `data/guides-fresenius-kabi.json`; the shard is already listed in `data/guides.json`. All three taxonomy values already existed: `Infusion Pump` in `data/hub-asset.json`, `Fresenius Kabi` in `data/hub-manufacturer.json`, and `Agilia` in `data/hub-model.json`. The URL was already added to `sitemap.xml` by the earlier sitemap commit `eb541b1`. This history shows that the present workflow can be split across commits and can temporarily expose a sitemap/JSON entry before its HTML file exists.

The JSON record contains card/discovery metadata, a flattened representation of the numbered steps, a CCR example, and the helpful-details list. The HTML contains the richer, formatted guide: lists, expected-outcome paragraphs, escalation text, clinical-use tip, CCR explanatory labels and examples, final thought, related-guides mount point, feedback block, shared scripts, and footer. Therefore the HTML and JSON are not interchangeable copies.

### New-taxonomy case: not recoverable as a recent incremental change

No recent taxonomy-creation example is available in the repository history supplied here. The only commit touching `data/hub-asset.json`, `data/hub-manufacturer.json`, or `data/hub-model.json` is the imported repository snapshot `0431400` (2026-07-22), which added essentially the whole site at once. It cannot establish whether a particular entity was created for a particular guide.

The Hamilton C6 gas-supply guide in that snapshot is still a useful end-state trace. Its guide record is in `data/guides-hamilton.json`, while `Ventilator`, `Hamilton`, and `C6` records are in the three hub registries. It also exposes a real naming hazard: the guide uses manufacturer `Hamilton`, but the C6 model profile says `Hamilton Medical`. A publisher must not infer that those strings are equivalent; it must select one canonical registry value or report the mismatch for human correction. This case must not be represented as a proven incremental taxonomy introduction.

## Current sources of truth and runtime dependencies

| Concern | Current source of truth | Consumers / consequence |
|---|---|---|
| Full page wording and formatting | `guides/<slug>.html` | The published page. This is the only copy of escalation, clinical tip, final thought, and formatted step structure. |
| Guide discovery/card data | `data/guides-<manufacturer-slug>.json` | Guide library, homepage, search, hub pages, related guides, counts, titles, badges, dates, and card descriptions. |
| Set of discovery shards | `data/guides.json` | `guides.js` and `related-guides.js` fetch only files named here. A valid shard omitted here is effectively invisible to those experiences. |
| Asset taxonomy | `data/hub-asset.json` | Asset browse/hub pages and asset icon lookup. |
| Manufacturer taxonomy | `data/hub-manufacturer.json` | Manufacturer browse/hub pages and hub links. |
| Model taxonomy and links | `data/hub-model.json` | Model browse/hub pages; each model profile links to manufacturer and asset type by display string. |
| Crawlable URL list | `sitemap.xml` | Search-engine discovery. `generate_sitemap.py` can regenerate it from every repository HTML file. |

There is no independent generated search-index file. Site search and guide/hub pages load the JSON at runtime. The homepage and guide library ultimately load the shards through `data/guides.json`; related guides locate the current record by URL and then use an **exact, case-sensitive `model` equality**. Model hubs also prefer exact equality to the hub record name. Asset icons accept exact asset name or a derived slug. These mixed rules make canonical spelling important even where one screen appears tolerant.

The hub `stats` fields currently contain placeholder values and the UI derives many counts from guide data. Publishing one guide does not presently require manually incrementing hub statistics. Likewise, `content.featuredGuides` and `pinnedModels` are optional editorial controls, not routine guide-publishing dependencies. The homepage's featured URL list is hard-coded in `index.html` and need not change unless the new guide is intentionally featured.

## Canonical HTML form

There is no template or generator file in the repository. The **de facto current template** is the newest complete guide page, `guides/fresenius-kabi-agilia-air-in-line-alarm-or-air-detector-false-alarm.html`. Copy its chrome and structure, not an older page with legacy variations.

Required page metadata/chrome:

1. `<!DOCTYPE html>`, `<html lang="en">`, and `<head>`.
2. `<title>` exactly matching the JSON `title`.
3. `../style.css`, Google Analytics, AdSense, and an absolute canonical URL of `https://jaketroubleshoots.com/guides/<slug>.html`.
4. Standard header/logo/navigation.
5. Hero: `<h2>` containing manufacturer and model; `<p>` containing the issue title.
6. Main content with Asset Type, Manufacturer, and Model values matching JSON and hub spelling.
7. Standard related-guides section and `related-guides.js`.
8. Standard feedback/suggestion section; `hub-links.js`, `feedback.js`, and `guide-icons.js`.
9. Standard footer and trained-personnel disclaimer.

Current guide-content sequence:

1. **What This Guide Helps With** (same meaning as the JSON description; current pages commonly use identical wording).
2. **Step-by-Step Troubleshooting**, with numbered `<h4>` steps. Preserve paragraph/list boundaries and explicit **Expected outcome:** language.
3. **If the Problem Persists**, including stop/escalate and return-to-service criteria.
4. **Clinical Use Tip**.
5. **Work Order Documentation (CCR Method)**, including Complaint, Cause, and Resolution explanations/examples.
6. **Helpful Details to Include (If Known)**.
7. **Final Thought**, ending with the standard successful-troubleshooting statement when supplied.

The JSON guide record requires these keys:

```json
{
  "title": "Manufacturer Model Asset Type - Issue",
  "description": "Short card/search description.",
  "assetType": "Canonical Asset Type",
  "manufacturer": "Canonical Manufacturer",
  "model": "Canonical Model",
  "url": "guides/<slug>.html",
  "dateAdded": "YYYY-MM-DD",
  "steps": [{"title": "1. ...", "instructions": "Flattened step wording ..."}],
  "documentation": {"CCR": {"Complaint": "...", "Cause": "...", "Resolution": "..."}},
  "helpfulDetails": ["..."]
}
```

`steps[].instructions` currently flattens HTML paragraphs and bullets into a single string. It must preserve the words and their order even though presentation is removed. The JSON does not currently store the escalation, clinical tip, or final-thought sections.

## Naming, filenames, and canonical capitalization

* File path and public URL are `guides/<slug>.html`, with no leading slash in JSON and an absolute site URL in the canonical tag and sitemap.
* Current slugs concatenate manufacturer, model, and issue: `<manufacturer-slug>-<model-slug>-<issue-slug>`. Use lowercase ASCII, hyphens between words, and no spaces. Retain meaningful error numbers. Do not silently “improve” an already approved explicit slug.
* Manufacturer shards use `data/guides-<manufacturer-slug>.json`; the relative shard path must appear exactly once in `data/guides.json`.
* Hub query URLs are `hub-asset.html?slug=<asset-slug>`, `hub-manufacturer.html?slug=<manufacturer-slug>`, and `hub-model.html?slug=<model-slug>`.
* `assetType`, `manufacturer`, and `model` in the guide record and HTML must copy the corresponding hub `name` **exactly**, including case, spaces, punctuation, acronyms, and brand styling. The model profile's `manufacturer` and `assetType` must do the same.
* The repository has historical exceptions (for example Hamilton/Hamilton Medical and filenames containing `+`). Do not use those exceptions as conventions; detect and report them.

## Exact current manual publishing process

1. **Start safely.** Work on `codex-edits`; confirm a clean tree. Do not publish directly to `main`.
2. **Choose canonical taxonomy before writing files.** Search all three hub registries by exact name, case-folded name, and normalized slug. Confirm the intended asset, manufacturer, and model rather than trusting free text.
3. **Resolve taxonomy.** Reuse exact `name` values when records exist. If any entity is genuinely new, add the complete record(s) described below first in memory, and ensure the model profile references the selected manufacturer and asset type.
4. **Choose title and slug.** Confirm that the HTML path, canonical URL, JSON URL, and sitemap URL do not exist and do not normalize to an existing guide.
5. **Generate HTML from the current template.** Replace title, canonical, hero, taxonomy, description, steps, escalation, clinical tip, CCR, helpful details, and final thought. Do not alter shared chrome/scripts.
6. **Create the discovery record.** Add the object to the matching manufacturer shard. Preserve supplied wording when flattening each step into `instructions`.
7. **Register a new shard only if needed.** If the manufacturer has no shard, create `data/guides-<manufacturer-slug>.json` as a JSON array and add its relative filename exactly once to `data/guides.json`. Existing manufacturers require no `data/guides.json` edit.
8. **Update the sitemap.** Prefer `python generate_sitemap.py`, then review the complete diff. It enumerates every `.html` file recursively, sorts paths, uses `/` for `index.html`, and emits no `lastmod`. Because it includes all HTML—not only guides—an unrelated untracked page would also enter the sitemap; ensure the tree is clean first. For a single guide, exactly one new `<url><loc>.../guides/<slug>.html</loc></url>` should result.
9. **Validate as one change set.** Parse every touched JSON and the sitemap XML; check cross-file equality, uniqueness, existence of each referenced file/icon, canonical equality, template sections, and that the shard is in the manifest. Load the site locally and verify guide library, search, manufacturer/asset/model hubs, related guides, and direct page navigation.
10. **Review and commit together.** Diff only the intended HTML, guide shard, any required taxonomy records/manifest entry, and sitemap. Commit them atomically. A documentation-only task such as the present one is the exception and must not touch publishing data.

## Creating and linking taxonomy records

A new **asset** record in `data/hub-asset.json` needs `type`, canonical `name`, unique `slug`, `icon`, hub `url`, `meta` (`description`, `keywords`, `lastUpdated`), `profile` (`blurb`, `commonManufacturers`, `relatedAssets`, `clinicalSetting`), `content` (`featuredGuides`, `commonIssues`, `tips`, `warnings`), `stats` (`guideCount`, `manufacturerCount`, `modelCount`), and `flags` (`exists`, `featured`, `verified`). The icon path should point to an existing asset under `images/icons-asset/`; otherwise cards silently hide the broken icon. Creating an image asset is a separate reviewed requirement, not something a guide script should fabricate.

A new **manufacturer** record in `data/hub-manufacturer.json` needs `type`, `name`, unique `slug`, hub `url`, `meta`, `profile` (blurb, founding/headquarters/site/vendor/logo/specialties fields), `content`, `stats` (`guideCount`, `modelCount`, `assetTypes`), and flags including vendor/logo flags. It also normally requires a new guide shard and `data/guides.json` manifest entry. `data/vendors.json` is not required merely to publish a guide; update it only through a separate vendor-page workflow.

A new **model** record in `data/hub-model.json` needs `type`, `name`, unique `slug`, hub `url`, `meta`, `profile` (`blurb`, canonical `manufacturer`, canonical `assetType`, `website`), `content`, `stats.guideCount`, and flags. Those profile strings are the links among model, manufacturer, and asset; there are no IDs or foreign keys. Consequently renames are migrations across guides and registries, not local edits.

## Proposed Markdown input

Use one UTF-8 Markdown file as human-reviewed input. YAML front matter holds structured values; prose remains Markdown so paragraph/list boundaries survive rendering.

```markdown
---
schemaVersion: 1
title: "Fresenius Kabi Agilia Infusion Pump - Air-in-Line Alarm or Air Detector False Alarm"
issueTitle: "Air-in-Line Alarm or Air Detector False Alarm"
description: "Troubleshooting repeated air-in-line alarms ..."
assetType: "Infusion Pump"
manufacturer: "Fresenius Kabi"
model: "Agilia"
slug: "fresenius-kabi-agilia-air-in-line-alarm-or-air-detector-false-alarm"
dateAdded: "2026-07-27"
taxonomyMode: "reuse" # reuse | create-missing
ccr:
  complaint: "Clinical staff reported ..."
  cause: "Approved administration tubing ..."
  resolution: "Removed the pump ..."
helpfulDetails:
  - "Exact alarm message recorded"
---

## What This Guide Helps With

Troubleshooting repeated air-in-line alarms ...

## Step-by-Step Troubleshooting

### 1. Ensure Patient Safety First

Do not troubleshoot ...

- Notify ...

**Expected outcome:** Patient therapy ...

## If the Problem Persists
...
## Clinical Use Tip
...
## Work Order Documentation (CCR Method)
<!-- CCR examples come from front matter; optional explanatory prose may follow. -->
## Helpful Details to Include (If Known)
<!-- rendered from front matter -->
## Final Thought
...
```

For `create-missing`, front matter should contain complete `newAsset`, `newManufacturer`, and/or `newModel` objects matching the registry schemas. The tool must never invent profiles, icons, URLs, safety claims, or canonical brand names merely because an entity is absent.

## Architecture for a single-guide publisher

A future `publish-guide` tool should be separated into pure stages:

1. **Parse:** YAML front matter plus Markdown AST; reject unknown/duplicate keys and malformed required sections.
2. **Load catalog:** all hub registries, shard manifest, guide shards, sitemap, and template/chrome.
3. **Resolve taxonomy:** exact canonical match first; normalized matches become warnings requiring explicit selection; create only complete explicitly supplied records.
4. **Plan:** derive target shard/path/URLs and an in-memory list of file edits. No disk writes.
5. **Validate:** schema, required sections, canonical equality, links, uniqueness, technical-wording preservation, rendered HTML safety, sitemap delta, and manifest reachability.
6. **Render:** deterministic HTML and deterministic pretty-printed JSON. Generate sitemap with the same path ordering as `generate_sitemap.py`.
7. **Report/diff:** show resolved entities, creations, touched files, and unified diffs.
8. **Commit writes:** write the already validated plan atomically, then re-read and validate the final tree. Git commit remains an explicit human action unless separately requested.

### Dry run

Dry run must be the default and must produce **zero filesystem changes**. It should report the target URL and shard, reused/created entities, exact files that would change, validation errors/warnings, duplicate candidates, sitemap additions, and a deterministic diff. `--write` should be refused unless the same input and catalog digest were dry-run successfully (or `--confirm-plan <digest>` is supplied), preventing a stale plan from overwriting intervening work.

### Duplicate detection

Reject exact duplicates of HTML path, canonical URL, JSON URL, guide title, or normalized slug. Also compare case-folded and punctuation/whitespace-normalized titles; manufacturer/model/issue tuples; error codes; and near-similar issue titles within the same manufacturer/model. Reject duplicate hub names, slugs, or URLs both within and across planned additions. A normalized/near match must be shown as a candidate and require an explicit override; never append automatically. Detect duplicate shard manifest entries, the same guide in multiple shards, orphan HTML, orphan JSON, mismatched canonical tags, and model-name collisions across manufacturers (the current model hub keys primarily by model name/slug, so collisions are especially dangerous).

### All-or-nothing and rollback

Take a shared lock, require a clean worktree (or limit rollback to paths the tool owns), render all outputs to a temporary directory on the same filesystem, validate them there, and only then atomically replace destinations. Before replacement, store byte-for-byte backups and file modes. If any rename or post-write validation fails, restore every destination and delete newly created files. Emit a machine-readable transaction manifest with pre/post hashes. Do not leave a guide HTML page without JSON, taxonomy, manifest, or sitemap counterparts. Git provides an additional review/revert boundary, but it is not a substitute for transaction-safe writes.

## Future batch publishing

1. Place reviewed inputs in a batch directory plus a manifest defining order and optional explicit dependencies (for example, one new manufacturer shared by ten guides).
2. Parse **all** inputs, resolve taxonomy globally, and coalesce identical proposed entities before writing anything.
3. Run cross-batch and repository duplicate checks; ensure a shared entity has one identical definition and detect model-slug collisions.
4. Produce one dry-run report with per-guide results and one aggregate diff. Any error blocks the whole batch by default; an explicit `--allow-partial` could create independent transactions, but should not be the normal publishing mode.
5. On approval, create missing taxonomy and shards once, append all guide records deterministically, regenerate the sitemap once, validate all hub/search/related dependencies, and atomically commit the complete transaction.
6. Review in a staging deployment, then make one batch commit (or explicitly planned dependency-safe commits) on `codex-edits`.

## Wording that automation must preserve exactly

The publisher may convert Markdown structure to HTML and may flatten structure for JSON, but it must not paraphrase, autocorrect, normalize punctuation inside, reorder, or silently omit supplied technical content. Preserve exactly:

* alarm/error text, codes, displayed messages, model/product/software identifiers, units, symbols (including O₂/FiO₂), limits, timings, and test values;
* every safety instruction, warning, prohibition, patient-transfer instruction, escalation/stop condition, expected outcome, return-to-service criterion, and qualification/authorization boundary;
* step order and wording, including distinctions such as “verify,” “calibrate,” “replace,” and “remove from service”;
* CCR Complaint/Cause/Resolution wording and helpful-detail labels;
* the What This Guide Helps With, If the Problem Persists, Clinical Use Tip, and Final Thought prose;
* canonical taxonomy spelling and approved title/slug/date.

Permitted mechanical transformations must be explicit and testable: Markdown headings to the prescribed heading levels, Markdown lists to `<ul>/<li>`, escaping HTML characters, and whitespace-only flattening into JSON `instructions`. The tool should compare normalized text extracted from rendered HTML and JSON against the input AST and fail if words or their order change.

## Principal failure risks

* **Partial publishing:** HTML, shard, taxonomy, manifest, and sitemap can be committed separately; runtime discovery may lead to a 404 or omit a live page.
* **Invisible data:** a new manufacturer shard not listed in `data/guides.json` is absent from guide/search/related experiences.
* **Naming drift:** exact string comparisons can detach guides from model hubs or related guides; slug fallback can conceal the defect on only some pages.
* **Duplicate identity:** no database constraints prevent duplicate titles, URLs, hub slugs, or a record copied into multiple shards.
* **Model collision:** model records are addressed by model-only slug/name rather than manufacturer-qualified identity.
* **Content divergence:** JSON step text and HTML prose are maintained separately and can disagree; extra HTML-only sections make reverse generation lossy.
* **Sitemap collateral changes:** the generator includes every HTML file in the tree, including unrelated or accidental files.
* **Broken icons/profiles:** new taxonomy objects may be syntactically valid but incomplete, point to missing icons, or link model profiles using noncanonical names.
* **Unsafe editing:** flattening lists, typographic “cleanup,” or AI rewriting can change clinically important technical or safety wording.
