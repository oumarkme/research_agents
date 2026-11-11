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
    if any(a in ("-h", "--help") for a in sys.argv[1:]):
        print(__doc__)
        return 0
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
    try:
        z = zipfile.ZipFile(io.BytesIO(data))
    except zipfile.BadZipFile:
        print(f"Download is not a valid zip archive ({len(data)} bytes); try again later.")
        return 2
    with z:
        for m in z.namelist():  # reject path traversal
            if m.startswith("/") or ".." in Path(m).parts:
                print(f"Unsafe path in archive: {m}")
                return 2
        dest.mkdir(parents=True, exist_ok=True)
        z.extractall(dest)
        # GitHub archives carry the commit ID as the zip comment.
        sha = re.fullmatch(r"[0-9a-f]{40}", z.comment.decode("ascii", "replace").strip())
    roots = [p for p in dest.iterdir() if p.is_dir()]
    if not roots:
        print("Archive has no top-level folder; the template layout changed.")
        return 2
    final = dest / "slide_template"
    roots[0].rename(final)
    try:
        readme = (final / "README.md").read_text(encoding="utf-8")
    except OSError:
        print(f"README.md is missing from the template ({final}); the layout may have changed.")
        return 2
    m = re.search(r"Version\s+(\d+(?:\.\d+)*)", readme)
    print(f"Template version: {m.group(1) if m else 'unknown'}")
    if sha:
        print(f"Template commit: {sha.group(0)}")
    print(f"Folder: {final}")
    print(f"HTML:   {final / 'html' / 'index.html'}")
    print(f"LaTeX:  {final / 'latex' / 'template.tex'} (fonts: bash {final / 'fonts' / 'download.sh'})")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):  # Windows consoles default to a legacy code page
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
