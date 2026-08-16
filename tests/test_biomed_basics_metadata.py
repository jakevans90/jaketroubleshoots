import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class BiomedBasicsMetadataTests(unittest.TestCase):
    def test_every_published_article_has_valid_last_revision(self):
        articles = json.loads((ROOT / "data" / "biomed-basics.json").read_text(encoding="utf-8"))

        self.assertTrue(articles)
        for article in articles:
            with self.subTest(slug=article.get("slug")):
                self.assertRegex(article.get("lastRevision", ""), r"^\d{4}-\d{2}-\d{2}$")
                self.assertTrue((ROOT / article["url"]).is_file())


if __name__ == "__main__":
    unittest.main()
