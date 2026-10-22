---
name: sample-and-assay-planning
description: 'Use when planning sampling, DNA or RNA extraction QC, assay choice, replicates, controls, batch layout, or sample tracking for a genomics study.'
---

# Sample and assay planning

1. Assay from question. State what must be detected and in how many samples, then choose: SNVs and small indels (short-read genome, exome, or panel); structural variants, repeats, and phasing (long reads); many markers across many lines for selection (SNP array, genotyping-by-sequencing, low-pass sequencing, or targeted genotyping); expression (RNA-seq); methylation (bisulfite or long-read). Check reference quality and budget before the choice is final.
2. Sampling. Record what you need to interpret the data later: tissue, time, and for plants field position, plant ID, and growth stage; for animals breed, sex, age, farm, and pedigree ID; for humans consent reference and collection protocol. Separate biological replicates from technical ones.
3. Extraction QC. Measure quantity, purity, and integrity with a named method. Set pass and fail thresholds before looking at results, following the assay and kit specifications. Flag failed samples; do not drop them silently.
4. Design. Spread samples across extraction, library, and sequencing batches so that batch does not line up with the main contrast. Include a positive control (a reference sample or a repeated internal sample) and a negative control. Choose replicate numbers from precision or power (`study-design`).
5. Tracking. Use unique, stable IDs and one sample sheet as the single source of truth. After sequencing, check identity (genotype concordance, sex check) and flag swaps and contamination.
6. Record kit, lot, instrument, run ID, date, and operator for every batch.

Do not relabel samples after submission, pool without a record, or change the plan after seeing the results without saying so. Format questions: `genomics-pitfalls`. Data handling: `data-stewardship`, `research-ethics`.
