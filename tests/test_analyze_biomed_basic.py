import contextlib
import io
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from analyze_biomed_basic import InputError, build_report, main, parse_input  # noqa: E402
from prepare_biomed_publication import RELATED  # noqa: E402


class BiomedBasicAnalyzerTests(unittest.TestCase):
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
        landing = (ROOT / "biomed-basics.html").read_text(encoding="utf-8")
        self.assertEqual(landing.count(f"biomed-basics/{slug}.html"), 1)
        hero = re.search(r'<section class="hero">(.*?)</section>', landing, re.S).group(1)
        grid = re.search(r'<div class="guides-grid">(.*?)</div>\s*</section>', landing, re.S).group(1)
        self.assertNotIn(f"biomed-basics/{slug}.html", hero)
        self.assertIn(f"biomed-basics/{slug}.html", grid)
        self.assertEqual((ROOT / "sitemap.xml").read_text(encoding="utf-8").count(f"biomed-basics/{slug}.html"), 1)

    def test_vendor_article_is_registered_in_grid_and_preserves_key_copy(self):
        slug = "how-to-think-before-calling-a-vendor"
        page = (ROOT / "biomed-basics" / f"{slug}.html").read_text(encoding="utf-8")
        self.assertIn("What is the device supposed to be doing?", page)
        self.assertIn("A practical troubleshooting mindset for biomeds", page)
        landing = (ROOT / "biomed-basics.html").read_text(encoding="utf-8")
        self.assertEqual(landing.count(f"biomed-basics/{slug}.html"), 1)
        hero = re.search(r'<section class="hero">(.*?)</section>', landing, re.S).group(1)
        grid = re.search(r'<div class="guides-grid">(.*?)</div>\s*</section>', landing, re.S).group(1)
        self.assertNotIn(f"biomed-basics/{slug}.html", hero)
        self.assertIn(f"biomed-basics/{slug}.html", grid)
        self.assertEqual((ROOT / "sitemap.xml").read_text(encoding="utf-8").count(f"biomed-basics/{slug}.html"), 1)

    def test_published_articles_are_removed_from_planned_topics(self):
        landing = (ROOT / "biomed-basics.html").read_text(encoding="utf-8")
        planned = re.search(
            r'<h3>Planned Topics</h3>.*?<ul>(.*?)</ul>', landing, re.S
        ).group(1)
        self.assertNotIn("When to remove medical equipment from service", planned)
        self.assertNotIn("How to think before calling a vendor", planned)
        self.assertIn("What HL7 means in plain English", planned)


if __name__ == "__main__":
    unittest.main()
