---
name: reference-genomes-and-liftover
description: 'Use when choosing a reference build or contig naming, or converting coordinates and VCFs between builds. Not for general build bug checks (genomics-pitfalls) or alignment pipelines (sequencing-pipelines).'
---

# Reference genomes and liftover

## Capability
One build per project, chosen before alignment, with contig names that agree across files and counted, checked conversions.

## Decide
1. If a collaborator, database, or panel fixes the build, follow it. Else reuse an indexed reference from the directory in CLAUDE.md if one is stated; else ask.
2. Match the build to the question: where annotation, frequency, and clinical resources live; whether repeats, centromeres, or SVs matter; whether a pangenome is needed. Non-human: `reference-genome-selection`; record accession and version.
3. Choose the sequence variant (alt-aware, no-alt, masked): `${CLAUDE_SKILL_DIR}/references/build-variants.md`.
4. Align, call, and annotate on one FASTA. Compare contig names and lengths across all files; rename with a contig map.
5. Lift over only when re-mapping reads is impossible. Never lift clinical-reporting variants.
6. After liftover, apply `${CLAUDE_SKILL_DIR}/references/liftover.md`. Stop and ask when many records fail, the source build is uncertain, or the chain is from another patch level.

## Find current information
Follow `current-methods-lookup`. Ask: which build target databases use now; which assembly is current for this species; which liftover tool and chain fit this data.
Sources in order: assembly provider (GRC, NCBI, Ensembl, UCSC) and tool docs; consortium page; independent evaluations of recent years (PubMed, Europe PMC); preprints, labeled.
Check release date, patch level. Seeds: `references/where-to-look.md`.

## Verify
* `@SQ` or VCF contig lines match the FASTA `.fai`.
* REF alleles equal the FASTA base at every site.
* Round trip: lift a random sample forward and back; report the fraction recovered.
* Known sites (ClinVar, rsIDs) sit at the expected position in the target build.
* Unmapped counts by contig; repeats and sex chromosomes fail more.
Failing: find the mismatch; re-run from reads.

## Failure modes
Mixed builds; strand flips; swapped REF; lifting SVs and X, Y, MT, unplaced contigs; wrong chain.

## Record and report
Log: question, date retrieved, sources, version chosen, NOT verified, recheck date. Report build, FASTA checksum, contig naming, chain, tool version, unmapped counts, REF mismatches.
