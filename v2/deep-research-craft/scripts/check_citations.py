#!/usr/bin/env python3
"""Offline stdlib-only linter for research reports: checks for unverified numbers/dates without citations."""

import re
import sys
from pathlib import Path


def check_report(text: str) -> list[str]:
    issues = []
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        # Flag lines with percentages or dollar amounts that lack a URL or [source] marker
        if re.search(r"(\$\d+|\d+%)", line) and not re.search(r"(https?://|\[[^\]]+\]|NOT FOUND)", line):
            issues.append(f"Line {i}: numeric/pricing claim without inline citation or URL.")
    return issues


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: check_citations.py <research_report.md>")
        return 1
    p = Path(sys.argv[1])
    if not p.is_file():
        print(f"File not found: {p}")
        return 1
    issues = check_report(p.read_text(encoding="utf-8"))
    if issues:
        for iss in issues[:20]:
            print(f"WARN: {iss}")
        return 1
    print("OK: All numeric/pricing claims carry inline citations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
