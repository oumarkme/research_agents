---
name: hpc-resource-planning
description: 'Use when sizing cores, memory, disk, GPU, and runtime for a job, or splitting parallel jobs under the host limit. Not for a slow job that already runs (performance-profiling) or a failed job (troubleshooting-failed-jobs).'
---

# HPC resource planning

## Capability
Request resources from measurement so jobs finish inside host limits. Correct: a written plan with pilot numbers, a stated margin, and a core total with its arithmetic.

## Decide
1. Read host and limits from CLAUDE.md. The scheduler is unknown: ask for queue, walltime and memory caps, and fair-share rules before any submit script.
2. Pilot: one representative small input; record wall, CPU time, CPU use, peak memory.
3. Scale: repeat at a second input size. Superlinear growth: size from the larger run.
4. Memory from the peak, never the mean, plus a stated margin.
5. Set threads explicitly; declared equals used.
6. Core total = concurrent jobs times threads, plus helpers, at or under the limit. Show it.
7. Disk peak = inputs + intermediates + outputs + temp; check free space.
8. GPU: one job per GPU; ask before taking all.

## Find current information
Follow `current-methods-lookup`. Questions:
* What memory and thread behavior does this tool version document?
* How does the engine report per-task time and memory?
* Which GPU selection does the tool and host support?
Sources, in order: tool documentation and release notes; host policy or admin; independent benchmarks of recent years (PubMed, Europe PMC); preprints, labeled.
Check: release date, fit to our data size and hardware.

## Verify
* Keep a sizing log: tool, version, input, threads, wall, CPU time, CPU use, peak memory, temp disk.
* Forecast the full run from two pilot sizes, run it, compare. If peak exceeds request or wall is far off, resize from the real run.
* Watch core use against the plan.
* A cached pilot understates I/O; repeat cold.

## Failure modes
* Tools that ignore the thread setting, or libraries that start their own threads.
* Runtime heap plus off-heap overhead above the memory limit.
* Repeated reads from network storage (low CPU use).

## Record and report
`analysis-log`: question, date retrieved, sources, version chosen, not verified, recheck date. Report pilot numbers, requested cores, memory, disk, GPUs, expected wall time, and the core total. Ask before exceeding stated cores, half of RAM, all GPUs, or near-full temp space.

Seeds: `references/`.
