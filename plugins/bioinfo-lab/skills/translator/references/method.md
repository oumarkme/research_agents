# translator: detailed rules

## 1. Fidelity

* Complete: every sentence, clause, number, qualifier, and citation in the source appears in the target. Do not summarize, merge, or omit; do not add explanation, evaluation, or background.
* Precise: keep the source's strength of claim. keep the verb strength (*show*, *suggest*, *may*, *associated with*) in the target language equivalents (see the language file); never upgrade association to causation or soften a finding.
* Keep scope words (*all, some, only, at least, approximately*), negation, quantifiers, comparators, and conditions exactly. Keep tense logic and modality.
* Keep numbers, units, P values, confidence intervals, sample sizes, versions, gene and variant notation (HGVS), and identifiers character for character.
* Keep the document's structure: headings, list order, paragraph breaks, table and figure references, citation positions. Citations (author names, years, titles) are never translated or reformatted except to the target style requested.
* If the source is wrong, unclear, or self-contradictory, translate it as written and flag the problem in a separate note to the user; do not repair it silently.

## 2. Restructure for the target language

* Follow the restructuring rules in `languages/<code>.md` for the pair. Use the target field's habitual phrasing for Methods, Results, abstracts, captions, and slides; do not carry over the source language's habits. Slides stay as fragments if the source is fragments.
* Ambiguity: the target must have one reading. If the target language forces a choice the source does not make (number, definiteness, scope, who did what), pick the reading the context supports, and list the choice in a note to the user when it matters.

## Long documents

* Split at section headings (Abstract, Introduction, Methods, Results, Discussion). Never split inside a paragraph.
* Pass each section three things: the text, `glossary.tsv`, and a one-line summary of the previous section. Do not pass earlier sections in full.
* After each section run `check_translation.py` on that section pair, then once on the whole file. A section-level FAIL is easier to fix than a file-level one.
* Keep one rendering per term across sections; if a later section needs a new decision, add it to the glossary and re-check earlier sections for the same term.
