# Site quality audit

`tools/audit_site.py` performs a read-only structural audit of every HTML file below
`guides/`, all guide shards registered in `data/guides.json`, the three taxonomy hub
files, and `sitemap.xml`. It does not assess technical or clinical accuracy.

## Run the audit

From the repository root:

```powershell
python tools/audit_site.py
```

This rewrites the deterministic reports at:

- `reports/site-quality-audit.json`
- `reports/site-quality-audit.md`

Use `--no-write` for a console-only run. By default, findings do not make the command
fail because the repository report is an inventory. CI can opt into a threshold:

```powershell
python tools/audit_site.py --no-write --fail-on critical
```

`--fail-on critical`, `high`, `medium`, or `low` exits with status 1 when a finding
at that severity or above exists. `--root`, `--json-output`, and `--markdown-output`
support fixtures and alternate report locations.

## Interpretation

- Critical: broken discovery, missing files, invalid JSON, or incorrect canonical routing.
- High: wrong metadata, duplicate records, taxonomy mismatches, or explicit stale
  template/placeholder content.
- Medium: repeated CCR labels, escaped comments, or missing standard sections.
- Low: formatting inconsistencies, paragraph-based list candidates, or empty elements.

The wording checks are deliberately conservative. They compare HTML against the
guide's own JSON metadata and identify explicit placeholder markers; they do not
rewrite or judge safety instructions, steps, outcomes, escalation language, CCR
examples, manufacturer claims, PM intervals, specifications, or return-to-service
criteria.

Each finding contains the issue type, file, guide title or URL, explanation,
recommended structural correction, manufacturer, and model. Summary tables aggregate
findings by issue type, severity, manufacturer, and model.

## Tests

```powershell
python -m unittest discover -s tests
python -m py_compile tools/audit_site.py tests/test_audit_site.py
```
