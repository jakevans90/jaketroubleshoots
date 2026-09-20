# Jake Troubleshoots

Free biomedical equipment troubleshooting, preventive-maintenance, and Biomed
Basics resources for trained BMET, clinical engineering, and HTM personnel.

## Site architecture

The committed HTML, CSS, JavaScript, images, and JSON are the production site.
There is no application server, package-install step, or JavaScript bundle build.

- Root HTML files contain the homepage, library indexes, search, browse pages,
  vendor/contact resources, and the three query-driven hub templates.
- `guides/`, `preventive-maintenance/`, and `biomed-basics/` contain published
  articles. Their HTML is the source of truth for formatted technical content.
- `data/guides.json` registers the authoritative manufacturer guide shards.
  `data/guides-*.json` contains discovery metadata and a flattened representation
  of guide content; it does not replace the full HTML article.
- `data/hub-asset.json`, `data/hub-manufacturer.json`, and `data/hub-model.json`
  define canonical taxonomy. Other library catalogs live alongside them in `data/`.
- `style.css` provides shared styling. `guides.js` loads compact card metadata;
  `site-search.js`, `related-guides.js`, `pm-related-guides.js`, and
  `learning-recommendations.js` supply discovery and related-resource behavior.
  Root pages also contain their page-specific rendering scripts.
- `incoming-guides/` and `incoming-biomed-basics/` contain publishing inputs.
  `tools/`, `scripts/`, `tests/`, `docs/`, and `reports/` support maintenance and review.

Preserve published URLs and exact taxonomy spelling. Treat technical steps,
measurements, limits, intervals, and safety statements as reviewed content.

## Preview locally

With Python available, run from the repository root:

```sh
python tools/serve_site.py --port 8766
```

Open [the local preview](http://127.0.0.1:8766/). The preview server binds only to
localhost and disables caching so edits are visible during browser checks.

## Publish and rebuild derived output

Use the reviewed-input workflow in [the guide publishing documentation](docs/guide-publisher.md)
for single or batch guide publication. See also the
[input and content contract](docs/guide-publishing-workflow.md) and
[guide enhancement engine](docs/guide-enhancement-engine.md).

After manual changes to published pages or guide catalogs, rebuild derived files:

```sh
python tools/build_guide_discovery.py
python tools/page_chrome.py --write
python generate_sitemap.py
```

The first command generates `data/guide-discovery.json` and the separate
`data/guide-search-terms.json`; edit the source shards instead of these files.
The second maintains static viewport metadata, page headings, skip links,
section navigation, and exact taxonomy links. The sitemap includes published
root pages and the three content libraries, excluding drafts and test fixtures.

The guide publishers already include discovery output in their transactions,
apply page chrome to new guides, and update the sitemap. The enhancement engine
also refreshes discovery output. See [current browser index behavior](docs/guide-discovery-index.md)
for the generated catalog contract.

## Verify changes

Python, Node.js, and Git should be available on `PATH`; publisher tests use
temporary Git repositories. Run:

```sh
python -m unittest discover -s tests
node --test tests/test_guide_loader.js tests/test_site_search.js
python tools/build_guide_discovery.py --check
python tools/page_chrome.py --check
python scripts/validate_site.py
python tools/crawl_site.py --output reports/production-crawl.json
git diff --check
```

Inspect the crawl report for metadata, sitemap, broken-link, and fragment findings.
The crawl reads published HTML and does not execute JavaScript. Complete browser
checks at desktop and mobile widths for search, navigation, keyboard controls,
console errors, and failed requests before publishing.
