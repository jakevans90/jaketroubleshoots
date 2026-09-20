# Jake Troubleshoots: usability and technical audit

Completed September 20, 2026. Changes are local; no deployment or URL migration was performed.

## Architecture and preserved conventions

The production output is committed static HTML, CSS, JavaScript, images, and JSON. There is no framework build or application server. The audit covered 3,841 published HTML files: 3,583 troubleshooting guides, 112 PM procedures, 127 Basics articles, and 19 root pages. The manufacturer guide shards registered in `data/guides.json` drive discovery; formatted technical content remains in the published HTML. Shared scripts/styles and inline index/hub renderers supply navigation. Existing transactional guide publishing, rollback, taxonomy spelling, and public URLs were preserved.

Before implementation, the existing 80 Python tests passed. Local browser review covered the homepage, troubleshooting and PM detail pages, Basics articles and index, asset/manufacturer/model hubs, guide library, PM library, search, model browsing, vendors, and contact. Representative journeys included IntelliVue communication problems, SIGMA battery trouble and exact-model maintenance, ventilator self-test searches, and networking concepts.

## Prioritized findings

| Impact | Classification | Finding | Action |
| --- | --- | --- | --- |
| High | Confirmed problem | All published pages lacked mobile viewport metadata; a late CSS override forced three narrow card columns on phones. | Fixed viewport output and responsive grids; retained the existing visual identity. |
| High | Confirmed problem | Listing and related-resource scripts downloaded roughly 20.20 MB of complete guide records, including instructions; related scripts defeated caching with timestamps. | Generated a 1.62 MB metadata catalog and separate search vocabulary; cached loads and removed timestamp bypasses. |
| High | Confirmed problem | Short queries such as GE and ESU matched unrelated word fragments; accented manufacturer names and some model/symptom variants failed. Results beyond the first 24 per library were inaccessible. | Added token-aware matching, accent normalization, limited aliases, and accessible additional results. |
| High | Confirmed problem | The guide library initially constructed all 3,583 cards. | Render 60 initially, with incremental results and the same search rules as site search. |
| High | Confirmed problem | There were no H1 page headings or skip links; browse letters were nonsemantic spans. | Promoted existing page-title text, added skip links, repaired landmarks, and used keyboard-operable buttons. |
| Medium | Confirmed problem | robots.txt advertised a missing sitemap; 31 PM pages contained 124 broken favicon references; three B450 titles were generic and nine ordinary pages lacked descriptions. | Corrected the actual output and added scoped sitemap/crawl validation. |
| Medium | Confirmed problem | Existing taxonomy labels and model counts did not consistently provide direct navigation. | Added exact taxonomy links and links to existing troubleshooting/PM sections. |
| Medium | Reasonable improvement | Long procedures could benefit from a concise section navigator. | Added a collapsed native “On this page” control built from existing headings, avoiding pages that already have a section navigator. |
| Medium | Confirmed architecture limitation | Most inbound discovery links are rendered by JavaScript; query-driven hub templates share parameterless canonical URLs. | Documented for a dedicated architecture pass; no speculative canonical migration. |
| Medium | Confirmed data limitation | Seventy existing guide records lack their required `steps` metadata. | Documented; did not invent biomedical instructions. |
| Low | Subjective idea | A broad visual redesign, new branding, or larger promotional sections. | Deliberately not implemented. |

## Changes and benefits

### Search and performance

- Browser listings, hubs, and related-resource panels use `data/guide-discovery.json`. Its 1,620,058 bytes replace 20,201,559 bytes of guide-shard downloads: **92.0% fewer guide-data bytes** for those consumers. This excludes other page assets and HTTP compression.
- Site search and guide-library filtering also load a 6,985,838-byte vocabulary derived from all guide fields. Their combined guide data is 8,605,896 bytes, **57.4% less** than the old shards, while retaining instruction-only terms. The full instruction records remain unchanged.
- Catalog loading shares in-flight requests, supports retry after failure, and does not mutate cached metadata when adding search text. Search preserves the other libraries if one fails and reports the unavailable library.
- Search normalizes records once, debounces input, caches query results, supports partial/spaced/joined models, folds accents, and treats short biomedical abbreviations as tokens. Negation remains required but carries less ranking weight than the actual symptom, so incidental “not” wording does not outrank communication guides. Limited explicit typo suggestions avoid silently substituting exact model or error identifiers.
- Site search reveals 24 more results per group; the grouped guide library starts at 60 and reveals 60 more. Counts, loading/error messages, and focus movement make additional results discoverable.
- Guide-library filters reuse the same matcher, avoiding contradictory ESU results between search and the library. Existing asset/manufacturer/model grouping remains.
- Guide, batch, and enhancement publishing transactions include generated discovery assets, source digests, and rollback, so new content does not leave the browser catalog stale.

### Navigation, accessibility, and mobile use

- Added language/encoding metadata where absent, viewport tags, existing-title H1s, keyboard skip links, and reliable main landmarks. Hero wording and appearance remain intact.
- Added visible focus styling, named feedback controls, native A–Z filter buttons with state, and larger mobile navigation targets. Homepage search now has a native GET form.
- Converted existing exact-match asset/manufacturer/model values into static hub links. Existing browse choices have real destinations that support modified clicks; model count links lead to the relevant troubleshooting or PM section.
- Restricted same-model related troubleshooting matches to the same manufacturer, preventing identically named equipment from being mixed.
- Added collapsible section navigation derived from existing headings on long detail pages, with focused targets and sticky-header clearance. Existing Basics section navigators were retained.
- Repaired one/two/three-column collection breakpoints, mobile search controls, related-card minimum widths, and model tips/warnings overflow. Reduced-motion preferences disable movement.
- Most detail pages with complete static taxonomy links no longer need the extra taxonomy lookup requests. No generic link blocks were added.

