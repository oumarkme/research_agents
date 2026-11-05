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

UNIT = r"(?:\s?(?:%|°C|°F|[kMGT]b|bp|[kMG]B|kDa|cM|×|x|-?fold|Hz|kg|mg|µg|ng|mL|µL|nM|µM|mM|min|h|s|d))?"
NUM = r"(?<![\w.])[-+−]?\d[\d,]*(?:\.\d+)?(?:[eE][-+]?\d+)?"

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
    "url": re.compile(r"https?://[^\s)\]>\"]+"),
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


def tokens(text: str, kind: str) -> Counter:
    pat = PATTERNS[kind]
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
    try:
        a = open(args[0], encoding="utf-8").read()
        b = open(args[1], encoding="utf-8").read()
    except OSError as e:
        print(f"error: {e}")
        return 2
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
    sys.exit(main(sys.argv[1:]))
