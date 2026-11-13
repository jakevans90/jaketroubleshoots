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
    elif adapter == "phenom":
        base["adapterConfig"].update({"searchUrl": "https://example.test/search", "jobIdentifierField": "jobId", "queryParameter": "keywords"})
    else:
        base["adapterConfig"].update({
            "searchUrl": "https://example.test/search-jobs",
            "resultsUrl": "https://example.test/search-jobs/results",
            "organizationId": "12345",
        })
    return base


class CollectorTests(unittest.TestCase):
    def test_live_source_configuration_is_valid(self):
        config = json.loads((ROOT / MODULE.CONFIG_PATH).read_text(encoding="utf-8"))
        self.assertEqual([], MODULE.validate_config(config))
        self.assertEqual(25, len(config["sources"]))
        expected_expansion = {
            "bd-careers", "abbott-careers", "danaher-careers", "iqvia-medtech-careers",
            "allina-health-careers", "houston-methodist-careers", "uams-health-careers",
            "halifax-health-careers", "brown-health-careers", "cape-fear-valley-careers",
            "trinity-health-careers", "adventhealth-careers", "commonspirit-health-careers",
        }
        self.assertTrue(expected_expansion.issubset({item["id"] for item in config["sources"]}))

    def test_hospital_title_rules_accept_htm_roles_and_reject_false_positives(self):
        config = json.loads((ROOT / MODULE.CONFIG_PATH).read_text(encoding="utf-8"))
        cleveland = next(item for item in config["sources"] if item["id"] == "cleveland-clinic-careers")
        self.assertTrue(MODULE.relevant_title(cleveland, "CE Technician II"))
        self.assertTrue(MODULE.relevant_title(cleveland, "Clinical Engineering Technician II"))
        self.assertTrue(MODULE.relevant_title(cleveland, "Biomedical Equipment Technician"))
        self.assertFalse(MODULE.relevant_title(cleveland, "Research Biomedical Engineer"))
        self.assertFalse(MODULE.relevant_title(cleveland, "Facilities Engineering Technician"))
        self.assertFalse(MODULE.relevant_title(cleveland, "Patient Care Equipment Technician"))

    def test_phenom_ddo_parser_reads_embedded_jobs(self):
        payload = {"eagerLoadRefineSearch": {"status": 200, "hits": 1, "totalHits": 1, "data": {"jobs": [{"jobId": "R1"}]}}}
        html = "<script>window.x = 1; phApp.ddo = " + json.dumps(payload) + "; window.y = 2;</script>"
        jobs, hits, total = MODULE.phenom_page_data(html)
        self.assertEqual([{"jobId": "R1"}], jobs)
        self.assertEqual((1, 1), (hits, total))

    def test_talentbrew_parser_reads_cards_and_pagination(self):
        html = """
        <section id="search-results" data-total-job-results="1" data-total-pages="1"
          data-current-page="1" data-records-per-page="11">
          <a class="search-results-list__job-link" href="/job/austin/bmet/35300/987" data-job-id="987">
            Biomedical Equipment Technician II
          </a>
          <li class="search-results-list__item job-location">Austin, TX</li>
        </section>
        """
        jobs, meta = MODULE.talentbrew_page_data(html)
        self.assertEqual({"total": 1, "totalPages": 1, "currentPage": 1, "pageSize": 11}, meta)
        self.assertEqual("Biomedical Equipment Technician II", jobs[0]["title"])
        self.assertEqual("Austin, TX", jobs[0]["location"])

    def test_talentbrew_collection_paginates_filters_and_deduplicates(self):
        configured = source("talentbrew")
        first = """
        <section id="search-results" data-total-job-results="2" data-total-pages="2"
          data-current-page="1" data-records-per-page="1">
          <a class="search-results-list__job-link" href="/job/austin/bmet/35300/1" data-job-id="1">Biomedical Technician I</a>
          <li class="job-location">Austin, TX</li>
        </section>
        """
        second = """
        <section id="search-results" data-total-job-results="2" data-total-pages="2"
          data-current-page="2" data-records-per-page="1">
          <a class="search-results-list__job-link" href="/job/austin/nurse/35300/2" data-job-id="2">Registered Nurse</a>
          <li class="job-location">Austin, TX</li>
        </section>
        """

        result = MODULE.collect_talentbrew(
            configured, "2026-11-13T12:00:00Z", 10,
            get=lambda url, timeout: first,
            get_object=lambda url, timeout: {"results": second},
        )
        self.assertTrue(result.complete)
        self.assertEqual(2, result.scanned)
        self.assertEqual(1, len(result.postings))
        self.assertEqual("https://example.test/job/austin/bmet/35300/1", result.postings[0]["url"])

    def test_new_source_closure_guard_overrides_complete_snapshot_confirmation(self):
        configured = source("workday")
        result = MODULE.CollectionResult("example-careers", [], 0, True, {})
        self.assertTrue(MODULE.missing_jobs_may_close(configured, result, True))
        configured["adapterConfig"]["guardClosures"] = True
        self.assertFalse(MODULE.missing_jobs_may_close(configured, result, True))

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

    def test_workday_foreign_remote_is_rejected_without_rejecting_us_place_names(self):
        configured = source("workday")
        foreign = MODULE.workday_record(configured, {
            "title": "Biomedical Field Service Technician",
            "externalPath": "/job/United-Kingdom---Remote/Technician_R101",
            "locationsText": "GBR - Remote",
        }, "2026-10-20T12:00:00Z")
        maine = MODULE.workday_record(configured, {
            "title": "Biomedical Field Service Technician",
            "externalPath": "/job/Norway-Maine-United-States/Technician_R102",
            "locationsText": "Norway, ME",
        }, "2026-10-20T12:00:00Z")
        self.assertIsNone(foreign)
        self.assertIsNotNone(maine)
        self.assertEqual("ME", maine["location"]["state"])

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

    def test_explicit_empty_snapshot_is_allowed_for_new_narrow_sources(self):
        configured = source("workday")
        configured["adapterConfig"]["allowEmptySnapshot"] = True

        def fake_post(url, payload, timeout):
            return {"total": 0, "jobPostings": []}

        result = MODULE.collect_workday(configured, "2026-10-20T12:00:00Z", 10, post=fake_post)
        self.assertTrue(result.complete)
        self.assertEqual([], result.postings)

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

    def test_multi_location_duplicate_on_one_page_deduplicates_without_faking_pagination_failure(self):
        configured = source("workday")
        job = {"title": "Biomedical Technician I", "externalPath": "/job/Austin-TX/Tech_R1", "locationsText": "Austin, TX"}

        def fake_post(url, payload, timeout):
            return {"total": 2, "jobPostings": [job, {**job, "locationsText": "Dallas, TX"}]}

        result = MODULE.collect_workday(configured, "2026-10-20T12:00:00Z", 10, post=fake_post)
        self.assertTrue(result.complete)
        self.assertEqual(2, result.scanned)
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

    def test_reclassify_closes_existing_non_us_workday_posting(self):
        configured = source("workday")
        store = {
            "taxonomy": {"categories": [{"id": "other-htm", "label": "Other", "description": "", "titlePatterns": []}]},
            "postings": {"records": [{
                "source": "example-careers", "title": "Biomedical Field Service Technician",
                "role_category_id": "other-htm", "status": "active", "closed_at": None,
                "canonical_url": "https://example.test/en-US/jobs/job/Canada---Remote/Technician_R1",
                "location": {"text": "Canada - Remote"}, "updated_at": "2026-10-01T00:00:00Z",
            }]},
        }
        changed = MODULE.reclassify_configured_postings(store, {"sources": [configured]}, "2026-10-21T12:00:00Z")
        self.assertEqual(1, changed)
        self.assertEqual("closed", store["postings"]["records"][0]["status"])
        self.assertEqual("2026-10-21T12:00:00Z", store["postings"]["records"][0]["closed_at"])


if __name__ == "__main__":
    unittest.main()
