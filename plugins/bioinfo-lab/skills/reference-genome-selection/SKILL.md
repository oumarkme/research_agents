---
name: reference-genome-selection
description: 'Use when choosing or recording the reference assembly and annotation for a non-human eukaryote project, or deciding on a new one. Not for liftover mechanics (reference-genomes-and-liftover) or building the assembly (genome-assembly-and-curation).'
---

# Reference genome selection (non-human)

## Capability
Choose one assembly and one annotation for the question, reproducibly. A correct result gives the versioned accession, checksum, and annotation source and release.

## Decide
1. Name species, accession, cultivar or breed, and the question. Ask if the population differs from the reference.
2. Reuse an indexed project reference with a checksum (location in CLAUDE.md if stated; else ask).
3. List candidates from archives, portals, and the species consortium; prefer its release.
4. Compare level, haplotype type, contiguity, completeness, consensus quality (QV), gaps, organelles, year. Prefer chromosome-scale, curated, and community-used.
5. Match the annotation to the assembly version; use one annotation per comparison.
6. Check contig names across FASTA, GFF, and VCF; record which archive version you used.
7. Build a new one only if none fits (wrong cultivar or breed with large SV content, draft, missing haplotype): `genome-assembly-and-curation`.
8. Ask when references compete, the reference is a distant relative, or data used another build.

## Find current information
Follow `current-methods-lookup`. Ask: (1) which assemblies exist now and which the community uses; (2) the current annotation release for the chosen assembly; (3) how each archive names and versions accessions; (4) each assembly's QC report. Sources in order: NCBI, Ensembl, and species-database pages; consortium pages (VGP, EBP, ERGA); recent database papers (PubMed); labeled preprints. Check release date, curation. Seeds: `references/where-to-look.md`.

## Verify
* Checksum equals the archive's value.
* FASTA index contigs match GFF column 1 and VCF contigs; mismatch count is zero.
* Annotation assembly accession matches the FASTA.
* Map known marker or gene positions and confirm them.

## Failure modes
* Accession version dropped.
* Annotation from another patch.
* RefSeq and Ensembl IDs mixed in one table.

## Record and report
Log: question, date, sources, versions, not verified, recheck date. Report species, accession, source, download date, md5, annotation release, contig naming, reason, rejected candidates. Liftover: `reference-genomes-and-liftover`.
