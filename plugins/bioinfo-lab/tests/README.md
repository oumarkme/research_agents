# Tests

Run from the repository root:

    python -m pytest plugins/bioinfo-lab/tests -q

Requirements: Python 3.10 or newer and `pytest`. Nothing else is needed for the
core tests; they use only the standard library and run the bundled scripts with
`python -I -X utf8`.

Optional (the matching tests are skipped when missing, never failed):

| Package or tool | Needed by | Install |
|---|---|---|
| Pillow | `test_plotting.py`, `check_png.py`, `check_pdf.py` | `pip install pillow` |
| `rsvg-convert` (librsvg) | SVG preview tests | `apt install librsvg2-bin` or `conda install -c conda-forge librsvg` |
| `pdfinfo`, `pdffonts`, `pdftoppm` (poppler) | PDF tests | `apt install poppler-utils` or `conda install -c conda-forge poppler` |
| OpenCC (`opencc`) | optional Simplified-Chinese check in `lint_prose.py` | `pip install opencc-python-reimplemented` |

The tests make no network calls (downloads are mocked) and write only to pytest
temporary folders. CI (`.github/workflows/ci.yml`) installs pytest, Pillow, and
the two system packages on Ubuntu and runs Python 3.10 and 3.13.
