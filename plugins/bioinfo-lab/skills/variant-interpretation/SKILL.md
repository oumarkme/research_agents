---
name: variant-interpretation
description: 'Use when classifying or reviewing human germline variants: ACMG/AMP with ClinGen refinements, evidence table, build and transcript rules, report fields. Not for somatic variants or pipeline validation.'
---

# Germline variant interpretation

Goal: classify a human germline variant from combined, sourced evidence.

## What decides the class

* **Normalization:** HGVS (genomic with build, transcript with version, protein), left-aligned; state the build; pick the transcript by disease.
* **Evidence table**, one row per criterion: value, source, database release, retrieval date, access label (`trusted-sources`).
  * Population frequency: dataset, subset, ancestry match; databases under-represent some ancestries.
  * Computational: one calibrated predictor with tool, score, version, at the strength its calibrated thresholds allow (Pejaver, PMID 36413997); do not double count with PM1.
  * Functional and literature: verified PMIDs, ClinVar submitters, review status, and conflicts, gene-disease validity, HPO match.
  * Case-level: de novo with confirmed parentage, segregation, phase, phenotype specificity, other diagnosis.
* **Mechanism:** loss of function counts only when it is an established mechanism for the gene; apply the current transcript, exon, and reading-frame decision logic.
* **Combining:** use the current official framework; state which version and whether a gene- or disease-specific expert-panel specification overrides generic rules. Report class, criteria with strength, conflicts, and what evidence would change the class.
* **Phenotype fit:** gene and patient HPO terms must agree; a mismatch means an unrelated or incidental finding or a possible phenotype expansion, and the class is unchanged.

## Find current information
Follow `current-methods-lookup`. Ask: which ACMG/AMP guideline and ClinGen SVI refinements apply now; does the gene have an expert-panel specification; which CNV/SV standard; which secondary-findings list version. Sources in order: ACMG, AMP, and ClinGen pages (retrieve current text, record the retrieval date); ClinVar and ClinGen records. Never use remembered criteria or points. Seeds: `references/where-to-look.md`.

## Verify
* Agent output is a draft: a second reviewer re-derives the class from the table, and a qualified clinical laboratory geneticist signs any clinical class or report.
* Expert-reviewed variants are reproduced.
* HGVS round-trips between build, transcript, and protein.

## Failure modes
* Mixed builds or transcript versions; ancestry-unmatched frequency.
* Double-counting correlated evidence; prediction as proof.
* Stale ClinVar status; citing from memory.

## Record and report
Log: question, date retrieved, sources, guideline version, not verified, recheck date. Report gene; HGVS with build and transcript; zygosity; inheritance; class with criteria; ClinVar status and date; frequency source; follow-up; reanalysis date.
