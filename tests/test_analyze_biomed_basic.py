import contextlib
import io
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from analyze_biomed_basic import InputError, build_report, main, parse_input  # noqa: E402
from prepare_biomed_publication import RELATED, biomed_group, remove_published_planned_topics  # noqa: E402


class BiomedBasicAnalyzerTests(unittest.TestCase):
    def biomed_catalog(self):
        return json.loads((ROOT / "data" / "biomed-basics.json").read_text(encoding="utf-8"))

    def write_input(self, directory: Path, title="Ground Fault Basics", slug="") -> Path:
        slug_line = f"slug: \"{slug}\"\n" if slug else ""
        path = directory / "article.md"
        path.write_text(
            f'''---\ntitle: "{title}"\n{slug_line}description: "Ground resistance and leakage current explained."\ncategory: "Electrical Safety"\n---\n\n## Overview\n\nProtective earth and leakage current matter during electrical safety testing.\n''',
            encoding="utf-8",
        )
        return path

    def make_site(self):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        (root / "biomed-basics").mkdir()
        (root / "biomed-basics.html").write_text("landing\n", encoding="utf-8")
        (root / "sitemap.xml").write_text("sitemap\n", encoding="utf-8")
        (root / "search.html").write_text("search\n", encoding="utf-8")
        (root / "biomed-basics/electrical-safety.html").write_text(
            "<h2>Electrical Safety Testing</h2><p>Protective earth, ground resistance, and leakage current.</p>",
            encoding="utf-8",
        )
        return temporary, root

    def test_derives_slug_and_related_article(self):
        temporary, root = self.make_site()
        self.addCleanup(temporary.cleanup)
        input_path = self.write_input(root)
        article = parse_input(input_path)
        report, ready = build_report(article, root)
        self.assertEqual(article.slug, "ground-fault-basics")
        self.assertTrue(ready)
        self.assertIn("biomed-basics/ground-fault-basics.html", report)
        self.assertIn("biomed-basics/electrical-safety.html", report)
        self.assertIn("No search data file exists", report)

    def test_duplicate_target_blocks(self):
        temporary, root = self.make_site()
        self.addCleanup(temporary.cleanup)
        input_path = self.write_input(root, slug="electrical-safety")
        report, ready = build_report(parse_input(input_path), root)
        self.assertFalse(ready)
        self.assertIn("target already exists", report)

    def test_main_does_not_modify_site_files(self):
        temporary, root = self.make_site()
        self.addCleanup(temporary.cleanup)
        input_path = self.write_input(root)
        before = {path: path.read_bytes() for path in root.rglob("*") if path.is_file()}
        with contextlib.redirect_stdout(io.StringIO()):
            code = main([str(input_path), "--root", str(root)])
        after = {path: path.read_bytes() for path in root.rglob("*") if path.is_file()}
        self.assertEqual(code, 0)
        self.assertEqual(before, after)

    def test_rejects_unknown_front_matter(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.md"
            path.write_text("---\ntitle: Test\nuncontrolled: yes\n---\nBody\n", encoding="utf-8")
            with self.assertRaises(InputError):
                parse_input(path)

    def test_accepts_plain_pasted_markdown(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pasted.md"
            path.write_text(
                "# When to Remove Medical Equipment From Service\n\n"
                "## Knowing when troubleshooting needs to stop\n\n"
                "A practical guide to recognizing safety concerns.\n",
                encoding="utf-8",
            )
            article = parse_input(path)
            self.assertEqual(article.title, "When to Remove Medical Equipment From Service")
            self.assertEqual(article.slug, "when-to-remove-medical-equipment-from-service")
            self.assertEqual(article.description, "A practical guide to recognizing safety concerns.")

    def test_published_related_sections_have_five_valid_unique_links(self):
        for slug, expected in RELATED.items():
            path = ROOT / "biomed-basics" / f"{slug}.html"
            source = path.read_text(encoding="utf-8")
            section = re.search(
                r'<h3>Related Biomed Basics</h3>\s*<ul>(.*?)</ul>', source, re.S
            )
            self.assertIsNotNone(section, slug)
            hrefs = re.findall(r'href="([^"]+\.html)"', section.group(1))
            self.assertEqual(hrefs, [f"{target}.html" for target in expected], slug)
            self.assertEqual(len(hrefs), 5, slug)
            self.assertEqual(len(set(hrefs)), 5, slug)
            self.assertNotIn(f"{slug}.html", hrefs, slug)
            for href in hrefs:
                self.assertTrue((ROOT / "biomed-basics" / href).is_file(), f"{slug}: {href}")

    def test_new_article_is_registered_once_and_preserves_key_copy(self):
        slug = "when-to-remove-medical-equipment-from-service"
        page = (ROOT / "biomed-basics" / f"{slug}.html").read_text(encoding="utf-8")
        self.assertIn("Do I have enough confidence in this device to put it back on a patient?", page)
        self.assertIn("A practical guide to recognizing safety concerns", page)
        self.assertIn('href="#the-simple-version"', page)
        matches = [item for item in self.biomed_catalog() if item["slug"] == slug]
        self.assertEqual(len(matches), 1)
        self.assertEqual((ROOT / "sitemap.xml").read_text(encoding="utf-8").count(f"biomed-basics/{slug}.html"), 1)

    def test_vendor_article_is_registered_in_grid_and_preserves_key_copy(self):
        slug = "how-to-think-before-calling-a-vendor"
        page = (ROOT / "biomed-basics" / f"{slug}.html").read_text(encoding="utf-8")
        self.assertIn("What is the device supposed to be doing?", page)
        self.assertIn("A practical troubleshooting mindset for biomeds", page)
        matches = [item for item in self.biomed_catalog() if item["slug"] == slug]
        self.assertEqual(len(matches), 1)
        self.assertEqual((ROOT / "sitemap.xml").read_text(encoding="utf-8").count(f"biomed-basics/{slug}.html"), 1)

    def test_published_articles_are_removed_from_planned_topics(self):
        landing = (ROOT / "biomed-basics.html").read_text(encoding="utf-8")
        planned = re.search(
            r'<section class="content-box planned-topics-section">(.*?)</section>\s*</div>\s*</section>', landing, re.S
        ).group(1)
        self.assertNotIn("When to remove medical equipment from service", planned)
        self.assertNotIn("How to think before calling a vendor", planned)
        self.assertNotIn("What HL7 means in plain English", planned)
        self.assertNotIn("Nurse call integration basics", planned)
        self.assertNotIn("How to Read a Medical Equipment Service Manual", planned)
        self.assertNotIn("How to Reproduce a Clinical Complaint on the Bench", planned)
        self.assertNotIn("How to Use a Multimeter in Biomed", planned)
        self.assertNotIn("What “Known-Good” Actually Means", planned)
        self.assertNotIn("Fuses, Breakers, and Power Supplies", planned)
        self.assertNotIn("Voltage, Current, Resistance, and Continuity in Plain English", planned)
        self.assertNotIn("Sensors and Transducers Basics", planned)
        self.assertNotIn("Relays and Contact Closures in Plain English", planned)
        self.assertNotIn("Preserving Device Logs After a Serious Event", planned)
        self.assertNotIn("What to Do When a Medical Device Is Involved in an Incident", planned)
        self.assertNotIn("How to Avoid Confirmation Bias While Troubleshooting", planned)
        self.assertNotIn("When to Trust the Device's Internal Self-Test", planned)
        self.assertNotIn("Why Changing One Thing at a Time Matters", planned)
        self.assertNotIn("Ground, Neutral, and Hot in Medical Equipment", planned)
        self.assertNotIn("Error Codes: What They Tell You and What They Don't", planned)
        self.assertNotIn("What “Unable to Duplicate” Should Actually Mean", planned)
        self.assertNotIn("Connectors, Pins, and Strain Relief", planned)
        self.assertNotIn("How to Troubleshoot a Device That Will Not Power On", planned)
        self.assertNotIn("Alarm troubleshooting basics", planned)
        self.assertNotIn("Software, Firmware, and Configuration: What's the Difference?", planned)
        self.assertNotIn("Medical Device Logs: What to Look For", planned)
        self.assertNotIn("How to Prove a Repair Before Return to Service", planned)
        self.assertNotIn("How to Troubleshoot Communication Failures", planned)
        self.assertNotIn("How to Troubleshoot Charging Problems", planned)
        self.assertNotIn("The Troubleshooting Process: Observe, Isolate, Test, Verify", planned)
        self.assertNotIn("The Difference Between a Symptom, Cause, and Root Cause", planned)
        self.assertNotIn("How Experienced Biomeds Think Through a New Problem", planned)
        self.assertNotIn("How to Read a Troubleshooting Flowchart", planned)
        self.assertNotIn("AC vs DC Power Basics", planned)
        self.assertNotIn("Analog vs Digital Signals", planned)
        self.assertNotIn("Medical Device Batteries: Runtime, Capacity, and State of Health", planned)
        self.assertNotIn("How to Read Device Specifications", planned)
        self.assertNotIn("Tolerance vs Accuracy", planned)
        self.assertNotIn("How to Compare Your Test Result to Manufacturer Specification", planned)
        self.assertNotIn("Pass/Fail Limits and Why the Test Point Matters", planned)
        self.assertNotIn("How NIBP Works in a Patient Monitor", planned)
        self.assertNotIn("How SpO2 Measurement Works", planned)
        self.assertNotIn("How ECG Acquisition Works", planned)
        self.assertNotIn("How Sidestream CO2 Monitoring Works", planned)
        self.assertNotIn("How Ventilator Flow Sensors Work", planned)
        self.assertNotIn("How Ventilator Pressure Sensors Work", planned)
        self.assertNotIn("How Medical Equipment Measures Pressure", planned)
        self.assertNotIn("How Medical Equipment Measures Flow", planned)
        self.assertNotIn("How Invasive Blood Pressure Monitoring Works", planned)
        self.assertNotIn("How Oxygen Sensors Work in Ventilators and Anesthesia Machines", planned)
        self.assertNotIn("How an Anesthesia Machine Breathing System Works", planned)
        self.assertNotIn("How Anesthesia Waste Gas Scavenging Works", planned)
        self.assertNotIn("How a Ventilator Measures Tidal Volume", planned)
        self.assertNotIn("How PEEP Is Generated and Controlled", planned)
        self.assertNotIn("How Infusion Pump Occlusion Detection Works", planned)
        self.assertNotIn("How Infusion Pumps Measure or Control Flow", planned)
        self.assertNotIn("How Defibrillators Charge and Deliver Energy", planned)
        self.assertNotIn("How Medical Device Batteries Charge and Communicate", planned)
        self.assertNotIn("How Smart Batteries Communicate With Medical Equipment", planned)
        self.assertNotIn("How Parameter Modules Communicate With Host Monitors", planned)
        self.assertNotIn("How Patient Monitors Communicate With Central Stations", planned)
        self.assertNotIn("How ECG Lead-Off Detection Works", planned)
        self.assertNotIn("How Mainstream CO2 Monitoring Works", planned)
        self.assertNotIn("How Medical Gas Sampling Systems Work", planned)
        self.assertIn("How an Anesthesia Vaporizer Works", planned)
        self.assertIn("How Temperature Probes and Thermistors Work", planned)
        self.assertIn("<strong>78</strong>", planned)

    def test_latest_articles_are_registered_once_and_preserve_key_copy(self):
        expected = {
            "how-to-read-a-medical-equipment-service-manual": "Theory of Operation",
            "how-to-reproduce-a-clinical-complaint-on-the-bench": "The bench is not the clinical environment",
            "how-to-use-a-multimeter-in-biomed": "Do Not Measure Resistance on a Powered Circuit",
            "what-known-good-actually-means": "Known-good status should come from evidence",
            "fuses-breakers-and-power-supplies-in-medical-equipment": "A Blown Fuse Is Usually a Symptom",
            "voltage-current-resistance-and-continuity-in-plain-english": "Voltage is electrical potential difference",
            "sensors-and-transducers-basics": "A sensor detects something physical",
            "relays-and-contact-closures-in-plain-english": "A relay is controlled electrically",
            "preserving-device-logs-after-a-serious-event": "Do Not “Test It a Few Times” First",
            "what-to-do-when-a-medical-device-is-involved-in-an-incident": "This Is Not a Normal Work Order",
            "how-to-avoid-confirmation-bias-while-troubleshooting": "A Hypothesis Is Not a Diagnosis",
            "when-to-trust-the-device-s-internal-self-test": "What exactly just passed?",
            "why-changing-one-thing-at-a-time-matters": "Troubleshooting Is an Experiment",
            "ground-neutral-and-hot-in-medical-equipment": "Ground Is Not a Backup Neutral",
            "error-codes-what-they-tell-you-and-what-they-don-t": "Error Condition vs Root Cause",
            "what-unable-to-duplicate-should-actually-mean": "“Powers On” Is Not a Reproduction Attempt",
            "medical-equipment-cables-and-connectors-inspection-and-isolation": "Failure Follows the Cable",
            "how-to-troubleshoot-medical-device-accessories": "Does the problem follow the accessory",
            "how-to-isolate-device-vs-accessory-vs-infrastructure-problems": "The Last Known-Good Point",
            "medical-equipment-power-troubleshooting-outlet-to-internal-supply": "Where does the power stop?",
            "medical-device-alarm-troubleshooting-fundamentals": "Alarm Condition vs Alarm-System Failure",
            "environmental-causes-of-medical-equipment-failures": "Environment Can Expose an Internal Fault",
            "software-firmware-and-configuration-problems-in-medical-equipment": "Reboot Is a Result, Not Always a Repair",
            "how-to-read-and-use-medical-device-event-logs": "Logs Show What the Device Saw",
            "how-to-verify-a-repair-before-returning-equipment-to-service": "Repair Is Not Verification",
            "how-to-troubleshoot-communication-failures": "Find the Last Known-Good Point",
            "how-to-troubleshoot-charging-problems": "Battery Not Charging vs Short Runtime",
            "the-troubleshooting-process-observe-isolate-test-verify": "The Most Important Question",
            "the-difference-between-a-symptom-cause-and-root-cause": "Do Not Repair the Symptom",
            "how-experienced-biomeds-think-through-a-new-problem": "Ask What Still Works",
            "how-to-read-a-troubleshooting-flowchart": "A Decision Point Is a Question",
            "ac-vs-dc-power-basics": "AC From the Wall, DC Inside the Device",
            "analog-vs-digital-signals": "Continuity Is Not Signal Quality",
            "medical-device-batteries-runtime-capacity-and-state-of-health": "State of Charge Does Not Tell You Battery Health",
            "how-to-read-device-specifications": "Range Is Not Accuracy",
            "tolerance-vs-accuracy": "Tolerance Creates the Pass/Fail Window",
            "how-to-compare-your-test-result-to-manufacturer-specification": "Apply the Limit Before Looking at the Result",
            "pass-fail-limits-and-why-the-test-point-matters": "Multiple Points Reveal Error Patterns",
            "how-nibp-works-in-a-patient-monitor": "Oscillometric Measurement",
            "how-spo2-measurement-works": "AC and DC Components of the Optical Signal",
            "how-ecg-acquisition-works": "Common-Mode Rejection",
            "how-sidestream-co2-monitoring-works": "Pump Running Does Not Mean Flow Is Good",
            "how-ventilator-flow-sensors-work": "Flow Sensor Calibration Failure",
            "how-ventilator-pressure-sensors-work": "Pressure Control vs Pressure Measurement",
            "how-medical-equipment-measures-pressure": "Leak Test vs Accuracy Test",
            "how-medical-equipment-measures-flow": "Estimated Flow vs Measured Flow",
            "how-invasive-blood-pressure-monitoring-works": "Zeroing vs Leveling",
            "how-oxygen-sensors-work-in-ventilators-and-anesthesia-machines": "The Sensor Consumes Itself",
            "how-an-anesthesia-machine-breathing-system-works": "Fresh Gas Is Not the Entire Breath",
            "how-anesthesia-waste-gas-scavenging-works": "The Breathing System and Scavenging System Are Different",
            "how-a-ventilator-measures-tidal-volume": "Set Volume Is Not Measured Volume",
            "how-peep-is-generated-and-controlled": "Measurement Error vs Control Error",
            "how-infusion-pump-occlusion-detection-works": "Alarm Threshold Is Not Alarm Time",
            "how-infusion-pumps-measure-or-control-flow": "Programmed Flow vs Measured Flow",
            "how-defibrillators-charge-and-deliver-energy": "Set Energy vs Delivered Energy",
            "how-medical-device-batteries-charge-and-communicate": "AC Input Does Not Mean Battery Is Charging",
            "how-smart-batteries-communicate-with-medical-equipment": "Power Can Still Work",
            "how-parameter-modules-communicate-with-host-monitors": "Measurement and Display Are Separate",
            "how-patient-monitors-communicate-with-central-stations": "Central Monitoring Is Not Just Screen Mirroring",
            "how-ecg-lead-off-detection-works": "Lead-Off Is Different From Noisy ECG",
            "how-mainstream-co2-monitoring-works": "The Adapter Is Part of the Measurement System",
            "how-medical-gas-sampling-systems-work": "Pump Running Does Not Prove Sample Flow",
        }
        catalog = self.biomed_catalog()
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")

        for slug, key_copy in expected.items():
            page = (ROOT / "biomed-basics" / f"{slug}.html").read_text(encoding="utf-8")
            self.assertIn(key_copy, page)
            self.assertEqual(sum(item["slug"] == slug for item in catalog), 1)
            self.assertEqual(sitemap.count(f"biomed-basics/{slug}.html"), 1)

    def test_biomed_catalog_is_complete_and_landing_loads_it(self):
        catalog = self.biomed_catalog()
        slugs = [item["slug"] for item in catalog]
        self.assertEqual(len(catalog), 76)
        self.assertEqual(len(slugs), len(set(slugs)))
        self.assertEqual(set(slugs), set(RELATED))
        for item in catalog:
            self.assertEqual(item["url"], f'biomed-basics/{item["slug"]}.html')
            self.assertTrue((ROOT / item["url"]).is_file())
            self.assertIn(item["group"], {
                "start-here", "everyday-skills", "connected-systems",
                "career-communication", "troubleshooting-safety", "how-it-works",
            })
        landing = (ROOT / "biomed-basics.html").read_text(encoding="utf-8")
        self.assertIn("fetch('data/biomed-basics.json')", landing)
        self.assertIn('id="biomed-article-groups"', landing)
        self.assertNotIn('class="guide-card basics-card" data-biomed-group=', landing.split("<script>", 1)[0])

    def test_planned_topic_removal_works_across_cards_and_updates_count(self):
        landing = '''<section class="content-box planned-topics-section">
          <div class="planned-topic-count" aria-label="2 planned articles"><strong>2</strong></div>
          <h3>Planned Topics</h3>
          <div class="planned-topics-grid">
            <section><ul><li>First Topic</li></ul></section>
            <section><ul><li>Second Topic</li></ul></section>
          </div>
        </section>'''
        cleaned = remove_published_planned_topics(landing, {"Second Topic"})
        self.assertIn("First Topic", cleaned)
        self.assertNotIn("Second Topic", cleaned)
        self.assertIn('aria-label="1 planned articles"', cleaned)
        self.assertIn("<strong>1</strong>", cleaned)

    def test_new_article_categories_map_to_landing_page_groups(self):
        self.assertEqual(biomed_group("How It Works"), "how-it-works")
        self.assertEqual(biomed_group("Integration"), "connected-systems")
        self.assertEqual(biomed_group("Electrical Safety"), "start-here")
        self.assertEqual(biomed_group("Safety & Risk"), "troubleshooting-safety")
        self.assertEqual(biomed_group("Documentation"), "everyday-skills")

    def test_integration_batch_is_registered_once_and_preserves_key_copy(self):
        expected = {
            "what-hl7-means-in-plain-english": "HL7 Is Not the Network",
            "nurse-call-integration-basics": "The Device Is Often Just Providing a Signal",
        }
        catalog = self.biomed_catalog()
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        for slug, preserved_copy in expected.items():
            page = (ROOT / "biomed-basics" / f"{slug}.html").read_text(encoding="utf-8")
            self.assertIn(preserved_copy, page)
            self.assertEqual(sum(item["slug"] == slug for item in catalog), 1)
            self.assertEqual(sitemap.count(f"biomed-basics/{slug}.html"), 1)


if __name__ == "__main__":
    unittest.main()
