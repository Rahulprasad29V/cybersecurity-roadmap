#!/usr/bin/env python3
"""Validate local Markdown links and the CyberWolf 100-day roadmap structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
DAY_RE = re.compile(r"DAY-(\d{3})\.md$")


def markdown_files() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )


def local_link_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1:target.index(">")]
    else:
        target = target.split(maxsplit=1)[0] if target else ""

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None

    path_text = unquote(parsed.path)
    if not path_text:
        return source

    if path_text.startswith("/"):
        return ROOT / path_text.lstrip("/")

    return (source.parent / path_text).resolve()


def validate_links() -> list[str]:
    errors: list[str] = []
    for source in markdown_files():
        text = source.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw_target = match.group(1)
            target = local_link_target(source, raw_target)
            if target is None:
                continue
            if not target.exists():
                relative_source = source.relative_to(ROOT)
                errors.append(f"{relative_source}: broken local link: {raw_target}")
    return errors


def validate_roadmap() -> list[str]:
    errors: list[str] = []
    required = [
        ROOT / "README.md",
        ROOT / "ROADMAP.md",
        ROOT / "100-days" / "README.md",
        ROOT / "100-days" / "progress-tracker.md",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")

    day_dir = ROOT / "100-days"
    expected = {f"DAY-{number:03d}.md" for number in range(1, 101)}
    actual = {path.name for path in day_dir.glob("DAY-*.md")} if day_dir.exists() else set()
    missing = sorted(expected - actual)
    if missing:
        errors.append("Missing daily challenge files: " + ", ".join(missing))
    return errors


def main() -> int:
    errors = validate_links() + validate_roadmap()
    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Repository checks passed: {len(markdown_files())} Markdown files scanned.")
    print("All local Markdown links resolve and all 100 daily challenge files exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
