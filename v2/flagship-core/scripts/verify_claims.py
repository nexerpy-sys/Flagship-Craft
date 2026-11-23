#!/usr/bin/env python3
"""Offline stdlib-only linter to check final reports for A-E verification hygiene."""

import re
import sys
from pathlib import Path

WEASEL_PHRASES = [
    r"\bshould work\b",
    r"\bprobably works\b",
    r"\blooks good\b",
    r"\bseems fine\b",
    r"\bassuming it works\b",
]


def lint_report(text: str) -> list[str]:
    warnings = []
    for pat in WEASEL_PHRASES:
        for m in re.finditer(pat, text, flags=re.IGNORECASE):
            warnings.append(f"Unverified weasel phrase '{m.group(0)}'—replace with explicit Level A-E tag.")
    if "Level A" not in text and "Level B" not in text and "Not Verified" not in text:
        warnings.append("Report lacks explicit A-E verification tags or a Not Verified section.")
    return warnings


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: verify_claims.py <report.md>")
        return 1
    p = Path(sys.argv[1])
    if not p.is_file():
        print(f"File not found: {p}")
        return 1
    warnings = lint_report(p.read_text(encoding="utf-8"))
    if warnings:
        for w in warnings:
            print(f"WARN: {w}")
        return 1
    print("OK: Report passes A-E verification hygiene.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
