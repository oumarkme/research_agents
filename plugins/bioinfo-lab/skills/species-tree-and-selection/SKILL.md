---
name: species-tree-and-selection
description: 'Use when estimating a species tree from many gene trees or testing selection on codon alignments. Not for one gene or concatenated trees (phylogenetic-inference) or orthogroup inference (orthology-comparative-genomics).'
---

# Species trees and selection tests

## Capability
Estimate a species tree from gene trees and test selection on codon alignments. A correct result treats discordance as data, names the test and correction for each claim, and fixes the foreground set before the run.

## Decide
1. Choose loci: one ortholog per taxon, or a method for multi-copy genes. Paralogs in a single-copy method bias the tree.
2. Build gene trees with `phylogenetic-inference`.
3. State what support and branch lengths mean in the method (coalescent units are not time).
4. For selection: use an in-frame codon alignment of orthologs, screen for recombination, then pick the test by the question (gene-wide, branch, site, relaxed versus intensified).
5. Fix foreground branches before seeing results.
6. State the multiple-testing family (branches, sites, genes) and the correction.

## Find current information
Follow `current-methods-lookup`. Questions: (1) which species-tree method handles missing taxa and multi-copy genes; (2) which selection-test suite and release; (3) the correction each test needs; (4) recent benchmarks of alignment error in selection tests. Sources in order: tool documentation and release notes; method papers; recent independent benchmarks (PubMed, Europe PMC); labeled preprints. Check release date, maintenance, fit to taxa and data. Seeds: `references/where-to-look.md`.

## Verify
* Compare the species tree with a concatenated tree; list conflicting nodes.
* Re-run with a second aligner; a signal that vanishes was an alignment artifact.
* Remove long-branch gene trees; the result should hold.
* Run a neutral simulated alignment as a negative control; hits mean the pipeline is wrong.
* A significant gene-wide test means at least one site on one branch, not the whole lineage.

## Failure modes
* Frameshifts or misaligned codons read as selection.
* Gene-tree error read as discordance.
* Post hoc foreground choice.

## Record and report
Log: question, date, sources, version, not verified, recheck date. Report gene count, filters, versions, commands, support type, test, correction, sensitivity checks. Ask when a dated tree, network, or unsourced codon model is needed.
