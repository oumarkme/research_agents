#!/usr/bin/env python3
"""Spec check for stand-alone manuscript SVG figures, plus a PNG preview for viewing.

Usage: python check_svg.py figure.svg [more.svg ...]
Checks: width <= 88 mm, height <= 247 mm, white background, text >= 6 pt, one font family (Arial),
colors from Okabe-Ito / grays / viridis-like ramps (vector parts only), file name, rasterized layers.
Writes <scratch>/<name>_preview.png (rsvg-convert, 300 dpi); view it with Read for the legibility check.
Exit status 1 if any hard check fails. Colors inside rasterized layers are not inspected.
"""
import os
import re
import subprocess
import sys
import tempfile

MAX_W_MM, MAX_H_MM, MIN_PT = 88.0, 247.0, 6.0
OKABE_ITO = {"#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"}
BAD_NAME = re.compile(r"^(fig(ure)?[_-]?\d+|\d+[_-])", re.I)
UNIT_MM = {"pt": 25.4 / 72, "px": 25.4 / 96, "mm": 1.0, "cm": 10.0, "in": 25.4, "": 25.4 / 96}


def to_mm(v: str) -> float:
    m = re.fullmatch(r"([\d.]+)\s*([a-z]*)", v.strip())
    return float(m.group(1)) * UNIT_MM[m.group(2)]


def check(path: str) -> bool:
    svg = open(path, encoding="utf-8").read()
    ok = True
    res = []

    def rep(name, cond, msg, hard=True):
        nonlocal ok
        ok &= bool(cond) or not hard
        res.append(f"  [{'ok' if cond else ('FAIL' if hard else 'WARN')}] {name}: {msg}")

    tag = re.search(r"<svg\b[^>]*>", svg).group(0)
    w = to_mm(re.search(r"\swidth=['\"]([^'\"]+)", tag).group(1))
    h = to_mm(re.search(r"\sheight=['\"]([^'\"]+)", tag).group(1))
    rep("width", w <= MAX_W_MM + 0.1, f"{w:.1f} mm (limit {MAX_W_MM:g})")
    rep("height", h <= MAX_H_MM, f"{h:.1f} mm (limit {MAX_H_MM:g})")

    # text size in svg user units: svglite px == pt of the viewBox; matplotlib writes "font-size: 6px" in pt units
    vb = [float(x) for x in re.search(r"viewBox=['\"]([^'\"]+)", tag).group(1).split()]
    scale_pt = w / 25.4 * 72 / vb[2]  # user unit -> pt
    sizes = [float(x) * scale_pt for x in re.findall(r"font-size:\s*([\d.]+)(?:px|pt)?", svg)]
    rep("text size", not sizes or min(sizes) >= MIN_PT - 0.05,
        f"{min(sizes):.2f}-{max(sizes):.2f} pt over {len(sizes)} items" if sizes else "no text")
    fams = set(re.findall(r"font-family:\s*([^;\"']+)", svg))
    rep("font", fams <= {"Arial"}, f"{sorted(fams) or 'none'} (Arial expected)")

    bg = re.search(r"<rect[^>]*(?:fill|fill:)\s*[=:]?\s*['\"]?#?(?:ffffff|FFFFFF)", svg) or re.search(
        r"fill:\s*#FFFFFF", svg, re.I)
    rep("background", bool(bg), "white background rect found" if bg else "no white background rect")

    cols = {c.upper() for c in re.findall(r"(?:fill|stroke)[:=]\s*['\"]?\s*(#[0-9a-fA-F]{6})", svg)}
    grays = {c for c in cols if c[1:3] == c[3:5] == c[5:7]}
    other = sorted(cols - grays - OKABE_ITO)
    rep("colors", True, f"{len(cols & OKABE_ITO)} Okabe-Ito, {len(grays)} gray, {len(other)} other"
        + (f" (viridis/continuous only, else fix): {', '.join(other[:12])}" if other else ""), hard=False)
    if other and len(other) <= 8:
        res[-1] = res[-1].replace("[ok]", "[WARN]")

    n_img = len(re.findall(r"<image\b", svg))
    rep("raster layers", True, f"{n_img} embedded bitmap(s); dense layers should be rasterized, text/axes never"
        if n_img else "none (all vector); rasterize layers with more than ~2000 elements", hard=False)
    n_el = len(re.findall(r"<(?:circle|path|rect|polygon|polyline|line)\b", svg))
    rep("file weight", os.path.getsize(path) < 5e6 and n_el < 20000,
        f"{os.path.getsize(path) / 1e6:.1f} MB, {n_el} vector elements (rasterize dense layers if large)", hard=False)
    name = os.path.basename(path)
    rep("file name", not BAD_NAME.match(name), name + " (no figure numbers / ordering prefixes)")

    prev = os.path.join(tempfile.gettempdir(), name.rsplit(".", 1)[0] + "_preview.png")
    r = subprocess.run(["rsvg-convert", "-d", "300", "-p", "300", "-b", "white", path, "-o", prev], capture_output=True)
    rep("preview", r.returncode == 0, f"{prev} (view it with Read)" if r.returncode == 0 else r.stderr.decode()[:200])
    print(path)
    print("\n".join(res))
    return ok


if __name__ == "__main__":
    sys.exit(0 if all([check(p) for p in sys.argv[1:]]) else 1)
