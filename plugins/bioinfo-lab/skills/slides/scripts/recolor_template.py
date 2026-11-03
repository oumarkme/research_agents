#!/usr/bin/env python3
"""Recolor a fetched slide_template copy from Okabe-Ito to the lab's muted palette (HTML, LaTeX, README text).

Usage: python recolor_template.py <slide_template folder>
Maps by role: blue -> indigo (accent), vermillion -> wine (alerts), green -> green, purple -> purple,
orange -> sand, sky -> cyan, yellow -> olive. Rose is not a template slot; use it as a figure color.
Swatch labels are renamed to match. Safe to run twice. Edits files in place and prints a count per file.
"""
import re
import sys
from pathlib import Path

HEX = {"E69F00": "DDCC77", "56B4E9": "88CCEE", "009E73": "117733", "F0E442": "999933",
       "0072B2": "332288", "D55E00": "882255", "CC79A7": "AA4499"}
NAMES = [("Bluish green", "Green"), ("Reddish purple", "Purple"), ("Sky blue", "Cyan"), ("Vermillion", "Wine"),
         ("vermillion", "wine"), ("Orange", "Sand"), ("Yellow", "Olive"), (">Blue<", ">Indigo<"),
         ("{Blue}", "{Indigo}"), ("Okabe-Ito (Okabe & Ito, 2008)", "Muted palette (Tol, 2021)"),
         ("Okabe-Ito blue", "indigo"), ("Okabe-Ito", "muted")]


def recolor(text: str) -> str:
    for old, new in HEX.items():
        text = re.sub(old, new, text, flags=re.I)
    for old, new in NAMES:
        text = text.replace(old, new)
    return text


def main() -> int:
    if len(sys.argv) != 2 or not Path(sys.argv[1]).is_dir():
        print(__doc__)
        return 2
    root = Path(sys.argv[1])
    for p in sorted(root.rglob("*")):
        if p.suffix.lower() in (".html", ".tex", ".md", ".css") and ".git" not in p.parts:
            old = p.read_text(encoding="utf-8")
            new = recolor(old)
            if new != old:
                p.write_text(new, encoding="utf-8")
                print(f"recolored {p.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
