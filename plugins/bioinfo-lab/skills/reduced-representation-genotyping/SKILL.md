---
name: reduced-representation-genotyping
description: 'Use when designing or analyzing GBS, RAD, DArT, or skim-sequencing data, with or without a reference, including filters and low-coverage imputation. Not for SNP arrays (array-genotyping-and-imputation) or WGS calling (short-read-germline-calling).'
---

# Reduced-representation genotyping

## Capability
Turn sparse, low-depth sequencing into a marker set with measured error and missingness. A correct result has reported replicate concordance and no structure from parameters or plates.

## Decide
1. Match method to question and budget; dense LD, structural variants, or fixed markers across batches need array or WGS.
2. Design: locus count times depth per sample must fit the yield; digest the reference in silico; sequence parents deeper.
3. Reference present: align and call. Absent: build loci de novo and log every parameter.
4. Duplicated or polyploid genomes: use `polyploid-genotyping-dosage`.
5. Filter samples, genotypes, and markers; read limits from plotted distributions and replicate concordance.
6. Randomize samples over plates; add replicates and a control to each plate.
7. Low-coverage data: impute from a panel of the same population, then hand off to `genomic-prediction`.

## Find current information
Per `current-methods-lookup`, ask: which pipeline suits our organism and reference status; which enzymes fit our genome; what coverage imputation needs; which benchmark compares methods.
Search: tool docs and release notes, provider documentation (DArT scoring and call rates), recent benchmarks (PubMed), labeled preprints. Check release date, maintenance, fit to genome and diversity.

## Verify
* Replicates: genotype concordance at the filtered set.
* Mask known genotypes and re-impute; report accuracy by allele frequency.
* PCA colored by plate, library, lane, enzyme lot: batch must not drive PCs.
* Heterozygosity against depth: low depth under-calls heterozygotes.
* Rerun de novo with other parameters: structure holds.
* Missingness against PC scores: tracking ancestry means cut-site dropout.

## Failure modes
* Non-random missingness.
* Paralogs read as SNPs.
* Parameter-driven structure.
* Imputation panel from another population.

## Record and report
Log: question, date, sources, versions, not verified, recheck date. Report enzyme, size selection, reads per sample, loci per filter step, missingness, concordance, parameters.

Seeds: `references/where-to-look.md`.
