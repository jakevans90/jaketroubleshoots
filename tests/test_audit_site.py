import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from audit_site import SiteAuditor, markdown_report  # noqa: E402


class SiteAuditTests(unittest.TestCase):
    def fixture(self):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        (root / "data").mkdir()
        (root / "guides").mkdir()
        for kind, value in (
            ("asset", [{"name": "Monitor"}]),
            ("manufacturer", [{"name": "Acme"}]),
            ("model", [{"name": "Alpha", "slug": "alpha",
                        "profile": {"manufacturer": "Acme", "assetType": "Monitor"}}]),
        ):
            (root / f"data/hub-{kind}.json").write_text(json.dumps(value), encoding="utf-8")
        (root / "data/guides.json").write_text('["data/guides-acme.json"]', encoding="utf-8")
        record = {
            "title": "Acme Alpha - Error E42", "description": "Acme Alpha Error E42 guide.",
            "assetType": "Monitor", "manufacturer": "Acme", "model": "Alpha",
            "url": "guides/acme-alpha-error-e42.html", "dateAdded": "2026-01-01",
            "steps": [{"title": "Check", "instructions": "Verify the expected indicator."}],
            "documentation": {"CCR": {"Complaint": "x", "Cause": "y", "Resolution": "z"}},
            "helpfulDetails": ["Observed code"],
        }
        (root / "data/guides-acme.json").write_text(json.dumps([record]), encoding="utf-8")
        html = """<!doctype html><html><head>
<title>Acme Alpha - Error E42</title>
<meta name="description" content="Acme Alpha Error E42 guide.">
<link rel="canonical" href="https://jaketroubleshoots.com/guides/acme-alpha-error-e42.html">
</head><body>
<h3>Asset Type</h3><p>Monitor</p><h3>Manufacturer</h3><p>Acme</p><h3>Model</h3><p>Alpha</p>
<h2>What This Guide Helps With</h2><h2>Step-by-Step Troubleshooting</h2>
<h2>If the Problem Persists</h2><h2>Work Order Documentation (CCR Method)</h2>
<p>CCR = Complaint, Cause, Resolution</p><h2>Helpful Details to Include</h2>
<div id="related-guides-grid"></div>
<script src="/related-guides.js"></script><script src="../hub-links.js"></script>
<script src="../feedback.js"></script><script src="../guide-icons.js"></script>
<footer>Guides intended for trained personnel only.</footer></body></html>"""
        (root / record["url"]).write_text(html, encoding="utf-8")
        (root / "sitemap.xml").write_text(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'
            'https://jaketroubleshoots.com/guides/acme-alpha-error-e42.html'
            '</loc></url></urlset>', encoding="utf-8")
        return temporary, root

    def test_clean_fixture_has_no_findings(self):
        temporary, root = self.fixture()
        with temporary:
            result = SiteAuditor(root).audit()
            self.assertEqual(result["summary"]["totalFindings"], 0, result["findings"])

    def test_detects_canonical_duplicate_record_and_taxonomy_errors(self):
        temporary, root = self.fixture()
        with temporary:
            shard = json.loads((root / "data/guides-acme.json").read_text())
            duplicate = dict(shard[0], assetType="Patient monitor")
            (root / "data/guides-acme.json").write_text(json.dumps([shard[0], duplicate]))
            page = root / shard[0]["url"]
            page.write_text(page.read_text().replace(
                "https://jaketroubleshoots.com/guides/acme-alpha-error-e42.html",
                "http://example.test/wrong"))
            issues = {x["issue_type"] for x in SiteAuditor(root).audit()["findings"]}
            self.assertIn("incorrect_canonical_url", issues)
            self.assertIn("duplicate_url", issues)
            self.assertIn("missing_hub_taxonomy_record", issues)

    def test_duplicate_record_is_not_reported_twice_as_same_underlying_defect(self):
        temporary, root = self.fixture()
        with temporary:
            shard = json.loads((root / "data/guides-acme.json").read_text())
            (root / "data/guides-acme.json").write_text(json.dumps([shard[0], shard[0]]))
            issues = [x["issue_type"] for x in SiteAuditor(root).audit()["findings"]]
            self.assertIn("duplicate_title", issues)
            self.assertNotIn("duplicate_manufacturer_model_issue", issues)

    def test_alarm_priority_punctuation_keeps_titles_distinct(self):
        temporary, root = self.fixture()
        with temporary:
            shard = json.loads((root / "data/guides-acme.json").read_text())
            second = dict(shard[0], title="Acme Alpha - Error E42 !!")
            shard[0]["title"] = "Acme Alpha - Error E42 !!!"
            (root / "data/guides-acme.json").write_text(json.dumps([shard[0], second]))
            issues = [x["issue_type"] for x in SiteAuditor(root).audit()["findings"]]
            self.assertNotIn("duplicate_title", issues)

    def test_established_optional_helpful_details_heading_is_accepted(self):
        temporary, root = self.fixture()
        with temporary:
            page = root / "guides/acme-alpha-error-e42.html"
            page.write_text(page.read_text().replace(
                "Helpful Details to Include", "Helpful Details to Include (If Known)"))
            issues = {x["issue_type"] for x in SiteAuditor(root).audit()["findings"]}
            self.assertNotIn("missing_required_section", issues)

    def test_model_match_does_not_cross_word_boundary(self):
        temporary, root = self.fixture()
        with temporary:
            models = json.loads((root / "data/hub-model.json").read_text())
            models.append({"name": "ED-Flow", "slug": "ed-flow",
                           "profile": {"manufacturer": "Acme", "assetType": "Monitor"}})
            (root / "data/hub-model.json").write_text(json.dumps(models))
            shard = json.loads((root / "data/guides-acme.json").read_text())
            shard[0]["description"] = "Troubleshooting failed flow sensor calibration."
            (root / "data/guides-acme.json").write_text(json.dumps(shard))
            page = root / shard[0]["url"]
            page.write_text(page.read_text().replace(
                "Acme Alpha Error E42 guide.", shard[0]["description"]))
            issues = {x["issue_type"] for x in SiteAuditor(root).audit()["findings"]}
            self.assertNotIn("unrelated_metadata_wording", issues)

    def test_legitimate_issue_specific_meta_wording_need_not_be_identical(self):
        temporary, root = self.fixture()
        with temporary:
            page = root / "guides/acme-alpha-error-e42.html"
            page.write_text(page.read_text().replace(
                "Acme Alpha Error E42 guide.",
                "Troubleshooting Acme Alpha E42 failures caused by setup or sensor issues."))
            issues = {x["issue_type"] for x in SiteAuditor(root).audit()["findings"]}
            self.assertNotIn("meta_description_mismatch", issues)

    def test_insert_code_documentation_example_is_not_a_template_marker(self):
        temporary, root = self.fixture()
        with temporary:
            page = root / "guides/acme-alpha-error-e42.html"
            page.write_text(page.read_text().replace(
                "</body>", "<p>Error code recorded: [Insert code]</p></body>"))
            issues = {x["issue_type"] for x in SiteAuditor(root).audit()["findings"]}
            self.assertNotIn("placeholder_or_template_instruction", issues)

    def test_historical_model_taxonomy_aliases_are_accepted(self):
        temporary, root = self.fixture()
        with temporary:
            manufacturers = json.loads((root / "data/hub-manufacturer.json").read_text())
            manufacturers.append({"name": "Hamilton"})
            (root / "data/hub-manufacturer.json").write_text(json.dumps(manufacturers))
            models = json.loads((root / "data/hub-model.json").read_text())
            models.append({"name": "C3", "slug": "c3",
                           "profile": {"manufacturer": "Hamilton Medical", "assetType": "Monitor"}})
            (root / "data/hub-model.json").write_text(json.dumps(models))
            findings = SiteAuditor(root).audit()["findings"]
            aliases = [x for x in findings if x["issue_type"] == "model_noncanonical_taxonomy_link"]
            self.assertEqual(aliases, [])

    def test_registered_legacy_manufacturer_shard_name_is_accepted(self):
        temporary, root = self.fixture()
        with temporary:
            manufacturer = [{"name": "Senko Medical", "slug": "senko-medical"}]
            (root / "data/hub-manufacturer.json").write_text(json.dumps(manufacturer))
            shard = json.loads((root / "data/guides-acme.json").read_text())
            shard[0]["manufacturer"] = "Senko Medical"
            (root / "data/guides-acme.json").unlink()
            (root / "data/guides-senko.json").write_text(json.dumps(shard))
            (root / "data/guides.json").write_text('["data/guides-senko.json"]')
            issues = [x["issue_type"] for x in SiteAuditor(root).audit()["findings"]]
            self.assertNotIn("wrong_manufacturer_shard", issues)

    def test_invalid_json_and_unregistered_shard_are_reported(self):
        temporary, root = self.fixture()
        with temporary:
            (root / "data/guides-acme.json").write_text("{")
            (root / "data/guides-extra.json").write_text("[]")
            issues = {x["issue_type"] for x in SiteAuditor(root).audit()["findings"]}
            self.assertIn("invalid_json", issues)
            self.assertIn("unregistered_manufacturer_shard", issues)

    def test_markdown_groups_all_severities_and_required_fields(self):
        temporary, root = self.fixture()
        with temporary:
            page = root / "guides/acme-alpha-error-e42.html"
            page.write_text(page.read_text().replace("<title>", "<title></title><title>"))
            result = SiteAuditor(root).audit()
            report = markdown_report(result)
            for severity in ("Critical", "High", "Medium", "Low"):
                self.assertIn(f"## {severity}", report)
            self.assertIn("Recommended structural correction", report)
            self.assertIn("Counts by manufacturer", report)


if __name__ == "__main__":
    unittest.main()
