#!/usr/bin/env python3
"""Offline stdlib-only WCAG 2.1 contrast ratio checker."""

import sys


def hex_to_rgb(h: str) -> tuple[float, float, float]:
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Invalid hex color: #{h}")
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def rel_luminance(rgb: tuple[float, float, float]) -> float:
    def lin(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg: str, bg: str) -> float:
    l1 = rel_luminance(hex_to_rgb(fg))
    l2 = rel_luminance(hex_to_rgb(bg))
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: check_contrast.py <fg_hex> <bg_hex>")
        return 1
    ratio = contrast_ratio(sys.argv[1], sys.argv[2])
    aa_normal = "PASS" if ratio >= 4.5 else "FAIL"
    aa_large = "PASS" if ratio >= 3.0 else "FAIL"
    print(f"Contrast: {ratio:.2f}:1 | AA Normal (4.5:1): {aa_normal} | AA Large (3.0:1): {aa_large}")
    return 0 if ratio >= 4.5 else 1


if __name__ == "__main__":
    sys.exit(main())
