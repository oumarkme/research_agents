# Evidence-based engineering practices for agent skills, subagents, and plugins (as of 2026-11-04)

Evidence labels: [P] primary source (vendor docs, peer-reviewed or arXiv paper); [M] measured, author's own small benchmark; [S] secondary or aggregator; [O] opinion. Most search results were snippets plus page fetches by a small model, so exact figures should be re-checked in the linked source before being quoted in a manuscript.

## Skill triggering: description wording, length, number of skills, and mandatory-load enforcement

### Takeaway
Triggering is the weakest link: skills often go unloaded, and the description is the only thing the model sees. Measured fixes that worked were (a) forcing a visible evaluation step via a UserPromptSubmit hook and (b) making the content passive (always in context). Instruction text such as "always invoke skill X" did not reliably work. No published study isolates the effect of the number of installed skills.

### Cited Findings
- Agents see only name and description at startup; the description "carries the entire burden of triggering." Guidance: imperative phrasing ("Use this skill when..."), describe user intent not mechanics, be "pushy" and list contexts where the user does not name the domain, keep to a short paragraph, hard limit 1024 chars in the open spec. [P, official guidance, not measured] — [agentskills.io optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)
- Agents only consult skills for tasks beyond what they can do alone; a trivial one-step request may not trigger a skill even with a perfect description. [P] — same page
- Recommended trigger-eval protocol: ~20 queries (8-10 should-trigger, 8-10 should-not, with near-miss negatives that share keywords), 3 runs per query, trigger rate threshold 0.5, 60/40 train/validation split, about 5 iterations, pick best by validation score, avoid adding keywords copied from failed queries (overfitting). Detection via `claude -p --output-format json` and a `Skill` tool_use check. [P] — same page
- Claude Code listing: `description` plus `when_to_use` are combined and truncated at 1,536 characters in the skill listing; put the key use case first. The listing is in context every turn. `disable-model-invocation: true` keeps the description out of context entirely (manual `/name` only) and blocks preloading into subagents. [P] — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- Skill-Use benchmark (arXiv 2608.04828, Aug 2026): best of 8 models reached Skill-Use score 0.613 (GPT-5.5 under Claude Code). Triggering and compliance are separate bottlenecks (Trigger 0.972 but Compliance 0.611 for the best model; some models trigger on only ~32% of tasks). Preloading full skill text raised trigger and SU, especially for weak native triggerers; once triggered, SU was about equal, so retrieval is the main bottleneck. Scores and rankings change with the harness (GPT-5.5: 0.613 Claude Code vs 0.503 Codex). [P, preprint] — [Hugging Face papers 2608.04828](https://huggingface.co/papers/2608.04828)
- Vercel (Jan 2026), Next.js 16 tasks: skill never invoked in 56% of cases; pass rate 53% with skill vs 53% baseline; explicit "use the skill" instruction in AGENTS.md raised trigger to 95%+ and pass to 79%; an 8 KB compressed docs index embedded passively in AGENTS.md reached 100%. Wording changes caused large unpredictable swings. [M, one vendor's benchmark] — [Vercel blog](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals) (figures confirmed via secondary summaries)
- Scott Spence sandboxed evals (Sonnet 4.5, `claude -p`, ~250 invocations, $5.59, 22 prompts x 2 runs, four Svelte skills): no hook 55%/50%; one-line reminder hook 59%/50% (no gain); forced-eval hook (inject "for each skill answer YES/NO, then act") 100%/100% with 0 false positives on 5 negatives; Haiku-classifier hook 100% but 4 of 5 negatives falsely activated; native `type: "prompt"` hook 55%/41%. Baseline by prompt style: prompts containing a skill keyword ~100%, generic phrasing 20-40%, conceptual/indirect ~0%. Earlier Haiku 4.5 synthetic run reported 84% vs 20%, not comparable. [M, small sample, one author, activation measured within 20 s with max-turns 1] — [Spence](https://scottspence.com/posts/measuring-claude-code-skill-activation-with-sandboxed-evals)
- Third-party description-optimization attempt (20 queries, 13 train/7 test, 3 runs): three description styles all scored 46.2% train / 42.9% test; precision 100%, recall ~46%; no rewrite beat the original. Lesson: description rewording can fail to move recall; the query set or the skill's need may be the issue. [M, single author, small] — [Sogl, dev.to](https://dev.to/danielsogl/skills-without-evals-are-just-markdown-and-hope-3a71)
- Anthropic's skill-creator description optimizer: ~20 synthetic prompts, half should-not-trigger, 60/40 split, best by held-out score. A third-party blog says improved triggering on 5 of 6 built-in document skills; I could not verify this against an Anthropic primary source. [S] — [smartscope blog](https://smartscope.blog/en/generative-ai/claude/skill-creator-eval-pipeline-guide/)
- Strands Agents SDK ships a SkillSelectionAccuracyEvaluator (judge model checks whether each loaded skill made sense for the task); skillvitals reports recall, false-fire rate, F1; a 2026 eval manual recommends four prompt classes: obvious positives, paraphrased positives, hard negatives, collision prompts that fit two skills. [S/tool docs] — [Strands](https://strandsagents.com/docs/user-guide/evals-sdk/evaluators/skill_selection_accuracy_evaluator/index.md), [skillvitals](https://github.com/contextjet-ai/skillvitals)
- Hooks vs instructions for mandatory loading: Spence found a reminder hook was acknowledged then ignored, while a forced-evaluation hook that requires a written decision per skill worked; Vercel found instruction-in-AGENTS.md raised trigger to 95%+ but remained wording-sensitive. [M] — sources above

### Inferences
- For "load skill X before doing Y" rules: instructions alone are likely to fail on indirect or conceptual prompts (0-40% in Spence's data). A UserPromptSubmit hook that injects a forced per-skill decision, or a PreToolUse hook that denies Write/Edit on a file type until the Skill call appears in the transcript, is the evidence-backed route; a hard gate is more deterministic than a reminder (this specific gate pattern was not found tested; inference).
- Content that must always apply (lab-rules, style rules) is better as passive context (CLAUDE.md or preloaded) than as a skill the model must decide to open (Vercel; Skill-Use preloading result).
- Keep descriptions short, trigger-first, with explicit "not for" boundaries; test with collision prompts since 24 skills overlap (writing/humanizer, plotting/slides, lab-rules/lab-team).

### Gaps
- No published measurement of trigger accuracy versus number of installed skills or description length found.
- Anthropic's own measured results for skill-creator description optimization were not found in a primary source.
- Evidence is mostly small N, single-author, and tied to specific models; model versions change behavior.

## Evals: writing, running, and A/B against a no-skill baseline

### Takeaway
Anthropic now ships first-party tooling: `claude plugin eval` (suite in `evals/`, 3 runs per case, automatic no-plugin baseline with Δ, CI gating) and skill-creator (with/without subagent pairs, blind comparison, description optimizer). Start with small suites of realistic prompts, a trigger grader plus an outcome grader, and report Δ versus baseline.

### Cited Findings
- `claude plugin eval`: each case = prompt + graders; each case runs 3 times by default and again with no plugin; reports WITH, W/OUT, Δ per case; case passes when score >= `--threshold` (default 1.0). Cost about cases x runs x 2 agent runs plus 3 judge calls per llm/baseline grader. Requires Claude Code v2.1.269+. `claude plugin eval init` drafts cases and graders; `--ablation none` halves cost while iterating. [P] — [Plugin evals docs](https://code.claude.com/docs/en/plugin-evals)
- Six grader types: `regex`, `tool_used`, `tool_order`, `file_exists` (free, computed from transcript/files), plus `llm` and `baseline` (judge model calls). No custom-code graders. Guidance: use regex over file contents for long outputs, keep llm graders for short outputs with concrete PASS/FAIL rubrics, pair one result grader with one process grader (`tool_used: Skill`), and suspect the judge when the skill fired but Δ is negative (re-run with `--judge-model sonnet`). `tool_used: Skill` graders are excluded from scoring in both arms to avoid inflating Δ. Common first finding: Δ near zero with the Skill grader failing = Claude is not choosing the skill; fix the description. MCP servers are mocked by default. [P] — same page
- Skill-creator in Claude Code runs a similar comparison with its own `evals/evals.json`; the two tools do not read each other's case files. [P] — same page
- Skill-creator spawns with-skill and without-skill subagents per test case, blind comparator agents, and says evals reveal when "uplift" skills are no longer needed because the base model passes without them. [S, ainews/mcpservers summaries] — [ainews](https://www.ainews.com/p/anthropic-introduces-built-in-evaluation-and-benchmarking-for-claude-agent-skills-to-improve-enterpr)
- Example A/B (author's @ngrx/signals skill): 5 tasks, 41 assertions, with vs without skill: 100% vs 84% (+16 pp); one task showed 0 uplift (trim candidate); cost of skill: +28% time, +62% tokens per run. Proposed CI gate at 95%. [M, one run per eval, one author] — [Sogl](https://dev.to/danielsogl/skills-without-evals-are-just-markdown-and-hope-3a71)
- Other tools surfaced (not verified in detail): Strands skill-selection evaluator, `skill-doctor` (community static linter for frontmatter, broken script refs, description collisions, and routing evals via `skill.evals.json`), `cc-plugin-eval` (community). [S] — [cc-plugin-eval](https://github.com/sjnims/cc-plugin-eval), [Red Hat skill evaluation guide](https://redhat-documentation.github.io/redhat-docs-agent-tools/contribute/evaluating-skills)
- Anthropic's multi-agent research team evaluated with ~20 real-usage queries first (large effects detectable at small N), an LLM judge with a rubric (factual accuracy, citation accuracy, completeness, source quality, tool efficiency; 0.0-1.0 and pass/fail in a single prompt), plus human testers who caught what automation missed (SEO content farms favored). [P] — [Anthropic engineering](https://www.anthropic.com/engineering/multi-agent-research-system)

### Inferences
- A minimal suite for bioinfo-lab: per skill 2 should-trigger + 2 near-miss negatives + 1 collision prompt; deterministic graders first (regex on outputs, lint script exit code, `file_exists` for figures, `tool_used` order), llm grader only for short rubric items.
- Run Δ for the skills most likely to be "uplift" only (writing, plotting); lab-rules content that the base model already follows will show Δ ≈ 0 and is a candidate to cut.
- Science-specific example eval suites for skills: none found (see Gaps).

### Gaps
- No public eval suite for scientific or bioinformatics skills was found in this pass.
- I did not read the skill-creator repo primary files or the agentskills.io "evaluating skills" page.
- `claude plugin eval` docs read only partly (62 KB page); judge reliability numbers not reported there.

## Context cost and instruction budget

### Takeaway
Skill descriptions are an every-turn tax; bodies load on demand and persist once loaded; Anthropic recommends SKILL.md under 500 lines. Research shows instruction-following degrades as instruction count grows and for mid-context content, but I found no measured per-token cost table for MCP tools or a CLAUDE.md length study.

### Cited Findings
- Descriptions are present every turn; body loads when invoked and stays; SKILL.md under 500 lines; after auto-compaction the most recent invocation of each skill is re-attached, first 5,000 tokens each, within a shared 25,000-token budget. Subagents with a `skills` field get full skill content injected at startup along with CLAUDE.md. [P] — [Claude Code skills docs](https://code.claude.com/docs/en/skills)
- Measured per-use cost of a loaded skill: +62% tokens and +28% time per run (one skill, ~12k extra tokens). [M] — [Sogl](https://dev.to/danielsogl/skills-without-evals-are-just-markdown-and-hope-3a71)
- IFScale (arXiv 2507.11538, NeurIPS 2025): 20 models, 10-500 simultaneous instructions; best frontier models only 68% at 500; three degradation patterns; bias toward earlier instructions; omission errors dominate. Task was keyword inclusion (a narrow task). [P] — [arXiv HTML](https://arxiv.org/html/2507.11538v1)
- Lost in the Middle (Liu et al., TACL 2024): accuracy highest when relevant information is at the start or end of context, drops when in the middle, and falls as context grows even for long-context models. Older models; check newer long-context models before relying on magnitudes. [P] — [ACL Anthology](https://preview.aclanthology.org/setup/2024.tacl-1.9)
- Vercel: compressing a 40 KB docs injection to 8 KB (~80% smaller) kept 100% pass in that benchmark. [M] — Vercel link above
- Anthropic: a tool-description-rewriting agent cut task time 40%; use distinct clear tool descriptions. [P] — [Anthropic engineering](https://www.anthropic.com/engineering/multi-agent-research-system)

### Inferences
- With 24 skills at ≤1,536 chars each, the listing could reach up to roughly 37k characters (my arithmetic; actual is lower if descriptions are short); trimming every description to 1-2 sentences and setting `disable-model-invocation: true` on rarely auto-needed skills reduces the every-turn tax.
- Preloading lab-rules into all 10 agents multiplies its size by every agent spawn; keep it short, put critical rules first and last (position effects), and move detail into on-demand references.

### Gaps
- No measured token costs for MCP tool definitions or typical CLAUDE.md sizes found; no study found of CLAUDE.md length versus adherence specifically. "Context rot" (Chroma) was not retrieved. Suggested next step: count tokens of our own listing with a tokenizer or `/context`.

## Multi-agent delegation, cost multipliers, and verification

### Takeaway
Multi-agent wins on breadth-first, parallelizable research when the task value pays for ~15x tokens, and loses on sequential or tightly coupled work. Failure is more often coordination and verification than model weakness. Evidence that reviewers anchored on author text miss errors is indirect.

### Cited Findings
- Anthropic: Opus 4 lead + Sonnet 4 subagents beat single-agent Opus 4 by 90.2% on an internal research eval; agents use ~4x chat tokens, multi-agent ~15x; token usage alone explains 80% of variance in BrowseComp (tokens, tool calls, model choice together 95%); poor fit where agents share context or have many dependencies, and for most coding tasks. Failure modes: 50 subagents for simple queries, duplicated work, endless search. Fixes: explicit effort-scaling rules (1 agent/3-10 calls for facts; 2-4 subagents for comparisons; 10+ for complex research) and detailed task briefs (objective, output format, tools, boundaries). [P, internal eval, vendor] — [Anthropic engineering](https://www.anthropic.com/engineering/multi-agent-research-system)
- Cognition "Don't Build Multi-Agents" (12 Jun 2025): share full traces, actions carry implicit decisions; recommends single-threaded agent. Illustrative and anecdotal, no benchmarks. [O] — [Cognition](https://cognition.com/blog/dont-build-multi-agents)
- MAST (Cemri et al., arXiv 2503.13657, NeurIPS 2025 D&B): 14 failure modes in 3 categories (system design, inter-agent misalignment, task verification), from 1600+ annotated traces over 7 frameworks; many failures stem from organization and coordination, not model limits; kappa 0.88. [P] — [arXiv](https://arxiv.org/abs/2503.13657v3)
- "Towards a Science of Scaling Agent Systems" (Google Research et al., arXiv 2512.08296): 180 configurations, 5 architectures, 4 benchmarks; multi-agent variants lost 39-70% on sequential reasoning (PlanCraft) but gained up to +81% on parallelizable finance tasks; independent agents amplified errors 17.2x vs 4.4x for a centralized orchestrator acting as validation bottleneck. [P, preprint; figures via Google blog/HF summary] — [Google Research blog](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)
- Huang et al. (ICLR 2024): LLMs cannot self-correct reasoning without external feedback; self-correction can degrade performance; multi-agent debate was inferior to self-consistency at equal response counts. External signals (code execution results) work. [P] — [arXiv 2310.01798](https://arxiv.org/abs/2310.01798v1)
- Judge bias: an EACL 2026 Findings paper reports that code judges that correctly flagged wrong code flipped to "correct" after an authority cue (comment saying an expert wrote it); self-preference bias in LLM judges is documented. [P] — [EACL 2026 Findings](https://preview.aclanthology.org/ingest-eacl/2026.findings-eacl.70.pdf), [Self-preference bias](https://arxiv.org/html/2410.21819v1)

### Inferences
- A reviewer subagent should get the artifact and the claim list but not the author's reasoning, and should be given executable checks (tests, recomputation, lint output) because intrinsic review without external signals is weak; this is consistent with, but not directly tested by, the cited papers.
- Delegate only for isolation, parallelism, or breadth; our "PI does thinking itself" rule matches Anthropic and Cognition guidance for coupled work. Add explicit effort-scaling rules and brief templates to lab-team.

### Gaps
- No benchmark found directly measuring reviewer error-miss rate when author reasoning is visible (anchoring); one title-level hit on "Anchoring Bias in LLM-as-a-Judge" (arXiv 2608.25869) was not read.
- No data on Haiku/Sonnet/Opus tier routing quality inside plugins.

## Hooks as guardrails

### Takeaway
Hooks are the harness-executed, deterministic layer, but reliability reports are mixed: exit code 2 is documented to block PreToolUse, yet user bug reports say some tools ran anyway. Test every guard hook.

### Cited Findings
- Official docs: PreToolUse exit code 2 blocks the tool call and shows stderr to Claude; other non-zero codes are non-blocking errors. [P] — [Claude Code hooks docs](https://docs.anthropic.com/en/docs/claude-code/hooks)
- Open issues report exit 2 not blocking Write/Edit or Bash in some versions (e.g. file created anyway; `git push` still ran). Status and fix versions not verified. [S, user bug reports] — [issue 13744](https://github.com/anthropics/claude-code/issues/13744), [issue 23284](https://github.com/anthropics/claude-code/issues/23284)
- Third-party note: exit 1 blocks nothing; JSON output is processed only on exit 0. Unverified against current docs. [S] — [Crosley](https://blakecrosley.com/blog/claude-code-hooks-explained)
- UserPromptSubmit forced-eval hooks raised skill activation to 100% in a small test (see triggering section). [M] — Spence link above
- `claude plugin eval` graders (`tool_used`, `tool_order`, `regex`) can be used to test that hooks and rules actually fire in a run. [P] — plugin evals docs

### Inferences
- Candidate hooks for bioinfo-lab (design suggestions, not tested here): PreToolUse on Write/Edit denying paths outside working dir and scratch; PreToolUse on WebSearch/WebFetch matching patient-data patterns (sample ID regex, genotype strings) with deny; PostToolUse on Write of prose files running the lint script and feeding failures back; PostToolUse on figure saves running the check script; Stop hook refusing to finish if a required lint/check has not run. Combine deny-hooks with permission rules as defense in depth because of the reported exit-2 inconsistencies; write hook tests (feed JSON on stdin, assert exit code).

### Gaps
- No published research-hygiene hook collections with measured reliability found; not checked whether the exit-2 issues are fixed in current versions.

## Prose quality: AI-text tells and word lists

### Takeaway
The strongest evidence for lint lists is population-level excess-frequency data from PubMed (Kobak et al., Science Advances 2025); style verbs and adjectives dominate. Word lists should be built from excess ratios, and flagged as lower-evidence for any single document.

### Cited Findings
- Kobak et al.: 15.1M English PubMed abstracts 2010-2024; excess-word method (observed 2024 vs counterfactual frequency); at least 13.5% of 2024 abstracts LLM-processed (lower bound), from <5% to >40% across subcorpora; of 379 excess style words in 2024, 66% verbs and 14% adjectives; examples: delves r=28.0, underscores r=13.8, showcasing r=10.7, crucial δ=0.037, findings δ=0.041, potential δ=0.052. Published in Science Advances 2025 (DOI 10.1126/sciadv.adt3813). [P] — [arXiv v5](https://arxiv.org/html/2406.07016v5), [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12219543/)
- Caveats from the authors: cannot separate direct LLM use from authors adopting LLM-favored words; corpus-level only, cannot identify individual texts; ChatGPT-era models. [P] — same

### Inferences
- Lint rules based on rare high-ratio words (delve, underscore, showcase, pivotal, intricate) are supported; common words (crucial, potential, findings) have a high absolute gap but are normal scientific vocabulary, so flag by density, not presence. Word lists age as models change; review annually against newer excess-vocabulary studies. Do not use lint hits as detection evidence about any person.

### Gaps
- I did not retrieve studies on structural AI tells (em-dash rate, triplets, hedging), detector reliability, or evaluations of humanizer tools. Full ratio table for the top 20-30 words was not extracted; fetch the paper's supplementary list to tighten the word list.

## Reproducibility for AI-assisted analysis

### Takeaway
I did not research this question in this pass beyond the evals material; no sourced findings.

### Cited Findings
- None collected. (Only adjacent point: Anthropic's team found human testers caught issues LLM judges missed, supporting human spot-checks of AI claims — [Anthropic engineering](https://www.anthropic.com/engineering/multi-agent-research-system).)

### Inferences
- A claim ledger is best verified with executable checks (recompute each number from a logged script) rather than by an LLM reviewer, per the self-correction and judge-bias evidence above (inference).

### Gaps
- Provenance logging standards (W3C PROV, RO-Crate, workflow provenance), claim-ledger practice, and notebook/workflow practices for AI-assisted analysis were not searched; needs a separate pass.
