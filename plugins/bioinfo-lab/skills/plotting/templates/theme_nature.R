# Nature single-column theme, Okabe-Ito palette, and exact-size JPEG (default) / PDF (publication) / SVG writer (ggplot2 + ragg + svglite + ggrastr).
# Usage: source("<skill dir>/templates/theme_nature.R")  # the plotting skill gives the path as ${CLAUDE_SKILL_DIR}
# Units: text sizes in pt (theme); geom text/line sizes in ggplot2 are mm -> use pt_text() and pt_lw().
suppressPackageStartupMessages({ library(ggplot2); library(svglite); library(ggrastr); library(ragg) })
suppressPackageStartupMessages(library(ggpattern))

jpeg_dpi <- 300  # default output: JPEG at 300 dpi
fig_dpi <- 600   # resolution of rasterized layers in PDF/SVG only (those are vector); pt text sizes unchanged
# Publication (PDF) mode keeps the full Okabe-Ito colors (color-blind-safe) and adds a texture channel so groups
# stay distinguishable when printed in gray: filled areas get a pattern (tex_scales()), lines and points get a
# distinct linetype or shape (set by hand). Pattern ink is black on light fills and white on dark fills.
lab_linetype <- c("solid", "dashed", "dotted", "dotdash")
lab_shape    <- c(16, 17, 15, 18, 25, 3, 4, 8)
# Okabe-Ito palette (Okabe & Ito, 2008), color-vision-deficiency safe. Order of use (take the first n): blue, vermillion,
# bluish green, orange, sky blue, reddish purple, yellow. Contrast on white: blue 5.2, vermillion 3.9, bluish green 3.4,
# reddish purple 3.1, orange 2.3, sky blue 2.3, yellow 1.3. Orange, sky blue, and yellow are fill only, with a dark edge.
lab_fill <- c("#0072B2", "#D55E00", "#009E73", "#E69F00", "#56B4E9", "#CC79A7", "#F0E442")
lab_names <- c("blue", "vermillion", "bluish green", "orange", "sky blue", "reddish purple", "yellow")
lab_line <- c("#0072B2", "#D55E00", "#009E73", "#CC79A7")  # >= 3:1 on white: lines and thin marks
lab_black <- "#000000"  # reference or control, not a category
# Hierarchy: context in neutral gray, the focus group in the first palette color (blue). Gray is fill/marker only.
neutral <- "#BDBDBD"; neutral_line <- "#757575"
focus_colors <- function(levels, focus) {  # scale_*_manual(values = focus_colors(levels(d$g), "case"))
  v <- setNames(rep(neutral, length(levels)), levels); v[focus] <- lab_fill[seq_along(focus)]; v
}
# Texture per palette color (gray-print channel): pattern, angle, ink (white on blue only)
lab_pattern     <- c("crosshatch", "stripe", "crosshatch", "stripe", "stripe", "circle", "circle")
lab_pattern_ang <- c(45, 45, 0, 0, -45, 45, 0)
lab_pattern_ink <- c("#FFFFFF", "#000000", "#000000", "#000000", "#000000", "#000000", "#000000")
# Continuous data: viridis only (scale_fill_viridis_c). Always draw the color bar.

# Resolve the font by exact family from system_fonts() and register it under a fixed name.
# (systemfonts::match_fonts() and ragg's family lookup can silently return an unrelated file,
# e.g. a woff display font, which renders as garbled glyphs.)
.fig_family <- NA_character_
.register_fig_font <- function(prefs = c("Arial", "Liberation Sans", "Arimo", "Helvetica", "DejaVu Sans")) {
  f <- systemfonts::system_fonts()
  f <- f[!grepl("\\.woff2?$", f$path), ]
  for (fam in prefs) {
    g <- f[f$family == fam, ]
    pick <- function(style) { x <- g$path[g$style == style]; if (length(x)) x[1] else NA_character_ }
    reg <- pick("Regular")
    if (!is.na(reg)) {
      or_reg <- function(x) if (is.na(x)) reg else x
      systemfonts::register_font("FigSans", plain = reg, bold = or_reg(pick("Bold")),
                                 italic = or_reg(pick("Italic")), bolditalic = or_reg(pick("Bold Italic")))
      .fig_family <<- fam  # real family name, needed by cairo_pdf
      message("figure font: ", fam, " (", reg, ")")
      return("FigSans")
    }
  }
  stop("No Arial-compatible sans-serif font found; install Liberation Sans or Arimo.")
}
fig_font <- .register_fig_font()

pt_text <- function(pt) pt / ggplot2::.pt                # geom_text(size = pt_text(7))
pt_lw   <- function(pt) pt / (0.75 * ggplot2::.pt)        # ggplot2 linewidth from physical pt (R lwd 1 = 0.75 pt)

