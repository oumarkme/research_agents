---
name: translator
description: "Use for any translation of academic text between American academic English and another language (default target language from the user's CLAUDE.md, else ask): manuscripts, abstracts, captions, letters, READMEs."
---

# Translator (academic English ⇄ any language)

Goal: the target text carries exactly the source meaning and reads as if a specialist wrote it in the target language. For files, `writing` also applies to English text.

## Language pair

* Default: the target language set in the user's CLAUDE.md, else ask. A non-English source with no stated target goes to American English.
* Any other language: the user names it. Read `${CLAUDE_SKILL_DIR}/references/languages/<code>.md` if it exists (`zh-TW` ships as one example); if not, follow `_template.md` there, state your term and register choices in one line, and continue. Ask only if the choice changes the meaning.
* A pair with no English side: see the last line of `${CLAUDE_SKILL_DIR}/references/method.md`.

## Workflow (all steps mandatory)

1. Identify direction, register (manuscript, abstract, email, README), audience, and field. If the source is ambiguous, ask or state the chosen reading in one line.
2. List the terms, numbers, units, citations, abbreviations, and proper nouns, and fix one rendering for each. For a file, keep the fixed renderings in `glossary.tsv` beside the source (columns `source_term`, `target_term`, `note`; start from `${CLAUDE_SKILL_DIR}/templates/glossary.tsv`). Read it first if it exists. Record only decisions between renderings.
3. Translate sentence by sentence, then restructure for the target language. For manuscripts, abstracts, and grants read `${CLAUDE_SKILL_DIR}/references/method.md`. Over about 1,500 words, translate section by section with the glossary and a one-line summary of the previous section, and check each before moving on.
4. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/check_translation.py <source> <target>`. Fix every FAIL (DOI, URL, or number differs) and judge every WARN (citation, abbreviation, sentence count). Then do the manual back-check below.
5. For files, run the humanizer pass and the `writing` lint script (`python ${CLAUDE_SKILL_DIR}/../writing/scripts/lint_prose.py <file>`; add `--zh-tw` when the target is Taiwan Traditional Chinese). The lint script covers English and, with that flag, Taiwan Traditional Chinese; for another language, say it was not run. Translate code comments only when asked.

## Terms and back-check

* Proper nouns, symbols, species, software, versions, and identifiers stay in the source form. One source term, one target term; no coined terms or calques. When unsure whether a word is technical, keep the source form.
* After the script, compare by hand: sentence order, units, glossary terms, negations and qualifiers, claim strength, citations, nothing added or dropped, no sentence readable two ways, no AI-sounding phrasing.
* Full term rules (verifying field terms, abbreviations) and the back-check list: `${CLAUDE_SKILL_DIR}/references/terms-and-backcheck.md`.

## Output

* Deliver the translation first, alone, in the source's format (Markdown, LaTeX, plain text). No preamble or sign-off.
* Only if needed, add a short note after it (resolved ambiguities, suspected source errors, competing terms, a glossary for long texts) in the user's language.
* For files, keep the original unchanged unless asked, and name the new file with a language suffix (`manuscript.zh-TW.md`, `manuscript.en-US.md`, `manuscript.ja.md`).
* Do not translate code, paths, commands, or data values.
