---
name: clinical-pipeline-validation
description: 'Use when validating, freezing, or changing a human diagnostic NGS bioinformatics pipeline, or preparing evidence for accreditation. Not for variant classification (variant-interpretation) or research benchmarking (sequencing-pipelines).'
---

# Clinical pipeline validation

## Capability
Show with evidence that a locked pipeline performs as claimed per variant class. The director and quality manager decide the standard, acceptance numbers, and revalidation.

## Decide
1. Scope: sample types, kit and BED, build, transcripts, each variant class reported (SNV, indel, CNV, SV, mitochondrial, repeat, RNA).
2. Lock: image digests, reference md5, annotation releases, parameters, git tag.
3. Validation set: truth-set materials plus orthogonally confirmed in-house samples for each class and context.
4. Metrics per class and context: positive percent agreement, negative percent agreement, technical positive predictive value, each with CI lower bound. Truth sets cover high-confidence regions only.
5. Precision and limits of detection.
6. Acceptance criteria fixed before the run, never tuned on the validation set.
7. Orthogonal confirmation rules; identity check.
8. Change control: any change to caller, aligner, reference, annotation, filters, kit, or container is logged and triggers a regression run, revalidation by impact.
9. Plan, report, SOP, limitations, audit trail, sign-off.

## Find current information
Follow `current-methods-lookup`. Ask: which standard applies (accreditor, ISO, society); which truth sets are current; which changes need revalidation. Sources in order: accreditor and standards pages, society guidelines, GIAB and GA4GH, independent validation papers (PubMed). Retrieve current text, record the date; never cite criteria from memory. Seeds: `references/where-to-look.md`.

## Verify
* Known-answer run meets pre-set criteria.
* Repeats agree across days and operators.
* Orthogonal assay confirms calls per class, including difficult regions.
* A deliberate container change reproduces locked results; if not, stop.

## Failure modes
* Recall quoted for high-confidence regions only.
* Thresholds set on the claim samples; no limits stated for difficult genes.
* Undocumented minor updates; kit or build differs from production.

## Record and report
Log: question, date retrieved, sources, versions, not verified, recheck date. Report scope, criteria, results with intervals, failures, versions, limitations.
