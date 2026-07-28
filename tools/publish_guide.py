#!/usr/bin/env python3
"""Plan or transactionally publish one reviewed troubleshooting guide."""

from __future__ import annotations

import argparse
import difflib
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FIELDS = {"schemaVersion", "title", "issueTitle", "description", "assetType", "manufacturer", "model", "slug", "dateAdded", "taxonomyMode", "ccr", "helpfulDetails"}
OPTIONAL_FIELDS = {"newAsset", "newManufacturer", "newModel"}
SECTIONS = ["What This Guide Helps With", "Step-by-Step Troubleshooting", "If the Problem Persists", "Clinical Use Tip", "Work Order Documentation (CCR Method)", "Helpful Details to Include (If Known)", "Final Thought"]
REGISTRIES = {"assetType": ("data/hub-asset.json", "newAsset"), "manufacturer": ("data/hub-manufacturer.json", "newManufacturer"), "model": ("data/hub-model.json", "newModel")}
RECORD_KEYS = {
    "assetType": {"type", "name", "slug", "icon", "url", "meta", "profile", "content", "stats", "flags"},
    "manufacturer": {"type", "name", "slug", "url", "meta", "profile", "content", "stats", "flags"},
    "model": {"type", "name", "slug", "url", "meta", "profile", "content", "stats", "flags"},
}
NESTED_RECORD_KEYS = {
    "assetType": {"meta": {"description", "keywords", "lastUpdated"}, "profile": {"blurb", "commonManufacturers", "relatedAssets", "clinicalSetting"}, "content": {"featuredGuides", "commonIssues", "tips", "warnings"}, "stats": {"guideCount", "manufacturerCount", "modelCount"}, "flags": {"exists", "featured", "verified"}},
    "manufacturer": {"meta": {"description", "keywords", "lastUpdated"}, "profile": {"blurb", "founded", "headquarters", "website", "vendorPage", "logo", "specialties"}, "content": {"featuredGuides", "pinnedModels", "commonIssues", "tips", "warnings"}, "stats": {"guideCount", "modelCount", "assetTypes"}, "flags": {"exists", "featured", "hasLogo", "hasVendorPage", "verified"}},
    "model": {"meta": {"description", "keywords", "lastUpdated"}, "profile": {"blurb", "manufacturer", "assetType", "website"}, "content": {"featuredGuides", "commonIssues", "tips", "warnings"}, "stats": {"guideCount"}, "flags": {"exists", "featured", "verified"}},
}


class InputError(ValueError): pass
class TransactionError(RuntimeError): pass


def scalar(value: str) -> Any:
    value = value.strip()
    if not value: return {}
    if value[:1] in {'"', "'"}:
        if len(value) < 2 or value[-1] != value[0]: raise InputError("unterminated quoted YAML value")
        return json.loads(value) if value[0] == '"' else value[1:-1].replace("''", "'")
    value = re.sub(r"\s+#.*$", "", value).strip()
    if value in ("true", "false"): return value == "true"
    if re.fullmatch(r"\d+", value): return int(value)
    return value


def parse_yaml(text: str) -> dict[str, Any]:
    root: dict[str, Any] = {}; stack: list[tuple[int, Any]] = [(-1, root)]; keys: dict[int, set[str]] = {}
    raw_lines = text.splitlines()
    for index, raw in enumerate(raw_lines):
        number = index + 1
        if not raw.strip() or raw.lstrip().startswith("#"): continue
        indent = len(raw) - len(raw.lstrip(" "))
        if indent % 2: raise InputError(f"front matter line {number}: indentation must use pairs of spaces")
        while stack[-1][0] >= indent: stack.pop()
        parent, line = stack[-1][1], raw.strip()
        if line.startswith("- "):
            if not isinstance(parent, list): raise InputError(f"front matter line {number}: list item in a mapping")
            parent.append(scalar(line[2:])); continue
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9]*):(?:\s*(.*))?", line)
        if not match or not isinstance(parent, dict): raise InputError(f"front matter line {number}: unsupported YAML")
        key, raw_value = match.groups(); seen = keys.setdefault(id(parent), set())
        if key in seen: raise InputError(f"front matter line {number}: duplicate key {key!r}")
        seen.add(key); value = scalar(raw_value or "")
        if value == {}:
            following = next((line for line in raw_lines[index + 1:] if line.strip() and not line.lstrip().startswith("#")), "")
            next_indent = len(following) - len(following.lstrip(" ")) if following else -1
            if next_indent > indent and following.strip().startswith("- "): value = []
        parent[key] = value
        if isinstance(value, (dict, list)): stack.append((indent, value))
    return root


