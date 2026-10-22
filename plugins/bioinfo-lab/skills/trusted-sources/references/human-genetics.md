# Human genetics and clinical genomics

Checked 2026-10-22 unless marked. Always record the genome build (GRCh37 or GRCh38) and the database release.

## Reference genomes, genes, transcripts

| Resource | Use | Query | Access |
|---|---|---|---|
| NCBI Datasets and RefSeq | Assemblies, annotations, accessions | `https://api.ncbi.nlm.nih.gov/datasets/v2/`; `ncbi.nlm.nih.gov/refseq/` | open |
| Ensembl | Genes, transcripts, regulation, orthologs, VEP | REST `https://rest.ensembl.org` (GRCh37: `https://grch37.rest.ensembl.org`); web `ensembl.org` | open; respect rate limits |
| UCSC Genome Browser | Tracks, assemblies, liftOver | `https://api.genome.ucsc.edu/`; web `genome.ucsc.edu` | open |
| GENCODE and MANE | Reference annotation; MANE Select and Plus Clinical transcripts | `gencodegenes.org`; `ncbi.nlm.nih.gov/refseq/MANE/` | open |
| T2T-CHM13 and HPRC | Gap-free reference and human pangenome | `github.com/marbl/CHM13`; `humanpangenome.org` | open |
| HGNC | Official gene symbols | `https://rest.genenames.org/fetch/symbol/<symbol>` (send `Accept: application/json`) | open |

## Variants

| Resource | Use | Query | Access |
|---|---|---|---|
| ClinVar | Submitted interpretations with review status | Web `ncbi.nlm.nih.gov/clinvar/`; E-utilities `db=clinvar`; monthly bulk files | open |
| dbSNP | rsIDs, alleles, frequencies | `https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/<number>` | open |
| dbVar | Structural variants | `ncbi.nlm.nih.gov/dbvar/` | open |
| gnomAD | Population allele frequency and constraint (state version, subset, build) | Web `gnomad.broadinstitute.org`; GraphQL API at `/api` (POST) | open |
| ClinGen | Gene-disease validity, variant curation expert panels, dosage sensitivity, Allele Registry | Web `clinicalgenome.org`, `search.clinicalgenome.org`; Allele Registry API `https://reg.genome.network/allele?hgvs=<HGVS>` | open |
| Ensembl VEP | Consequence prediction | `https://rest.ensembl.org/vep/human/region/<chr>:<start>-<end>:1/<alt>` | open |
| VariantValidator and Mutalyzer | Check and convert HGVS | `https://rest.variantvalidator.org/`; `mutalyzer.nl` | open |
| HGVS nomenclature | Notation rules | `hgvs-nomenclature.org` | open |
| NCBI GTR and MedGen | Genetic tests and condition records | `ncbi.nlm.nih.gov/gtr/`, `/medgen/` | open |
| DECIPHER | Developmental disorder cases and CNVs | `deciphergenomics.org` | key for some data |
| HGMD | Disease-associated variants | commercial vendor | licensed |
| LOVD | Locus-specific databases | `lovd.nl` (not reachable from the link check; verify) | open |

## Genes, diseases, phenotypes

| Resource | Use | Query | Access |
|---|---|---|---|
| OMIM | Gene-phenotype entries | `omim.org` (blocks scripts; API by registration; never hard-code a key) | key |
| Human Phenotype Ontology | Phenotype terms | `hpo.jax.org`; API `https://ontology.jax.org/api/hp/terms/<HP:id>` | open |
| Orphanet | Rare diseases | `orpha.net` | open |
| Monarch Initiative | Gene, disease, phenotype graph | API `https://api-v3.monarchinitiative.org/v3/api/` | open |
| GenCC | Gene-disease validity from many curators | `search.thegencc.org` | open |
| PanelApp | Gene panels with confidence ratings | `https://panelapp.genomicsengland.co.uk/api/v1/panels/` | open |
| MONDO and OLS | Disease ontology; ontology lookup | `mondo.monarchinitiative.org`; `https://www.ebi.ac.uk/ols4/api/` | open |

## Pharmacogenomics, cancer, trials, benchmarks

| Resource | Use | Query | Access |
|---|---|---|---|
| ClinPGx (formerly PharmGKB) and CPIC | Drug-gene annotations and dosing guidelines | `https://api.clinpgx.org/v1/data/gene?symbol=<gene>`; `https://api.cpicpgx.org/v1/` | open |
| NCI GDC and cBioPortal | Cancer genomics (TCGA and others) | `https://api.gdc.cancer.gov/`; `https://www.cbioportal.org/api/` | open; some data controlled |
| COSMIC | Somatic mutations | `cancer.sanger.ac.uk/cosmic` | key; license for commercial use |
| ClinicalTrials.gov | Trial records | `https://clinicaltrials.gov/api/v2/studies` | open |
| Genome in a Bottle | Truth sets for variant calling | `nist.gov/programs-projects/genome-bottle` | open |
| ACMG and ClinGen | Classification standards and secondary-findings list (check the current version) | `acmg.net`, `clinicalgenome.org` | open |
