---
name: writing
description: 'Use whenever you write or edit prose in a file (manuscript, abstract, methods, caption, README, report, grant): American academic English rules, mandatory humanizer pass, lint script.'
---

# Writing (academic English)

Goal: a reader outside the sub-field, including a non-native reader, understands each sentence once, in one way. Scope: every text you write (files, skill and README edits, code comments, commit messages, chat), all of it with the humanizer pass and the word choice rule below. Chat follows the user's language. File text is American English unless the user asks for another language (`translator`; default pair: Taiwan Traditional Chinese). In an existing document, keep its voice, format, and spelling, and apply these rules only to text you add or change.

## Workflow (all steps mandatory)

1. Write the main message in one sentence: what was done or found, and why it matters. Every paragraph serves it.
2. Draft with the quick rules below. For a manuscript, abstract, grant, report, or text over about 150 words, first read `${CLAUDE_SKILL_DIR}/references/rules.md` and `references/field-vocabulary.md`.
3. Humanizer pass: read `${CLAUDE_SKILL_DIR}/references/humanizer.md` and rewrite until the text reads like a careful specialist wrote it by hand. Never skipped, even for a README or a caption.
4. Run `python ${CLAUDE_SKILL_DIR}/scripts/lint_prose.py <file>`. Fix every flag that is a real problem (flags are heuristics). Repeat steps 3 and 4 until clean or each remaining flag is justified.
5. Re-read as a hostile reader: any sentence with two readings, any claim without a number, citation, or stated basis, anything that sounds like a chatbot.
6. Evidence: cite recent, primary, reputable sources in APA 7, verified by PMID or DOI (`trusted-sources`). Never invent a reference; AI text is not a source. If evidence is missing, say so in the text or ask.

## Quick rules

* Active voice with "we"; one idea per sentence, under 30 words; plain words (use, show, about, to).
* One term per concept; define each abbreviation once; no sentence starting with a bare This or It.
* Every comparison has a number, a unit, and a comparator. "Significant" means statistically significant, with test and P value. Correlation is not effect; use causal verbs only when the design supports them.
* No priority or praise (novel, first, robust, crucial). Match strength to evidence: show, suggest, may.
* Tense: past for what was done and found; present for established knowledge and what a figure shows.
* American spelling (analyze, color, behavior, center, program, modeling, labeled, gray, license); serial comma; periods and commas inside quotation marks; dates as 2026-10-02 in files; SI units with a space (5 kb, 37 °C).
* Gene symbols in italics, protein symbols upright; species in Latin italics at first mention; give genome build, software, version, and key parameters.
* Word choice: use the term that recent papers in the field use most often (check PubMed or a recent review when unsure), not the word LLMs overuse. Say *read depth*, not *sequencing intensity*; *prediction accuracy*, not *performance metric*; *contrast ratio*, not *visual distinguishability*.
* Humanizer in brief: cut stock vocabulary and reflex structures (not only X but also Y, rule of three, closing recap), em dashes, bold lead-ins, and vague attribution. Add specifics, vary sentence length, say it once.

Final check: main message stated · numbers have units and comparators · abbreviations defined once · claims match evidence · citations verified · humanizer done · lint clean.
