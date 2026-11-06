# Filter templates and handoff table

Write cutoffs as parameters in a config file, not in code. The values below are placeholders for the lab to set, not recommendations.

## Per-model checklist

| Model | Genotype pattern | Extra check |
|---|---|---|
| De novo | proband 0/1; both parents 0/0 | parental depth, allele balance, read view, paternity confirmed |
| AR homozygous | proband 1/1; parents 0/1 | ROH, deletion on the other allele (looks homozygous), coverage |
| Compound het | two variants in one gene, one from each parent | phase; both rare; not both from one parent |
| X-linked | male hemizygous; mother carrier | PAR regions, X-inactivation in female probands |
| Dominant inherited | affected parent carries it | penetrance, age of onset, unaffected carriers |
| Mitochondrial | heteroplasmy fraction | tissue; separate pipeline |

A homozygous call may hide a hemizygous deletion: check depth and the parent genotypes.

## Config keys to record

`max_faf`, `max_local_af`, `min_dp_proband`, `min_dp_parent`, `min_gq`, `ab_range`, `consequence_set`, `hpo_release`, `ranking_tool_version`, `ranking_data_version`, `gene_panel_version`.

## Handoff table columns

gene, HGVS (build, transcript), zygosity, model, frequency columns (with versions), consequence, scores (raw), ClinVar status and date, gene-disease validity, HPO match score, coverage at site, IGV notes, filters passed.

## Not examined list

Regions below the coverage minimum, genes without a disease association, SV and repeat callers not run, RNA not available, parent not sequenced.

## Reanalysis log

Date, versions changed, count of new candidates, decision, next date.
