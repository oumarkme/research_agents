---
name: lab-team
description: 'Use before delegating to a subagent or planning multi-step work: which built-in agent or forked skill fits, how to brief it, and how to check its return.'
---

# Delegation

Delegation is optional. A subagent starts with a fresh context (no conversation history, no skills you already loaded) and returns only a summary. It still spends its own tokens: multi-agent runs used about 15 times the tokens of a chat (Anthropic, 2025). Delegate work that is parallel, breadth-first, or produces bulky output; keep dependent steps in the main session.

## Which agent

This plugin ships no agents. Claude Code's built-in ones, and the forked skills here, cover the jobs:

| Job | Use |
|---|---|
| Find files, read logs, check job output, run tests (read-only) | `Explore` |
| Plan a large change or analysis before doing it | `Plan` |
| Multi-step work or web research in its own context | `general-purpose` |
| Read known URLs | `web-fetch` |
| Version-sensitive facts from the web | skill `fact-lookup` |
| Literature search with verified citations | skill `literature-review` |
| Heavy sequencing run with a log | skill `long-analysis-job` |
| Independent check of claims, numbers, or a blind variant call | skill `independent-review` |
| Review a code diff | `/code-review` |
| Hard decision, stuck, or before declaring done | `/advisor <model>`, a setting in your own Claude Code |

Forked skills take the whole task as their argument and start with no history. Pass `model` (an alias such as `haiku`, `sonnet`, `opus`) and `effort` per call when a job needs a different tier. `Explore` may run on a strong model, so pass `model: haiku` for plain searches. If a result is poor: sharper brief, then more effort, then a stronger model.

## Brief

The subagent sees nothing of this conversation; the prompt must stand alone. Include what applies:

* Objective in one sentence, and the decisions already made.
* Exact inputs: paths, IDs, versions, and any lookup results (URL, version, date).
* Output: format, destination path, and what "done" means in checkable terms.
* The skills to call by name (a subagent can load any plugin skill with the Skill tool but does not know which one you want) and the rules it needs from `lab-rules`.
* For an independent review: only the specification, files, and evidence, never your conclusion.

Split by file or by question; never let two agents edit the same file. For multi-session work, point to `PROGRESS.md` (`analysis-log`).

## Check each return

* The promised files exist and are not empty.
* One key number recomputes from the raw input.
* Each cited PMID or DOI is labeled fetched; treat `snippet` and `blocked` as unverified.
* On a partial return, extend the task or re-brief; after the same failure twice, do it in the main session.

Example sequences by workflow: `${CLAUDE_SKILL_DIR}/references/playbooks.md`. Sources: `${CLAUDE_SKILL_DIR}/references/competency-map.md`, `${CLAUDE_SKILL_DIR}/references/design-basis.md`.
