import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("collect_htm_hiring_pulse", ROOT / "tools" / "collect_htm_hiring_pulse.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def source(adapter):
    base = {
        "id": "example-careers",
        "enabled": True,
        "employer": {"name": "Example", "employerType": "oem", "careerUrl": "https://example.test/jobs", "websiteUrl": "https://example.test"},
        "adapter": adapter,
        "queries": ["biomedical"],
        "relevancePatterns": [r"\bbiomed(?:ical)?\b"],
        "roleOverrides": [],
        "adapterConfig": {
            "publicBaseUrl": "https://example.test",
            "publicSitePath": "/en-US/jobs",
            "robotsUrl": "https://example.test/robots.txt",
            "pageSize": 20,
            "maxResultsPerQuery": 100,
        },
    }
    if adapter == "workday":
        base["adapterConfig"]["apiUrl"] = "https://example.test/wday/jobs"
    else:
        base["adapterConfig"].update({"searchUrl": "https://example.test/search", "jobIdentifierField": "jobId", "queryParameter": "keywords"})
    return base


class CollectorTests(unittest.TestCase):
    def test_live_source_configuration_is_valid(self):
        config = json.loads((ROOT / MODULE.CONFIG_PATH).read_text(encoding="utf-8"))
        self.assertEqual([], MODULE.validate_config(config))
        self.assertEqual(5, len(config["sources"]))

    def test_phenom_ddo_parser_reads_embedded_jobs(self):
        payload = {"eagerLoadRefineSearch": {"status": 200, "hits": 1, "totalHits": 1, "data": {"jobs": [{"jobId": "R1"}]}}}
        html = "<script>window.x = 1; phApp.ddo = " + json.dumps(payload) + "; window.y = 2;</script>"
        jobs, hits, total = MODULE.phenom_page_data(html)
        self.assertEqual([{"jobId": "R1"}], jobs)
        self.assertEqual((1, 1), (hits, total))

    def test_workday_collection_paginates_filters_and_deduplicates(self):
        configured = source("workday")
        responses = [
            {"total": 2, "jobPostings": [
                {"title": "Biomedical Equipment Technician II", "externalPath": "/job/Pittsburgh-PA/BMET_R100", "locationsText": "Pittsburgh, PA", "postedOn": "Posted 2 Days Ago"},
                {"title": "Software Developer", "externalPath": "/job/Pittsburgh-PA/Developer_R200", "locationsText": "Pittsburgh, PA", "postedOn": "Posted Today"},
            ]}
        ]

        def fake_post(url, payload, timeout):
            return responses.pop(0)

        result = MODULE.collect_workday(configured, "2026-10-20T12:00:00Z", 10, post=fake_post)
        self.assertTrue(result.complete)
        self.assertEqual(2, result.scanned)
        self.assertEqual(1, len(result.postings))
        self.assertEqual("2026-10-18", result.postings[0]["postedDate"])
        self.assertEqual("PA", result.postings[0]["location"]["state"])

    def test_phenom_record_uses_exact_posted_date_and_us_location(self):
        configured = source("phenom")
        record = MODULE.phenom_record(configured, {
            "jobId": "R300",
            "title": "Biomedical Technician",
            "cityState": "Boston, Massachusetts",
            "country": "United States of America",
            "postedDate": "2026-10-19T00:00:00.000+0000",
            "descriptionTeaser_first200": "Maintains medical equipment.",
        }, "2026-10-20T12:00:00Z")
        self.assertIsNotNone(record)
        self.assertEqual("MA", record["location"]["state"])
        self.assertEqual("2026-10-19", record["postedDate"])
        self.assertEqual("https://example.test/en-US/jobs/job/R300/biomedical-technician", record["url"])

    def test_zero_relevant_results_are_rejected(self):
        configured = source("workday")

        def fake_post(url, payload, timeout):
            return {"total": 1, "jobPostings": [{
                "title": "Software Developer", "externalPath": "/job/Austin-TX/Developer_R400", "locationsText": "Austin, TX"
            }]}

        with self.assertRaisesRegex(MODULE.CollectionError, "zero relevant US jobs"):
            MODULE.collect_workday(configured, "2026-10-20T12:00:00Z", 10, post=fake_post)

    def test_live_total_change_keeps_partial_results_but_disables_closure(self):
        configured = source("workday")
        configured["adapterConfig"]["pageSize"] = 1
        responses = [
            {"total": 2, "jobPostings": [{"title": "Biomedical Technician I", "externalPath": "/job/Austin-TX/Tech_R1", "locationsText": "Austin, TX"}]},
            {"total": 1, "jobPostings": []},
        ]

        def fake_post(url, payload, timeout):
            return responses.pop(0)

        result = MODULE.collect_workday(configured, "2026-10-20T12:00:00Z", 10, post=fake_post)
        self.assertFalse(result.complete)
        self.assertEqual(1, len(result.postings))

    def test_duplicate_jobs_across_pages_disable_complete_snapshot(self):
        configured = source("workday")
        configured["adapterConfig"]["pageSize"] = 1
        job = {"title": "Biomedical Technician I", "externalPath": "/job/Austin-TX/Tech_R1", "locationsText": "Austin, TX"}
        responses = [
            {"total": 2, "jobPostings": [job]},
            {"total": 2, "jobPostings": [job]},
        ]

        def fake_post(url, payload, timeout):
            return responses.pop(0)

        result = MODULE.collect_workday(configured, "2026-10-20T12:00:00Z", 10, post=fake_post)
        self.assertFalse(result.complete)
        self.assertEqual(1, len(result.postings))

    def test_dry_run_does_not_write_authoritative_data(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            destination = root / MODULE.pulse.DATA_DIR
            destination.mkdir(parents=True)
            for filename in MODULE.pulse.FILES.values():
                (destination / filename).write_bytes((ROOT / MODULE.pulse.DATA_DIR / filename).read_bytes())
            (root / MODULE.CONFIG_PATH).write_bytes((ROOT / MODULE.CONFIG_PATH).read_bytes())
            before = {name: (destination / name).read_bytes() for name in MODULE.pulse.FILES.values()}
            store = MODULE.pulse.load_store(root)
            posting = {
                "employer": {"name": "Example", "employerType": "oem"},
                "title": "Biomedical Equipment Technician",
                "location": {"text": "Austin, TX", "city": "Austin", "state": "TX", "country": "US", "remote": False},
                "url": "https://example.test/job/R500/biomedical-equipment-technician",
                "sourcePostingId": "R500",
            }
            MODULE.pulse.upsert_records(store, [posting], "example-careers", "2026-10-20T12:00:00Z", False)
            MODULE.pulse.save_store(root, store, {"employers", "postings", "observations"}, dry_run=True)
            after = {name: (destination / name).read_bytes() for name in MODULE.pulse.FILES.values()}
            self.assertEqual(before, after)

    def test_reclassify_updates_existing_configured_posting(self):
        configured = source("phenom")
        configured["relevancePatterns"] = ["service manager"]
        store = {
            "taxonomy": {"categories": [
                {"id": "leadership", "label": "Leadership", "description": "", "titlePatterns": ["service manager"]},
                {"id": "other-htm", "label": "Other", "description": "", "titlePatterns": []},
            ]},
            "postings": {"records": [{"source": "example-careers", "title": "Technical Service Manager", "role_category_id": "other-htm", "updated_at": "2026-10-01T00:00:00Z"}]},
        }
        changed = MODULE.reclassify_configured_postings(store, {"sources": [configured]}, "2026-10-21T12:00:00Z")
        self.assertEqual(1, changed)
        self.assertEqual("leadership", store["postings"]["records"][0]["role_category_id"])


if __name__ == "__main__":
    unittest.main()
