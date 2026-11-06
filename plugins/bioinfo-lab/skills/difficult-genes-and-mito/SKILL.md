---
name: difficult-genes-and-mito
description: 'Use when a gene has a paralog, pseudogene, or segmental duplication (SMN1, GBA1, CYP2D6, HBA1) or an organelle variant needs calling. Not for general SV calling (sv-cnv-calling) or ACMG classification (variant-interpretation).'
---

# Difficult genes and mitochondrial variants

## Capability
Variants and copy number in ambiguously mapped regions and organelle genomes. Correct: a short-read call here is a hypothesis until the paralog is excluded.

## Decide
1. Check the gene against the project's difficult-region list (Human: also GIAB challenging genes). Other species: find paralogs by self-alignment. Record the build.
2. Keep MAPQ 0 and multi-mapped reads; inspect depth and soft clips.
3. Use a paralog-aware, locus-specific method or long reads, not the generic pipeline.
4. Separate copy-number change, gene conversion or fusion, and point variant; name the event.
5. Exclude pseudogene sequence before a pathogenic call; phase with long reads if either copy could carry it.
6. Confirm orthogonally when the result decides care.
7. Organelles: call on the species mito or plastid reference (Human: rCRS, chrM). Report heteroplasmy as a fraction with depth and tissue. Exclude nuclear copies (low fraction, nuclear-like depth).
8. Set the heteroplasmy floor by validation.
9. If unresolvable, state the limit; ask before a negative.

## Find current information
Follow `current-methods-lookup`. Ask: which tools support this locus, build, and assay; which curated benchmark is current; which mtDNA pipeline and frequency resource fit the species. Search tool repositories, release notes, GIAB, gnomAD, then independent benchmarks (PubMed, Europe PMC; preprints labeled). Check date, maintenance, fit.

## Verify
* Human: score the locus on GIAB challenging-gene benchmarks.
* Paralog depth ratio steps at copy-number change; MAPQ 0 reads with high mismatch mean paralog contamination.
* Two methods or an orthogonal assay agree; mito replicates reproduce fractions above the floor.
* Failing: methods disagree; report unresolved.

## Failure modes
* Pseudogene variant called pathogenic; conversion read as point variant.
* Mixed chrM names or reference revisions.
* Heteroplasmy below the floor.

## Record and report
Log (`analysis-log`): question, date, sources, versions, unverified, recheck. Report region, build, event type, copy number, phase, depth, orthogonal result.

Seeds: `${CLAUDE_SKILL_DIR}/references/where-to-look.md`.