### SEO and maintainability

- Corrected the sitemap declaration, 124 broken favicon references, three generic titles, and nine missing descriptions using existing content.
- Restricted sitemap generation and validation to published output, excluding drafts and fixtures. All 3,841 existing published URLs remain covered.
- Added a repeatable raw-HTML crawl for links, fragments, titles, H1s, metadata, canonicals, robots directives, and sitemap coverage. Fixed platform-dependent UTF-8 validation.
- Added an idempotent page-chrome tool and integrated it with guide/Basics publication. Updated heading-dependent analysis/enhancement helpers to accept the resulting markup.
- Versioned changed shared assets to avoid stale CSS/JavaScript after publication. Added a localhost preview server that disables browser caching and documented the architecture and commands in the README.

## Verification and measurements

- Baseline: **80 Python tests passed**. Final: **94 Python tests and 17 Node tests passed**. Coverage includes publishing transactions/rollback, generated asset freshness, page-chrome idempotency and text preservation, sitemap scope, crawl defects, search relevance, acronyms, joined models, negation, exact PM lookup, and failure recovery.
- Rebuilt discovery output and sitemap; discovery freshness and page-chrome checks passed. The committed HTML is the production build output; no nonexistent npm build was substituted. JavaScript syntax checks and `git diff --check` passed.
- Crawled **3,841 published pages**. Final output has **zero broken local file links, duplicate titles, missing viewport tags, malformed canonical reports, unexpected noindex reports, or sitemap coverage defects**.
- The one page without an H1/description is the pre-existing instant redirect `ge-mac-vu360-leads-noisy-ecg.html`. It was left as a redirect.
- Eight raw fragment reports reference six Basics category sections inserted by JavaScript. Every destination ID was verified in the rendered browser. They remain evidence of dependence on JavaScript, not broken rendered navigation.
- The legacy validator improved from **272 to 148 errors**: all 124 removed errors were broken favicon references. Remaining errors are the same 140 reports from 70 missing-step records plus the eight dynamic fragment reports. Its 3,595 warnings are unchanged. This validator is not claimed to pass.
- Compared normalized visible body text against HEAD for **all 3,822 detail pages**, excluding only new skip/section navigation and non-visible markup. **Zero technical body-text changes** were found; see `content-preservation.json`.
- Browser checks covered all listed page families at desktop and 390-pixel phone widths, with additional homepage/search/library/model/PM/Basics checks at 320, 768, and 1440 pixels. Final checked layouts had no horizontal document overflow. Console warning/error checks were empty, and checked images loaded. These were viewport simulations, not physical-device testing or a WCAG certification.
- Confirmed keyboard skip-to-heading, expandable section navigation and focused destinations, model-to-PM links, search filters, 24→48 search results, 60→120 library results, and ESU consistency. Browser results for ESU now show 75 troubleshooting guides and three PMs, excluding the unrelated resume article.
- At a 390-pixel viewport, a representative search card changed from about **101 pixels wide / 1,185 pixels tall** in the forced three-column layout to **303 pixels wide / approximately 394–418 pixels tall** in one column.
- Local ranking-only measurements improved in eight representative queries. Examples: GE **389→37 ms**, ESU **259→22 ms**, IntelliVue communication **177→52 ms**. These are medians of three runs, comparing baseline scoring and final scoring in the same Node process. The current index is built before timing; network, DOM work, and index construction are excluded. These are not production Core Web Vitals claims. See `search-benchmark.json`.

The before-crawl artifact was captured after the robots-only correction; the original robots defect is confirmed independently in the Git diff. Crawl reports count only static inbound anchors: the remaining 3,703 pages without such an anchor are not asserted to be actual orphaned pages.

## Deliberately unchanged

- Biomedical troubleshooting steps, maintenance requirements, measurements, intervals, electrical-safety values, and clinical statements. No independent clinical validation was attempted.
- Existing URLs, branding, colorful hero artwork, dense technical content, and the Troubleshoot/Maintain/Understand structure.
- Historical model/manufacturer aliases and uncertain PM-only model identities. Automatic normalization could attach procedures to the wrong equipment.
- Query-hub canonical strategy, structured data, and a full static-generation migration. These need their own URL/identity model and evidence, not a broad SEO guess.
- External vendor/contact destinations were inspected as resources; this pass does not certify every external contact or manufacturer document as current.

## Next best opportunities

1. **Generate useful static discovery pages and stable hub identities.** Address JavaScript-dependent internal linking and query-hub canonicals together, preserving established URLs and testing exact model relationships.
2. **Reconcile technical metadata against reviewed source content.** Repair the 70 missing-step records and review the Skytron Elite 6500 and Mortara ELI 250 / ELI 210 PM-only hub identities without inventing content.
3. **Curate symptom-specific learning recommendations.** Existing related Basics links are often category-driven; networking, battery, and self-test concepts could be more precisely related after editorial review.
4. **Measure deployed performance.** Check compressed transfer sizes, cache headers, LCP/CLS, and real mobile search latency. The remaining search vocabulary is still substantial and is a candidate for a smaller inverted index or worker if field measurements justify it.

Evidence: `production-crawl-before.json`, `production-crawl-after.json`, `validator-baseline.txt`, `validator-after.txt`, `content-preservation.json`, and `search-benchmark.json` in this directory.
