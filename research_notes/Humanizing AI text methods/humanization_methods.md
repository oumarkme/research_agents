# Humanizing LLM-written text: methods, evidence, and existing tools

Date of research: 2026-11-05. Labels: [FETCHED] = page or abstract opened and read by the researcher (via WebFetch, which summarizes with a small model; numbers below are as reported by that read of the abstract or page). [SNIPPET] = from search-result summaries only, not verified against the source. [PREPRINT] = arXiv or working paper, not peer reviewed. [VENDOR] = marketing or competitor claim.

## 1. How well does each approach lower detectability and, separately, change quality?

### Takeaway
Paraphrasing, especially detector-guided paraphrasing, lowers detector scores sharply, with only "slight" quality loss as judged by the attack authors themselves. Prompt-only style instructions and few-shot author samples help much less and are less well measured. Detection evasion and quality are separate axes: evasion numbers say nothing about whether the text is better, and independent quality evidence is thin.

### Cited Findings
- DIPPER paraphrasing (Krishna et al., NeurIPS 2023) dropped DetectGPT detection from 70.3% to 4.6% at a 1% false-positive rate; GPTZero, OpenAI classifier, and watermarking were also evaded (no figures in the fetched abstract). A retrieval defense (searching a database of prior generations) caught 80% to 97% of paraphrased outputs at 1% false positives on human text. [FETCHED abstract] — [arXiv 2303.13408](https://arxiv.org/abs/2303.13408)
- DIPPER human evaluation: three native-English teachers/editors rated semantic fidelity on 60 pairs at lexical-diversity settings L20/L40/L60; scores were not retrieved. Related paraphrase literature says meaning preservation gets harder as diversity rises. [SNIPPET] — [arXiv 2303.13408 PDF](https://arxiv.org/pdf/2303.13408)
- Recursive paraphrasing (Sadasivan et al., TMLR, arXiv v4 Jan 2025): OPT-13B watermark detection fell from about 99.8% to 9.7% after five rounds, and below 50% after two; DetectGPT AUROC fell from 96.5% to 25.2%; the retrieval detector fell from 100% to below 60% after five rounds. Authors report only slight quality loss by human study. Numbers come from secondary summaries. [SNIPPET] — [arXiv 2303.11156](https://arxiv.org/abs/2303.11156v4)
- Adversarial Paraphrasing (Cheng, Sadasivan, Saberi, Saha, Feizi; NeurIPS 2025): plain LLM paraphrasing changed true-positive rate at 1% FPR (T@1%F) by +8.57% on RADAR and +15.03% on Fast-DetectGPT (i.e., it made detection easier in those cases, per the abstract wording "raised"). Detector-guided paraphrasing (guided by OpenAI-RoBERTa-Large) cut T@1%F by 64.49% on RADAR and 98.96% on Fast-DetectGPT, and by 87.88% on average across detector families (neural, watermark, zero-shot). Quality: "mostly slight degradation" (authors' claim). [FETCHED abstract] — [arXiv 2506.07001](https://arxiv.org/abs/2506.07001)
- Simple prompt rewriting changes detector outcomes in both directions: asking ChatGPT-4 to "Enhance the word choices to sound more like that of a native speaker" reduced false flags on TOEFL essays by non-native writers; asking it to "Simplify word choices as if written by a non-native speaker" raised misclassification of US 8th-grade essays from 5.19% to 56.65% on average (the second experiment targets human text, so it shows detector fragility, not humanizing). Mechanism proposed: perplexity-based detectors react to low linguistic variability. [SNIPPET] — [arXiv 2304.02819](https://arxiv.org/html/2304.02819v3) (Liang et al., Patterns 2023)
- Few-shot author imitation: with five real-author samples in the prompt, one write-up reports Originality.ai missed 18%, GPTZero 11%, Pangram 10% of 297 imitation passages. This is a secondary blog write-up; sample per cell is small. [SNIPPET] — [ai2.work summary](https://ai2.work/blog/ai-detectors-miss-18-of-style-mimicked-text-new-study-finds)
- "Catch Me If You Can? Not Yet" (arXiv 2509.14543, 2025): LLMs imitate formal domains (news, email) better than informal ones (blogs, forums); few-shot output remained largely detectable by GPTZero; adding one human-written snippet raised evasion. [SNIPPET, PREPRINT] — [arXiv 2509.14543](https://arxiv.org/html/2509.14543v1)
- Style-fidelity study (arXiv 2509.24930): few-shot prompting gives up to 23.5x higher style-matching accuracy than zero-shot, yet outputs are less perplexing than human essays, so style match does not equal human-like unpredictability. [SNIPPET, PREPRINT] — [arXiv 2509.24930](https://arxiv.org/abs/2509.24930v1)
- "Beating the Style Detector" (arXiv 2605.02620): an agent given detector feedback over iterations flipped held-out mimics to the human side. Only excerpts seen. [SNIPPET, PREPRINT] — [arXiv 2605.02620](https://arxiv.org/pdf/2605.02620.pdf)
- Humanizer-tool market study (19 tools; Pangram authors, GenAIDetect workshop at COLING 2025, arXiv 2501.03437): off-the-shelf detectors fail on humanized text; the authors' retrained detector generalizes across humanizers; they also assess faithfulness qualitatively. The abstract gave no numbers. A secondary source says GPTZero fell from about 99.7% to about 60%; not verified. Authors are a detector vendor, so treat robustness claims as self-reported. [FETCHED abstract; numbers SNIPPET; VENDOR-authored] — [arXiv 2501.03437](https://arxiv.org/abs/2501.03437)
- Competitor claim: GPTZero reports Pangram v3 had 50.2% AI recall on its own benchmark of 12+ paraphrasers. [SNIPPET, VENDOR] — [GPTZero blog](https://gptzero.me/news/detecting-ai-humanized-text-how-gptzero-stays-ahead/)
- Trained humans: five frequent-LLM-user annotators, voting, misclassified 1 of 300 articles (GPT-4o, Claude 3.5 Sonnet, o1-Pro), outperforming most commercial and open-source detectors including under paraphrase and humanizer evasion; occasional users were poor. Cues were "AI vocabulary" plus formality, originality, and clarity. [SNIPPET] — [ACL 2025, arXiv 2501.15654](https://arxiv.org/abs/2501.15654)
- Fine-tuning on human text and human post-editing: no study found that measured detector effect and quality together for these. See Gaps.

### Inferences
- Detector-guided paraphrase is the strongest known evasion method, but it optimizes against a detector score, not reader value; a lab skill aimed at quality should not copy it.
- Plain paraphrase is not reliably an evasion method (the +8.57% and +15.03% rises), and recursive paraphrase degrades meaning risk over rounds; both argue against rewrite-by-paraphrase for science text.
- The human-expert result suggests the residual tells live in originality, specificity, and formality, which prompt rules on vocabulary do not touch.

### Gaps
- No peer-reviewed head-to-head of prompt-based style rules ("write like a human", banned words) versus paraphrasers on detector score plus blind human quality ratings was found.
- DIPPER human-eval fluency and fidelity scores were not retrieved (appendix C.2 of 2303.13408).
- No controlled study of fine-tuning on human text for detector evasion was found.
- Recursive paraphrase numbers were not checked against the primary PDF.

## 2. Do banned tell-words just shift the tells? Do structure, rhythm, specificity matter more than vocabulary?

### Takeaway
Vocabulary tells are real and measurable, but the evidence that suppressing them merely moves the tells to other words was not found either way in what I could read. Structural and rhetorical features differ systematically between LLM and human text, and expert human detectors rely on more than words. Banning lists alone is therefore weak design.

### Cited Findings
- Excess-vocabulary study: 14 million PubMed abstracts (2010 to 2024) show a sudden rise of style words (for example "delves") after ChatGPT, implying at least 10% of 2024 abstracts were LLM-processed (conservative lower bound), up to 30% in some fields in a later version. Title changed in later versions to "...LLM-assisted writing in biomedical publications...". [SNIPPET] — [Kobak et al., arXiv 2406.07016](https://arxiv.org/abs/2406.07016v4)
- Antislop (arXiv 2510.15061, code MIT, sam-paech/auto-antislop): some slop patterns occur over 1,000x more often in LLM output than in human text; a backtracking sampler suppresses 8,000+ patterns while maintaining quality; plain token banning becomes unusable near 2,000 patterns; FTPO training gives about 90% slop reduction while maintaining or improving GSM8K, MMLU, and creative-writing results; DPO suppresses less and degrades writing quality and lexical diversity. The abstract does not say whether suppressed patterns are replaced by new over-represented ones (a paper research question, answer not read). [FETCHED abstract, PREPRINT] — [arXiv 2510.15061](https://arxiv.org/abs/2510.15061)
- Grammatical and rhetorical style: LLMs use nominalizations about 1.5 to 2 times the human rate; GPT-4o uses agentless passives at about half the human rate; instruction tuning appears to push an information-dense noun-heavy style and limits mimicry of other styles. The present-participle result comes only from secondary summaries. [SNIPPET] — [Reinhart et al., PNAS 2025, DOI 10.1073/pnas.2422455122; arXiv 2410.16107](https://arxiv.org/html/2410.16107v2)
- Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup) groups signs into vocabulary, structure and content (inflated significance, vague attribution to unnamed experts, rigid "Challenges and Future Prospects" sections), grammar ("serves as" for "is", "not just X, but Y", triads), formatting, and citations. It states that signs are observations not rules, many occur in human writing, fixing surface features can hide underlying problems such as fabricated content, human detection is near chance in one 2025 study, and detector scores are not valid deletion grounds. Only the first 100,000 of 243,468 characters were read. [FETCHED, partial] — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Expert annotators used AI vocabulary and also formality, originality, clarity (see Q1). [SNIPPET] — [arXiv 2501.15654](https://arxiv.org/abs/2501.15654)

### Inferences
- A banned-word list is a lagging indicator: the lists must be refreshed per model era (Wikipedia page itself sorts words by era), and substitution drift is plausible but unmeasured in the sources read.
- Design implication: spend rule budget on structure (stock contrasts, triads, closers, vague attribution), specificity (named entities, numbers, concrete method details), and sentence-length variation, and keep word lists short and secondary.

### Gaps
- No direct measurement of "ban word A, frequency of word B rises" for prompt-based banning was found. The Antislop RQ on replacement needs the full paper.
- Evidence on rhythm (burstiness) as a human-judged feature rather than a detector feature was not found.

## 3. What do scientific-writing style guides add that raises quality regardless of detection?

### Takeaway
Gopen and Swan's reader-expectation rules (topic position, stress position, subject-verb proximity, old-before-new) are a quality framework independent of detection, and they target exactly the structural weaknesses (diffuse emphasis, nominalization) that LLM text shows. Journal-specific guidance (Nature, Science) and plain-language evidence were not retrieved.

### Cited Findings
- Gopen and Swan, "The Science of Scientific Writing" (American Scientist, 1990): readers expect old information in the topic position and new or emphasized information in the stress position at the sentence end; subject and verb should be close; violated expectations make readers spend effort unraveling structure instead of content; misplaced old/new information is called the top problem in professional writing. Source text not retrieved; these are secondary summaries. [SNIPPET] — [mirror on win.tue.nl](https://www.win.tue.nl/~wstomv/quotes/science-of-scientific-writing.html), [AcaWiki](https://acawiki.org/The_Science_of_Scientific_Writing)
- Reinhart et al. find LLM text is noun-heavy with high nominalization, which Gopen and Swan's "put the action in the verb" rule directly counters. [SNIPPET] — [arXiv 2410.16107](https://arxiv.org/html/2410.16107v2)

### Inferences
- A skill can add checks that are quality rules rather than detector rules: verbs carry actions, one point per paragraph, stress position holds the new claim, define terms once.
- These are explicit and lintable only partly (nominalization suffix counts, sentence length); the rest needs a read-through pass.

### Gaps
- Nature and Science author guidance on style was not retrieved.
- Plain-language effect evidence in scientific writing (comprehension experiments) was not searched.
- Primary text of Gopen and Swan not read.

## 4. Existing humanizer skills and tools

### Takeaway
The open-source skills are prompt catalogs built on Wikipedia's Signs of AI writing, with a mark-draft-check pipeline and, in the version read, no scripts and no published effectiveness evidence. Commercial humanizers are paraphrasers with unverified marketing bypass rates; the only structured independent look found is one vendor-authored study and blogs.

### Cited Findings
- blader/humanizer SKILL.md v3.1.0, license MIT: 26 patterns ranked strongest first; patterns 1 to 5 justify an edit on one sighting, some marked "weak alone"; categories A staging instead of stating, B rhythm by rule (triads, repeated openings, dashes, stacked qualifiers), C inflation and borrowed authority (stock vocabulary, vague attribution, avoidance of "is/are"), D formatting, E leftovers (chatbot residue, cutoff disclaimers), F wrong reader. Pipeline: Mark, Draft, Check (read aloud, confirm nothing added or lost), Finalize. Rules: "do not add facts, names, numbers, or quotes"; no em or en dashes unless the sample uses them. Modes: pasted text returns draft, remaining patterns, final; file mode writes only final text and leaves code and links unchanged; embedded mode returns final only. No scripts mentioned; file size not stated. [FETCHED via summarizer] — [SKILL.md raw](https://raw.githubusercontent.com/blader/humanizer/main/SKILL.md)
- Forks (search snippets only, repos not opened): rahul21luhar, vs4848, jooray, wey-gu, lanxkk, rbaddam (claims 18 patterns, never changes technical terms), jpeggdev/humanize-writing (eight-pass process plus the Wikipedia patterns). Counts of 25 and 29 patterns appear in different forks. Catalog credited to WikiProject AI Cleanup (CC BY-SA 4.0); a detect-only mode is triggered by asking whether text looks AI-written. [SNIPPET] — [GitHub search results, e.g. jpeggdev/humanize-writing](https://github.com/jpeggdev/humanize-writing)
- Anthropic skill authoring guidance: name max 64 characters (lowercase, digits, hyphens; no "anthropic" or "claude"); description max 1,024 characters, third person, states what and when; keep SKILL.md body under 500 lines; references one level deep; reference files over 100 lines get a table of contents; prefer pre-made scripts for deterministic checks; validate-fix-repeat feedback loops; plan-validate-execute for fragile operations; build at least three evaluations before extensive documentation and test with Haiku, Sonnet, and Opus; use consistent terms; give a default, not many options. [FETCHED] — [Anthropic docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Commercial tools: Undetectable.ai, StealthGPT, QuillBot (usually a paraphraser rather than a humanizer), GPTHuman and others appear only in blogs and affiliate-style reviews. One blog cites an 87% average bypass against Turnitin, GPTZero, Copyleaks, Originality.ai; a Hugging Face "AI Humanizer Benchmarks" page ranks GPTHuman first (authorship and independence unclear); an independent non-peer-reviewed 2026 study reports the most resistant of 14 humanizers fell from 93% to 69% detector accuracy. All unverified. [SNIPPET, VENDOR/blog] — [DEV Community review](https://dev.to/manolo_dreamsdreams_43/best-ai-bypass-humanizers-tools-of-2026-tested-ranked-3a6a), [HF benchmarks](https://huggingface.co/AIHumanizerBenchmarks), [GradPilot](https://gradpilot.com/news/do-ai-humanizers-work)
- Detector benchmark: a University of Chicago working paper (BFI WP 2025-116) finds commercial detectors outperform open-source ones and notes robustness to StealthGPT varies by detector. Details not read. [SNIPPET, PREPRINT] — [BFI WP 2025-116](https://bfi.uchicago.edu/wp-content/uploads/2025/09/BFI_WP_2025-116.pdf)
- Grammarly Humanizer and Anthropic marketplace humanizer plugins: not surveyed (no sources retrieved).

### Inferences
- The blader design is a sound template: ranked rules, explicit "no new facts" guard, mode separation, file mode that edits only prose. Its weaknesses for science: no number/citation preservation script, no effectiveness evaluation, and a "no dashes" style rule that is a taste choice, not evidence.
- A plugin skill should add: a lint script (pattern counts, sentence-length spread, dash and stock-phrase counts), a preservation checker (below), and 3 or more evaluation cases per Anthropic guidance; keep SKILL.md under 500 lines with the pattern catalog in a one-level-deep reference file.
- Do not recommend any commercial tool: no independent evidence of quality preservation was found.

### Gaps
- No independent peer-reviewed evaluation of any Claude Code humanizer skill.
- Forks' contents, star counts, and licenses (other than blader MIT) not verified.
- Grammarly, QuillBot, and Undetectable.ai rule sets and pricing not documented from primary pages.

## 5. How do humanizers damage science, and what safeguards are recommended?

### Takeaway
Paraphrasers trade meaning preservation for diversity, and synonym-swapping tools produce "tortured phrases" that the Problematic Paper Screener flags. LLM rewriting also corrupts references and numbers. Recommended safeguards are mechanical: diff every number, identifier, and citation against the original, and verify references against databases.

### Cited Findings
- Tortured phrases (Cabanac, Labbé, Magazinov, arXiv 2107.06751 for the 2021 preprint): odd synonym substitutes for standard terms, for example "fake neural organization" for "artificial neural network", from free rewriting websites. The screener uses fingerprint queries (276 tortured phrases found 1,694 problematic papers in the earlier reported set), now checks about 130 million papers weekly, and has supported more than 1,000 retractions. A 2025 Peer Review Congress regex detector flagged 2,455 Hindawi articles with 58% overlap with the screener. [SNIPPET] — [Peer Review Congress abstract](https://peerreviewcongress.org/abstract/screening-articles-for-tortured-phrases-with-a-regular-expressions-based-detector), [Univ. Grenoble Alpes / The Conversation](https://univ-grenoble-alpes.fr/news/the-conversation/the-conversation-problematic-paper-screener-trawling-for-fraud-in-the-scientific-literature--1547580.kjsp)
- Meaning drift trade-off: higher lexical diversity in paraphrase makes meaning preservation harder (DIPPER lexical codes L20 to L60). [SNIPPET] — [arXiv 2303.13408 PDF](https://arxiv.org/pdf/2303.13408)
- Citation corruption: reported 2% to 6% of 2025 proceedings papers contain unverifiable citations and one study a 17.0% "phantom rate"; practitioner guidance notes LLM rewriting can transpose authors, garble titles, invent page numbers, and DOIs are error-prone. Named error types include semantic drift, exaggeration, minimization. No study specifically of humanizers. [SNIPPET] — [arXiv 2602.05930](https://arxiv.org/pdf/2602.05930.pdf), [arXiv 2605.27700](https://arxiv.org/pdf/2605.27700), [third-bit.com](https://third-bit.com/aida/communicate/)
- Wikipedia: surface fixes can hide fabricated or unsupported content; its AI-writing sign list includes invalid DOIs and DOIs pointing to unrelated articles. [FETCHED, partial] — [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Disclosure: secondary sources say Nature exempts AI-assisted copy editing from disclosure but requires Methods documentation of other LLM use; ICMJE and individual journals differ (JCI requires disclosure of all AI use). Primary policy pages not read. [SNIPPET, low-quality aggregators] — [Kennesaw State summary](https://www.kennesaw.edu/research/ai-disclosure.php), [manusights](https://manusights.com/blog/nature-ai-policy)

### Inferences
- Recommended safeguards (design, not from a single source): (1) extract all numbers with units, p-values, gene and variant names, accession IDs, and citation keys before and after, and fail on any difference; (2) forbid rewriting inside citation, math, code, and table blocks; (3) show a word-level diff for human review; (4) never let the model add or reformat references; verify any reference changes against Crossref or PubMed; (5) run a tortured-phrase list check on output; (6) rewrite at sentence level without synonym-forcing, so no lexical-diversity pressure.
- A "humanizer" for manuscripts should be an editor that removes tells and adds author-supplied specifics, not a paraphraser.

### Gaps
- No empirical measurement of number or citation alteration rates by humanizer tools was found.
- Cabanac primary papers not opened; figures above are from secondary pages.
- Current Nature, Science, and ICMJE AI policies need checking from primary pages.

## 6. Do readers and reviewers prefer or trust human-edited versus raw LLM text?

### Takeaway
The one study found (CHI 2026, preprint) suggests readers cannot tell versions apart, yet rate LLM-edited abstracts best and fully LLM-generated abstracts lowest. Evidence specific to peer reviewers and human-post-edited versus raw LLM text in science is sparse.

### Cited Findings
- "LLM or Human? Perceptions of Trust and Information Quality in Research Summaries" (Akpinar et al., arXiv 2601.15556, accepted CHI 2026): ML-expert readers rated human-written, LLM-generated, and LLM-edited versions of the same abstract; detection was near chance with high confidence; LLM-edited scored best on clarity, conciseness, trustworthiness; fully LLM-generated scored lowest; raw LLM text drew "information overload" and "empty technicality" comments; beliefs about LLM involvement shaped ratings. Read through secondary summaries and an arXiv HTML listing. [SNIPPET, PREPRINT] — [arXiv 2601.15556](https://arxiv.org/abs/2601.15556)
- Frequent LLM users detect AI text accurately while rare users do not (Q1), so reviewers' exposure matters. [SNIPPET] — [arXiv 2501.15654](https://arxiv.org/abs/2501.15654)

### Inferences
- "LLM-edited" here means an LLM edit of human text, not a human edit of LLM text; the best-rated condition keeps human content. This supports an author-content-first workflow.

### Gaps
- No study of human post-editing of raw LLM drafts in a scientific genre with blind quality ratings.
- No reviewer-level (peer review) trust studies found.

## Suggested design lessons (from the evidence above, flagged as inference)
- Two-pass: audit (flag tells ranked by strength) then minimal rewrite, then a check pass; matches blader pipeline and Anthropic feedback-loop guidance.
- Prioritize structure, specificity, and reader-expectation rules over vocabulary lists; keep vocabulary list short and dated by model era.
- Add scripts: lint (counts, sentence-length variance, stock phrases, tortured phrases) and a preservation diff (numbers, identifiers, citations, headings).
- Do not market or evaluate success by detector score; evaluate by blind human rating plus preservation checks (Anthropic: at least three evals, test on Haiku, Sonnet, Opus).
- Mention disclosure: check journal AI policy before submission.
