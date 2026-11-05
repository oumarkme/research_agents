---
name: humanizer
description: 'Use when you edit text so it reads like a careful specialist wrote it by hand: audit measured AI tells, clean invisible characters, and check that numbers, identifiers, and citations did not change. Called by writing. Not a detector-evasion or watermark tool.'
---

# Humanizer

Goal: the author's text reads naturally, keeps every fact, and carries no formatting residue. The pass edits prose and checks it with scripts. It does not tune text against detectors, and it cannot remove a statistical watermark (`references/limits.md`).

## Rules

1. Add no facts, names, numbers, or references. Specifics come from the author's source text or from the user.
2. Edit the author's text. Do not generate a draft only to humanize it. If you drafted the text yourself, say so in the report; the author may need to disclose it (`references/disclosure.md`).
3. Judge success by the checks below and by a human reader, never by a detector score. If asked for text that is "undetectable" or "watermark-free", do the ordinary edit, do not optimize against any detector, and say in one line that disclosure is the safeguard.

## Workflow

1. Keep the original: copy the file, or confirm it is committed. For chat text, skip the scripts and apply step 2 to the draft.
2. Audit. Read `${CLAUDE_SKILL_DIR}/references/tells.md` and list the tells you find, measured ones first. Use the field's own terms (`writing`, `references/field-vocabulary.md`).
3. Edit. Make the smallest change that removes each tell. Protected content stays as it is: numbers with units, P values, variant and gene strings, accessions, DOIs, PubMed IDs (PMIDs), citations, code, tables, and headings (`references/preservation.md`). Keep the author's wording where it is correct.
4. Check. Each command must pass:
   * `python ${CLAUDE_SKILL_DIR}/scripts/preserve_diff.py ORIGINAL EDITED` exits 0, or the author confirms each difference.
   * `python ${CLAUDE_SKILL_DIR}/scripts/unicode_check.py EDITED` reports nothing, or you run it with `--fix` and re-read the report.
   * `python ${CLAUDE_SKILL_DIR}/../writing/scripts/lint_prose.py EDITED` has no flag you cannot justify.
5. Report. Give the author the changed sentences (`git diff --word-diff` or `wdiff`), the three check results, and one line on whether a model rewrote sentences, so they can declare it where the journal asks.

## Notes

* The word list decays as models change. `references/era-words.md` is dated, so check its date before relying on it.
* Agentless passives in Methods are normal. Leave them.
* Chinese text follows `translator`; the checks above still run on it.
* Test cases and fixtures: `${CLAUDE_SKILL_DIR}/evals/evals.md`.
