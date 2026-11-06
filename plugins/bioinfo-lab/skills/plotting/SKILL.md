---
name: plotting
description: 'Use for any figure, plot, chart, or heatmap: Nature-style 88 mm single-column spec, Okabe-Ito palette, viridis, JPEG 300 dpi by default or PDF on request, templates, and a mandatory legibility check.'
---

# Plotting

Draft figures (JPEG, 300 dpi) and publication figures (vector PDF) after the Nature figure guidelines, the Nature Reviews "Guide to designing figures", and Rougier et al. (2014).

## Workflow

1. State the one message of the figure.
2. Mode: default JPEG at 300 dpi. Publication PDF (color plus texture) only when the user asks for journal or print quality. SVG or PNG only on explicit request.
3. Source `${CLAUDE_SKILL_DIR}/templates/theme_nature.R` (R) or `theme_nature.py` (Python) for the theme, palette, and `save_fig()`; the file extension selects the format. Do not re-implement them. Use ggplot2 or plotnine first, matplotlib only for what they cannot do. Needs are listed in `references/design.md` ("Output formats"); if something is missing, say so before installing.
4. Render, then check with `${CLAUDE_SKILL_DIR}/scripts/check_png.py <file.jpeg>` (`--gray` only on request), `check_pdf.py`, or `check_svg.py`.
5. Do the legibility check below, fix, and re-render until it passes.
6. After the last change, check and view the final file again. Never report a figure you have not viewed in its final state.
7. Report the path and what was checked. Error-bar definitions, n, and explanations go in the caption you give the user, not in the figure.

## Output

* JPEG: RGB, 300 dpi, quality 95 (never lower), opaque white background, no title.
* One plot per file, 88 mm wide, at most 247 mm high, created at that size and never rescaled, so text stays 7 to 8 pt. No subfigures, panel labels, or facet grids that read as multi-panel; write separate files.
* File names describe the content, with no figure numbers.
* Set sizes in pt (`pt_lw(pt)` for lines) and measure a known element in the output (px = pt / 72 x dpi).
* PDF details, dense-layer rasterization, SVG and PNG: `${CLAUDE_SKILL_DIR}/references/design.md`.

## Palette and text

* Categories: Okabe-Ito, set explicitly, in the order of `references/color.md` (the single source of hex codes and contrast; do not copy them elsewhere). Continuous data: viridis, never jet, rainbow, Turbo, or red-green, with a drawn colorbar. Color only where it clarifies; the focus group is blue and the rest gray. A group keeps its color in every figure of a project.
* Read `${CLAUDE_SKILL_DIR}/references/color.md` for template color objects, any continuous map, more than 4 groups, or a projected figure.
* Text: one sans-serif font; 7 pt minimum (8 pt axis titles); black on white; axes carry units. Read `${CLAUDE_SKILL_DIR}/references/design.md` ("Text and legibility") for font, labeling, and layout rules.

## Legibility check (mandatory)

View the file with Read at full size and zoomed on each crowded region (crop with PIL; for a PDF, re-run `pdftoppm -r 600`). Pass only if text is at least 7 pt, readable, unclipped, and non-overlapping; lines and points are distinguishable by style or shape as well as color; axes, ticks, and units are visible; groups are separable in the gray preview (PDF), and you fix every pair the check warns about; and the figure is 88 mm wide and legible at 100% in PowerPoint. If nothing is crowded, say so.

Read `design.md` also for publication PDFs, more than 3 groups, or crowded plots.
