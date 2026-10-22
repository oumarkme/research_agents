---
name: data-stewardship
description: 'Use when planning, organizing, documenting, or sharing research data: directory layout, metadata, data dictionaries, provenance, FAIR, plant phenotype standards, repositories, and data management plans.'
---

# Data stewardship

* Layout: `raw/` read-only with checksums, `processed/`, `results/`, `metadata/`, and a README with a data dictionary (column, type, unit, allowed values, missing code). Never edit raw files; every result traces to a command and versions (Sandve et al., 2013; Wilson et al., 2017).
* Metadata: one record per sample and per file, with stable IDs, species, tissue, assay, platform, build, and date. Plant trials: describe them with MIAPPE and exchange with BrAPI where the partner system supports it; check the current versions before use.
* FAIR: persistent identifiers, rich metadata, open formats, a license, and a stated access route (Wilkinson et al., 2016).
* Repositories: raw reads to ENA/SRA; controlled-access human data to a controlled repository (dbGaP or EGA), never a public one; polygenic scores to the PGS Catalog; variants to ClinVar only with consent and de-identification; code and small results to Zenodo or Dryad with a DOI.
* Data management plan: what is collected, formats, storage and backup, who can access, retention, sharing date, and who is responsible. Follow the funder's template when there is one.
* Do not share patient-level data, keep credentials in files, or rename files after release without a mapping table.

Sources (verified 2026-10-22): Sandve 2013, https://doi.org/10.1371/journal.pcbi.1003285; Wilson 2017, https://doi.org/10.1371/journal.pcbi.1005510; Wilkinson 2016, https://doi.org/10.1038/sdata.2016.18.