def parse_input(path: Path) -> tuple[dict[str, Any], dict[str, str], list[dict[str, str]]]:
    try: text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc: raise InputError("input must be UTF-8") from exc
    match = re.fullmatch(r"---\r?\n(.*?)\r?\n---\r?\n(.*)", text, re.S)
    if not match: raise InputError("input must begin with YAML front matter delimited by ---")
    meta = parse_yaml(match.group(1)); unknown = set(meta) - REQUIRED_FIELDS - OPTIONAL_FIELDS; missing = REQUIRED_FIELDS - set(meta)
    if unknown: raise InputError("unknown front matter fields: " + ", ".join(sorted(unknown)))
    if missing: raise InputError("missing front matter fields: " + ", ".join(sorted(missing)))
    headings = list(re.finditer(r"^## (.+?)\s*$", match.group(2), re.M)); sections: dict[str, str] = {}
    for i, heading in enumerate(headings):
        name = heading.group(1)
        if name in sections: raise InputError(f"duplicate required section: {name}")
        sections[name] = match.group(2)[heading.end():headings[i + 1].start() if i + 1 < len(headings) else None].strip()
    absent = [name for name in SECTIONS if not sections.get(name)]
    if absent: raise InputError("missing or empty required sections: " + ", ".join(absent))
    steps, step_text = [], sections[SECTIONS[1]]; step_heads = list(re.finditer(r"^### (\d+)\.\s+(.+?)\s*$", step_text, re.M))
    for i, heading in enumerate(step_heads):
        body = step_text[heading.end():step_heads[i + 1].start() if i + 1 < len(step_heads) else None].strip()
        if "Expected outcome:" not in body: raise InputError(f"troubleshooting step {heading.group(1)} is missing explicit 'Expected outcome:' text")
        steps.append({"number": heading.group(1), "title": heading.group(2), "body": body})
    if not steps or [s["number"] for s in steps] != [str(i) for i in range(1, len(steps) + 1)]: raise InputError("troubleshooting steps must use consecutive '### 1. Title' headings")
    return meta, sections, steps


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().casefold())


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle: return json.load(handle)


def json_bytes(value: Any) -> bytes: return (json.dumps(value, indent=4, ensure_ascii=False) + "\n").encode()
def sha(data: bytes) -> str: return hashlib.sha256(data).hexdigest()


@dataclass
class Plan:
    meta: dict[str, Any]; sections: dict[str, str] = field(default_factory=dict); steps: list[dict[str, str]] = field(default_factory=list)
    resolved: dict[str, str] = field(default_factory=dict); errors: list[str] = field(default_factory=list); warnings: list[str] = field(default_factory=list); duplicates: list[str] = field(default_factory=list)
    files: list[str] = field(default_factory=list); new_records: dict[str, bool] = field(default_factory=dict); target_shard: str = ""; new_shard: bool = False
    outputs: dict[str, bytes] = field(default_factory=dict); sources: dict[str, str] = field(default_factory=dict); digest: str = ""; sitemap_additions: list[str] = field(default_factory=list)


def validate_new_record(plan: Plan, field_name: str, record: dict[str, Any]) -> bool:
    missing = RECORD_KEYS[field_name] - set(record)
    if missing: plan.errors.append(f"{REGISTRIES[field_name][1]} is incomplete; missing: {', '.join(sorted(missing))}"); return False
    for parent, required in NESTED_RECORD_KEYS[field_name].items():
        value = record.get(parent)
        if not isinstance(value, dict) or (required - set(value)):
            missing_nested = required - set(value) if isinstance(value, dict) else required
            plan.errors.append(f"{REGISTRIES[field_name][1]}.{parent} is incomplete; missing: {', '.join(sorted(missing_nested))}")
            return False
    return True


