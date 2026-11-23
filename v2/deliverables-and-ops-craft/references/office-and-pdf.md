# Office, PDF & Editorial HTML Deliverables

Generating a binary file that "opens" is the bare minimum. Flagship deliverables look like a senior analyst or designer built them by hand, with zero formula errors, zero clipped tables, and zero orphaned headings.

## 1. Format-Specific Engineering Standards

### PDF (`.pdf`)
- **Margins & Grid**: Minimum `0.6in–0.75in` margins; consistent header/footer with page numbers (`Page X of Y`) on multi-page reports.
- **Page-Break Hygiene**: Never leave a heading orphaned at the bottom of a page (`break-after: avoid`). Never split a small table or callout box awkwardly across pages (`break-inside: avoid`).
- **Tables**: Repeat `<thead>` across page breaks; right-align numbers with `tabular-nums`; left-align text; never clip wide columns—wrap or switch to landscape.

### Excel (`.xlsx`)
- **Formulas Over Hardcoded Values**: Every total, subtotal, variance, and ratio must be a live Excel formula (`=SUM(...)`, `=IFERROR(..., 0)`, `=XLOOKUP(...)`), never a Python-computed static number.
- **Number Formatting**: Explicit currency (`$#,##0.00`), percentage (`0.0%`), and date (`YYYY-MM-DD`) formats.
- **Readability**: Freeze header rows, auto-fit column widths with `+2` padding, and use subtle zebra striping or hairline borders.

### Word (`.docx`)
- **Styles Over Direct Formatting**: Use semantic Heading 1/2/3 styles so the document navigation pane works.
- **Tables & Images**: Set explicit column widths and `cantSplit` on table rows.

### PowerPoint (`.pptx`)
- **One Takeaway Per Slide**: Title = the insight (e.g., *"Q3 churn dropped 18% after onboarding redesign"*), not a generic label (*"Q3 Metrics"*).
- **Density Cap**: Max 4–6 concise bullets or 1 primary chart/table per slide. Minimum `14pt` body text, `24pt+` titles.

## 2. Mandatory Sandbox Verification

Before delivering any binary file:
1. Verify file size > 0 and open/parse it back in Python to confirm zero corruption.
2. For `.xlsx`, verify every formula cell starts with `=` and no `#REF!`, `#DIV/0!`, `#VALUE!`, or `#NAME?` errors exist.
3. For `.pdf` / `.pptx`, render pages to images (when `pdftoppm` / LibreOffice is available in the sandbox) and visually inspect for clipping, overlaps, or blank pages.
