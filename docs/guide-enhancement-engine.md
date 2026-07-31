# Guide Enhancement Engine

`tools/enhance_guides.py` is a conservative editorial analyzer for existing
troubleshooting guides. Version 2 does not treat a populated template as an
enhancement. It accepts a proposal only when it adds novel, issue-specific,
grounded decision value and stays within configured growth limits.

## Review workflow

Dry-run one guide first:

```sh
python tools/enhance_guides.py \
  --guide ge-b650-error-0xhost1001-internal-temperature-out-of-specification \
  --include-ccr
```

Dry-run is the default. `No enhancement recommended` is a successful result.
The report identifies existing structure and content, accepted revisions,
duplicate proposals, rejection reasons, novelty and issue-specificity metrics,
relationship strong signals, projected word growth, Related Guides UI
detection, proposed placement, and the deterministic plan digest.

A later write still requires both flags and an exact digest:

```sh
python tools/enhance_guides.py --guide <slug> \
  --write --confirm-plan <reviewed-digest>
```

Writes require a clean worktree, reject stale plans, stage deterministic output,
preserve patient-safety text, validate JSON/HTML synchronization and link
targets, run the full project validator and tests, and roll back on failure.

## Acceptance rules

Before accepting text, the analyzer normalizes punctuation, capitalization,
whitespace, and common generic terms. It measures token and phrase overlap
against the current guide. Direct duplicates, close paraphrases, title or
complaint restatements, and reorganized troubleshooting steps are rejected.

Each accepted proposal records:

- new decision-making value;
- the existing content it differs from;
- repository evidence;
- novelty and issue-specificity scores;
- diagnostic value, grounding, duplication risk, safety correctness, and
  placement quality.

Start Here requires at least three novel classification checks. Verification
must describe successful post-correction testing; it cannot confirm that the
fault remains. Error disappearance alone is explicitly insufficient for return
to service. CCR changes distinguish Complaint, Evaluation, established Cause,
Resolution, Verification, and Final status, without promoting suspected causes
to facts.

## Relationships and existing UI

Exact-model identity is not a strong signal. A troubleshooting relationship
also needs an error-code, subsystem, symptom, or failure-domain signal and must
meet the configured score and strong-signal thresholds. Corresponding PM and
Basics resources are matched separately. Self-links, duplicate targets, weak
same-model links, and missing targets are rejected.

When a page already contains `related-guides.js`, `related-guides-grid`, or a
Related Guides section, the engine does not append another generic list of
troubleshooting guides. It keeps structured relationships for review and may
show only exceptional non-guide resources when justified.

## Placement and limits

The engine prefers revising or inserting near an existing relevant area. Its
stable marker is placed before Work Order Documentation or Final Thought when a
safe structured edit is available; it is not appended after Final Thought by
default. Configuration limits maximum word growth, new sections, new bullets,
relationships, novelty, duplication, issue specificity, and relationship
strength.

Repository records still lack explicit provenance, symptom, subsystem, and
approval fields. Consequently, the analyzer remains conservative and can
legitimately recommend no change.
