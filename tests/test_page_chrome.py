import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from page_chrome import normalize_icon_links, normalize_page_chrome


class PageChromeTests(unittest.TestCase):
    def page(self):
        return ('<html><head><meta charset="UTF-8"></head><body><header>Nav</header>'
                '<section class="hero"><h2>Exact Device</h2><p>Original issue</p></section>'
                '<main><h3>Model</h3><p>Exact Device</p>' + ''.join(
                    f'<h2>{title}</h2><p>Do not change: 0.5 mA &amp; 12 months.</p>'
                    for title in ['Safety', 'Steps', 'Verification', 'Documentation']) + '</main></body></html>')

    def test_chrome_is_idempotent_and_preserves_technical_content(self):
        source = self.page()
        result = normalize_page_chrome(source, detail=True)
        self.assertEqual(result, normalize_page_chrome(result, detail=True))
        self.assertEqual(re.findall(r'<p>.*?</p>', source), re.findall(r'<p>.*?</p>', result))
        self.assertIn('<h1 id="page-heading" tabindex="-1">Exact Device</h1>', result)
        self.assertIn('width=device-width, initial-scale=1', result)
        self.assertIn('href="#section-verification"', result)

    def test_exact_catalog_links_only(self):
        hubs = {'Model': [{'name': 'Exact Device', 'url': 'hub-model.html?slug=exact-device', 'flags': {'exists': True}}]}
        result = normalize_page_chrome(self.page(), detail=True, hubs=hubs)
        self.assertIn('<a href="/hub-model.html?slug=exact-device">Exact Device</a>', result)
        self.assertEqual(result, normalize_page_chrome(result, detail=True, hubs=hubs))
        hubs['Model'][0]['name'] = 'EXACT DEVICE'
        self.assertNotIn('hub-model.html', normalize_page_chrome(self.page(), detail=True, hubs=hubs))

    def test_existing_identifiers_viewport_and_newline_preserved(self):
        source = self.page().replace('<h2>Exact Device</h2>', '<h1 id="hub-name">Exact Device</h1>').replace('<head>', '<head>\r\n<meta name="viewport" content="width=device-width">')
        result = normalize_page_chrome(source)
        self.assertIn('href="#hub-name"', result)
        self.assertEqual(result.count('name="viewport"'), 1)
        self.assertNotIn('page-toc', result)

    def test_duplicate_section_names_get_unique_targets(self):
        source = self.page().replace('<h2>Steps</h2>', '<h2>Safety</h2>')
        result = normalize_page_chrome(source, detail=True)
        self.assertIn('href="#section-safety-2"', result)
        self.assertEqual(result, normalize_page_chrome(result, detail=True))

    def test_legacy_pages_without_charset_get_viewport_and_language(self):
        source = self.page().replace('<meta charset="UTF-8">', '')
        result = normalize_page_chrome(source)
        self.assertIn('<meta charset="UTF-8">', result)
        self.assertIn('name="viewport"', result)
        self.assertIn('<html lang="en">', result)
        self.assertEqual(result, normalize_page_chrome(result))

    def test_existing_section_navigation_is_preserved_without_duplicate_toc(self):
        source = self.page().replace('<main>', '<main><h3>Jump to a Section</h3>')
        result = normalize_page_chrome(source, detail=True)
        self.assertNotIn('class="page-toc"', result)

    def test_broken_pm_icon_bundle_uses_existing_site_icon(self):
        source = ('<head><link rel="icon" type="image/png" href="../images/favicon-96x96.png" sizes="96x96">'
                  '<link rel="icon" type="image/svg+xml" href="../images/favicon.svg">'
                  '<link rel="shortcut icon" href="../favicon.ico">'
                  '<link rel="apple-touch-icon" sizes="180x180" href="../images/apple-touch-icon.png"></head>')
        result = normalize_icon_links(source)
        self.assertIn('<link rel="icon" type="image/x-icon" href="../images/favicon.ico">', result)
        self.assertNotIn('favicon-96x96.png', result)
        self.assertNotIn('favicon.svg', result)
        self.assertNotIn('apple-touch-icon.png', result)
        self.assertEqual(result, normalize_icon_links(result))
