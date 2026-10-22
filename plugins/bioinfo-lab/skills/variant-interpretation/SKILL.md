---
name: variant-interpretation
description: 'Use when classifying or reviewing germline variants: ACMG/AMP with ClinGen refinements, evidence table, build and transcript rules, report fields.'
---

# Germline variant interpretation

Standard: ACMG/AMP 2015 (Richards et al.) with ClinGen SVI refinements and, where one exists, the gene- or disease-specific ClinGen Variant Curation Expert Panel (VCEP) specification, which overrides generic thresholds. Check the current specification and ACMG secondary-findings list version before reporting; do not rely on remembered thresholds. CNVs and SVs follow the ACMG/ClinGen CNV standard.

## Workflow

1. Normalize: HGVS (genomic with build, transcript with version, protein), left-aligned; MANE Select transcript unless the disease requires another. State GRCh37 or GRCh38.
2. Evidence table, one row per criterion, with value, source, database release, date, and access label (`trusted-sources`):
   * Population: gnomAD (version, subset, filtering allele frequency, homozygote count) and a population-matched biobank when available; gnomAD under-represents many ancestries, so state the ancestry match.
   * Computational: calibrated predictors (state tool, score, version); splice predictors; conservation. Prediction alone never reaches strong evidence on its own.
   * Functional and literature: PubMed (verified PMIDs), ClinVar (submitter count, review status, conflicts), ClinGen gene-disease validity, OMIM, HPO match.
   * Case-level: de novo (confirmed parentage), segregation, phase (trans/cis), phenotype specificity, other diagnosis in the same patient.
3. Mechanism: loss-of-function must be an established mechanism for the gene; apply the ClinGen PVS1 decision tree (transcript, last exon, NMD, reading frame, exon importance).
4. Combine: use the point-based Bayesian framework (Tavtigian) or the ACMG table; state which. Report the classification and the criteria with strength, plus conflicts and what evidence would change the class.
5. Phenotype fit: ask whether the gene and the patient's HPO terms agree; a pathogenic variant in a non-matching gene is a secondary finding or a non-diagnosis.

## Report fields

Gene; HGVS (build, transcript); zygosity; inheritance; classification with criteria; ClinVar status (date); frequency (version); evidence summary; recommended follow-up (segregation, functional test, reanalysis date). Patient-level data never goes into queries; query by rsID, HGVS, or gene only.

Sources (verified 2026-10-22): Richards 2015, https://doi.org/10.1038/gim.2015.30 · Riggs 2020 (CNV), https://doi.org/10.1038/s41436-019-0686-8 · Tavtigian 2018, https://doi.org/10.1038/gim.2017.210 · Tavtigian 2020 (points), https://doi.org/10.1002/humu.24088 · Smedley 2015 (Exomiser), https://doi.org/10.1038/nprot.2015.124. Plan reanalysis of unsolved cases and name the date in the report.
