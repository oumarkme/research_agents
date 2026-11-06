---
name: rare-disease-prioritization
description: 'Use when ranking human candidate variants in a proband, trio, or family: filter ladder, inheritance models, phenotype ranking, reanalysis. Not for ACMG classification (variant-interpretation) or calling (sequencing-pipelines).'
---

# Rare-disease prioritization

## Capability
A ranked table for the clinical geneticist plus an exclusion log. Human only (animals: OMIA).

## Decide
1. Inputs: pedigree, HPO terms, joint-called VCF, annotation versions (`annotation-and-databases`). Check sex and parentage from genotypes; stop if a trio fails.
2. Filter ladder, count logged per step: quality, frequency (filtering allele frequency, local data), consequence, model. Cutoffs are lab decisions in a config.
3. Models: de novo, recessive, compound heterozygous (singleton: "phase unknown"), X-linked, mitochondrial separately: `${CLAUDE_SKILL_DIR}/references/models.md`.
4. De novo: inspect reads in all three; record minimum parental depth; exclude segmental duplication. Parents may be mosaic.
5. Rank by HPO match; gene panels for virtual filtering.
6. Unsolved: add CNV, SV, repeats, non-coding, splice, RNA outliers (`rna-seq-and-splicing`).
7. Hand off table, filters, versions, poorly covered genes; classify in `variant-interpretation`.

## Find current information
Per `current-methods-lookup`, ask: which phenotype-ranking tool and HPO release are current and independently evaluated; which gene-disease and panel resources apply; current guidance on reanalysis.
Sources in order: tool docs; ClinGen, HPO, PanelApp; independent reviews of recent years (PubMed, Europe PMC); preprints, labeled. Fetch guidelines on the day of use; do not restate criteria.
Check date, ancestry fit. Seeds: `references/where-to-look.md`.

## Verify
* Spike a known pathogenic variant or solved case into the data; it must pass all filters and rank high, else fix the step that dropped it.
* Founder or under-represented groups: test the frequency step on a known positive.
* Compare two ranking methods. A large drop at one step marks a bug or cutoff error.

## Failure modes
Frequency cutoffs over-filter some groups; general HPO terms flatten ranks; versions differ within a family; homozygous may hide a deletion.

## Record and report
Log: question, date retrieved, sources, versions chosen, NOT verified, recheck date. Set reanalysis date and triggers at the first report (current guideline); rerun with new versions; list what was not examined.
