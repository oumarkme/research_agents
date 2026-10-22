#!/usr/bin/env python3
"""Heuristic prose linter for the writing skill. Flags, does not fix.

Usage: python lint_prose.py file.md [file2 ...]
Skips YAML front matter, fenced code, HTML/style blocks, tables, and link targets.
Checks: self-praise/priority words, filler, vague quantifiers, bare "This/It" openers,
long sentences, undefined abbreviations, "significant" without a statistic, causal verbs,
missing space before units, passive-voice candidates (informational).
"""
import re
import sys

BANNED = r"novel|unprecedented|groundbreaking|ground-breaking|remarkabl[ey]|striking(ly)?|dramatic(ally)?|superior|state-of-the-art|cutting-edge|paradigm[- ]shift\w*|pioneering|crucial(ly)?|first (report|time|study|to)|world-class"
FILLER = r"it is worth noting|it should be noted|needless to say|a total of|due to the fact that|in order to|as a matter of fact|in the context of|basically|obviously|very|really|quite|utili[sz]e[sd]?|interestingly|plays? an? (important|crucial|key|vital) role"
VAGUE = r"a lot of|lots of|many|several|numerous|some|various|good|better|worse|high(?:er)?|low(?:er)?|improved?|similar|large|small"
CAUSAL = r"causes?|caused|leads? to|drives?|driven by|results? in|affects?|regulates?|controls?"
AI_WORDS = r"delv(e|es|ing)|tapestry|landscape of|realm|underscor(e|es|ing)|showcas(e|es|ing)|foster(s|ing)?|pivotal|vital|intricate|multifaceted|nuanced|comprehensive|seamless(ly)?|leverag(e|es|ing)|harness(es|ing)?|streamlin(e|es|ing)|bolster(s|ing)?|elucidat(e|es|ing)|shed(s|ding)? light|pave[sd]? the way|in the era of|testament|ever-evolving|game[- ]chang\w+|holistic|synerg\w+|myriad|plethora|notably|importantly|moreover|furthermore|additionally|in conclusion|in summary|overall,|it is important to note|it is worth mentioning|serves? as|stands? as|acts? as|robust|navigat(e|es|ing) the|certainly|great question|i hope this helps"
AI_STRUCT = [
    (r"\bnot only\b.{0,80}\bbut (also|rather)\b", "'not only ... but also' construction"),
    (r"\bit(?:'s| is) not (?:just|merely|only)\b", "'it is not just X' construction"),
    (r",\s+(?:highlighting|underscoring|emphasizing|demonstrating|showcasing|reflecting|illustrating|suggesting that)\b", "trailing -ing clause adding vague significance"),
    (r"\b(studies|research|experts|scientists) (show|suggest|indicate|agree|have shown)\b(?![^.]*[\(\[])", "vague attribution without citation"),
    (r"—|--", "em dash (use comma, colon, parentheses, or split the sentence)"),
]
BRITISH = r"analys(e|ed|es|ing)|colou?r?ed|colour\w*|behaviour\w*|centre\w*|programme\w*|fibre\w*|licence|modell(ing|ed)|labell(ed|ing)|catalogue|grey\w*|defence|\w+isation\w*|\w+is(e|ed|es|ing)\b(?<!otherwise)(?<!advise)(?<!revise)(?<!revised)(?<!revising)(?<!exercise)(?<!rise)(?<!raise)|whilst|amongst|favour\w*|neighbour\w*|haem\w*|oestr\w*|sulph\w*|tumour\w*|paediatric\w*|ageing|judgement|artefact\w*"
try:
    from opencc import OpenCC
    _S2TWP = OpenCC("s2twp")
except Exception:  # fall back to the character list below
    _S2TWP = None
SIMPLIFIED = set("这个们为国对时会来发学经现说还从体关实术进过动机资数据软网络视频质预设库产种变异检测验确论图简报写设测试态状乱码环视显")
ZH_TERMS = "基因體學|基因體|基因組|基因型|表現型|表型|定序|測序|變異|變體|突變|等位基因|染色體|轉錄體|蛋白質體|生物資訊|關聯分析|連鎖不平衡|遺傳率|育種值|育種|基因剔除|資料庫|演算法|機器學習|深度學習|迴歸|交叉驗證|訓練集|測試集|組裝|比對|讀長|覆蓋度|深度學習|顯著性|信賴區間|標準差|標準誤"
STD_ABBR = {"DNA", "RNA", "SD", "SEM", "CI", "PCR", "USA", "UK", "SI", "PDF", "HTML", "CSV", "PNG", "URL", "DOI", "APA", "SNP", "QTL", "GWAS", "ONT", "GPU", "CPU", "RAM", "README", "YAML", "ID", "OK"}


def strip(text: str) -> str:
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<style.*?</style>|<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"^\s*\|.*\|\s*$", "", text, flags=re.M)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"`[^`]*`", "``", text)
    return text


