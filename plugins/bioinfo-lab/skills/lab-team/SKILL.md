---
name: lab-team
description: 'Use before delegating to an agent or planning multi-step work: routing rule, agent roster with when not to delegate, and escalation order.'
---

# Lab team

## Default: route

The main session, as deputy PI, routes. Delegate by default: split the task, send each part to the best-matching agent, and integrate the returns. Work alone only when no agent fits or the step is trivial (one lookup, a one-line edit). A multi-agent run costs about 15 times the tokens of a chat (Anthropic, 2025), so give each agent a bounded task and a capped report. Run independent agents in one message, chain at most 3, and say in one line which agent you used.

Cost: send routine work with no judgment in it to `assistant` (Haiku) first: searches, public-ID lookups, log and job checks, test runs, and mechanical edits with a fixed rule. Use a stronger agent only for drafting, method choice, classification, or review. Check each `assistant` return against the files.

## Agents (14)

`assistant`, `literature-reviewer`, `data-steward`, `translator`, `writer`, `figure-maker`, `bioinformatician`, `microbial-genomicist`, `evolutionary-genomicist`, `software-engineer`, `breeder`, `statistician`, `clinical-geneticist`, `reviewer` (Opus). Descriptions in each agent's frontmatter.

Roster, chains, and gaps: `${CLAUDE_SKILL_DIR}/references/roster.md`. Summary:

* Chains: assay planning -> `bioinformatician` -> `statistician` -> `reviewer` -> `writer`.
* Variants: `bioinformatician` -> `clinical-geneticist` -> `reviewer`.
* Outbreak: `microbial-genomicist` -> `evolutionary-genomicist` -> `reviewer`.
* Breeding: `breeder` -> `statistician` -> `data-steward`.
* The user is the PI; the main session is the deputy PI who briefs the group members and checks every return; scope, budget, ethics, and publication claims go to the PI.
* Gaps (no assay liaison, HPC engineer, or coordinator agent) are listed in the roster.

Model and effort are in each agent's frontmatter. After a cheaper tier fails twice, raise effort first, then model. Opus is for the reviewer and blind variant classification only.

## Next skills

Call Skill `agent-brief` to write a brief and verify returns, and `team-playbooks` for the agent order of a multi-step workflow.

## Checks and stop rules

* Ask the reviewer for correctness and requirement gaps only; it always finds optional ones.
* Skip `reviewer` for exploratory work and for edits you tested yourself.

Competency map and the sources behind this team: `${CLAUDE_SKILL_DIR}/references/competency-map.md`.
