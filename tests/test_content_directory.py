import json
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from build_content_directory import (
    DIRECTORY_NAME,
    DirectoryBuildError,
    build_outputs,
    changed_outputs,
    load_content,
    write_outputs,
)


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            attributes = dict(attrs)
            if "href" in attributes:
                self.hrefs.append(attributes["href"])


class ContentDirectoryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "data").mkdir()
        self.guides = [
            {"title": "Zoll & Lead <Error>", "url": "guides/zoll-lead-error.html"},
            {"title": "Alpha Alarm", "url": "guides/alpha-alarm.html"},
            {"title": "Beta Battery", "url": "guides/beta-battery.html"},
        ]
        self.pm = [
            {"title": "Monitor PM", "url": "preventive-maintenance/monitor-pm.html"},
        ]
        self.basics = [
            {"title": "ECG Basics", "url": "biomed-basics/ecg-basics.html"},
        ]
        self._write_catalogs()

    def tearDown(self):
        self.temporary.cleanup()

    def _write_json(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def _write_catalogs(self):
        guide_shards = [self.guides[:2], self.guides[2:]]
        self._write_json("data/guides.json", ["data/guides-a.json", "data/guides-b.json"])
        self._write_json("data/guides-a.json", guide_shards[0])
        self._write_json("data/guides-b.json", guide_shards[1])
        self._write_json("data/preventive-maintenance.json", self.pm)
        self._write_json("data/biomed-basics.json", self.basics)
        for record in self.guides + self.pm + self.basics:
            target = self.root / record["url"]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("<!doctype html><title>Published</title>", encoding="utf-8")

    def test_every_destination_appears_once_and_html_is_escaped(self):
        outputs = build_outputs(self.root, page_size=2)
        detail_urls = []
        for relative, output in outputs.items():
            if not relative.startswith(DIRECTORY_NAME + "/"):
                continue
            parser = LinkParser()
            parser.feed(output)
            detail_urls.extend(href[3:] for href in parser.hrefs if href.startswith(("../guides/", "../preventive-maintenance/", "../biomed-basics/")))
        expected = {record["url"] for record in self.guides + self.pm + self.basics}
        self.assertEqual(set(detail_urls), expected)
        self.assertEqual(len(detail_urls), len(expected))
        guide_page = outputs["directory/troubleshooting-guides-002.html"]
        self.assertIn("Zoll &amp; Lead &lt;Error&gt;", guide_page)
        self.assertNotIn("Zoll & Lead <Error>", guide_page)

    def test_metadata_and_pagination_are_unique_and_crawlable(self):
        outputs = build_outputs(self.root, page_size=2)
        pages = [outputs[path] for path in sorted(outputs)]
        titles = []
        canonicals = []
        h1s = []
        for output in pages:
            titles.append(output.split("<title>", 1)[1].split("</title>", 1)[0])
            canonicals.append(output.split('<link rel="canonical" href="', 1)[1].split('">', 1)[0])
            h1s.append(output.split('<h1 id="page-heading" tabindex="-1">', 1)[1].split("</h1>", 1)[0])
            self.assertIn('<meta name="description" content="', output)
        self.assertEqual(len(titles), len(set(titles)))
        self.assertEqual(len(canonicals), len(set(canonicals)))
        self.assertEqual(len(h1s), len(set(h1s)))
        first = outputs["directory/troubleshooting-guides-001.html"]
        second = outputs["directory/troubleshooting-guides-002.html"]
        self.assertIn('href="troubleshooting-guides-002.html" rel="next"', first)
        self.assertIn('href="troubleshooting-guides-001.html" rel="prev"', second)
        self.assertIn('href="../content-directory.html#troubleshooting-guides"', first)

    def test_output_is_deterministic_and_check_detects_no_drift(self):
        first = build_outputs(self.root, page_size=2)
        second = build_outputs(self.root, page_size=2)
        self.assertEqual(first, second)
        changed, stale = write_outputs(self.root, first)
        self.assertEqual(set(changed), set(first))
        self.assertEqual(stale, [])
        self.assertEqual(changed_outputs(self.root, second), ([], []))

    def test_removed_records_remove_obsolete_generated_pages(self):
        outputs = build_outputs(self.root, page_size=1)
        write_outputs(self.root, outputs)
        obsolete = self.root / "directory/troubleshooting-guides-003.html"
        self.assertTrue(obsolete.is_file())
        removed = self.guides.pop()
        (self.root / removed["url"]).unlink()
        self._write_catalogs()
        # _write_catalogs recreates current published destinations only.
        updated = build_outputs(self.root, page_size=1)
        changed, stale = write_outputs(self.root, updated)
        self.assertIn("directory/troubleshooting-guides-003.html", stale)
        self.assertFalse(obsolete.exists())
        self.assertTrue(changed)

    def test_duplicate_and_missing_destinations_are_rejected(self):
        self.guides.append({"title": "Duplicate", "url": self.guides[0]["url"]})
        self._write_catalogs()
        with self.assertRaisesRegex(DirectoryBuildError, "Duplicate"):
            load_content(self.root)

        self.guides.pop()
        self._write_catalogs()
        (self.root / self.basics[0]["url"]).unlink()
        with self.assertRaisesRegex(DirectoryBuildError, "does not exist"):
            build_outputs(self.root)

    def test_unsafe_urls_and_unmarked_directory_files_are_rejected(self):
        self.guides[0]["url"] = "guides/../secrets.html"
        self._write_catalogs()
        with self.assertRaisesRegex(DirectoryBuildError, "Unsafe"):
            build_outputs(self.root)

        self.guides[0]["url"] = "guides/zoll-lead-error.html"
        self._write_catalogs()
        directory = self.root / DIRECTORY_NAME
        directory.mkdir()
        (directory / "manual.html").write_text("<title>Manual</title>", encoding="utf-8")
        with self.assertRaisesRegex(DirectoryBuildError, "unmarked"):
            changed_outputs(self.root, build_outputs(self.root))


if __name__ == "__main__":
    unittest.main()
