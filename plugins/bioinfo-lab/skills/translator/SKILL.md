---
name: translator
description: 'Use for any translation of academic text between American academic English and another language (default pair: Taiwan Traditional Chinese, zh-TW): manuscripts, abstracts, captions, letters, READMEs.'
---

# Translator (academic English ⇄ any language)

Goal: the target text carries exactly the source meaning, nothing added or dropped, and reads as if a specialist wrote it in the target language. For files, the `writing` skill also applies to English text.

## Language pair

* Default pair: American academic English ⇄ Taiwan Traditional Chinese (zh-TW). English source with no stated target goes to zh-TW; Chinese source with no stated target goes to American English.
* Any other language: the user names it. Read `${CLAUDE_SKILL_DIR}/references/languages/<code>.md` if it exists (`zh-TW` ships). If not, follow `_template.md` in the same folder, state in one line which term and register choices you made, and continue. Do not ask unless the choice changes the meaning.
* A pair with no English side (for example Japanese to Korean): translate the same way, and say that the fidelity checks below were run on the source and target directly.

## Workflow (all steps mandatory)

1. Identify direction, register (manuscript, abstract, email, README), audience, and field. If the source is ambiguous, ask or state the chosen reading in one line.
2. List the terms, numbers, units, citations, abbreviations, and proper nouns, and fix one rendering for each. For a file, keep the fixed renderings in `glossary.tsv` beside the source (columns `source_term`, `target_term`, `note`; start from `${CLAUDE_SKILL_DIR}/templates/glossary.tsv`). Read it first if it exists. Record only decisions where you chose between renderings; do not list terms that simply stay in the source form.
3. Translate sentence by sentence, then restructure for the target language. For manuscripts, abstracts, and grants read `${CLAUDE_SKILL_DIR}/references/method.md`. Over about 1,500 words, translate section by section: give each section the glossary and a one-line summary of the previous section, and check each section before you move on.
4. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/check_translation.py <source> <target>`. It works for any pair. Fix every FAIL (DOI, URL, or number differs) and judge every WARN (citation, abbreviation, or sentence count). Then do the manual back-check below.
5. For files, run the humanizer pass and the `writing` lint script (`python ${CLAUDE_SKILL_DIR}/../writing/scripts/lint_prose.py <file>`). The lint script checks English and Chinese only; for another language, say that it was not run.

## Terms (all languages)

* Proper nouns stay in the original language: person names, institutions (keep an official English name), journals, gene and protein symbols, species (Latin, italic), cultivars, software, databases, versions, and identifiers.
* Technical terms follow the target language file. When no file exists, use the form that recent journals in the target language use for this field. If none is established, keep the English term.
* When unsure whether a word is technical, keep the source form. If the field has two accepted forms, use the one most frequent in the last five years of its journals, and verify (PubMed, HGNC, Gene Ontology, Sequence Ontology), not from memory.
* One source term, one target term. Keep the source's abbreviations and define them at first use as the target style requires. No coined terms or calques.
* Plain words and simple structure in both languages; no idioms or metaphors unless the source depends on one.

## Back-check

The script covers numbers, DOIs, URLs, citations, abbreviations, and sentence count. By hand, compare sentence order · units and identifiers · terms follow the fixed glossary · negations and qualifiers kept · claim strength unchanged · citations and proper nouns untouched · nothing added or dropped · the rules of the target language file · no sentence readable two ways · no AI-sounding phrasing.

## Output

* Deliver the translation first, alone, in the source's format (Markdown, LaTeX, plain text). No preamble or sign-off.
* Only if needed, add a short note after it: ambiguities resolved, suspected source errors, competing term forms, and a glossary for long texts, in the user's language.
* For files, keep the original unchanged unless asked, and name the new file with a language suffix (`manuscript.zh-TW.md`, `manuscript.en-US.md`, `manuscript.ja.md`).
* Do not translate code, paths, commands, or data values; translate comments only when asked.
