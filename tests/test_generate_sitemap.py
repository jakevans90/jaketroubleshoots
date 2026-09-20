import sys
import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from generate_sitemap import BASE_URL, main, production_html_files, render_sitemap, sitemap_urls


class SitemapTests(unittest.TestCase):
    def test_only_published_libraries_are_discovered(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            public = ["index.html", "search.html", "guides/device-error.html",
                      "preventive-maintenance/device.html", "biomed-basics/networking.html"]
            private = ["tests/fixtures/guide.html", "reports/preview.html",
                       "incoming-guides/draft.html", ".publish-stage/guide.html",
                       "node_modules/example/index.html", "guides/.draft.html",
                       "guides/staging/draft.html"]
            for relative in public + private:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("<!doctype html><title>Fixture</title>", encoding="utf-8")
            self.assertEqual({p.relative_to(root).as_posix() for p in production_html_files(root)}, set(public))
            self.assertEqual(sitemap_urls(root)[0], BASE_URL + "/")
            self.assertNotIn(BASE_URL + "/index.html", sitemap_urls(root))

    def test_xml_is_escaped_and_output_is_deterministic_utf8(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text("", encoding="utf-8")
            (root / "device&accessory.html").write_text("", encoding="utf-8")
            xml = render_sitemap(root)
            parsed = ElementTree.fromstring(xml)
            urls = [element.text for element in parsed.findall(".//{*}loc")]
            self.assertEqual(urls, sitemap_urls(root))
            self.assertIn("device&amp;accessory.html", xml)
            self.assertEqual(main(["--root", directory]), 0)
            self.assertEqual((root / "sitemap.xml").read_text(encoding="utf-8"), xml)

    def test_robots_points_to_existing_sitemap(self):
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn(f"Sitemap: {BASE_URL}/sitemap.xml", robots)
        self.assertTrue((ROOT / "sitemap.xml").is_file())


if __name__ == "__main__":
    unittest.main()
