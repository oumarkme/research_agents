---
name: breeding-metadata-and-archives
description: 'Use when describing or sharing phenotype, sample, and sequence data from breeding or agricultural projects (MIAPPE, BrAPI, ontologies, FAANG, ENA, EVA). Not for general data layout or DMPs (data-stewardship).'
---

# Breeding metadata and archives

## Capability
Describe breeding data for reuse by a stranger and deposit it where it stays findable. A correct result has IDs that join across tables, ontology-coded variables, a named build, and a set license and embargo. Layout and DMPs: `data-stewardship`.

## Decide
1. Classify each data type (phenotypes, animal samples, reads, assemblies, variants, microbiome). Each has one community standard and one archive.
2. Plant phenotypes: use the community minimum-information standard (MIAPPE); name variables with crop or plant ontology terms, with method, scale, and unit.
3. System-to-system exchange: use BrAPI where both sides support it.
4. Farm animals: use FAANG metadata rules; parentage SNP exchange follows ICAR.
5. Reads go to an INSDC archive with BioSample records and the MIxS checklist that fits the sample. Assemblies to ENA or GenBank; variants to EVA, citing the assembly accession.
6. Set license, persistent ID, and embargo. Check `access-benefit-sharing-and-data-governance` before depositing germplasm data.
7. Collect metadata in the field book.

## Find current information
Follow `current-methods-lookup`. Ask: which version of each standard is current and which does the target archive validate; what the archive requires at submission; which ontology release holds our traits.
Search: the standard's own site, archive documentation (ENA, EVA, NCBI), then recent reviews in PubMed. Check version date and validator output.

## Verify
* Sample IDs join across phenotype, genotype, and read tables with zero orphans.
* Every variable has an ontology term, unit, and scale.
* Reference build and annotation release are in the VCF header.
* Run the archive validator before submission.
* A collaborator re-derives one statistic from the deposit alone.

## Failure modes
* Read sample names differ from the phenotype table.
* Free-text trait names.
* Variants against an unnamed assembly.
* Embargoed or restricted germplasm made public.

## Record and report
Log: question, date, sources, standard versions, not verified, recheck. Report standards used, accessions, validator results, license, embargo.

Seeds: `references/where-to-look.md`.
