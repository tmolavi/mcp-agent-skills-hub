#!/usr/bin/env python3
"""Description Collision and Distinctness Checker for Agent Skills Catalog."""

import os
import sys
import re
from typing import Dict, List, Tuple

def parse_frontmatter(content: str) -> Dict[str, str]:
    meta = {}
    if not content.startswith("---"):
        return meta
    parts = content.split("---", 2)
    if len(parts) < 3:
        return meta
    yaml_block = parts[1]
    
    current_key = None
    multiline_val = []

    for line in yaml_block.splitlines():
        trimmed = line.strip()
        if not trimmed or trimmed.startswith("#"):
            continue
        
        # Check if new key
        if ":" in line and not line.startswith(" ") and not line.startswith("\t"):
            if current_key and multiline_val:
                meta[current_key] = " ".join(multiline_val).strip().strip("'\"")
                multiline_val = []
            
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip()
            if v in [">", "|", ">-", "|-"]:
                current_key = k
                multiline_val = []
            else:
                current_key = None
                meta[k] = v.strip().strip("'\"")
        elif current_key and (line.startswith(" ") or line.startswith("\t")):
            multiline_val.append(trimmed)

    if current_key and multiline_val:
        meta[current_key] = " ".join(multiline_val).strip().strip("'\"")

    return meta

def check_catalog(skills_dir: str) -> Tuple[bool, List[str], List[str]]:
    errors = []
    warnings = []
    descriptions: Dict[str, str] = {}

    skill_folders = [d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))]
    print(f"Auditing {len(skill_folders)} skills in catalog: {skills_dir}\n")

    for skill_name in sorted(skill_folders):
        skill_file = os.path.join(skills_dir, skill_name, "SKILL.md")
        if not os.path.exists(skill_file):
            errors.append(f"[{skill_name}] Missing SKILL.md")
            continue

        try:
            with open(skill_file, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()
        except Exception as e:
            errors.append(f"[{skill_name}] Read error: {e}")
            continue

        meta = parse_frontmatter(content)
        desc = meta.get("description", "").strip()

        if not desc:
            warnings.append(f"[{skill_name}] Missing or empty 'description' in frontmatter")
            continue

        if len(desc) < 15:
            warnings.append(f"[{skill_name}] Description is suspiciously short (<15 chars): '{desc}'")

        # Collision detection (identical descriptions)
        if desc in descriptions:
            errors.append(f"Description collision between '{skill_name}' and '{descriptions[desc]}'")
        else:
            descriptions[desc] = skill_name

    return len(errors) == 0, errors, warnings

if __name__ == "__main__":
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    skills_path = os.path.join(repo_root, "skills")
    success, errors, warnings = check_catalog(skills_path)

    print(f"Warnings: {len(warnings)}")
    for w in warnings[:10]:
        print(f"  ! {w}")
    if len(warnings) > 10:
        print(f"  ... and {len(warnings) - 10} more warnings")

    if not success:
        print(f"\nErrors: {len(errors)}")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)

    print("\n✓ Description collision and catalog audit PASSED.")
    sys.exit(0)
