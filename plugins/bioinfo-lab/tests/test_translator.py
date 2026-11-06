import pytest

from conftest import run

CHECK = "translator/scripts/check_translation.py"


def status(write, src, tgt):
    r = run(CHECK, write("s.txt", src), write("t.txt", tgt))
    return r.returncode, r.stdout


@pytest.mark.parametrize("src,tgt", [
    ("The P value was 1.5e-8.", "P 值為 1.2e-8。"),
    ("The insert was 3.2kb long.", "插入片段長 3.7kb。"),
    ("We found β = -0.12.", "我們得到 β = 0.12。"),
])
def test_changed_number_fails(write, src, tgt):
    code, out = status(write, src, tgt)
    assert code == 1, out
    assert "FAIL number" in out


def test_identical_numbers_pass(write):
    code, out = status(write, "Of n = 5. Effect -0.12, 1.5e-8, 3.2kb, 2020-2021.",
                       "共 n = 5。效果 -0.12、1.5e-8、3.2kb、2020-2021。")
    assert code == 0, out


def test_url_before_chinese_clause_not_absorbed(write):
    code, out = status(write, "See https://a.org/x, and more text here.",
                       "請見 https://a.org/x，以及更多內容。")
    assert code == 0, out


def test_changed_url_still_fails(write):
    code, out = status(write, "See https://a.org/x, now.", "請見 https://a.org/y，現在。")
    assert code == 1 and "FAIL URL" in out


def test_thousands_separator_before_cjk(write):
    code, out = status(write, "There are 1,000 items.", "共有 1,000個項目。")
    assert code == 0, out


def test_lost_en_dash_minus_fails(write):
    code, out = status(write, "We found β = –0.12.", "我們得到 β = 0.12。")
    assert code == 1, out
    assert "FAIL number" in out


def test_en_dash_range_unchanged_passes(write):
    code, out = status(write, "Ages 5–10 years.", "年齡 5–10 歲。")
    assert code == 0, out
