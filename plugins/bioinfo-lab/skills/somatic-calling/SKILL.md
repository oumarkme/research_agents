---
name: somatic-calling
description: 'Use when calling and filtering somatic SNVs and indels from tumor-normal, tumor-only, or low-VAF mosaic data. Not for germline calling (short-read-germline-calling) or build and contig checks (genomics-pitfalls).'
---

# Somatic calling

## Capability
Turn tumor (and normal) reads into a filtered somatic call set with known purity and error profile.

## Decide
1. Record matched normal (same individual, batch, kit), tissue, purity, depth, build. Stop if the normal is missing and certain somatic status is needed.
2. Confirm tumor and normal are one individual (genotype concordance).
3. Pick the caller class by design: tumor-normal; tumor-only (same-kit panel of normals, germline resource; calls are candidates); mosaic; long reads. Add a second, independent caller if precision matters.
4. Filter in order: model-based caller filters, then depth, alt reads, mapping quality, population frequency, repeats. Set thresholds on the lab's truth set or spike-in. Keep failed calls with filter state.
5. Read VAF against copy number and purity, not as clonal fraction. Human blood: consider clonal hematopoiesis.
6. Germline cohorts with suspected mosaicism: `${CLAUDE_SKILL_DIR}/references/mosaic-and-validation.md`.
7. Stop and ask when purity is low, the normal holds tumor, or VAF is near the caller's floor.

## Find current information
Follow `current-methods-lookup`. Ask: which caller and panel-of-normals approach fits this design now; which artifact filters apply to FFPE or this sequencer; which germline resource fits the organism.
Sources in order: official docs and release notes; GA4GH or SEQC2 pages; independent benchmarks of recent years (PubMed, Europe PMC); preprints, labeled.
Check release date, maintenance, VAF range tested. Seeds: `references/where-to-look.md`.

## Verify
* Known answer: titration of two genotyped samples or a public truth set; recall by VAF bin.
* Identity: a tumor-normal swap makes calls look germline.
* Sanity: clonal VAF peak near purity/2; no substitution class with strand bias.
* Two callers: concordance; inspect discordant calls in reads. Orthogonal assay (ddPCR) for low VAF.
Failing: stop, refit filters, rerun.

## Failure modes
FFPE artifacts; germline called somatic (shallow normal); mixed caller versions.

## Record and report
Log: question, date retrieved, sources, version chosen, NOT verified, recheck date. Report caller, version, panel, filter counts, purity, per-call VAF and depth.
