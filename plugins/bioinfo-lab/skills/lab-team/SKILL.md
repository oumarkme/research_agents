---
name: lab-team
description: 'Use before delegating or when planning multi-step work: which Claude Code built-in agents and forked skills fit which job, and when delegation pays off. Guidance, not a rule.'
---

# Lab team

Delegation is optional. A subagent starts with no conversation history, returns only a summary, and spends its own tokens; multi-agent runs used about 15 times the tokens of a chat (Anthropic, 2025). Delegate when the work is parallel, breadth-first, or produces large intermediate output. Keep dependent steps, and anything that needs the conversation, in the main session.

This plugin ships no agents of its own. Use Claude Code's built-in ones and pass `model` and `effort` per call when a job needs a different tier:

* `Explore`: read-only search across many files, logs, or outputs; also log and job checks and test runs.
* `Plan`: an implementation or analysis plan before a large change.
* `general-purpose`: multi-step work in its own context, including web lookups (`current-methods-lookup`) and an independent review. `web-fetch` reads known URLs.
* `literature-review` and `long-analysis-job`: skills of this plugin that run in their own context. Pass the full task as the argument.
* `/advisor <model>`: an optional setting in your own Claude Code that lets Claude consult a stronger model before committing to an approach or declaring a task done. The advisor sees the whole conversation. `/code-review` reviews a code diff.

For an independent review of claims, numbers, or a blind variant classification, start a fresh `general-purpose` subagent with a strong model and give it only the specification, files, and evidence, never your conclusion. Do it once before results are reported or shared; skip it for exploratory work and for edits you have tested.

If a result is poor, retry with a sharper brief, then raise effort, then raise the model.

Briefing and checking returns: `agent-brief`. Example sequences: `team-playbooks`. Sources: `${CLAUDE_SKILL_DIR}/references/competency-map.md`, `${CLAUDE_SKILL_DIR}/references/design-basis.md`.
