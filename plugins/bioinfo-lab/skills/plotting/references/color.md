# plotting: color

Rules for figures, tables, diagrams, slides, and posters. Categories use the Okabe-Ito palette, continuous data use viridis, and the background is white. Contrast ratios are WCAG 2.1 values against white.

## Palette (Okabe & Ito, 2008)

The palette was built to stay distinguishable under the common forms of color vision deficiency (CVD). Take colors in this order, first n:

| # | Name | Hex | Contrast on white | Use |
|---|---|---|---|---|
| 1 | Blue | `#0072B2` | 5.2 | fill, line, text; focus color and slide accent |
| 2 | Vermillion | `#D55E00` | 3.9 | fill, line; second color for contrast or alerts; text only if large and bold |
| 3 | Bluish green | `#009E73` | 3.4 | fill, line; text only if large and bold |
| 4 | Orange | `#E69F00` | 2.3 | fill with a dark edge |
| 5 | Sky blue | `#56B4E9` | 2.3 | fill with a dark edge |
| 6 | Reddish purple | `#CC79A7` | 3.1 | fill, line |
| 7 | Yellow | `#F0E442` | 1.3 | fill with a dark edge; not used on slides |

* Black `#000000` marks the reference or control and is not a category. Gray: `#333333` for text, `#757575` (4.6:1) for context lines, `#BDBDBD` (1.9:1) for context fills only.
* Lines and thin marks need at least 3:1: blue, vermillion, bluish green, reddish purple (`PALETTE_LINE`). Colored text needs 4.5:1, which only blue reaches. Vermillion and bluish green pass the 3:1 large-text threshold, so they are allowed for bold text of 24 pt or more.
* Orange, sky blue, and yellow have a luminance too high for lines or text. Use them as fills with a 0.25 to 0.5 pt dark edge.
* Text on a colored fill is white on blue and black on all other colors.
* Do not use vermillion and bluish green as the only cue for two opposite meanings. Add a label, a shape, or a line style.

* Template objects: `PALETTE` / `lab_fill` (fills), `PALETTE_LINE` / `lab_line` (lines and thin marks), `focus_colors()`, `scale_color_lab(line=True)`, `scale_fill_lab()`.
* Gray: `#BDBDBD` fills, `#757575` lines. Use a field convention color (for example a disease or tissue color) only when one exists, and state it in the caption.

## When to use color

* Use color only where it makes the information clearer. Everything else stays black and gray. One accent color on gray context is the default. Add a second color when the comparison needs it, and a third only when there is a third group.
* The focus group is blue (`focus_colors()`) and the other groups are gray.
* Color encodes a group, an ordered value, or a field convention (for example a disease or tissue color). A convention outside the palette is allowed and is stated in the caption.
* A group keeps its color in every figure and slide of the project.
* Black type, with direct labels in addition to color. No transparency on overlapping colored groups.
* Four colored groups at once is typical. Seven is the limit and needs direct labels or texture. With more groups, split the figure.

## Continuous data (Crameri et al., 2020)

Rainbow colormaps (jet, Turbo, hsv) have uneven luminance, which creates false boundaries in the data, and red-green colormaps are unreadable with CVD.

* Use viridis for every continuous scale, including data centered on a value: `scale_*_viridis_c()` in ggplot2, `scale_*_cmap("viridis")` in plotnine, `cmap="viridis"` in matplotlib. Its luminance increases monotonically, so it is also readable in grayscale.
* For data centered on a value (log fold change, z-score, residual), set symmetric limits (`-m` to `m`) and mark the center on the colorbar. Viridis has no neutral midpoint.
* Always draw the colorbar with ticks and units. Do not clip, stretch, or truncate the colormap, and use the same colormap for the same quantity in every figure.
* Leave a thin white gap between heatmap tiles when cell values matter, because touching tiles shift the perceived color.
* Do not use viridis for categories or the categorical palette for ordered values.

## Slides and posters

The background is white. Choose colors by their contrast on white, because projectors lift dark tones and wash out light ones.

* Text, axes, and context are black, `#333333`, or gray. Color goes on the compared groups, the highlighted result, or an alert. If a slide reads the same in black and gray, leave it that way.
* Blue is the accent for emphasis, links, and the focus group. Vermillion is the second color, for contrast or an alert. Bluish green and reddish purple are for a third and fourth group, as fills or thick lines.
* Orange, sky blue, and yellow appear only as large fills with a dark edge. Never use them for text, thin lines, or small markers.
* Titles and body text are black or `#333333`. Colored text is blue, or bold vermillion at 24 pt or more.
* No colored backgrounds, gradients, or title bars.
* Posters follow the same rules. Viewers read from 1 to 2 m, so figure lines are at least 1.5 pt and groups carry direct labels.

## Screens and print

* PDF for journals: Okabe-Ito colors plus a texture channel (`design.md`). Run `check_pdf.py` or `check_png.py --gray`.
* PowerPoint: the 88 mm figure can be enlarged. Keep lines at 0.75 pt or more in the figure, and prefer thick lines to small markers.
* Dark backgrounds are not part of this design.

## Checks

1. View the figure, then the grayscale preview (`check_png.py --gray` or `check_pdf.py`). Fix each flagged pair.
2. For a projected figure, view it at half size or 25% zoom. Every group must still be separable.
3. For a continuous map, confirm the colorbar is present, the range is not clipped, and no rainbow, jet, or red-green default slipped in (matplotlib, ggplot2, and heatmap packages differ).
4. For a slide, take each colored element and ask what is lost when it turns black or gray. If nothing is lost, remove the color.

## References

* Okabe, M., & Ito, K. (2008). Color Universal Design (CUD). https://jfly.uni-koeln.de/color/
* Crameri, F., Shephard, G. E., & Heron, P. J. (2020). The misuse of colour in science communication. *Nature Communications, 11*, 5444. https://doi.org/10.1038/s41467-020-19160-7
* Nature Reviews. Guide to designing figures (artwork guide).
* Garnier, S., Ross, N., Rudis, R., Camargo, A. P., Sciaini, M., & Scherer, C. viridis: Colorblind-friendly color maps for R. https://sjmgarnier.github.io/viridis/
* World Wide Web Consortium. (2018). Web Content Accessibility Guidelines (WCAG) 2.1, success criteria 1.4.3 and 1.4.11. https://www.w3.org/TR/WCAG21/
