#!/usr/bin/env python3
"""Run the prose checks on an edit and print one summary.

Usage: python prose_check.py ORIGINAL EDITED

Runs, as separate processes (their own command-line tools stay unchanged):
  lint_prose.py      on EDITED          heuristic flags -> WARN (judge each)
  preserve_diff.py   ORIGINAL vs EDITED lost or added numbers, IDs, citations -> FAIL
  unicode_check.py   on EDITED          invisible characters -> FAIL
Exit code: 0 no FAIL, 1 at least one FAIL (a check that could not run counts as FAIL),
2 usage error. Unicode_check is run without --fix, so no file is changed.
"""
import subprocess
import sys
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[2]
LINT = Path(__file__).resolve().with_name("lint_prose.py")
DIFF = SKILLS / "humanizer" / "scripts" / "preserve_diff.py"
UNI = SKILLS / "humanizer" / "scripts" / "unicode_check.py"


def run(script, *args):
    r = subprocess.run(
        [sys.executable, "-I", "-X", "utf8", str(script), *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout + r.stderr).rstrip()


def main(argv):
    if any(a in ("-h", "--help") for a in argv):
        print(__doc__)
        return 0
    if len(argv) != 2:
        print(__doc__)
        return 2
    orig, edited = argv
    steps = [
        ("lint_prose", "WARN", LINT, (edited,), {0}),
        ("preserve_diff", "FAIL", DIFF, (orig, edited), {0}),
        ("unicode_check", "FAIL", UNI, (edited,), {0}),
    ]
    summary, fails = [], 0
    for name, level, script, args, ok_codes in steps:
        code, out = run(script, *args)
        print(f"== {name} (exit {code})")
        print("\n".join("   " + line for line in out.splitlines()) or "   (no output)")
        if code in ok_codes:
            summary.append(f"ok   {name}")
        elif code == 1 and level == "WARN":
            summary.append(f"WARN {name}")
        else:  # FAIL level, or exit 2 / crash from any check
            summary.append(f"FAIL {name}")
            fails += 1
    print("\nSummary")
    print("\n".join("  " + s for s in summary))
    return 1 if fails else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):  # Windows consoles default to a legacy code page
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
