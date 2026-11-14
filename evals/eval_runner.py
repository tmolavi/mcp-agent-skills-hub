#!/usr/bin/env python3
"""Behavioral Schema and Quality Tier Evaluator for Agent Skills."""

import os
import sys
import json
from typing import Dict, Any, List

def evaluate_skill(skill_dir: str) -> Dict[str, Any]:
    skill_file = os.path.join(skill_dir, "SKILL.md")
    result = {
        "name": os.path.basename(skill_dir),
        "has_skill_md": os.path.exists(skill_file),
        "frontmatter_valid": False,
        "has_when_to_use": False,
        "has_anti_rationalization": False,
        "score": 0.0,
        "passed": False,
        "messages": []
    }

    if not result["has_skill_md"]:
        result["messages"].append("Missing SKILL.md")
        return result

    try:
        with open(skill_file, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()
    except Exception as e:
        result["messages"].append(f"Failed to read SKILL.md: {e}")
        return result

    # Check frontmatter
    if content.startswith("---") and "---" in content[3:]:
        result["frontmatter_valid"] = True
        result["score"] += 40.0
    else:
        result["messages"].append("Invalid or missing YAML frontmatter markers")

    # Check sections
    lower = content.lower()
    if (
        "when to use" in lower
        or "use this skill when" in lower
        or "trigger" in lower
        or "overview" in lower
        or "purpose" in lower
        or "usage" in lower
    ):
        result["has_when_to_use"] = True
        result["score"] += 30.0

    if (
        "rules" in lower
        or "checklist" in lower
        or "verification" in lower
        or "guidelines" in lower
        or "instructions" in lower
        or "workflow" in lower
        or "patterns" in lower
        or "best practices" in lower
        or "scripts" in lower
    ):
        result["score"] += 30.0

    result["passed"] = result["score"] >= 70.0
    return result

def run_suite(skills_dir: str) -> bool:
    print(f"=== Running Agent Skill Quality & Schema Suite ===")
    folders = [d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))]
    passed = 0
    failed = 0

    for folder in sorted(folders):
        res = evaluate_skill(os.path.join(skills_dir, folder))
        if res["passed"]:
            passed += 1
        else:
            failed += 1
            print(f"  ✗ {res['name']}: Score {res['score']} - {res['messages']}")

    print(f"\nTotal Skills Evaluated: {len(folders)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    return failed == 0

if __name__ == "__main__":
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    skills_path = os.path.join(repo_root, "skills")
    success = run_suite(skills_path)
    sys.exit(0 if success else 1)
