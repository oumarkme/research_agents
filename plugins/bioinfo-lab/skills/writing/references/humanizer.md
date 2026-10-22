# Humanizer pass

Goal: the text should read as if a careful specialist wrote it by hand. Note that AI-text detectors are unreliable and cannot be guaranteed against; the standard here is the observable absence of the patterns below plus natural, specific, evidence-led prose.

Remove or rewrite:

* **Vocabulary tells**: *delve, tapestry, landscape* (as metaphor), *realm, underscore, highlight* (as a verb for results), *showcase, foster, pivotal, crucial, vital, intricate, multifaceted, nuanced, comprehensive, robust, seamless, leverage, harness, streamline, bolster, elucidate, shed light on, pave the way, in the era of, a testament to, ever-evolving, cutting-edge, game-changer, holistic, synergy, navigate* (metaphor), *myriad, plethora, notably, importantly, significantly* (non-statistical), *Moreover, Furthermore, Additionally, Overall, In summary, In conclusion, It is important to note, It is worth mentioning*. Use plain verbs and specific nouns instead.
* **Structure tells**: "Not only X but also Y"; "It's not just X, it's Y"; "serves as / stands as / acts as" for *is*; three-item lists used by reflex (rule of three); paired antitheses; sentence-final *-ing* clauses that add vague significance ("…, highlighting the importance of…"); a summary sentence that restates the paragraph; opening and closing paragraphs that announce what the text will or did do; every paragraph of the same length and shape; questions answered by the writer ("What does this mean? It means…").
* **Formatting tells**: em dashes (use a comma, parentheses, colon, or two sentences; at most one per page, none in short files); bold lead-in phrases in every bullet ("**Key point:** …"); Title Case or numbered-emoji headings (use sentence case); emoji; decorative bullets; curly quotes mixed with straight; excessive headings in short documents; bullet lists where a sentence would do.
* **Tone tells**: promotional or inflated language; vague attribution ("studies show", "experts agree", "recent research suggests") without a citation; hedging stacks; a balanced "on the one hand / on the other hand" ending with no verdict; polite filler ("Certainly", "Great question", "I hope this helps"); first-person narration of the writing process.
* **Content tells**: generic statements true of any paper; claims with no number; invented-sounding specifics; symmetrical pros and cons; "future work" boilerplate.

Rewrite with:

* **Specifics**: exact numbers, units, versions, parameters, sample sizes, file and sample names, citations. A sentence that could appear in any paper on any topic gets deleted or made specific.
* **Natural rhythm**: vary sentence length (short next to longer; but keep each sentence simple); vary how sentences begin; use contractions never in formal papers, sparingly in READMEs and notes; plain connectors (*but, so, because, then, also*) rather than formal transitions.
* **Author voice**: first-person *we* (or *I* in notes) for choices and findings; state decisions and their reasons ("We excluded 3 accessions with <5× coverage") instead of describing the process in the abstract.
* **Restraint**: say it once; stop when the point is made; no recap.
* For edits to existing text, keep the author's wording where it is correct; change only what breaks a rule.

Self-test before saving: read each paragraph aloud; if any sentence sounds like a brochure, an essay, or a chatbot, rewrite it. Then run the lint script; it flags the vocabulary, structure, and formatting tells above.
