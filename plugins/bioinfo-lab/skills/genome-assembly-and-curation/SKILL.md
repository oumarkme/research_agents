---
name: genome-assembly-and-curation
description: 'Use when assembling a eukaryotic genome from long reads and Hi-C: haplotype strategy, scaffolding, contamination screening, QC, curation. Not for bacteria (bacterial-genome-assembly-annotation) or gene models (gene-annotation-te-repeats).'
---

# Genome assembly and curation

## Capability
Produce a eukaryotic assembly with known quality and limits. A correct result matches the k-mer profile, has no foreign DNA, and passes independent QC.

## Decide
1. Profile the reads first (size, heterozygosity, ploidy). Ask if they disagree with the literature.
2. Choose the strategy by sample: heterozygous diploid (haplotype-resolved), inbred (collapsed, purging off), polyploid or single-platform (read the tool docs).
3. Screen contigs for foreign DNA with the correct taxon; keep organelles apart.
4. Scaffold with Hi-C, then inspect the contact map.
5. Curate a reference manually; log every cut, join, and flip as an AGP edit.
6. Score with several metrics: contiguity, gene-space completeness, k-mer QV and completeness, phasing.
7. Compare with the current consortium standard (VGP, EBP, ERGA).

## Find current information
Follow `current-methods-lookup`. Ask: (1) which assembler and scaffolder suit this read type and ploidy now; (2) which contamination screen and database release; (3) current consortium targets; (4) recent benchmarks of assemblers on your clade. Sources in order: README and release notes; VGP, EBP, ERGA pages; recent benchmarks (PubMed, Europe PMC); labeled preprints. Check date, maintenance, fit. Seeds: `references/where-to-look.md`.

## Verify
* Assembly size within the k-mer estimate; large excess means haplotigs or contamination.
* K-mer spectra: no missing or doubled content; duplicated BUSCO needs a k-mer check before purging.
* Hi-C map: strong diagonal, no off-diagonal blocks that indicate misjoins.
* Compare two assemblers on the same reads.
* On failure, fix before annotation.

## Failure modes
* Collapsed repeats; false duplications.
* Haplotype switches in the alternate set.
* Contamination inflating size.
* Misjoins visible only in the Hi-C map.

## Record and report
Log: question, date, sources, versions, not verified, recheck date. Report reads (type, depth, N50), versions, commands, strategy, metrics table, contamination removed, curation log, accessions. Bacteria: `bacterial-genome-assembly-annotation`. Downstream: `gene-annotation-te-repeats`, `pangenome-and-pav`.