def resolve_one(plan: Plan, field_name: str, registry: list[dict[str, Any]], new_key: str) -> None:
    supplied = str(plan.meta[field_name]); exact = [r for r in registry if r.get("name") == supplied]; normalized = [r for r in registry if norm(str(r.get("name", ""))) == norm(supplied)]
    if len(exact) == 1: plan.resolved[field_name] = exact[0]["name"]; plan.new_records[field_name] = False
    elif not exact and normalized:
        plan.errors.append(f"{field_name} is noncanonical: {supplied!r}; possible canonical match: {normalized[0]['name']!r}"); plan.warnings.append(f"normalized-name match for {field_name}: {supplied!r} -> {normalized[0]['name']!r}")
    elif plan.meta["taxonomyMode"] == "create-missing" and isinstance(plan.meta.get(new_key), dict) and plan.meta[new_key].get("name") == supplied:
        if validate_new_record(plan, field_name, plan.meta[new_key]): plan.resolved[field_name] = supplied; plan.new_records[field_name] = True
    else: plan.errors.append(f"cannot resolve canonical {field_name} {supplied!r}")


def markdown_inline(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*(.+?)\*", r"<em>\1</em>", escaped)
    return escaped


def markdown_blocks(value: str) -> str:
    value = re.sub(r"<!--.*?-->", "", value, flags=re.S)
    blocks, paragraph, items = [], [], []
    def flush() -> None:
        nonlocal paragraph, items
        if paragraph: blocks.append("<p>" + "\n".join(markdown_inline(x) for x in paragraph) + "</p>"); paragraph = []
        if items: blocks.append("<ul>\n" + "\n".join(f"  <li>{markdown_inline(x)}</li>" for x in items) + "\n</ul>"); items = []
    for line in value.splitlines():
        if line.startswith("- "):
            if paragraph: flush()
            items.append(line[2:])
        elif not line.strip(): flush()
        else:
            if items: flush()
            paragraph.append(line)
    flush(); return "\n\n".join(blocks)


def flatten(value: str) -> str:
    plain = re.sub(r"^[-*]\s+", "", value, flags=re.M); plain = re.sub(r"\*\*(.*?)\*\*|\*(.*?)\*", lambda m: m.group(1) or m.group(2), plain)
    return " ".join(plain.split())


def canonical_template(root: Path, guides: list[tuple[str, dict[str, Any]]]) -> Path:
    candidates = sorted(guides, key=lambda x: (str(x[1].get("dateAdded", "")), x[1].get("url", "")), reverse=True)
    for _, guide in candidates:
        path = root / str(guide.get("url", ""))
        if path.is_file() and all(marker in path.read_text(encoding="utf-8", errors="replace") for marker in ("Related Guides", "guide-feedback", "Guides intended for trained personnel only.")): return path
    raise InputError("no complete troubleshooting-guide page is available as the canonical template")


def render_html(plan: Plan, template: str) -> str:
    meta = plan.meta; canonical = f"https://jaketroubleshoots.com/guides/{meta['slug']}.html"
    head = template[:template.index('<section class="hero">')]
    tail = template[template.index('\n<section style="padding:40px; text-align:center;"', template.index("</main>")):]
    head = re.sub(r"<title>.*?</title>", f"<title>{html.escape(str(meta['title']))}</title>", head, count=1)
    description_tag = f'<meta name="description" content="{html.escape(str(meta["description"]), quote=True)}">'
    head, replacements = re.subn(
        r"""<meta\b(?=[^>]*\bname\s*=\s*["']description["'])[^>]*>""",
        description_tag,
        head,
        count=1,
        flags=re.I,
    )
    if not replacements:
        head = head.replace("</head>", description_tag + "\n</head>", 1)
    head = re.sub(r'<link rel="canonical" href="[^"]+"\s*/>', f'<link rel="canonical" href="{canonical}" />', head, count=1)
    body = [f'<section class="hero">\n  <h2>{html.escape(str(meta["manufacturer"]))} {html.escape(str(meta["model"]))}</h2>\n  <p>{html.escape(str(meta["issueTitle"]))}</p>\n</section>', '<main style="max-width:900px; margin:40px auto; padding:0 20px;">']
    for label, key in (("Asset Type", "assetType"), ("Manufacturer", "manufacturer"), ("Model", "model")): body += [f"<h3>{label}</h3>", f"<p>{html.escape(str(meta[key]))}</p>"]
    body += [f"<h2>{SECTIONS[0]}</h2>", markdown_blocks(plan.sections[SECTIONS[0]]), f"<h2>{SECTIONS[1]}</h2>"]
    for step in plan.steps: body += [f'<h4>{step["number"]}. {html.escape(step["title"])}</h4>', markdown_blocks(step["body"])]
    for name in SECTIONS[2:4]: body += [f"<h2>{name}</h2>", markdown_blocks(plan.sections[name])]
    body += [f"<h2>{SECTIONS[4]}</h2>", markdown_blocks(plan.sections[SECTIONS[4]]), "<p><strong>CCR = Complaint, Cause, Resolution</strong></p>"]
    for label, key, explanation in (("Complaint", "complaint", "What was reported by the clinical staff."), ("Cause", "cause", "What was observed during troubleshooting."), ("Resolution", "resolution", "What action was taken.")):
        body += [f"<h4>{label}</h4>", f"<p>{explanation}</p>", f'<p><em>Example:</em><br>"{html.escape(str(meta["ccr"][key]))}"</p>']
    body += [f"<h2>{SECTIONS[5]}</h2>", markdown_blocks(plan.sections[SECTIONS[5]]), "<ul>\n" + "\n".join(f"  <li>{html.escape(str(x))}</li>" for x in meta["helpfulDetails"]) + "\n</ul>", f"<h2>{SECTIONS[6]}</h2>", markdown_blocks(plan.sections[SECTIONS[6]]), "</main>"]
    return head + "\n\n".join(body) + tail


def build_plan(meta: dict[str, Any], root: Path = ROOT, sections: dict[str, str] | None = None, steps: list[dict[str, str]] | None = None, input_bytes: bytes = b"") -> Plan:
    plan = Plan(meta, sections or {}, steps or [])
    if meta["schemaVersion"] != 1: plan.errors.append("schemaVersion must be 1")
    if meta["taxonomyMode"] not in ("reuse", "create-missing"): plan.errors.append("taxonomyMode must be reuse or create-missing")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(meta["slug"])): plan.errors.append("slug must contain lowercase ASCII words separated by hyphens")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(meta["dateAdded"])): plan.errors.append("dateAdded must use YYYY-MM-DD")
    ccr = meta.get("ccr")
    if not isinstance(ccr, dict) or set(ccr) != {"complaint", "cause", "resolution"} or not all(ccr.values()): plan.errors.append("ccr must contain nonempty complaint, cause, and resolution")
    if not isinstance(meta.get("helpfulDetails"), list) or not meta["helpfulDetails"]: plan.errors.append("helpfulDetails must be a nonempty list")
    registries = {name: load_json(root / spec[0]) for name, spec in REGISTRIES.items()}
    for name, (_, new_key) in REGISTRIES.items(): resolve_one(plan, name, registries[name], new_key)
    if all(k in plan.resolved for k in REGISTRIES) and not plan.new_records.get("model"):
        record = next(r for r in registries["model"] if r.get("name") == plan.resolved["model"]); profile = record.get("profile", {})
        if profile.get("manufacturer") != plan.resolved["manufacturer"] or profile.get("assetType") != plan.resolved["assetType"]: plan.errors.append("model registry links do not match the resolved manufacturer and asset type")
    if plan.new_records.get("model"):
        profile = meta["newModel"].get("profile", {})
        if profile.get("manufacturer") != plan.resolved.get("manufacturer") or profile.get("assetType") != plan.resolved.get("assetType"): plan.errors.append("newModel profile must link the canonical manufacturer and asset type")
    manifest = load_json(root / "data/guides.json")
    if len(manifest) != len(set(manifest)): plan.errors.append("data/guides.json contains duplicate shard registrations")
    guides: list[tuple[str, dict[str, Any]]] = []
    for shard in manifest:
        if not (root / shard).is_file(): plan.errors.append(f"registered manufacturer shard is missing: {shard}")
        else: guides.extend((shard, guide) for guide in load_json(root / shard))
    canonical_sets = {name: {record.get("name") for record in records} for name, records in registries.items()}
    for shard, guide in guides:
        for field_name in REGISTRIES:
            if guide.get(field_name) not in canonical_sets[field_name]: plan.errors.append(f"missing taxonomy record for existing guide in {shard}: {field_name}={guide.get(field_name)!r}")
    for path in (root / "data").glob("guides-*.json"):
        rel = path.relative_to(root).as_posix()
        if rel not in set(manifest): plan.warnings.append(f"unregistered manufacturer shard: {rel}")
    slug = str(meta["slug"]); html_path = f"guides/{slug}.html"; canonical = "https://jaketroubleshoots.com/" + html_path
    manufacturer_slug = re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", str(plan.resolved.get("manufacturer", meta["manufacturer"])).casefold()))
    plan.target_shard = f"data/guides-{manufacturer_slug}.json"; plan.new_shard = plan.target_shard not in manifest
    if plan.new_shard and not plan.new_records.get("manufacturer"): plan.errors.append("creating a manufacturer shard requires a complete, explicitly supplied newManufacturer record")
    plan.files = [html_path, plan.target_shard] + (["data/guides.json"] if plan.new_shard else []) + [REGISTRIES[n][0] for n in REGISTRIES if plan.new_records.get(n)] + ["sitemap.xml"]
    for shard, guide in guides:
        reasons=[]; title=str(guide.get("title", "")); url=str(guide.get("url", ""))
        if title == meta["title"]: reasons.append("title")
        elif norm(title) == norm(str(meta["title"])): reasons.append("normalized title")
        if url == html_path: reasons += ["slug/HTML path", "JSON URL"]
        wanted=(norm(str(meta["manufacturer"])), norm(str(meta["model"])), norm(str(meta["issueTitle"]))); identity=(norm(str(guide.get("manufacturer", ""))), norm(str(guide.get("model", ""))), norm(title.split(" - ",1)[-1]))
        ratio=difflib.SequenceMatcher(None, identity[2], wanted[2]).ratio()
        if identity[:2] == wanted[:2] and ratio >= .78: reasons.append(f"manufacturer/model/issue near-match ({ratio:.0%})")
        if reasons: plan.duplicates.append(f"{title} [{shard}]: {', '.join(dict.fromkeys(reasons))}")
    sitemap_urls = {n.text for n in ET.parse(root / "sitemap.xml").iter() if n.tag.endswith("loc")}
    if canonical in sitemap_urls: plan.duplicates.append(f"sitemap already contains {canonical}")
    if (root / html_path).exists(): plan.duplicates.append(f"HTML file already exists: {html_path}")
    canonical_pattern = re.compile(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)', re.I)
    for existing in (root / "guides").glob("*.html"):
        found = canonical_pattern.search(existing.read_text(encoding="utf-8", errors="replace"))
        if found and found.group(1) == canonical: plan.duplicates.append(f"canonical URL is already used by: {existing.relative_to(root).as_posix()}")
    if plan.duplicates: plan.errors.append("duplicate resolution is uncertain; review the reported candidates")
    if not plan.errors and sections is not None:
        template_path = canonical_template(root, guides); template = template_path.read_text(encoding="utf-8"); plan.sources[template_path.relative_to(root).as_posix()] = sha(template.encode())
        plan.outputs[html_path] = render_html(plan, template).encode()
        record = {"title": meta["title"], "description": meta["description"], "assetType": meta["assetType"], "manufacturer": meta["manufacturer"], "model": meta["model"], "url": html_path, "dateAdded": meta["dateAdded"], "steps": [{"title": f'{s["number"]}. {s["title"]}', "instructions": flatten(s["body"])} for s in plan.steps], "documentation": {"CCR": {"Complaint": ccr["complaint"], "Cause": ccr["cause"], "Resolution": ccr["resolution"]}}, "helpfulDetails": meta["helpfulDetails"]}
        shard_data = [] if plan.new_shard else load_json(root / plan.target_shard); plan.outputs[plan.target_shard] = json_bytes(shard_data + [record])
        if plan.new_shard: plan.outputs["data/guides.json"] = json_bytes(manifest + [plan.target_shard])
        for name, (path, new_key) in REGISTRIES.items():
            if plan.new_records.get(name): plan.outputs[path] = json_bytes(registries[name] + [meta[new_key]])
        tree=ET.parse(root / "sitemap.xml"); ns="{http://www.sitemaps.org/schemas/sitemap/0.9}"; node=ET.SubElement(tree.getroot(), ns+"url"); ET.SubElement(node, ns+"loc").text=canonical
        urls=sorted((n.find(ns+"loc").text for n in tree.getroot().findall(ns+"url"))); root_node=ET.Element(ns+"urlset")
        for url in urls: u=ET.SubElement(root_node, ns+"url"); ET.SubElement(u, ns+"loc").text=url
        ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9"); plan.outputs["sitemap.xml"] = (ET.tostring(root_node, encoding="unicode", xml_declaration=True) + "\n").encode(); plan.sitemap_additions=[canonical]
    relevant = ["data/guides.json", "data/hub-asset.json", "data/hub-manufacturer.json", "data/hub-model.json", "sitemap.xml"] + list(manifest)
    for rel in relevant:
        if (root/rel).is_file(): plan.sources[rel] = sha((root/rel).read_bytes())
    payload={"input":sha(input_bytes), "sources":dict(sorted(plan.sources.items())), "outputs":{k:sha(v) for k,v in sorted(plan.outputs.items())}, "meta":meta}
    plan.digest=hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return plan


