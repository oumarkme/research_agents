---
name: plotting
description: 'Use for any figure, plot, chart, or heatmap: Nature-style 88 mm single-column spec, Okabe-Ito palette, viridis, JPEG 300 dpi by default or PDF on request, templates, and a mandatory legibility check.'
---

# Plotting

Draft figures for PowerPoint or slides (JPEG, 300 dpi) and publication figures (vector PDF), following the Nature figure guidelines, the Nature Reviews "Guide to designing figures", and Rougier et al. (2014).

## Workflow

1. State the one message of the figure.
2. Mode: default JPEG at 300 dpi. Publication PDF (Okabe-Ito colors plus texture, so groups stay distinct in grayscale) only when the user asks for journal or print quality. SVG or PNG only on explicit request.
3. Source `${CLAUDE_SKILL_DIR}/templates/theme_nature.R` (R) or `theme_nature.py` (Python) for the theme, palette, and `save_fig()`; the file extension selects the format. Do not re-implement them. Pick R or Python by context; ggplot2 or plotnine first, matplotlib only for what they cannot do. Needs: R with ggplot2, svglite, ggrastr, ragg, ggpattern, or Python with plotnine, matplotlib, Pillow; `pdftoppm` (PDF) and `rsvg-convert` (SVG) for previews. If something is missing, say so before installing.
4. Render, then check: `python ${CLAUDE_SKILL_DIR}/scripts/check_png.py <file.jpeg>` (add `--gray` only on request), `check_pdf.py <file.pdf>`, or `check_svg.py <file.svg>`.
5. Do the legibility check below, fix, and re-render until it passes.
6. After the last change, check and view the final file again. Never report a figure you have not viewed in its final state.
7. Report the path and what was checked. Error-bar definitions, n, and explanations go in the caption you give the user, not in the figure.

## Output

* JPEG: RGB, 300 dpi, quality 95 (never lower), opaque white background, no title.
* One plot per file, 88 mm wide, at most 247 mm high, created at that size and never rescaled, so text stays 7 to 8 pt. No subfigures, panel labels, or facet grids that read as multi-panel; write separate files.
* File names describe the content; no figure numbers or ordering prefixes.
* Set text, line, and point sizes in pt (`pt_lw(pt)` for lines), then measure a known element in the output (px = pt / 72 x dpi) and view it.
* PDF details, dense-layer rasterization, SVG and PNG: `${CLAUDE_SKILL_DIR}/references/design.md`.

## Palette

* Okabe-Ito, set explicitly and taken in this order, first n: blue `#0072B2`, vermillion `#D55E00`, bluish green `#009E73`, orange `#E69F00`, sky blue `#56B4E9`, reddish purple `#CC79A7`, yellow `#F0E442`. Templates: `PALETTE` / `lab_fill`, `PALETTE_LINE` / `lab_line`; `scale_color_lab(line=True)`, `scale_fill_lab()`.
* Lines and thin marks: blue, vermillion, bluish green, reddish purple (3:1 or more on white). Colored text: blue only (4.5:1); vermillion and bluish green only as large bold text. Orange, sky blue, and yellow are fills with a dark edge. Black is the reference or control, not a category. Gray (`#BDBDBD`, lines `#757575`) is context.
* Use color only where it makes the information clearer; the rest stays black and gray. The focus group is blue (`focus_colors()`) and the other groups are gray. Four colored groups at once is typical; seven is the limit and needs direct labels or texture.
* A group keeps its color, shape, order, and orientation within a figure and across the figures of a project. Use a field convention color (for example a disease or tissue color) only when one exists, and state it in the caption.
* Continuous data, including data centered on a value: viridis. For centered data, use symmetric limits and mark the center. No jet, rainbow, Turbo, or red-green. Always draw the colorbar (Crameri et al., 2020).
* Read `${CLAUDE_SKILL_DIR}/references/color.md` for any continuous map, more than 4 groups, or a projected figure.

## Text

* One sans-serif throughout (Arial, Liberation Sans, Helvetica, or DejaVu Sans as a last resort). Check that the font resolves in your library, with no silent fallback.
* 7 pt for tick labels, legends, and annotations; 8 pt for axis titles (Nature house style 8 pt; drafts at least 7 pt). Never below 7. Black type on white. On colored fills, black text, except white on blue. Short labels, few abbreviations (define each in the caption).
* Emphasis by position, bold, or color only. No italic or size changes for emphasis; italic only for gene and species names and variables.
* Label the first instance of every object, and label directly rather than relying on color alone. Axes carry units; a key explains every color and symbol. Keep legends to five entries or fewer.
* Information flows top-left to bottom-right; no circular layouts unless the process is a cycle.
* If the content is a list or categories without a process or measured data, give a table, not a figure.

## Legibility check (mandatory)

View the file with Read at full size and zoomed on each crowded region (crop with PIL; for a PDF, re-run `pdftoppm -r 600`). Pass only if: text is at least 7 pt, readable, unclipped, and does not overlap; lines and points are visible and distinguishable by style or shape as well as color; axes, ticks, and units are visible; groups are separable (view the gray preview for PDFs and fix every pair the check warns about); the figure is 88 mm wide and legible at 100% in PowerPoint. If nothing is crowded, say so.

Design rules, gray-print texture, and overlap handling: `${CLAUDE_SKILL_DIR}/references/design.md`. Read it for publication PDFs, more than 3 groups, or crowded plots. Core: one message per figure, minimal decoration, label axes with units, show individual points over box or bar plots.
