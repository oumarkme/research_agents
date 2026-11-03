# plotting: color

Palette rules for categorical and continuous data, tuned for color-vision deficiency (CVD), gray print, screens, and projected slides. Numbers below were computed for this plugin with the CIEDE2000 color difference (ΔE) after the Machado et al. (2009) CVD simulation at full severity (deutan, protan, tritan), CIELAB lightness (L*), and Web Content Accessibility Guidelines (WCAG) contrast ratios on white.

## The palette

Eight muted colors (Tol, 2021, "muted" set), no vivid primaries. Chosen for the Nature art guide (few colors, hierarchy, black type, no red-green) and checked for color-vision deficiency (CVD): the smallest CIE76 color difference (dE) between any two of the eight, under normal vision and Machado et al. (2009) deutan, protan, and tritan simulation at full severity, is 17 (above about 10 reads as distinct). Use them in this order and take the first n:

| # | Name | Hex | L* | Contrast on white | Use |
|---|---|---|---|---|---|
| 1 | Indigo | `#332288` | 22 | 12.2 | fill, line, text; the focus color |
| 2 | Rose | `#CC6677` | 56 | 3.7 | fill, line (not text) |
| 3 | Wine | `#882255` | 32 | 8.7 | fill, line, text |
| 4 | Green | `#117733` | 44 | 5.7 | fill, line, text |
| 5 | Cyan | `#88CCEE` | 79 | 1.8 | fill only, dark edge |
| 6 | Olive | `#999933` | 61 | 3.0 | fill only, dark edge |
| 7 | Sand | `#DDCC77` | 82 | 1.6 | fill only, dark edge |
| 8 | Purple | `#AA4499` | 46 | 5.3 | fill, line, text |

* Neutrals are not counted: black `#000000` (reference or control), gray `#BDBDBD` (context fill) and `#757575` (context line).
* Lines and thin marks use only colors with at least 3:1 contrast on white: indigo, rose, wine, green, purple (`PALETTE_LINE`, five at most). Colored text needs 4.5:1: indigo, wine, green, purple. Cyan, olive, and sand are fills with a 0.25-0.5 pt dark edge.
* Rose and wine are close in hue; they are separated by lightness (L* 56 and 32). Keep both on the same figure only with direct labels or texture.
* Lightness spreads from 22 to 82, but several mid colors sit near each other in gray (46 to 61), so print in gray needs the texture channel (see `design.md`).

## Hierarchy and restraint (Nature Reviews art guide)

* The most important element is the most saturated; background and context share one neutral gray (`#BDBDBD` fill, `#757575` line). Example: one cohort in blue against others in gray.
* Use color for hierarchy, categories, or a scientific convention (off-palette is acceptable only for a field convention; flag it in the caption). Random or decorative color is a mistake.
* Same group, same color across all figures of a project.
* Prefer black type; avoid red-green; use a CVD and contrast check (this plugin's checks, or Coblis-type simulators).
* Do not rely on color alone: label directly where possible.

## Categorical data

* Take colors in the table order. One to four groups is typical (Nature: five items per list is optimal); use more only when each is directly labeled or textured. Eight is the maximum; beyond that, split the figure.
* Hierarchy: the focus group gets indigo (`focus_colors()`), everything else gray.
* Black is the reference or control, not a category.
* No red-green pairs, no rainbow cycles, no alpha blending of colored groups.

## Continuous data (Crameri et al., 2020)

Crameri, Shephard, and Heron (2020) show that rainbow-like maps (jet, Turbo, hsv) distort data, because uneven lightness creates false boundaries and hides real gradients by more than 7% of the displayed variation. Red-green maps exclude the roughly 8% of men and 0.5% of women with CVD. Rules that follow:

* Sequential data: viridis (or cividis for the strongest CVD fidelity). Lightness rises monotonically, so it survives gray print. Never jet, rainbow, Turbo, or red-green.
* Diverging data (centered on zero, a reference, or a threshold): `scale_*_lab_div()` (plotnine, ggplot2) or `cmap_diverging()` (matplotlib). It runs a muted blue, light gray, muted red (ColorBrewer RdBu anchors, interpolated in CIELAB); the ends differ by 4 L* and lightness peaks at the gray middle, so it stays readable under CVD. Set symmetric limits (`-m` to `m`) so the gray midpoint is the reference value. 
* Optional upgrade: the Scientific colour maps (Crameri, 2018; `cmcrameri` in Python, `scico` in R) are the reference implementation: `batlow` (sequential), `vik` (diverging), `romaO` (cyclic). The lab default stays viridis plus the muted diverging map; use Crameri maps when a journal or collaborator asks, and say so in the caption.
* Always draw the color bar with ticks and units. A cropped or missing bar makes even a good map unreadable.
* Never stretch, clip, truncate, or edit a map. Do not reverse it without reason, and keep the same map for the same quantity across figures.
* Heatmap tiles that touch alter perceived color; leave a thin white gap or draw a thin outline when cell values matter.
* Do not use a perceptually uniform map for categories, or a categorical palette for ordered values.

## Screens, print, and large canvases

* Paper (PDF): the full palette plus a texture channel (see `design.md`). Run `check_pdf.py` or `check_png.py --gray`.
* Screen and PowerPoint: the 88 mm figure may be enlarged. Keep lines at least 0.75 pt in the figure; thicker lines survive scaling better than small markers.
* Projector or large hall: projectors lift dark tones and wash out light ones. Cyan, olive, and sand are fill-only; prefer indigo, wine, and black for the message.
* Text: black or dark gray `#333333` by default (Nature: primarily black type); colored text (4.5:1 or more) only indigo, wine, green, or purple.
* Text on a colored fill: white on indigo, wine, green, and purple; black on rose, cyan, olive, and sand.
* Dark backgrounds are not part of the lab template. If one is unavoidable, cyan and sand become the strong colors and indigo the weak one; swap roles and re-check.

## Checks

1. View the figure as is, then the gray preview (`check_png.py --gray` or `check_pdf.py`). Fix every flagged pair.
2. For a figure that will be projected, view it at half size and from across the room (or at 25% zoom). Every group must still be separable.
3. For a continuous map, confirm the color bar is present, the range is not clipped, and no rainbow, jet, or red-green map slipped in from a default (matplotlib, ggplot2, and heatmap packages differ).

## References

* Nature Reviews. Guide to designing figures (artwork guide, "Scientific illustration for commissioned content"): hierarchy, visual editing, clarity, accessibility; at least 7 pt text in drafts.
* Crameri, F., Shephard, G. E., & Heron, P. J. (2020). The misuse of colour in science communication. *Nature Communications, 11*, 5444. https://doi.org/10.1038/s41467-020-19160-7
* Crameri, F. (2018). Scientific colour maps. Zenodo. https://doi.org/10.5281/zenodo.1243862
* Tol, P. (2021). Colour schemes (technical note SRON/EPS/TN/09-002, v3.2). https://sronpersonalpages.nl/~pault/
* Okabe, M., & Ito, K. (2008). Color Universal Design (CUD). https://jfly.uni-koeln.de/color/ (the earlier lab palette; its vivid hues were replaced by the muted set above)
* Machado, G. M., Oliveira, M. M., & Fernandes, L. A. F. (2009). A physiologically-based model for simulation of color vision deficiency. *IEEE Transactions on Visualization and Computer Graphics, 15*(6), 1291–1298. https://doi.org/10.1109/TVCG.2009.113
* W3C. (2018). Web Content Accessibility Guidelines (WCAG) 2.1, success criteria 1.4.3 and 1.4.11. https://www.w3.org/TR/WCAG21/
