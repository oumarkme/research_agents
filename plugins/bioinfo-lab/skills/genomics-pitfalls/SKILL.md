---
name: genomics-pitfalls
description: 'Use when code or analysis handles genomic coordinates, variants, builds, sample tables, genotypes, or prediction: checklist of bug classes (coordinates, builds, contigs, REF/ALT, sample order, leakage).'
---

# Genomics and genomic prediction pitfalls

Assert each item in code or state why it does not apply. Report only problems with a concrete failing input.

## Coordinates, builds, variants

* BED is 0-based, half-open; VCF, GFF, and SAM are 1-based, closed. `chr1 100 200` in BED covers 1-based positions 101 to 200. Convert once, at one place, and document it in the docstring.
* Genome build: GRCh37 versus GRCh38 (and the crop assembly version) must match across variants, annotations, and references. Read the build from the file header or `@SQ` lines, assert it, and write it to the output.
* Contig naming: `chr1` versus `1`, `chrM` versus `MT`. Normalize with an explicit map, not by stripping `chr`. Check that all contigs in the input exist in the reference.
* REF/ALT: left-align and normalize indels (`bcftools norm`), split multi-allelic sites before joins, check the REF allele against the reference FASTA, and remember that a REF longer than one base spans several positions. Strand matters for array and imputation data.
* Joins on variants use chromosome, position, REF, and ALT together, not position alone.
* Filtering order changes results; record it. State allele frequency, missingness, quality, and depth thresholds and the sample set they are computed on.

File formats and what to check in each: `${CLAUDE_SKILL_DIR}/references/file-formats.md`.

## Samples and tables

* Sample order must be identical between genotype, phenotype, covariate, and kinship files. Match by ID, assert equality, and fail on duplicates or missing IDs. Never rely on row position.
* Handle NA explicitly; do not let it become 0 or a string. Check types after reading (chromosome as text, position as integer).
* Patient-level data (sample IDs, genotypes, phenotypes, clinical notes) stay in the project; never in logs that leave it, commits, or external queries.

## Statistics and genomic prediction

* Leakage: relatedness between training and test folds, scaling, imputation, or feature selection fitted on all samples, markers or principal components computed before the split. Fit every preprocessing step inside the cross-validation loop; split by family or population structure when relatives are present.
* Report the validation scheme, accuracy metric (correlation with the phenotype or adjusted phenotype, and how it is scaled by heritability), and a baseline model (for example GBLUP) with the same folds.
* Correct for multiple testing and state the method; check population structure and batch as confounders; watch for inflated effects in small panels.
* Set and log random seeds; report the software version.

## Variant interpretation

* Use ACMG/AMP with ClinGen specifications, HGVS notation with the transcript and build, and verify ClinVar, gnomAD, and OMIM entries directly (see `trusted-sources`).
