# Color Systems, Taste Archetypes & Surfaces

Never pick colors from a generic template. Match the palette, contrast, and surface elevation to the product's actual domain and lighting environment.

---

## 1. Domain Taste Archetypes

| Archetype | Base Canvas | Elevated Surface | Primary Ink | Muted Ink | Dominant Accent |
| --- | --- | --- | --- | --- | --- |
| **Editorial / Finance** | Warm paper `#FAF8F5` | `#FFFFFF` + `1px` `#E7E2DA` | `#1A1816` | `#57534E` | Deep forest `#1B4332` |
| **Developer / Technical** | Crisp slate `#0B0F17` | `#131924` + `1px` `#1F2937` | `#F3F4F6` | `#9CA3AF` | Electric cobalt `#3B82F6` |
| **Industrial / Ops** | Neutral stone `#F4F4F5` | `#FFFFFF` + `1px` `#D4D4D8` | `#09090B` | `#52525B` | Signal orange `#EA580C` |
| **Consumer / Calm** | Soft off-white `#F8FAFC` | `#FFFFFF` + `0 1px 2px` | `#0F172A` | `#475569` | Teal `#0D9488` |

---

## 2. Surface Hierarchy & Elevation

- **Tonal Elevation Over Heavy Shadows**: Separate layers using `2%–5%` lightness shifts and `1px` structural hairlines (`border-color`) rather than muddy `box-shadow` stacks.
- **1 Dominant Accent Rule**: Reserve the accent color strictly for primary CTAs, active navigation states, and focus rings. Secondary actions use neutral ghost/outline styles.
- **Semantic Status Pairing**: Never rely on color alone for status (e.g., red/green). Always pair status colors with an icon or explicit text label (*"Failed"*, *"Paid"*).

---

## 3. Verification & Contrastive Anchors

- Run `python3 scripts/check_contrast.py <fg_hex> <bg_hex>` in Task Mode (`>=4.5:1` normal text, `>=3.0:1` large text/UI).
- **Naive**: Uses `#9CA3AF` muted text on `#FFFFFF` (`2.54:1` — FAILS WCAG AA) and 4 competing neon accents on dark cards.
- **Flagship**: Uses `#4B5563` on `#FFFFFF` (`7.56:1` — PASSES WCAG AA) with 1 calm neutral canvas and 1 intentional accent.
