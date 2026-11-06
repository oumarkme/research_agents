#!/usr/bin/env python3
"""Spec check for stand-alone raster figures (default .jpeg at 300 dpi; .png at 600 dpi): size, mode, dpi, background, tight crop, grayscale.

Usage: python check_png.py [--gray] [--outdir DIR] figure.jpeg [more.jpeg ...]
--gray (always for publication PDF previews; otherwise only when the user asks for grayscale-safe figures) adds a grayscale-separability warning and preview.
--outdir DIR sets the preview folder (default: a fresh temporary folder, printed).
Exit status 1 if any hard check fails. Text size cannot be inferred from pixels:
measure a known element (px = pt / 72 * 600) and still do the visual legibility check.
"""
from __future__ import annotations

import argparse
import itertools
import os
import re
import sys
import tempfile

try:
    from PIL import Image, ImageChops
except ImportError:
    sys.exit("error: Pillow is required (pip install pillow or conda install pillow).")

MAX_H_MM = 247
MIN_GRAY_GAP = 40  # of 255; colored groups closer than this merge when printed in grayscale
BAD_NAME = re.compile(r"^(fig(ure)?[_-]?\d+|\d+[_-])", re.I)


def check(path: str, gray: bool = False, outdir: str | None = None) -> bool:
    im = Image.open(path)
    DPI = 300 if path.lower().endswith((".jpg", ".jpeg")) else 600  # JPEG default 300 dpi; PNG/PDF previews 600
    MAX_W_PX = round(88 / 25.4 * DPI)
    ok = True
    w, h = im.size
    dpi = tuple(round(d) for d in im.info.get("dpi", (0, 0)))
    res = []

    def rep(name, cond, msg):
        nonlocal ok
        ok &= bool(cond)
        res.append(f"  [{'ok' if cond else 'FAIL'}] {name}: {msg}")

    rep("mode", im.mode == "RGB", im.mode + (" (convert to RGB, no alpha)" if im.mode != "RGB" else ""))
    rep("width", w <= MAX_W_PX, f"{w} px = {w / DPI * 25.4:.1f} mm (limit {MAX_W_PX} px / 88 mm; previews at other dpi: judge by mm)")
    rep("height", h / DPI * 25.4 <= MAX_H_MM, f"{h} px = {h / DPI * 25.4:.1f} mm (limit {MAX_H_MM} mm)")
    rep("dpi", dpi in {(DPI, DPI), (0, 0)} or path.lower().endswith(".pdf"), f"{dpi} (0,0 = unset; {DPI} expected)")
    rgb = im.convert("RGB")
    corners = {rgb.getpixel(p) for p in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]}
    rep("background", corners == {(255, 255, 255)}, f"corner pixels {sorted(corners)}")
    bbox = ImageChops.difference(rgb, Image.new("RGB", im.size, (255, 255, 255))).getbbox()
    if bbox:
        m = (bbox[0], bbox[1], w - bbox[2], h - bbox[3])
        rep("tight crop", max(m) <= DPI // 5, f"white margins L/T/R/B = {m} px (≤ {DPI // 5} px ≈ 5 mm expected)")
    else:
        rep("content", False, "image is blank")
    name = os.path.basename(path)
    rep("file name", not BAD_NAME.match(name), name + " (no figure numbers / ordering prefixes)")
    print(path)
    print("\n".join(res))
    if gray:
        gray_check(rgb, path, outdir)
    return ok


def gray_check(rgb, path, outdir=None):
    """Warn when saturated colors in the figure map to near-identical grays; write a grayscale preview.

    Advisory only: groups that also differ by shape, line style, or label are fine. View the preview.
    """
    px = rgb.get_flattened_data() if hasattr(rgb, "get_flattened_data") else rgb.getdata()
    counts = {}
    for r, g, b in px:
        if max(r, g, b) - min(r, g, b) >= 60:  # saturated; skips black, white, grays, most anti-aliasing
            k = (r // 16 * 16 + 8, g // 16 * 16 + 8, b // 16 * 16 + 8)
            counts[k] = counts.get(k, 0) + 1
    total = sum(counts.values())
    main = [c for c, n in counts.items() if n >= 0.02 * total] if total else []
    lum = lambda c: round(0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2])
    # merge quantization bins that are the same hue family (within 48 in every channel)
    reps = []
    for c in sorted(main, key=lambda c: -counts[c]):
        if all(max(abs(a - b) for a, b in zip(c, r)) > 48 for r in reps):
            reps.append(c)
    close = [(a, b) for a, b in itertools.combinations(reps, 2) if abs(lum(a) - lum(b)) < MIN_GRAY_GAP]
    outdir = outdir or tempfile.mkdtemp(prefix="figcheck_")
    os.makedirs(outdir, exist_ok=True)
    prev = os.path.join(outdir, os.path.basename(path).rsplit(".", 1)[0] + "_gray_preview.png")
    rgb.convert("L").save(prev)
    tag = "WARN" if close else "ok"
    msg = f"{len(reps)} main colors; grayscale preview {prev} (view it)"
    if close:
        msg += "; near-identical grays (need shape/line style/label as second channel, or recolor): " + ", ".join(
            "#%02X%02X%02X~#%02X%02X%02X" % (*a, *b) for a, b in close)
    print(f"  [{tag}] grayscale: {msg}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Spec check for raster figures.")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--gray", action="store_true")
    ap.add_argument("--outdir", help="folder for the grayscale preview (default: new temporary folder)")
    args = ap.parse_args(argv)
    outdir = args.outdir or (tempfile.mkdtemp(prefix="figcheck_") if args.gray else None)
    if outdir:
        print(f"preview folder: {outdir}")
    results = []
    for p in args.files:
        try:
            results.append(check(p, args.gray, outdir))
        except OSError as e:  # missing file or not an image (PIL's error subclasses OSError)
            print(f"error: cannot read {p} as an image ({e})")
            return 2
    return 0 if all(results) else 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):  # Windows consoles default to a legacy code page
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
