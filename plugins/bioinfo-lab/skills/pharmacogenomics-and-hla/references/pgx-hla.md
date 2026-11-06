# PGx and HLA input checklist

## Before a star-allele run
| Check | Why |
|---|---|
| Build matches the tool's requirement | Coordinates are build-specific |
| Every PGx position present as reference, variant, or missing | Missing means no call, not reference |
| Multiallelic sites normalized as the tool expects | Matching fails on split or merged records |
| Sample IDs and order match the sample sheet | `genomics-pitfalls` |
| Coverage at each PGx position | Low depth turns heterozygous into false homozygous |
| Tool, definition, and guideline versions logged | Alleles and phenotypes are revised |

## HLA validation set (lab-owned)
* Samples with clinical typing (SBT or NGS) covering the reported alleles.
* Concordance per locus at two fields with sample count; list no-calls separately.
* Re-run on every change of tool, nomenclature release, reference, or capture kit.

## Cohort-scale HLA
Imputation from array genotypes uses a trained model: choose one trained on a matched population and check call posterior before use.

## Machines
Use the host, containers, and thread cap in CLAUDE.md if stated, else ask; check the container directory before building an image. Graph-based typers need their reference; keep the path in the config.
