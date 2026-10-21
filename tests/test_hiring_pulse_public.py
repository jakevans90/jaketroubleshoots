import copy
import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("build_hiring_pulse_public", ROOT / "tools" / "build_hiring_pulse_public.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class HiringPulsePublicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.store = MODULE.pulse.load_store(ROOT)

    def test_snapshot_aggregations_match_active_source_records(self):
        snapshot = MODULE.build_public_snapshot(copy.deepcopy(self.store))
        active = [item for item in self.store["postings"]["records"] if item["status"] == "active"]
        self.assertEqual(len(active), snapshot["summary"]["activePostings"])
        self.assertEqual(len({item["employer_id"] for item in active}), snapshot["summary"]["employersRepresented"])
        self.assertEqual(len({item["location"]["state"] for item in active if item["location"].get("state")}), snapshot["summary"]["statesRepresented"])
        self.assertEqual(len({item["role_category_id"] for item in active}), snapshot["summary"]["roleCategoriesRepresented"])
        self.assertEqual(len(active), sum(item["activePostings"] for item in snapshot["breakdowns"]["roles"]))
        self.assertEqual(len(active), sum(item["activePostings"] for item in snapshot["breakdowns"]["employers"]))
        self.assertEqual(len(active), sum(item["activePostings"] for item in snapshot["breakdowns"]["employerTypes"]))
        self.assertTrue(all(item["employerTypeLabel"] for item in snapshot["postings"]))

    def test_public_records_are_unique_canonical_and_omit_descriptions(self):
        postings = MODULE.build_public_snapshot(copy.deepcopy(self.store))["postings"]
        self.assertEqual(len(postings), len({item["id"] for item in postings}))
        self.assertEqual(len(postings), len({item["url"] for item in postings}))
        self.assertTrue(all(item["url"].startswith("https://") for item in postings))
        self.assertTrue(all("description" not in item and "description_snippet" not in item for item in postings))

    def test_optional_salary_and_dates_may_be_missing(self):
        snapshot = MODULE.build_public_snapshot(copy.deepcopy(self.store))
        sample = snapshot["postings"][0]
        self.assertIn("salary", sample)
        self.assertIn("postedDate", sample)
        self.assertIn("firstObserved", sample)
        self.assertIsNotNone(sample["firstObserved"])

    def test_empty_active_data_uses_unavailable_fallback_without_zero_cards(self):
        store = copy.deepcopy(self.store)
        for posting in store["postings"]["records"]:
            posting["status"] = "closed"
            posting["closed_at"] = posting["last_seen"]
        snapshot = MODULE.build_public_snapshot(store)
        self.assertEqual("unavailable", snapshot["availability"])
        self.assertIsNone(snapshot["summary"])
        rendered = MODULE.render_static_summary(snapshot)
        self.assertIn("temporarily unavailable", rendered)
        self.assertNotIn(">0<", rendered)

    def test_invalid_canonical_url_is_rejected(self):
        store = copy.deepcopy(self.store)
        active = next(item for item in store["postings"]["records"] if item["status"] == "active")
        active["canonical_url"] = "javascript:alert(1)"
        with self.assertRaises(ValueError):
            MODULE.build_public_snapshot(store)

    def test_generated_files_are_current(self):
        self.assertTrue(MODULE.build(ROOT, check=True))


if __name__ == "__main__":
    unittest.main()
