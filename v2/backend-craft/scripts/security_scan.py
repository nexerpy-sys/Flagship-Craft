#!/usr/bin/env python3
"""Offline stdlib-only static security scanner for backend code (.py, .js, .sh)."""

import re
import sys
from pathlib import Path

RULES = [
    ("HARDCODED_SECRET", re.compile(r"(api_key|secret_key|password|token)\s*=\s*['\"][^'\"]{8,}['\"]", re.I)),
    ("UNSAFE_SHELL", re.compile(r"shell\s*=\s*True")),
    ("SQL_INTERPOLATION", re.compile(r"(SELECT|INSERT|UPDATE|DELETE)\s+.*(\{[^}]+\}|%s\s*%\s*|\+\s*[a-zA-Z_])", re.I)),
    ("EVAL_EXEC", re.compile(r"\b(eval|exec)\s*\(")),
]


def scan_file(path: Path) -> list[str]:
    findings = []
    for i, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        for name, pat in RULES:
            if pat.search(line):
                findings.append(f"{path}:{i}: [{name}] {line.strip()[:80]}")
    return findings


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: security_scan.py <file_or_dir>")
        return 1
    target = Path(sys.argv[1])
    files = [target] if target.is_file() else [
        p for p in target.rglob("*") if p.is_file() and p.suffix in {".py", ".js", ".sh"}
    ]
    all_findings = []
    for f in files:
        all_findings.extend(scan_file(f))
    if all_findings:
        for item in all_findings[:30]:
            print(f"WARN: {item}")
        return 1
    print(f"OK: Scanned {len(files)} file(s), 0 security patterns flagged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
