# plotting: detailed rules

## Design

* Decide the main message first; minimal: no redundant gridlines, borders, legends, 3D, or decoration.
* Color-blind-safe, no red-green contrast; also vary shape or line style where it helps. Gray-print safety is a **publication-mode (PDF) requirement** and applies to other formats only when the user asks. Keep the full Okabe-Ito colors (color-blind-safe) and add a **texture channel**, so hue is never the only cue: filled areas (bars, boxes, areas, legend keys) get a hatch or pattern per group; lines get a distinct line style (`LINETYPES` / `okabe_linetype`); points get a distinct shape (`SHAPES` / `okabe_shape`). Python: `save_fig(..., hatch=True)` (default for `.pdf`) hatches filled groups automatically by fill color (`HATCH` map; matplotlib hatches via `apply_hatch`). R: use ggpattern geoms (`geom_col_pattern`, `geom_boxplot_pattern`, ...) with `tex_scales(levels(d$g))` and map `fill`, `pattern`, `pattern_angle`, `pattern_fill` to the same variable (usage in the template comment). Pattern ink is black on light fills and white on dark fills; the black group stays solid. Up to eight groups; more than that, split the figure or use direct labels. Avoid alpha on overlapping colored groups (blending collapses their grays and hides textures). Continuous data: viridis. `check_pdf.py` runs the grayscale check automatically (for a JPEG add `check_png.py --gray`); its WARN list is advisory (hue-only pairs): view the `_gray_preview.png` and fix every pair that cannot be told apart by texture, line style, shape, or label.
* Label axes directly with units; show individual points over box or bar plots; direct labels over legends.
* Lines 0.25–1 pt; markers ≥ ~2 pt with thin edges.
* Keep styling, scales, and colors consistent across separate figures of the same project.

## Overlap

Avoid first, then keep any remainder readable.

* Avoid: repel or offset labels (`adjustText`, `ggrepel`), leader lines, shorter or rotated labels, smaller markers, jitter or dodge, splitting into separate stand-alone figures, larger plot area.
* Unavoidable: alpha ~0.3–0.6 with thin edges; hexbin/density for dense data; fixed draw order with distinct line styles; text on top with a thin white outline or semi-opaque white box. Text never overlaps text.


## Output formats

* Publication PDF (only on request): vector, TrueType fonts embedded (no Type 3), live text in an Arial-compatible font, opaque white background, gray-print safe through texture. Dense layers (more than about 2000 points, hexbin, tiles, density clouds) are rasterized at 600 dpi inside the PDF; axes, text, and small layers stay vector. R: `rast(geom_point(...))` (ggrastr) written with `cairo_pdf`. plotnine: `save_fig()` rasterizes any collection above `raster_min` (2000). matplotlib or seaborn: call `mpl_style()` once, pass `rasterized=True` to dense artists, save with `save_mpl()`. Never rasterize text, axes, or lines.
* SVG on request: live Arial text, checked with `check_svg.py`, which reads pt sizes directly. PNG on request: 600 dpi, checked with `check_png.py`.
* Fonts: some systems lack Arial (use Liberation Sans or Arimo, which are metric-compatible). In R, the template registers the font by exact path (`FigSans`) because ragg's own family lookup can pick an unrelated file and draw garbled glyphs; always view the render to confirm.
