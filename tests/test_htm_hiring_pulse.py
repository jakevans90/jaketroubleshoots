import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("htm_hiring_pulse", ROOT / "tools" / "htm_hiring_pulse.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class HiringPulseTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        destination = self.root / MODULE.DATA_DIR
        destination.mkdir(parents=True)
        source = ROOT / MODULE.DATA_DIR
        for filename in MODULE.FILES.values():
            (destination / filename).write_bytes((source / filename).read_bytes())

    def tearDown(self):
        self.temporary.cleanup()

    def posting(self, job_id="123", query="utm_source=test"):
        return {
            "employer": {"name": "Example Health", "employerType": "health-system"},
            "title": "Biomedical Equipment Technician II",
            "location": {"text": "Pittsburgh, PA", "city": "Pittsburgh", "state": "pa", "country": "us", "remote": False},
            "url": f"https://jobs.example.org/postings/{job_id}?{query}",
            "sourcePostingId": job_id,
        }

    def test_seed_data_validates(self):
        self.assertEqual([], MODULE.validate_store(MODULE.load_store(self.root)))

    def test_tracking_parameters_do_not_create_duplicates(self):
        store = MODULE.load_store(self.root)
        MODULE.upsert_records(store, [self.posting(query="utm_source=one")], "test-source", "2026-10-01T12:00:00Z", False)
        MODULE.upsert_records(store, [self.posting(query="utm_source=two&gclid=abc")], "test-source", "2026-10-02T12:00:00Z", False)
        self.assertEqual(1, len(store["employers"]["records"]))
        self.assertEqual(1, len(store["postings"]["records"]))
        self.assertEqual("2026-10-02T12:00:00Z", store["postings"]["records"][0]["last_seen"])
        self.assertEqual([], MODULE.validate_store(store))

    def test_complete_sync_closes_missing_and_reopens_seen_posting(self):
        store = MODULE.load_store(self.root)
        first = [self.posting("123"), self.posting("456")]
        MODULE.upsert_records(store, first, "test-source", "2026-10-01T12:00:00Z", True)
        check = MODULE.upsert_records(store, [self.posting("123")], "test-source", "2026-10-02T12:00:00Z", True)
        closed = next(item for item in store["postings"]["records"] if item["source_posting_id"] == "456")
        self.assertEqual("closed", closed["status"])
        self.assertEqual(1, check["closed_count"])
        reopened_check = MODULE.upsert_records(store, [self.posting("456")], "test-source", "2026-10-03T12:00:00Z", False)
        self.assertEqual("active", closed["status"])
        self.assertEqual(1, reopened_check["reopened_count"])
        self.assertIsNone(closed["closed_at"])
        self.assertEqual([], MODULE.validate_store(store))

    def test_partial_sync_never_closes_missing_postings(self):
        store = MODULE.load_store(self.root)
        MODULE.upsert_records(store, [self.posting("123"), self.posting("456")], "test-source", "2026-10-01T12:00:00Z", True)
        check = MODULE.upsert_records(store, [self.posting("123")], "test-source", "2026-10-02T12:00:00Z", False)
        self.assertEqual(0, check["closed_count"])
        self.assertTrue(all(item["status"] == "active" for item in store["postings"]["records"]))

    def test_summary_counts_active_employers_new_jobs_states_and_roles(self):
        store = MODULE.load_store(self.root)
        MODULE.upsert_records(store, [self.posting("123"), self.posting("456")], "test-source", "2026-10-01T12:00:00Z", True)
        summary = MODULE.build_summary(store, "2026-10-02T12:00:00Z", 7)
        self.assertEqual(2, summary["activePostings"])
        self.assertEqual(1, summary["employersRepresented"])
        self.assertEqual(2, summary["newlyObservedJobs"])
        self.assertEqual({"count": 1, "states": ["PA"]}, summary["statesRepresented"])
        self.assertEqual("bmet", summary["roleCategories"][0]["id"])

    def test_dry_run_does_not_write(self):
        input_path = self.root / "input.json"
        input_path.write_text(json.dumps([self.posting()]), encoding="utf-8")
        before = {name: (self.root / MODULE.DATA_DIR / name).read_bytes() for name in MODULE.FILES.values()}
        code = MODULE.main(["--root", str(self.root), "upsert", "--source", "test-source", "--input", str(input_path), "--observed-at", "2026-10-02T12:00:00Z", "--dry-run"])
        after = {name: (self.root / MODULE.DATA_DIR / name).read_bytes() for name in MODULE.FILES.values()}
        self.assertEqual(0, code)
        self.assertEqual(before, after)

    def test_validation_rejects_malformed_url(self):
        store = MODULE.load_store(self.root)
        broken = self.posting()
        broken["url"] = "javascript:alert(1)"
        with self.assertRaisesRegex(ValueError, "absolute HTTP"):
            MODULE.upsert_records(store, [broken], "test-source", "2026-10-02T12:00:00Z", False)


if __name__ == "__main__":
    unittest.main()
