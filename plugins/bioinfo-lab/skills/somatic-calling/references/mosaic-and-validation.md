# Mosaicism, purity, validation

Logic below is statistical, not tool-specific. Confirm any cutoff with the lab's validation data.

## VAF and purity
* Expected clonal heterozygous VAF is purity / 2 in a diploid region; correct for copy number elsewhere.
* A cluster at about half the top VAF cluster suggests a subclone.
* At low VAF, binomial sampling alone spreads the observed value; expected alt reads = depth x VAF.

## Mosaic variants in germline cohorts
* A caller run in a tumor-only mode also reports germline sites: filter by population frequency and by expected VAF below heterozygous.
* Compare with parents or other tissues. A variant in one tissue at intermediate VAF and absent in parents is a mosaic candidate.
* Rule out mapping artifacts in segmental duplications, cross-contamination, and index hopping.
* Confirm with a second method before any clinical statement.

## Detection limit
* Power to see k alt reads at VAF f and depth n follows the binomial; solve it for the design.
* Error rate sets a floor: without molecular barcodes, plain deep short-read data cannot separate very low VAF from error.
* Report the limit of detection from spike-ins, not from the formula alone.

## Clonal hematopoiesis
Age-related clonal hematopoiesis is common (Jaiswal, PMID 25426837); blood-derived tumor-only calls in those genes need a non-blood comparator.
