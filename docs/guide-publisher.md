# Single-guide publisher

`tools/publish_guide.py` plans and, after explicit confirmation, transactionally publishes one reviewed troubleshooting guide. The workflow and input contract in [`guide-publishing-workflow.md`](guide-publishing-workflow.md) are authoritative.

## Dry run (default)

Run the tool without `--write`:

```sh
python tools/publish_guide.py path/to/reviewed-guide.md
```

A successful dry run exits `0`, makes **zero filesystem changes**, prints every proposed path and taxonomy decision, and ends with a deterministic SHA-256 plan digest. A blocked plan exits `2`. Review all proposed changes and retain the exact digest:

```text
Status: READY
Mode: dry-run (no files written)
Plan digest: 0123456789abcdef...
```

The digest covers the input, registered guide shards, shard manifest, taxonomy catalogs, sitemap, selected canonical HTML template, and rendered outputs. Any relevant intervening change produces a different digest.

## Confirmed write

Start from a clean Git worktree, using the same input reviewed in dry run:

```sh
python tools/publish_guide.py path/to/reviewed-guide.md \
  --write \
  --confirm-plan 0123456789abcdef...
```

Both `--write` and the complete `--confirm-plan` value are required. The publisher refuses dirty worktrees, stale or incorrect digests, validation errors, warnings, normalized taxonomy matches, duplicate candidates, incomplete taxonomy proposals, and unauthorized new manufacturer shards.

Write mode renders every proposed file into a repository-local temporary directory and validates it before replacing destinations. It backs up existing bytes and modes, uses atomic replacements, re-reads and validates all results, and restores every destination if replacement or post-write validation fails. Its JSON transaction report lists created and modified files, before/after SHA-256 hashes, taxonomy decisions, the confirmed plan digest, and the sitemap addition. It never invokes `git commit`, `git push`, or merge.

## Generated change set

A successful transaction creates the guide HTML from the newest complete registered troubleshooting guide's chrome and structure, appends one discovery record to the manufacturer shard, adds the guide URL once to `sitemap.xml`, and, only when required and fully supplied:

* creates and registers a new manufacturer shard once; and
* appends complete asset, manufacturer, or model records to their taxonomy catalogs.

No unrelated content, HTML, JSON, JavaScript, CSS, images, or files are rewritten.

## Input and taxonomy rules

The UTF-8 Markdown input uses YAML front matter and the seven sections specified by the workflow. Unknown and duplicate keys are rejected. Two-space-indented mappings and scalar lists are supported; advanced YAML features are not. Steps must be consecutive `### 1. Title` headings and each must contain the exact `Expected outcome:` marker.

With `taxonomyMode: reuse`, asset, manufacturer, and model names must exactly match existing canonical names. Normalized matches block publication rather than being silently selected. With `taxonomyMode: create-missing`, every missing record must be explicitly included as `newAsset`, `newManufacturer`, or `newModel` and contain the complete top-level and nested registry schema. A new model must link the resolved canonical manufacturer and asset type. A new manufacturer shard is permitted only with a validated `newManufacturer` record.

Markdown-to-HTML conversion is mechanical: headings, paragraphs, emphasis, and lists are rendered and HTML-special characters are escaped. Supplied technical, safety, escalation, expected-outcome, return-to-service, CCR, helpful-detail, and section wording is checked against the rendered page. Step instructions in discovery JSON differ only by documented whitespace/Markdown flattening.

## Tests

Tests always create isolated temporary Git repositories; they never process or write the real guide library:

```sh
python -m unittest discover -s tests -v
```

The suite covers HTML generation, existing-shard update, new manufacturer-shard creation and registration, sitemap insertion, wording preservation, unchanged unrelated files, transaction reporting, rollback after simulated failure, dirty-worktree rejection, and incorrect/stale digest rejection.
