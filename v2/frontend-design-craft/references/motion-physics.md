# Motion Physics, Choreography & Accessibility

Motion is not decoration. Every animation must earn its pixels by doing one of three jobs: **explaining a spatial relationship**, **confirming a state change**, or **guiding attention** during a transition.

---

## 1. Performance & GPU-Only Discipline

- **Animate Only `transform` and `opacity`**: Never animate `width`, `height`, `top`, `left`, `margin`, or `padding`—they trigger layout recalculations and jank on 60Hz/120Hz displays.
- **Will-Change Restraint**: Apply `will-change: transform` only on elements actively animating, never globally.
- **No Layout Thrashing**: Never interleave DOM reads (`getBoundingClientRect`) and writes (`element.style.transform = ...`) inside a loop.

---

## 2. Timing, Easing & Choreography

| Interaction Type | Duration | Easing | Rule |
| --- | --- | --- | --- |
| **Micro-interaction** (button press, toggle, hover) | `120ms–180ms` | `cubic-bezier(0.2, 0, 0, 1)` | Snappy, immediate feedback. |
| **Panel / Drawer / Modal** (enter) | `220ms–280ms` | `cubic-bezier(0.22, 1, 0.36, 1)` | Fast start, smooth settle. |
| **Panel / Drawer / Modal** (exit) | `150ms–200ms` | `cubic-bezier(0.4, 0, 1, 1)` | Exits should be faster than entrances. |
| **Staggered List** | `20ms–40ms` per item | Cap total stagger at `<=240ms` | Never make the user wait for item #12. |

---

## 3. Accessibility (`prefers-reduced-motion`)

- Always wrap non-essential motion in `@media (prefers-reduced-motion: reduce)`.
- Under reduced motion, replace translations/scales with instant state changes or subtle `100ms` opacity fades—never leave elements stuck invisible (`opacity: 0`).

---

## 4. Contrastive Anchors (Naive vs. Flagship Motion)

- **Naive**: Animates `height: 0 -> auto` on accordions, uses `500ms ease-in-out` on every button, staggers 20 table rows by `100ms` each (2 full seconds of waiting), and ignores `prefers-reduced-motion`.
- **Flagship**: Uses `transform` + `opacity` at `150ms–240ms`, caps list stagger at `<=200ms`, and respects `prefers-reduced-motion: reduce` cleanly.
