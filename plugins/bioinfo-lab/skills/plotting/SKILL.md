---
name: plotting
description: 'Use for any figure, plot, chart, or heatmap: Nature-style 88 mm single-column spec, muted 8-color palette, JPEG 300 dpi by default or PDF on request, templates, and a mandatory legibility check.'
---

# Plotting

Manuscript-draft figures for PowerPoint or slides (JPEG, 300 dpi) and publication figures as vector PDF, following the Nature figure guidelines and the Nature Reviews "Guide to designing figures" (hierarchy, clarity, accessibility), plus Rougier et al. (2014).

## Workflow

1. State the one message of the figure.
2. Mode: default JPEG at 300 dpi. Publication PDF (muted colors plus texture, so groups survive gray printing) only when the user asks for journal or print quality. SVG or PNG only on explicit request.
3. Source `${CLAUDE_SKILL_DIR}/templates/theme_nature.R` (R) or `theme_nature.py` (Python) for the theme, palette, and `save_fig()`; the file extension selects the format. Do not re-implement them. Choose R or Python by context; use ggplot2 or plotnine first, matplotlib only for what they cannot do. Needs: R with ggplot2, svglite, ggrastr, ragg, ggpattern, or Python with plotnine, matplotlib, Pillow; `pdftoppm` (PDF) and `rsvg-convert` (SVG) for previews. If something is missing, say so before installing.
4. Render, then check: `python ${CLAUDE_SKILL_DIR}/scripts/check_png.py <file.jpeg>` (add `--gray` only on request), `check_pdf.py <file.pdf>`, or `check_svg.py <file.svg>`.
5. Do the legibility check below, fix, and re-render until it passes.
6. After the last change, including recoloring, check and view the final file again. Never report a figure you have not viewed in its final state.
7. Report the path and what was checked. Error-bar definitions, n, and explanations go in the caption text you give the user, not in the figure.

## Output

* JPEG: RGB, 300 dpi, quality 95 (never lower), opaque white background, no title.
* One plot per file, 88 mm wide, at most 247 mm high, created at that size and never rescaled, so text stays 7 to 8 pt. No subfigures, panel labels, or facet grids that read as multi-panel; write separate files.
* File names describe the content; no figure numbers or ordering prefixes.
* Set text, line, and point sizes in pt (`pt_lw(pt)` for lines), then measure a known element in the output (px = pt / 72 x dpi) and view it.
* PDF details, dense-layer rasterization, SVG and PNG: `${CLAUDE_SKILL_DIR}/references/design.md`.

## Palette

* Muted palette, eight colors at most (Tol muted set, color-blind safe, checked for Nature: few colors, no red-green, black type), set explicitly and used in this order, first n: indigo `#332288`, rose `#CC6677`, wine `#882255`, green `#117733`, cyan `#88CCEE`, olive `#999933`, sand `#DDCC77`, purple `#AA4499`. Templates: `PALETTE` / `lab_fill`, `PALETTE_LINE` / `lab_line`; `scale_color_lab(line=True)`, `scale_fill_lab()`.
* Lines and thin marks: only indigo, rose, wine, green, purple (at least 3:1 on white). Colored text: indigo, wine, green, purple (at least 4.5:1); rose is not for text. Cyan, olive, and sand are fill only, with a dark edge. Black is the reference or control, not a category; gray (`#BDBDBD`, lines `#757575`) is context.
* Hierarchy: color carries the message. The focus group gets indigo (`focus_colors()`) and context groups go gray; four colored groups at once is typical (Nature: five items per list is optimal); use up to eight only with direct labels or texture.
* Consistency: a group keeps the same color, shape, order, and orientation within a figure and across the project's figures. Use a convention color (for example a disease or tissue standard) only when the field has one, and say so in the caption.
* Sequential data: viridis. Data centered on a value: `scale_*_lab_div()` or `cmap_diverging()`. Never jet, rainbow, Turbo, or red-green; always draw the color bar (Crameri et al., 2020).
* Read `${CLAUDE_SKILL_DIR}/references/color.md` for any continuous map, more than 4 groups, or a projected figure.

## Text

* One sans-serif throughout (Arial, Liberation Sans, Helvetica, or DejaVu Sans as a last resort). Check that the font resolves in your library, with no silent fallback.
* 7 pt for tick labels, legends, and annotations; 8 pt for axis titles (Nature house style 8 pt; drafts at least 7 pt). Never below 7. Black type on white; contrast of at least 4.5:1 on colored fills. Short labels, few abbreviations (define each in the caption).
* Emphasis by position, bold, or color only. No italic or size changes for emphasis; italic only for gene and species names and variables.
* Label the first instance of every object, and label directly rather than relying on color alone. Axes carry units; a key explains every color and symbol. Keep legends to five entries or fewer.
* Information flows top-left to bottom-right; no circular layouts unless the process is a cycle.
* If the content is a list or categories without a process or measured data, give a table, not a figure.

## Legibility check (mandatory)

View the file with Read at full size and zoomed on each crowded region (crop with PIL; for a PDF, re-run `pdftoppm -r 600`). Pass only if: text is at least 7 pt, readable, unclipped, and does not overlap; lines and points are visible and distinguishable by style or shape as well as color; axes, ticks, and units are visible; groups are separable (view the gray preview for PDFs and fix every pair the check warns about); the figure is 88 mm wide and legible at 100% in PowerPoint. If nothing is crowded, say so.

Design rules, gray-print texture, and overlap handling: `${CLAUDE_SKILL_DIR}/references/design.md`. Read it for publication PDFs, more than 3 groups, or crowded plots. Core: one message per figure, minimal decoration, label axes with units, show individual points over box or bar plots.
