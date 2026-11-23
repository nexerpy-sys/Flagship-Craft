#!/usr/bin/env python3
"""Offline stdlib-only HTML accessibility linter."""

from html.parser import HTMLParser
import sys
from pathlib import Path


class A11yParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.issues: list[str] = []
        self.has_main = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        if tag == "main":
            self.has_main = True
        elif tag == "img" and "alt" not in attr_map:
            self.issues.append("<img> missing 'alt' attribute.")
        elif tag == "input" and attr_map.get("type") not in {"hidden", "submit", "button"}:
            if "aria-label" not in attr_map and "aria-labelledby" not in attr_map and "id" not in attr_map:
                self.issues.append("<input> missing 'id', 'aria-label', or 'aria-labelledby'.")
        elif tag == "html" and "lang" not in attr_map:
            self.issues.append("<html> missing 'lang' attribute.")


def check_html(text: str) -> list[str]:
    parser = A11yParser()
    parser.feed(text)
    if not parser.has_main:
        parser.issues.append("Document missing <main> landmark.")
    return parser.issues


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: check_a11y.py <file.html>")
        return 1
    p = Path(sys.argv[1])
    if not p.is_file():
        print(f"File not found: {p}")
        return 1
    issues = check_html(p.read_text(encoding="utf-8", errors="ignore"))
    if issues:
        for iss in issues:
            print(f"WARN: {iss}")
        return 1
    print("OK: HTML passed basic a11y checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
