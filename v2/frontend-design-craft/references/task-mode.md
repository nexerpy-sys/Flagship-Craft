# Task Mode Adapter (Frontend Design Craft)

In **Gemini Task Mode**, you can build, lint, render, and visually inspect the real UI.

## Execution Rules
1. **Mandatory Contrast Check**: Run `python3 scripts/check_contrast.py <fg_hex> <bg_hex>` on all primary and muted text pairs (`>=4.5:1` normal, `>=3.0:1` large) before rendering.
2. **Multi-Viewport Inspection**: Render the UI and inspect actual screenshots at **375px** (mobile), **768px** (tablet), and **1440px** (desktop).
3. **Visual Critique Loop**: Name the **single weakest visual element** in the rendered screenshots, fix it, and re-inspect before reporting done.
