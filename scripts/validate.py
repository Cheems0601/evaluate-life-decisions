#!/usr/bin/env python3
"""Validate the repository's skill package and evaluation fixtures."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "evaluate-life-decisions"
SKILL_MD = SKILL_DIR / "SKILL.md"

REQUIRED = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "CONTRIBUTING.md",
    SKILL_MD,
    SKILL_DIR / "agents" / "openai.yaml",
    SKILL_DIR / "references" / "decision-method.md",
    SKILL_DIR / "references" / "evidence-standard.md",
    SKILL_DIR / "references" / "regional-sources.md",
    SKILL_DIR / "references" / "region-template.md",
    ROOT / "evals" / "cases.json",
    ROOT / "evals" / "rubric.md",
]


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def check_frontmatter(errors: list[str]) -> None:
    text = SKILL_MD.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md has no valid opening frontmatter block", errors)
        return
    lines = [line for line in match.group(1).splitlines() if line.strip()]
    keys = [line.split(":", 1)[0].strip() for line in lines if ":" in line]
    if keys != ["name", "description"]:
        fail("SKILL.md frontmatter must contain only name and description", errors)
    if "name: evaluate-life-decisions" not in match.group(1):
        fail("Unexpected skill name", errors)
    if len(text.splitlines()) > 500:
        fail("SKILL.md exceeds 500 lines", errors)


def check_local_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean = target.split("#", 1)[0]
            if clean and not (path.parent / clean).resolve().exists():
                fail(f"Broken local link in {path.relative_to(ROOT)}: {target}", errors)


def check_evals(errors: list[str]) -> None:
    path = ROOT / "evals" / "cases.json"
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"Invalid eval JSON: {exc}", errors)
        return
    if not isinstance(cases, list) or len(cases) < 5:
        fail("Expected at least five evaluation cases", errors)
        return
    ids: set[str] = set()
    for case in cases:
        if not isinstance(case, dict) or not {"id", "prompt", "checks"} <= case.keys():
            fail("Every evaluation case needs id, prompt, and checks", errors)
            continue
        if case["id"] in ids:
            fail(f"Duplicate evaluation id: {case['id']}", errors)
        ids.add(case["id"])
        if not isinstance(case["checks"], list) or len(case["checks"]) < 3:
            fail(f"Evaluation case {case['id']} needs at least three checks", errors)


def check_time_neutrality(errors: list[str]) -> None:
    for path in (SKILL_MD, *SKILL_DIR.joinpath("references").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if re.search(r"\b20(?:2[6-9]|[3-9]\d)\b", text):
            fail(f"Future/current year appears in runtime instructions: {path.relative_to(ROOT)}", errors)


def main() -> int:
    errors: list[str] = []
    for path in REQUIRED:
        if not path.is_file():
            fail(f"Missing required file: {path.relative_to(ROOT)}", errors)
    if not errors:
        check_frontmatter(errors)
        check_local_links(errors)
        check_evals(errors)
        check_time_neutrality(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
