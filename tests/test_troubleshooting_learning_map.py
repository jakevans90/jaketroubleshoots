import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TroubleshootingLearningMapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mapping = json.loads((ROOT / "data" / "troubleshooting-learning-map.json").read_text(encoding="utf-8"))
        cls.articles = json.loads((ROOT / "data" / "biomed-basics.json").read_text(encoding="utf-8"))
        cls.assets = json.loads((ROOT / "data" / "hub-asset.json").read_text(encoding="utf-8"))

    def resolve(self, value):
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            return self.mapping.get("articleSets", {}).get(value)
        return None

    def test_every_asset_type_has_a_mapping(self):
        expected = {asset["slug"] for asset in self.assets}
        actual = set(self.mapping["assetTypeDefaults"])
        self.assertEqual(expected, actual)

    def test_display_names_resolve_through_the_canonical_asset_slug(self):
        mappings = self.mapping["assetTypeDefaults"]
        for asset in self.assets:
            with self.subTest(asset=asset["name"]):
                self.assertIn(asset["slug"], mappings)
                self.assertIsNotNone(self.resolve(mappings[asset["slug"]]))

    def test_every_mapping_resolves_to_three_to_five_published_articles(self):
        published = {article["slug"] for article in self.articles}
        for asset, configured in self.mapping["assetTypeDefaults"].items():
            with self.subTest(asset=asset):
                resolved = self.resolve(configured)
                self.assertIsInstance(resolved, list)
                self.assertGreaterEqual(len(resolved), 3)
                self.assertLessEqual(len(resolved), 5)
                self.assertEqual(len(resolved), len(set(resolved)))
                self.assertTrue(set(resolved) <= published)

    def test_article_sets_only_reference_published_articles(self):
        published = {article["slug"] for article in self.articles}
        for name, articles in self.mapping["articleSets"].items():
            with self.subTest(article_set=name):
                self.assertGreaterEqual(len(articles), 3)
                self.assertLessEqual(len(articles), 5)
                self.assertEqual(len(articles), len(set(articles)))
                self.assertTrue(set(articles) <= published)


if __name__ == "__main__":
    unittest.main()
