"""Nature single-column theme, Okabe-Ito palette, and exact-size JPEG (default) / PDF (publication) / SVG writer (plotnine).

Usage:
    import sys, os; sys.path.insert(0, "<skill dir>/templates")  # the plotting skill gives the path as ${CLAUDE_SKILL_DIR}
    from theme_nature import *
plotnine text sizes are pt; line/point `size` units differ from ggplot2, so measure the rendered PNG.
"""
import os
import re

os.environ.setdefault("MPLBACKEND", "Agg")  # headless; avoids Qt and Wayland errors on headless systems
import matplotlib
from matplotlib import font_manager
from plotnine.ggplot import plot_context
from plotnine import element_blank, element_line, element_rect, element_text, scale_color_manual, scale_fill_manual, theme, theme_classic

JPEG_DPI = 300  # default output: JPEG at 300 dpi
DPI = 600  # resolution of rasterized layers in PDF/SVG only (those are vector); pt text sizes unchanged
JPEG_QUALITY = 95
# Publication (PDF) mode keeps the full Okabe-Ito colors (color-blind-safe) and adds a texture channel so groups
# stay distinguishable when printed in gray: filled areas get a hatch (save_fig applies it by fill color),
# lines and points get a distinct line style or shape (set by hand). Hatch ink is black on light fills and white
# on dark fills so it contrasts with the fill in gray.
HATCH = {"#E69F00": "////", "#56B4E9": "\\\\\\\\", "#009E73": "----", "#F0E442": "||||",
         "#0072B2": "xxxx", "#D55E00": "++++", "#CC79A7": "....", "#000000": ""}
HATCH_INK = {"#E69F00": "#000000", "#56B4E9": "#000000", "#009E73": "#FFFFFF", "#F0E442": "#000000",
             "#0072B2": "#FFFFFF", "#D55E00": "#FFFFFF", "#CC79A7": "#000000", "#000000": "#000000"}
LINETYPES = ["solid", "dashed", "dotted", "dashdot"]  # per group, for lines
SHAPES = ["o", "^", "s", "D", "v", "P", "X", "*"]  # per group, for points
OKABE_ITO = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]

_available = {f.name for f in font_manager.fontManager.ttflist}
FIG_FONT = next((f for f in ("Arial", "Liberation Sans", "Arimo", "Helvetica", "DejaVu Sans") if f in _available), "DejaVu Sans")
matplotlib.rcParams["svg.fonttype"] = "none"  # live text; family is rewritten to Arial in save_fig
matplotlib.rcParams["svg.hashsalt"] = "fig"  # reproducible ids
matplotlib.rcParams["hatch.linewidth"] = 0.4  # pt; keeps hatching fine at 88 mm
matplotlib.rcParams["pdf.fonttype"] = 42  # embed TrueType (no Type 3), text stays selectable


def pt_lw(pt: float) -> float:
    """plotnine line `size` from physical points (measured: size 1 renders 1.77 pt at any dpi; physical pt)."""
    return pt / 1.771


def theme_nature(base_size: float = 7):
    return theme_classic(base_size=base_size, base_family=FIG_FONT) + theme(
        text=element_text(size=base_size, color="#000000", family=FIG_FONT),
        axis_text=element_text(size=6, color="#333333"),
        axis_title=element_text(size=7, color="#000000"),
        axis_line=element_line(size=pt_lw(0.5), color="#000000"),
        axis_ticks=element_line(size=pt_lw(0.5), color="#000000"),
        legend_text=element_text(size=6),
        legend_title=element_text(size=7),
        panel_background=element_rect(fill="white"),
        plot_background=element_rect(fill="white", color="white"),
        panel_grid=element_blank(),
    )


def scale_color_okabe(**kw):
    return scale_color_manual(values=OKABE_ITO, **kw)


def scale_fill_okabe(**kw):
    return scale_fill_manual(values=OKABE_ITO, **kw)


def _ext(file: str) -> str:
    ext = os.path.splitext(file)[1].lower()
    assert ext in (".jpg", ".jpeg", ".pdf", ".svg"), "use .jpeg (default), .pdf (publication), or .svg (on request)"
    return ext


def _fix_svg(file: str):
    with open(file, encoding="utf-8") as fh:
        svg = fh.read()
    # Agg skips zero-length paths but SVG viewers draw them as dots with square caps: drop them
    svg = re.sub(r'<path d="M [-\d.e]+ [-\d.e]+ ?\n?"[^>]*/>\n?', "", svg)
    svg = re.sub(r"font-family:\s*'?[^;\"']*'?", "font-family: Arial", svg)
    with open(file, "w", encoding="utf-8") as fh:
        fh.write(svg)


