---
name: livestock-genotype-qc-imputation
description: 'Use when cleaning livestock SNP-array genotypes: parentage and pedigree checks, sex and breed checks, imputation to a denser panel. Not for generic array QC (array-genotyping-and-imputation) or the prediction model (genomic-prediction).'
---

# Livestock genotype QC and imputation

## Capability
Deliver genotypes with confirmed identity, parentage, sex, and breed, imputed to a denser panel. A correct result has Mendelian-consistent families and accuracy measured on held-out animals.

## Decide
1. Put chips on one manifest, assembly, and strand before merging.
2. Animal and marker QC; read limits from plotted distributions.
3. Sex check: X heterozygosity and intensity against recorded sex. A mismatch is a swap or record error.
4. Parentage: count opposing-homozygote conflicts for each animal against recorded parents, using the species guideline (ICAR for cattle). Run parentage discovery before editing a pedigree.
5. Breed: PCA with reference breeds catches mislabeled crossbreds.
6. Reference panel: dense animals of the same breed and generation, with key ancestors.
7. Impute, and keep validation animals out of the reference. Hand off to `genomic-prediction`.

## Find current information
Follow `current-methods-lookup`. Ask: which parentage guideline edition applies to our species; which imputation tools are maintained and which a recent benchmark favors for our breed and chip density; which SNP sets serve parentage or breed proportion.
Search: ICAR and ISAG pages, tool docs and release notes, benchmarks (PubMed), labeled preprints. Check edition, release date, breed match.

## Verify
* Mendelian conflicts per family against the guideline; a bad family shows low imputation accuracy.
* Mask known genotypes in held-out animals; report correct-call rate and dosage correlation by chip and allele frequency.
* Compare two tools on your own mask.
* Allele frequencies agree between merged chips; a gap means strand or build error.
* Duplicate genotypes of one animal must match.

## Failure modes
* Wrong pedigree.
* Chips merged on mixed builds or strands.
* Accuracy taken from another breed.

## Record and report
Log: question, date, guideline and tool versions, panel, not verified, recheck date. Report chips, build, counts removed per step, parentage statuses, sex mismatches, accuracy bins. Ask before changing a pedigree.

Seeds: `references/where-to-look.md`, `icar-cattle-2023.md`.
