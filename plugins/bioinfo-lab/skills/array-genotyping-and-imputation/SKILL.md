---
name: array-genotyping-and-imputation
description: 'Use when processing SNP-array or low-pass data in any organism: array QC, strand and build, phasing, imputation, panel choice, info filters. Not for GWAS models (association-studies) or sample swaps (genomics-pitfalls).'
---

# Array genotyping and imputation

## Capability
Turn array or low-pass data into QC-passed, build-consistent genotypes and imputed dosages.

## Decide
1. Convert to plus strand on the panel's build; verify against panel REF/ALT, not the manifest label.
2. Sample QC (call rate, sex, heterozygosity, relatedness, ancestry) and variant QC (call rate, Hardy-Weinberg in controls, MAF). Skip Hardy-Weinberg for inbred lines. Take thresholds from a published protocol; log them.
3. Drop variants absent or mismatched in the panel. Resolve palindromic sites by frequency only if MAF is far from 0.5. A large frequency gap to the panel signals strand error or ancestry mismatch.
4. Panel: same build as the target and containing the study ancestry. Human: a public or local WGS panel. Other species: a breed panel; with pedigrees see `livestock-genotype-qc-imputation` (judgment).
5. Phase, then impute; low-pass data from genotype likelihoods.
6. Filter on the imputation quality metric by MAF bin and use; log the cutoff (judgment). Rare variants impute worst.
7. Human data whose consent bars external servers: impute on your own host (the one in CLAUDE.md, else ask), not a public server.

## Find current information
Follow `current-methods-lookup`. Ask: which phasing and imputation tools suit this sample size; which panels fit this ancestry or species; which QC protocol is current. Sources in order: official docs and release notes; panel documentation; recent independent benchmarks (PubMed, Europe PMC); preprints, labeled. Check date, maintenance, benchmark, fit. Seeds: `references/`.

## Verify
* Mask typed variants, impute, report concordance by MAF bin; low means wrong panel, build, or strand.
* Imputed frequencies track typed neighbors and the panel.
* PCA of dosages shows no batch shift versus typed data.
* Two panels compared on one masked set.
* Build, sample order, and variant count match the input.

## Failure modes
* Probe-name IDs; `chr` prefix mismatch.
* Multiallelics, duplicate positions, X PAR or ploidy mishandled.
* Hard calls where models need dosages.

## Record and report
Log: question, date retrieved, sources, versions, not verified, recheck date. Report array, build, strand method, QC counts, tools, panel, cutoff, concordance, variants kept.
