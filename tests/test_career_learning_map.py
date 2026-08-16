import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CareerLearningMapTests(unittest.TestCase):
    def test_every_mapped_slug_is_a_published_biomed_basic(self):
        articles = json.loads((ROOT / "data" / "biomed-basics.json").read_text(encoding="utf-8"))
        mapping = json.loads((ROOT / "data" / "career-learning-map.json").read_text(encoding="utf-8"))
        published = {article["slug"] for article in articles}
        mapped = [
            *mapping.get("educationPage", []),
            *(slug for slugs in mapping.get("certifications", {}).values() for slug in slugs),
        ]

        self.assertEqual(len(mapped), len(set(mapped)), "Career learning map contains duplicate slugs")
        self.assertTrue(mapped, "Career learning map should contain at least one article")
        self.assertEqual([], sorted(set(mapped) - published))


if __name__ == "__main__":
    unittest.main()
