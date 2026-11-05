# Marker words by period

Checked 2026-11-05. Dated lists decay, so read the period before you use a word as evidence.

## 2023 to 2024 (measured)

Kobak et al. (Science Advances 2025; arXiv 2406.07016, read through the preprint) compared 15.1 million PubMed abstracts. Excess words in 2024 were mostly verbs (66%) and adjectives (14%). Largest ratios: *delves* 28.0, *underscores* 13.8, *showcasing* 10.7. The largest absolute gaps were *potential, findings, crucial*. At least 13.5% of 2024 abstracts were processed by a large language model (LLM), a lower bound. The full word list is in the authors' repository `berenslab/llm-excess-vocab`; it was not fetched for this skill.

The lint script also flags these:

*delve, tapestry, realm, underscore, showcase, foster, pivotal, vital, intricate, multifaceted, nuanced, comprehensive, seamless, leverage, harness, streamline, bolster, elucidate, shed light on, pave the way, testament, game-changer, holistic, synergy, myriad, plethora, notably, importantly, robust, navigate* (as a metaphor), and the transitions *Moreover, Furthermore, Additionally, In conclusion*.

## 2025 to 2026 (community-observed, not measured)

Wikipedia "Signs of AI writing" lists later waves: *align with, enhance, fostering, showcasing*, then *emphasizing* and *highlighting* as verbs for results, and in 2026 *leverage* and *multifaceted* with shorter sentences. The lint script flags *align with, emphasize, enhance, multifaceted*. No peer-reviewed study separates Claude, GPT-5 (Generative Pre-trained Transformer), or Gemini 3 vocabulary in scientific text.

A PubMed Central (PMC) full-text analysis (arXiv 2509.09596, abstract only) found *underscore* and *intricate* still rising through July 2025, while *delve* fell after it became widely known. A Korean abstract study (arXiv 2609.07447, working paper) reports the marker set turning over with model generations.

## Refresh recipe

1. Pull recent abstracts from the author's sub-field (PubMed, by year).
2. Compute word frequencies per year and the ratio of the latest year to a pre-2022 baseline, as Kobak et al. did.
3. Replace this file's lists, with the date and the corpus.
4. Test substitution drift: run the skill on its own outputs and compare the frequency tables before and after. No study has measured whether banning one word raises another.

Avoiding listed words leaves a gap in the word distribution, so word swaps alone do not make text read as human. Rewrite the sentence from the facts.
