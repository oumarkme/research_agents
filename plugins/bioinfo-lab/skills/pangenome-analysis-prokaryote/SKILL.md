---
name: pangenome-analysis-prokaryote
description: 'Use when comparing gene content across many bacterial or archaeal genomes: core and accessory genes, annotation consistency, recombination. Not for single genomes (bacterial-genome-assembly-annotation) or graph pangenomes (pangenome-and-pav).'
---

# Prokaryote pangenome analysis

## Capability
A trusted gene presence-absence table with stated limits: uniform annotation, a defined species set, counts that survive a change of settings.

## Decide
1. State the question (content, structure, phylogeny). Define the species boundary and drop outliers before clustering.
2. QC every assembly; remove contaminated or fragmented ones, which inflate the accessory genome.
3. Re-annotate all genomes with one tool and release; mixed sources create false accessory genes.
4. Choose a clustering method that tolerates draft-assembly errors; test it on a known subset.
5. Treat the core cutoff as a choice: report it and test a second value.
6. Plot gene-count growth per genome added; an "open" claim needs it.
7. For phylogeny use the core alignment and test for recombination first.
8. Ask if sampling is biased (one clone), species are mixed, or paralogs matter.

## Find current information
Follow `current-methods-lookup`. Questions: maintained pangenome tools for draft assemblies; current species-boundary criteria and taxonomy source; recombination tool for this sampling; annotation tool and release. Sources in order: tool docs and release notes; GTDB and NCBI taxonomy; independent benchmarks (PubMed, Europe PMC, recent years); preprints, labeled. Check date, maintenance, benchmark, fit to genome count.

## Verify
* Known answer: closed genomes with simulated gene loss; recover it.
* Two methods on a subset; examine differing genes.
* Spot-check absences by protein search or read mapping; a gene at a contig edge is a gap, not a loss.
* Rerun on a random subset of genomes; counts should move little. Large shifts mean sampling or annotation noise.

## Failure modes
* Mixed annotation; draft assemblies splitting genes into false absences.
* Mobile elements inflating accessory genes.
* Uneven lineage sampling read as species pattern.

## Record and report
Analysis-log: question, date, sources, versions, not verified, recheck date. Report genome list and QC, tool versions, parameters, core definition, category counts, growth curve, recombination check.

See `references/where-to-look.md`.
