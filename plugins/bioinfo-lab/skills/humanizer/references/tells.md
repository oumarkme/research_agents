# Tells, ranked by evidence

Rank matters. Fix tier 1 first, treat tier 2 as a prompt to look, and apply tier 3 as house style.

## Tier 1: measured in published text

| Tell | Evidence | Rewrite |
|---|---|---|
| Excess style words (verbs and adjectives such as *delves, underscores, showcasing, pivotal, intricate, crucial*) | 15.1 million PubMed abstracts; ratio to expected 2024 use: *delves* 28.0, *underscores* 13.8, *showcasing* 10.7 (Kobak et al., Science Advances 2025, read via arXiv 2406.07016). | Use the plain verb or the field's term. Check the date of `era-words.md`. |
| Present participial clause at the end of a sentence ("..., highlighting the need for ...") | 5.3 times the human rate in GPT-4o text (Reinhart et al., PNAS 2025, arXiv 2410.16107). | Split into two sentences, or cut the clause if it adds no fact. |
| Nominalizations ("the implementation of the filtering") | 2.1 times the human rate in GPT-4o text (same study). | Use the verb: "we filtered". |
| Several marker words in one passage | The words co-occur far more in 2024 than in 2022 (arXiv 2509.09596, abstract only). | One word proves nothing; a cluster is worth a full rewrite of the paragraph. |

## Tier 2: community-observed, no frequency data

From the Wikipedia field guide "Signs of AI writing", which says these are observations and not proof. Treat each as a prompt to ask whether the sentence says anything specific.

* "Not only X but also Y" and "it is not just X, it is Y".
* Rule of three used by reflex.
* Vague attribution ("studies show", "experts agree") with no citation.
* Inflated significance ("a testament to", "plays a pivotal role").
* *Serves as / stands as / acts as* where *is* works.
* A closing sentence that restates the paragraph; an opening that announces what the text will do.
* Paragraphs of near-equal length; every sentence the same length. The lint script measures the second.
* Polite filler and chat remnants ("Certainly", "I hope this helps", "Regenerate response").

## Tier 3: house style

These come from the lab's rules and have weak or contested evidence. Keep them for consistency.

* No em dashes. Rates differ by model and the sources conflict (arXiv 2603.27006, preprint), so this is a style choice. Use a comma, colon, parentheses, or two sentences.
* Sentence-case headings; no emoji; no bold lead-in on every bullet; no decorative bullets.
* Straight quotes in plain files.

## Not tells

* Agentless passives in Methods ("reads were filtered"): GPT-4o used them at about half the human rate.
* Words that are frequent in the field: *variant calling, read depth, heritability*. Repeat a technical term instead of swapping a synonym; synonym swaps create "tortured phrases" such as "fake neural organization".
* Ordinary words with high absolute counts (*potential, findings*).

## What to add

* Exact numbers, units, versions, parameters, sample sizes, file names, citations.
* The author's decision and its reason ("We dropped 3 accessions below 5× coverage").
* Plain connectors (*but, so, because, then*) in place of formal transitions.
* Short sentences next to longer ones, without forcing it. Say it once and stop.

Self-test: read each paragraph aloud. If a sentence sounds like a brochure, an essay, or a chatbot, rewrite it from the author's facts.
