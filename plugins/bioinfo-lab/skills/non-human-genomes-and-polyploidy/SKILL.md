---
name: non-human-genomes-and-polyploidy
description: 'Use when working on non-human genomes (crops, trees, livestock, companion, model, wildlife): reference, ploidy, heterozygosity, sex chromosomes, GBS, arrays. Not for prediction (genomic-prediction).'
---

# Non-human genomes and polyploidy

## Capability
Set reference, ploidy, and genotype coding for non-human data.

## Decide
1. Reference: the species community reference and annotation; record accession, version, FASTA md5; do not mix releases. None adequate: `genome-assembly-and-curation`.
2. Ploidy per sample and chromosome; diploid callers misgenotype polyploids. ZW, XY, and haplodiploid systems need sex-aware ploidy (judgment).
3. Polyploid calling: homoeologous reads create false SNPs; filter by mapping quality and subgenome markers. Call dosage from allele ratios; log depth floor.
4. GBS and RADseq: high missingness; filter by site missing rate, then impute.
5. Arrays: confirm probe positions on the current reference; drop multi-locus probes.
6. Marker density from LD decay.
7. Files: VCF GT of true ploidy; dosage matrix with the counted allele stated. Check tools that assume diploid human chromosomes.

## Find current information
Follow `current-methods-lookup`. Ask: which reference and annotation the species community uses; which polyploid, GBS, and assembly tools fit this ploidy. Sources in order: official docs and release notes; species consortium page; recent independent benchmarks (PubMed, Europe PMC); preprints, labeled. Check date, maintenance, benchmark, fit. Seeds: `references/`.

## Verify
* Replicate libraries give concordant dosages.
* With a pedigree, count Mendelian inconsistencies per marker; drop high-error markers (logged).
* Allele-ratio histograms peak at expected dosages; smeared peaks mean paralogous mapping.

## Failure modes
* Pedigree-genotype mismatch untested.
* Chromosome names differ across FASTA, GFF, VCF.
* Marker set and reads on different references.

## Record and report
Log: question, date, sources, versions, not verified, recheck date. Report accession and md5, annotation, ploidy model, filters, callers, marker counts.

See: `polyploid-genotyping-dosage`, `reduced-representation-genotyping`, `livestock-genotype-qc-imputation`, `popgen-inbreeding-ne-germplasm`, `genome-assembly-and-curation`, `gene-annotation-te-repeats`, `pangenome-and-pav`, `reference-genome-selection`, `plant-field-trial-gwas`, `breeding-metadata-and-archives`, `agricultural-microbiome`.