def validate_outputs(plan: Plan, root: Path) -> None:
    for rel, data in plan.outputs.items():
        if rel.endswith(".json"): json.loads(data)
        if rel == "sitemap.xml": ET.fromstring(data)
    page=plan.outputs[f'guides/{plan.meta["slug"]}.html'].decode(); visible=html.unescape(re.sub(r"<[^>]+>", "", page))
    for wording in [plan.meta["title"], plan.meta["description"], *plan.meta["ccr"].values(), *plan.meta["helpfulDetails"], *[s["title"] for s in plan.steps]]:
        if html.escape(str(wording), quote=False) not in page and str(wording) not in plan.outputs[plan.target_shard].decode(): raise TransactionError(f"rendered output omitted supplied wording: {wording}")
    for supplied in [value for name, value in plan.sections.items() if name != SECTIONS[1]] + [s["body"] for s in plan.steps]:
        for line in re.sub(r"<!--.*?-->", "", supplied, flags=re.S).splitlines():
            wording = re.sub(r"^[-*]\s+", "", line.strip())
            wording = re.sub(r"\*\*(.*?)\*\*|\*(.*?)\*", lambda m: m.group(1) or m.group(2), wording)
            if wording and wording not in visible: raise TransactionError(f"rendered HTML omitted supplied wording: {wording}")
    canonical=f'https://jaketroubleshoots.com/guides/{plan.meta["slug"]}.html'
    if plan.outputs["sitemap.xml"].decode().count(canonical) != 1: raise TransactionError("sitemap addition is not unique")


