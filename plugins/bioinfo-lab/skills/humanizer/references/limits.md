# Limits and open points

Checked 2026-11-05.

## What the skill claims

* It reduces measured stylistic tells and formatting residue.
* It checks that numbers, identifiers, and citations did not change.
* It reminds the author to disclose AI assistance.

## What it does not claim

* No guarantee against any detector. Detectors misclassify non-native English writing as AI-generated (Liang et al., Patterns 2023; arXiv 2304.02819), and OpenAI withdrew its own classifier in July 2023.
* No detection or removal of statistical watermarks. A statistical watermark sits in word choice and leaves no character to delete. Providers say light edits probably leave it and a full rewrite weakens it. Editing changes it only as a side effect, so the skill neither promises nor measures that.
* It does not supply the author's specifics or check that a claim is true.
* Word lists decay as models change.

## Raw drafts may carry a provider mark

An Anthropic page dated 2026-08-14 (updated 2026-09-01) says Claude models launched on or after 2 August 2026 carry a version of SynthID-Text, with "no hidden characters". Google documents SynthID-Text for Gemini (Dathathri et al., Nature 2024, DOI 10.1038/s41586-024-08025-4). Treat raw drafts from recent models as possibly marked until the author has rewritten them in their own words, and disclose AI assistance where the venue asks.

## Unverified points

1. The Anthropic watermark page was read by one researcher only, and no second source confirms its details. IEEE Spectrum dates the announcement 11 August.
2. The 2 August 2026 EU AI Act date comes from Anthropic and IEEE Spectrum. The Act text and any delay were not checked.
3. OpenAI's current text-watermark status rests on 2024 news reports.
4. The primary policy pages of Nature, Science, MDPI, and Cell Press were not read.
5. No NSTC research-writing guideline and no NTUH policy were found.
6. Syntax and vocabulary effect sizes come from GPT-4o and 2024 PubMed text. No peer-reviewed study separates Claude 4.x or 5, GPT-5, or Gemini 3, and no sourced list of zh-TW tells exists.

Full source notes and the underlying report: `reports/Humanizing AI text methods.md` in the plugin repository.
