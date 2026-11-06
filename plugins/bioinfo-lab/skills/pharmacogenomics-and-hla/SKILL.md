---
name: pharmacogenomics-and-hla
description: 'Use when calling human star alleles, diplotypes, or HLA types from WGS, WES, RNA, or arrays, or reporting drug-gene results. Not for general variant classification (variant-interpretation).'
---

# Pharmacogenomics and HLA

## Capability
Turn sequence or array data into star-allele and HLA genotypes, map them to phenotype by a named guideline, and state call confidence. Clinical use needs sign-off.

## Decide
1. Star alleles need an explicit record at every required position, reference and missing included. An absent position is a no call, not reference. Use all-sites or gVCF calls.
2. Genes with structural variants or paralogs (CYP2D6) need a structure-aware method on WGS or long reads. Copy number must be known to link a recommendation.
3. Unphased data: report ambiguous diplotypes as such.
4. HLA: method by data type; report two fields with the nomenclature release. Low depth at typing exons is a no call.
5. Phenotype comes from the current guideline and allele definitions; record versions.
6. Choose pairs by population allele frequency and evidence level (CPIC A/B; PharmGKB level 1A/1B); see `references/pgx-hla.md`.
7. Stop and ask: unknown copy number in a clinical request; HLA call disagrees with clinical typing; any return of results.

## Find current information
Per `current-methods-lookup`, ask: which matcher and allele definition release are current; which structure-aware caller is benchmarked independently; which HLA typer suits this data; which guideline version applies.
Sources in order: CPIC, PharmGKB/ClinPGx, PharmVar, IPD-IMGT/HLA and tool docs; independent benchmarks of recent years (PubMed, Europe PMC); preprints, labeled. Retrieve guidelines on the day of use.
Check date and ancestry. See `references/where-to-look.md`.

## Verify
* Lab-owned truth set with clinical or orthogonal typing (SBT, NGS, long-range PCR, copy-number assay) covering the reported alleles; concordance per locus, no-calls separate.
* Reference samples with published genotypes; two methods on one sample, explain discordance.
* Coverage per position; low depth makes false homozygotes.
* Repeat after any tool, release, or kit change.
Failing: no call; do not guess.

## Failure modes
Missing read as reference; unresolved CYP2D6 structure; mixed releases; sample order errors.

## Record and report
Log: question, date retrieved, sources, versions, NOT verified, recheck date. Report gene, diplotype, phenotype, guideline version, build, tool versions, confidence, confirmation.
