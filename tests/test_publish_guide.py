import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from publish_guide import InputError, build_plan, parse_input  # noqa: E402


class PublisherTests(unittest.TestCase):
    def fixture(self, name):
        return ROOT / "tests" / "fixtures" / name

    def test_parses_front_matter_sections_and_steps(self):
        meta, sections, steps = parse_input(self.fixture("valid-guide.md"))
        self.assertEqual(meta["model"], "Agilia")
        self.assertEqual(len(sections), 7)
        self.assertEqual([step["number"] for step in steps], ["1", "2"])
        self.assertIn("Expected outcome:", steps[0]["body"])

    def test_resolves_exact_canonical_taxonomy(self):
        meta, _, _ = parse_input(self.fixture("valid-guide.md"))
        plan = build_plan(meta)
        self.assertEqual(plan.resolved, {"assetType": "Infusion Pump", "manufacturer": "Fresenius Kabi", "model": "Agilia"})
        self.assertFalse(plan.errors)
        self.assertEqual(plan.target_shard, "data/guides-fresenius-kabi.json")

    def test_normalized_manufacturer_match_blocks_plan(self):
        meta, _, _ = parse_input(self.fixture("noncanonical-manufacturer.md"))
        plan = build_plan(meta)
        self.assertTrue(any("noncanonical" in error for error in plan.errors))
        self.assertTrue(any("normalized-name match" in warning for warning in plan.warnings))

    def test_duplicate_guide_is_blocked(self):
        meta, _, _ = parse_input(self.fixture("duplicate-guide.md"))
        plan = build_plan(meta)
        self.assertTrue(plan.duplicates)
        self.assertTrue(any("JSON URL" in match for match in plan.duplicates))
        self.assertTrue(any("duplicate resolution" in error for error in plan.errors))

    def test_rejects_duplicate_yaml_key(self):
        original = self.fixture("valid-guide.md").read_text()
        broken = original.replace("schemaVersion: 1", "schemaVersion: 1\nschemaVersion: 1")
        path = self.fixture("temporary-invalid.md")
        try:
            path.write_text(broken)
            with self.assertRaises(InputError):
                parse_input(path)
        finally:
            path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
