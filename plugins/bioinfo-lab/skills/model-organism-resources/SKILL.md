---
name: model-organism-resources
description: 'Use when looking up genes, alleles, phenotypes, orthologs, or GO annotations for a model organism, or citing and downloading these resources. Not for crop or livestock databases (trusted-sources).'
---

# Model-organism resources

## Capability
Retrieve curated gene, allele, phenotype, ortholog, and GO data for model organisms with traceable IDs and releases. A correct result joins on stable IDs from one release and states how each call was made.

## Decide
1. Map the organism to its species database for curated detail; use a consortium portal for cross-species views.
2. Start from a stable ID, not a symbol. Symbols change. Record ID, symbol, and record date.
3. Treat an ortholog as an inference: record the method and release, and review one-to-many matches by hand.
4. Keep GO evidence codes: experimental and electronic evidence differ; transfer by orthology is a hypothesis.
5. Download bulk files from the resource, not by scraping. Do not mix releases across tables.
6. Ask when a gene has several IDs across releases, the strain is ambiguous, or files have moved between resources.

## Find current information
Follow `current-methods-lookup`. Questions: (1) which database is the current home for this organism and what does it now cover; (2) the current release and bulk-download route; (3) which ortholog method and evidence codes it uses; (4) the preferred citation; (5) license terms. Sources in order: the resource's own download and about pages and release notes; the Alliance of Genome Resources and Gene Ontology Consortium pages; recent database papers in NAR or GENETICS (PubMed); labeled preprints. Check release date and curation status. Seeds: `references/where-to-look.md`.

## Verify
* Join on stable ID and count unmatched rows; outdated IDs show up as non-matches.
* Spot-check a few genes against the live record.
* Compare the ortholog call with a second method; list disagreements.
* Confirm all tables carry the same release.

## Failure modes
* Outdated IDs matched to a newer annotation.
* Orthology from one release combined with GO from another.
* Annotated genes counted as studied genes: annotation depth follows research interest.

## Record and report
Log: question, date retrieved, sources, release chosen, what was not verified, recheck date. Report resource, release, access date, IDs, ortholog method, GO release and evidence codes kept, unmatched IDs.
