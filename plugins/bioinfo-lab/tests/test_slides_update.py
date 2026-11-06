import io
import json
import zipfile

import pytest

from conftest import load_module

ft = load_module("slides/scripts/fetch_template.py")
cu = load_module("update/scripts/check_update.py")
SHA = "0123456789abcdef0123456789abcdef01234567"


def make_zip(files, comment=b""):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, text in files.items():
            z.writestr(name, text)
        z.comment = comment
    return buf.getvalue()


def fetch(monkeypatch, tmp_path, data):
    class Resp:
        def read(self):
            return data
    monkeypatch.setattr(ft.urllib.request, "urlopen", lambda *a, **k: Resp())
    monkeypatch.setattr(ft.sys, "argv", ["x", str(tmp_path / "dest")])
    return ft.main()


def test_bad_zip(monkeypatch, tmp_path, capsys):
    assert fetch(monkeypatch, tmp_path, b"not a zip") == 2
    assert "zip" in capsys.readouterr().out.lower()


def test_missing_readme(monkeypatch, tmp_path, capsys):
    assert fetch(monkeypatch, tmp_path, make_zip({"slide_template-main/a.txt": "x"})) == 2
    assert "README" in capsys.readouterr().out


def test_commit_id_printed(monkeypatch, tmp_path, capsys):
    data = make_zip({"slide_template-main/README.md": "Version 2.1\n"}, SHA.encode())
    assert fetch(monkeypatch, tmp_path, data) == 0
    out = capsys.readouterr().out
    assert "2.1" in out and SHA in out


@pytest.mark.parametrize("a,b", [("1.7.0-rc1", "1.7.0"), ("1.6.0", "1.7.0-rc1"), ("1.6", "1.6.1")])
def test_parse_orders_prerelease(a, b):
    assert cu.parse(a) < cu.parse(b)


def run_update(monkeypatch, tmp_path, local_text, remote="1.7.0"):
    loc = tmp_path / "plugin.json"
    if local_text is not None:
        loc.write_text(local_text)
    monkeypatch.setattr(cu, "LOCAL", loc)
    monkeypatch.setattr(cu, "get", lambda url: json.dumps({"version": remote}) if "plugin.json" in url else "[]")
    monkeypatch.setattr(cu.sys, "argv", ["x"])
    return cu.main()


def test_prerelease_local(monkeypatch, tmp_path):
    assert run_update(monkeypatch, tmp_path, '{"version": "1.7.0-rc1"}') == 10


def test_missing_local(monkeypatch, tmp_path, capsys):
    assert run_update(monkeypatch, tmp_path, None) == 2
    assert "plugin.json" in capsys.readouterr().out