def git_clean(root: Path) -> bool:
    result=subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=root, text=True, capture_output=True, check=True)
    return not result.stdout


def write_plan(plan: Plan, root: Path) -> dict[str, Any]:
    if not git_clean(root): raise TransactionError("--write requires a clean Git worktree")
    validate_outputs(plan, root); created=[]; modified=[]; backups: dict[str, tuple[bytes, int] | None]={}
    with tempfile.TemporaryDirectory(prefix="publish-guide-", dir=root) as temp_name:
        temp=Path(temp_name)
        for rel,data in plan.outputs.items(): (temp/rel).parent.mkdir(parents=True, exist_ok=True); (temp/rel).write_bytes(data)
        for rel,data in plan.outputs.items():
            if (temp/rel).read_bytes()!=data: raise TransactionError("temporary rendering verification failed")
        try:
            for index,(rel,data) in enumerate(plan.outputs.items(),1):
                dest=root/rel; backups[rel]=(dest.read_bytes(), dest.stat().st_mode) if dest.exists() else None
                (modified if dest.exists() else created).append(rel); dest.parent.mkdir(parents=True, exist_ok=True); os.replace(temp/rel, dest)
                if os.environ.get("PUBLISH_GUIDE_FAIL_AFTER_REPLACE") == str(index): raise TransactionError("simulated write failure")
            for rel,data in plan.outputs.items():
                if (root/rel).read_bytes()!=data: raise TransactionError(f"post-write verification failed: {rel}")
            validate_outputs(plan, root)
        except Exception:
            for rel,backup in reversed(list(backups.items())):
                dest=root/rel
                if backup is None: dest.unlink(missing_ok=True)
                else: dest.write_bytes(backup[0]); os.chmod(dest, backup[1])
            raise
    return {"status":"committed", "planDigest":plan.digest, "createdFiles":created, "modifiedFiles":modified, "hashes":{rel:{"before":sha(backups[rel][0]) if backups[rel] else None,"after":sha(data)} for rel,data in plan.outputs.items()}, "taxonomyDecisions":{n:("created" if plan.new_records.get(n) else "reused") for n in REGISTRIES}, "sitemapAdditions":plan.sitemap_additions}


