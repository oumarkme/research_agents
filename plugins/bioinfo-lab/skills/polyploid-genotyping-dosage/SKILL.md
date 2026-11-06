---
name: polyploid-genotyping-dosage
description: 'Use when calling or analyzing genotypes in polyploid crops as allele dosage (0 to ploidy). Not for reference choice and assembly (non-human-genomes-and-polyploidy) or the prediction model (genomic-prediction).'
---

# Polyploid genotyping and dosage

## Capability
Produce dosage genotypes, with uncertainty, that match true ploidy. A correct result has allele ratios on the i/ploidy grid, no collapsed paralogs, and dosage consistent with pedigree and replicates.

## Decide
1. Fix ploidy and type (auto-, allo-, segmental) per sample from cytometry or k-mer evidence.
2. Map to a reference holding all subgenomes or haplotypes; decide on multi-mapping reads.
3. Auto- and segmental polyploids: a caller with per-sample ploidy and an allele-bias model. Disomic allopolyploids on a reference with all subgenomes: diploid calling per subgenome, then check homeolog cross-mapping.
4. Keep dosage probabilities, not only best calls; set priors to the population type.
5. Filter on depth, missingness, and diagnostic fit, with limits read from plotted distributions.
6. Give models dosage and polyploid-aware relatedness.

## Find current information
Follow `current-methods-lookup`. Ask: which dosage callers fit our ploidy, population type, and platform; what minimum depth they need; which independent benchmark used real polyploid data; which relatedness and association tools take dosage.
Search: caller docs and release notes, then recent benchmarks (PubMed, Europe PMC), then labeled preprints. Check release date, maintenance, benchmark species.

## Verify
* Allele-ratio plot per marker: peaks at i/ploidy (tetraploid: 0, 0.25, 0.5, 0.75, 1). Shifted peaks mean allele bias; one wide peak near 0.5 means collapsed paralogs. Remap or drop markers.
* Families: dosage must obey expected segregation; count violations.
* Replicates: report dosage concordance.
* Two callers on a subset: disagreement shows method dependence.
* Known-answer test: simulate reads from known dosages at project depth and recover them.

## Failure modes
* Collapsed paralogs: excess heterozygosity, depth spike.
* Depth below the caller's need.
* Duplicated loci in GBS read as SNPs.
* Mixed ploidy pooled in one allele-frequency estimate.

## Record and report
Log: question, date retrieved, sources, caller and version, prior, not verified, recheck date. Report ploidy evidence, markers dropped per filter, allele-ratio plots, concordance, and how uncertainty entered the model.

See `references/where-to-look.md`. See `genomic-prediction`, `association-studies`.
