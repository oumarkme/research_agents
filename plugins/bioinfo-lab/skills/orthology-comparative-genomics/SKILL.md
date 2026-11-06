---
name: orthology-comparative-genomics
description: 'Use when inferring orthogroups, gene-family gain and loss, synteny, or whole-genome duplication across species. Not for tree building (phylogenetic-inference) or selection tests (species-tree-and-selection).'
---

# Orthology and comparative genomics

## Capability
Infer orthologs, family change, synteny, and genome duplications across species. A correct result justifies the species set, audits annotation quality, and backs each claim with two lines of evidence.

## Decide
1. Choose species for the question: ingroup, an outgroup, balanced clades. Justify each genome.
2. Audit each genome: assembly level, annotation method, date, completeness. Missing genes mimic loss; flag weak annotations.
3. Prepare proteomes: one isoform per gene (record the rule), no internal stops, consistent headers.
4. Run orthogroup inference with a rooted species tree if available; read hierarchical orthogroups at the node of interest.
5. For gain and loss, use a model on an ultrametric tree; state how very large families are treated.
6. For synteny and genome duplication, require block-level and synonymous-divergence evidence to agree.
7. Ask when the tree is uncertain at the node of interest or pipelines are mixed.

## Find current information
Follow `current-methods-lookup`. Ask: (1) which orthology method and release; (2) its recommended options; (3) which gain-and-loss and synteny tools are maintained; (4) recent benchmarks on your clade; (5) how primary transcripts are chosen. Sources in order: README and release notes; recent independent benchmarks (PubMed, Europe PMC); labeled preprints. Check date, maintenance, fit. See `references/where-to-look.md`.

## Verify
* Completeness per genome; a low score cannot support loss claims.
* Re-annotate a subset with one pipeline; family change should persist.
* Re-run with another method or tree and compare.
* Unassigned-gene fraction should be similar across comparable species; an outlier flags annotation or divergence.
* Family gene counts must sum to the proteome totals.

## Failure modes
* Annotation differences read as family change.
* Lineage-specific genes that are detection failures.
* Fragmented assemblies break synteny.
* Isoforms as paralogs.

## Record and report
Log: question, date, sources, versions, not verified, recheck date. Report species table (source, version, completeness), filters, options, tree, models, untested items.
