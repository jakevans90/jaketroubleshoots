import copy
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("automate_htm_hiring_pulse", ROOT / "tools" / "automate_htm_hiring_pulse.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class HiringPulseAutomationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        destination = self.root / MODULE.pulse.DATA_DIR
        destination.mkdir(parents=True)
        for filename in MODULE.pulse.FILES.values():
            shutil.copy2(ROOT / MODULE.pulse.DATA_DIR / filename, destination / filename)
        shutil.copy2(ROOT / MODULE.collector.CONFIG_PATH, self.root / MODULE.collector.CONFIG_PATH)
        shutil.copy2(ROOT / MODULE.THRESHOLDS_PATH, self.root / MODULE.THRESHOLDS_PATH)

    def tearDown(self):
        self.temporary.cleanup()

    def external_record(self, source_id="trimedx-careers"):
        store = MODULE.pulse.load_store(self.root)
        posting = next(item for item in store["postings"]["records"] if item["source"] == source_id and item["status"] == "active")
        config = MODULE.collector.load_config(self.root)
        source = next(item for item in config["sources"] if item["id"] == source_id)
        return {
            "employer": source["employer"],
            "title": posting["title"],
            "location": copy.deepcopy(posting["location"]),
            "url": posting["canonical_url"],
            "sourcePostingId": posting["source_posting_id"],
            "employmentType": posting["employment_type"],
            "experienceLevel": posting["experience_level"],
            "salaryText": posting["salary_text"],
            "postedDate": posting["posted_date"],
            "descriptionSnippet": posting["description_snippet"],
            "roleCategoryId": posting["role_category_id"],
        }

    def test_partial_source_collapse_refreshes_seen_job_without_closing_missing_jobs(self):
        record = self.external_record()
        baseline_active = sum(MODULE.active_by_source(MODULE.pulse.load_store(self.root)).values())

        def fake_collect(source, checked_at, timeout):
            return MODULE.collector.CollectionResult(source["id"], [record], 1, True, {"biomedical": 1})

        report = MODULE.run_automation(
            self.root, ["trimedx-careers"], "2026-10-22T12:00:00Z", 10,
            True, True, self.root / "health.json", fake_collect,
        )
        self.assertEqual("warning", report["status"])
        self.assertEqual(1, report["summary"]["sourcesPartiallyChecked"])
        self.assertEqual(0, report["summary"]["postingsClosed"])
        self.assertEqual(baseline_active, report["summary"]["activePostings"])
        self.assertIn("collapsed", " ".join(report["warnings"]))

    def test_failed_zero_source_does_not_write_production_data(self):
        postings_path = self.root / MODULE.pulse.DATA_DIR / MODULE.pulse.FILES["postings"]
        before = postings_path.read_bytes()

        def zero_collect(source, checked_at, timeout):
            raise MODULE.collector.CollectionError("returned zero relevant US jobs")

        report_path = self.root / "health.json"
        with self.assertRaises(MODULE.collector.CollectionError):
            MODULE.run_automation(
                self.root, ["trimedx-careers"], "2026-10-22T12:00:00Z", 10,
                True, True, report_path, zero_collect,
            )
        self.assertEqual(before, postings_path.read_bytes())
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertEqual("failed", report["status"])
        self.assertEqual(1, report["summary"]["sourcesFailed"])

    def test_incomplete_pagination_never_closes_missing_jobs(self):
        record = self.external_record()

        def partial_collect(source, checked_at, timeout):
            return MODULE.collector.CollectionResult(source["id"], [record], 2, False, {"biomedical": 2})

        report = MODULE.run_automation(
            self.root, ["trimedx-careers"], "2026-10-22T12:00:00Z", 10,
            True, True, None, partial_collect,
        )
        self.assertEqual(0, report["summary"]["postingsClosed"])
        self.assertFalse(report["sources"][0]["snapshotComplete"])
        self.assertEqual("partial", report["sources"][0]["sourceStatus"])

    def test_health_report_contains_operational_totals(self):
        record = self.external_record()

        def complete_collect(source, checked_at, timeout):
            current = MODULE.active_by_source(MODULE.pulse.load_store(self.root))[source["id"]]
            records = [record] * current
            return MODULE.collector.CollectionResult(source["id"], records, current, False, {"test": current})

        report = MODULE.run_automation(
            self.root, ["trimedx-careers"], "2026-10-22T12:00:00Z", 10,
            False, False, None, complete_collect,
        )
        for key in ("activePostings", "trackedEmployers", "statesRepresented", "newPostingsDiscovered", "sourcesSuccessfullyChecked", "sourcesPartiallyChecked", "sourcesFailed", "postingsClosed"):
            self.assertIn(key, report["summary"])

    def test_workflow_validates_before_commit_and_uses_scoped_git_add(self):
        workflow = (ROOT / ".github" / "workflows" / "htm-hiring-pulse.yml").read_text(encoding="utf-8")
        self.assertIn('cron: "17 7 */3 * *"', workflow)
        self.assertLess(workflow.index("Run full validation"), workflow.index("Commit validated data update"))
        self.assertIn("--confirm-close-missing", workflow)
        self.assertNotIn("git add .", workflow)


if __name__ == "__main__":
    unittest.main()
