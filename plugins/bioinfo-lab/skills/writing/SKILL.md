---
name: writing
description: 'Use whenever you draft or edit prose in a file (manuscript, abstract, methods, caption, README, report, grant): American academic English, humanizer pass, lint script. Not for the audit-only clean pass (humanizer).'
---

# Writing (academic English)

Goal: a reader outside the sub-field, including a non-native reader, reads each sentence one way. Scope: every text you write (files, skill and README edits, code comments, commit messages, chat), with the humanizer pass. Chat follows the user's language. File text is American English unless the user asks otherwise (`translator`). In an existing document, keep its voice, format, and spelling; apply these rules only to text you add or change.

## Workflow (all steps mandatory)

1. Write the main message in one sentence: what was done or found, and why it matters. Every paragraph serves it.
2. Draft with the quick rules below. For a manuscript, abstract, grant, report, or text over about 150 words, first read `${CLAUDE_SKILL_DIR}/references/rules.md` and `references/field-vocabulary.md`.
3. Humanizer pass: load the `humanizer` skill and follow it (tells audit, preservation diff, Unicode check). Never skip it, even for a README or caption. For chat text, apply its `references/tells.md` without the scripts.
4. Run `python ${CLAUDE_SKILL_DIR}/scripts/prose_check.py ORIGINAL EDITED` (one command for lint, preserve_diff, and unicode_check), or `lint_prose.py <file>` alone for a new file. Fix each real problem (flags are heuristics). Repeat steps 3 and 4 until clean or every remaining flag is justified. If a model wrote or rewrote sentences, tell the author, who may need to declare it (`humanizer/references/disclosure.md`).
5. Re-read as a hostile reader: any sentence with two readings, any claim without a number, citation, or stated basis, anything that sounds like a chatbot.
6. Evidence: cite recent, primary, reputable sources in APA 7, verified by PMID or DOI (`trusted-sources`). Never invent a reference; AI text is not a source. If evidence is missing, say so in the text or ask.

## Quick rules

* Active voice with "we"; one idea per sentence, under 30 words; plain words (use, show, about).
* One term per concept; define each abbreviation once; no sentence starting with a bare This or It.
* Every comparison has a number, a unit, and a comparator. "Significant" means statistically significant, with test and P value. Correlation is not effect; use causal verbs only when the design supports them.
* No priority or praise (novel, first, robust, crucial). Match strength to evidence: show, suggest, may.
* Tense: past for what was done and found; present for established knowledge and what a figure shows.
* American spelling (analyze, color, behavior, center, modeling, labeled, gray); serial comma; periods and commas inside quotation marks; dates as 2026-10-02 in files; SI units with a space (5 kb, 37 °C).
* Gene symbols in italics, protein symbols upright; species in Latin italics at first mention; give genome build, software, version, and key parameters.
* Word choice: use the term recent papers in the field use most often (check PubMed when unsure), not a word LLMs overuse: *read depth*, not *sequencing intensity*; *prediction accuracy*, not *performance metric*.
* Humanizer: cut stock vocabulary, reflex structures, em dashes, and vague attribution; add specifics (`humanizer`).

Final check: main message stated · numbers have units and comparators · abbreviations defined once · claims match evidence · citations verified · humanizer done · lint clean.
