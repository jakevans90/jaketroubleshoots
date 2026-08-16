#!/usr/bin/env python3
"""Analyze a proposed Biomed Basics article without writing repository files."""

from __future__ import annotations

import argparse
import html
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://jaketroubleshoots.com"
REQUIRED_FIELDS = {"title"}
ALLOWED_FIELDS = {"title", "slug", "description", "category", "badge", "cardNote"}
STOP_WORDS = {
    "about", "after", "also", "and", "appear", "are", "basics", "before", "biomed",
    "biomedical", "biomeds", "can", "current", "equipment", "exactly", "english", "for", "from", "how", "into", "its",
    "means", "medical", "more", "not", "page", "plain", "problems", "that", "the", "their", "these", "this",
    "through", "using", "what", "when", "where", "which", "with", "your",
}


class InputError(ValueError):
    pass


@dataclass(frozen=True)
class Article:
    path: Path
    metadata: dict[str, str]
    body: str
    title: str
    slug: str
    description: str


@dataclass(frozen=True)
class ExistingArticle:
    path: Path
    title: str
    text: str
    href: str


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", normalized.lower())).strip("-")


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_input(path: Path) -> Article:
    try:
        source = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise InputError(f"cannot read input: {exc}") from exc
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)(.*)\Z", source, re.DOTALL)
    if not match:
        return parse_plain_markdown(path, source)
    metadata: dict[str, str] = {}
    for number, raw_line in enumerate(match.group(1).splitlines(), 2):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        field = re.match(r"^([A-Za-z][A-Za-z0-9]*):\s*(.*)$", raw_line)
        if not field:
            raise InputError(f"unsupported front-matter syntax on line {number}")
        key, value = field.group(1), _unquote(field.group(2))
        if key in metadata:
            raise InputError(f"duplicate front-matter field: {key}")
        if key not in ALLOWED_FIELDS:
            raise InputError(f"unknown front-matter field: {key}")
        metadata[key] = value.strip()
    missing = sorted(key for key in REQUIRED_FIELDS if not metadata.get(key))
    if missing:
        raise InputError(f"missing required field(s): {', '.join(missing)}")
    body = match.group(2).strip()
    if not body:
        raise InputError("article body is empty")
    title = metadata["title"]
    slug = metadata.get("slug") or slugify(title)
    if not slug or slug != slugify(slug):
        raise InputError("slug must contain lowercase ASCII letters, numbers, and single hyphens")
    description = metadata.get("description", "")
    if not description:
        first_paragraph = next((p.strip() for p in re.split(r"\n\s*\n", body) if not p.lstrip().startswith("#")), "")
        description = re.sub(r"[*_`\[\]()]", "", first_paragraph).strip()
    return Article(path, metadata, body, title, slug, description)


def parse_plain_markdown(path: Path, source: str) -> Article:
    """Accept a pasted article with an H1 title and infer only planning metadata."""
    heading = re.match(r"\A\s*#\s+(.+?)\s*(?:\n|\Z)", source)
    if not heading:
        lines = [line.rstrip() for line in source.splitlines()]
        while lines and not lines[0].strip():
            lines.pop(0)
        if len(lines) < 3 or not lines[0].strip() or not lines[1].strip():
            raise InputError("input needs YAML-style front matter, a Markdown H1, or plain title and subtitle lines")
        title = lines.pop(0).strip()
        subtitle = lines.pop(0).strip()
        converted = [f"## {subtitle}", ""]
        list_mode = False
        for index, raw in enumerate(lines):
            line = raw.strip()
            if not line:
                converted.append("")
                continue
            previous = lines[index - 1].strip() if index else ""
            following = lines[index + 1].strip() if index + 1 < len(lines) else ""
            words = line.split()
            if list_mode:
                if len(words) <= 7 and not line.endswith((".", "?", "!", ":")):
                    converted.append(f"- {line}")
                    continue
                list_mode = False
            next_is_prose = len(following.split()) >= 7 or following.endswith((".", "?", "!", ":"))
            looks_like_heading = (
                len(words) <= 10
                and not line.endswith((".", "!", ":", ","))
                and not previous.endswith(":")
                and next_is_prose
                and line not in {"Pass", "Fail", "Strong evidence"}
                and "↓" not in line
                and "=" not in line
            )
            converted.extend(([f"# {line}", ""] if looks_like_heading else [line, ""]))
            if line.endswith(":"):
                list_mode = True
        body = "\n".join(converted).strip()
        description = re.sub(r"[*_`\[\]()]", "", subtitle).strip()
        return Article(path, {}, body, title, slugify(title), description)
    title = heading.group(1).strip()
    body = source[heading.end():].strip()
    if not body:
        raise InputError("article body is empty")
    paragraphs = [
        part.strip()
        for part in re.split(r"\n\s*\n", body)
        if part.strip() and not part.lstrip().startswith("#")
    ]
    description = re.sub(r"[*_`\[\]()]", "", paragraphs[0]).strip() if paragraphs else ""
    return Article(path, {}, body, title, slugify(title), description)


