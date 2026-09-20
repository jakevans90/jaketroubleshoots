import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_guide_discovery import CARD_FIELDS, DISCOVERY_PATH, SEARCH_PATH, build_outputs, search_vocabulary


class GuideDiscoveryTests(unittest.TestCase):
    def test_committed_indexes_match_every_authoritative_record(self):
        for relative, expected in build_outputs(ROOT).items():
            with self.subTest(index=relative):
                self.assertEqual((ROOT / relative).read_bytes(), expected,
                                 "Run python tools/build_guide_discovery.py after changing guide metadata")

    def test_vocabulary_preserves_instruction_only_words_and_normalizes_diacritics(self):
        record = {"title": "Café Monitor", "steps": [{"instructions": "NIBP ERR-42, café; NIBP."}]}
        self.assertEqual(search_vocabulary(record), "42 cafe err monitor nibp")

    def test_staged_shard_and_manifest_are_included_without_modifying_source(self):
        record = {field: field for field in CARD_FIELDS}
        record["steps"] = [{"instructions": "PACS communication retry"}]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            (root / "data/guides.json").write_text("[]", encoding="utf-8")
            staged = {
                "data/guides.json": b'["data/guides-example.json"]',
                "data/guides-example.json": json.dumps([record]).encode(),
            }
            output = build_outputs(root, staged)
            self.assertEqual(json.loads(output[DISCOVERY_PATH]), [{field: record[field] for field in CARD_FIELDS}])
            self.assertIn("pacs", json.loads(output[SEARCH_PATH])[record["url"]].split())
            self.assertEqual((root / "data/guides.json").read_text(), "[]")
            self.assertFalse((root / "data/guides-example.json").exists())

    def test_duplicate_urls_are_rejected(self):
        record = {field: field for field in CARD_FIELDS}
        with self.assertRaisesRegex(ValueError, "Duplicate guide URL"):
            build_outputs(ROOT, {"data/guides.json": json.dumps([record, record]).encode()})


if __name__ == "__main__":
    unittest.main()
