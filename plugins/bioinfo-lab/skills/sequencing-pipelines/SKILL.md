---
name: sequencing-pipelines
description: 'Use when building or validating sequencing analysis: short- and long-read QC, alignment, variant calling, benchmarking, assembly, pangenomes, and Nextflow or Snakemake workflows.'
---

# Sequencing pipelines

* Inputs: record instrument, chemistry, read length, and expected depth. Check raw QC before alignment; stop and report on a failed run instead of analyzing it.
* Align with minimap2 for long reads; use the project's short-read aligner and record its version. Mark duplicates, check coverage and insert size, and confirm sample identity against known genotypes when you have them.
* Call variants with a caller matched to the data (GATK or DeepVariant for short reads; a long-read caller for SV and repeat expansions). Normalize with `bcftools norm`; follow `genomics-pitfalls`.
* Benchmark before trusting: run `hap.py` or `vcfeval` against GIAB truth sets, stratified by region and variant type, and report precision and recall per stratum, not one number. Outside high-confidence regions the truth set says nothing.
* Clinical or diagnostic pipelines: validate on a representative sample set, define accuracy and precision per variant class, freeze versions, and keep a change log (AMP/CAP guideline, Roy et al., 2018).
* Assembly: assemble haplotype-resolved with hifiasm (HiFi, optionally ultra-long ONT and Hi-C), then check completeness (BUSCO or k-mer), contiguity, and phasing. Pangenomes: pick a graph tool by the question, and keep a linear reference for coordinates and annotation.
* Workflows: Nextflow (nf-core layout) or Snakemake. Pin each tool version (container, conda environment, module, or a recorded list), validate the sample sheet, use resumable runs, and store the command and config. Test on a small input first. Without a workflow manager, run the steps as a documented script or a Galaxy workflow.
* Do not tune on the truth set, do not mix builds, and do not re-run finished steps; use resume.

Sources and versions: `${CLAUDE_SKILL_DIR}/references/sources.md`.
