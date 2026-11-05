# Empirical stylistic and linguistic markers of LLM-generated text (scientific and biomedical focus)

Date compiled: 2026-11-05. Verification labels: [F] = abstract/page fetched and read in this session; [S] = search snippet only; [K] = from background knowledge, not re-checked this session (treat as unverified). Full-text PDFs of Kobak and Reinhart did not extract; their numbers come from the arXiv HTML versions [F]. The "Science Advances" and "Nature Human Behaviour" publisher pages were not read (403 or not fetched); journal DOIs come from search results/known records.

## 1. Excess words and phrases in PubMed and scientific abstracts

### Takeaway
Excess-vocabulary studies converge: after Nov 2022, style words (mostly verbs and adjectives such as "delves", "underscores", "showcasing", "crucial", "comprehensive") rose far above trend in biomedical and other scientific abstracts. Published ratios reach ~28x for "delves" (2024 vs extrapolated trend). Estimated LLM-processed share is a lower bound of ~13.5% of 2024 PubMed abstracts, with strong heterogeneity by field, country, and journal. These are indirect population-level markers, not per-document detectors.

### Cited Findings
- Kobak et al., Science Advances 2025 (DOI 10.1126/sciadv.adt3813; arXiv 2406.07016v5, preprint version read) analyzed 15,103,888 PubMed abstracts from 2010-2024 (24.8M passed filtering). Excess = observed 2024 frequency p vs expected q extrapolated from 2021-2022; ratio r = p/q, gap delta = p - q; excess word if delta > 0.01 or log10 r > (log10 2 / 4) * log10 p. [F, arXiv HTML] — [arXiv 2406.07016](https://arxiv.org/html/2406.07016v5)
- Same paper: top ratio words "delves" r = 28.0, "underscores" r = 13.8, "showcasing" r = 10.7; top gap words "potential" delta = 0.052, "findings" 0.041, "crucial" 0.037. [F] — [arXiv 2406.07016](https://arxiv.org/html/2406.07016v5)
- Same paper: 454 excess words in 2024 (343 unique lemmas), versus a peak of 190 in 2021 (Covid). Of 379 excess style words in 2024, 66% verbs and 14% adjectives; pre-2024 excess words were mostly content nouns (79.2% nouns). [F] — [arXiv 2406.07016](https://arxiv.org/html/2406.07016v5)
- Same paper: "common" marker set (10 words): across, additionally, comprehensive, crucial, enhancing, exhibited, insights, notably, particularly, within. A "rare" set of 291 style words (2024 frequency < 0.02) is in Fig. S6 (not reproduced). [F] — [arXiv 2406.07016](https://arxiv.org/html/2406.07016v5)
- Same paper: lower-bound LLM-processed abstracts in 2024 = 13.5% (average of 0.136 rare and 0.134 common sets); at least ~200,000 papers per year; about twice the Covid-word effect (delta 0.069). [F] — [arXiv 2406.07016](https://arxiv.org/html/2406.07016v5)
- Same paper, subgroups (lower bounds): computational fields about 0.20, range <0.05 to >0.40 across subcorpora; UK and Australia about 0.05 vs China, South Korea, Taiwan about 0.20; journals Sensors 0.25, Cureus 0.20, MDPI 0.21, Frontiers 0.20, Nature/Science/Cell 0.07, Nature family 0.10; male first/last authors 0.09 vs female 0.07-0.08; Chinese computation papers 0.41. [F] — [arXiv 2406.07016](https://arxiv.org/html/2406.07016v5). Note that lower bound varies with journal and country, so a country-level difference is not evidence of misconduct.
- Liang et al., Nature Human Behaviour 2025 (DOI 10.1038/s41562-025-02273-8; preprint arXiv 2404.01268, "Mapping the Increasing Use of LLMs in Scientific Papers"): 1,121,912 preprints/papers, Jan 2020-Sep 2024, arXiv, bioRxiv, Nature portfolio; fastest and largest growth in computer science, lower in mathematics and Nature portfolio; higher estimates for first authors who post more preprints, crowded areas, shorter papers. Press/aggregator figures: ~22% of CS abstract sentences, ~9.8% physics, ~7.8% mathematics; these specific numbers are secondhand and vary between preprint and journal versions. [S] — [search result](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf), [Tribune summary](https://www.tribuneindia.com/news/science-technology/computer-science-research-papers-show-fastest-uptake-of-ai-use-in-writing-analysis-finds)
- Liang et al., "Monitoring AI-Modified Content at Scale" (arXiv 2403.07183, ICML 2024): 6.5%-16.9% of peer-review text at ICLR 2024, NeurIPS 2023, CoRL 2023, EMNLP 2023 possibly substantially LLM-modified; higher with lower reviewer confidence and near-deadline reviews. Not the biomedical NHB paper. [F] — [arXiv 2403.07183](https://arxiv.org/abs/2403.07183)
- Gray 2024 (arXiv 2403.16887, preprint): keyword proxy in Dimensions full-text; at least 60,000 papers (>1%) published in 2023 were LLM-assisted; "commendable", "meticulous", "innovative" rose >30% on average 2023 vs 2022 (press summary); very few disclosed use. Later follow-up arXiv 2512.01560 argues >10% of 2024 papers. [S] — [arXiv 2403.16887](https://arxiv.org/abs/2403.16887), [coverage](https://www.computing.co.uk/news/4190311/meticulously-commendable-ais-fingerprints-recent-academic-papers)
- Geng & Trotta (arXiv 2404.08627, v2 Nov 2024): ~1M arXiv abstracts May 2018-Jan 2024; word-frequency shift calibrated against GPT-3.5 "revise" outputs; ~35% LLM-style share in computer science abstracts by Jan 2024 (their upper estimate); they caution the style need not mean direct LLM use and may spread via imitation by non-native writers. [S] — [arXiv 2404.08627](https://arxiv.org/html/2404.08627v2)
- PubMed term tracking ("Delving Into PubMed Records", PMC12679996, pmejournal.org, DOI 10.5334/pme.1929; journal and year taken from the URL, not verified): 27,501,542 PubMed records 2000-2024; 135 candidate terms vs 84 control phrases; 103 of 135 exceeded modified Z-score 3.5 in 2024; largest: delve, underscore, primarily, meticulous, boast; also commendable, showcase, surpass, intricate, tapestry, unlocking. Group effect beta = 0.655, p < 0.001. Data end 2024. [F] — [PMC12679996](https://pmc.ncbi.nlm.nih.gov/articles/PMC12679996/)
- Multi-database analysis (arXiv 2509.09596; Scientometrics 2026, DOI 10.1007/s11192-026-05601-5): 12 terms in six databases 2015-2024; 2022-2024 change: delve +1,500%, underscore +1,000%, intricate +700%; PMC full text (2.4M papers, 2021-Jul 2025): share of papers using "underscore" 6+ times up >10,000%, intricate +5,400%, meticulous +2,800%; co-occurrence of marker words rose (2024: underscore-pivotal r = 0.449, underscore-delve r = 0.311, vs ~0.03 and 0.02 in 2022); STEM grew more than social sciences/humanities. [F abstract] — [arXiv 2509.09596](https://arxiv.org/abs/2509.09596). Contradicts the idea that "delve" is already gone in full text through early 2025 (see Q4).
- Wikipedia page cites a drop of more than 10% in "is"/"are" in 2023 academic writing (original study not located here). [F as relayed by the Wikipedia page, original not checked] — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Mechanism: Juzek & Ward, COLING 2025 (arXiv 2412.11385): RLHF evidence for lexical overrepresentation is mixed; Llama experiment supports it, but a participant study did not show a preference for "delve" itself. The popular "Nigerian annotators" story was not found in the paper abstract/excerpts; treat as unverified. [S] — [arXiv 2412.11385](https://arxiv.org/html/2412.11385v1). Follow-up (arXiv 2508.01930, preprint) emulates the feedback procedure and reports participants systematically prefer variants with certain words ("delve", "intricate"). [F abstract] — [arXiv 2508.01930](https://arxiv.org/abs/2508.01930)
- Large-scale lexical vs syntactic drift: 21.36M abstracts 2020-2024 (arXiv 2504.12317, preprint): 2024 turning point with lexical complexity up and syntactic complexity down; stronger for authors from typologically distant languages; polishing experiments with LLMs reproduce it. [F abstract] — [arXiv 2504.12317](https://arxiv.org/abs/2504.12317)

### Inferences
- Verbs and adjectives of evaluation ("underscore", "showcase", "crucial", "comprehensive", "notably", "enhancing") are better markers than content nouns, and Kobak's method supplies per-word ratios usable as a blocklist for revision.
- Individual-word presence is weak evidence at the document level; a cluster (several markers co-occurring, as in the 2509.09596 correlations) is stronger but still not proof.
- Prevalence estimates differ by method (Kobak 13.5% lower bound, Liang and Geng up to 20-35% in CS); direct comparisons across studies are inappropriate.

### Gaps
- Official Science Advances and NHB pages were not fetched; Liang's field-wise numbers are secondhand.
- Full Kobak supplementary word lists (Fig. S6) not extracted. The `berenslab/llm-excess-vocab` GitHub repository holds them and should be fetched if a full list is needed.
- Geng & Trotta and Gray details come from search snippets only.

## 2. Syntactic and structural features

### Takeaway
Reinhart et al. (PNAS 2025) show instruction-tuned LLMs use present participial clauses, nominalizations, and phrasal coordination at multiples of human rates, and agentless passives at about half the human rate (GPT-4o); differences persist with size and are larger after instruction tuning. Evidence for burstiness, rule of three, negative parallelism, and em-dash frequency is much thinner and mostly non-peer-reviewed.

### Cited Findings
- Reinhart et al., PNAS 122 (2025), arXiv 2410.16107 (v2 Aug 2025): HAP-E corpus (8,290 human texts, 66,320 chunks; academic, news, fiction, spoken, blogs, TV/movie), CAP check corpus (9,615 texts), M4 external. Features follow Biber. [F, arXiv HTML] — [arXiv 2410.16107](https://arxiv.org/html/2410.16107)
- Present participial clauses: instruction-tuned models 2-5x human; GPT-4o 5.3x (Cohen's d = 1.38). Nominalizations: 1.5-2x; GPT-4o 2.1x (d = 1.23). "That"-clauses as subjects: GPT-4o 2.6x (d = 0.77). Phrasal coordination: GPT-4o 1.9x (d = 0.81). Agentless passives: GPT-4o about half the human rate. Clausal coordination avoided by GPT-4o but over-used by Llama 3 variants. [F] — [arXiv 2410.16107](https://arxiv.org/html/2410.16107)
- Word-level in GPT-4o (fiction-heavy prompts): "camaraderie" 162x, "tapestry" 155x (appears in 23% of outputs), "intricate" 119x, "underscore" 107x, "amidst" 100x (27% of outputs), "palpable" 95x. [F] — [arXiv 2410.16107](https://arxiv.org/html/2410.16107)
- Base Llama models are closest to human feature rates; instruction tuning widens divergence; larger size does not close the gap. Random forest: 93-98% pairwise human-vs-LLM accuracy; seven-way 66%; 4.2% LLM texts called human and 9.8% human texts called LLM; accuracy drops on external M4 data. [F] — [arXiv 2410.16107](https://arxiv.org/html/2410.16107)
- Kobak's 454 excess words are 66% verbs, consistent with participial and nominalized registers in 2024 abstracts. [F] — [arXiv 2406.07016](https://arxiv.org/html/2406.07016v5)
- Time-series study of preprints (Hubarava & Ineichen, arXiv 2610.26008, EMNLP 2026 accepted, preprint Oct 2026): after Nov 2022 average word length rose; formula-based readability fell; maximum dependency-tree depth and sentence-level depth variation fell (flatter, more uniform syntax); some lexical markers persist, others rise then recede. No effect sizes in abstract. [F abstract] — [arXiv 2610.26008](https://arxiv.org/abs/2610.26008)
- Em dash: Freeburg (arXiv 2603.27006, independent-author preprint): 12 models, 5 providers; em-dash rates from 0.0 (Llama) to 9.1 per 1,000 words (GPT-4.1 under suppression); persists after markdown is prohibited; present in base vs instruct comparison, so cause may predate RLHF; suppression instructions sometimes fail. [F abstract] — [arXiv 2603.27006](https://arxiv.org/abs/2603.27006). Secondary reports (Economist test, Graphite-type summaries) conflict on which model uses most (Economist: only Claude above human; others report GPT-4.1/GPT-5 at >2x a 3.14 per 1,000 baseline). [S, blogs] — [search result](https://blog.pebblous.ai/report/opus-5-5-em-dash-ai-tells-drift/en/)
- Perplexity: LLM text has lower perplexity; Binoculars (Hans et al., ICML 2024, arXiv 2401.12070) reports >90% of ChatGPT samples detected at 0.01% FPR, zero-shot, using contrast between two LLMs. [F abstract] — [arXiv 2401.12070](https://arxiv.org/abs/2401.12070). Lower perplexity of ChatGPT than humans on HC3 also reported. [S] — [survey arXiv 2309.07689](https://arxiv.org/pdf/2309.07689)
- Model fingerprints: Sun et al., ICML 2025 (arXiv 2502.12150): classifier identifies which of ChatGPT/Claude/Grok/Gemini/DeepSeek wrote a text with 97.1% accuracy; signal sits in word-level distributions, survives rewriting/translation/summarization; markdown contributes moderately. [S] — [arXiv 2502.12150](https://arxiv.org/pdf/2502.12150)

### Inferences
- A usable humanizing checklist grounded in measurements: reduce stacked "-ing" participial tails, convert some nominalizations back to verbs, prefer agent-named active sentences (but note that GPT-4o underuses agentless passives, so Methods-section passives are not an AI tell), vary syntactic depth.
- Type-token ratio, burstiness, and sentence-length variance are plausible but I found no peer-reviewed human-vs-LLM effect size for scientific text. The 2610.26008 result (declining depth variation) is the closest direct evidence.

### Gaps
- No empirical rates found for negative parallelism ("not just X, but Y"), rule of three, or paragraph uniformity (searches returned only commentary).
- Reinhart effect sizes for attributive adjectives not found in the text read.
- Em-dash frequency by model is contested and based on preprints/blogs.

## 3. Wikipedia "Signs of AI writing": empirical support vs folklore

### Takeaway
The Wikipedia page is a community-compiled field guide that explicitly says its signs are not proof. A subset has independent measurement; others (negative parallelism, rule of three, significance inflation) have no rate data I could find.

### Cited Findings
- Page categories (language, style, structure, markup, citations, chat leftovers) and its explicit caveat that signs are not proof; it lists vocabulary eras and says human writing is becoming more LLM-like. [F, first 100k of 243k characters read] — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Supported empirically: overused vocabulary (delve, underscore, showcase, intricate, tapestry, pivotal; Kobak, Liang, Reinhart, 2509.09596); present participial "-ing" tails as superficial analysis (Reinhart 2-5x, GPT-4o 5.3x); avoidance of simple copulas (Wikipedia cites 2023 study; original not located); markdown/formatting as model-specific (Sun et al.); em dashes (model-dependent, preprint-level, conflicting).
- Weak or no independent support found: negative parallelism, rule of three, "Despite these challenges" template sections, vague attribution ("experts argue"), inflated significance language. These are plausibly true but rest on editor observation. The only data-style discussions were blogs on "It's not X, it's Y" and argued detectors over-flag them. [S] — [commentary](https://news.lavx.hu/article/why-it-s-not-x-it-s-y-isn-t-the-problem-it-s-the-metrics-we-use-to-police-language)
- Citation-related signs (invalid DOIs, utm_source, unused named refs) are artifacts of tool use, not stylistic, and are verifiable by inspection (observed on page; no study).
- Wikipedia relays: experts identified about 90% of AI texts with 3.3% false positives; less experienced readers near chance; a German thesis study 57% AI / 64% human recognition. [F as relayed] — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

### Inferences
- For a humanizer rule set, rank rules: (a) measured vocabulary and participial/nominalization patterns; (b) measured formatting/em-dash habits per model; (c) folk structure patterns, applied lightly and labeled as heuristic.
- Because humans are adopting LLM-style words (Geng & Trotta, 2509.09596), a single marker is a weak signal.

### Gaps
- Remaining 143k characters of the Wikipedia page not read.
- No peer-reviewed frequency data for rule of three or negative parallelism located.

## 4. Drift across model generations (2023-2026)

### Takeaway
Marker sets turn over. Early GPT-3.5/4 tells (delve, intricate, tapestry) were extremely over-represented but have partly receded in some corpora after being publicized; other markers (underscore) kept rising, and newer eras emphasize participial phrases and shorter sentences. Evidence is largely observational and not model-attributed for Claude 4.x/5 or Gemini 2.x/3.

### Cited Findings
- Wikipedia's eras (community-compiled): 2023-mid-2024 (GPT-4): delve, intricate, tapestry, testament; mid-2024-mid-2025 (GPT-4o): align with, fostering, showcasing; mid-2025-mid-2026 (GPT-5): highlighting, showcasing, notability language; mid-2026 on: leverage, multifaceted, shorter sentences and more periods; Grok overuses "causal" and "empirical"; "delve" fell sharply in 2025. [F] — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Treat as folklore-level, not measured.
- A marked drop in several once-overused words, such as "delve", began soon after they were publicized in early 2024 (arXiv abstract study). [S, original not identified] — [search result](https://arxiv.org/html/2610.26008)
- Hubarava & Ineichen 2610.26008: some markers keep accelerating, others rise then recede, so no stable inventory. [F abstract] — [arXiv 2610.26008](https://arxiv.org/abs/2610.26008)
- Counterpoint: PMC full text through Jul 2025 shows "underscore" and "intricate" still rising, and "delve" growth to up to five uses per article between 2022 and 2025 in a subset. [S/F abstract] — [arXiv 2509.09596](https://arxiv.org/abs/2509.09596)
- COLING 2025 paper reports "delve" still overused but less in a newer model. [S] — [aclanthology](https://aclanthology.org/2025.coling-main.426.pdf)
- Korean journal abstracts (Lee, arXiv 2609.07447, working paper, Sep 2026): 398,296 abstracts, 2018-Aug 2026; no 2023 shift, onset late 2024, rise through 2025, flattening mid-2026; "suggest" (sisahada) in 21.4% of 2026 abstracts vs 5.3% expected; marker turnover consistent with successive model generations; English abstracts of the same articles show the excess about a year earlier. [F abstract] — [arXiv 2609.07447](https://arxiv.org/abs/2609.07447)
- Em-dash rate differs by model and version; reports say it rose with GPT-4o and later fell in some newer Claude releases (blog-level, conflicting). [S] — [Pebblous](https://blog.pebblous.ai/report/opus-5-5-em-dash-ai-tells-drift/en/)

### Inferences
- Any fixed word list decays; a humanizer should key on structure plus a regularly refreshed list, and ideally test against the target journal's current excess words.
- Writers who avoid listed words create a new signal (Kobak style gaps), so avoidance alone is not "human".

### Gaps
- No peer-reviewed study that separates GPT-5, Claude 4.x/5, or Gemini 2.x/3 vocabulary in scientific writing was found.
- Direct 2025-2026 PubMed excess-vocabulary updates were not located.

## 5. Chinese (zh-TW, Mandarin) and non-English scientific text

### Takeaway
Evidence on zh-TW-specific LLM tells is thin. Cross-lingual patterns (more nouns, longer sentences, lower perplexity) are shown on HC3; Taiwan-vs-mainland term leakage is documented by benchmarks but not as a style measurement of generated text.

### Cited Findings
- HC3-based analysis (Guo et al., as summarized in a 2023 detection survey, arXiv 2309.07689): ChatGPT uses more nouns (English 21.1% vs 18.7% human; Chinese 27.5% vs 26.0%), longer sentences, more determiners/conjunctions, more neutral sentiment; lower perplexity. [S] — [arXiv 2309.07689](https://arxiv.org/pdf/2309.07689)
- Weibo comments (Li & Zhang, CCL 2025): stylometric feature set with a self-attention classifier, F1 91.8% for detecting AI short comments; short-text detection remains hard. [S] — [ACL Anthology](https://preview.aclanthology.org/fix-8040/2025.ccl-1.64)
- SC-TC-Bench (Lyu et al., FAccT 2025, arXiv 2505.22645): 11 LLMs; in the regional term task most models favored Simplified-Chinese usage; in the name task they favored Traditional Chinese names; attributed to training data, script preference, tokenization. [S] — [arXiv 2505.22645](https://arxiv.org/abs/2505.22645)
- TMMLU+ (arXiv 2403.01858) reports Simplified-Chinese-trained models outperform Traditional ones at the same size by at least 19% on a Taiwan knowledge benchmark; TMLU notes some Simplified characters remain in a Taiwan-tailored set. [S] — [arXiv 2403.01858](https://arxiv.org/html/2403.01858v3)
- A COSCUP 2026 talk (zhtw-mcp) describes LLM zh-TW output mixing zh-CN vocabulary, Simplified phrasing, inconsistent punctuation, and unstable technical terms, with an MCP checker. Practitioner source, not peer-reviewed. [S] — [COSCUP 2026](https://pretalx.coscup.org/coscup-2026/talk/7VSVUT.ics)
- Non-English scientific text: Korean abstracts show the LLM register shift (2609.07447, above); first/last authors in China, South Korea, Taiwan have higher Kobak lower bounds (~0.20) than UK/Australia (~0.05). [F] — [arXiv 2406.07016](https://arxiv.org/html/2406.07016v5)

### Inferences
- For zh-TW output, a rule-based check for mainland vocabulary (for example software/information/network terms), punctuation (full-width), and character set is justified by the benchmarks and talk, but concrete term lists need a sourced Taiwan glossary (for example National Academy for Educational Research terminology) before use.
- English markers do not translate one-to-one; translated Chinese likely retains calqued participial/nominalized patterns, but no source tested this.

### Gaps
- No peer-reviewed list of zh-TW LLM lexical tells, and no Chinese-language excess-vocabulary study for Chinese scientific abstracts, was found.
- SC-TC-Bench and Weibo details are snippet-only.

## 6. Can human experts spot LLM text?

### Takeaway
Frequent LLM users are highly accurate (majority of five annotators: 1 of 300 articles wrong) and robust to paraphrase and "humanizer" tools, mainly via lexical clues plus higher-level cues. Accuracy is much lower for people without LLM experience.

### Cited Findings
- Russell, Karpinska & Iyyer, ACL 2025 (arXiv 2501.15654): 300 non-fiction English articles (human vs GPT-4o, Claude, o1); hired annotators gave verdicts with paragraph explanations; frequent LLM-using annotators did best without training; five-expert majority vote misclassified 1 of 300; outperformed most commercial and open detectors, including on paraphrased and humanized text. Cues: "AI vocabulary", formality, originality, clarity. Data and code released. [F abstract] — [arXiv 2501.15654](https://arxiv.org/abs/2501.15654)
- Wikipedia relays that less experienced participants were near chance and that another 2025 study found humans no better than chance. [F as relayed] — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Reinhart et al.: statistical classifier is highly accurate in-domain (93-98% pairwise) but drops on external data; 9.8% of human text falsely labeled LLM. [F] — [arXiv 2410.16107](https://arxiv.org/html/2410.16107)

### Inferences
- A false-positive rate near 3% to 10% means "sounds like AI" judgments applied to human text are common; any workflow that edits to evade detection should not be framed as proof of authorship.

### Gaps
- Specific cue frequency tables from Russell et al. not read (abstract only).
- Evidence for newer 2026 models (GPT-5, Claude 4.x/5) in expert detection was not found.
