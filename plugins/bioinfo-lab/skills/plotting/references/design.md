# plotting: detailed rules

## Design

* Hierarchy (Nature Reviews guide): one saturated color (blue) on the most important element, neutral gray for context; for data, `focus_colors()` colors the message group and grays the rest. Drop repeated or decorative elements; ask what can be removed and still communicate.
* Decide the main message first; minimal: no redundant gridlines, borders, legends, 3D, or decoration.
* Color-blind-safe, no red-green contrast; also vary shape or line style where it helps. Gray-print safety is a **publication-mode (PDF) requirement** and applies to other formats only when the user asks. Keep the full Okabe-Ito palette colors (color-blind-safe) and add a **texture channel**, so hue is never the only cue: filled areas (bars, boxes, areas, legend keys) get a hatch or pattern per group; lines get a distinct line style (`LINETYPES` / `lab_linetype`); points get a distinct shape (`SHAPES` / `lab_shape`). Python: `save_fig(..., hatch=True)` (default for `.pdf`) hatches filled groups automatically by fill color (`HATCH` map; matplotlib hatches via `apply_hatch`). R: use ggpattern geoms (`geom_col_pattern`, `geom_boxplot_pattern`, ...) with `tex_scales(levels(d$g))` and map `fill`, `pattern`, `pattern_angle`, `pattern_fill` to the same variable (usage in the template comment). Pattern ink is white on blue and black on every other fill; the black group stays solid. Up to seven groups; more than that, split the figure or use direct labels. Avoid alpha on overlapping colored groups (blending collapses their grays and hides textures). Continuous data: viridis; group order and contrast rules are in `color.md`. `check_pdf.py` runs the grayscale check automatically (for a JPEG add `check_png.py --gray`); its WARN list is advisory (hue-only pairs): view the `_gray_preview.png` and fix every pair that cannot be told apart by texture, line style, shape, or label.
* Label axes directly with units; show individual points over box or bar plots; direct labels over legends.
* Text: 7 pt minimum (tick labels, legends, annotations), 8 pt axis titles; black. No italic or size for emphasis. At most about six panels belong in a full-page figure, and this plugin writes one plot per file, so never merge panels to fit.
* Lines 0.25–1 pt; markers ≥ ~2 pt with thin edges.
* Keep styling, scales, and colors consistent across separate figures of the same project: same group, same color, shape, and order.
* Do not rely on color alone for definition; add direct labels, shape, or line style. Avoid multiple arrow weights or styles unless each means something.

## Text and legibility

* One sans-serif throughout (Arial, Liberation Sans, Helvetica, or DejaVu Sans as a last resort). Check that the font resolves in your library, with no silent fallback.
* 7 pt for tick labels, legends, and annotations; 8 pt for axis titles (Nature house style 8 pt; drafts at least 7 pt). Never below 7. Black type on white. On colored fills, black text, except white on blue. Short labels, few abbreviations (define each in the caption).
* Emphasis by position, bold, or color only. No italic or size changes for emphasis; italic only for gene and species names and variables.
* Label the first instance of every object, and label directly rather than relying on color alone. Axes carry units; a key explains every color and symbol. Keep legends to five entries or fewer.
* Information flows top-left to bottom-right; no circular layouts unless the process is a cycle.
* If the content is a list or categories without a process or measured data, give a table, not a figure.

## Overlap

Avoid first, then keep any remainder readable.

* Avoid: repel or offset labels (`adjustText`, `ggrepel`), leader lines, shorter or rotated labels, smaller markers, jitter or dodge, splitting into separate stand-alone figures, larger plot area.
* Unavoidable: alpha ~0.3–0.6 with thin edges; hexbin/density for dense data; fixed draw order with distinct line styles; text on top with a thin white outline or semi-opaque white box. Text never overlaps text.


## Output formats

* Needs: R with ggplot2, svglite, ggrastr, ragg, ggpattern, or Python with plotnine, matplotlib, Pillow; `pdftoppm` (PDF) and `rsvg-convert` (SVG) for previews. Pick R or Python by context.
* Publication PDF (only on request): vector, TrueType fonts embedded (no Type 3), live text in an Arial-compatible font, opaque white background, gray-print safe through texture. Dense layers (more than about 2000 points, hexbin, tiles, density clouds) are rasterized at 600 dpi inside the PDF; axes, text, and small layers stay vector. R: `rast(geom_point(...))` (ggrastr) written with `cairo_pdf`. plotnine: `save_fig()` rasterizes any collection above `raster_min` (2000). matplotlib or seaborn: call `mpl_style()` once, pass `rasterized=True` to dense artists, save with `save_mpl()`. Never rasterize text, axes, or lines.
* SVG on request: live Arial text, checked with `check_svg.py`, which reads pt sizes directly. PNG on request: 600 dpi, checked with `check_png.py`.
* Fonts: some systems lack Arial (use Liberation Sans or Arimo, which are metric-compatible). In R, the template registers the font by exact path (`FigSans`) because ragg's own family lookup can pick an unrelated file and draw garbled glyphs; always view the render to confirm.
