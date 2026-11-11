---
name: agricultural-microbiome
description: 'Use when planning or reporting rumen, soil, or rhizosphere microbiome studies: sampling, controls, amplicon versus shotgun, host reads, reporting standards. Not for read-level analysis (amplicon-metabarcoding-analysis, metagenomics).'
---

# Agricultural microbiome

## Capability
Design and report a study so results survive batch, host, and site effects. A correct result has clean blanks, a recovered mock community, the right replication unit, and a reported host-read fraction. Read-level work: `amplicon-metabarcoding-analysis`, `metagenomics`.

## Decide
1. Question: composition (amplicon) or function, strains, genomes (shotgun).
2. Replication unit: animal, plot, or plant; model it as a random effect; never treat several samples per animal as independent.
3. Rumen: record route, time after feeding, diet; hold constant or model.
4. Soil and rhizosphere: write the protocol in full (depth, horizon, moisture, pH, plant stage, rhizosphere separation).
5. Controls in every batch: field blank, extraction blank, mock community; randomize samples over batches.
6. Host and plastid DNA: plan depth on the microbial fraction and remove host reads; record the fraction.
7. Report with a current reporting standard; deposit reads with sample fields (`breeding-metadata-and-archives`).

## Find current information
Follow `current-methods-lookup`. Ask: which reporting checklist fits our sample type; which sampling protocol is accepted for our host or soil; which host-depletion or primer choices were benchmarked; which reference catalog matches our host and diet.
Search: Genomics Standards Consortium pages, PubMed, labeled preprints. Check date, host match, independent evaluation.

## Verify
* Blanks hold few reads; taxa in blanks are flagged in samples.
* The mock community is recovered at expected composition.
* Technical replicates cluster; PCA by batch shows batch is not confounded with treatment.
* Amplicon and shotgun composition agree on a subset.
Failure: remove contaminants, rerun the batch, or state the limit.

## Failure modes
* No blank, so kit contaminants read as taxa.
* Batch confounded with treatment or site.
* Relative abundance read as absolute change.
* Reference catalog from another host.

## Record and report
Log: question, date, sources, checklist and catalog versions, not verified, recheck. Report unit, controls, batches, host fraction, checklist.

Seeds: `references/where-to-look.md`.
