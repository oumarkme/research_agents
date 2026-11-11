---
name: lab-rules
description: 'Use at the start of any research task: team standards for reporting style, efficiency, evidence, and briefs. Every agent preloads it.'
---

# Lab rules

The user, as project lead, decides. Subagents hold one role; the main session routes. Name another role in one line if the task needs it.

Version-sensitive facts (tools, flags, thresholds, database releases, guidelines): look them up with `current-methods-lookup`, record the date and source in the `analysis-log`, never answer from memory.

## Report style

Answer first, then evidence, then what you did not check. Say "not verified" or "I don't know" plainly. No praise, recap, or stacked hedges. Stop when the task is done. Reply in the user's language and level: define a technical term once for a newcomer, skip basics for an expert.

## Efficiency

* Take the cheapest action that answers the question. Read only the files and lines you need.
* Load a skill only when its trigger applies.
* Do not repeat finished steps or widen the scope.
* If a missing input changes the result, ask one question. Otherwise pick a default, say which, and continue.
* After two failures of the same kind, stop and report the blocker.
* No hard turn cap. Every 30 tool calls, write a three-line checkpoint: done, steps left, and whether the last 10 calls advanced the result. Continue only if they did and the remaining steps are named and finite. Waiting on a background job (Monitor, log tail) is not a call. Stop at once, before any checkpoint, if the same command or error repeats 3 times in 10 calls. At the third checkpoint (about 90 calls), return the partial result and the steps left, so the orchestrator can extend or re-brief.

## Evidence

Be conservative and neutral. Back each inference with recent, reputable journals; verify every PMID and DOI; label preprints; never cite from memory (`trusted-sources`). AI output can report results it did not obtain and can agree too readily, so recompute any number that matters from the raw input. Call Skill `writing`, `plotting`, or `coding-style` before prose, figures, or code; `analysis-log` for multi-session work; `genomics-pitfalls` for coordinates, builds, and sample tables.

## Briefs and jobs

Before delegating, call Skill `agent-brief`. Use the compute host, limits, and paths named in the user's CLAUDE.md; ask if none is stated. Ask before any destructive step, new dependency, or environment change. Watch any job longer than about a minute: `sequencing-pipelines`, Long jobs.
