"""Generate the sitemap from published pages, never drafts or test fixtures."""
from __future__ import annotations

import argparse
from pathlib import Path
from xml.sax.saxutils import escape

BASE_URL = "https://jaketroubleshoots.com"
ROOT = Path(__file__).resolve().parent
CONTENT_DIRECTORIES = ("guides", "preventive-maintenance", "biomed-basics")


def production_html_files(root: Path = ROOT) -> list[Path]:
    """The deployed site uses flat root pages and three flat content libraries.

    Keep this explicit: recursive discovery can publish temporary transaction
    output, review reports, incoming drafts, or fixtures in a public sitemap.
    Add a directory here when intentionally introducing a new public library.
    """
    pages = list(root.glob("*.html"))
    for directory in CONTENT_DIRECTORIES:
        pages.extend((root / directory).glob("*.html"))
    return sorted(path for path in pages if path.is_file() and not path.name.startswith("."))


def sitemap_urls(root: Path = ROOT) -> list[str]:
    urls = []
    for path in production_html_files(root):
        relative = path.relative_to(root).as_posix()
        urls.append(f"{BASE_URL}/" if relative == "index.html" else f"{BASE_URL}/{relative}")
    return sorted(urls, key=lambda url: (url != f"{BASE_URL}/", url))


def render_sitemap(root: Path = ROOT) -> str:
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in sitemap_urls(root):
        lines.extend(("<url>", f"<loc>{escape(url)}</loc>", "</url>"))
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    (root / "sitemap.xml").write_text(render_sitemap(root), encoding="utf-8")
    print(f"Sitemap generated with {len(sitemap_urls(root))} URLs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