def html_text(source: str) -> str:
    source = re.sub(r"<(script|style)\b.*?</\1>", " ", source, flags=re.I | re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", source))).strip()


def load_existing(root: Path) -> list[ExistingArticle]:
    articles = []
    for path in sorted((root / "biomed-basics").glob("*.html")):
        source = path.read_text(encoding="utf-8")
        heading = re.search(r"<h2\b[^>]*>(.*?)</h2>", source, re.I | re.S)
        title = html_text(heading.group(1)) if heading else path.stem.replace("-", " ").title()
        articles.append(ExistingArticle(path, title, html_text(source), f"biomed-basics/{path.name}"))
    return articles


def keywords(value: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKD", value).lower())
    return {word for word in words if len(word) >= 4 and word not in STOP_WORDS}


def related(article: Article, existing: list[ExistingArticle], limit: int = 5) -> list[tuple[ExistingArticle, list[str]]]:
    proposed = keywords(f"{article.title} {article.description} {article.body}")
    ranked = []
    for current in existing:
        shared = proposed & keywords(f"{current.title} {current.text}")
        title_terms = keywords(current.title)
        title_overlap = shared & title_terms
        score = len(shared) + 3 * len(title_overlap)
        # A single generic word from a long page is not a useful link suggestion.
        if title_overlap:
            ranked.append((score, current.title.lower(), current, sorted(title_overlap or shared)[:6]))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [(item[2], item[3]) for item in ranked[:limit]]


def build_report(article: Article, root: Path) -> tuple[str, bool]:
    existing = load_existing(root)
    target = f"biomed-basics/{article.slug}.html"
    canonical = f"{SITE_URL}/{target}"
    title_key = re.sub(r"[^a-z0-9]", "", article.title.lower())
    duplicates = []
    if (root / target).exists():
        duplicates.append(f"target already exists: {target}")
    for current in existing:
        current_key = re.sub(r"[^a-z0-9]", "", current.title.lower())
        if current_key == title_key:
            duplicates.append(f"title matches existing article: {current.href}")
    warnings = []
    if len(article.description) > 180:
        warnings.append(f"description is {len(article.description)} characters; review before using it as metadata/card copy")
    if not article.metadata.get("category"):
        warnings.append("category is not supplied; choose landing-page badge text during publishing")
    candidates = related(article, existing)
    lines = [
        "BIOMED BASICS DRY RUN", "=====================", "",
        f"Status: {'BLOCKED' if duplicates else 'READY'}", "Mode: analysis only (no files written)", "",
        "Article:", f"  {article.title}", "",
        "Proposed slug and URL:", f"  {article.slug}", f"  /{target}", f"  {canonical}", "",
        "Would create in a future publisher:", f"  {target}", "",
        "Would modify in a future publisher:",
        "  biomed-basics.html (add article card)",
        "  sitemap.xml (add canonical URL; current generator discovers HTML files)", "",
        "Search/index impact:",
        "  No search data file exists for Biomed Basics.",
        "  search.html currently loads troubleshooting-guide JSON only; no change is proposed by this analyzer.", "",
        "Candidate internal-link updates (review manually):",
    ]
    if candidates:
        for current, terms in candidates:
            lines.append(f"  {current.href}  [shared topics: {', '.join(terms)}]")
    else:
        lines.append("  None found")
    lines += ["", "Candidate outbound links for the new article:"]
    if candidates:
        for current, terms in candidates:
            lines.append(f"  /{current.href}  [possible anchor topics: {', '.join(terms)}]")
    else:
        lines.append("  None found")
    lines += ["", "Duplicates/conflicts:"] + ([f"  {item}" for item in duplicates] or ["  None"])
    lines += ["", "Warnings:"] + ([f"  {item}" for item in warnings] or ["  None"])
    lines += ["", "NO FILES WRITTEN"]
    return "\n".join(lines), not duplicates


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="reviewed Markdown article draft")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    try:
        article = parse_input(args.input)
        report, ready = build_report(article, args.root.resolve())
    except InputError as exc:
        print(f"Biomed Basics dry run blocked: {exc}", file=sys.stderr)
        return 2
    print(report)
    return 0 if ready else 2


if __name__ == "__main__":
    raise SystemExit(main())
