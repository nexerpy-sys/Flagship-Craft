# Accessibility (WCAG 2.1 AA) Architecture

Accessibility is structural, not a coat of paint added at the end. Every interactive surface must work seamlessly with a keyboard, screen reader, and high-contrast display.

---

## 1. Semantic HTML & Landmark Structure

- **Native Elements First**: Use `<button type="button">` for in-page actions and `<a href="...">` for navigation. Never attach `onClick` to a `<div>` or `<span>` without full keyboard (`Enter`/`Space`) and `role="button"` + `tabIndex={0}` semantics.
- **Landmarks**: Structure every page with `<header>`, `<nav>`, `<main>`, and `<footer>`, a single `<h1>`, and sequential heading levels (`h1 -> h2 -> h3`, never skipping levels).
- **Form Labeling**: Every `<input>`, `<select>`, and `<textarea>` must have an explicit `<label for="...">` or `aria-label`. Placeholders are **not** labels.

---

## 2. Keyboard Navigation, Focus & Modals

| Component | Mandatory Keyboard & Focus Behavior |
| --- | --- |
| **All Interactive Controls** | Reachable via `Tab`; visible `:focus-visible` ring (never `outline: none` without replacement). |
| **Modal / Dialog** | Traps focus inside while open; closes on `Escape`; restores focus to the triggering element on close. |
| **Dropdown / Menu** | `ArrowUp`/`ArrowDown` moves between items; `Escape` closes and returns focus to trigger. |
| **Toast / Async Status** | Uses `aria-live="polite"` (or `assertive` for critical errors) so screen readers announce updates without stealing focus. |

---

## 3. Contrast & Touch Targets

- **Contrast**: Minimum `4.5:1` for normal text, `3.0:1` for large text (`>=18pt` or `14pt bold`) and UI borders/icons.
- **Touch Targets**: Minimum `44x44px` hit area on mobile interactive controls.

---

## 4. Contrastive Anchors (Naive vs. Flagship A11y)

1. **Delete Confirmation Modal**:
   - *Naive*: `<div class="modal">` with `<span onClick={close}>X</span>`, no focus trap, and `outline: none` on buttons.
   - *Flagship*: `<dialog>` / `role="dialog" aria-modal="true"` with `aria-labelledby`, focus trapped inside, `Escape` to close, and focus restored to the Delete button on close.
2. **Icon-Only Action Button**:
   - *Naive*: `<button><TrashIcon /></button>` (screen reader announces *"button"*).
   - *Flagship*: `<button type="button" aria-label="Delete invoice"><TrashIcon aria-hidden="true" /></button>`.
