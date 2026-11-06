"""Shared helpers: run bundled scripts in isolated mode and import them by path."""
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

SKILLS = Path(__file__).resolve().parents[1] / "skills"


def script(rel):
    return SKILLS / rel


def run(rel, *args, env=None):
    """Runs a script with `python -I`; returns CompletedProcess with text output."""
    return subprocess.run(
        [sys.executable, "-I", "-X", "utf8", str(script(rel)), *map(str, args)],
        capture_output=True, text=True, encoding="utf-8", env=env,
    )


def load_module(rel):
    path = script(rel)
    sys.path.insert(0, str(path.parent))
    try:
        spec = importlib.util.spec_from_file_location(path.stem + "_t", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        sys.path.remove(str(path.parent))
    return mod


@pytest.fixture
def write(tmp_path):
    def _write(name, text):
        p = tmp_path / name
        p.write_bytes(text.encode("utf-8"))
        return p
    return _write
