---
name: lab-team
description: 'Use before delegating or when planning multi-step work: what each agent is good at and when delegation pays off. Guidance, not a rule.'
---

# Lab team

Delegation is optional. A subagent starts with no conversation history, returns only a summary, and spends its own tokens; multi-agent runs used about 15 times the tokens of a chat (Anthropic, 2025). Delegate when the work is parallel, breadth-first, or produces large intermediate output. Keep dependent steps, and anything that needs the conversation, in the main session.

Agents (descriptions are in each agent's frontmatter): `assistant` (cheap bulk work: searches, public-ID lookups, log and job checks, test runs), `literature-reviewer`, `data-steward`, `translator`, `writer`, `figure-maker`, `bioinformatician`, `microbial-genomicist`, `evolutionary-genomicist`, `software-engineer`, `breeder`, `statistician`, `clinical-geneticist`, and `reviewer` (independent, read-only, Opus).

`reviewer` is worth a call before results are reported or shared, because it did not produce the work. Skip it for exploratory work and for edits you have tested.

If a result is poor, retry with a sharper brief, then raise effort (the main model may pass `effort` per call), then raise the model.

Roster with hand-offs: `${CLAUDE_SKILL_DIR}/references/roster.md`. Briefing and checking returns: `agent-brief`. Sequences for common workflows: `team-playbooks`. Sources: `${CLAUDE_SKILL_DIR}/references/competency-map.md`.
