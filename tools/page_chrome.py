"""Maintain accessible static page chrome without rewriting technical content.

Run with --write after publishing; --check verifies committed production HTML.
Only explicit page tags, heading attributes, navigation, and exact catalog links
are changed. Existing technical text and URLs remain the source of truth.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DETAIL_DIRS = ("guides", "preventive-maintenance", "biomed-basics")
TOC = re.compile(r'<!-- page-navigation:start -->.*?<!-- page-navigation:end -->\s*', re.S)


def production_pages(root):
    yield from sorted(root.glob("*.html"))
    for directory in DETAIL_DIRS:
        yield from sorted((root / directory).glob("*.html"))


def plain_text(value):
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def normalize_page_chrome(source, detail=False, hubs=None):
    newline = "\r\n" if "\r\n" in source else "\n"
    # Version changed shared assets so cached pages cannot mix old JS/CSS with
    # new semantic markup. Keep this stable until the next shared-asset release.
    source = re.sub(r'(href|src)="((?:\.\./|/)?)(style\.css|guides\.js|site-search\.js|related-guides\.js|feedback\.js|guide-icons\.js|hub-links\.js)(?:\?[^\"]*)?"',
                    lambda match: f'{match[1]}="{match[2]}{match[3]}?v={"20260919-2" if match[3] == "site-search.js" else "20260919"}"', source)
    source = re.sub(r'<html(?![^>]*\blang=)(\b[^>]*)>', r'<html lang="en"\1>', source, count=1, flags=re.I)
    if not re.search(r'<meta\s+[^>]*charset=', source, re.I):
        source = re.sub(r'(<head\b[^>]*>)', r'\1' + newline + '  <meta charset="UTF-8">', source, count=1, flags=re.I)
    if not re.search(r'<meta\s+[^>]*name=[\"\']viewport[\"\']', source, re.I):
        source = re.sub(r'(<meta\s+charset=[^>]+>)', r'\1' + newline +
                        '  <meta name="viewport" content="width=device-width, initial-scale=1">', source, count=1, flags=re.I)
    # Promote the existing page title, preserving its wording and identifier.
    if not re.search(r'<h1\b', source, re.I):
        source = re.sub(r'(<section\b[^>]*class="[^"]*\bhero\b[^"]*"[^>]*>.*?)<h2(\b[^>]*)>(.*?)</h2>',
                        r'\1<h1\2>\3</h1>', source, count=1, flags=re.S)
    heading = re.search(r'<h1\b([^>]*)>', source)
    if heading:
        attrs = heading[1]
        identifier = re.search(r'\bid="([^"]+)"', attrs)
        target = identifier[1] if identifier else "page-heading"
        if not identifier:
            attrs += f' id="{target}"'
        if "tabindex=" not in attrs:
            attrs += ' tabindex="-1"'
        source = source[:heading.start()] + '<h1' + attrs + '>' + source[heading.end():]
        if 'class="skip-link"' not in source:
            source = re.sub(r'(<body\b[^>]*>)', r'\1' + newline +
                            f'<a class="skip-link" href="#{target}">Skip to content</a>', source, count=1)
    if not detail:
        return source

    source = TOC.sub("", source)
    main = re.search(r'(<main\b[^>]*>)(.*?)(</main>)', source, re.S)
    if not main:
        return source
    body = main[2]
    # Make existing taxonomy values usable before scripts load. Never infer aliases.
    if hubs:
        for label, catalog in hubs.items():
            pattern = re.compile(r'(<h3\b[^>]*>' + re.escape(label) + r'</h3>\s*<p\b[^>]*>)([^<]+)(</p>)')
            def link_value(match):
                name = plain_text(match[2])
                matches = [h for h in catalog if h.get('name') == name and h.get('flags', {}).get('exists') is True]
                if len(matches) != 1:
                    return match[0]
                url = matches[0].get('url', '')
                if not url.startswith(('hub-asset.html?slug=', 'hub-manufacturer.html?slug=', 'hub-model.html?slug=')):
                    return match[0]
                return match[1] + f'<a href="/{html.escape(url, quote=True)}">' + match[2] + '</a>' + match[3]
            body = pattern.sub(link_value, body)

    level = "h2" if len(re.findall(r'<h2\b', body)) >= 4 else "h3"
    headings = list(re.finditer(r'<' + level + r'\b([^>]*)>(.*?)</' + level + '>', body, re.S))
    excluded = {"Asset Type", "Manufacturer", "Model", "Manual Reference", "Related Biomed Basics", "Jump to a Section"}
    headings = [h for h in headings if plain_text(h[2]) not in excluded]
    if 4 <= len(headings) <= 24 and 'Jump to a Section' not in body:
        ids = set(re.findall(r'\bid="([^"]+)"', source))
        links = []
        replacements = []
        for match in headings:
            attrs, text = match[1], plain_text(match[2])
            existing = re.search(r'\bid="([^"]+)"', attrs)
            identifier = existing[1] if existing else 'section-' + re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
            if not existing:
                base, suffix = identifier, 2
                while identifier in ids:
                    identifier = f'{base}-{suffix}'
                    suffix += 1
                attrs += f' id="{identifier}"'
                ids.add(identifier)
            if 'tabindex=' not in attrs:
                attrs += ' tabindex="-1"'
            replacements.append((match.start(), match.end(), f'<{level}{attrs}>{match[2]}</{level}>'))
            links.append(f'      <li><a href="#{html.escape(identifier, quote=True)}">{html.escape(text)}</a></li>')
        for start, end, replacement in reversed(replacements):
            body = body[:start] + replacement + body[end:]
        toc = newline.join(['<!-- page-navigation:start -->', '<details class="page-toc">',
                            '  <summary>On this page</summary>', '  <nav aria-label="On this page">',
                            '    <ul>', *links, '    </ul>', '  </nav>', '</details>',
                            '<!-- page-navigation:end -->', ''])
        body = newline + toc + body.lstrip('\r\n')
    source = source[:main.start(2)] + body + source[main.end(2):]
    # Emoji alone is an ambiguous accessible button name.
    source = source.replace('class="thumb-btn yes"', 'class="thumb-btn yes" aria-label="This guide was helpful"') if 'aria-label="This guide was helpful"' not in source else source
    source = source.replace('class="thumb-btn no"', 'class="thumb-btn no" aria-label="This guide was not helpful"') if 'aria-label="This guide was not helpful"' not in source else source
    return source


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args(argv)
    hubs = {label: json.loads((args.root / 'data' / filename).read_text(encoding='utf-8'))
            for label, filename in [('Asset Type', 'hub-asset.json'), ('Manufacturer', 'hub-manufacturer.json'), ('Model', 'hub-model.json')]}
    changed = 0
    for path in production_pages(args.root):
        original = path.read_bytes().decode('utf-8')
        updated = normalize_page_chrome(original, path.parent.name in DETAIL_DIRS, hubs)
        if updated != original:
            changed += 1
            if args.write:
                with tempfile.NamedTemporaryFile(dir=path.parent, suffix='.tmp', delete=False) as output:
                    temporary = Path(output.name)
                    output.write(updated.encode('utf-8'))
                try:
                    os.replace(temporary, path)
                finally:
                    temporary.unlink(missing_ok=True)
    print(f'{changed} production pages {"updated" if args.write else "need chrome updates"}.')
    return 1 if args.check and changed else 0


if __name__ == '__main__':
    raise SystemExit(main())
