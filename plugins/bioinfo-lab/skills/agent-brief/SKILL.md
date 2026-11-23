---
name: agent-brief
description: 'Use when you write the prompt for an agent or subagent: what to include, when to parallelize, and how to check each return.'
---

# Agent brief

A subagent sees none of this conversation, so the prompt must stand alone. Include what applies:

* Objective, in one sentence, and the decisions already made.
* Exact inputs: paths, IDs, versions, and any lookup results (URL, version, date) the agent needs.
* Output: format, destination path, and what "done" means in checkable terms.
* Skills to call, and where it may write.

For multi-session work, point to `PROGRESS.md` (`analysis-log`).

## Parallelism

Split by file or by question. Never let two agents edit the same file. Keep steps that share context, or depend on each other, in one agent or in sequence.

## Check each return

* The promised files exist and are not empty.
* One key number recomputes from the raw input.
* Each cited PMID or DOI is labeled fetched; treat `snippet` and `blocked` as unverified.
* On a partial return, extend the task or re-brief; after the same failure twice, do it in the main session.
