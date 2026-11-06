---
name: workflow-engines-and-containers
description: 'Use when choosing, writing, or debugging a workflow engine setup, or a container or environment that fixes software versions. Not for pipeline content (sequencing-pipelines) or code style (coding-style).'
---

# Workflow engines and containers

## Capability
Run analyses as pinned, restartable, auditable workflows. Correct: a second run on a second host, same inputs and pins, gives record-level identical outputs.

## Decide
1. Reuse a maintained community pipeline at a pinned revision before writing one.
2. Engine: the one the team runs and the host supports; ask before adopting another.
3. Software source, in order: shared image directory if CLAUDE.md names one (read-only: ask the owner to add images), a project-built container, a locked environment.
4. Pin every layer (image digest, lock file, reference checksum). Never a floating tag.
5. The scheduler is unknown. Ask for executor, queue, walltime, and memory rules.
6. Total cores within the limit in CLAUDE.md (else ask). Work directory in private scratch; results to the project.
7. Retry only resource-related failures, with a bounded count and a memory cap below the host limit.

## Find current information
Follow `current-methods-lookup`. Questions:
* Which maintained pipeline fits this assay, and which release?
* What do current engine docs say about resume and caching on our file system, retries, and container use?
* Which container runtime and GPU passthrough does the host support?
Sources, in order: engine docs and release notes; pipeline release page; runtime docs; independent reviews of recent years (PubMed, Europe PMC); preprints, labeled.
Check: release date, maintenance, fit to our host.

## Verify
* Dry run lists expected jobs.
* Smallest input end to end against a known answer.
* Rerun unchanged: nothing re-executes. Change one input: only dependents rerun.
* Compare outputs at record level across two runs or hosts.
* Failing (all reruns, or outputs differ): find the changed pin or timestamp.
* Peak concurrent cores stay within the limit.

## Failure modes
* Floating tags; absolute paths in configs.
* Work directory deleted before results are final.
* File-system timestamps break the cache.

## Record and report
`analysis-log`: question, date retrieved, sources, version chosen, not verified, recheck date. Report engine and version, pipeline revision, image digests, config, parameters, full command, run reports.

Seeds: `references/`.
