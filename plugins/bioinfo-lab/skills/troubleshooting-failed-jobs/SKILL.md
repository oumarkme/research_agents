---
name: troubleshooting-failed-jobs
description: 'Use when a pipeline step, container, or job fails, hangs, is killed, or leaves empty or truncated output. Not for sizing before launch (hpc-resource-planning) or tuning a slow job (performance-profiling).'
---

# Troubleshooting failed jobs

## Capability
Find the first real cause of a failure and fix it, not the symptom. Correct: evidence shows the cause, a minimal reproduction tests the fix, the rerun passes checks.

## Decide (triage order)
1. Freeze evidence: keep the work directory; note command, host, time, logs.
2. Find the first real error, reading the log from the top. Record the exit status. A command killed by signal n returns 128+n (bash manual).
3. Classify: killed by signal, tool error, missing command, permission, bad input.
4. Check inputs before code: integrity, checksum against source, index age, build and contig names (`genomics-pitfalls`).
5. Check environment: disk and quota, writable paths, tool or image version against the last good run.
6. Reproduce on the smallest failing input, same image and command; grow it until it fails.
7. Rerun only when the cause is found and transient. After two same-kind failures, stop and report.

## Find current information
Follow `current-methods-lookup`. Questions:
* What do the tool's documentation and issue tracker say about this error and exit status?
* Which integrity check does the format's tool offer, and what can it not detect?
* Where does the engine keep per-task commands and logs in this version?
Sources, in order: tool and engine docs and release notes; the issue tracker; the exact error text in official forums.
Check: version matches ours; fix confirmed.

## Verify
* A job is done only when expected outputs exist and pass a content check, not when exit is 0.
* Known-answer rerun on the minimal input first.
* Failing (same error returns): the cause was wrong; redo step 2 on the new log.

## Failure modes
* Partial output taken as complete.
* Exit 0 with empty output from a pipe.
* Cache holding a corrupt task: delete only that task, in your own directory.
* More memory given for a truncated input.

## Record and report
`analysis-log`: question, date retrieved, sources, version, not verified, recheck date. Report failing step, exit status, first error line, evidence, fix, rerun result. Ask first if the fix needs root or deleting outside your directory; corrupt read-only raw data are reported, not repaired.

Seeds: `references/`.
