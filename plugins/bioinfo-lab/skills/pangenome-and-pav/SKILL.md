---
name: pangenome-and-pav
description: 'Use when building or using a eukaryotic pangenome (graph or linear), calling presence/absence variation, or genotyping SVs across accessions or breeds. Not for bacteria (pangenome-analysis-prokaryote) or single-sample SV calling (sv-cnv-calling).'
---

# Pangenome and PAV (eukaryotes)

## Capability
Build and use a pangenome with traceable assemblies, one coordinate frame, and uniform gene calls. A correct result separates real PAV from assembly and annotation artifacts.

## Decide
1. State the question: SV discovery, reference-bias removal, gene PAV, or SV genotyping in a large panel.
2. Choose the structure: a linear collection suffices for gene PAV and core counts; a graph is needed for SV-aware mapping and genotyping.
3. Pick inputs of similar quality, haplotype-resolved if possible; check each with `genome-assembly-and-curation`; screen contamination.
4. Fix one coordinate frame (a reference path, agreed chromosome names).
5. Annotate every assembly the same way (`gene-annotation-te-repeats`).
6. Call gene PAV from orthogroups; confirm absences in reads or the genome.
7. Define core and dispensable by a stated threshold and sample count; show the pan-gene curve.
8. Ask when quality varies widely, ploidy is mixed, or the panel misses the target population.

## Find current information
Follow `current-methods-lookup`. Ask: (1) which graph builder suits the species and sample count; (2) which short-read graph genotyper and settings; (3) how recent benchmarks compare graph and linear callers; (4) the current PAV conventions for the kingdom. Sources in order: README and release notes; recent independent benchmarks and reviews (PubMed, Europe PMC); labeled preprints. Check date, maintenance, fit. See `references/where-to-look.md`.

## Verify
* Subset check: graph genotypes against a linear-reference caller and long-read calls; confirm absences by read mapping.
* Re-run with a leave-one-out set; core size should be stable.
* Report whether the rarefaction curve plateaus.
* Fail: trace discordant calls to assembly gaps or annotation.

## Failure modes
* Gaps and collapsed repeats called as deletions.
* Annotation differences called as PAV.
* Graph clipping removing large or repeat SVs.
* Uneven sampling biasing frequencies.

## Record and report
Log: question, date, sources, versions, not verified, recheck date. Report inputs, versions, reference path, filters, PAV method, core threshold, validation.
