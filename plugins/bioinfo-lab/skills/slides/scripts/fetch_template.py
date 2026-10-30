#!/usr/bin/env python3
"""Download the newest slide template into a fresh folder.

Usage: python fetch_template.py <dest_dir>
Downloads github.com/oumarkme/slide_template (branch main) as a zip, unpacks it
to <dest_dir>/slide_template, and prints the template version and the files to
copy. <dest_dir> must be empty or absent. Exit status: 0 ok, 2 failed.
"""
import io
import re
import sys
import urllib.request
import zipfile
from pathlib import Path

URL = "https://codeload.github.com/oumarkme/slide_template/zip/refs/heads/main"


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    dest = Path(sys.argv[1])
    if dest.exists() and any(dest.iterdir()):
        print(f"{dest} is not empty; pass a new or empty folder.")
        return 2
    try:
        req = urllib.request.Request(URL, headers={"User-Agent": "bioinfo-lab-slides"})
        data = urllib.request.urlopen(req, timeout=30).read()
    except Exception as e:
        print(f"Download failed: {e}")
        return 2
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for m in z.namelist():  # reject path traversal
            if m.startswith("/") or ".." in Path(m).parts:
                print(f"Unsafe path in archive: {m}")
                return 2
        z.extractall(dest)
    root = next(p for p in dest.iterdir() if p.is_dir())
    final = dest / "slide_template"
    root.rename(final)
    readme = (final / "README.md").read_text(encoding="utf-8")
    m = re.search(r"Version\s+(\d+(?:\.\d+)*)", readme)
    print(f"Template version: {m.group(1) if m else 'unknown'}")
    print(f"Folder: {final}")
    print(f"HTML:   {final / 'html' / 'index.html'}")
    print(f"LaTeX:  {final / 'latex' / 'template.tex'} (fonts: bash {final / 'fonts' / 'download.sh'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
