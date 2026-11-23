#!/usr/bin/env python3
"""Offline stdlib-only validator for Gemini v2 skill packages."""

import ast
import os
import re
import sys
from pathlib import Path

BANNED_EXTENSIONS = {
    ".ts", ".tsx", ".jsx", ".sql",
    ".doc", ".xls", ".ppt",
    ".zip", ".tar", ".gz", ".7z",
    ".mp3", ".wav", ".mp4", ".mov", ".avi",
}
BANNED_NAMES = {"__pycache__", "Makefile", ".DS_Store"}
KEBAB_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NETWORK_MODULES = {"urllib", "http", "socket", "ftplib", "smtplib", "poplib", "imaplib", "ssl"}


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    block = text[4:end]
    data = {}
    for line in block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip().strip('"').strip("'")
    return data


def check_python_script(path: Path) -> list[str]:
    errors = []
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as e:
        return [f"{path}: SyntaxError: {e}"]

    stdlib = sys.stdlib_module_names
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                top = alias.name.split(".")[0]
                if top not in stdlib:
                    errors.append(f"{path}: non-stdlib import '{top}'")
                if top in NETWORK_MODULES:
                    errors.append(f"{path}: network module '{top}' not allowed in offline sandbox")
        elif isinstance(node, ast.ImportFrom) and node.module:
            top = node.module.split(".")[0]
            if top not in stdlib:
                errors.append(f"{path}: non-stdlib import '{top}'")
            if top in NETWORK_MODULES:
                errors.append(f"{path}: network module '{top}' not allowed in offline sandbox")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [f"{skill_dir.name}: missing root SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    name = fm.get("name", "")
    desc = fm.get("description", "")

    if not name:
        errors.append(f"{skill_dir.name}: missing frontmatter 'name'")
    elif not KEBAB_RE.match(name):
        errors.append(f"{skill_dir.name}: name '{name}' is not valid kebab-case")
    elif len(name) > 64:
        errors.append(f"{skill_dir.name}: name exceeds 64 chars ({len(name)})")
    elif name != skill_dir.name:
        errors.append(f"{skill_dir.name}: name '{name}' does not match folder name")

    if not desc:
        errors.append(f"{skill_dir.name}: missing frontmatter 'description'")
    elif len(desc) > 1024:
        errors.append(f"{skill_dir.name}: description exceeds 1024 chars ({len(desc)})")

    file_count = 0
    total_bytes = 0
    for root, dirs, files in os.walk(skill_dir):
        for d in list(dirs):
            if d in BANNED_NAMES:
                errors.append(f"{skill_dir.name}: banned directory '{d}'")
        for f in files:
            p = Path(root) / f
            file_count += 1
            total_bytes += p.stat().st_size
            if f in BANNED_NAMES:
                errors.append(f"{p}: banned filename")
            if p.suffix.lower() in BANNED_EXTENSIONS:
                errors.append(f"{p}: banned extension '{p.suffix}'")
            if p.suffix == ".py":
                errors.extend(check_python_script(p))

    if file_count > 100:
        errors.append(f"{skill_dir.name}: exceeds 100 files ({file_count})")
    if total_bytes > 100 * 1024 * 1024:
        errors.append(f"{skill_dir.name}: exceeds 100 MB")

    return errors


def main() -> int:
    v2_root = Path(__file__).resolve().parent
    skills = sorted(
        p for p in v2_root.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.name not in {"dist", "__pycache__"}
    )
    if not skills:
        print("No skill directories found in v2/")
        return 1

    all_errors = []
    for s in skills:
        errs = validate_skill(s)
        if errs:
            all_errors.extend(errs)
        else:
            print(f"OK: {s.name}")

    if all_errors:
        print("\nVALIDATION ERRORS:")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print(f"\nAll {len(skills)} skills passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
