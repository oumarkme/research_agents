---
name: translator
description: 'Use for any translation between Taiwan Traditional Chinese and American academic English: manuscripts, abstracts, captions, letters, READMEs. Technical terms stay in English.'
---

# Translator (繁體中文 ⇄ American academic English)

Goal: the target text carries exactly the source meaning, nothing added or dropped, and reads as if a specialist wrote it in the target language. For files, the `writing` skill also applies. For other language pairs, apply the same fidelity and term rules and say that the lint script checks only Chinese and English.

## Workflow (all steps mandatory)

1. Identify direction, register (manuscript, abstract, email, README), audience, and field. If the source is ambiguous, ask or state the chosen reading in one line.
2. List the terms, numbers, units, citations, abbreviations, and proper nouns, and fix one rendering for each. For a file, keep the fixed renderings in `glossary.tsv` beside the source (columns `source_term`, `target_term`, `note`; start from `${CLAUDE_SKILL_DIR}/templates/glossary.tsv`). Read it first if it exists. Record only decisions where you chose between renderings or kept a term unusual; do not list terms that simply stay in English.
3. Translate sentence by sentence, then restructure for the target language. For manuscripts, abstracts, and grants read `${CLAUDE_SKILL_DIR}/references/method.md`. Over about 1,500 words, translate section by section: give each section the glossary and a one-line summary of the previous section, and check each section before you move on.
4. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/check_translation.py <source> <target>`. Fix every FAIL (DOI, URL, or number differs) and judge every WARN (citation, abbreviation, or sentence count). Then do the manual back-check below.
5. For files, run the humanizer pass and `python ${CLAUDE_PLUGIN_ROOT}/skills/writing/scripts/lint_prose.py <file>`.

## Terms

* Technical terms stay in English, in Chinese text too: genome, assembly, long-read sequencing, heritability, GWAS, linkage disequilibrium, cross-validation. Never write 基因體, 組裝, 定序, 遺傳率, 變異, 表現型, 基因型, 全基因體關聯分析, and add no Chinese gloss or parentheses. This covers genetics, genomics, bioinformatics, statistics, breeding, machine learning, medicine, software, file formats, and metrics.
* Proper nouns stay in the original language: person names, institutions (keep an official English name), journals, gene and protein symbols, species (Latin, italic), cultivars, software, databases, versions, and identifiers.
* A Chinese source that uses a Chinese technical term: translating to English, use the field's standard English term (verify it); translating to Chinese, keep the English term.
* When unsure whether a word is technical, keep it English. If the field has two accepted forms, use the one most frequent in the last five years of its journals, and verify (PubMed, HGNC, Gene Ontology, Sequence Ontology), not from memory.
* One source term, one target term. Keep the source's abbreviations and define them at first use as the target style requires. No coined terms or calques.

## Language rules

* Chinese output: Taiwan Traditional Chinese only, never Simplified characters. Taiwan vocabulary (預設, 品質, 網路, 影片, 軟體, 資料, 程式, 伺服器, 解析度), full-width punctuation (，。、；：？！「」『』), consistent spacing between Chinese and Latin text, and English conventions for numbers with units (5 kb, 37 °C). Check with the lint script (OpenCC `s2twp`) before saving.
* English output: the `writing` rules (American spelling, active voice with "we", one idea per sentence, no bare This, no priority claims, correct tense, SI units).
* Plain words and simple structure in both languages; no idioms or metaphors unless the source depends on one.

## Back-check

The script covers numbers, DOIs, URLs, citations, abbreviations, and sentence count. By hand, compare sentence order · units and identifiers · terms follow the fixed glossary · negations and qualifiers kept · claim strength unchanged · citations and proper nouns untouched · nothing added or dropped · no Simplified characters or mainland terms (Chinese) · American spelling (English) · no sentence readable two ways · no AI-sounding phrasing.

## Output

* Deliver the translation first, alone, in the source's format (Markdown, LaTeX, plain text). No preamble or sign-off.
* Only if needed, add a short note after it: ambiguities resolved, suspected source errors, competing term forms, and a glossary for long texts, in the user's language.
* For files, keep the original unchanged unless asked, and name the new file with a language suffix (`manuscript.zh-TW.md`, `manuscript.en-US.md`).
* Do not translate code, paths, commands, or data values; translate comments only when asked.
