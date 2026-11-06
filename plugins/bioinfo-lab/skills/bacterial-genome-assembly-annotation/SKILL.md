---
name: bacterial-genome-assembly-annotation
description: 'Use when assembling, polishing, annotating, and checking a bacterial isolate genome from long or hybrid reads. Not for AMR calls (amr-genotype-phenotype) or many-genome comparison (pangenome-analysis-prokaryote).'
---

# Bacterial genome assembly and annotation

## Capability
One isolate's reads become a closed or near-closed genome: circular chromosome, plasmids as separate contigs with own depth, taxonomy matching the label.

## Decide
1. Check purity from reads first (stop if mixed); record species, reads, basecaller model, N50, depth.
2. One assembler gives a labeled draft; a finished genome needs independent assemblies, reviewed.
3. Polish with reads matching chemistry and model, then short reads. Compare before and after.
4. Check circularity, contig count, replicon sizes; flag duplicates, chimeras.
5. Annotate compared genomes with one tool and database release.
6. Set pass limits in the plan before running; no cutoffs from other taxa.
7. Ask if fragmented, contaminated, repeat-rich, or multi-chromosome.

## Find current information
Follow `current-methods-lookup`. Questions: assembly and consensus approach for this chemistry; matching polisher and model; annotation tool and database release; completeness tool and this taxon's limits. Sources in order: tool docs and release notes; NCBI/INSDC submission requirements; independent benchmarks (PubMed, Europe PMC, recent years); preprints, labeled. Check release date, maintenance, benchmark, fit to organism.

## Verify
* Known answer: assemble a strain with a closed public genome; compare.
* Map reads back: even depth per contig; breaks or clipped reads mean misassembly.
* Compare two assemblies; resolve each disagreement. Re-run on a read subsample; consensus must be stable.
* GC and taxonomy per contig match the species; outliers are contaminants.
* Frameshifts near the count in close relatives; excess means indel errors.
On failure: re-polish, re-assemble, re-culture.

## Failure modes
* Wrong polishing model; one assembler's circular call trusted.
* Plasmids lost to size selection or short-read assembly; annotation release drift.

## Record and report
Analysis-log: question, date, sources, version, not verified, recheck date. Report reads, tool versions, contig table (length, depth, circular, type), completeness, contamination, annotation release, checks not done.

Seeds: `references/where-to-look.md`.
