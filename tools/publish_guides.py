#!/usr/bin/env python3
"""Plan or transactionally publish a directory of reviewed guides."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from publish_guide import (
    ROOT,
    InputError,
    Plan,
    REGISTRIES,
    SECTIONS,
    TransactionError,
    build_plan,
    git_clean,
    norm,
    parse_input,
    sha,
)


@dataclass
class BatchPlan:
    inputs: list[Path]
    guides: list[tuple[Path, Plan]] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    duplicates: list[str] = field(default_factory=list)
    outputs: dict[str, bytes] = field(default_factory=dict)
    sources: dict[str, str] = field(default_factory=dict)
    digest: str = ""

    @property
    def blocked(self) -> bool:
        return bool(self.errors or self.warnings or self.duplicates)


def _copy_repository(root: Path, destination: Path, excluded: Path) -> None:
    excluded = excluded.resolve()

    def ignore(directory: str, names: list[str]) -> set[str]:
        base = Path(directory).resolve()
        ignored = {".git", "__pycache__"}
        for name in names:
            candidate = (base / name).resolve()
            if candidate == excluded or excluded in candidate.parents:
                ignored.add(name)
        return ignored

    shutil.copytree(root, destination, ignore=ignore)


def _identity(meta: dict[str, Any]) -> dict[str, str]:
    slug = str(meta["slug"])
    path = f"guides/{slug}.html"
    return {
        "title": norm(str(meta["title"])),
        "slug": norm(slug),
        "html path": path.casefold(),
        "JSON URL": path.casefold(),
        "canonical URL": f"https://jaketroubleshoots.com/{path}".casefold(),
        "manufacturer/model/issue": "|".join(
            norm(str(meta[key])) for key in ("manufacturer", "model", "issueTitle")
        ),
    }


def _batch_duplicates(parsed: list[tuple[Path, dict[str, Any], dict[str, str], list[dict[str, str]], bytes]]) -> list[str]:
    found: list[str] = []
    indexes: dict[str, dict[str, Path]] = {}
    for path, meta, _, _, _ in parsed:
        for kind, value in _identity(meta).items():
            previous = indexes.setdefault(kind, {}).get(value)
            if previous is not None:
                found.append(f"{path.name} duplicates {previous.name} by {kind}")
            else:
                indexes[kind][value] = path
    return found


def _validate_complete(plan: BatchPlan) -> None:
    for rel, data in plan.outputs.items():
        if rel.endswith(".json"):
            json.loads(data)
        elif rel == "sitemap.xml":
            ET.fromstring(data)
    sitemap = plan.outputs.get("sitemap.xml", b"").decode()
    for _, guide in plan.guides:
        page_rel = f'guides/{guide.meta["slug"]}.html'
        page = plan.outputs[page_rel].decode()
        visible = html.unescape(re.sub(r"<[^>]+>", "", page))
        wording = [
            guide.meta["title"],
            guide.meta["description"],
            *guide.meta["ccr"].values(),
            *guide.meta["helpfulDetails"],
            *[step["title"] for step in guide.steps],
        ]
        for section_name, supplied in guide.sections.items():
            if section_name != SECTIONS[1]:
                wording.extend(re.sub(r"<!--.*?-->", "", supplied, flags=re.S).splitlines())
        for step in guide.steps:
            wording.extend(re.sub(r"<!--.*?-->", "", step["body"], flags=re.S).splitlines())
        for supplied in wording:
            text = re.sub(r"^[-*]\s+", "", str(supplied).strip())
            text = re.sub(r"\*\*(.*?)\*\*|\*(.*?)\*", lambda match: match.group(1) or match.group(2), text)
            if text and text not in visible and text not in plan.outputs[guide.target_shard].decode():
                raise TransactionError(f"{page_rel} omitted supplied wording: {text}")
        canonical = f'https://jaketroubleshoots.com/guides/{guide.meta["slug"]}.html'
        if sitemap.count(canonical) != 1:
            raise TransactionError(f"sitemap must contain exactly one entry for {canonical}")


def build_batch_plan(input_directory: Path, root: Path = ROOT) -> BatchPlan:
    inputs = sorted(input_directory.glob("*.md"), key=lambda path: path.name.casefold())
    batch = BatchPlan(inputs)
    if not input_directory.is_dir():
        batch.errors.append(f"input directory does not exist: {input_directory}")
        return batch
    if not inputs:
        batch.errors.append("input directory contains no Markdown files")
        return batch

    parsed = []
    for path in inputs:
        try:
            meta, sections, steps = parse_input(path)
            parsed.append((path, meta, sections, steps, path.read_bytes()))
        except (InputError, OSError) as exc:
            batch.errors.append(f"{path.name}: {exc}")
    if len(parsed) != len(inputs):
        return _finish_digest(batch, root, parsed)

    batch.duplicates.extend(_batch_duplicates(parsed))
    if batch.duplicates:
        batch.errors.append("duplicate candidates exist within the batch")
        return _finish_digest(batch, root, parsed)

    with tempfile.TemporaryDirectory(prefix="publish-guides-plan-") as temporary:
        virtual = Path(temporary) / "repository"
        _copy_repository(root, virtual, input_directory)
        touched: set[str] = set()
        for path, meta, sections, steps, input_bytes in parsed:
            guide = build_plan(meta, virtual, sections, steps, input_bytes)
            batch.guides.append((path, guide))
            for rel in guide.sources:
                source = root / rel
                if source.is_file():
                    batch.sources[rel] = sha(source.read_bytes())
            batch.errors.extend(f"{path.name}: {item}" for item in guide.errors)
            batch.warnings.extend(f"{path.name}: {item}" for item in guide.warnings)
            batch.duplicates.extend(f"{path.name}: {item}" for item in guide.duplicates)
            if guide.errors or guide.warnings or guide.duplicates:
                continue
            for rel, data in sorted(guide.outputs.items()):
                target = virtual / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                touched.add(rel)
        if not batch.blocked:
            for rel in sorted(touched):
                batch.outputs[rel] = (virtual / rel).read_bytes()
            _validate_complete(batch)
    return _finish_digest(batch, root, parsed)


def _finish_digest(
    batch: BatchPlan,
    root: Path,
    parsed: list[tuple[Path, dict[str, Any], dict[str, str], list[dict[str, str]], bytes]],
) -> BatchPlan:
    relevant = {
        "data/guides.json",
        "data/hub-asset.json",
        "data/hub-manufacturer.json",
        "data/hub-model.json",
        "sitemap.xml",
    }
    manifest_path = root / "data/guides.json"
    if manifest_path.is_file():
        relevant.update(json.loads(manifest_path.read_text(encoding="utf-8")))
    for rel in sorted(relevant):
        path = root / rel
        if path.is_file():
            batch.sources[rel] = sha(path.read_bytes())
    payload = {
        "inputs": {path.name: sha(data) for path, _, _, _, data in parsed},
        "sources": batch.sources,
        "outputs": {rel: sha(data) for rel, data in sorted(batch.outputs.items())},
        "errors": batch.errors,
        "warnings": batch.warnings,
        "duplicates": batch.duplicates,
    }
    batch.digest = hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode()
    ).hexdigest()
    return batch


def write_batch(plan: BatchPlan, root: Path) -> dict[str, Any]:
    if not git_clean(root):
        raise TransactionError("--write requires a clean Git worktree")
    _validate_complete(plan)
    backups: dict[str, tuple[bytes, int] | None] = {}
    created: list[str] = []
    modified: list[str] = []
    with tempfile.TemporaryDirectory(prefix="publish-guides-write-", dir=root) as temporary:
        staged = Path(temporary)
        for rel, data in sorted(plan.outputs.items()):
            target = staged / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        try:
            for index, (rel, data) in enumerate(sorted(plan.outputs.items()), 1):
                staged_file = staged / rel
                if staged_file.read_bytes() != data:
                    raise TransactionError(f"temporary rendering verification failed: {rel}")
                destination = root / rel
                backups[rel] = (
                    (destination.read_bytes(), destination.stat().st_mode)
                    if destination.exists()
                    else None
                )
                (modified if destination.exists() else created).append(rel)
                destination.parent.mkdir(parents=True, exist_ok=True)
                os.replace(staged_file, destination)
                if os.environ.get("PUBLISH_GUIDES_FAIL_AFTER_REPLACE") == str(index):
                    raise TransactionError("simulated batch write failure")
            for rel, data in plan.outputs.items():
                if (root / rel).read_bytes() != data:
                    raise TransactionError(f"post-write verification failed: {rel}")
            _validate_complete(plan)
        except Exception:
            for rel, backup in reversed(list(backups.items())):
                destination = root / rel
                if backup is None:
                    destination.unlink(missing_ok=True)
                else:
                    destination.write_bytes(backup[0])
                    os.chmod(destination, backup[1])
            raise
    return {
        "status": "committed",
        "planDigest": plan.digest,
        "guideCount": len(plan.guides),
        "guides": [
            {"input": path.name, "status": "published", "html": f'guides/{guide.meta["slug"]}.html'}
            for path, guide in plan.guides
        ],
        "createdFiles": created,
        "modifiedFiles": modified,
        "hashes": {
            rel: {"before": sha(backups[rel][0]) if backups[rel] else None, "after": sha(data)}
            for rel, data in sorted(plan.outputs.items())
        },
        "sitemapAdditions": [
            f'https://jaketroubleshoots.com/guides/{guide.meta["slug"]}.html'
            for _, guide in plan.guides
        ],
    }


def report(plan: BatchPlan) -> str:
    lines = [
        "Guide batch publisher dry run",
        "=============================",
        f"Status: {'BLOCKED' if plan.blocked else 'READY'}",
        "Mode: dry-run (no files written)",
        f"Plan digest: {plan.digest}",
        f"Batch guides: {len(plan.inputs)}",
        "",
        "Per-guide results:",
    ]
    by_name = {path.name: guide for path, guide in plan.guides}
    for path in plan.inputs:
        guide = by_name.get(path.name)
        status = "READY" if guide and not (guide.errors or guide.warnings or guide.duplicates) and not plan.blocked else "BLOCKED"
        target = f' -> guides/{guide.meta["slug"]}.html' if guide else ""
        lines.append(f"  - {path.name}: {status}{target}")
    lines += ["", "Files proposed:"] + ([f"  - {rel}" for rel in sorted(plan.outputs)] or ["  (none)"])
    for heading, values in (
        ("Validation errors", plan.errors),
        ("Warnings", plan.warnings),
        ("Duplicate candidates", plan.duplicates),
    ):
        lines += ["", heading + ":"] + ([f"  - {value}" for value in values] or ["  (none)"])
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--confirm-plan")
    args = parser.parse_args(argv)
    try:
        plan = build_batch_plan(args.input, args.root)
        if not args.write:
            print(report(plan))
            return 2 if plan.blocked else 0
        if plan.blocked:
            raise TransactionError("write refused because the batch has unresolved blockers")
        if not args.confirm_plan:
            raise TransactionError("--write requires --confirm-plan <digest>")
        if args.confirm_plan != plan.digest:
            raise TransactionError(f"incorrect or stale plan digest (current: {plan.digest})")
        print(json.dumps(write_batch(plan, args.root), indent=2))
        return 0
    except (
        InputError,
        TransactionError,
        OSError,
        json.JSONDecodeError,
        ET.ParseError,
        subprocess.CalledProcessError,
    ) as exc:
        print(f"Guide batch publisher\nStatus: BLOCKED\nValidation errors:\n  - {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
