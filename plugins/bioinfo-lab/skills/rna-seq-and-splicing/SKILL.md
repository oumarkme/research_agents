---
name: rna-seq-and-splicing
description: 'Use when analyzing bulk RNA-seq in any organism: strandedness, QC, quantification, differential expression, splicing, fusions, or human rare-disease outliers. Not for assay planning (sample-and-assay-planning).'
---

# RNA-seq and splicing

## Capability
Quantify and test expression, splicing, or fusions in bulk RNA-seq.

## Decide
1. Strandedness: infer it from the data and compare with the kit; a mismatch stops the run.
2. Per-sample QC: RNA integrity, rRNA fraction, mapping, duplication, 3' bias, and identity against the DNA sample. Set exclusions before seeing results (judgment).
3. Alignment or pseudoalignment by need (splicing and fusions need alignment). One annotation release per project. No reference: de novo assembly. Polyploids: quantify homeologs separately; sum only after checking (judgment).
4. Differential expression on raw counts, never TPM; batch in the design; replicates set power (2 versus 2 is exploratory, judgment); shrink fold changes.
5. Splicing: case-control or single-sample outlier methods, by design.
6. Fusions: require split-read and spanning-pair support; confirm by RT-PCR.
7. Human rare-disease outliers: controls of the same tissue, kit, and batch; the gene must be expressed in the tissue.

## Find current information
Follow `current-methods-lookup`. Ask: which aligner, quantifier, differential expression, splicing, and fusion methods fit this organism and sample size; which annotation release; minimum controls for outlier methods. Sources in order: official docs, vignettes, release notes; the annotation body page; recent independent benchmarks (PubMed, Europe PMC); preprints, labeled. Check date, maintenance, benchmark, fit. Seeds: `references/`.

## Verify
* Strandedness agrees across samples and with the kit.
* PCA by batch, sex, RNA quality, and group before testing.
* Read genotypes match the DNA sample.
* Two methods agree on top hits; positive-control genes move as expected.
* Fusions and outliers: RT-PCR, read inspection, or a DNA variant; otherwise report as unexplained.

## Failure modes
* Batch confounded with condition: stop and ask.
* Mixed annotation versions across tables.
* Tissue mismatch; a normal result does not exclude a variant in an unexpressed gene.

## Record and report
Log: question, date retrieved, sources, versions, not verified, recheck date. Report library type, strandedness, annotation, tools, design, filters, multiple testing, controls, exclusions.
