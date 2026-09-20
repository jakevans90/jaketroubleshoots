#!/usr/bin/env python3
"""Build compact browser indexes from the authoritative guide shards.

Card metadata and full-content search vocabulary are separate so ordinary
navigation never needs to download the troubleshooting instructions.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DISCOVERY_PATH = "data/guide-discovery.json"
SEARCH_PATH = "data/guide-search-terms.json"
INDEX_PATHS = (DISCOVERY_PATH, SEARCH_PATH)
CARD_FIELDS = ("title", "description", "assetType", "manufacturer", "model", "url", "dateAdded")


def text_values(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from text_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from text_values(child)


def search_vocabulary(record: dict[str, Any]) -> str:
    text = unicodedata.normalize("NFD", " ".join(text_values(record)))
    text = re.sub(r"[\u0300-\u036f]", "", text).lower()
    return " ".join(sorted(set(re.sub(r"[^a-z0-9]+", " ", text).split())))


def build_outputs(root: Path = ROOT, overrides: dict[str, bytes] | None = None) -> dict[str, bytes]:
    """Render indexes, optionally including a publisher's staged JSON outputs."""
    overrides = overrides or {}

    def read_json(relative: str):
        return json.loads(overrides[relative] if relative in overrides else (root / relative).read_bytes())

    manifest = read_json("data/guides.json")
    if not isinstance(manifest, list):
        raise ValueError("data/guides.json must be an array")
    records = [record for shard in manifest for record in read_json(shard)] if manifest and isinstance(manifest[0], str) else manifest
    cards, vocabulary, seen = [], {}, set()
    for record in records:
        if not isinstance(record, dict) or not all(isinstance(record.get(field), str) for field in CARD_FIELDS):
            raise ValueError("Every guide needs string card metadata")
        url = record["url"]
        if url in seen:
            raise ValueError(f"Duplicate guide URL: {url}")
        seen.add(url)
        cards.append({field: record[field] for field in CARD_FIELDS})
        vocabulary[url] = search_vocabulary(record)
    # One record per line keeps generated diffs reviewable without inflating the payload.
    compact = lambda value: json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    card_bytes = ("[\n" + ",\n".join(compact(card) for card in cards) + "\n]\n").encode("utf-8")
    search_bytes = ("{\n" + ",\n".join(compact(url) + ":" + compact(terms) for url, terms in vocabulary.items()) + "\n}\n").encode("utf-8")
    return {DISCOVERY_PATH: card_bytes, SEARCH_PATH: search_bytes}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true", help="Fail if committed browser indexes need rebuilding")
    args = parser.parse_args(argv)
    outputs = build_outputs(args.root)
    stale = []
    for relative, contents in outputs.items():
        path = args.root / relative
        if args.check:
            if not path.is_file() or path.read_bytes() != contents:
                stale.append(relative)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(contents)
        print(f"{relative}: {len(contents):,} bytes")
    if stale:
        print("Stale discovery indexes: " + ", ".join(stale))
        print("Run python tools/build_guide_discovery.py")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
