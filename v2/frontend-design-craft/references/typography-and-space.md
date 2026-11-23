# Typography & Spatial Rhythm

Typography carries 80% of a UI's perceived craft. If the type scale, line-height, and spacing rhythm are sloppy, no color palette or animation will save it.

---

## 1. Type Scale & Hierarchy

| Role | Size | Tracking | Line Height | Weight |
| --- | --- | --- | --- | --- |
| **Display / Hero** | `2.25rem–3.5rem` (`36px–56px`) | `-0.025em` | `1.1–1.15` | `600–700` |
| **Section / H2** | `1.5rem–1.875rem` (`24px–30px`) | `-0.015em` | `1.25` | `600` |
| **Card / Group H3** | `1.125rem–1.25rem` (`18px–20px`) | `-0.01em` | `1.35` | `600` |
| **Body** | `1rem` (`16px`) | `0` | `1.5–1.6` | `400` |
| **Metadata / Caption** | `0.75rem–0.875rem` (`12px–14px`) | `0.01em` | `1.4` | `400–500` |

---

## 2. Essential Typographic Rules

- **Measure (Line Length)**: Constrain prose to `55ch–72ch`. Never let paragraphs span a 1440px viewport.
- **Tabular Numerals**: Always apply `font-variant-numeric: tabular-nums` to tables, prices, KPIs, timestamps, and counters so digits align vertically.
- **Minimum Readable Size**: Never drop primary body copy below `14px` (`0.875rem`).

---

## 3. Spatial Rhythm (`4px / 8px` Scale) & Contrastive Anchors

- Stick to a strict scale: `4, 8, 12, 16, 24, 32, 48, 64, 96`.
- **Proximity Rule**: Space *between* distinct sections (`48px–64px`) must be at least **2x–3x** the space *within* a related group (`12px–16px`).
- **Naive**: 18px H1 vs. 16px body, 110ch wide paragraphs, proportional digits jumping sideways in a price column.
- **Flagship**: 40px H1 vs. 16px body, `64ch` max-width prose, `tabular-nums` on all numeric columns, and crisp `16px`/`48px` internal/external spacing.
