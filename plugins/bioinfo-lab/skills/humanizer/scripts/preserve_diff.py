#!/usr/bin/env python3
"""Check that an edit did not change numbers, identifiers, or citations.

Usage: python preserve_diff.py ORIGINAL EDITED [--skip KIND[,KIND...]] [--list]

Extracts protected tokens from both files, compares them as multisets, and prints
every token that was lost or added. Exit code 0 means identical protected content;
1 means at least one difference; 2 means a usage or read error.

Kinds: numbers, comparisons, hgvs, rsid, accession, doi, pmid, url, citation_key,
author_year, code, heading, figref, symbol. Use --skip heading when headings were
meant to change. Use --list to print the kinds and exit.

This is a mechanical check. It does not see numbers written as words, a changed
claim strength, or a reordered argument. Read the diff as well.
"""
import re
import sys
from collections import Counter

# A unit must end at a letter boundary, so "12 samples" is not "12 s".
UNIT = r"(?:\s?(?:%|°C|°F|[kMGT]b|bp|[kMG]B|kDa|cM|×|x|-?fold|Hz|kg|mg|µg|ng|mL|µL|nM|µM|mM|min|h|s|d)(?![A-Za-z]))?"
# Thousands groups only, so "n = 12, p" does not keep the comma.
NUM = r"(?<![\w.])[-+−]?\d+(?:,\d{3})*(?:\.\d+)?(?:[eE][-+]?\d+)?"

PATTERNS = {
    "numbers": re.compile(NUM + UNIT),
    "comparisons": re.compile(r"(?:\b[PpQq]|\bFDR|\bOR|\bHR|\bCI)\s*[<>=≤≥]\s*[-+]?\d[\d.eE-]*"),
    "hgvs": re.compile(r"\b[cgmnpr]\.[A-Za-z0-9_>*+\-?=()]+"),
    "rsid": re.compile(r"\brs\d+\b"),
    "accession": re.compile(
        r"\b(?:NM|NP|NR|NC|NG|XM|XP|ENST|ENSG|ENSP|GCA|GCF|SRR|SRX|SRP|ERR|PRJNA|PRJEB|SAMN|GSE|GSM|VCV|RCV|SCV|MIM)[_:]?\d+(?:\.\d+)?"
    ),
    "doi": re.compile(r"10\.\d{4,9}/[^\s\"<>)\]]+"),
    "pmid": re.compile(r"PMID:?\s*\d+"),
    "url": re.compile(r"https?://[^\s)\]>\",;\u3000-\u9fff\uff00-\uffef]+"),
    "citation_key": re.compile(r"\[@[^\]]+\]|\\cite\w*\{[^}]+\}"),
    "author_year": re.compile(
        r"\b([A-Z][A-Za-z'\-]+)(?: et al\.| (?:and|&) [A-Z][A-Za-z'\-]+)?,? \(?(\d{4}[a-z]?)\)?"
    ),
    "code": re.compile(r"```.*?```|`[^`\n]+`", re.S),
    "heading": re.compile(r"^#{1,6}\s+(.*)$", re.M),
    "figref": re.compile(
        r"\b(?:Supplementary\s+)?(?:Fig(?:ure)?s?\.?|Tables?)\s*S?\d+[A-Za-z]?", re.I
    ),
    "symbol": re.compile(r"\b[A-Z][A-Z0-9]{2,}\b"),
}


# An en dash is a minus sign only when no digit or word precedes it, so 5-10 stays a range.
EN_DASH_SIGN = re.compile(r"(?<![\w.)])(?<!\w\s)\u2013(?=\d)")


def tokens(text: str, kind: str) -> Counter:
    pat = PATTERNS[kind]
    if kind == "numbers":
        text = EN_DASH_SIGN.sub("-", text)
    out = Counter()
    for m in pat.finditer(text):
        if kind == "author_year":
            tok = m.group(1) + " " + m.group(2)
        elif kind == "heading":
            tok = m.group(1).strip()
        else:
            tok = re.sub(r"\s+", "", m.group(0)) if kind == "numbers" else m.group(0).strip()
        out[tok.replace("−", "-")] += 1
    return out


def main(argv):
    if any(a in ("-h", "--help") for a in argv):
        print(__doc__)
        return 0
    if "--list" in argv:
        print("\n".join(PATTERNS))
        return 0
    skip = set()
    args = []
    i = 0
    while i < len(argv):
        if argv[i] == "--skip" and i + 1 < len(argv):
            skip = set(argv[i + 1].split(","))
            i += 2
        else:
            args.append(argv[i])
            i += 1
    if len(args) != 2 or not skip <= set(PATTERNS):
        print(__doc__)
        return 2
    texts = []
    for path in args:
        try:
            with open(path, encoding="utf-8-sig") as f:
                texts.append(f.read())
        except UnicodeDecodeError as e:
            print(f"error: {path} is not valid UTF-8 ({e.reason} at byte {e.start}); "
                  "convert it first, for example: iconv -f <encoding> -t UTF-8")
            return 2
        except OSError as e:
            print(f"error: {e}")
            return 2
    a, b = texts
    bad = 0
    for kind in PATTERNS:
        if kind in skip:
            continue
        ca, cb = tokens(a, kind), tokens(b, kind)
        lost, added = ca - cb, cb - ca
        for tok, n in sorted(lost.items()):
            print(f"[{kind}] LOST  x{n}: {tok[:100]}")
            bad += 1
        for tok, n in sorted(added.items()):
            print(f"[{kind}] ADDED x{n}: {tok[:100]}")
            bad += 1
    if bad:
        print(f"{bad} protected-token difference(s). Fix the edit or confirm each one with the author.")
        return 1
    print("protected tokens identical")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):  # Windows consoles default to a legacy code page
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main(sys.argv[1:]))
