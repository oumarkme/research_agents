---
name: performance-profiling
description: 'Use when a step is slower or heavier than expected and you must find the bottleneck and tune threads, I/O, compression, or indexing. Not for sizing a new job (hpc-resource-planning) or a crash (troubleshooting-failed-jobs).'
---

# Performance profiling

## Capability
Find what limits a step and change it with measured gain. Correct: before and after on the same input, repeated runs, output unchanged.

## Decide
1. Fix the metric (wall, CPU hours, peak memory) and a record-level output-equality check; file checksums fail when headers carry dates.
2. Baseline: one fixed input, repeated runs, same node; note host load.
3. Classify by CPU use against threads: near full is CPU-bound; far lower is I/O wait, a serial stage, or contention; memory near the limit is memory-bound.
4. Tune the largest block of the timeline first. One change per run; log failures too.
5. Levers in order: threads until gain per thread is small; local scratch; compression level; indexed access instead of scans; scatter by interval; streaming.
6. Stop when the next gain is below run-to-run variation, or the step is a small share of the run.
7. Ask first if a change alters results or needs cores beyond the limit.

## Find current information
Follow `current-methods-lookup`. Questions:
* What do this version's docs say about threads, buffers, and compression?
* Does a newer release or other tool address this bottleneck?
* How does the engine report per-task time, CPU, and memory?
Sources, in order: tool documentation and release notes; independent benchmarks of recent years (PubMed, Europe PMC); preprints, labeled.
Check: release date, maintenance, benchmark data and hardware like ours, output equal to the old tool's.

## Verify
* Speedup = wall(1) / wall(n); efficiency = speedup / n. Report medians of repeats.
* Equal-output check passes before any speedup is claimed. Failing: the change altered results; revert.
* Wall far above CPU time per thread means waiting; CPU time rising with flat wall means contention.
* Compare cold and warm cache.

## Failure modes
* Different nodes or loads between runs; a single run.
* Tuning a stage that is a few percent of the run.
* More threads than allocated.

## Record and report
`analysis-log`: question, date retrieved, sources, version chosen, not verified, recheck date. Report before and after: wall, CPU hours, peak memory, threads, input size, output check, command line.

See `references/where-to-look.md`.
