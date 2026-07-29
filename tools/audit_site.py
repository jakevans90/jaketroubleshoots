#!/usr/bin/env python3
"""Read-only structural quality audit for Jake Troubleshoots guide content."""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

BASE_URL = "https://jaketroubleshoots.com"
REQUIRED_FIELDS = {
    "title", "description", "assetType", "manufacturer", "model", "url",
    "dateAdded", "steps", "documentation", "helpfulDetails",
}
REQUIRED_HEADINGS = {
    "asset type", "manufacturer", "model", "what this guide helps with",
    "step-by-step troubleshooting", "if the problem persists",
    "work order documentation (ccr method)", "helpful details to include",
}
SHARED_SCRIPTS = {"related-guides.js", "hub-links.js", "feedback.js", "guide-icons.js"}
SEVERITY_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}


def compact(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def normalized(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", "", compact(value).casefold())


def slugify(value: object) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", compact(value).casefold())).strip("-")


@dataclass(frozen=True)
class Finding:
    severity: str
    issue_type: str
    file: str
    title_or_url: str
    explanation: str
    recommended_correction: str
    manufacturer: str = ""
    model: str = ""


class GuideParser(HTMLParser):
    """Collect structural facts without interpreting guide instructions."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.titles: list[str] = []
        self.descriptions: list[str] = []
        self.canonicals: list[str] = []
        self.headings: list[str] = []
        self.paragraphs: list[str] = []
        self.scripts: list[str] = []
        self.ids: set[str] = set()
        self.list_errors: list[str] = []
        self._capture: str | None = None
        self._buffer: list[str] = []
        self._list_stack: list[str] = []
        self._li_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "meta" and (values.get("name") or "").casefold() == "description":
            self.descriptions.append(compact(values.get("content")))
        if tag == "link" and (values.get("rel") or "").casefold() == "canonical":
            self.canonicals.append(compact(values.get("href")))
        if tag == "script" and values.get("src"):
            self.scripts.append(values["src"] or "")
        if tag in {"title", "h1", "h2", "h3", "h4", "h5", "h6", "p"}:
            self._capture, self._buffer = tag, []
        if tag in {"ul", "ol"}:
            self._list_stack.append(tag)
        if tag == "li":
            if not self._list_stack:
                self.list_errors.append("list item outside a ul or ol")
            self._li_depth += 1

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "li":
            self._li_depth = max(0, self._li_depth - 1)
        if tag in {"ul", "ol"}:
            if self._list_stack and self._list_stack[-1] == tag:
                self._list_stack.pop()
            else:
                self.list_errors.append(f"unbalanced {tag} list")
        if tag == self._capture:
            text = compact("".join(self._buffer))
            if tag == "title":
                self.titles.append(text)
            elif tag.startswith("h"):
                self.headings.append(text)
            elif tag == "p":
                self.paragraphs.append(text)
            self._capture, self._buffer = None, []


class SiteAuditor:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.findings: list[Finding] = []
        self.records: list[tuple[str, int, dict]] = []
        self.records_by_url: dict[str, list[tuple[str, int, dict]]] = defaultdict(list)
        self.listed_shards: list[str] = []
        self.hubs: dict[str, list[dict]] = {}

    def add(self, severity: str, issue: str, file: str, subject: str,
            explanation: str, correction: str, record: dict | None = None) -> None:
        record = record or {}
        self.findings.append(Finding(
            severity, issue, file.replace("\\", "/"), compact(subject),
            compact(explanation), compact(correction),
            compact(record.get("manufacturer")), compact(record.get("model")),
        ))

    def load_json(self, rel: str, severity: str = "Critical") -> object | None:
        path = self.root / rel
        if not path.is_file():
            self.add(severity, "missing_file", rel, rel, "Required JSON file does not exist.",
                     "Create or restore the required file and register it where applicable.")
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            self.add("Critical", "invalid_json", rel, rel, f"JSON cannot be parsed: {exc}.",
                     "Correct the JSON syntax without changing guide content.")
            return None

    def audit(self) -> dict:
        self._load_hubs()
        self._load_records()
        self._audit_records()
        self._audit_html()
        self._audit_sitemap()
        self._audit_taxonomy()
        self.findings.sort(key=lambda f: (
            SEVERITY_ORDER[f.severity], f.issue_type, f.file, f.title_or_url
        ))
        return self.result()

    def _load_hubs(self) -> None:
        for kind in ("asset", "manufacturer", "model"):
            rel = f"data/hub-{kind}.json"
            value = self.load_json(rel)
            if value is not None and not isinstance(value, list):
                self.add("Critical", "invalid_json_shape", rel, rel, "Hub JSON must contain a list.",
                         "Change the top-level JSON structure to a list.")
                value = []
            self.hubs[kind] = value or []

    def _load_records(self) -> None:
        index = self.load_json("data/guides.json")
        if index is None:
            return
        if not isinstance(index, list):
            self.add("Critical", "invalid_json_shape", "data/guides.json", "data/guides.json",
                     "Guide index must contain a list of shard paths.",
                     "Change the top-level JSON structure to a list.")
            return
        self.listed_shards = [x for x in index if isinstance(x, str)]
        for rel in self.listed_shards:
            data = self.load_json(rel)
            if data is None:
                continue
            if not isinstance(data, list):
                self.add("Critical", "invalid_json_shape", rel, rel,
                         "Guide shard must contain a list.", "Change the top-level value to a list.")
                continue
            for index, record in enumerate(data):
                if not isinstance(record, dict):
                    self.add("Critical", "invalid_guide_record", rel, f"record {index}",
                             "Guide record is not an object.", "Replace it with a guide object.")
                    continue
                self.records.append((rel, index, record))
                if isinstance(record.get("url"), str):
                    self.records_by_url[record["url"]].append((rel, index, record))
        registered = {Path(x).as_posix() for x in self.listed_shards}
        for path in sorted((self.root / "data").glob("guides-*.json")):
            rel = path.relative_to(self.root).as_posix()
            if rel not in registered:
                self.add("Critical", "unregistered_manufacturer_shard", rel, rel,
                         "Manufacturer guide shard is not listed in data/guides.json.",
                         "Register the shard in data/guides.json.")

    def _audit_records(self) -> None:
        title_groups: dict[str, list[tuple[str, dict]]] = defaultdict(list)
        combo_groups: dict[tuple[str, str, str], list[tuple[str, dict]]] = defaultdict(list)
        for rel, index, record in self.records:
            subject = record.get("title") or record.get("url") or f"record {index}"
            missing = sorted(k for k in REQUIRED_FIELDS if k not in record)
            empty = sorted(k for k in REQUIRED_FIELDS if k in record and record[k] in ("", None, []))
            if missing or empty:
                detail = ", ".join([*(f"missing {x}" for x in missing), *(f"empty {x}" for x in empty)])
                self.add("High", "missing_required_guide_fields", rel, subject, detail,
                         "Populate the required structural fields.", record)
            url = record.get("url")
            if isinstance(url, str) and not (self.root / url).is_file():
                self.add("Critical", "json_url_missing_html", rel, url,
                         "The JSON URL does not resolve to an HTML file.",
                         "Create the matching guide HTML or remove/correct the record.", record)
            ccr = record.get("documentation", {}).get("CCR") if isinstance(record.get("documentation"), dict) else None
            if not isinstance(ccr, dict) or any(not compact(ccr.get(x)) for x in ("Complaint", "Cause", "Resolution")):
                self.add("High", "missing_or_malformed_ccr", rel, subject,
                         "documentation.CCR must contain non-empty Complaint, Cause, and Resolution strings.",
                         "Restore the required CCR object structure without paraphrasing its content.", record)
            details = record.get("helpfulDetails")
            if not isinstance(details, list) or not details or any(not compact(x) for x in details):
                self.add("High", "missing_or_empty_helpful_details", rel, subject,
                         "helpfulDetails must be a non-empty array of non-empty values.",
                         "Restore the helpfulDetails array structure.", record)
            title_groups[normalized(record.get("title"))].append((rel, record))
            combo_groups[tuple(normalized(record.get(x)) for x in ("manufacturer", "model", "title"))].append((rel, record))
            manufacturer_hub = next(
                (x for x in self.hubs["manufacturer"]
                 if isinstance(x, dict) and normalized(x.get("name")) == normalized(record.get("manufacturer"))),
                {},
            )
            expected_shard = f"data/guides-{manufacturer_hub.get('slug') or slugify(record.get('manufacturer'))}.json"
            if compact(record.get("manufacturer")) and rel != expected_shard:
                self.add("High", "wrong_manufacturer_shard", rel, subject,
                         f"Manufacturer maps to {expected_shard}, but record is stored in {rel}.",
                         "Move the unchanged record to its manufacturer shard.", record)
        self._duplicates(title_groups, "duplicate_title", "Guide title is duplicated.")
        self._duplicates(self.records_by_url, "duplicate_url", "Guide URL is duplicated.")
        self._duplicates(combo_groups, "duplicate_manufacturer_model_issue",
                         "Normalized manufacturer/model/issue combination is duplicated.")
        for url, members in self.records_by_url.items():
            shards = {x[0] for x in members}
            if len(shards) > 1:
                for rel, _, record in members:
                    self.add("High", "duplicate_guide_across_shards", rel, url,
                             f"The same guide URL occurs across shards: {sorted(shards)!r}.",
                             "Keep the unchanged record in only its canonical manufacturer shard.", record)

    def _duplicates(self, groups: dict, issue: str, explanation: str) -> None:
        for _, members in groups.items():
            if len(members) < 2 or not _:
                continue
            for member in members:
                rel, record = member[0], member[-1]
                self.add("High", issue, rel, record.get("title") or record.get("url"),
                         explanation, "Keep one canonical record and remove duplicate registration.", record)

    def _audit_html(self) -> None:
        html_paths = sorted((self.root / "guides").rglob("*.html"))
        html_urls = {p.relative_to(self.root).as_posix() for p in html_paths}
        for url in sorted(html_urls - set(self.records_by_url)):
            self.add("Critical", "html_without_json_record", url, url,
                     "Guide HTML has no record in the registered JSON shards.",
                     "Add the guide to the correct registered manufacturer shard.")
        for path in html_paths:
            rel = path.relative_to(self.root).as_posix()
            raw = path.read_text(encoding="utf-8", errors="replace")
            parser = GuideParser()
            parser.feed(raw)
            record = self.records_by_url.get(rel, [(None, None, {})])[0][2]
            subject = record.get("title") or rel
            self._check_count(parser.titles, 1, "title_tag", rel, subject, record)
            if len(parser.titles) == 1 and record.get("title") and compact(parser.titles[0]) != compact(record["title"]):
                self.add("High", "title_mismatch_html_json", rel, subject,
                         f"HTML title is {parser.titles[0]!r}; JSON title is {record['title']!r}.",
                         "Make the HTML and JSON titles identical.", record)
            self._check_count(parser.descriptions, 1, "meta_description", rel, subject, record)
            if len(parser.descriptions) == 1 and record.get("description") and compact(parser.descriptions[0]) != compact(record["description"]):
                self.add("High", "meta_description_mismatch", rel, subject,
                         "HTML meta description differs from the guide JSON description.",
                         "Use the guide's matching JSON description in the HTML metadata.", record)
            if len(parser.descriptions) == 1 and record:
                description_key = normalized(parser.descriptions[0])
                expected_model = normalized(record.get("model"))
                other_models = sorted({
                    compact(other.get("model")) for _, _, other in self.records
                    if normalized(other.get("model")) not in ("", expected_model)
                    and len(normalized(other.get("model"))) >= 5
                    and normalized(other.get("model")) in description_key
                })
                if expected_model and expected_model not in description_key and other_models:
                    self.add("High", "unrelated_metadata_wording", rel, subject,
                             f"Meta description omits the expected model and names other known model(s): {other_models[:5]!r}.",
                             "Replace stale metadata with wording for this guide's model and issue.", record)
            self._check_count(parser.canonicals, 1, "canonical_url", rel, subject, record, "Critical")
            expected = f"{BASE_URL}/{rel}"
            if len(parser.canonicals) == 1:
                canonical = parser.canonicals[0]
                parsed = urlparse(canonical)
                if parsed.scheme != "https" or parsed.netloc != "jaketroubleshoots.com" or canonical != expected:
                    self.add("Critical", "incorrect_canonical_url", rel, subject,
                             f"Canonical is {canonical!r}; expected {expected!r}.",
                             "Set one absolute canonical URL matching the HTML filename and JSON URL.", record)
            headings = [compact(x) for x in parser.headings]
            heading_counts = Counter(x.casefold() for x in headings if x)
            for heading, count in heading_counts.items():
                if count > 1:
                    self.add("Medium", "duplicate_section_heading", rel, subject,
                             f"Heading {heading!r} appears {count} times.",
                             "Keep one structural heading for that section.", record)
            for heading in sorted(REQUIRED_HEADINGS - set(heading_counts)):
                self.add("Medium", "missing_required_section", rel, subject,
                         f"Required heading {heading!r} is absent.",
                         "Add the missing standard section without changing existing guide content.", record)
            if any(not x for x in parser.headings):
                self.add("Low", "empty_heading", rel, subject, "One or more headings are empty.",
                         "Remove empty headings or supply the intended structural label.", record)
            if any(not x for x in parser.paragraphs):
                self.add("Low", "empty_paragraph", rel, subject, "One or more paragraphs are empty.",
                         "Remove empty spacing paragraphs and use layout styles.", record)
            ccr_count = len(re.findall(r"CCR\s*=\s*Complaint\s*,\s*Cause\s*,\s*Resolution", html.unescape(raw), re.I))
            if ccr_count > 1:
                self.add("Medium", "duplicate_ccr_label", rel, subject,
                         f"The CCR definition appears {ccr_count} times.", "Keep one CCR definition line.", record)
            if re.search(r"&lt;!--.*?--&gt;", raw, re.I | re.S):
                self.add("Medium", "escaped_instructional_comment", rel, subject,
                         "Escaped HTML comment markup may be visible to readers.",
                         "Convert it to a real comment or remove the template instruction.", record)
            if re.search(r"\b(?:TODO|TBD|INSERT\s+(?:TEXT|CONTENT)|REPLACE\s+THIS|LOREM IPSUM)\b|\[(?:INSERT|TODO|PLACEHOLDER)[^\]]*\]", raw, re.I):
                self.add("High", "placeholder_or_template_instruction", rel, subject,
                         "Explicit placeholder or template instruction is present.",
                         "Replace or remove the visible template marker.", record)
            if parser.list_errors:
                self.add("Low", "malformed_list", rel, subject, "; ".join(sorted(set(parser.list_errors))),
                         "Repair list nesting and containment markup.", record)
            bulletish = sum(bool(re.match(r"^\s*(?:[-*•]|\d+[.)])\s+", x)) for x in parser.paragraphs)
            if bulletish >= 2:
                self.add("Low", "likely_paragraph_based_list", rel, subject,
                         f"{bulletish} paragraph elements begin with bullet-like markers.",
                         "Use semantic ul/ol and li markup if these paragraphs are a list.", record)
            if "related-guides-grid" not in parser.ids:
                self.add("High", "missing_related_guides_mount", rel, subject,
                         "The related-guides mount point is absent.", "Add the standard related-guides-grid mount.", record)
            script_names = {Path(urlparse(x).path).name for x in parser.scripts}
            missing_scripts = sorted(SHARED_SCRIPTS - script_names)
            if missing_scripts:
                self.add("High", "missing_shared_script", rel, subject,
                         f"Missing shared scripts: {', '.join(missing_scripts)}.",
                         "Include the standard shared guide scripts.", record)
            if not re.search(r"<footer\b", raw, re.I):
                self.add("Medium", "missing_standard_footer", rel, subject,
                         "Guide has no footer element.", "Add the standard site footer.", record)
            if "Guides intended for trained personnel only." not in raw:
                self.add("Medium", "missing_trained_personnel_disclaimer", rel, subject,
                         "The standard trained-personnel disclaimer is absent.",
                         "Add the standard disclaimer verbatim in the footer.", record)
            # Conservative expected-outcome heuristic: structure only, never correctness.
            steps = record.get("steps") if isinstance(record.get("steps"), list) else []
            if steps and not any(re.search(r"\b(expected|verify|confirm|observe|should|successful|passes?|functional)\b",
                                           compact(s.get("instructions")), re.I)
                                 for s in steps if isinstance(s, dict)):
                self.add("Medium", "missing_expected_outcome_statement", rel, subject,
                         "No step contains a recognizable expected/verification outcome marker.",
                         "Add an explicit expected-outcome statement without changing technical meaning.", record)

    def _check_count(self, values: list[str], expected: int, kind: str, rel: str,
                     subject: str, record: dict, severity: str = "High") -> None:
        if len(values) != expected or (values and not values[0]):
            issue = f"missing_{kind}" if not values or (len(values) == 1 and not values[0]) else f"duplicate_{kind}"
            self.add(severity, issue, rel, subject, f"Found {len(values)} usable {kind.replace('_', ' ')} values; expected one.",
                     f"Provide exactly one non-empty {kind.replace('_', ' ')}.", record)

    def _sitemap_locs(self) -> list[str]:
        path = self.root / "sitemap.xml"
        try:
            tree = ET.parse(path)
        except (OSError, ET.ParseError) as exc:
            self.add("Critical", "invalid_sitemap", "sitemap.xml", "sitemap.xml",
                     f"Sitemap cannot be parsed: {exc}.", "Correct the sitemap XML structure.")
            return []
        return [compact(node.text) for node in tree.findall(".//{*}loc")]

    def _audit_sitemap(self) -> None:
        locs = self._sitemap_locs()
        counts = Counter(locs)
        for url, count in counts.items():
            if url and count > 1:
                self.add("Critical", "duplicate_sitemap_url", "sitemap.xml", url,
                         f"URL occurs {count} times.", "Keep one sitemap entry for the URL.")
        for rel, members in self.records_by_url.items():
            record = members[0][2]
            expected = f"{BASE_URL}/{rel}"
            accepted = {expected, expected.removesuffix(".html")}
            if not accepted.intersection(locs):
                self.add("Critical", "guide_absent_from_sitemap", "sitemap.xml", rel,
                         "Registered guide is absent from sitemap.xml.",
                         "Add its canonical guide URL to sitemap.xml.", record)
        for url in locs:
            parsed = urlparse(url)
            if parsed.netloc not in ("jaketroubleshoots.com", "www.jaketroubleshoots.com"):
                continue
            rel = parsed.path.lstrip("/")
            candidates = [self.root / rel]
            if not Path(rel).suffix:
                candidates.extend([self.root / f"{rel}.html", self.root / rel / "index.html"])
            if rel and not any(x.is_file() for x in candidates):
                self.add("Critical", "sitemap_url_missing_file", "sitemap.xml", url,
                         "Sitemap URL has no matching local file.", "Remove the stale URL or restore its file.")

    def _audit_taxonomy(self) -> None:
        canonical = {
            "assetType": {normalized(x.get("name")): compact(x.get("name")) for x in self.hubs["asset"] if isinstance(x, dict)},
            "manufacturer": {normalized(x.get("name")): compact(x.get("name")) for x in self.hubs["manufacturer"] if isinstance(x, dict)},
            "model": {normalized(x.get("name")): compact(x.get("name")) for x in self.hubs["model"] if isinstance(x, dict)},
        }
        observed: dict[str, dict[str, set[str]]] = {x: defaultdict(set) for x in canonical}
        for rel, _, record in self.records:
            for field in canonical:
                value = compact(record.get(field))
                key = normalized(value)
                observed[field][key].add(value)
                if key not in canonical[field]:
                    self.add("High", "missing_hub_taxonomy_record", rel, record.get("title") or record.get("url"),
                             f"{field} value {value!r} has no canonical hub record.",
                             f"Add the missing hub record or use an existing canonical {field} spelling.", record)
                elif value != canonical[field][key]:
                    self.add("High", "noncanonical_taxonomy_spelling", rel, record.get("title") or record.get("url"),
                             f"{field} is {value!r}; canonical spelling is {canonical[field][key]!r}.",
                             "Use the canonical hub spelling.", record)
        for field, groups in observed.items():
            for values in groups.values():
                if len(values) > 1:
                    for value in sorted(values):
                        self.add("High", "normalized_taxonomy_duplicate", f"data/hub-{field.replace('Type', '').lower()}.json",
                                 value, f"Values normalize to the same {field}: {sorted(values)!r}.",
                                 "Choose one canonical spelling across hubs and guide JSON.")
        model_slugs: dict[str, list[dict]] = defaultdict(list)
        for model in self.hubs["model"]:
            if not isinstance(model, dict):
                continue
            model_slugs[compact(model.get("slug"))].append(model)
            for field, hub_kind in (("manufacturer", "manufacturer"), ("assetType", "assetType")):
                value = compact((model.get("profile") or {}).get(field)) if isinstance(model.get("profile"), dict) else ""
                key = normalized(value)
                if value and key not in canonical[hub_kind]:
                    self.add("High", "model_noncanonical_taxonomy_link", "data/hub-model.json", model.get("name"),
                             f"Model links to unknown {field} {value!r}.",
                             f"Link the model to a canonical {field} hub value.")
                elif value and value != canonical[hub_kind][key]:
                    self.add("High", "model_noncanonical_taxonomy_link", "data/hub-model.json", model.get("name"),
                             f"Model uses {value!r}; canonical {field} is {canonical[hub_kind][key]!r}.",
                             f"Use the canonical {field} spelling.")
        for slug, models in model_slugs.items():
            if slug and len(models) > 1:
                self.add("High", "model_slug_collision", "data/hub-model.json", slug,
                         f"Slug is shared by models: {[x.get('name') for x in models]!r}.",
                         "Assign unique canonical model slugs.")

    def result(self) -> dict:
        by_issue = Counter(x.issue_type for x in self.findings)
        by_severity = Counter(x.severity for x in self.findings)
        by_manufacturer = Counter(x.manufacturer or "(unattributed)" for x in self.findings)
        by_model = Counter(x.model or "(unattributed)" for x in self.findings)
        return {
            "schemaVersion": 1,
            "scope": {
                "guideHtmlFiles": len(list((self.root / "guides").rglob("*.html"))),
                "registeredShards": len(self.listed_shards),
                "guideRecords": len(self.records),
            },
            "summary": {
                "totalFindings": len(self.findings),
                "byIssueType": dict(sorted(by_issue.items())),
                "bySeverity": {x: by_severity[x] for x in SEVERITY_ORDER},
                "byManufacturer": dict(sorted(by_manufacturer.items())),
                "byModel": dict(sorted(by_model.items())),
            },
            "findings": [asdict(x) for x in self.findings],
        }


def markdown_report(result: dict) -> str:
    summary = result["summary"]
    lines = [
        "# Site Quality Audit", "",
        "> Structural audit only. Technical and clinical accuracy is outside this audit's scope.", "",
        "## Summary", "",
        f"- Guide HTML files: {result['scope']['guideHtmlFiles']}",
        f"- Registered JSON shards: {result['scope']['registeredShards']}",
        f"- Guide records: {result['scope']['guideRecords']}",
        f"- Total findings: {summary['totalFindings']}", "",
    ]
    for label, key in (("Severity", "bySeverity"), ("Issue type", "byIssueType"),
                       ("Manufacturer", "byManufacturer"), ("Model", "byModel")):
        lines.extend([f"### Counts by {label.lower()}", "", f"| {label} | Count |", "|---|---:|"])
        lines.extend(f"| {name.replace('|', '\\|')} | {count} |" for name, count in summary[key].items())
        lines.append("")
    for severity in SEVERITY_ORDER:
        findings = [x for x in result["findings"] if x["severity"] == severity]
        lines.extend([f"## {severity} ({len(findings)})", ""])
        if not findings:
            lines.extend(["No findings.", ""])
            continue
        for item in findings:
            lines.extend([
                f"### {item['issue_type']}: `{item['file']}`", "",
                f"- Guide: {item['title_or_url'] or '(not available)'}",
                f"- Explanation: {item['explanation']}",
                f"- Recommended structural correction: {item['recommended_correction']}", "",
            ])
    return "\n".join(lines).rstrip() + "\n"


def write_reports(root: Path, result: dict, json_path: Path, markdown_path: Path) -> None:
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown_path.write_text(markdown_report(result), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--markdown-output", type=Path)
    parser.add_argument("--no-write", action="store_true", help="Audit without writing report files.")
    parser.add_argument("--fail-on", choices=("none", "critical", "high", "medium", "low"), default="none")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    result = SiteAuditor(root).audit()
    if not args.no_write:
        json_path = args.json_output or root / "reports/site-quality-audit.json"
        md_path = args.markdown_output or root / "reports/site-quality-audit.md"
        write_reports(root, result, json_path, md_path)
    print(json.dumps({"scope": result["scope"], "summary": result["summary"]["bySeverity"],
                      "totalFindings": result["summary"]["totalFindings"]}, indent=2))
    if args.fail_on == "none":
        return 0
    threshold = SEVERITY_ORDER[args.fail_on.title()]
    return int(any(SEVERITY_ORDER[x["severity"]] <= threshold for x in result["findings"]))


if __name__ == "__main__":
    sys.exit(main())
