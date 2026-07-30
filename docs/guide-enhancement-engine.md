# Guide Enhancement Engine

`tools/enhance_guides.py` audits existing troubleshooting guides and builds
grounded, reviewable enhancement proposals. It does not browse the web and does
not modify published content unless a reviewed plan is confirmed.

## Safe workflow

Dry-run one guide, manufacturer, or model family:

```sh
python tools/enhance_guides.py --guide ge-b650-network-instability
python tools/enhance_guides.py --manufacturer "GE Healthcare" --max-guides 5
python tools/enhance_guides.py --model "CARESCAPE B650" --max-guides 5 --include-ccr
```

The JSON report includes word counts, editorial scores, proposed sections,
duplication findings, rejected unsupported proposals, evidence, affected files,
and a SHA-256 plan digest. Scores are editorial signals, not claims of clinical
validity. Use `--report-path reports/proposal.json` for a machine-readable copy.

A write requires both flags and an exactly matching digest:

```sh
python tools/enhance_guides.py --guide ge-b650-network-instability \
  --write --confirm-plan <reviewed-digest>
```

Writes are refused on a dirty worktree. The engine re-hashes every source,
stages output, validates JSON, HTML markers, link targets, safety-language
preservation, and JSON/HTML synchronization, then runs site validation, the
test suite, Python compilation, and `git diff --check`. Any failure restores
every changed file.

## Grounding and schema

Generated statements are extracted from the selected guide and other repository
records. Failure-pattern text is always labeled with non-definitive language.
Unsupported verification text is rejected instead of invented.

Existing guide fields are unchanged. Optional `enhancements`, `relationships`,
and `enhancementMetadata` objects are added. Existing manual content is merged
first; manual and locked values are never removed. Relationships store canonical
slugs, score, reasons, source, and lock state.

HTML is inserted between `GUIDE-ENHANCEMENTS:BEGIN` and
`GUIDE-ENHANCEMENTS:END` markers immediately before `</main>`. Re-running the
engine replaces only that block, preserving page metadata, navigation,
analytics, scripts, CSS hooks, accessibility behavior, and safety wording.

Weights, minimum relationship score, and per-category/total link limits are in
`tools/guide_enhancement_config.json`.

## Current limitations

The repository’s guide JSON has no explicit symptom, subsystem, approval, or
source-provenance fields. The analyzer therefore uses conservative text
classification and reports its evidence. It will not infer manufacturer
approval, menu paths, versions, serial applicability, or internal repair steps.
Contextual in-paragraph link insertion is reported as zero in this first
implementation; only the stable Related Resources block is generated.
