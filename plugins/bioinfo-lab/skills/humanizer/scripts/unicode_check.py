#!/usr/bin/env python3
"""Report invisible and look-alike characters in a text file; optionally fix a safe set.

Usage: python unicode_check.py FILE [--fix]

Reports line, column, code point, name, and the action for each finding. Exit code 1
if anything was found (before fixing), 0 if the file is clean, 2 on a read error.

--fix rewrites FILE and changes only these characters:
  removed: zero-width space, word joiner, byte-order mark, soft hyphen, directional
           marks and embeddings, variation selectors, and the tag block (U+E0000 range)
  to space: no-break space, narrow no-break space, figure space, en/em/thin/hair spaces
  to "-":  non-breaking hyphen
Never touched, only reported: zero-width joiner and non-joiner (needed in some
scripts), the ideographic space (zh-TW typesetting), other control characters, and
every look-alike such as the micro sign, Greek letters, superscripts, and ligatures.
Do not run NFKC over a whole file: it turns the micro sign into a Greek mu and
h² into h2.

These characters are formatting residue. None of this touches a statistical
watermark, which is carried by word choice and leaves no character to remove.
"""
import sys
import unicodedata

REMOVE = {0x200B, 0x2060, 0xFEFF, 0x00AD, 0x200E, 0x200F, 0x061C}
REMOVE |= set(range(0x202A, 0x202F)) | set(range(0x2066, 0x206A))
REMOVE |= set(range(0xFE00, 0xFE10)) | set(range(0xE0100, 0xE01F0)) | set(range(0xE0000, 0xE0080))
TO_SPACE = {0x00A0, 0x202F, 0x2007} | set(range(0x2000, 0x200B))
TO_HYPHEN = {0x2011}
WARN_ONLY = {0x200C, 0x200D, 0x3000}


def action(cp: int, ch: str) -> str | None:
    if cp in REMOVE:
        return "remove"
    if cp in TO_SPACE:
        return "space"
    if cp in TO_HYPHEN:
        return "hyphen"
    if cp in WARN_ONLY:
        return "report only"
    cat = unicodedata.category(ch)
    if cat == "Cc" and ch not in "\n\t\r":
        return "report only"
    if cat == "Cf":
        return "report only"
    if cat == "Zs" and ch != " ":
        return "report only"
    return None


def main(argv):
    fix = "--fix" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if len(paths) != 1:
        print(__doc__)
        return 2
    try:
        text = open(paths[0], encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"error: {e}")
        return 2
    found = 0
    out = []
    for lineno, line in enumerate(text.split("\n"), 1):
        for col, ch in enumerate(line, 1):
            cp = ord(ch)
            act = action(cp, ch)
            if act:
                found += 1
                name = unicodedata.name(ch, "UNNAMED")
                print(f"{paths[0]}:{lineno}:{col}: U+{cp:04X} {name} -> {act}")
        out.append(line)
    if fix and found:
        fixed = []
        for ch in text:
            cp = ord(ch)
            if cp in REMOVE:
                continue
            fixed.append(" " if cp in TO_SPACE else "-" if cp in TO_HYPHEN else ch)
        with open(paths[0], "w", encoding="utf-8", newline="") as f:
            f.write("".join(fixed))
        print(f"fixed the safe set in {paths[0]}; 'report only' items were left in place")
    if not found:
        print(f"{paths[0]}: no invisible or look-alike characters")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
