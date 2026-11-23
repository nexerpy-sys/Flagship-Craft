# Accessibility (WCAG 2.1 AA) Architecture

Accessibility is structural, not a coat of paint added at the end.

---

## 1. Semantic HTML & Landmarks

- Use `<button type="button">` for in-page actions and `<a href="...">` for navigation—never `<div onClick>`.
- Structure every page with `<header>`, `<nav>`, `<main>`, and `<footer>` landmarks, plus a single `<h1>` and sequential heading levels (`h1 -> h2 -> h3`).
- Every form control (`<input>`, `<select>`, `<textarea>`) must have an explicit `<label for="...">` or `aria-label`.

---

## 2. Keyboard, Focus & Modals

- **Keyboard Reachability**: Every interactive element must be reachable via `Tab` and activatable via `Enter` / `Space`.
- **Focus Visibility**: Never use `outline: none` without a clear `:focus-visible` replacement ring.
- **Modal / Drawer Discipline**: Trap focus inside open modals, close on `Escape`, and restore focus to the triggering element on close.
- **Dynamic Updates**: Use `aria-live="polite"` for toast notifications and async status updates.

---

## 3. Deterministic Verification

In Task Mode, run `python3 scripts/check_a11y.py <file.html>` on generated HTML and `check_contrast.py` on color pairs before reporting done.