def apply_hatch(fig) -> int:
    """Hatch every filled Okabe-Ito patch/polygon (bars, boxes, areas, legend keys) by its fill color.

    matplotlib hatches a whole collection with one pattern, so a PolyCollection that mixes fill colors
    (plotnine draws all bars of a layer as one) is split into one collection per color first.
    """
    from matplotlib.collections import PolyCollection
    from matplotlib.colors import to_hex
    from matplotlib.patches import Patch

    def style(o, hexc):
        o.set_hatch(HATCH[hexc])
        o.set_edgecolor(HATCH_INK[hexc])
        o.set_linewidth(0.0)

    n = 0
    for o in fig.findobj(lambda o: type(o) is PolyCollection or isinstance(o, Patch)):
        if isinstance(o, Patch):
            fc = o.get_facecolor()
            hexc = to_hex(fc[:3]).upper() if fc[3] > 0 else None
            if hexc in HATCH and HATCH[hexc]:
                style(o, hexc)
                n += 1
            continue
        fcs = o.get_facecolor()
        if len(fcs) == 0:
            continue
        verts = [p.vertices for p in o.get_paths()]
        cols = [to_hex(fcs[i % len(fcs)][:3]).upper() for i in range(len(verts))]
        if not any(c in HATCH and HATCH[c] for c in cols):
            continue
        for c in dict.fromkeys(cols):
            idx = [i for i, x in enumerate(cols) if x == c]
            sub = PolyCollection([verts[i] for i in idx], closed=True, facecolors=c, edgecolors=c, linewidths=0,
                                 transform=o.get_transform(), zorder=o.get_zorder(), clip_on=o.get_clip_on())
            sub.set_clip_path(o.get_clip_path())
            if HATCH.get(c):
                style(sub, c)
                n += 1
            o.axes.add_collection(sub, autolim=False)
        o.remove()
    return n


def save_fig(plot, file: str, height_mm: float = 70, width_mm: float = 88, raster_min: int = 2000,
             hatch: bool = True):
    """Write an exact-size figure on opaque white (no bbox_inches='tight', so size stays exact).

    .jpeg default: RGB JPEG, 300 dpi, quality 95.
    .pdf  publication: vector, TrueType fonts embedded; dense layers (collections with more than `raster_min`
          elements) are rasterized at DPI; full Okabe-Ito colors, with `hatch=True` adding a texture to filled
          groups by fill color (see above); set `linetype`/`shape` per group by hand for lines and points.
    .svg  only on request: vector, live text written as Arial, same rasterization rule as PDF.
    """
    ext = _ext(file)
    assert width_mm <= 88 and height_mm <= 247
    jpg = ext in (".jpg", ".jpeg")
    kw = dict(format="jpeg" if jpg else ext[1:], width=width_mm, height=height_mm, units="mm",
              dpi=JPEG_DPI if jpg else DPI, verbose=False, facecolor="white")
    sv = plot.save_helper(file, **kw)
    n_raster = n_hatch = 0
    if not jpg:
        if hatch and ext == ".pdf":
            n_hatch = apply_hatch(sv.figure)
        for ax in sv.figure.axes:
            for coll in ax.collections:
                if max(len(coll.get_offsets()), len(coll.get_paths())) > raster_min:
                    coll.set_rasterized(True)
                    n_raster += 1
    elif "pil_kwargs" not in sv.kwargs:
        sv.kwargs["pil_kwargs"] = {"quality": JPEG_QUALITY, "dpi": (JPEG_DPI, JPEG_DPI)}
    with plot_context(plot).rc_context:  # same context ggplot.save() uses; keeps legend keys and ticks correct
        sv.figure.savefig(**sv.kwargs)
    if ext == ".svg":
        _fix_svg(file)
    print(f"wrote {file} ({width_mm} x {height_mm} mm, {'JPEG %d dpi' % JPEG_DPI if jpg else ext[1:].upper()}, "
          f"font {FIG_FONT}, {n_raster} rasterized layer(s), {n_hatch} hatched fill(s))")


def mpl_style():
    """matplotlib/seaborn counterpart of theme_nature (6-7 pt Arial-family text, thin black axes, Okabe-Ito cycle).

    Dense layers: pass rasterized=True to scatter/hexbin/pcolormesh/imshow-like calls; save with save_mpl().
    """
    import matplotlib.pyplot as plt
    from cycler import cycler

    plt.rcParams.update({
        "font.family": FIG_FONT, "font.size": 7, "axes.labelsize": 7, "axes.titlesize": 7,
        "xtick.labelsize": 6, "ytick.labelsize": 6, "legend.fontsize": 6, "legend.title_fontsize": 7,
        "text.color": "#000000", "axes.labelcolor": "#000000", "xtick.color": "#000000", "ytick.color": "#000000",
        "axes.edgecolor": "#000000", "axes.linewidth": 0.5, "xtick.major.width": 0.5, "ytick.major.width": 0.5,
        "xtick.major.size": 2.5, "ytick.major.size": 2.5, "lines.linewidth": 0.75,
        "axes.spines.top": False, "axes.spines.right": False, "axes.grid": False, "legend.frameon": False,
        "axes.prop_cycle": cycler(color=OKABE_ITO), "figure.facecolor": "white", "axes.facecolor": "white",
        "svg.fonttype": "none", "savefig.facecolor": "white", "figure.dpi": 100,
    })


def save_mpl(fig, file: str, height_mm: float = 70, width_mm: float = 88):
    """Exact-size .jpeg (default, 300 dpi), .pdf (publication), or .svg (on request) from a matplotlib figure.

    Create it with figsize=(88/25.4, h/25.4) and constrained layout; pass rasterized=True to dense artists
    (affects PDF/SVG only; the JPEG is a bitmap anyway).
    """
    ext = _ext(file)
    assert width_mm <= 88 and height_mm <= 247
    fig.set_size_inches(width_mm / 25.4, height_mm / 25.4)
    if ext in (".jpg", ".jpeg"):
        fig.savefig(file, format="jpeg", dpi=JPEG_DPI, facecolor="white",
                    pil_kwargs={"quality": JPEG_QUALITY, "dpi": (JPEG_DPI, JPEG_DPI)})
    else:
        fig.savefig(file, format=ext[1:], dpi=DPI, facecolor="white")
    if ext == ".svg":
        _fix_svg(file)
    print(f"wrote {file} ({width_mm} x {height_mm} mm, font {FIG_FONT})")
