#!/usr/bin/env python3
"""Validate and package each v2 skill into v2/dist/<skill-name>.zip for Gemini import."""

import subprocess
import sys
import zipfile
from pathlib import Path

SKIP_DIRS = {"dist", "__pycache__"}


def main() -> int:
    v2_root = Path(__file__).resolve().parent
    validator = v2_root / "validate_skills.py"
    res = subprocess.run([sys.executable, str(validator)], check=False)
    if res.returncode != 0:
        print("Validation failed; aborting packaging.")
        return 1

    dist_dir = v2_root / "dist"
    dist_dir.mkdir(exist_ok=True)

    skills = sorted(
        p for p in v2_root.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.name not in SKIP_DIRS
    )

    for skill_dir in skills:
        zip_path = dist_dir / f"{skill_dir.name}.zip"
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for file_path in sorted(skill_dir.rglob("*")):
                if file_path.is_file():
                    arcname = file_path.relative_to(skill_dir)
                    zf.write(file_path, arcname)
        print(f"Packaged: {zip_path.relative_to(v2_root)} ({zip_path.stat().st_size} bytes)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
