---
name: sample-identity-and-contamination
description: 'Use when confirming sample sex, relatedness, pedigree, cross-sample contamination, or a suspected swap in sequencing or array data. Not for run-level QC (run-qc-and-demultiplexing) or variant calling (short-read-germline-calling).'
---

# Sample identity and contamination

## Capability
Show each sample is who the sheet says, related as recorded, and clean before interpretation. Correct: inferred facts agree with the record, or the gap is explained.

## Decide
1. Collect recorded sex, pedigree, sample type, earlier genotypes. Stop if sheet and pedigree disagree.
2. Fix one build and one site set (common, unlinked, biallelic). Other species: build it from the cohort or a population VCF.
3. Sex: compare sex-chromosome coverage and heterozygosity with the record, by the species' system (XY, ZW, haplodiploid; skip if none). Aneuploidy and mosaicism look like mismatches.
4. Relatedness: compare kinship with the pedigree; check duplicates, parent-child pairs, Mendelian errors. Inbred lines and clones are near-identical.
5. Contamination: estimate it, check heterozygous allele balance, and report depth beside it (low depth inflates the estimate).
6. Compare with the array or earlier sample on the same sites; check plate neighbors of a failure.
7. On failure, read `${CLAUDE_SKILL_DIR}/references/decisions.md`.
8. Ask when a clinical sample is swapped or a re-draw is needed.

## Find current information
Follow `current-methods-lookup`. Ask: which tools estimate sex, kinship, and contamination for this organism and depth; which panels match the build; the documented cutoffs and their basis; independent comparisons. Search tool documentation, then PubMed and Europe PMC (preprints labeled). Check date, maintenance, build, fit.

## Verify
* One signal is a flag; two independent signals support a swap.
* Known duplicates, trios, and a control give the expected kinship and no contamination.
* Two tools agree on a subset.
* Failing: use `decisions.md`; never relabel to fit the data.

## Failure modes
* Site set from another build or species.
* Contamination judged at low depth; swap called from sex alone.
* Population structure inflates kinship.

## Record and report
Log (`analysis-log`): question, date, sources, versions, unverified, recheck. Per sample: sex (recorded, inferred), relatedness versus expected, contamination with depth, concordance, decision, who edited the sheet.

Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.