def lint(path: str) -> int:
    raw = open(path, encoding="utf-8").read()
    text = strip(raw)
    n = 0

    def flag(kind, snippet):
        nonlocal n
        n += 1
        print(f"{path}: [{kind}] {snippet.strip()[:110]}")

    sentences = [s for s in re.split(r"(?<=[.!?])\s+|\n{2,}|\n[*\-] |\n#+ ", text) if s.strip()]
    seen_abbr = set()
    for s in sentences:
        words = s.split()
        if len(words) > 35:
            flag("long sentence (%d words)" % len(words), s)
        if re.match(r"\s*(This|These|Those|It|They|Such)\b(?!\s+\w+(?:\s+\w+)?\s+(?:is|are|was|were)\b.*\bwhich\b)", s) and re.match(r"\s*(This|These|It|They|Such)\s+(is|are|was|were|has|have|had|can|may|will|shows?|suggests?|means?|leads?)\b", s):
            flag("bare pronoun opener", s)
        for m in re.finditer(BANNED, s, re.I):
            flag("self-praise/priority: " + m.group(0), s)
        for m in re.finditer(FILLER, s, re.I):
            flag("filler: " + m.group(0), s)
        for m in re.finditer(r"\b(%s)\b" % VAGUE, s, re.I):
            if not re.search(r"\d", s):
                flag("vague, no number: " + m.group(0), s)
                break
        if re.search(r"\bsignificant(ly)?\b", s, re.I) and not re.search(r"[Pp]\s*[<=>≤]|CI|\bFDR\b|q\s*[<=]|test", s):
            flag("'significant' without statistic", s)
        if re.search(r"\b(%s)\b" % CAUSAL, s, re.I):
            flag("causal verb: check design supports causality", s)
        if re.search(r"\d(?:\.\d+)?(kb|Mb|Gb|bp|mM|µM|uM|nM|mg|kg|ml|mL|µL|°C|%?h|min|GB|TB)\b", s):
            flag("missing space between number and unit", s)
        if re.search(r"\b(?:is|are|was|were|been|being|be)\s+\w+(?:ed|en)\b(?!\s+(?:by\s+)?(?:the\s+)?\w+\s+(?:of)\b)", s) and len(words) > 8:
            if re.search(r"\bby\b", s):
                flag("passive with agent (consider active)", s)
        for m in re.finditer(r"\b(%s)\b" % AI_WORDS, s, re.I):
            flag("AI-typical word: " + m.group(0), s)
        for pat, msg in AI_STRUCT:
            if re.search(pat, s, re.I):
                flag("AI-typical pattern: " + msg, s)
        for m in re.finditer(r"\b(%s)\b" % BRITISH, s, re.I):
            if m.group(0).lower() not in {"otherwise", "advise", "likewise", "precise", "exercise", "promise", "surprise", "wise", "premise", "expertise", "comprise", "enterprise", "compromise", "paradise", "disguise", "concise", "noise", "praise"}:
                flag("British spelling (use American): " + m.group(0), s)
                break
        if re.search(r"[\u4e00-\u9fff]", s):
            if _S2TWP is not None:
                conv = _S2TWP.convert(s)
                if conv != s:
                    diff = [f"{a}->{b}" for a, b in zip(s, conv) if a != b][:8]
                    flag("Simplified characters or mainland usage (OpenCC s2twp): " + " ".join(diff) + (" ..." if len(diff) == 8 else ""), s)
            else:
                bad = sorted({c for c in s if c in SIMPLIFIED})
                if bad:
                    flag("possible Simplified Chinese characters (install OpenCC for a full check): " + "".join(bad), s)
            zh = sorted(set(re.findall(ZH_TERMS, s)))
            if zh:
                flag("technical term in Chinese (keep English): " + " ".join(zh), s)
            if re.search(r"[\u4e00-\u9fff][,:;?!]|[,:;?!][\u4e00-\u9fff]|[\u4e00-\u9fff]\.(?:\s|$)", s):
                flag("half-width punctuation next to Chinese (use full-width ，：；？！。)", s)
        for m in re.finditer(r"\b([A-Z][A-Za-z]*[A-Z0-9]+[a-z]?s?)\b", s):
            ab = m.group(1).rstrip("s")
            if ab in STD_ABBR or ab in seen_abbr or len(ab) < 2 or ab.isdigit():
                continue
            seen_abbr.add(ab)
            if not re.search(r"\(\s*%s\s*\)" % re.escape(ab), text):
                flag("abbreviation not defined as '(%s)'" % ab, s)
    if re.search(r"^\s*[*\-]\s+\*\*[^*]+\*\*[:.]?|^\s*[*\-]\s+\*\*[^*]*[:.]\*\*", text, re.M):
        flag("AI-typical formatting", "bold lead-in phrases in bullets")
    if re.search(r"^#{1,6}\s+(?:[A-Z][a-z]+\s+){2,}[A-Z][a-z]+\s*$", text, re.M):
        flag("AI-typical formatting", "Title Case heading (use sentence case)")
    if re.search(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", text):
        flag("AI-typical formatting", "emoji")
    if re.search(r"[\u201c\u201d\u2018\u2019]", text):
        flag("formatting", "curly quotes (use straight quotes in plain files)")
    paras = [p for p in re.split(r"\n{2,}", text) if len(p.split()) > 20]
    if len(paras) >= 4:
        lens = [len(p.split()) for p in paras]
        if max(lens) - min(lens) < 0.2 * (sum(lens) / len(lens)):
            flag("AI-typical rhythm", "paragraphs are nearly identical in length")
    if n == 0:
        print(f"{path}: no flags")
    else:
        print(f"{path}: {n} flag(s) — judge each; heuristics produce false positives")
    return n


if __name__ == "__main__":
    total = sum(lint(p) for p in sys.argv[1:])
    sys.exit(1 if total else 0)
