---
name: fungal-genomics
description: 'Use when assembling, annotating, or comparing fungal genomes (yeast, molds, plant and human pathogens). Evidence is thin; ask. Not for bacterial genomes (bacterial-genome-assembly-annotation) or amplicon profiling (amplicon-metabarcoding-analysis).'
---

# Fungal genomics

## Capability
Fungal genomes assembled, annotated, and compared with stated ploidy, purity, and annotation evidence. No fungus-specific guideline found; state choices as defaults.

## Decide
1. Record species, ploidy, strain, expected size, culture purity. Screen for bacterial or host contamination.
2. Prefer long reads; heterozygous or polyploid genomes may need haplotype-aware handling. Check mitochondrial and rDNA contigs (they collapse or inflate).
3. Mask repeats, then predict genes with RNA-seq or protein evidence from the clade; without evidence, accuracy is unknown.
4. Assess completeness with a lineage set matched to the clade. It counts single-copy orthologs, not gene models; low scores may mean the wrong lineage.
5. Compare gene counts with the closest public reference.
6. For populations, map to one reference, call with ploidy set, filter, then test structure. Check recombination before a tree or admixture model.
7. For pathogens, take resistance loci from species literature.
8. Ask if ploidy is unknown, no close reference exists, or evidence is ab initio.

## Find current information
Follow `current-methods-lookup`. Questions: gene-prediction and repeat-masking tools for this clade; lineage dataset and release; resistance loci for this species; any annotation standard. Sources in order: tool docs and release notes; JGI MycoCosm, NCBI, FungiDB; independent reviews (PubMed, recent years); preprints, labeled. Check date, maintenance, fit.

## Verify
* GC, taxonomy, and depth per contig show no outliers.
* Completeness holds across two lineage sets.
* Gene and intron counts near close relatives; RNA-seq reads map into predicted exons.
* Telomere repeats at contig ends.
* A known strain reproduces its published gene count.
On failure, re-screen, change evidence, or label a draft.

## Failure modes
* Mixed cultures read as large genomes; lineage mismatch.
* Gene counts compared across annotation methods.
* Mating type and aneuploidy ignored.

## Record and report
Analysis-log: question, date, sources, versions, not verified, recheck date. Report assembly stats, contamination check, masking, gene evidence, lineage set, unrun checks.

Seeds: `references/where-to-look.md`.
