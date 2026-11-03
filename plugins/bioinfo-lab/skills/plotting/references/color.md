# plotting: color

Palette rules for categorical and continuous data, tuned for color-vision deficiency (CVD), gray print, screens, and projected slides. Numbers below were computed for this plugin with the CIEDE2000 color difference (ΔE) after the Machado et al. (2009) CVD simulation at full severity (deutan, protan, tritan), CIELAB lightness (L*), and Web Content Accessibility Guidelines (WCAG) contrast ratios on white.

## Why the palette needed rules

Okabe-Ito (Okabe & Ito, 2008) is CVD-safe in hue, and it stays the only categorical palette. Its weak points are lightness and contrast, which hue-based safety does not cover:

| Color | Hex | L* | Contrast on white | Contrast on black |
|---|---|---|---|---|
| Blue | `#0072B2` | 46 | 5.2 | 4.0 |
| Vermilion | `#D55E00` | 54 | 3.9 | 5.4 |
| Green | `#009E73` | 58 | 3.4 | 6.1 |
| Pink | `#CC79A7` | 61 | 3.1 | 6.9 |
| Sky blue | `#56B4E9` | 70 | 2.3 | 9.1 |
| Orange | `#E69F00` | 71 | 2.3 | 9.3 |
| Yellow | `#F0E442` | 89 | 1.3 | 15.9 |
| Black | `#000000` | 0 | 21.0 | 1.0 |

* Orange and sky blue differ by 0.8 L*, so they print as the same gray. The canonical order (orange, sky blue, green, ...) put exactly this pair first.
* Four of eight colors fall under 3:1 on white (WCAG 1.4.11 minimum for graphics). Thin lines and small text in sky blue, orange, or yellow disappear on a projector.
* Across the eight colors, the smallest CVD ΔE is 10.9, so hue is safe; lightness is the problem.

## Categorical data

* Use the pick order, not the canonical order. The first groups are the best separated under every CVD type and in lightness. Smallest pairwise ΔE and L* gap: n = 2, 51 and 25; n = 3, 12 and 12; n = 4, 12 and 4.
  * Fills, bars, areas, large markers (`OKABE_FILL` / `okabe_fill`): blue, orange, green, vermilion, sky blue, pink, yellow, black.
  * Thin lines, small marks, colored text (`OKABE_LINE` / `okabe_line`): blue, vermilion, pink, green, black. Only these have at least 3:1 contrast on white. Five groups is the limit; beyond that, split the figure or label directly.
* Light colors (orange, sky blue, yellow) are fill-only and need a dark edge (0.25–0.5 pt, `#000000` or `#333333`) on white.
* Black is for reference or control (the baseline, the null), not a category, unless every other color is taken.
* From the fifth group on, lightness gaps drop below 1 L*. Add a second channel (hatch, line style, shape) or label the groups directly. Beyond five groups, direct labels beat a legend.
* No red-green pairs, no rainbow cycles, no alpha blending of colored groups.

## Continuous data (Crameri et al., 2020)

Crameri, Shephard, and Heron (2020) show that rainbow-like maps (jet, Turbo, hsv) distort data, because uneven lightness creates false boundaries and hides real gradients by more than 7% of the displayed variation. Red-green maps exclude the roughly 8% of men and 0.5% of women with CVD. Rules that follow:

* Sequential data: viridis (or cividis for the strongest CVD fidelity). Lightness rises monotonically, so it survives gray print. Never jet, rainbow, Turbo, or red-green.
* Diverging data (centered on zero, a reference, or a threshold): `scale_*_okabe_div()` (plotnine, ggplot2) or `cmap_diverging()` (matplotlib). It runs Okabe-Ito blue, light gray, vermilion, interpolated in CIELAB; step ΔE has a coefficient of variation of 0.18 (viridis: 0.15), and end-to-end ΔE is at least 50 under all CVD types. Set symmetric limits (`-m` to `m`) so the gray midpoint is the reference value. The two ends differ by 8 L*, which is small enough to read as balanced.
* Optional upgrade: the Scientific colour maps (Crameri, 2018; `cmcrameri` in Python, `scico` in R) are the reference implementation: `batlow` (sequential), `vik` (diverging), `romaO` (cyclic). The lab default stays viridis plus the Okabe-Ito diverging map; use Crameri maps when a journal or collaborator asks, and say so in the caption.
* Always draw the color bar with ticks and units. A cropped or missing bar makes even a good map unreadable.
* Never stretch, clip, truncate, or edit a map. Do not reverse it without reason, and keep the same map for the same quantity across figures.
* Heatmap tiles that touch alter perceived color; leave a thin white gap or draw a thin outline when cell values matter.
* Do not use a perceptually uniform map for categories, or a categorical palette for ordered values.

## Screens, print, and large canvases

* Paper (PDF): full Okabe-Ito plus a texture channel (see `design.md`). Run `check_pdf.py` or `check_png.py --gray`.
* Screen and PowerPoint: the 88 mm figure may be enlarged. Keep lines at least 0.75 pt in the figure; thicker lines survive scaling better than small markers.
* Projector or large hall: projectors lift dark tones and wash out light ones. Treat any color under 3:1 on white as fill-only, and prefer blue, vermilion, and black for the message.
* Text contrast: at least 4.5:1 for body text (black, dark gray `#333333`, or blue `#0072B2` on white), at least 3:1 for text of 24 pt or larger (adds vermilion, green, pink). Never put text in orange, sky blue, or yellow on white.
* Text on a colored fill: black on orange, sky blue, yellow, green, and pink; white on blue and vermilion. Check 4.5:1 with the numbers above (white on blue is 5.2:1, white on vermilion is 3.9:1, so vermilion needs bold or 24 pt text).
* Dark backgrounds are not part of the lab template. If one is unavoidable, sky blue, orange, and yellow become the strong colors and blue (4.0:1 on black) becomes the weak one; swap roles accordingly and re-check.

## Checks

1. View the figure as is, then the gray preview (`check_png.py --gray` or `check_pdf.py`). Fix every flagged pair.
2. For a figure that will be projected, view it at half size and from across the room (or at 25% zoom). Every group must still be separable.
3. For a continuous map, confirm the color bar is present, the range is not clipped, and no rainbow, jet, or red-green map slipped in from a default (matplotlib, ggplot2, and heatmap packages differ).

## References

* Crameri, F., Shephard, G. E., & Heron, P. J. (2020). The misuse of colour in science communication. *Nature Communications, 11*, 5444. https://doi.org/10.1038/s41467-020-19160-7
* Crameri, F. (2018). Scientific colour maps. Zenodo. https://doi.org/10.5281/zenodo.1243862
* Okabe, M., & Ito, K. (2008). Color Universal Design (CUD): How to make figures and presentations that are friendly to colorblind people. https://jfly.uni-koeln.de/color/
* Machado, G. M., Oliveira, M. M., & Fernandes, L. A. F. (2009). A physiologically-based model for simulation of color vision deficiency. *IEEE Transactions on Visualization and Computer Graphics, 15*(6), 1291–1298. https://doi.org/10.1109/TVCG.2009.113
* W3C. (2018). Web Content Accessibility Guidelines (WCAG) 2.1, success criteria 1.4.3 and 1.4.11. https://www.w3.org/TR/WCAG21/
