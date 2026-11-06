import shutil
import sys
from pathlib import Path

import pytest

Image = pytest.importorskip("PIL.Image", reason="Pillow not installed")

from conftest import run

SVG = ('<svg xmlns="http://www.w3.org/2000/svg" width="80mm" height="50mm" viewBox="0 0 80 50">'
       '<rect width="80" height="50" fill="#FFFFFF"/><text style="font-size: 7px; font-family: Arial">x</text></svg>')
needs_rsvg = pytest.mark.skipif(not shutil.which("rsvg-convert"), reason="rsvg-convert missing")
needs_poppler = pytest.mark.skipif(not shutil.which("pdftoppm"), reason="poppler missing")


def pngs(d):
    return sorted(p.name for p in Path(d).glob("*.png"))


@needs_rsvg
def test_svg_outdir(tmp_path):
    f = tmp_path / "plot.svg"
    f.write_text(SVG)
    out = tmp_path / "out"
    out.mkdir()
    r = run("plotting/scripts/check_svg.py", f, "--outdir", out)
    assert pngs(out) == ["plot_preview.png"], r.stdout + r.stderr


@needs_rsvg
def test_svg_default_is_fresh_dir_and_printed(tmp_path):
    f = tmp_path / "plot.svg"
    f.write_text(SVG)
    dirs = set()
    for _ in range(2):
        r = run("plotting/scripts/check_svg.py", f)
        line = [l for l in r.stdout.splitlines() if "plot_preview.png" in l]
        assert line, r.stdout + r.stderr
        dirs.add(str(Path(line[0].split("preview:")[-1].split("(")[0].strip()).parent))
    assert len(dirs) == 2


def make_png(path):
    Image.new("RGB", (200, 100), (255, 255, 255)).save(path, dpi=(600, 600))


def test_png_gray_outdir(tmp_path):
    f = tmp_path / "plot.png"
    make_png(f)
    out = tmp_path / "out"
    out.mkdir()
    run("plotting/scripts/check_png.py", "--gray", f, "--outdir", out)
    assert pngs(out) == ["plot_gray_preview.png"]


def make_pdf(path):
    Image.new("RGB", (200, 100), (255, 255, 255)).save(path, "PDF", resolution=72)


@needs_poppler
def test_pdf_outdir(tmp_path):
    f = tmp_path / "plot.pdf"
    make_pdf(f)
    out = tmp_path / "out"
    out.mkdir()
    run("plotting/scripts/check_pdf.py", f, "--outdir", out)
    assert "plot_preview.png" in pngs(out)


def test_pdf_missing_poppler_clear_error(tmp_path):
    f = tmp_path / "plot.pdf"
    make_pdf(f)
    empty = tmp_path / "empty"
    empty.mkdir()
    r = run("plotting/scripts/check_pdf.py", f, env={"PATH": str(empty)})
    assert r.returncode == 2
    assert "pdfinfo" in r.stdout + r.stderr and "poppler" in r.stdout + r.stderr
    assert "Traceback" not in r.stderr
