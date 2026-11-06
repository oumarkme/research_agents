---
name: repeat-expansions
description: 'Use when testing human samples for pathogenic repeat expansions (FMR1, C9orf72, RFC1, HTT) from short or long reads. Not for SNV, indel, or SV calling (sv-cnv-calling) or paralogs (difficult-genes-and-mito).'
---

# Repeat expansions

## Capability
Human clinical (other species: species catalog, same logic). Short reads screen, long reads size, an orthogonal assay confirms. Correct: sizes with method and support, plus the method's limit.

## Decide
1. Name locus, gene, motif (gene strand), build, disease. Stop if no locus.
2. Use a versioned locus catalog (coordinates, motif, strand). Check the motif on both strands and all rotations.
3. Short reads: an allele longer than the read has no spanning read. Report "at least N repeats", not a size.
4. Compare each call with same-batch controls; flag outliers, not cut-offs copied from one paper.
5. Long reads: read the full allele with interruptions; check support per allele, balance, and mapping.
6. Classify by the disease's curated source (GeneReviews, ClinGen, lab SOP), with date.
7. Confirm orthogonally: repeat-primed PCR (presence), fragment analysis (size), Southern blot or long reads (large alleles). Test FMR1 methylation separately.
8. Ask when a call is near the premutation or intermediate boundary, interrupted, or methods disagree.

## Find current information
Follow `current-methods-lookup`. Ask: which genotypers fit this read length and platform; which catalog release covers the locus; current clinical thresholds per locus; which methods handle interruptions and mosaicism. Search tool documentation, ClinGen, GeneReviews, then independent comparisons (PubMed, Europe PMC; preprints labeled). Check date, maintenance, fit.

## Verify
* A control with a known allele per reported locus, same kit and read length.
* A lone long allele with few reads is low confidence.
* Two methods agree; if not, ask.
* Failing: control mis-sized or allele missing. Do not report.

## Failure modes
* "No expansion" from short reads at a locus whose alleles exceed the read.
* Motif rotation or strand mismatch.
* One-allele dropout: expanded plus normal allele looks homozygous.
* Mosaicism read as one size; ONT sizing error.

## Record and report
Log (`analysis-log`): question, date, sources, versions, unverified, recheck. Report locus, catalog version, motif, build, sizes with support, interruptions, confirmation.

Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.
