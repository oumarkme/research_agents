---
name: amr-genotype-phenotype
description: 'Use when detecting antimicrobial resistance genes and mutations in bacterial genomes and relating them to phenotype. Not for building the assembly (bacterial-genome-assembly-annotation) or core-genome work (pangenome-analysis-prokaryote).'
---

# AMR genotype and phenotype

## Capability
Detect resistance determinants and relate them to measured susceptibility. A correct result states genotype or phenotype and shows discordance per drug.

## Decide
1. Record species, input type, assembly QC. Stop if QC failed.
2. Match tool to input (assembly or reads) and question (acquired genes, point mutations, phenotype rules).
3. Run two tools when a claim depends on it; reconcile hit by hit.
4. Fix the database release; re-run before comparing batches.
5. Report any change to identity and coverage limits. Partial or split hits are flags, not calls.
6. Map genotype to phenotype only with a named rule source per drug and species. Without testing, write "predicted", not "resistant".
7. Take breakpoints from the current EUCAST or CLSI document; cite version.
8. Ask when the phenotype drives a clinical or regulatory decision, the species has no validated panel, or hits match no catalog.

## Find current information
Follow `current-methods-lookup`. Questions: maintained detection tools and databases; species and drugs the rules cover; current breakpoint version; current guidance on genotype-based prediction. Sources in order: tool docs and release notes; EUCAST, CLSI, NCBI Pathogen Detection, society guidance; independent benchmarks (PubMed, Europe PMC, recent years); preprints, labeled. Check release date, maintenance, benchmark, fit to species.

## Verify
* Tabulate genotype against measured result per drug (true and false positives, false negatives, gaps).
* Two tools agree, or differences are explained.
* A known gene spiked into a test assembly must be found.
Failure: unexplained discordance; check assembly, nomenclature, and rules before reporting.

## Failure modes
* Gene present but inactive; efflux, copy number, and regulatory changes missed.
* Plasmid genes split across contigs.
* Runs from different database releases compared.

## Record and report
Analysis-log: question, date, sources, versions, not verified, recheck date. Report tool versions, database release, limits, hit and discordance tables, untested drug-organism pairs.

Seeds: `references/where-to-look.md`.