theme_nature <- function(base_size = 7) {
  theme_classic(base_size = base_size, base_family = fig_font) %+replace%
    theme(
      text         = element_text(size = base_size, color = "#000000", family = fig_font),
      axis.text    = element_text(size = 7, color = "#000000"),
      axis.title   = element_text(size = 8, color = "#000000"),
      axis.line    = element_line(linewidth = pt_lw(0.5), color = "#000000"),
      axis.ticks   = element_line(linewidth = pt_lw(0.5), color = "#000000"),
      legend.text  = element_text(size = 7), legend.title = element_text(size = 8),
      legend.key.size = unit(3, "mm"),
      plot.background  = element_rect(fill = "white", color = NA),
      panel.background = element_rect(fill = "white", color = NA),
      plot.margin  = margin(2, 2, 2, 2, "mm"),
      complete = TRUE
    )
}

# line = TRUE: thin lines and text-weight marks (4 colors, all >= 3:1 on white); default: points, fills (7 colors).
scale_color_lab  <- function(line = FALSE, ...) scale_color_manual(values = if (line) lab_line else lab_fill, ...)
scale_colour_lab <- scale_color_lab
scale_fill_lab   <- function(...) scale_fill_manual(values = lab_fill, ...)
# Continuous: scale_fill_viridis_c() / scale_color_viridis_c(). Keep the full range, never squeeze or clip the ramp,
# and keep gaps between heatmap tiles (Crameri et al. 2020).

# Dense layers (thousands of points, hexbin, tiles): wrap the layer, e.g. rast(geom_point(...)).
# In PDF/SVG only that layer becomes a 600 dpi bitmap; axes, text, and other layers stay vector (JPEG is a bitmap anyway).
# Use when a layer has more than ~2000 elements; keep small layers vector.
rast <- function(layer, dpi = fig_dpi) ggrastr::rasterise(layer, dpi = dpi)

# Texture scales for filled groups in publication PDFs. Use with ggpattern geoms and the same variable for all
# four aesthetics, e.g. geom_col_pattern(aes(fill = g, pattern = g, pattern_angle = g, pattern_fill = g),
# pattern_colour = NA, pattern_density = 0.4, pattern_spacing = 0.02, pattern_key_scale_factor = 0.5) + tex_scales(levels(d$g)).
tex_scales <- function(lv) {
  i <- seq_along(lv)
  stopifnot(length(lv) <= 7)
  j <- match(lab_fill[i], lab_fill)  # pattern vectors follow the palette order
  list(scale_fill_manual(values = setNames(lab_fill[i], lv)),
       ggpattern::scale_pattern_manual(values = setNames(lab_pattern[j], lv)),
       ggpattern::scale_pattern_angle_manual(values = setNames(lab_pattern_ang[j], lv)),
       ggpattern::scale_pattern_fill_manual(values = setNames(lab_pattern_ink[j], lv)))
}

# Exact 88 mm wide figure on opaque white, chosen by file extension:
#   .jpeg default: RGB JPEG, 300 dpi, quality 95 (ragg).
#   .pdf  publication: vector, fonts embedded (cairo_pdf); wrap dense layers in rast(); full Okabe-Ito colors plus
#         texture (tex_scales, lab_linetype, lab_shape) so groups survive gray printing.
#   .svg  only on request: live text, font name written as Arial (metric-compatible with Liberation Sans/Arimo).
save_fig <- function(plot, file, height_mm = 70, width_mm = 88) {
  stopifnot(width_mm <= 88, height_mm <= 247, grepl("\\.(jpe?g|pdf|svg)$", file, ignore.case = TRUE))
  if (grepl("\\.jpe?g$", file, ignore.case = TRUE)) {
    ragg::agg_jpeg(file, width = width_mm, height = height_mm, units = "mm", res = jpeg_dpi, quality = 95, background = "white")
  } else if (grepl("\\.pdf$", file, ignore.case = TRUE)) {
    # cairo_pdf resolves families through fontconfig, which does not know the registered "FigSans" alias
    plot <- plot + theme(text = element_text(family = .fig_family))
    grDevices::cairo_pdf(file, width = width_mm / 25.4, height = height_mm / 25.4, family = .fig_family, bg = "white")
  } else {
    svglite::svglite(file, width = width_mm / 25.4, height = height_mm / 25.4, bg = "white")
  }
  print(plot); invisible(dev.off())
  if (grepl("\\.svg$", file, ignore.case = TRUE)) {
    x <- readLines(file, warn = FALSE)
    x <- gsub('font-family: "[^"]*"', "font-family: Arial", x)
    writeLines(x, file)
  }
  message("wrote ", file, " (", width_mm, " x ", height_mm, " mm, font ", fig_font, ")")
}
