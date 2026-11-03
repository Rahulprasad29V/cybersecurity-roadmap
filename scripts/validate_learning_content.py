#!/usr/bin/env python3
"""Validate CyberWolf quiz banks, achievements, glossary and required files."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{path.relative_to(ROOT)}: invalid JSON: {exc}", errors)
        return None


def validate_quizzes(errors: list[str]) -> int:
    count = 0
    for path in sorted((ROOT / "quizzes").glob("*.json")):
        if path.name == "quiz.schema.json":
            continue
        data = load_json(path, errors)
        if not isinstance(data, dict):
            continue
        questions = data.get("questions")
        if data.get("format_version") != 1 or not data.get("title") or not isinstance(questions, list) or not questions:
            fail(f"{path.relative_to(ROOT)}: expected format_version=1, title and non-empty questions", errors)
            continue
        seen_ids: set[str] = set()
        for index, question in enumerate(questions, start=1):
            label = f"{path.relative_to(ROOT)} question {index}"
            if not isinstance(question, dict):
                fail(f"{label}: expected an object", errors)
                continue
            question_id = question.get("id")
            if not isinstance(question_id, str) or not question_id:
                fail(f"{label}: missing id", errors)
            elif question_id in seen_ids:
                fail(f"{label}: duplicate question id {question_id!r}", errors)
            else:
                seen_ids.add(question_id)

            options = question.get("options")
            if not isinstance(options, list) or len(options) < 2:
                fail(f"{label}: expected at least two options", errors)
                continue
            option_ids = [option.get("id") for option in options if isinstance(option, dict)]
            if len(option_ids) != len(options) or len(set(option_ids)) != len(option_ids):
                fail(f"{label}: options must be objects with unique ids", errors)
            if question.get("correct_option") not in option_ids:
                fail(f"{label}: correct_option must match one option id", errors)
            if not question.get("prompt") or not question.get("explanation"):
                fail(f"{label}: prompt and explanation are required", errors)
            if question.get("difficulty") not in {"beginner", "intermediate", "advanced"}:
                fail(f"{label}: invalid difficulty", errors)
            count += 1
    return count


def validate_achievements(errors: list[str]) -> int:
    path = ROOT / "achievements" / "achievements.json"
    data = load_json(path, errors)
    if not isinstance(data, dict):
        return 0
    achievements = data.get("achievements")
    if data.get("format_version") != 1 or not isinstance(achievements, list):
        fail("achievements/achievements.json: expected format_version=1 and achievements array", errors)
        return 0
    ids = [item.get("id") for item in achievements if isinstance(item, dict)]
    if len(ids) != len(achievements) or len(ids) != len(set(ids)):
        fail("achievements/achievements.json: achievement ids must be present and unique", errors)
    return len(achievements)


def validate_glossary(errors: list[str]) -> int:
    path = ROOT / "glossary" / "glossary.csv"
    if not path.is_file():
        fail("Missing glossary/glossary.csv", errors)
        return 0
    try:
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            required = {"term", "definition", "category", "reference"}
            if not required.issubset(set(reader.fieldnames or [])):
                fail("glossary/glossary.csv: required columns are missing", errors)
                return 0
            rows = list(reader)
            for number, row in enumerate(rows, start=2):
                if not all((row.get(key) or "").strip() for key in required):
                    fail(f"glossary/glossary.csv:{number}: empty required value", errors)
            return len(rows)
    except (OSError, csv.Error) as exc:
        fail(f"glossary/glossary.csv: unable to parse CSV: {exc}", errors)
        return 0


def main() -> int:
    errors: list[str] = []
    quiz_count = validate_quizzes(errors)
    achievement_count = validate_achievements(errors)
    glossary_count = validate_glossary(errors)

    if errors:
        print("Learning-content validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Learning-content validation passed.")
    print(f"Validated {quiz_count} quiz questions, {achievement_count} achievements and {glossary_count} glossary terms.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
