---
name: gene-annotation-te-repeats
description: 'Use when annotating repeats, transposable elements, and genes on a eukaryotic assembly, or transferring an annotation. Not for building the assembly (genome-assembly-and-curation) or choosing a public annotation (reference-genome-selection).'
---

# Gene, TE, and repeat annotation

## Capability
Produce a soft-masked genome, a gene set with stated evidence, and QC numbers. A correct result has valid GFF, matching contig names, and counts consistent with close relatives.

## Decide
1. Confirm the assembly is final (name, md5); annotating a draft wastes the run.
2. Build a species-specific TE library, soft-mask, and keep both.
3. Pick the gene method by evidence: RNA-seq plus proteins, proteins only, none, or a close annotated relative to lift from.
4. Use RNA-seq from several tissues or stages, preferably long reads; check strandedness and adapters.
5. Assign function from homology and domains; label inferred terms.
6. Ask when protein BUSCO is far below assembly BUSCO or gene counts leave the relatives' range.

## Find current information
Follow `current-methods-lookup`. Ask: (1) which TE annotation method suits this TE landscape; (2) which gene predictor and evidence mode fit the data; (3) which liftover or ab initio model matches the lineage; (4) how recent benchmarks compare them. Sources in order: README and release notes; Dfam and curated repeat resources; recent independent benchmarks (PubMed, Europe PMC); labeled preprints. Check date, maintenance, fit to lineage. Seeds: `references/where-to-look.md`.

## Verify
* GFF validates; every contig name is in the FASTA index.
* Translate CDS: internal stops and missing starts counted.
* Protein-level completeness near the assembly score.
* Gene, exon, intron counts and lengths within close relatives' range.
* Few genes overlap masked TEs or carry TE domains.
* Compare two methods; check disagreements by hand.

## Failure modes
* Unmasked TEs yield false genes; over-masking hides multicopy genes.
* Lift flags (partial, low identity) kept silently.
* Mixed annotations in one comparison change expression estimates.
* GTF and GFF3 converted with sed.

## Record and report
Log: question, date, sources, versions, not verified, recheck date. Report assembly ID, library, masking percent by class, versions, commands, evidence, QC table, functional sources and versions.
