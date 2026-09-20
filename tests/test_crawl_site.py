import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from crawl_site import crawl
from generate_sitemap import BASE_URL, render_sitemap


class CrawlTests(unittest.TestCase):
    def test_reports_real_same_site_failures_and_ignores_fixtures(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "tests").mkdir()
            (root / "tests/fixture.html").write_text("<title>Ignored</title>", encoding="utf-8")
            for name in ("index.html", "guide.html"):
                canonical = BASE_URL + ("/" if name == "index.html" else "/guide.html")
                html = f'''<title>Duplicate</title><meta name="viewport" content="width=device-width">
                <meta name="description" content="Resource"><link rel="canonical" href="{canonical}">
                <h1>Resource</h1><a href="https://jaketroubleshoots.com/guide.html#target">Guide</a>
                <a href="/guide.html?filter=example#missing">Missing fragment</a><a href="mailto:a@b.test">Email</a>
                <img src="missing.png"><p id="target">Content</p>'''
                (root / name).write_text(html, encoding="utf-8")
            (root / "robots.txt").write_text(f"Sitemap: {BASE_URL}/missing.xml\n", encoding="utf-8")
            (root / "sitemap.xml").write_text(render_sitemap(root), encoding="utf-8")
            result = crawl(root)
            self.assertEqual(result["pages"], 2)
            self.assertEqual(result["counts"]["broken_links"], 2)
            self.assertEqual(result["counts"]["broken_fragments"], 2)
            self.assertEqual(result["counts"]["duplicate_titles"], 1)
            self.assertEqual(result["counts"]["broken_robots_sitemap"], 1)
            self.assertEqual(result["counts"].get("canonical_mismatch", 0), 0)
            self.assertEqual(result["counts"]["unexpected_sitemap_entries"], 0)


if __name__ == "__main__":
    unittest.main()
