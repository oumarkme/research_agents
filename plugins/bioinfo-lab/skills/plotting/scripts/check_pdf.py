#!/usr/bin/env python3
"""Spec check for publication PDF figures (vector, grayscale-print friendly), plus a PNG preview for viewing.

Usage: python check_pdf.py figure.pdf [more.pdf ...]
Checks: one page, width <= 88 mm, height <= 247 mm, all fonts embedded and none Type 3, one font family,
file name. Renders <scratch>/<name>_preview.png (pdftoppm, 300 dpi) and runs the grayscale check from
check_png.py on it (view the grayscale preview; every WARN needs shape, line style, or a direct label).
Exit status 1 if any hard check fails.
"""
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image

from check_png import BAD_NAME, gray_check

MAX_W_MM, MAX_H_MM = 88.0, 247.0


def check(path: str) -> bool:
    ok = True
    res = []

    def rep(name, cond, msg):
        nonlocal ok
        ok &= bool(cond)
        res.append(f"  [{'ok' if cond else 'FAIL'}] {name}: {msg}")

    info = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    w_pt, h_pt = map(float, re.search(r"Page size:\s+([\d.]+) x ([\d.]+) pts", info).groups())
    w_mm, h_mm = w_pt / 72 * 25.4, h_pt / 72 * 25.4
    rep("pages", pages == 1, str(pages))
    rep("width", w_mm <= MAX_W_MM + 0.5, f"{w_mm:.1f} mm (limit 88)")
    rep("height", h_mm <= MAX_H_MM, f"{h_mm:.1f} mm (limit 247)")
    fonts = subprocess.run(["pdffonts", path], capture_output=True, text=True).stdout.strip().splitlines()[2:]
    rows = [f.split() for f in fonts]
    emb = [r for r in rows if len(r) >= 5 and "yes" in r[-5:-3]]  # 'emb' column
    types = {" ".join(r[1:3]) if r[1] == "CID" else r[1] for r in rows if len(r) > 1}
    rep("fonts embedded", len(emb) == len(rows), f"{len(emb)}/{len(rows)} embedded")
    rep("no Type 3", not any("Type 3" in f for f in fonts), "; ".join(sorted(types)) or "no text")
    fams = {re.sub(r"^[A-Z]{6}\+", "", r[0]).split("-")[0] for r in rows}
    rep("font family", len(fams) <= 1, ", ".join(sorted(fams)) or "none")
    name = os.path.basename(path)
    rep("file name", not BAD_NAME.match(name), name + " (no figure numbers / ordering prefixes)")
    prev = os.path.join(tempfile.gettempdir(), name.rsplit(".", 1)[0] + "_preview")
    subprocess.run(["pdftoppm", "-r", "300", "-png", "-singlefile", "-f", "1", "-l", "1", path, prev], check=True)
    print(path)
    print("\n".join(res))
    print(f"  preview: {prev}.png (300 dpi; view it with Read, zoom on crowded regions)")
    gray_check(Image.open(prev + ".png").convert("RGB"), prev + ".png")
    return ok


if __name__ == "__main__":
    sys.exit(0 if all([check(p) for p in sys.argv[1:]]) else 1)
