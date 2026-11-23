# Taste, Art Direction & Anti-Slop Kill-List

Every visual surface you build is judged in the first 500 milliseconds. Competent AI UI looks like a template; flagship UI feels intentional, calm, and unmistakably tailored to its domain.

---

## 1. The Anti-Slop Kill-List (Ban by Default)

If you catch yourself reaching for any of these, stop and redesign:

- **Purple/Blue SaaS-Slop Gradients**: Never default to `#6366F1 -> #8B5CF6` gradients on dark `#0F172A` cards. Choose a palette rooted in the product's actual domain (warm paper + ink for editorial/finance, crisp slate + cobalt for developer tools, neutral stone + signal orange for industrial/ops).
- **Card-Soup**: Never wrap every 2-line metric, list item, or control in a bordered, shadowed, `rounded-xl` box. Use **whitespace, alignment, hairline dividers (`1px solid`), and typographic scale** first. Reserve cards only for genuinely distinct, interactive, or scannable entities.
- **Timid Hierarchy**: If H1, H2, and body text only differ by 2px–4px, the page has no focal point. Establish unmistakable contrast in size, weight, and color.
- **Unanchored Floating Badges & Pill Overload**: Every status pill, tag, and icon must earn its pixels. If a badge repeats information already obvious from context, delete it.
- **Centered-Everything Syndrome**: Left-align body copy, tables, and dense UIs. Center-align only hero statements, empty states, or narrow modals.
- **Fake Glassmorphism & Heavy Drop Shadows**: Avoid `backdrop-blur` + muddy `box-shadow` stacks on every surface. Prefer crisp tonal elevation (2%–5% lightness shift) and `1px` structural hairlines.

---

## 2. Art Direction & Layout Composition

Before writing CSS, lock these four decisions:
1. **Density Mode**:
   - *Editorial / Marketing*: Generous whitespace (`64px–120px` section gaps), `55ch–68ch` reading measure, expressive display type.
   - *Operational / Dashboard*: Tight, scannable grid (`12px–16px` gaps), `tabular-nums`, high information-to-chrome ratio, sticky headers.
2. **Grid & Alignment**: Align every element to an explicit column grid. Misaligned 2px–4px offsets between headers, cards, and inputs immediately signal amateur work.
3. **Focal Point**: Every viewport must have **one** primary visual anchor (the hero metric, the primary chart, or the main action) and clear secondary/tertiary layers.
4. **Responsive Breakpoints**: Design intentionally for **375px** (mobile), **768px** (tablet), and **1440px** (desktop)—never let desktop tables or multi-column grids simply squish or overflow horizontally.

---

## 3. Contrastive Anchors (Naive vs. Flagship UI)

1. **Dashboard Overview**:
   - *Naive*: 6 glowing gradient cards at the top, 3 mismatched icon styles, pie charts with 9 slices, cramped 12px gray-on-gray labels, and horizontal scrollbars on 375px mobile.
   - *Flagship*: Clean tonal canvas, 1 primary KPI strip with `tabular-nums` and delta indicators, 1–2 focused charts with direct data labels, crisp 4.5:1+ contrast, and a deliberate single-column stack on 375px.
2. **Data Table**:
   - *Naive*: Center-aligned numbers that don't line up vertically, truncated headers, no empty state, and `box-shadow` on every row.
   - *Flagship*: Left-aligned text, right-aligned `tabular-nums` numbers, sticky header, `1px` hairline row dividers, and an actionable empty state.
