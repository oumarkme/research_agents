---
name: agent-brief
description: 'Use when you write the prompt for a team agent or subagent: the brief template, parallelism rules, and the checks to run on each return.'
---

# Agent brief

You are the deputy PI briefing a group member, who sees none of this conversation. Fill every line. The member escalates to you; you escalate PI decisions (scope, budget, ethics approvals, publication claims) to the user.

```
Objective: one sentence.
Context: decisions already made.
Inputs (paths): exact files, IDs, versions.
Output (format, cap, path): e.g. table, under 200 words, /path/out.tsv.
Boundaries: writable dirs; threads within the host limit in CLAUDE.md; scratch dir; no edits outside the paths.
Skills to call: names.
Done when: checkable condition (files exist, check passes).
Current facts: paste the assistant's lookup result here (URL, version, date); the agent does not browse for documentation.
```

For multi-session work, point to `PROGRESS.md` (`analysis-log`).

## Parallelism

Split by file or by question. Never let two agents edit the same file. Keep steps that share context or depend on each other in one agent or in sequence. The limits in `lab-team` follow vendor guidance (`lab-team/references/design-basis.md`), untested here.

## Verify each return

1. Confirm the promised output files exist and are not empty.
2. Recompute one key number from the raw input.
3. Check that each cited PMID or DOI is labeled fetched; treat `snippet` and `blocked` as unverified.
4. On a partial return (`lab-rules` checkpoint), extend or re-brief. After the same failure twice, do the task yourself.
