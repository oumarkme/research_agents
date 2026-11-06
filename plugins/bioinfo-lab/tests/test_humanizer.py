from conftest import load_module, run

pd = load_module("humanizer/scripts/preserve_diff.py")


def toks(text, kind="numbers"):
    return set(pd.tokens(text, kind))


def test_unit_needs_boundary():
    assert toks("We had 12 samples.") == {"12"}
    assert toks("A 3 kb insert, 5-fold, 20 %.") >= {"3kb", "5-fold"}


def test_no_trailing_comma_in_number():
    assert toks("n = 12, then 1,234,567 reads") == {"12", "1,234,567"}


def test_non_utf8_input_clear_error(tmp_path):
    a, b = tmp_path / "a.txt", tmp_path / "b.txt"
    a.write_bytes(b"caf\xe9 1\n")
    b.write_text("cafe 1\n")
    r = run("humanizer/scripts/preserve_diff.py", a, b)
    assert r.returncode == 2
    assert "UTF-8" in r.stdout and "a.txt" in r.stdout
    assert "Traceback" not in r.stderr


def test_unicode_fix_keeps_crlf(tmp_path):
    p = tmp_path / "f.txt"
    p.write_bytes("a b\r\nc​\r\n".encode())
    r = run("humanizer/scripts/unicode_check.py", p, "--fix")
    assert r.returncode == 1
    assert p.read_bytes() == b"a b\r\nc\r\n"


def test_url_stops_at_fullwidth_punctuation():
    assert list(toks("見 https://example.org/data，for the", "url")) == ["https://example.org/data"]


def test_en_dash_minus_is_sign_but_range_is_not():
    assert "-0.12" in toks("β = –0.12", "numbers")
    assert toks("n = 5–10", "numbers") == toks("n = 5–10", "numbers")
    assert "-10" not in toks("n = 5–10", "numbers")
    assert "-10" not in toks("n = 5 – 10", "numbers")
