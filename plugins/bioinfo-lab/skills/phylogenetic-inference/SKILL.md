---
name: phylogenetic-inference
description: 'Use when building a maximum-likelihood tree from DNA, codon, or protein sequences of any organism: alignment, trimming, model choice, support, rooting, reporting. Not for gene-tree discordance or selection tests (species-tree-and-selection).'
---

# Phylogenetic inference

## Capability
A tree with recorded, checked sequences, alignment, model, and root: orthologous input, converged search, support with a stated meaning, root chosen beforehand.

## Decide
1. State question, taxa, marker. Choose DNA, codon, or protein by divergence and saturation.
2. Check input: unique names, no duplicates or contaminants, one orthologous locus per taxon.
3. Use an aligner suited to the sequences; inspect the alignment.
4. Trim only for a stated reason, as a sensitivity analysis: compare trimmed and untrimmed trees.
5. Select the model by a criterion, per partition when loci differ.
6. Infer with a method that reports support; fix the seed; run independent searches.
7. Root with an outgroup fixed in advance; midpoint rooting assumes clock-like data. An unrooted tree has no direction.
8. Ask if the outgroup is distant, sequences are saturated, or key nodes have low support.

## Find current information
Follow `current-methods-lookup`. Questions: alignment and inference software for this data size and type; support measures and how the field reads them; model-selection practice; trimming evidence. Sources in order: tool docs, release notes, command references; benchmarks and reviews (PubMed, recent years); preprints, labeled. Check date, maintenance.

## Verify
* Known answer: simulate on a known tree under the chosen model; recover it.
* Independent searches reach equal best likelihood and one topology; read warnings.
* Two aligners, trimmed and untrimmed: key clades persist.
* Drop the longest branch and re-run (long-branch attraction).
* Support measures sit on different scales; report each with its cutoff.
Failure: report an unstable key node as unresolved.

## Failure modes
* Long-branch attraction; alignment errors in gap-rich blocks.
* Identical sequences; unconverged runs.
* Support read as probability.

## Record and report
Analysis-log: question, date, sources, versions, not verified, recheck date. Report versions, command lines, seed, alignment length and gap share, model per partition, support type, rooting, trimming comparison, untested items.

See `references/where-to-look.md`.
