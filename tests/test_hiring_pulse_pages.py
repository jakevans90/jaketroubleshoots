import importlib.util
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
SPEC = importlib.util.spec_from_file_location("build_hiring_pulse_pages", ROOT / "tools" / "build_hiring_pulse_pages.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class HiringPulsePagesTests(unittest.TestCase):
    def test_generated_pages_are_current_and_selective(self):
        self.assertTrue(MODULE.build(ROOT, check=True))
        snapshot = MODULE.public.pulse.load_json(ROOT / MODULE.public.PUBLIC_PATH)
        directory = (ROOT / MODULE.DIRECTORY / "index.html").read_text(encoding="utf-8")
        self.assertEqual(4, len(MODULE.PAGES))
        for slug, title, criteria in MODULE.PAGES:
            matches = MODULE.matching(snapshot["postings"], criteria)
            page = (ROOT / MODULE.DIRECTORY / f"{slug}.html").read_text(encoding="utf-8")
            self.assertEqual(len(matches) >= MODULE.MIN_LISTINGS, f'{slug}.html' in directory)
            self.assertIn(f'<h1 id="page-heading">{title}</h1>', page)
            self.assertEqual(len(matches) if len(matches) >= MODULE.MIN_LISTINGS else 0, page.count('<article class="jobs-employer-card">'))
            self.assertNotIn('content="noindex,follow"', page) if len(matches) >= MODULE.MIN_LISTINGS else self.assertIn('content="noindex,follow"', page)
            self.assertTrue(all(item["freshness"] == "recent" for item in matches))

    def test_sitemap_contains_only_eligible_pages_once(self):
        snapshot = MODULE.public.pulse.load_json(ROOT / MODULE.public.PUBLIC_PATH)
        locations = [item.text for item in ET.parse(ROOT / "sitemap.xml").iter() if item.tag.endswith("loc")]
        prefix = MODULE.BASE + "htm-jobs/"
        actual = [url for url in locations if url.startswith(prefix)]
        expected = [prefix] + [prefix + slug + ".html" for slug, _, criteria in MODULE.PAGES if len(MODULE.matching(snapshot["postings"], criteria)) >= MODULE.MIN_LISTINGS]
        self.assertEqual(sorted(expected), sorted(actual))
        self.assertEqual(len(actual), len(set(actual)))

    def test_thin_page_is_noindexed_without_fake_listings(self):
        rendered = MODULE.render_page("test", "Test Jobs", [], "2026-11-24T12:00:00Z").decode("utf-8")
        self.assertIn('content="noindex,follow"', rendered)
        self.assertNotIn('<article class="jobs-employer-card">', rendered)


if __name__ == "__main__":
    unittest.main()
