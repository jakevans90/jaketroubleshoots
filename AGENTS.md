# Jake Troubleshoots repository instructions

## Required publishing finalization

Apply this workflow whenever published site content is added, removed, or changed, including troubleshooting guides, preventive-maintenance procedures, and Biomed Basics articles.

1. Work on `codex-edits` or another non-`main` branch. Never publish directly to `main`.
2. Immediately before final generation, synchronize with the latest remote branch. Reconcile any incoming changes before continuing so generated files do not overwrite another session's work.
3. Complete the normal content-specific publishing workflow and validations.
4. Run `python tools/build_content_directory.py` to regenerate the static content directory.
5. If any troubleshooting guide was added, removed, or modified, run `python tools/build_guide_discovery.py` to regenerate guide discovery data.
6. Run `python generate_sitemap.py` to regenerate `sitemap.xml`.
7. Confirm each newly published page is present in its expected generated directory page and appears exactly once in `sitemap.xml`.
8. Run the relevant content-specific validation tests plus the content-directory and sitemap tests.
9. Review the diff and include all regenerated files in the same publishing commit.

Do not manually edit `content-directory.html`, files under `directory/`, guide discovery outputs, or `sitemap.xml`. Change their authoritative source data and rerun the appropriate generator. Do not modify or commit unrelated content.
