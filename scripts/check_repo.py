#!/usr/bin/env python3
"""Validate local Markdown links and required CyberWolf curriculum structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

REQUIRED_FILES = [
    "README.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "100-days/README.md",
    "100-days/progress-tracker.md",
    "advanced/README.md",
    "advanced/30-day-challenge.md",
    "capstones/README.md",
    "assessments/README.md",
    "curriculum/curriculum.json",
    "curriculum/curriculum.schema.json",
    "datasets/manifest.json",
    "quizzes/advanced-scenarios.json",
    "instructor-guide/README.md",
    "scripts/check_repo.py",
    "scripts/validate_learning_content.py",
    ".github/workflows/quality.yml",
]


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
            target = local_link_target(source, match.group(1))
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: link escapes repository: {match.group(1)}")
                continue
            if not target.exists():
                errors.append(f"{source.relative_to(ROOT)}: broken local link: {match.group(1)}")
    return errors


def validate_structure() -> list[str]:
    errors: list[str] = []
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            errors.append(f"Missing required file: {relative_path}")

    day_dir = ROOT / "100-days"
    expected = {f"DAY-{number:03d}.md" for number in range(1, 101)}
    actual = {path.name for path in day_dir.glob("DAY-*.md")} if day_dir.exists() else set()
    missing = sorted(expected - actual)
    if missing:
        errors.append("Missing daily challenge files: " + ", ".join(missing))

    return errors


def main() -> int:
    errors = validate_links() + validate_structure()
    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Repository checks passed: {len(markdown_files())} Markdown files scanned.")
    print(f"All {len(REQUIRED_FILES)} required files and 100 daily challenge pages exist.")
    print("All repository-relative Markdown links resolve inside the repository.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
