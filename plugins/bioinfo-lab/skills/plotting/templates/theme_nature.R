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
okabe_pattern     <- c("stripe", "stripe", "stripe", "stripe", "crosshatch", "crosshatch", "circle", "none")
okabe_pattern_ang <- c(45, -45, 0, 90, 45, 0, 0, 0)
okabe_pattern_ink <- c("#000000", "#000000", "#FFFFFF", "#000000", "#FFFFFF", "#FFFFFF", "#000000", "#000000")
okabe_linetype <- c("solid", "dashed", "dotted", "dotdash")
okabe_shape    <- c(16, 17, 15, 18, 25, 3, 4, 8)
okabe_ito <- c("#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000")  # canonical order; the pattern vectors above follow it
# Pick order (see references/color.md): first groups are the best separated under all CVD types and in lightness.
# Fills and large markers: blue, orange, green, vermilion, sky blue, pink, yellow, black.
okabe_fill <- c("#0072B2", "#E69F00", "#009E73", "#D55E00", "#56B4E9", "#CC79A7", "#F0E442", "#000000")
# Lines, thin marks, text: only colors with >= 3:1 contrast on white (max 5 groups; more: split or label directly).
okabe_line <- c("#0072B2", "#D55E00", "#CC79A7", "#009E73", "#000000")
# Diverging data (centered on a meaningful value): Okabe-Ito blue -> light gray -> vermilion, interpolated in CIELAB
# (17 anchors, step dE2000 even to within 0.9 of the exact ramp). Sequential data: viridis. Always draw the color bar.
okabe_div <- c("#0072B2", "#4181BB", "#6191C3", "#7DA1CC", "#97B2D5", "#AFC3DD", "#C8D4E6", "#E0E6EF", "#F7F6F6",
               "#F9E3D8", "#F8D0BA", "#F6BD9D", "#F2AA80", "#EC9764", "#E68447", "#DE7029", "#D55E00")

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

pt_text <- function(pt) pt / ggplot2::.pt                # geom_text(size = pt_text(6))
pt_lw   <- function(pt) pt / (0.75 * ggplot2::.pt)        # ggplot2 linewidth from physical pt (R lwd 1 = 0.75 pt)

theme_nature <- function(base_size = 7) {
  theme_classic(base_size = base_size, base_family = fig_font) %+replace%
    theme(
      text         = element_text(size = base_size, color = "#000000", family = fig_font),
      axis.text    = element_text(size = 6, color = "#333333"),
      axis.title   = element_text(size = 7, color = "#000000"),
      axis.line    = element_line(linewidth = pt_lw(0.5), color = "#000000"),
      axis.ticks   = element_line(linewidth = pt_lw(0.5), color = "#000000"),
      legend.text  = element_text(size = 6), legend.title = element_text(size = 7),
      legend.key.size = unit(3, "mm"),
      plot.background  = element_rect(fill = "white", color = NA),
      panel.background = element_rect(fill = "white", color = NA),
      plot.margin  = margin(2, 2, 2, 2, "mm"),
      complete = TRUE
    )
}

# line = TRUE: thin lines and text-weight marks (5 colors, all >= 3:1 on white); default: points, fills (8 colors).
scale_color_okabe  <- function(line = FALSE, ...) scale_color_manual(values = if (line) okabe_line else okabe_fill, ...)
scale_colour_okabe <- scale_color_okabe
scale_fill_okabe   <- function(...) scale_fill_manual(values = okabe_fill, ...)
# Continuous: scale_*_okabe_div(limits = c(-m, m)) centers 0 for diverging data; sequential: scale_fill_viridis_c().
# Keep the full range, never squeeze or clip the ramp, and keep gaps between heatmap tiles (Crameri et al. 2020).
scale_fill_okabe_div  <- function(...) scale_fill_gradientn(colours = okabe_div, ...)
scale_color_okabe_div <- function(...) scale_color_gradientn(colours = okabe_div, ...)

# Dense layers (thousands of points, hexbin, tiles): wrap the layer, e.g. rast(geom_point(...)).
# In PDF/SVG only that layer becomes a 600 dpi bitmap; axes, text, and other layers stay vector (JPEG is a bitmap anyway).
# Use when a layer has more than ~2000 elements; keep small layers vector.
rast <- function(layer, dpi = fig_dpi) ggrastr::rasterise(layer, dpi = dpi)

# Texture scales for filled groups in publication PDFs. Use with ggpattern geoms and the same variable for all
# four aesthetics, e.g. geom_col_pattern(aes(fill = g, pattern = g, pattern_angle = g, pattern_fill = g),
# pattern_colour = NA, pattern_density = 0.4, pattern_spacing = 0.02, pattern_key_scale_factor = 0.5) + tex_scales(levels(d$g)).
tex_scales <- function(lv) {
  i <- seq_along(lv)
  stopifnot(length(lv) <= 8)
  j <- match(okabe_fill[i], okabe_ito)  # pattern vectors follow the canonical order
  list(scale_fill_manual(values = setNames(okabe_fill[i], lv)),
       ggpattern::scale_pattern_manual(values = setNames(okabe_pattern[j], lv)),
       ggpattern::scale_pattern_angle_manual(values = setNames(okabe_pattern_ang[j], lv)),
       ggpattern::scale_pattern_fill_manual(values = setNames(okabe_pattern_ink[j], lv)))
}

# Exact 88 mm wide figure on opaque white, chosen by file extension:
#   .jpeg default: RGB JPEG, 300 dpi, quality 95 (ragg).
#   .pdf  publication: vector, fonts embedded (cairo_pdf); wrap dense layers in rast(); full Okabe-Ito colors plus
#         texture (tex_scales, okabe_linetype, okabe_shape) so groups survive gray printing.
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
