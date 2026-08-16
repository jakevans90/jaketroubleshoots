# Biomed Basics publishing workflow

The first version is intentionally analysis-only. It reads a reviewed Markdown draft and the existing `biomed-basics/*.html` pages, then prints a publication plan. It never creates or changes an article, landing page, sitemap, search file, patch, commit, or branch.

Run the sample dry run:

```sh
python tools/analyze_biomed_basic.py incoming-biomed-basics/new-article.md
```

The preferred input uses a small YAML-style front matter block. `title` is required. `slug` is optional and otherwise derived from the title. `description`, `category`, `badge`, `cardNote`, and `lastRevision` capture the metadata used by current article pages and landing-page cards. Use `YYYY-MM-DD` for `lastRevision`. The remainder is the reviewed article Markdown. A raw pasted draft with a leading `# Title` is also accepted for analysis; its slug and first prose paragraph are inferred, and missing card metadata is reported for later review.

The report identifies the proposed flat HTML path (`biomed-basics/<slug>.html`), the card update to `biomed-basics.html`, and the canonical sitemap entry. It also checks exact title/slug conflicts and ranks existing articles with shared topic words as candidate inbound and outbound links. Those links are suggestions for editorial review; this version does not edit them.

There is currently no Biomed Basics search index. `search.html` loads the troubleshooting-guide JSON shards registered in `data/guides.json` and describes itself as troubleshooting-guide-only. The analyzer reports that fact and does not propose unrelated guide-data changes.

## Existing site conventions found

- Biomed Basics articles are flat standalone HTML files under `biomed-basics/`.
- `biomed-basics.html` contains a hand-maintained `.guides-grid` of article cards.
- Article pages share site chrome, canonical metadata, a hero, content-box sections, the Biomed Basics backlink, and the trained-personnel footer disclaimer; there is no single source template yet.
- `generate_sitemap.py` discovers every repository HTML file and rewrites `sitemap.xml`; a future publisher should plan only the one expected URL and validate against collateral additions.
- Troubleshooting publishers default to dry run, digest the complete plan, require explicit confirmation, stage and validate outputs, replace files transactionally, roll back failures, and never commit or push. A later write-capable Biomed Basics publisher should reuse those controls and remain limited to `codex-edits` or another non-main branch.

## Deliberately deferred

HTML rendering, landing-card insertion, sitemap mutation, semantic Codex analysis, plan digests, confirmed writes, rollback, and `codex-edits` publication are deferred until the read-only report is reviewed against real article drafts.
