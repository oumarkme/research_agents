#!/usr/bin/env python3
"""Compare a source text and its translation for language-neutral items.

Usage: python3 check_translation.py SOURCE TARGET

Checks (Chinese and English, either direction; standard library only):
  FAIL  a DOI or URL differs between the texts
  FAIL  a number differs (multiset comparison, thousands separators ignored)
  WARN  a citation (surname, year) is missing from one text
  WARN  an abbreviation, gene symbol, or mixed-case term present in the source is
        absent from the target (spelled-out forms can explain this; judge it)
  WARN  the sentence counts differ by more than 25% or by 3 or more

Limits: numbers written as words or Chinese numerals, and dates written in words,
are not matched. A clean run does not prove the translation is correct; it only
shows that these items survived. Exit code 1 when any FAIL is found.
"""
import re
import sys
import unicodedata
from collections import Counter

DOI = re.compile(r"10\.\d{4,9}/[^\s)\]，。；、]+")
URL = re.compile(r"https?://[^\s)\]，。；、]+")
NUM = re.compile(r"(?<![A-Za-z0-9_.])\d+(?:\.\d+)?(?![A-Za-z0-9_])")
YEAR = re.compile(r"(?<!\d)(?:19|20)\d{2}[a-z]?(?!\d)")
SURNAME = re.compile(r"([A-Z][A-Za-z'’\-]+)(?:\s+et al\.?|\s+(?:&|and)\s+[A-Z][A-Za-z'’\-]+)?[\s,(]*$")
TERM = re.compile(r"\b(?=[A-Za-z0-9\-]*[A-Z][A-Za-z0-9\-]*[A-Z0-9])[A-Za-z][A-Za-z0-9\-]{1,}\b")
TRAIL = ".,;:)]}。，；："


def load(path):
    with open(path, encoding="utf-8") as f:
        text = unicodedata.normalize("NFKC", f.read())
    return re.sub(r"(?<=\d),(?=\d{3}\b)", "", text)


def clean(items):
    return [i.rstrip(TRAIL) for i in items]


def extract(text):
    dois = clean(DOI.findall(text))
    urls = clean(URL.findall(text))
    body = DOI.sub(" ", URL.sub(" ", text))
    nums = Counter(NUM.findall(body))
    cites = Counter()
    for m in YEAR.finditer(body):
        s = SURNAME.search(body[max(0, m.start() - 40):m.start()])
        if s:
            cites[(s.group(1), m.group())] += 1
    terms = Counter(t for t in TERM.findall(body) if len(t) > 1)
    sents = len([s for s in re.split(r"(?<=[.!?。！？])\s*", body) if len(s.strip()) > 3])
    return Counter(dois), Counter(urls), nums, cites, terms, sents


def diff(a, b):
    return sorted((a - b).elements()), sorted((b - a).elements())


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    s_doi, s_url, s_num, s_cit, s_term, s_n = extract(load(argv[1]))
    t_doi, t_url, t_num, t_cit, t_term, t_n = extract(load(argv[2]))
    fails = warns = 0
    for label, a, b in (("DOI", s_doi, t_doi), ("URL", s_url, t_url), ("number", s_num, t_num)):
        only_s, only_t = diff(a, b)
        if only_s or only_t:
            fails += 1
            print(f"FAIL {label}: only in source {only_s or '-'}; only in target {only_t or '-'}")
    only_s, only_t = diff(s_cit, t_cit)
    if only_s or only_t:
        warns += 1
        print(f"WARN citation: only in source {only_s or '-'}; only in target {only_t or '-'}")
    missing = sorted(t for t in s_term if t not in t_term)
    if missing:
        warns += 1
        print(f"WARN term absent from target: {missing}")
    if abs(s_n - t_n) >= 3 or (s_n and abs(s_n - t_n) / s_n > 0.25):
        warns += 1
        print(f"WARN sentence count: source {s_n}, target {t_n}")
    print(f"{fails} FAIL, {warns} WARN" + ("" if fails or warns else " (items preserved)"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
