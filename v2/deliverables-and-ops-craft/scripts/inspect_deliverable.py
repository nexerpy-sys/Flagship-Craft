#!/usr/bin/env python3
"""Offline stdlib-only deliverable inspector for .csv, .json, .html, .md, .xlsx, .docx, .pptx."""

import csv
import json
import sys
import zipfile
from pathlib import Path

EXCEL_ERRORS = ("#REF!", "#DIV/0!", "#VALUE!", "#NAME?", "#N/A", "#NUM!")


def inspect_file(path: Path) -> list[str]:
    if not path.is_file():
        return [f"File not found: {path}"]
    if path.stat().st_size == 0:
        return [f"Empty file (0 bytes): {path}"]

    ext = path.suffix.lower()
    issues: list[str] = []

    if ext == ".json":
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:
            issues.append(f"Invalid JSON: {e}")
    elif ext == ".csv":
        try:
            with path.open("r", encoding="utf-8", newline="") as f:
                rows = list(csv.reader(f))
            if len(rows) < 2:
                issues.append("CSV has fewer than 2 rows (header + data).")
        except Exception as e:
            issues.append(f"CSV read error: {e}")
    elif ext in {".xlsx", ".docx", ".pptx"}:
        try:
            with zipfile.ZipFile(path, "r") as zf:
                bad = zf.testzip()
                if bad:
                    issues.append(f"Corrupt ZIP entry in {ext}: {bad}")
                if ext == ".xlsx":
                    for name in zf.namelist():
                        if name.startswith("xl/worksheets/") and name.endswith(".xml"):
                            xml = zf.read(name).decode("utf-8", errors="ignore")
                            for err in EXCEL_ERRORS:
                                if err in xml:
                                    issues.append(f"Excel formula error '{err}' found in {name}")
        except zipfile.BadZipFile:
            issues.append(f"Corrupt Office archive: {path}")
    return issues


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: inspect_deliverable.py <file>")
        return 1
    p = Path(sys.argv[1])
    issues = inspect_file(p)
    if issues:
        for iss in issues:
            print(f"WARN: {iss}")
        return 1
    print(f"OK: {p.name} ({p.stat().st_size} bytes) passed deliverable inspection.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
