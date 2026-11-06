---
name: pathogen-genomic-epidemiology
description: 'Use when turning pathogen sequence data into consensus genomes, lineages, time trees, and outbreak reports with metadata and sharing. Not for isolate assembly (bacterial-genome-assembly-annotation) or run QC (run-qc-and-demultiplexing).'
---

# Pathogen genomic epidemiology

## Capability
A defensible tree and a reproducible report. Each claim traces to sampling, metadata, and a quality-gated genome set.

## Decide
1. State the question (link cases, name lineages, date an introduction, track spread); it sets sampling and tree type.
2. Metadata first: date with precision, place, host, specimen, method, sample-to-sequence link. Missing dates stop a time tree. Sensitive fields follow ethics approval (`research-ethics`).
3. Build consensus on a pinned reference with a depth rule and N mask; record primer scheme and caller.
4. Gate by completeness and ambiguity before the tree; report cutoffs.
5. Assign lineages with the pathogen's designation tool; record software and data release (assignments change).
6. Align, mask problem sites, build a maximum-likelihood tree. Date only after a clock-signal check.
7. Share sequences in an INSDC archive where allowed.
8. Ask if sampling is uneven, dates are missing, or transmission rests on SNP distance alone.

## Find current information
Follow `current-methods-lookup`. Questions: lineage nomenclature and tool for this pathogen; consensus pipeline for this primer scheme; time-tree tools; published linkage distance for this pathogen; current reporting standard and sharing terms. Sources in order: tool docs and release notes; WHO, ECDC, CDC, national references; INSDC; independent reviews (PubMed, recent years); preprints, labeled. Check date, maintenance, fit.

## Verify
* Negative controls give no genome; a known sample reproduces its lineage.
* Replicate sequencing gives one consensus.
* Root-to-tip distance rises with date, and the slope vanishes with shuffled dates.
* Two methods or references keep key clades.
Failure: flag or drop; do not date.

## Failure modes
* Reference or mask changing lineage calls; sampling bias read as spread.
* Recombination in the alignment.
* SNP cluster called an outbreak without epidemiology.

## Record and report
Analysis-log: question, date, sources, versions, not verified, recheck date. Report per STROME-ID, plus versions, cutoffs, accessions, unchecked items.

See `references/where-to-look.md`.
