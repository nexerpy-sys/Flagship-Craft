# Chat Mode Adapter (Frontend Design Craft)

In **Gemini Chat Mode**, you have **no browser renderer** and **no sandbox**—and Skills do **not** run inside Gemini's Canvas tool.

## Execution Rules
1. **Design Tokens First**: Define explicit color hexes, type scale, and `4px/8px` spacing tokens before writing HTML/CSS.
2. **Manual Contrast & Anti-Slop Check**: Because `scripts/check_contrast.py` cannot run here, manually avoid light-gray-on-white (`#9CA3AF` on `#FFFFFF`) and apply the Anti-Slop Kill-List.
3. **Canvas Handoff**: If the user wants interactive Canvas co-editing, deliver clean, self-contained HTML/CSS/JS they can paste directly into Canvas.
4. **Honest Verification Label**: Close with: *"Visual rendering and contrast not verified (Level E—no browser/sandbox in Chat Mode)."*
