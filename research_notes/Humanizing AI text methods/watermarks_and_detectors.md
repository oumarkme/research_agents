# AI text watermarks, invisible characters, stylistic fingerprints, and detectors: what exists and what it means for a researcher

Date of research: 2026-11-05. Labels: [F] = page fetched and read; [S] = search-result snippet only (not verified at source); [P] = preprint. Provider news from Aug-Sep 2026 is very recent and may change.

## 1. How text watermarks work and who deploys them in 2026

### Takeaway
Statistical watermarks (Kirchenbauer, Aaronson, SynthID-Text, Christ, Kuditipudi) bias or key the token sampling so that a key holder can run a hypothesis test later. Google has deployed SynthID-Text on Gemini since 2024; Anthropic announced in Aug 2026 that Claude models launched on or after 2 Aug 2026 carry a SynthID-Text-family watermark (EU AI Act driver); OpenAI built one but, per the latest source I found, has not shipped it.

### Cited Findings
- Kirchenbauer et al. (arXiv:2301.10226, 2023, ICML 2023) [F abstract]: before each token a randomized "green" set is chosen and green tokens are softly promoted; detection is a statistical test giving interpretable p-values, without model access. Abstract reports negligible quality impact on an OPT model, no numeric robustness result in the abstract. — [arXiv](https://arxiv.org/abs/2301.10226)
- Christ, Gunn, Zamir, "Undetectable Watermarks for Language Models" (arXiv:2306.09194, COLT 2024, PMLR 247) [S]: cryptographic notion; assuming one-way functions, watermarked and original models are computationally indistinguishable even to adaptive queriers. A theory construction, not a deployed system. — [PMLR](https://proceedings.mlr.press/v247/christ24a.html)
- Kuditipudi et al., "Robust Distortion-free Watermarks" (arXiv:2307.15593, TMLR 2024) [S]: maps a key-derived random sequence to samples; on OPT-1.3B and LLaMA-7B detectable from 35 tokens with 40-50% of tokens randomly edited; Alpaca-7B harder (about 25% of ~100-token responses detectable at p<=0.01). — [arXiv](https://arxiv.org/html/2307.15593v3)
- SynthID-Text, Dathathri et al., Nature 634:818-823, 2024, DOI 10.1038/s41586-024-08025-4 [S; Nature page redirected to a login, not fetched]: tournament sampling, modifies only sampling, no retraining, detection without the LLM; live test on nearly 20 million Gemini responses with no measurable quality loss in user feedback. — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11499265/)
- Google developer documentation [F]: SynthID Text is a logits processor applied after Top-K/Top-P using a keyed g-function; detector (Bayesian) returns watermarked / not watermarked / uncertain; "robust to some transformations" (cropping, a few word changes, mild paraphrasing); less effective on factual responses; confidence "can drop substantially" under heavy rewriting or translation; "not designed to stop determined adversaries". Open source in Hugging Face Transformers >=4.46.0. — [Google AI for Developers](https://ai.google.dev/responsible/docs/safeguards/synthid)
- Aaronson's 2022 proposal is the lineage Anthropic cites for the family (see below); I did not fetch Aaronson's own talk/blog. [S via Anthropic page]
- Anthropic, "How Claude's text watermark works", published 14 Aug 2026, updated 1 Sep 2026 [F]: models launched on or after 2 Aug 2026 produce watermarked text; it is "a version of the SynthID-Text approach"; only the source of randomness for choosing among candidate words is changed (key plus preceding words); "Nothing is added to the text and there are no hidden characters"; no extra tokens or cost; internal testing found "no impact" on content, creativity, readability. Applied globally "because we don't yet have a durable way to scope it by region". Older models are to be watermarked "over the coming months". Signed the EU Code of Practice on Transparency of AI-Generated Content (July 2026). Detection API in private preview for regulators, law enforcement, media, fact-checkers, independent researchers, educational organizations, EU civil society, and enterprises with Act obligations. Privacy: carries no identifying information, cannot be traced to a person, organization, or chat. — [Anthropic](https://www.anthropic.com/news/claude-text-watermark)
- Same Anthropic page, limits [F]: indicates only whether Claude likely wrote part of the text; cannot show human authorship or identify other AI systems; weak on short text; less signal in factual passages; code and exact-output answers generally not watermarked, code comments can be; "Light editing probably won't remove the watermark completely; a complete rewrite where every word is replaced will"; cannot distinguish "Claude wrote this" from "Claude heavily edited this"; human text only proofread by Claude has little watermark; Claude translations are watermarked. Images/files (.png, .jpg, .svg) get a C2PA credential in metadata. Notes that Pangram-type detectors work differently (stylistic tells).
- IEEE Spectrum (Sept 2026) [F]: Anthropic announced 11 August (the Anthropic page dates itself 14 Aug; minor discrepancy); Google "already applies a text watermark to Gemini"; OpenAI "has not yet added a text watermark but has said it plans to" and uses image and video watermarks; Anthropic declined to say how its method differs from SynthID-Text. Quotes Sadasivan that short text needs roughly 50-60% green words for good detection; Kirchenbauer: a watermark "wouldn't be detectable if there wasn't a change". — [IEEE Spectrum](https://spectrum.ieee.org/ai-watermark-text-anthropic-openai)
- OpenAI 2024 [S, secondary news, WSJ-originated]: OpenAI updated its May 2024 blog post to say it had built a text watermark but "continues to consider" it while researching alternatives (metadata). Reported reasons: possible disproportionate impact on non-native English users, circumvention by translation or rewording, and a survey where almost 30% of ChatGPT users said they would use it less. I did not find OpenAI's own current statement (gap). — [Engadget](https://www.engadget.com/openai-confirms-its-looking-into-text-watermarking-for-chatgpt-that-could-expose-cheating-students-223920531.html), [DailyAI](https://dailyai.com/?p=13739)
- EU driver [F via Anthropic and IEEE]: AI Act transparency marking applies to providers serving the EU from 2 Aug 2026 per both sources. Flag: I did not check the Act text or any later delay/omnibus changes.

### Inferences
- Answer to "is there a text watermark in Claude output": yes for Claude models launched on/after 2 Aug 2026 per Anthropic's own statement; it is statistical (word choice), not characters. Earlier Claude models: not at launch, being added later; status of any given model version should be checked against Anthropic's page.
- A watermark detector only gives a probability for a specific provider's key; a negative says little (other models, short text, factual text, heavy edits).
- Unwatermarked output from OpenAI or open-weight models is likely, but I could not confirm OpenAI's current status beyond a secondary source.

### Gaps
- Nature paper itself not fetched (paywall/login); Gemini deployment claim rests on PMC snippet and IEEE.
- No primary OpenAI statement for 2025-2026; no Aaronson primary; no verification of which Gemini surfaces are watermarked (Google docs name no products).
- Anthropic's algorithm differences from SynthID-Text are undisclosed.

## 2. Robustness: paraphrase, translation, editing, mixing

### Takeaway
All statistical watermarks are weak watermarks: they survive light edits and degrade as the fraction of rewritten tokens grows; paraphrase models, translation, and full rewrites defeat or sharply reduce them, and a theory result says strong watermarking is impossible under natural assumptions. There is no single "minimum rewrite" number; it depends on scheme, text length, and entropy.

### Cited Findings
- Sadasivan et al., "Can AI-Generated Text be Reliably Detected?" (arXiv:2303.11156, TMLR; v4 Jan 2025) [F abstract]: recursive paraphrasing lowers detection of watermark, neural, zero-shot, and retrieval detectors with small quality loss; watermarked LLMs can be spoofed (human text flagged); theory links best-detector AUROC to total variation distance between human and AI distributions. — [arXiv](https://arxiv.org/abs/2303.11156)
- Krishna et al., DIPPER (arXiv:2303.13408, NeurIPS 2023) [F abstract]: 11B paraphraser evades watermarks, GPTZero, DetectGPT, OpenAI classifier; DetectGPT 70.3% to 4.6% at 1% FPR. Proposed retrieval defense (provider stores generations): 80-97% detection of paraphrases at 1% FPR with 15M-generation database. — [arXiv](https://arxiv.org/abs/2303.13408)
- Zhang et al., "Watermarks in the Sand" (arXiv:2311.04378, ICML 2024, PMLR 235) [S]: under assumptions (quality oracle, perturbation oracle) strong watermarking is impossible even with private detection; generic attack removed Kirchenbauer, Kuditipudi, and Zhao schemes with minor quality loss; weak watermarks still useful, for example to avoid training on AI data. — [PMLR](https://proceedings.mlr.press/v235/zhang24o.html)
- Kuditipudi numbers above: tolerance of 40-50% random token edits on some models at 35+ tokens, but weaker on instruction-tuned output. [S]
- Provider statements above: Google, "heavy rewriting or translation" drops confidence; Anthropic, a complete rewrite where every word is replaced removes it; translation by Claude is itself watermarked. [F]
- Sadasivan quote: short texts need roughly 50-60% green words. [F, IEEE]

### Inferences
- Mixing: detection is a per-span or whole-text statistic, so a few watermarked sentences in a long human document dilute the score; this is why providers state detection needs sufficient length and why a negative is uninformative.
- Because paraphrase, translation, and light edits act differently by scheme, any "X% rewrite" figure would be scheme-specific; I found no reputable 2024-2026 source giving a general threshold, and I do not give an evasion recipe.
- Spoofing (Sadasivan) means a positive is also not proof of authorship by a specific party.

### Gaps
- Newer 2024-2026 robustness work (for example against SynthID-Text specifically) was not searched in depth; only the 2023-2024 core papers were verified.
- No fetched full text of Zhang et al., Christ, or Kuditipudi (abstract-level snippets).

## 3. Invisible Unicode characters and formatting residue

### Takeaway
Odd characters in LLM output are real but are not a deliberate watermark: Anthropic states its watermark adds no hidden characters, and the evidence for a character-level watermark in ChatGPT is anecdotal. The characters mostly come from typography habits, tokenization, and copy-paste/markdown pipelines. They are trivially visible to checks and are separate from the statistical watermark, which survives their removal.

### Cited Findings
- Anthropic: "Nothing is added to the text and there are no hidden characters." [F] — [Anthropic](https://www.anthropic.com/news/claude-text-watermark)
- A commercial detector vendor blog and Reddit threads (Apr 2025, anecdotal) report U+202F narrow no-break space, U+200B zero-width space, em dash U+2014, curly quotes in ChatGPT-family output (o3, o4-mini); the vendor itself says they are not for watermarking; a blog attributes them to training artifacts. No OpenAI statement found. [S, low quality, vendor interest] — [Originality.ai](https://originality.ai/pt/blog/invisible-text-detector-remover)
- C2PA 2.3 lists plain text among manifest-carrying types; the third-party c2patxt package implements this with Unicode variation selectors appended to text, so an explicit provenance mark in text would be invisible characters, but absence proves nothing and stripping removes it. [S, third-party docs] — [PyPI c2patxt](https://pypi.org/project/c2patxt/), [C2PA](https://c2pa.org/the-c2pa-launches-content-credentials-2-3-and-celebrates-5-years-of-impact-across-the-digital-ecosystem/)

### Inferences
- Practical checks (my own standard-tool suggestions, not from a cited source). Report characters rather than guess:
  - `grep -nP '[\x{200B}-\x{200F}\x{2028}-\x{202F}\x{2060}-\x{2064}\x{FEFF}\x{00A0}\x{00AD}\x{2011}\x{FE00}-\x{FE0F}]' file.txt` (GNU grep with PCRE; U+E0000 tag block can be added).
  - `hexdump -C file.txt | grep -E 'e2 80 (8b|8c|8d|af)|c2 a0|ef bb bf'` for the UTF-8 byte forms.
  - Python: `import unicodedata as u; [(i, hex(ord(c)), u.name(c, '?'), u.category(c)) for i, c in enumerate(s) if u.category(c) in ('Cf','Zs','Cc') and c not in ' \n\t']`; normalize with `u.normalize('NFKC', s)` (converts NBSP and U+202F to a plain space and U+2011 to a hyphen) and then drop Cf characters.
  - Curly quotes and em dashes are ordinary visible typography; replace only if the journal style requires.
- Removing these characters is hygiene (LaTeX and diff tools choke on them), not removal of a statistical watermark.

### Gaps
- No authoritative source on why specific models emit U+202F or U+200B; no independent study quantifying frequency.

## 4. Stylistic fingerprints and classifier detectors

### Takeaway
Classifier detectors read style, not a key, so they are probabilistic, vendor-dependent, and biased against some human writers. Independent evidence is mixed: a few commercial tools look good in controlled benchmarks, but older tools failed, and institutions generally refuse to treat scores as proof.

### Cited Findings
- Liang et al., Patterns 2023 (arXiv:2304.02819) [F abstract]: GPT detectors consistently misclassify non-native English writing as AI-generated; simple prompting that raises linguistic variety reduces the bias and also evades detectors; authors caution against use in evaluative and educational settings. — [arXiv](https://arxiv.org/abs/2304.02819)
- OpenAI AI Classifier, launched 31 Jan 2023, withdrawn 20 Jul 2023 for "low rate of accuracy"; reported 26% true-positive and 9% false-positive on its challenge set. [S, news summaries of OpenAI's note] — [Search Engine Land](https://searchengineland.com/openai-ai-classifier-no-longer-available-429912)
- RAID (Dugan et al., ACL 2024, arXiv:2405.07940) [S]: 6M+ generations, 11 models, 8 domains, 11 attacks; detectors easily fooled by adversarial attacks, sampling changes, repetition penalties, unseen models. A 2025 shared task on RAID reported some systems above 99% at 5% FPR. — [arXiv](https://arxiv.org/abs/2405.07940)
- Jabarian and Imas, BFI Working Paper 2025-116 (Aug 2025; not peer reviewed) [S]: of Pangram, Originality.ai, GPTZero, RoBERTa, only Pangram met a 0.5% false-positive cap without losing detection power. Pangram's "1 in 10,000" and robust-to-humanizer claims are company statements; a back-translation result (97% to 94%) is secondhand and unverified. No independent paraphrase-specific FPR found. — [BFI](https://bfi.uchicago.edu/wp-content/uploads/2025/09/BFI_WP_2025-116.pdf), [Pangram blog](https://www.pangram.com/blog/third-party-pangram-evals)
- Weber-Wulff et al. (arXiv:2306.15666, 2023) [S]: tested detection tools were unsuitable as evidence of misconduct. — [arXiv](https://arxiv.org/pdf/2306.15666)
- Institutions [S, secondary, verify at primary pages]: Vanderbilt, Pitt, Michigan State, Northwestern, UT Austin, Waterloo (Sept 2025) disabled Turnitin's AI detector; Yale and Johns Hopkins reportedly bar scores as sole evidence; Turnitin says about 98% accuracy and under 1% FPR for documents with more than 20% AI text, raised minimum length from 150 to 300 words, and has acknowledged higher document-level false positives than first stated. — [AI Weekly](https://aiweekly.co/alerts/yale-johns-hopkins-waterloo-pull-back-on-ai-detection-tools), [Georgetown CNDLS](https://cndls.georgetown.edu/ai/related-topics/)
- Anthropic itself distinguishes watermarking from stylistic detectors such as Pangram. [F]

### Inferences
- A style fingerprint (such as overused connectors or uniform sentence rhythm) is a property of the writing, so it persists through character cleaning and can be altered only by genuine rewriting; this is separate from any watermark and is the part that is legitimately improved by editing.
- Non-native-writer bias is the strongest equity argument; both Liang and OpenAI's own reported rationale point to it.

### Gaps
- No peer-reviewed independent 2025-2026 benchmark of GPTZero, Originality, Turnitin on current frontier-model output found; M4 and MAGE not retrieved.
- Institutional claims are from aggregators; primary university pages not fetched.

## 5. Provenance standards

### Takeaway
C2PA/Content Credentials is mature for images and files via signed metadata; for text it is only now specified (v2.3, via embedded Unicode variation selectors), is not broadly adopted, and is lost under copy-paste normalization or stripping.

### Cited Findings
- C2PA announced Content Credentials 2.3 listing plain-text documents among supported types. [S] — [C2PA](https://c2pa.org/the-c2pa-launches-content-credentials-2-3-and-celebrates-5-years-of-impact-across-the-digital-ecosystem/)
- Anthropic attaches C2PA credentials to .png/.jpg/.svg outputs; text uses the statistical watermark instead. [F]
- OpenAI reportedly favored metadata-based provenance over text watermarking (2024). [S]
- c2patxt docs: mark bound to NFC-normalized text; absence proves nothing; signature can outlast text changes. [S, third-party]

### Inferences
- For a manuscript pipeline, C2PA is unlikely to be present; the Anthropic statistical watermark is the relevant mechanism.

### Gaps
- No evidence found that any major chat product embeds C2PA text manifests today; the C2PA spec text itself was not read.

## 6. Ethics and policy framing

### Takeaway
Sources agree on disclosure rather than concealment: AI tools cannot be authors, and use should be declared. Editing prose so it reads better is acceptable; deliberately defeating a provider mark in order to conceal AI use from a venue or instructor that requires disclosure is a different act and is what the policies target. Honest practice is to disclose and to write your own text where a venue prohibits AI.

### Cited Findings
- Weber-Wulff et al. 2023 and Liang et al. 2023 both advise against detector scores as evidence. [S/F above]
- Publisher and ICMJE/COPE positions: AI cannot be an author; AI use must be disclosed; Nature reportedly asks authors to describe LLM use in Methods or acknowledgements, naming tool and purpose. [S, secondary aggregators (CASRAI, Enago); primary pages not fetched; one mirror had unverified placeholders] — [CASRAI](https://casrai.org/for-authors/ai-disclosure)
- COPE reportedly advises editors not to reject solely on suspicion of AI use (Enago summary, unverified). [S]
- Anthropic's watermark is positioned as probabilistic provenance, not proof; detection API access is restricted. [F]

### Inferences
- A researcher who wants text "without machine fingerprint" should separate three goals: (1) clean formatting residue (legitimate, item 3); (2) improve prose and voice by actually rewriting (legitimate, reduces stylistic tells, and incidentally dilutes any watermark as a side effect); (3) concealing disclosed-prohibited AI use (not endorsed; no recipe given here). Disclosure removes the problem: a declared use cannot be "caught".
- Because detection yields only a probability and can be spoofed, negative or positive results should not be treated as evidence by either side.

### Gaps
- Primary journal/ICMJE/COPE/Nature policy text not fetched; the researcher should check the target venue's current policy directly.
- No survey of discipline-specific bioinformatics or genetics journals.
