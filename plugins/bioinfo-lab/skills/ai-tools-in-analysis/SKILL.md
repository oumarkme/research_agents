---
name: ai-tools-in-analysis
description: 'Use when an AI coding or writing assistant helps with analysis code, numbers, or text: what to delegate, verification, provenance, disclosure. Not for editing prose tells (humanizer).'
---

# AI tools in analysis

## Capability
Use AI assistants without importing their errors. Correct: every AI-touched code, number, or citation was checked by a route independent of the model, and its use is logged and disclosed.

## Decide
1. Match verification effort to checkability, your expertise, and the cost of an error. Low risk (boilerplate, plotting): run and read. Medium (parsers, statistics code): known-input tests. High (coordinates, variant logic, clinical calls, paper numbers): write or review yourself, recompute from raw input.
2. Specify inputs, outputs, and edge cases in the prompt.
3. Model agreement is not evidence.

## Find current information
Follow `current-methods-lookup`. Questions:
* What do the target journal and ICMJE currently require for AI-use disclosure?
* What does the institution or funder require?
* What do recent studies report about error rates of AI tools in this task?
Fetch the current journal and ICMJE text and cite the retrieval date; do not rely on remembered policy.
Sources, in order: ICMJE and journal policy pages; institution and funder policy; independent studies and risk frameworks (PubMed, Europe PMC); preprints, labeled.
Check: retrieval date, policy version, fit to the task.

## Verify
* Read every line before it runs; code that runs can be wrong.
* Test a tiny input with a known answer, then empty, boundary, and missing values.
* Recompute each reported number by an independent route.
* Check every flag, function, and option against the tool's own help.
* Check every citation by PMID or DOI (`trusted-sources`).
* Failing: discard the output and redo; a repeat prompt is not a check.
* Genomics tests: `references/failure-modes.md`; bug classes: `genomics-pitfalls`.

## Failure modes
Hallucinated functions or citations, sycophancy, plausible but wrong logic, silent filtering, toy-case-only code.

## Record and report
`analysis-log`: tool and model, version or date, purpose, prompt, files touched, verification, checker, plus question, retrieval date, sources, not verified, recheck date. Commit AI code with its test. Disclosure: `humanizer/references/disclosure.md`.

Seeds: `references/`.
