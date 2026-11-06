---
name: proteomics-metabolomics-integration
description: 'Use when adding proteomics or metabolomics to genomic data in any organism: pQTL, colocalization, identifier mapping, normalization, missing values, multi-omics factor models. Not for GWAS itself (association-studies).'
---

# Proteomics and metabolomics with genomics

## Capability
Link protein or metabolite levels to genotype.

## Decide
1. State the question (QTL discovery, GWAS locus support, variant effect, biomarker panel). Count overlap.
2. Record platform and panel (mass spectrometry or affinity; targeted or not).
3. Identifiers: proteins by accession, not gene symbol; metabolites by structure key and identification level. One mapping table; list unmapped.
4. Normalize within platform. Plot sample medians and PCA by batch and run order before and after; diagnose before correcting.
5. Missing values: separate random loss from below detection; filter by group-wise presence; impute to match the cause; log fraction imputed.
6. Genetic link: cis-QTL first, colocalization at the locus, then Mendelian randomization with cis instruments and sensitivity checks (judgment).
7. Affinity assays: protein-altering variants can change binding and mimic a pQTL (judgment); check the lead variant against the sequence and a second platform.
8. Factor models are exploratory, not causal (judgment); few samples with many features overfit.

## Find current information
Follow `current-methods-lookup`. Ask: which normalization, imputation, colocalization, and MR methods fit this platform; the identifier release; public pQTL atlases for this tissue. Sources in order: platform and software docs; repository and atlas pages; recent independent benchmarks (PubMed, Europe PMC); preprints, labeled. Check date, maintenance, benchmark, fit. Seeds: `references/`.

## Verify
* Replicates and pooled QC samples cluster; no run-order trend.
* Known cis-pQTLs replicate in direction; the lead pQTL replicates on a second platform.
* Colocalization stable across priors and window; alleles and build match.
* Factors stable on held-out samples and seeds.

## Failure modes
* Batch equals group; sample IDs misaligned across layers.
* Gene symbols or unversioned IDs as keys.
* Deposit without consent (`data-stewardship`).

## Record and report
Log: question, date retrieved, sources, versions, not verified, recheck date. Report platform, features per filter, ID release, normalization, missing-value rule, covariates, overlap, seeds.
