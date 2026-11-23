# Typography & Spatial Rhythm

Typography carries 80% of a UI's perceived craft. If the type scale, line-height, and spacing rhythm are sloppy, no color palette or animation will save it.

---

## 1. Type Scale & Hierarchy

Establish unmistakable separation between levels:
- **Display / H1**: `2.25rem–3.5rem` (`36px–56px`), tight tracking (`-0.025em`), tight leading (`1.1–1.15`), `font-weight: 600–700`.
- **Section / H2**: `1.5rem–1.875rem` (`24px–30px`), tracking `-0.015em`, leading `1.25`.
- **Body**: `1rem` (`16px`), leading `1.5–1.6`, `font-weight: 400`. Never drop primary body copy below `14px`.
- **Metadata / Caption**: `0.75rem–0.875rem` (`12px–14px`), muted ink, `letter-spacing: 0.01em`.

### Essential Typographic Rules
- **Measure (Line Length)**: Constrain prose to `55ch–72ch`. Never let paragraphs span a 1440px viewport.
- **Tabular Numerals**: Always apply `font-variant-numeric: tabular-nums` to tables, prices, KPIs, timestamps, and counters so digits align vertically.

---

## 2. Spatial Rhythm (`4px / 8px` Scale)

Stick to a strict scale: `4, 8, 12, 16, 24, 32, 48, 64, 96`.
- **Proximity Rule**: Space *between* distinct sections (`48px–64px`) must be at least **2x–3x** the space *within* a related group (`12px–16px`).
- **Optical Alignment**: Align text baselines and icon centers—not just bounding boxes.
