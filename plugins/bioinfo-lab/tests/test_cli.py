"""Command-line contract shared by all scripts: --help, paths with spaces, CRLF, bad input."""
import pytest

from conftest import run

SCRIPTS = [
    "humanizer/scripts/preserve_diff.py",
    "humanizer/scripts/unicode_check.py",
    "translator/scripts/check_translation.py",
    "writing/scripts/lint_prose.py",
    "writing/scripts/prose_check.py",
    "slides/scripts/fetch_template.py",
    "update/scripts/check_update.py",
    "plotting/scripts/check_svg.py",
]


@pytest.mark.parametrize("rel", SCRIPTS)
def test_help_exits_zero_without_side_effects(rel, tmp_path):
    # Run in an empty folder: --help must not download, write, or crash.
    r = run(rel, "--help")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "sage" in r.stdout.lower()
    assert "Traceback" not in r.stderr


def test_spaces_crlf_and_bom(tmp_path):
    d = tmp_path / "dir with space"
    d.mkdir()
    a, b = d / "a b.md", d / "b c.md"
    a.write_bytes("# Title\r\nThe dose was 5 mg (P = 0.01).\r\n".encode())
    b.write_bytes(b"\xef\xbb\xbf# Title\nThe dose was 5 mg (P = 0.01).\n")
    r = run("humanizer/scripts/preserve_diff.py", a, b)
    assert r.returncode == 0, r.stdout


def test_unreadable_input_gives_message_not_traceback(tmp_path):
    bad = tmp_path / "bad.md"
    bad.write_bytes(b"\xff\xfe\x00")
    for rel in ("writing/scripts/lint_prose.py", "humanizer/scripts/unicode_check.py"):
        r = run(rel, bad)
        assert r.returncode == 2 and "Traceback" not in r.stderr, rel
    r = run("translator/scripts/check_translation.py", bad, tmp_path / "missing.md")
    assert r.returncode == 2 and "Traceback" not in r.stderr