def report(plan: Plan) -> str:
    status="BLOCKED" if plan.errors or plan.warnings or plan.duplicates else "READY"; lines=["Guide publisher dry run","=======================",f"Status: {status}","Mode: dry-run (no files written)",f"Plan digest: {plan.digest}","","Resolved canonical taxonomy:"]
    lines += [f"  {n}: {plan.resolved.get(n, 'UNRESOLVED')}" for n in REGISTRIES]
    lines += ["",f'Target HTML path: guides/{plan.meta["slug"]}.html',f"Target manufacturer shard: {plan.target_shard}",f"New shard required: {'yes' if plan.new_shard else 'no'}","Files proposed:"]+[f"  - {x}" for x in dict.fromkeys(plan.files)]
    for heading, values in (("Validation errors",plan.errors),("Warnings",plan.warnings),("Possible duplicate matches",plan.duplicates)): lines += ["",heading+":"] + ([f"  - {x}" for x in values] or ["  (none)"])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("input",type=Path); parser.add_argument("--root",type=Path,default=ROOT,help=argparse.SUPPRESS); parser.add_argument("--write",action="store_true"); parser.add_argument("--confirm-plan")
    args=parser.parse_args(argv)
    try:
        meta,sections,steps=parse_input(args.input); plan=build_plan(meta,args.root,sections,steps,args.input.read_bytes())
        blocked=bool(plan.errors or plan.warnings or plan.duplicates)
        if not args.write: print(report(plan)); return 2 if blocked else 0
        if blocked: raise TransactionError("write refused because the plan has unresolved blockers")
        if not args.confirm_plan: raise TransactionError("--write requires --confirm-plan <digest>")
        if args.confirm_plan != plan.digest: raise TransactionError(f"incorrect or stale plan digest (current: {plan.digest})")
        print(json.dumps(write_plan(plan,args.root),indent=2)); return 0
    except (InputError,TransactionError,OSError,json.JSONDecodeError,ET.ParseError,subprocess.CalledProcessError) as exc:
        print(f"Guide publisher\nStatus: BLOCKED\nValidation errors:\n  - {exc}",file=sys.stderr); return 2


if __name__ == "__main__": raise SystemExit(main())
