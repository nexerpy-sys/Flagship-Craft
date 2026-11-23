# Color Systems, Taste Archetypes & Surfaces

Never pick colors from a generic template. Match the palette and surface elevation to the product's actual domain:

## 1. Taste Archetypes

| Archetype | Base Canvas | Elevated Surface | Ink | Dominant Accent |
| --- | --- | --- | --- | --- |
| **Editorial / Finance** | Warm paper `#FAF8F5` | `#FFFFFF` + `1px` `#E7E2DA` | `#1A1816` | Deep forest `#1B4332` or oxblood `#7F1D1D` |
| **Developer / Technical** | Crisp slate `#0B0F17` | `#131924` + `1px` `#1F2937` | `#F3F4F6` | Electric cobalt `#3B82F6` |
| **Industrial / Ops** | Neutral stone `#F4F4F5` | `#FFFFFF` + `1px` `#D4D4D8` | `#09090B` | Signal orange `#EA580C` |
| **Consumer / Calm** | Soft off-white `#F8FAFC` | `#FFFFFF` + subtle `0 1px 2px` | `#0F172A` | Teal `#0D9488` |

## 2. Surface & Contrast Discipline

- **Tonal Elevation Over Heavy Shadows**: Use `2%–5%` lightness shifts and `1px` structural hairlines rather than muddy drop shadows.
- **Semantic Pairing**: Never rely on color alone for status (pair red/green/amber with icons or text labels).
- **Deterministic Check**: Run `python3 scripts/check_contrast.py <fg_hex> <bg_hex>` in Task Mode (>=4.5:1 normal text, >=3.0:1 large text/UI).
