import contextlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import unittest
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from publish_guide import InputError, build_plan, main, parse_input  # noqa: E402


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
        original = self.fixture("valid-guide.md").read_text(encoding="utf-8")
        broken = original.replace("schemaVersion: 1", "schemaVersion: 1\nschemaVersion: 1")
        path = self.fixture("temporary-invalid.md")
        try:
            path.write_text(broken, encoding="utf-8")
            with self.assertRaises(InputError):
                parse_input(path)
        finally:
            path.unlink(missing_ok=True)

    def make_repository(self, new_manufacturer=False):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        (root / "data").mkdir()
        (root / "guides").mkdir()
        template = (ROOT / "guides/fresenius-kabi-agilia-air-in-line-alarm-or-air-detector-false-alarm.html").read_text(encoding="utf-8")
        (root / "guides/acme-alpha-existing.html").write_text(template, encoding="utf-8")
        asset = [{"type": "asset", "name": "Infusion Pump", "slug": "infusion-pump"}]
        manufacturer = [{"type": "manufacturer", "name": "Acme", "slug": "acme"}]
        model = [{"type": "model", "name": "Alpha", "slug": "alpha", "profile": {"manufacturer": "Acme", "assetType": "Infusion Pump"}}]
        guide = {"title": "Acme Alpha Infusion Pump - Existing", "description": "Existing.", "assetType": "Infusion Pump", "manufacturer": "Acme", "model": "Alpha", "url": "guides/acme-alpha-existing.html", "dateAdded": "2026-01-01", "steps": [], "documentation": {"CCR": {}}, "helpfulDetails": []}
        files = {
            "data/hub-asset.json": asset,
            "data/hub-manufacturer.json": manufacturer,
            "data/hub-model.json": model,
            "data/guides.json": ["data/guides-acme.json"],
            "data/guides-acme.json": [guide],
        }
        for name, value in files.items():
            (root / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        (root / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://jaketroubleshoots.com/guides/acme-alpha-existing.html</loc></url></urlset>\n', encoding="utf-8")
        (root / "unrelated.txt").write_text("do not change\n", encoding="utf-8")
        source = self.new_manufacturer_input() if new_manufacturer else self.normal_input()
        (root / "input.md").write_text(source, encoding="utf-8")
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "tests@example.invalid"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "Publisher Tests"], cwd=root, check=True)
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "fixture"], cwd=root, check=True)
        return temporary, root

    @staticmethod
    def normal_input():
        return '''---
schemaVersion: 1
title: "Acme Alpha Infusion Pump - Error E42"
issueTitle: "Error E42"
description: "Preserve O₂ at 5 L/min and Error E42 exactly."
assetType: "Infusion Pump"
manufacturer: "Acme"
model: "Alpha"
slug: "acme-alpha-error-e42"
dateAdded: "2026-07-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported Error E42 during O₂ delivery."
  cause: "The approved test found flow below 5 L/min."
  resolution: "Removed from service; return only after the E42 test passes."
helpfulDetails:
  - "Exact Error E42 display"
---
## What This Guide Helps With

Preserve O₂ at 5 L/min and Error E42 exactly.

## Step-by-Step Troubleshooting

### 1. Stop Safely

Remove from patient use; do not bypass Error E42.

**Expected outcome:** O₂ delivery continues on a verified device.

## If the Problem Persists

Escalate to authorized personnel. Return to service only after all tests pass.

## Clinical Use Tip

Transfer therapy before testing.

## Work Order Documentation (CCR Method)

Use the supplied wording.
CCR = Complaint, Cause, Resolution
<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

Use the supplied label.
<!-- Helpful details come from front matter. -->

## Final Thought

Safe escalation protects patients.
'''

    def new_manufacturer_input(self):
        text = self.normal_input().replace('title: "Acme Alpha Infusion Pump - Error E42"', 'title: "NewCo Beta Infusion Pump - Error E42"').replace('manufacturer: "Acme"', 'manufacturer: "NewCo"').replace('model: "Alpha"', 'model: "Beta"').replace('slug: "acme-alpha-error-e42"', 'slug: "newco-beta-error-e42"').replace('taxonomyMode: "reuse"', 'taxonomyMode: "create-missing"')
        insertion = '''newManufacturer:
  type: "manufacturer"
  name: "NewCo"
  slug: "newco"
  url: "hub-manufacturer.html?slug=newco"
  meta:
    description: "NewCo devices"
    keywords: "NewCo"
    lastUpdated: "2026-07-27"
  profile:
    blurb: "NewCo profile"
    founded: "2020"
    headquarters: "Test City"
    website: "https://example.invalid"
    vendorPage: "vendors/newco.html"
    logo: "images/newco.png"
    specialties: "Infusion pumps"
  content:
    featuredGuides: "new guide"
    pinnedModels: "Beta"
    commonIssues: "Error E42"
    tips: "Approved procedures"
    warnings: "Trained personnel only"
  stats:
    guideCount: 1
    modelCount: 1
    assetTypes: "Infusion Pump"
  flags:
    exists: true
    featured: false
    hasLogo: true
    hasVendorPage: true
    verified: true
newModel:
  type: "model"
  name: "Beta"
  slug: "beta"
  url: "hub-model.html?slug=beta"
  meta:
    description: "Beta model"
    keywords: "Beta"
    lastUpdated: "2026-07-27"
  profile:
    blurb: "Beta profile"
    manufacturer: "NewCo"
    assetType: "Infusion Pump"
    website: "https://example.invalid/beta"
  content:
    featuredGuides: "new guide"
    commonIssues: "Error E42"
    tips: "Approved procedures"
    warnings: "Trained personnel only"
  stats:
    guideCount: 1
  flags:
    exists: true
    featured: false
    verified: true
'''
        return text.replace('ccr:\n', insertion + 'ccr:\n')

    def planned(self, root):
        path = root / "input.md"
        meta, sections, steps = parse_input(path)
        return build_plan(meta, root, sections, steps, path.read_bytes())

    def run_main(self, root, *extra):
        output, error = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(error):
            code = main([str(root / "input.md"), "--root", str(root), *extra])
        return code, output.getvalue(), error.getvalue()

    def test_successful_write_generates_html_shard_and_sitemap_without_collateral_changes(self):
        temporary, root = self.make_repository()
        with temporary:
            plan = self.planned(root)
            before = (root / "unrelated.txt").read_bytes()
            code, output, error = self.run_main(root, "--write", "--confirm-plan", plan.digest)
            self.assertEqual((code, error), (0, ""))
            report = json.loads(output)
            page = (root / "guides/acme-alpha-error-e42.html").read_text(encoding="utf-8")
            description_match = re.search(r'<meta name="description" content="([^"]*)">', page)
            self.assertIsNotNone(description_match)
            self.assertEqual(description_match.group(1), plan.meta["description"])
            self.assertNotIn("Turn Assist and Continuous Lateral Rotation", page)
            self.assertNotIn("&lt;!--", page)
            self.assertNotIn("CCR examples come from front matter.", page)
            self.assertNotIn("Helpful details come from front matter.", page)
            self.assertIn("Preserve O₂ at 5 L/min and Error E42 exactly.", page)
            self.assertIn("Removed from service; return only after the E42 test passes.", page)
            self.assertIn("Remove from patient use; do not bypass Error E42.", page)
            self.assertIn("Escalate to authorized personnel. Return to service only after all tests pass.", page)
            self.assertEqual(page.count("CCR = Complaint, Cause, Resolution"), 1)
            self.assertIn("<p><strong>CCR = Complaint, Cause, Resolution</strong></p>", page)
            self.assertNotIn("<p>CCR = Complaint, Cause, Resolution</p>", page)
            for value in plan.meta["ccr"].values():
                self.assertIn(f'"{value}"', page)
            self.assertIn("Related Guides", page)
            self.assertEqual(len(json.loads((root / "data/guides-acme.json").read_text(encoding="utf-8"))), 2)
            self.assertEqual((root / "sitemap.xml").read_text(encoding="utf-8").count("guides/acme-alpha-error-e42.html"), 1)
            self.assertEqual((root / "unrelated.txt").read_bytes(), before)
            self.assertEqual(report["taxonomyDecisions"]["manufacturer"], "reused")

    def test_new_manufacturer_shard_is_created_and_registered_once(self):
        temporary, root = self.make_repository(new_manufacturer=True)
        with temporary:
            plan = self.planned(root)
            self.assertFalse(plan.errors)
            code, _, _ = self.run_main(root, "--write", "--confirm-plan", plan.digest)
            self.assertEqual(code, 0)
            self.assertTrue((root / "data/guides-newco.json").is_file())
            self.assertEqual(json.loads((root / "data/guides.json").read_text(encoding="utf-8")).count("data/guides-newco.json"), 1)

    def test_simulated_failure_rolls_back_every_destination(self):
        temporary, root = self.make_repository()
        with temporary:
            plan = self.planned(root)
            baseline = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file() and ".git" not in p.parts}
            os.environ["PUBLISH_GUIDE_FAIL_AFTER_REPLACE"] = "2"
            try: code, _, _ = self.run_main(root, "--write", "--confirm-plan", plan.digest)
            finally: os.environ.pop("PUBLISH_GUIDE_FAIL_AFTER_REPLACE")
            self.assertEqual(code, 2)
            after = {p.relative_to(root): p.read_bytes() for p in root.rglob("*") if p.is_file() and ".git" not in p.parts}
            self.assertEqual(after, baseline)

    def test_write_rejects_dirty_worktree_and_incorrect_or_stale_digest(self):
        temporary, root = self.make_repository()
        with temporary:
            plan = self.planned(root)
            code, _, error = self.run_main(root, "--write", "--confirm-plan", "wrong")
            self.assertEqual(code, 2); self.assertIn("incorrect or stale", error)
            (root / "unrelated.txt").write_text("dirty\n", encoding="utf-8")
            code, _, error = self.run_main(root, "--write", "--confirm-plan", plan.digest)
            self.assertEqual(code, 2); self.assertIn("clean Git worktree", error)
            subprocess.run(["git", "checkout", "--", "unrelated.txt"], cwd=root, check=True)
            catalog = json.loads((root / "data/hub-asset.json").read_text(encoding="utf-8")); catalog[0]["note"] = "changed"
            (root / "data/hub-asset.json").write_text(json.dumps(catalog), encoding="utf-8")
            code, _, error = self.run_main(root, "--write", "--confirm-plan", plan.digest)
            self.assertEqual(code, 2); self.assertIn("incorrect or stale", error)


if __name__ == "__main__":
    unittest.main()
