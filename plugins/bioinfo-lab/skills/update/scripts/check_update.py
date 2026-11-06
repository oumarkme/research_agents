#!/usr/bin/env python3
"""Compare the installed bioinfo-lab version with the latest on GitHub.

Usage: python check_update.py [--json]
Reads the local plugin.json, fetches the remote one, lists the newest commit
subjects, and prints the commands that update the plugin. It changes nothing.
Exit status: 0 up to date, 10 update available, 2 could not check.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

REPO = "oumarkme/research_agents"
REMOTE = f"https://raw.githubusercontent.com/{REPO}/main/plugins/bioinfo-lab/.claude-plugin/plugin.json"
COMMITS = f"https://api.github.com/repos/{REPO}/commits?per_page=5"
LOCAL = Path(__file__).resolve().parents[2].parent / ".claude-plugin" / "plugin.json"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "bioinfo-lab-update"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode("utf-8")


def parse(v):
    """Sortable key for 'X.Y[.Z][-pre]'; a pre-release sorts before its release."""
    m = re.match(r"\s*v?(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:[-+.]?([0-9A-Za-z.\-]+))?", v)
    if not m:
        raise ValueError(f"unrecognized version: {v!r}")
    nums = tuple(int(x or 0) for x in m.groups()[:3])
    pre = m.group(4) or ""
    return nums + (0 if pre else 1, pre)


def main():
    if any(a in ("-h", "--help") for a in sys.argv[1:]):
        print(__doc__)
        return 0
    as_json = "--json" in sys.argv
    try:
        local = json.loads(LOCAL.read_text(encoding="utf-8"))["version"]
        parse(local)
    except (OSError, ValueError, KeyError, TypeError) as e:
        local = None
        print(f"Installed version unknown: cannot read a version from {LOCAL} ({e}).")
    try:
        remote = json.loads(get(REMOTE))["version"]
    except Exception as e:  # network, DNS, or JSON failure
        print(f"Could not reach GitHub ({e}). Installed: {local or 'unknown'}.")
        return 2
    if local is None:
        print(f"Latest: {remote}. Compare it with your installed version by hand.")
        return 2
    newer = parse(remote) > parse(local)
    commits = []
    try:
        commits = [c["commit"]["message"].splitlines()[0] for c in json.loads(get(COMMITS))]
    except Exception:
        pass
    if as_json:
        print(json.dumps({"installed": local, "latest": remote, "update": newer, "recent": commits}))
    else:
        print(f"Installed: {local}\nLatest:    {remote}")
        print("Update available." if newer else "Up to date.")
        if commits:
            print("Recent changes on main:")
            for c in commits:
                print(f"  - {c}")
        if newer:
            print("\nRun in Claude Code, then restart or reload:")
            print(f"  /plugin marketplace update {REPO.split('/')[1]}")
            print("  /plugin update bioinfo-lab@research_agents")
            print("  /reload-plugins")
    return 10 if newer else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):  # Windows consoles default to a legacy code page
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
