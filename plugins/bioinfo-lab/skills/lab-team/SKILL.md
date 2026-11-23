---
name: lab-team
description: 'Use before delegating or when planning multi-step work: what the two agents and the forked skills are good at, and when delegation pays off. Guidance, not a rule.'
---

# Lab team

Delegation is optional. A subagent starts with no conversation history, returns only a summary, and spends its own tokens; multi-agent runs used about 15 times the tokens of a chat (Anthropic, 2025). Delegate when the work is parallel, breadth-first, or produces large intermediate output. Keep dependent steps, and anything that needs the conversation, in the main session.

* `assistant` (Haiku, low effort): cheap bulk work such as searches, public-ID lookups, log and job checks, and test runs.
* `reviewer` (Opus, high effort, read-only): independent review of code, claims, or a blind variant classification. Worth one call before results are reported or shared, because it did not produce the work; skip it for exploratory work and for edits you have tested.
* `literature-review` and `long-analysis-job`: skills that run in their own context. Pass the full task as the argument.
* All other expertise (statistics, breeding, variant interpretation, data stewardship, writing, figures, code) is in skills the main session loads.

If a result is poor, retry with a sharper brief, then raise effort (the main model may pass `effort` per call), then raise the model.

Briefing and checking returns: `agent-brief`. Example sequences: `team-playbooks`. Sources: `${CLAUDE_SKILL_DIR}/references/competency-map.md`, `${CLAUDE_SKILL_DIR}/references/design-basis.md`.
