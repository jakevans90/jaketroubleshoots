import os
import sys
import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from generate_sitemap import (
    BASE_URL,
    SITEMAP_EXCLUDED_PATHS,
    main,
    production_html_files,
    render_sitemap,
    sitemap_urls,
)


class SitemapTests(unittest.TestCase):
    @staticmethod
    def _write_path(path, text):
        resolved = path.resolve()
        if os.name == "nt":
            resolved = Path("\\\\?\\" + str(resolved))
        resolved.write_text(text, encoding="utf-8")

    def test_only_published_libraries_are_discovered(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            public = ["index.html", "search.html", "guides/device-error.html",
                      "preventive-maintenance/device.html", "biomed-basics/networking.html",
                      "directory/troubleshooting-guides-001.html"]
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

    def test_long_windows_guide_path_is_not_omitted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            guides = root / "guides"
            guides.mkdir()
            filename = "guide-" + ("long-name-" * 20) + ".html"
            target = guides / filename
            self._write_path(target, "<!doctype html><title>Long path</title>")
            try:
                self.assertIn(target, production_html_files(root))
                self.assertIn(f"{BASE_URL}/guides/{filename}", sitemap_urls(root))
            finally:
                resolved = target.resolve()
                if os.name == "nt":
                    resolved = Path("\\\\?\\" + str(resolved))
                resolved.unlink()

    def test_robots_points_to_existing_sitemap(self):
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn(f"Sitemap: {BASE_URL}/sitemap.xml", robots)
        self.assertTrue((ROOT / "sitemap.xml").is_file())

    def test_legacy_redirect_remains_public_but_is_not_in_sitemap(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            legacy = next(iter(SITEMAP_EXCLUDED_PATHS))
            for relative in (legacy, "guides/ge-mac-vu360-leads-noisy.html"):
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("<!doctype html><title>Fixture</title>", encoding="utf-8")
            published = {path.relative_to(root).as_posix() for path in production_html_files(root)}
            self.assertIn(legacy, published)
            self.assertNotIn(f"{BASE_URL}/{legacy}", sitemap_urls(root))
            self.assertIn(f"{BASE_URL}/guides/ge-mac-vu360-leads-noisy.html", sitemap_urls(root))


if __name__ == "__main__":
    unittest.main()
