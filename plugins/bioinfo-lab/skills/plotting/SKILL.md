---
name: plotting
description: 'Use for any figure, plot, chart, or heatmap: Nature-style 88 mm single-column spec, Okabe-Ito colors, JPEG 300 dpi by default or PDF on request, templates, and a mandatory legibility check.'
---

# Plotting

Manuscript-draft figures for PowerPoint or slides (JPEG, 300 dpi) and publication figures as vector PDF, following the Nature figure guidelines (plus Rougier et al., 2014).

## Workflow

1. State the one message of the figure.
2. Mode: default JPEG at 300 dpi. Publication PDF (Okabe-Ito colors plus texture, so groups survive gray printing) only when the user asks for journal or print quality. SVG or PNG only on explicit request.
3. Source `${CLAUDE_SKILL_DIR}/templates/theme_nature.R` (R) or `theme_nature.py` (Python) for the theme, palette, and `save_fig()`; the file extension selects the format. Do not re-implement them. Choose R or Python by context; use ggplot2 or plotnine first, matplotlib only for what they cannot do. Needs: R with ggplot2, svglite, ggrastr, ragg, ggpattern, or Python with plotnine, matplotlib, Pillow; `pdftoppm` (PDF) and `rsvg-convert` (SVG) for previews. If something is missing, say so before installing.
4. Render, then check: `python ${CLAUDE_SKILL_DIR}/scripts/check_png.py <file.jpeg>` (add `--gray` only on request), `check_pdf.py <file.pdf>`, or `check_svg.py <file.svg>`.
5. Do the legibility check below, fix, and re-render until it passes.
6. After the last change, including recoloring, check and view the final file again. Never report a figure you have not viewed in its final state.
7. Report the path and what was checked. Error-bar definitions, n, and explanations go in the caption text you give the user, not in the figure.

## Output

* JPEG: RGB, 300 dpi, quality 95 (never lower), opaque white background, no title.
* One plot per file, 88 mm wide, at most 247 mm high, created at that size and never rescaled, so text stays 6 to 7 pt. No subfigures, panel labels, or facet grids that read as multi-panel; write separate files.
* File names describe the content; no figure numbers or ordering prefixes.
* Set text, line, and point sizes in pt (`pt_lw(pt)` for lines), then measure a known element in the output (px = pt / 72 x dpi) and view it.
* PDF details, dense-layer rasterization, SVG and PNG: `${CLAUDE_SKILL_DIR}/references/design.md`.

## Palette

* Okabe-Ito (Okabe & Ito, 2008), set explicitly: `#E69F00`, `#56B4E9`, `#009E73`, `#F0E442`, `#0072B2`, `#D55E00`, `#CC79A7`, `#000000`. Templates export them.
* Continuous or diverging data: viridis or another perceptually uniform, color-blind-safe map.
* Light colors (`#F0E442`, `#56B4E9`): fills or large markers with a dark edge only; never text or thin lines.

## Text

* One sans-serif throughout (Arial, Liberation Sans, Helvetica, or DejaVu Sans as a last resort). Check that the font resolves in your library, with no silent fallback.
* 6 to 7 pt for all text, never below 6. Black or dark gray on white; contrast of at least 4.5:1 on colored fills. Short labels.

## Legibility check (mandatory)

View the file with Read at full size and zoomed on each crowded region (crop with PIL; for a PDF, re-run `pdftoppm -r 600`). Pass only if: text is readable, unclipped, and does not overlap; lines and points are visible and distinguishable by style or shape as well as color; axes, ticks, and units are visible; groups are separable (view the gray preview for PDFs and fix every pair the check warns about); the figure is 88 mm wide and legible at 100% in PowerPoint. If nothing is crowded, say so.

Design rules, gray-print texture, and overlap handling: `${CLAUDE_SKILL_DIR}/references/design.md`. Read it for publication PDFs, more than 3 groups, or crowded plots. Core: one message per figure, minimal decoration, label axes with units, show individual points over box or bar plots.
