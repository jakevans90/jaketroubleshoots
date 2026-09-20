"""Read-only crawl of published HTML, including same-site links and metadata.

This checks the committed production output without running JavaScript. A page
without static inbound links may still be linked by client-side navigation.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from generate_sitemap import BASE_URL, production_html_files


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.h1 = 0
        self.description = []
        self.canonical = []
        self.robots = []
        self.viewport = []
        self.links = []
        self.ids = set()
        self.structured_data = []
        self.in_structured_data = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.h1 += 1
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "meta":
            name = attrs.get("name", "").lower()
            if name in ("description", "robots", "viewport"):
                getattr(self, name).append(attrs.get("content", ""))
        if tag == "link" and attrs.get("rel", "").lower() == "canonical":
            self.canonical.append(attrs.get("href", ""))
        if tag in ("a", "link") and attrs.get("href"):
            self.links.append((tag, attrs["href"]))
        if tag in ("img", "script", "iframe") and attrs.get("src"):
            self.links.append((tag, attrs["src"]))
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.in_structured_data = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script":
            self.in_structured_data = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_structured_data:
            self.structured_data.append(data)


def crawl(root: Path) -> dict:
    root = root.resolve()
    pages = {}
    findings = defaultdict(list)
    titles = defaultdict(list)
    inbound = Counter()
    for path in production_html_files(root):
        relative = path.relative_to(root).as_posix()
        page = Page()
        page.feed(path.read_text(encoding="utf-8-sig"))
        pages[relative] = page
        titles[page.title.strip()].append(relative)
        if not page.title.strip():
            findings["missing_title"].append(relative)
        if page.h1 != 1:
            findings["h1_count_not_one"].append(relative)
        if not page.description or not all(page.description):
            findings["missing_description"].append(relative)
        if not page.viewport:
            findings["missing_viewport"].append(relative)
        expected = BASE_URL + "/" + ("" if relative == "index.html" else relative)
        if page.canonical != [expected]:
            findings["canonical_mismatch"].append({"page": relative, "canonical": page.canonical})
        if any("noindex" in robots.lower() for robots in page.robots):
            findings["noindex"].append(relative)
        for data in page.structured_data:
            try:
                json.loads(data)
            except ValueError:
                findings["invalid_structured_data"].append(relative)
    targets = {}
    for relative, page in pages.items():
        for tag, href in page.links:
            url = urlsplit(href)
            if url.scheme and url.scheme not in ("http", "https"):
                continue
            if url.netloc and url.netloc not in ("jaketroubleshoots.com", "www.jaketroubleshoots.com"):
                continue
            path = unquote(url.path)
            key = ("" if path.startswith("/") else str(Path(relative).parent), path or relative)
            if key not in targets:
                if not path:
                    target = root / relative
                else:
                    target = root / path.lstrip("/") if path.startswith("/") else (root / relative).parent / path
                target = target.resolve()
                if target.is_dir():
                    target /= "index.html"
                targets[key] = (target, target.is_file())
            target, exists = targets[key]
            if not exists:
                findings["broken_links"].append({"page": relative, "tag": tag, "href": href})
                continue
            if not target.is_relative_to(root):
                findings["outside_site_links"].append({"page": relative, "href": href})
                continue
            target_relative = target.relative_to(root).as_posix()
            if tag == "a" and target_relative in pages:
                if target_relative != relative:
                    inbound[target_relative] += 1
                if url.fragment and unquote(url.fragment) not in pages[target_relative].ids:
                    findings["broken_fragments"].append({"page": relative, "href": href})
    findings["duplicate_titles"] = [{"title": title, "pages": paths}
                                     for title, paths in titles.items() if title and len(paths) > 1]
    sitemap = ElementTree.parse(root / "sitemap.xml")
    locations = [entry.text or "" for entry in sitemap.findall(".//{*}loc")]
    expected = {BASE_URL + "/" + ("" if path == "index.html" else path) for path in pages}
    findings["missing_sitemap_entries"] = sorted(expected - set(locations))
    findings["unexpected_sitemap_entries"] = sorted(set(locations) - expected)
    findings["duplicate_sitemap_entries"] = [url for url, count in Counter(locations).items() if count > 1]
    findings["no_static_inbound_links"] = [path for path in pages if not inbound[path]]
    robots = root / "robots.txt"
    if robots.exists():
        for line in robots.read_text(encoding="utf-8").splitlines():
            if line.lower().startswith("sitemap:"):
                url = line.split(":", 1)[1].strip()
                if not (root / unquote(urlsplit(url).path).lstrip("/")).is_file():
                    findings["broken_robots_sitemap"].append(url)
    return {"pages": len(pages), "sitemap_urls": len(locations),
            "structured_data_pages": sum(bool(page.structured_data) for page in pages.values()),
            "scope": "Published HTML only; links generated by JavaScript are not counted as static inbound links.",
            "counts": {key: len(value) for key, value in sorted(findings.items())},
            "samples": {key: value[:20] for key, value in sorted(findings.items()) if value}}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    result = crawl(args.root)
    output = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    print(json.dumps({"pages": result["pages"], "counts": result["counts"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
