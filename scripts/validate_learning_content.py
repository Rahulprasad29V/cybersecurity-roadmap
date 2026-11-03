#!/usr/bin/env python3
"""Validate CyberWolf learning data, curriculum manifest and synthetic datasets."""

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


def validate_curriculum(errors: list[str]) -> int:
    path = ROOT / "curriculum" / "curriculum.json"
    schema_path = ROOT / "curriculum" / "curriculum.schema.json"
    data = load_json(path, errors)
    schema = load_json(schema_path, errors)
    if not isinstance(data, dict):
        return 0
    if not isinstance(schema, dict) or schema.get("title") != "CyberWolf Competency Curriculum":
        fail("curriculum/curriculum.schema.json: schema document is missing or unexpected", errors)

    modules = data.get("modules")
    if data.get("format_version") != 1 or not isinstance(modules, list) or not modules:
        fail("curriculum/curriculum.json: expected format_version=1 and non-empty modules", errors)
        return 0

    ids: set[str] = set()
    for index, module in enumerate(modules, start=1):
        label = f"curriculum/curriculum.json module {index}"
        if not isinstance(module, dict):
            fail(f"{label}: expected an object", errors)
            continue
        module_id = module.get("id")
        if not isinstance(module_id, str) or not module_id or module_id in ids:
            fail(f"{label}: id must be present and unique", errors)
        else:
            ids.add(module_id)
        if module.get("level") not in {"beginner", "intermediate", "advanced"}:
            fail(f"{label}: invalid level", errors)
        if not isinstance(module.get("estimated_hours"), int) or module.get("estimated_hours", 0) < 1:
            fail(f"{label}: estimated_hours must be a positive integer", errors)
        content_path = module.get("path")
        if not isinstance(content_path, str):
            fail(f"{label}: module path must be a repository-relative string", errors)
        else:
            resolved_path = (ROOT / content_path).resolve()
            try:
                resolved_path.relative_to(ROOT)
                inside_repo = True
            except ValueError:
                inside_repo = False
            if not inside_repo or not resolved_path.is_file():
                fail(f"{label}: module path is missing or escapes repository: {content_path}", errors)
        if not isinstance(module.get("learning_outcomes"), list) or not module.get("learning_outcomes"):
            fail(f"{label}: learning_outcomes must be a non-empty list", errors)
    return len(modules)


def validate_datasets(errors: list[str]) -> int:
    manifest_path = ROOT / "datasets" / "manifest.json"
    manifest = load_json(manifest_path, errors)
    if not isinstance(manifest, dict):
        return 0
    if manifest.get("format_version") != 1 or manifest.get("classification") != "synthetic-training-data":
        fail("datasets/manifest.json: classification must explicitly identify synthetic training data", errors)
    records = manifest.get("datasets")
    if not isinstance(records, list) or not records:
        fail("datasets/manifest.json: datasets must be a non-empty list", errors)
        return 0

    count = 0
    seen: set[str] = set()
    for record in records:
        if not isinstance(record, dict):
            fail("datasets/manifest.json: each dataset entry must be an object", errors)
            continue
        relative_path = record.get("path")
        if not isinstance(relative_path, str) or relative_path in seen:
            fail(f"datasets/manifest.json: invalid or duplicate dataset path {relative_path!r}", errors)
            continue
        seen.add(relative_path)
        path = (ROOT / "datasets" / relative_path).resolve()
        try:
            path.relative_to((ROOT / "datasets").resolve())
            inside_dataset_dir = True
        except ValueError:
            inside_dataset_dir = False
        if not inside_dataset_dir:
            fail(f"datasets/manifest.json: dataset path escapes datasets directory: {relative_path}", errors)
            continue
        if record.get("synthetic") is not True:
            fail(f"datasets/manifest.json: {relative_path} must be explicitly marked synthetic", errors)
        if not path.is_file():
            fail(f"datasets/manifest.json: missing dataset file {relative_path}", errors)
            continue
        try:
            with path.open(encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                if not reader.fieldnames or len(reader.fieldnames) < 2:
                    fail(f"datasets/{relative_path}: CSV header is missing or incomplete", errors)
                rows = list(reader)
                if not rows:
                    fail(f"datasets/{relative_path}: dataset has no sample rows", errors)
        except (OSError, csv.Error) as exc:
            fail(f"datasets/{relative_path}: unable to parse CSV: {exc}", errors)
        count += 1
    return count


def validate_student_template(errors: list[str]) -> bool:
    path = ROOT / "student-progress" / "student-profile.template.json"
    data = load_json(path, errors)
    if not isinstance(data, dict) or data.get("format_version") != 1 or not isinstance(data.get("profile"), dict):
        fail("student-progress/student-profile.template.json: invalid learner profile template", errors)
        return False
    return True


def main() -> int:
    errors: list[str] = []
    quiz_count = validate_quizzes(errors)
    achievement_count = validate_achievements(errors)
    glossary_count = validate_glossary(errors)
    module_count = validate_curriculum(errors)
    dataset_count = validate_datasets(errors)
    validate_student_template(errors)

    if errors:
        print("Learning-content validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Learning-content validation passed.")
    print(
        f"Validated {quiz_count} quiz questions, {achievement_count} achievements, "
        f"{glossary_count} glossary terms, {module_count} curriculum modules, "
        f"and {dataset_count} synthetic datasets."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
