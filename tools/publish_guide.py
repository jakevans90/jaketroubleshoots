#!/usr/bin/env python3
"""Validate and plan publication of one guide. This version never writes site data."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FIELDS = {"schemaVersion", "title", "issueTitle", "description", "assetType", "manufacturer", "model", "slug", "dateAdded", "taxonomyMode", "ccr", "helpfulDetails"}
OPTIONAL_FIELDS = {"newAsset", "newManufacturer", "newModel"}
SECTIONS = ["What This Guide Helps With", "Step-by-Step Troubleshooting", "If the Problem Persists", "Clinical Use Tip", "Work Order Documentation (CCR Method)", "Helpful Details to Include (If Known)", "Final Thought"]


class InputError(ValueError):
    pass


def scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return {}
    if value[0:1] in {'"', "'"}:
        if len(value) < 2 or value[-1] != value[0]:
            raise InputError("unterminated quoted YAML value")
        return json.loads(value) if value[0] == '"' else value[1:-1].replace("''", "'")
    value = re.sub(r"\s+#.*$", "", value).strip()
    if value in ("true", "false"):
        return value == "true"
    if re.fullmatch(r"\d+", value):
        return int(value)
    return value


def parse_yaml(text: str) -> dict[str, Any]:
    """Parse the intentionally small YAML subset used by guide inputs."""
    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]
    keys: dict[int, set[str]] = {}
    for number, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if indent % 2:
            raise InputError(f"front matter line {number}: indentation must use pairs of spaces")
        while stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        line = raw.strip()
        if line.startswith("- "):
            if not isinstance(parent, list):
                raise InputError(f"front matter line {number}: list item in a mapping")
            parent.append(scalar(line[2:]))
            continue
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9]*):(?:\s*(.*))?", line)
        if not match or not isinstance(parent, dict):
            raise InputError(f"front matter line {number}: unsupported YAML")
        key, raw_value = match.groups()
        seen = keys.setdefault(id(parent), set())
        if key in seen:
            raise InputError(f"front matter line {number}: duplicate key {key!r}")
        seen.add(key)
        value = scalar(raw_value or "")
        # Empty helpfulDetails is the only required list container; object children are mappings.
        if value == {} and key == "helpfulDetails":
            value = []
        parent[key] = value
        if isinstance(value, (dict, list)):
            stack.append((indent, value))
    return root


def parse_input(path: Path) -> tuple[dict[str, Any], dict[str, str], list[dict[str, str]]]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise InputError("input must be UTF-8") from exc
    match = re.fullmatch(r"---\r?\n(.*?)\r?\n---\r?\n(.*)", text, re.S)
    if not match:
        raise InputError("input must begin with YAML front matter delimited by ---")
    meta = parse_yaml(match.group(1))
    unknown = set(meta) - REQUIRED_FIELDS - OPTIONAL_FIELDS
    missing = REQUIRED_FIELDS - set(meta)
    if unknown:
        raise InputError("unknown front matter fields: " + ", ".join(sorted(unknown)))
    if missing:
        raise InputError("missing front matter fields: " + ", ".join(sorted(missing)))
    headings = list(re.finditer(r"^## (.+?)\s*$", match.group(2), re.M))
    sections: dict[str, str] = {}
    for i, heading in enumerate(headings):
        name = heading.group(1)
        if name in sections:
            raise InputError(f"duplicate required section: {name}")
        sections[name] = match.group(2)[heading.end():headings[i + 1].start() if i + 1 < len(headings) else None].strip()
    absent = [name for name in SECTIONS if not sections.get(name)]
    if absent:
        raise InputError("missing or empty required sections: " + ", ".join(absent))
    steps = []
    step_text = sections[SECTIONS[1]]
    step_heads = list(re.finditer(r"^### (\d+)\.\s+(.+?)\s*$", step_text, re.M))
    for i, heading in enumerate(step_heads):
        body = step_text[heading.end():step_heads[i + 1].start() if i + 1 < len(step_heads) else None].strip()
        if "Expected outcome:" not in body:
            raise InputError(f"troubleshooting step {heading.group(1)} is missing explicit 'Expected outcome:' text")
        steps.append({"number": heading.group(1), "title": heading.group(2), "body": body})
    if not steps or [s["number"] for s in steps] != [str(i) for i in range(1, len(steps) + 1)]:
        raise InputError("troubleshooting steps must use consecutive '### 1. Title' headings")
    return meta, sections, steps


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


@dataclass
class Plan:
    meta: dict[str, Any]
    resolved: dict[str, str] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    duplicates: list[str] = field(default_factory=list)
    files: list[str] = field(default_factory=list)
    new_records: dict[str, bool] = field(default_factory=dict)
    target_shard: str = ""
    new_shard: bool = False


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def resolve_one(plan: Plan, field_name: str, registry: list[dict[str, Any]], new_key: str) -> None:
    supplied = str(plan.meta[field_name])
    exact = [r for r in registry if r.get("name") == supplied]
    normalized = [r for r in registry if norm(str(r.get("name", ""))) == norm(supplied)]
    if len(exact) == 1:
        plan.resolved[field_name] = exact[0]["name"]
        plan.new_records[field_name] = False
    elif not exact and len(normalized) == 1:
        plan.errors.append(f"{field_name} is noncanonical: {supplied!r}; possible canonical match: {normalized[0]['name']!r}")
        plan.warnings.append(f"normalized-name match for {field_name}: {supplied!r} -> {normalized[0]['name']!r}")
    elif plan.meta["taxonomyMode"] == "create-missing" and isinstance(plan.meta.get(new_key), dict) and plan.meta[new_key].get("name") == supplied:
        plan.resolved[field_name] = supplied
        plan.new_records[field_name] = True
        plan.errors.append(f"new {field_name} record requires schema review before publishing")
    else:
        candidates = difflib.get_close_matches(norm(supplied), [norm(str(r.get("name", ""))) for r in registry], n=3, cutoff=.72)
        names = [r["name"] for r in registry if norm(str(r.get("name", ""))) in candidates]
        plan.errors.append(f"cannot resolve canonical {field_name} {supplied!r}" + (f"; possible matches: {', '.join(names)}" if names else ""))


def build_plan(meta: dict[str, Any], root: Path = ROOT) -> Plan:
    plan = Plan(meta)
    if meta["schemaVersion"] != 1:
        plan.errors.append("schemaVersion must be 1")
    if meta["taxonomyMode"] not in ("reuse", "create-missing"):
        plan.errors.append("taxonomyMode must be reuse or create-missing")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(meta["slug"])):
        plan.errors.append("slug must contain lowercase ASCII words separated by hyphens")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(meta["dateAdded"])):
        plan.errors.append("dateAdded must use YYYY-MM-DD")
    ccr = meta.get("ccr")
    if not isinstance(ccr, dict) or set(ccr) != {"complaint", "cause", "resolution"} or not all(ccr.values()):
        plan.errors.append("ccr must contain nonempty complaint, cause, and resolution")
    if not isinstance(meta.get("helpfulDetails"), list) or not meta["helpfulDetails"]:
        plan.errors.append("helpfulDetails must be a nonempty list")

    registries = {"assetType": load_json(root / "data/hub-asset.json"), "manufacturer": load_json(root / "data/hub-manufacturer.json"), "model": load_json(root / "data/hub-model.json")}
    resolve_one(plan, "assetType", registries["assetType"], "newAsset")
    resolve_one(plan, "manufacturer", registries["manufacturer"], "newManufacturer")
    resolve_one(plan, "model", registries["model"], "newModel")
    if all(k in plan.resolved for k in registries):
        matching_model = [r for r in registries["model"] if r.get("name") == plan.resolved["model"]]
        for record in matching_model:
            profile = record.get("profile", {})
            if profile.get("manufacturer") != plan.resolved["manufacturer"] or profile.get("assetType") != plan.resolved["assetType"]:
                plan.errors.append("model registry links do not match the resolved manufacturer and asset type")

    manifest = load_json(root / "data/guides.json")
    if len(manifest) != len(set(manifest)):
        plan.errors.append("data/guides.json contains duplicate shard registrations")
    guides: list[tuple[str, dict[str, Any]]] = []
    for shard in manifest:
        path = root / shard
        if not path.is_file():
            plan.errors.append(f"registered manufacturer shard is missing: {shard}")
            continue
        guides.extend((shard, guide) for guide in load_json(path))
    canonical_sets = {name: {r.get("name") for r in records} for name, records in registries.items()}
    for shard, guide in guides:
        for field_name in ("assetType", "manufacturer", "model"):
            if guide.get(field_name) not in canonical_sets[field_name]:
                plan.errors.append(f"missing taxonomy record for existing guide in {shard}: {field_name}={guide.get(field_name)!r}")
    registered = set(manifest)
    for path in (root / "data").glob("guides-*.json"):
        rel = path.relative_to(root).as_posix()
        if rel not in registered:
            plan.warnings.append(f"unregistered manufacturer shard: {rel}")

    slug = str(meta["slug"])
    html_path = f"guides/{slug}.html"
    canonical = f"https://jaketroubleshoots.com/{html_path}"
    manufacturer_slug = re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", str(plan.resolved.get("manufacturer", meta["manufacturer"])).casefold()))
    plan.target_shard = f"data/guides-{manufacturer_slug}.json"
    plan.new_shard = plan.target_shard not in registered
    plan.files = [html_path, plan.target_shard]
    if plan.new_shard:
        plan.files.append("data/guides.json")
    for field_name, required in (("assetType", "data/hub-asset.json"), ("manufacturer", "data/hub-manufacturer.json"), ("model", "data/hub-model.json")):
        if plan.new_records.get(field_name):
            plan.files.append(required)
    plan.files.append("sitemap.xml")

    sitemap_urls = {node.text for node in ET.parse(root / "sitemap.xml").iter() if node.tag.endswith("loc")}
    html_canonicals: dict[str, list[str]] = {}
    canonical_pattern = re.compile(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)', re.I)
    for html in (root / "guides").glob("*.html"):
        found = canonical_pattern.search(html.read_text(encoding="utf-8", errors="replace"))
        if found:
            html_canonicals.setdefault(found.group(1), []).append(html.relative_to(root).as_posix())
    seen_identity: dict[tuple[str, str, str], list[str]] = {}
    for shard, guide in guides:
        title, url = str(guide.get("title", "")), str(guide.get("url", ""))
        existing_canonical = "https://jaketroubleshoots.com/" + url.lstrip("/")
        reasons = []
        if title == meta["title"]: reasons.append("title")
        elif norm(title) == norm(str(meta["title"])): reasons.append("normalized title")
        if url == html_path: reasons.extend(["slug/HTML path", "JSON URL"])
        if existing_canonical == canonical: reasons.append("canonical URL")
        identity = (norm(str(guide.get("manufacturer", ""))), norm(str(guide.get("model", ""))), norm(title.split(" - ", 1)[-1]))
        wanted = (norm(str(meta["manufacturer"])), norm(str(meta["model"])), norm(str(meta["issueTitle"])))
        ratio = difflib.SequenceMatcher(None, identity[2], wanted[2]).ratio()
        if identity[:2] == wanted[:2] and ratio >= .78:
            reasons.append(f"manufacturer/model/issue near-match ({ratio:.0%})")
        if reasons:
            plan.duplicates.append(f"{title} [{shard}]: {', '.join(dict.fromkeys(reasons))}")
    if canonical in sitemap_urls:
        plan.duplicates.append(f"sitemap already contains {canonical}")
    if canonical in html_canonicals:
        plan.duplicates.append(f"canonical URL is already used by: {', '.join(html_canonicals[canonical])}")
    if (root / html_path).exists():
        plan.duplicates.append(f"HTML file already exists: {html_path}")
    if plan.duplicates:
        plan.errors.append("duplicate resolution is uncertain; review the reported candidates")
    return plan


def report(plan: Plan) -> str:
    status = "BLOCKED" if plan.errors else "READY (dry run only)"
    lines = ["Guide publisher dry run", "=======================", f"Status: {status}", "Mode: dry-run (no files written)", "", "Resolved canonical taxonomy:"]
    for name in ("assetType", "manufacturer", "model"):
        lines.append(f"  {name}: {plan.resolved.get(name, 'UNRESOLVED')}")
    slug = plan.meta["slug"]
    lines += ["", f"Target HTML path: guides/{slug}.html", f"Target manufacturer shard: {plan.target_shard}", f"New shard required: {'yes' if plan.new_shard else 'no'}", "New taxonomy records required:"]
    lines.extend(f"  {name}: {'yes' if plan.new_records.get(name) else 'no'}" for name in ("assetType", "manufacturer", "model"))
    lines += [f"Expected sitemap addition: https://jaketroubleshoots.com/guides/{slug}.html", "", "Files that a future write mode would create/change:"]
    lines.extend(f"  - {name}" for name in dict.fromkeys(plan.files))
    for heading, values in (("Validation errors", plan.errors), ("Warnings", plan.warnings), ("Possible duplicate matches", plan.duplicates)):
        lines += ["", f"{heading}:"]
        lines.extend([f"  - {value}" for value in values] or ["  (none)"])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="one UTF-8 Markdown guide")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    try:
        meta, _sections, _steps = parse_input(args.input)
        plan = build_plan(meta, args.root)
        print(report(plan))
        return 2 if plan.errors else 0
    except (InputError, OSError, json.JSONDecodeError, ET.ParseError) as exc:
        print(f"Guide publisher dry run\nStatus: BLOCKED\nValidation errors:\n  - {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
