# Guide discovery indexes

The authoritative guide records remain the manufacturer shards registered in
`data/guides.json`. Browser discovery uses two generated assets:

- `data/guide-discovery.json`: the existing card fields, without full instructions.
- `data/guide-search-terms.json`: a URL-keyed vocabulary of unique normalized words
  from each full record. Search loads this separately so instruction-only terms
  remain discoverable without making every listing or detail page download them.

Rebuild after manually editing a guide shard or its manifest:

```sh
python tools/build_guide_discovery.py
python tools/build_guide_discovery.py --check
```

The single-guide publisher, batch publisher, and guide-enhancement engine include
these assets in their planned, validated transaction and rollback. Their source
digests cover all input shards so stale discovery output cannot overwrite a newer
catalog. The Python test suite checks that the committed indexes match the source.

`fetchGuides()` caches one metadata request per page and preserves the existing
empty-array error result. `fetchGuides({ strict: true, search: true })` additionally
loads the vocabulary, returns records with `searchText`, and rejects on failure so
search can report an unavailable library. Failed requests can be retried. Shared
metadata records are never mutated by the search merge.

Run loader behavior tests with `node --test tests/test_guide_loader.js` and the
normal Python suite with `python -m unittest discover -s tests`.
