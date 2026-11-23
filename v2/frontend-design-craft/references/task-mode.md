# Task Mode Adapter (Frontend Design Craft)

In **Gemini Task Mode**, you can build, render, and visually inspect the real UI:

1. **Deterministic Token Checks**: Run `python3 scripts/check_contrast.py <fg_hex> <bg_hex>` on all primary/muted text pairs before rendering.
2. **Multi-Viewport Inspection**: Render the UI and inspect actual screenshots at:
   - **375px** (mobile): zero horizontal overflow, readable tap targets (`>=44px`), clean single-column stack.
   - **768px** (tablet): balanced grid, no awkward orphan columns.
   - **1440px** (desktop): constrained prose measure (`55ch–72ch`), clear focal point.
3. **Visual Critique Loop**: Name the **single weakest visual element** in the rendered screenshots, fix it, and re-inspect before reporting done.
