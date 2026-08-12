#!/usr/bin/env python3
"""Prepare the first Biomed Basics article publication and related-link cleanup."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import tempfile
from pathlib import Path

from analyze_biomed_basic import ROOT, SITE_URL, parse_input, slugify


RELATED = {
    "biomed-bmet-clinical-engineering-htm": ["biomed-translation-problems-medical-equipment-names", "biomed-resume-basics", "biomed-work-order-notes-ccr-method", "functional-testing-vs-calibration-vs-verification", "when-to-remove-medical-equipment-from-service"],
    "electrical-safety-testing-medical-equipment": ["voltage-current-resistance-and-continuity-in-plain-english", "how-to-use-a-multimeter-in-biomed", "fuses-breakers-and-power-supplies-in-medical-equipment", "when-to-remove-medical-equipment-from-service", "functional-testing-vs-calibration-vs-verification"],
    "functional-testing-vs-calibration-vs-verification": ["what-known-good-actually-means", "how-to-use-a-multimeter-in-biomed", "when-to-remove-medical-equipment-from-service", "electrical-safety-testing-medical-equipment", "how-to-read-a-medical-equipment-service-manual"],
    "biomed-work-order-notes-ccr-method": ["how-to-reproduce-a-clinical-complaint-on-the-bench", "how-to-read-a-medical-equipment-service-manual", "when-to-remove-medical-equipment-from-service", "functional-testing-vs-calibration-vs-verification", "how-to-think-before-calling-a-vendor"],
    "medical-equipment-battery-basics": ["fuses-breakers-and-power-supplies-in-medical-equipment", "voltage-current-resistance-and-continuity-in-plain-english", "how-to-use-a-multimeter-in-biomed", "what-known-good-actually-means", "electrical-safety-testing-medical-equipment"],
    "basic-networking-for-medical-equipment": ["hospital-emrs-and-medical-device-integration", "what-dicom-means-in-plain-english", "what-hl7-means-in-plain-english", "nurse-call-integration-basics", "biomed-work-order-notes-ccr-method"],
    "hospital-emrs-and-medical-device-integration": ["basic-networking-for-medical-equipment", "what-dicom-means-in-plain-english", "what-hl7-means-in-plain-english", "nurse-call-integration-basics", "biomed-work-order-notes-ccr-method"],
    "what-dicom-means-in-plain-english": ["hospital-emrs-and-medical-device-integration", "basic-networking-for-medical-equipment", "what-hl7-means-in-plain-english", "biomed-work-order-notes-ccr-method", "biomed-translation-problems-medical-equipment-names"],
    "biomed-resume-basics": ["biomed-bmet-clinical-engineering-htm", "biomed-translation-problems-medical-equipment-names", "biomed-work-order-notes-ccr-method", "basic-networking-for-medical-equipment", "when-to-remove-medical-equipment-from-service"],
    "biomed-translation-problems-medical-equipment-names": ["biomed-bmet-clinical-engineering-htm", "biomed-work-order-notes-ccr-method", "basic-networking-for-medical-equipment", "biomed-resume-basics", "when-to-remove-medical-equipment-from-service"],
    "when-to-remove-medical-equipment-from-service": ["how-to-reproduce-a-clinical-complaint-on-the-bench", "functional-testing-vs-calibration-vs-verification", "electrical-safety-testing-medical-equipment", "how-to-read-a-medical-equipment-service-manual", "how-to-think-before-calling-a-vendor"],
    "how-to-think-before-calling-a-vendor": ["what-known-good-actually-means", "how-to-read-a-medical-equipment-service-manual", "how-to-reproduce-a-clinical-complaint-on-the-bench", "when-to-remove-medical-equipment-from-service", "functional-testing-vs-calibration-vs-verification"],
    "what-hl7-means-in-plain-english": ["hospital-emrs-and-medical-device-integration", "basic-networking-for-medical-equipment", "what-dicom-means-in-plain-english", "nurse-call-integration-basics", "biomed-work-order-notes-ccr-method"],
    "nurse-call-integration-basics": ["what-hl7-means-in-plain-english", "basic-networking-for-medical-equipment", "hospital-emrs-and-medical-device-integration", "biomed-work-order-notes-ccr-method", "when-to-remove-medical-equipment-from-service"],
    "how-to-read-a-medical-equipment-service-manual": ["what-known-good-actually-means", "how-to-use-a-multimeter-in-biomed", "how-to-think-before-calling-a-vendor", "functional-testing-vs-calibration-vs-verification", "how-to-reproduce-a-clinical-complaint-on-the-bench"],
    "how-to-reproduce-a-clinical-complaint-on-the-bench": ["what-known-good-actually-means", "how-to-think-before-calling-a-vendor", "when-to-remove-medical-equipment-from-service", "functional-testing-vs-calibration-vs-verification", "biomed-work-order-notes-ccr-method"],
    "how-to-use-a-multimeter-in-biomed": ["voltage-current-resistance-and-continuity-in-plain-english", "fuses-breakers-and-power-supplies-in-medical-equipment", "electrical-safety-testing-medical-equipment", "functional-testing-vs-calibration-vs-verification", "what-known-good-actually-means"],
    "what-known-good-actually-means": ["how-to-reproduce-a-clinical-complaint-on-the-bench", "how-to-think-before-calling-a-vendor", "how-to-read-a-medical-equipment-service-manual", "functional-testing-vs-calibration-vs-verification", "how-to-use-a-multimeter-in-biomed"],
    "fuses-breakers-and-power-supplies-in-medical-equipment": ["voltage-current-resistance-and-continuity-in-plain-english", "how-to-use-a-multimeter-in-biomed", "medical-equipment-battery-basics", "electrical-safety-testing-medical-equipment", "how-to-read-a-medical-equipment-service-manual"],
    "voltage-current-resistance-and-continuity-in-plain-english": ["how-to-use-a-multimeter-in-biomed", "fuses-breakers-and-power-supplies-in-medical-equipment", "electrical-safety-testing-medical-equipment", "functional-testing-vs-calibration-vs-verification", "medical-equipment-battery-basics"],
}

ARTICLE_CONFIG = {
    "when-to-remove-medical-equipment-from-service": {
        "description": "A practical guide to deciding when medical equipment should be removed from clinical service and what must be verified before it is returned.",
        "category": "Safety & Risk",
        "badge": "Core Concept",
        "cardNote": "Removal and return-to-service decisions",
    },
    "how-to-think-before-calling-a-vendor": {
        "description": "A practical guide to gathering evidence, narrowing symptoms, and preparing for a productive medical-equipment vendor support call.",
        "category": "Troubleshooting",
        "badge": "Core Concept",
        "cardNote": "Vendor escalation and support-call basics",
    },
    "what-hl7-means-in-plain-english": {
        "description": "A practical introduction to HL7 messages, ADT and ORU workflows, interface engines, acknowledgements, and medical-device data exchange.",
        "category": "Integration",
        "badge": "Core Concept",
        "cardNote": "Device data and messaging basics",
    },
    "nurse-call-integration-basics": {
        "description": "A practical introduction to nurse call interfaces, contact closures, alarm signals, cables, room connections, and common failure patterns.",
        "category": "Integration",
        "badge": "Core Concept",
        "cardNote": "Alarm and nurse call interface basics",
    },
    "how-to-read-a-medical-equipment-service-manual": {
        "description": "A practical guide to finding troubleshooting steps, warnings, diagrams, specifications, service modes, parts, and verification procedures in medical-equipment manuals.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Service documentation and manual navigation",
    },
    "how-to-reproduce-a-clinical-complaint-on-the-bench": {
        "description": "A practical guide to recreating clinical failure conditions, isolating intermittent problems, using original accessories, and documenting meaningful bench testing.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Complaint reproduction and bench testing",
    },
    "how-to-use-a-multimeter-in-biomed": {
        "description": "A practical introduction to measuring voltage, resistance, and continuity safely while troubleshooting medical equipment.",
        "category": "Testing & Verification",
        "badge": "Core Skill",
        "cardNote": "Multimeter safety and measurement basics",
    },
    "what-known-good-actually-means": {
        "description": "A practical guide to validating known-good parts, accessories, test equipment, and comparison devices before relying on substitution testing.",
        "category": "Troubleshooting",
        "badge": "Core Concept",
        "cardNote": "Reliable substitution testing",
    },
    "fuses-breakers-and-power-supplies-in-medical-equipment": {
        "description": "A practical introduction to fuses, circuit breakers, power supplies, and the common power-path failures found in medical equipment.",
        "category": "Testing & Verification",
        "badge": "Core Concept",
        "cardNote": "Power protection and supply basics",
        "plannedTitles": ["Fuses, Breakers, and Power Supplies"],
    },
    "voltage-current-resistance-and-continuity-in-plain-english": {
        "description": "A plain-English introduction to voltage, current, resistance, and continuity for medical-equipment troubleshooting.",
        "category": "Testing & Verification",
        "badge": "Core Concept",
        "cardNote": "Essential electrical concepts",
    },
}


def inline(value: str) -> str:
    value = html.escape(value.strip(), quote=False)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*(.+?)\*(?!\*)", r"<em>\1</em>", value)
    return value


def split_article(body: str) -> tuple[str, str, list[tuple[str, list[str]]]]:
    lines = body.splitlines()
    subtitle = ""
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].startswith("## "):
        subtitle = lines.pop(0)[3:].strip()
    while lines and not lines[0].strip():
        lines.pop(0)
    intro = ""
    intro_lines = []
    while lines and not lines[0].startswith("## "):
        if lines[0].strip():
            intro_lines.append(lines[0].strip())
        elif intro_lines:
            break
        lines.pop(0)
    intro = " ".join(intro_lines)
    sections: list[tuple[str, list[str]]] = []
    current_title = ""
    current_lines: list[str] = []
    for line in lines:
        if line.startswith("## "):
            if current_title:
                sections.append((current_title, current_lines))
            current_title, current_lines = line[3:].strip(), []
        elif current_title:
            current_lines.append(line)
    if current_title:
        sections.append((current_title, current_lines))
    return subtitle, intro, sections


def render_lines(lines: list[str]) -> str:
    out: list[str] = []
    paragraph: list[str] = []
    list_kind = ""

    def flush_paragraph() -> None:
        if paragraph:
            out.append(f"    <p>{inline(' '.join(paragraph))}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_kind
        if list_kind:
            out.append(f"    </{list_kind}>")
            list_kind = ""

    for raw in lines + [""]:
        line = raw.strip()
        if line.startswith("### "):
            flush_paragraph(); close_list()
            out.append(f"    <h4>{inline(line[4:])}</h4>")
        elif re.match(r"^[-*]\s+", line):
            flush_paragraph()
            if list_kind != "ul":
                close_list(); list_kind = "ul"; out.append("    <ul>")
            out.append(f"      <li>{inline(re.sub(r'^[-*]\s+', '', line))}</li>")
        elif re.match(r"^\d+\.\s+", line):
            flush_paragraph()
            if list_kind != "ol":
                close_list(); list_kind = "ol"; out.append("    <ol>")
            out.append(f"      <li>{inline(re.sub(r'^\d+\.\s+', '', line))}</li>")
        elif line.startswith("> "):
            flush_paragraph(); close_list()
            out.append(f"    <blockquote><p>{inline(line[2:])}</p></blockquote>")
        elif not line:
            flush_paragraph(); close_list()
        else:
            close_list(); paragraph.append(line)
    return "\n".join(out)


def related_section(slug: str, titles: dict[str, str]) -> str:
    items = "\n".join(
        f'      <li><a href="{target}.html">{html.escape(titles[target])}</a></li>'
        for target in RELATED[slug]
    )
    return f'''  <section class="content-box">
    <h3>Related Biomed Basics</h3>
    <ul>
{items}
    </ul>
    <div class="hero-buttons" style="margin-top:20px; margin-bottom:0;">
      <a href="../biomed-basics.html" class="hero-button">Back to Biomed Basics</a>
    </div>
  </section>'''


def page_html(title: str, subtitle: str, description: str, hero_intro: str, sections: list[tuple[str, list[str]]], titles: dict[str, str]) -> str:
    slug = slugify(title)
    jump_targets = [(heading, slugify(heading)) for heading, _ in sections if heading not in {"Jump to a Section", "Important Note"}]
    rendered = []
    for heading, lines in sections:
        if heading == "Jump to a Section":
            labels = [re.sub(r"^[-*]\s+", "", line.strip()) for line in lines if re.match(r"^[-*]\s+", line.strip())]
            links = "\n".join(f'      <li><a href="#{slugify(label)}">{html.escape(label)}</a></li>' for label in labels)
            rendered.append(f'  <section class="content-box">\n    <h3>Jump to a Section</h3>\n    <ul>\n{links}\n    </ul>\n  </section>')
            continue
        rendered.append(f'  <section class="content-box" id="{slugify(heading)}">\n    <h3>{html.escape(heading)}</h3>\n{render_lines(lines)}\n  </section>')
    rendered.append(related_section(slug, titles))
    body = "\n\n".join(rendered)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{html.escape(title)} | Jake Troubleshoots</title>
  <meta name="description" content="{html.escape(description, quote=True)}">
  <link rel="stylesheet" href="../style.css">
  <link rel="icon" type="image/x-icon" href="../images/favicon.ico">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-1L34E3TJL6"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-1L34E3TJL6');</script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js?client=ca-pub-8569368568902704" crossorigin="anonymous"></script>
  <link rel="canonical" href="{SITE_URL}/biomed-basics/{slug}.html" />
  <script src="../social-links.js" defer></script>
</head>
<body>
<header>
  <a href="../index.html" class="site-logo"><img src="../images/logo.png" alt="Jake Troubleshoots Logo" class="site-icon"><span class="logo-text">Jake Troubleshoots</span></a>
  <nav><a href="../index.html">Home</a><a href="../guides.html">Guides</a><a href="../search.html">Search</a><a href="../preventive-maintenance.html">PMs</a><a href="../vendors.html">Vendors</a><a href="../contact.html">About</a></nav>
</header>
<section class="hero">
  <h2>{html.escape(title)}</h2>
  <p>{html.escape(subtitle)}</p>
  <p style="max-width:760px; margin:10px auto 0; font-size:0.95em;">{html.escape(hero_intro)}</p>
  <div class="hero-buttons" style="margin-top:20px; display:flex; justify-content:center; gap:12px; flex-wrap:wrap;"><a href="../biomed-basics.html" class="hero-button">Back to Biomed Basics</a></div>
</section>
<main>
{body}
</main>
<footer>
  <p>Contact: <a href="mailto:contact@jaketroubleshoots.com" style="color:#8fff00;">contact@jaketroubleshoots.com</a></p>
  <p><a href="../privacy-policy.html">Privacy Policy</a> &nbsp;|&nbsp; <a href="../terms-of-use.html">Terms of Use</a></p>
  <p>Guides intended for trained personnel only.</p><p>© 2026 Jake Troubleshoots</p>
</footer>
</body>
</html>
'''


def title_map(root: Path, new_titles: list[str]) -> dict[str, str]:
    titles = {slugify(title): title for title in new_titles}
    for path in (root / "biomed-basics").glob("*.html"):
        source = path.read_text(encoding="utf-8")
        match = re.search(r"<h2\b[^>]*>(.*?)</h2>", source, re.I | re.S)
        titles[path.stem] = re.sub(r"<[^>]+>", "", match.group(1)).strip() if match else path.stem.replace("-", " ").title()
    return titles


def parse_batch(path: Path) -> list:
    source = path.read_text(encoding="utf-8")
    chunks = re.split(r"\n\s*---\s*\n(?=#\s+)", source)
    articles = []
    with tempfile.TemporaryDirectory() as directory:
        for index, chunk in enumerate(chunks, 1):
            temporary = Path(directory) / f"article-{index}.md"
            temporary.write_text(chunk.strip() + "\n", encoding="utf-8")
            articles.append(parse_input(temporary))
    return articles


def replace_related(source: str, replacement: str) -> str:
    pattern = re.compile(r'\s*<section class="content-box">\s*<h3>Related Biomed Basics</h3>.*?</section>', re.I | re.S)
    updated, count = pattern.subn("\n\n" + replacement, source, count=1)
    if count != 1:
        raise ValueError("expected exactly one Related Biomed Basics section")
    return updated


def biomed_group(category: str) -> str:
    normalized = category.casefold()
    if any(word in normalized for word in ("network", "integration", "imaging", "dicom")):
        return "connected-systems"
    if any(word in normalized for word in ("career", "communication", "terminology")):
        return "career-communication"
    if any(word in normalized for word in ("testing", "electrical")):
        return "start-here"
    if any(word in normalized for word in ("troubleshoot", "safety", "risk")):
        return "troubleshooting-safety"
    return "everyday-skills"


def catalog_entry(title: str, slug: str, config: dict[str, str], existing: dict | None = None) -> dict:
    entry = {
        "title": title,
        "slug": slug,
        "url": f"biomed-basics/{slug}.html",
        "description": config["description"],
        "category": config["category"],
        "group": biomed_group(config["category"]),
        "badge": config["badge"],
        "cardNote": config["cardNote"],
    }
    for key in ("featured", "featuredOrder"):
        if existing and key in existing:
            entry[key] = existing[key]
    return entry


def remove_published_planned_topics(landing: str, published_titles: set[str]) -> str:
    section_pattern = re.compile(
        r'(<section class="content-box planned-topics-section">.*?<h3>Planned Topics</h3>.*?)(</section>\s*</div>\s*</section>)',
        re.S,
    )
    match = section_pattern.search(landing)
    if not match:
        raise SystemExit("Planned Topics section not found")
    normalized_titles = {slugify(title) for title in published_titles}
    cleaned_section = re.sub(
        r'\s*<li>(.*?)</li>',
        lambda item: "" if slugify(html.unescape(re.sub(r"<[^>]+>", "", item.group(1)))) in normalized_titles else item.group(0),
        match.group(1),
        flags=re.S,
    )
    remaining_count = len(re.findall(r'<li>.*?</li>', cleaned_section, re.S))
    cleaned_section = re.sub(
        r'(<div class="planned-topic-count"[^>]*>\s*<strong>)\d+(</strong>)',
        rf'\g<1>{remaining_count}\2',
        cleaned_section,
        count=1,
    )
    cleaned_section = re.sub(
        r'(aria-label=")\d+( planned articles")',
        rf'\g<1>{remaining_count}\2',
        cleaned_section,
        count=1,
    )
    return landing[:match.start()] + cleaned_section + match.group(2) + landing[match.end():]


def atomic_write(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(dir=path.parent, prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(data)
        os.replace(temporary, path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", type=Path, nargs="+")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--confirm-plan")
    args = parser.parse_args()
    articles = [article for input_path in args.inputs for article in parse_batch(input_path)]
    if len({article.slug for article in articles}) != len(articles):
        raise SystemExit("batch contains duplicate article slugs")
    configs = {}
    for article in articles:
        config = ARTICLE_CONFIG.get(article.slug)
        if not config:
            raise SystemExit(f"missing reviewed ARTICLE_CONFIG for {article.slug}")
        configs[article.slug] = config
    titles = title_map(ROOT, [article.title for article in articles])
    if set(titles) != set(RELATED):
        raise SystemExit(f"relationship map mismatch: missing={set(titles)-set(RELATED)}, extra={set(RELATED)-set(titles)}")
    outputs: dict[Path, str] = {}
    targets = {}
    for article in articles:
        subtitle, original_description, sections = split_article(article.body)
        target = ROOT / "biomed-basics" / f"{article.slug}.html"
        targets[article.slug] = target
        outputs[target] = page_html(article.title, subtitle, configs[article.slug]["description"], original_description, sections, titles)
    for slug in RELATED:
        path = ROOT / "biomed-basics" / f"{slug}.html"
        if slug in targets:
            continue
        outputs[path] = replace_related(path.read_text(encoding="utf-8"), related_section(slug, titles))
    catalog_path = ROOT / "data" / "biomed-basics.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    if not isinstance(catalog, list):
        raise SystemExit("data/biomed-basics.json must contain a list")
    catalog_by_slug = {item.get("slug"): item for item in catalog if isinstance(item, dict)}
    if len(catalog_by_slug) != len(catalog):
        raise SystemExit("data/biomed-basics.json contains an invalid or duplicate slug")
    for article in articles:
        catalog_by_slug[article.slug] = catalog_entry(
            article.title, article.slug, configs[article.slug], catalog_by_slug.get(article.slug)
        )
    catalog = sorted(catalog_by_slug.values(), key=lambda item: (item["group"], item["title"].casefold()))
    outputs[catalog_path] = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"

    landing = (ROOT / "biomed-basics.html").read_text(encoding="utf-8")
    published_titles = set(titles.values())
    for config in configs.values():
        published_titles.update(config.get("plannedTitles", []))
    landing = remove_published_planned_topics(landing, published_titles)
    outputs[ROOT / "biomed-basics.html"] = landing
    sitemap_path = ROOT / "sitemap.xml"
    sitemap = sitemap_path.read_text(encoding="utf-8")
    for article in articles:
        article_href = f"biomed-basics/{article.slug}.html"
        canonical = f"{SITE_URL}/{article_href}"
        if sitemap.count(canonical) == 0:
            next_entry = f"<url>\n<loc>{SITE_URL}/biomed-basics.html</loc>\n</url>"
            compact_entry = f"<url><loc>{SITE_URL}/biomed-basics.html</loc></url>"
            if next_entry in sitemap:
                addition = f"<url>\n<loc>{canonical}</loc>\n</url>\n"
                sitemap = sitemap.replace(next_entry, addition + next_entry, 1)
            elif compact_entry in sitemap:
                addition = f"<url><loc>{canonical}</loc></url>"
                sitemap = sitemap.replace(compact_entry, compact_entry + addition, 1)
            else:
                raise SystemExit("expected Biomed Basics sitemap insertion point not found")
        elif sitemap.count(canonical) != 1:
            raise SystemExit("new article canonical appears more than once in sitemap")
    outputs[sitemap_path] = sitemap
    digest_input = "".join(
        f"{path.relative_to(ROOT).as_posix()}\0{data}\0"
        for path, data in sorted(outputs.items(), key=lambda item: item[0].as_posix())
    )
    digest = hashlib.sha256(digest_input.encode("utf-8")).hexdigest()
    print("Biomed Basics publication plan")
    for path in outputs:
        print(f"  {'CREATE' if not path.exists() else 'UPDATE'} {path.relative_to(ROOT)}")
    print(f"Plan digest: {digest}")
    if not args.write:
        print("DRY RUN — NO FILES WRITTEN")
        return 0
    if args.confirm_plan != digest:
        raise SystemExit("--write requires --confirm-plan with the complete current dry-run digest")
    for path, data in outputs.items():
        atomic_write(path, data)
    print(f"WROTE {len(outputs)} FILES")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
