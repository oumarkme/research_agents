from conftest import run

PC = "writing/scripts/prose_check.py"


def test_clean_edit_passes(write):
    a = write("a.md", "We sequenced 12 samples at 30x depth.\n")
    b = write("b.md", "We sequenced 12 samples at 30x depth.\n")
    r = run(PC, a, b)
    assert r.returncode == 0, r.stdout
    assert "FAIL" not in r.stdout


def test_changed_number_fails(write):
    a = write("a.md", "We sequenced 12 samples.\n")
    b = write("b.md", "We sequenced 13 samples.\n")
    r = run(PC, a, b)
    assert r.returncode == 1
    assert "FAIL preserve_diff" in r.stdout


def test_invisible_char_fails(write):
    a = write("a.md", "We sequenced 12 samples.\n")
    b = write("b.md", "We sequenced 12​ samples.\n")
    r = run(PC, a, b)
    assert r.returncode == 1
    assert "FAIL unicode_check" in r.stdout


def test_usage(write):
    assert run(PC).returncode == 2
