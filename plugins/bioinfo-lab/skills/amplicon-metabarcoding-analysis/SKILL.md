---
name: amplicon-metabarcoding-analysis
description: 'Use when analyzing 16S, 18S, ITS, or other amplicon or eDNA metabarcoding reads: ASVs, taxonomy, controls, contamination, reporting. Not for shotgun metagenomes (metagenomics) or sampling planning (sample-and-assay-planning).'
---

# Amplicon and metabarcoding analysis

## Capability
Marker-gene reads become a sample-by-taxon table with false positives bounded by controls. Design matters more than software.

## Decide
1. Record marker, primers, platform, read length. Confirm biological and PCR replicates, extraction blanks, no-template and field blanks, and a mock community.
2. Remove primers before denoising.
3. Infer exact variants; truncation must keep pairs overlapping; check the error model. Variable-length markers need no fixed truncation.
4. State the unit (variants or clusters); clustering changes diversity.
5. Remove chimeras. Assign taxonomy with a database matching the marker and target taxa; fix its release and confidence cutoff.
6. Flag contaminants from controls with a statistical method; never subtract blanks blindly.
7. Log read loss per step; set a minimum-depth rule in the plan.
8. Ask if blanks hold near-sample reads, replicates disagree, or no reference covers the taxa.

## Find current information
Follow `current-methods-lookup`. Questions: denoising pipeline for this platform and marker; reference database and release; contaminant method; reporting standard for this sample type (human, environmental). Sources in order: tool docs and tutorials; database release pages; independent benchmarks (PubMed, recent years); preprints, labeled. Check date, maintenance.

## Verify
* Mock community: observed against expected variants; missing or extra ones measure error.
* Blanks carry few reads; shared taxa are suspect.
* Replicates agree; disagreement bounds detection.
* Error model fits observed errors.
* Share assigned per rank; many unclassified means database gaps.
Failure: fix primers, truncation, or database first.

## Failure modes
* Tag jumping and index hopping give false presences; use unique dual indexes.
* Database gaps give wrong near matches.
* Primers or pipelines differing by batch mimic biology.

## Record and report
Analysis-log: question, date, sources, versions, not verified, recheck date. Report design table, versions, read counts per step, database release, contaminant method, standard.

Seeds: `references/where-to-look.md`.
