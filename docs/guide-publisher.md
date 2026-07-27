# Single-guide publisher (planning version)

`tools/publish_guide.py` parses, validates, and plans one troubleshooting guide. This first version is deliberately **dry-run only**: it has no write flag and does not render or alter guide HTML, discovery JSON, taxonomy JSON, the shard manifest, or the sitemap.

## Usage

From the repository root, run:

```sh
python tools/publish_guide.py path/to/reviewed-guide.md
```

Exit status `0` means that the plan is ready for review. Exit status `2` means publication is blocked. In either case the command writes only its report to standard output (or an input error to standard error); it does not change the repository. Run the checked-in example with:

```sh
python tools/publish_guide.py tests/fixtures/valid-guide.md
```

No external packages are required. The tool uses Python 3's standard library and a deliberately limited YAML parser, rather than accepting the whole YAML language.

## Input contract

The input must be one UTF-8 Markdown file following the **Proposed Markdown input** in [`guide-publishing-workflow.md`](guide-publishing-workflow.md). Front matter must start on the first line and be enclosed by `---` lines. It must provide:

* `schemaVersion` (currently `1`), `title`, `issueTitle`, `description`, `assetType`, `manufacturer`, `model`, `slug`, `dateAdded`, and `taxonomyMode`;
* `ccr`, containing nonempty `complaint`, `cause`, and `resolution` values; and
* a nonempty `helpfulDetails` list.

Unknown and duplicate front-matter keys are rejected. Use two-space indentation, simple scalar values, nested mappings, and scalar lists. YAML anchors, tags, multiline scalar syntax, flow collections, and other advanced YAML features are intentionally unsupported. Quoting strings is recommended, particularly when they contain punctuation.

All seven required `##` sections documented in the workflow must be present once and nonempty. Troubleshooting steps must be consecutive `### 1. Title` headings, and every step must contain the exact marker `Expected outcome:`. The parser retains the supplied Markdown and never paraphrases, autocorrects, generates, or rewrites guide content.

## Taxonomy behavior

The publisher loads the three hub registries and resolves exact `name` values first. Case, whitespace, and punctuation variations are displayed as normalized-name candidates but **block** the plan: the input must be corrected to the explicit canonical value. Unresolved and ambiguous names also block the plan.

With `taxonomyMode: reuse`, all three names must already exist. `taxonomyMode: create-missing` can identify explicitly supplied `newAsset`, `newManufacturer`, or `newModel` mappings as proposed records, but this planning version blocks them for schema review and never invents missing profile data. It also verifies an existing model's manufacturer and asset-type links.

## Catalog and duplicate checks

Every run reads:

* `data/guides.json` and every shard it registers;
* `data/hub-asset.json`, `data/hub-manufacturer.json`, and `data/hub-model.json`;
* all `data/guides-*.json` paths to identify unregistered shards; and
* `sitemap.xml` and guide HTML canonical tags.

It blocks exact title, normalized title, slug/HTML path, JSON URL, canonical URL, sitemap URL, and manufacturer/model/issue duplicates. Similar issue wording for the same normalized manufacturer and model is reported as a possible duplicate and blocks the plan. It also reports duplicate/missing shard registrations, missing taxonomy records referenced by existing guides, normalized taxonomy candidates, and unregistered shards. There is intentionally no duplicate override in this version: uncertainty must be resolved in the reviewed input or catalog before continuing.

## Reading the report

The report includes the resolved canonical taxonomy, proposed HTML path, manufacturer shard, whether the shard or taxonomy records would be new, the expected sitemap URL, and every file that a future writer would create or change. Errors, warnings, and duplicate candidates have separate sections. `READY (dry run only)` does **not** publish anything; it only means no blocker was found by this planning pass.

Example successful summary:

```text
Status: READY (dry run only)
Mode: dry-run (no files written)
Resolved canonical taxonomy:
  assetType: Infusion Pump
  manufacturer: Fresenius Kabi
  model: Agilia
Target HTML path: guides/fresenius-kabi-agilia-intermittent-keypad-backlight.html
Target manufacturer shard: data/guides-fresenius-kabi.json
New shard required: no
Expected sitemap addition: https://jaketroubleshoots.com/guides/fresenius-kabi-agilia-intermittent-keypad-backlight.html
```

## Tests and fixtures

Run the standard-library test suite with:

```sh
python -m unittest discover -s tests -v
```

Fixtures cover a valid guide, a known duplicate, and a punctuation-variant/noncanonical manufacturer. They are test inputs only and are not publication-ready additions to the live catalog.
