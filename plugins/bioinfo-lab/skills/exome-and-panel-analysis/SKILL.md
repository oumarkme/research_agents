---
name: exome-and-panel-analysis
description: 'Use when analyzing WES or targeted panels: capture kit and BED, coverage metrics, per-gene gaps, padding, kit and panel versions, capture CNV. Not for WGS calling (short-read-germline-calling) or SV work (sv-cnv-calling).'
---

# Exome and panel analysis

## Capability
Capture data (any organism) analyzed with its kit and target BED. Correct: calls come from covered targets, and coverage gaps in reportable genes are reported with the result.

## Decide
1. Record kit, kit version, vendor BED, BED build, design date, panel version. Stop if unknown.
2. Match BED build to BAM. Lift over only with a stated chain; recheck exon counts.
3. One target BED per kit, fixed for the project. Report padding; padding-only variants are lower confidence.
4. Compute capture metrics (on-target, uniformity, depth, duplicates). Use limits validated for this kit, not WGS limits.
5. Make a per-exon coverage table for reportable genes (human: MANE Select; else canonical). Flag exons below the project minimum.
6. Several kits: call on the BED intersection, or per kit and merge. Add kit as covariate in burden tests.
7. Capture CNV: use a same-kit, same-batch reference set; never one sample against a public reference. Single-exon calls need confirmation.
8. Ask when a reportable gene is poorly covered in an unsolved case.

## Find current information
Follow `current-methods-lookup`. Ask: which metric and CNV tools are maintained for this kit and cohort size; the validation guidance of professional bodies (AMP, CAP, ACMG); the current gene-panel version (human: PanelApp, ClinGen); the vendor's BED. Search tool and guideline pages, then independent benchmarks (PubMed, Europe PMC; preprints labeled). Check date, maintenance, fit.

## Verify
* Metrics match the kit's validated history; one outlier in a batch points to input DNA.
* Reference material: expected variants called at expected depth.
* CNV: confirm orthogonally (MLPA, array, qPCR); batch-wide shifts mean a bad reference set.
* Failing: fix the reference set or kit mapping before any report.

## Failure modes
* Off-target variants trusted; wrong kit-version BED.
* PCR duplicates inflate panel coverage.
* Old gene list after a panel version change.

## Record and report
Log (`analysis-log`): question, date, sources, versions, unverified, recheck. Report kit, BED build, padding, metrics, low-coverage exons, CNV reference.

Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.
