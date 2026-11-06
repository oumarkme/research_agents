---
name: genomics-pitfalls
description: 'Use when code or analysis handles genomic coordinates, variants, builds, sample tables, genotypes, or prediction: checklist of bug classes (coordinates, builds, contigs, REF/ALT, sample order, leakage).'
---

# Genomics and genomic prediction pitfalls

Assert each item in code or say why it does not apply.

## Coordinates, builds, variants

* BED is 0-based, half-open; VCF, GFF, and SAM are 1-based, closed. `chr1 100 200` in BED covers 1-based positions 101 to 200. Convert once, in one place.
* Genome build (assembly accession and release) must match across variants, annotations, and references. Read it from the header or `@SQ` lines, assert it, and write it to the output.
* Contig naming: `chr1` versus `1`, `chrM` versus `MT`. Normalize with an explicit map, not by stripping `chr`; hg19 chrM is not the sequence of GRCh37 MT (rCRS), so renaming does not fix it. Check that all contigs in the input exist in the reference.
* REF/ALT: left-align and normalize indels, split multi-allelic sites before joins, check the REF allele against the reference FASTA, and remember that a REF longer than one base spans several positions. Strand matters for array and imputation data.
* Ploidy and haploid contigs: set ploidy per sample and contig (X, Y, Z, W, organelles, polyploids, haplodiploids). Human PARs are diploid in both sexes.
* Joins on variants use chromosome, position, REF, and ALT together, not position alone.
* Filtering order changes results; record it, with thresholds and the sample set they are computed on.

File formats and what to check in each: `${CLAUDE_SKILL_DIR}/references/file-formats.md`.

## Samples and tables

* Sample order must be identical between genotype, phenotype, covariate, and kinship files. Match by ID, assert equality, and fail on duplicates or missing IDs. Never rely on row position.
* Handle NA explicitly; never let it become 0 or a string. Check types after reading (chromosome as text, position as integer).

## Statistics and genomic prediction

* Leakage: relatedness between training and test folds, scaling, imputation, or feature selection fitted on all samples, markers or principal components computed before the split. Fit every preprocessing step inside the cross-validation loop; split by family or population structure when relatives are present.
* Report the validation scheme, accuracy metric (and its scaling), and a baseline model with the same folds.
* Correct for multiple testing and state the method; check structure and batch as confounders.
* Log seeds and software versions.

## Human variant interpretation

* Classify with the current ACMG/AMP and ClinGen guidance (`variant-interpretation`); give HGVS with transcript and build; verify database entries directly (`trusted-sources`).

## Find current information
For tool behavior and database releases follow `current-methods-lookup`; coordinate and format rules here are stable.

## Verify
Run a tiny known-answer input (expected coordinates, REF, sample order) and assert the output; compare REF to the FASTA and IDs across files. On failure, stop and fix.
