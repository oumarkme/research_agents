---
name: analysis-log
description: 'Use when work spans several steps or sessions (pipeline build, multi-step analysis, long jobs, manuscript revision): progress file, claims ledger, start-of-session routine, and provenance for every reported number.'
---

# Analysis log

Goal: a fresh session or agent resumes in minutes, and every reported number traces to a script, an input, and a version. Use it for work that will outlive one context window; skip it for a single short task.

## Files (project directory; copy from `${CLAUDE_SKILL_DIR}/templates/`)

* `PROGRESS.md`: goal, current state, next step, blockers, commands run, job IDs, scratch path, and each decision with its reason. Update after every step. Keep it to one page. No patient-level data if the project is shared.
* `claims.json`: the ledger of claims or deliverables. Each entry has `id`, `claim`, `check` (how it will be verified), `evidence` (path), `status` (`open`, `verified`, `failed`), and `notes`. Change only `status`, `evidence`, and `notes`. Never delete or reword an entry; add a new `id` instead. JSON resists accidental rewriting better than Markdown.
* `provenance.tsv`: one row per figure, table, or number that leaves the project: output file, script, input files and versions or genome build, key parameters, tool versions, date.

## Start of every session

1. Read `PROGRESS.md` and `claims.json`.
2. Check the real state: `git status` and `git log`, running jobs, files that should exist.
3. Re-run the smallest check that shows the last step still works. Fix a broken state before new work.

## During the work

* One step at a time. Save or commit after each step, and update `PROGRESS.md`.
* Set `verified` only after the check named in the entry has run in this session and you read its output. Prefer a check that does not share the method that produced the result (a second tool, a held-out sample, or `reviewer`). Never mark an entry from memory of an earlier run.
* Models can report results they did not obtain and can agree too readily with a plan. When a number matters, recompute it from the raw input.
* After two failures of the same kind, record the blocker in `PROGRESS.md` and stop.

## End of session

Leave a clean state: `PROGRESS.md` names the next step, no half-written files remain, and the scratch path is recorded for cleanup.

## Limits

This is a convention, not enforcement. If a step must never be skipped, ask for a hook (a `Stop` hook can block the end of a turn until a script passes). Design basis: `${CLAUDE_SKILL_DIR}/../lab-team/references/design-basis.md`.
