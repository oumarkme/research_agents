# Function, regulation, GWAS, and biobanks

Checked 2026-10-22.

| Resource | Use | Query | Access |
|---|---|---|---|
| UniProt | Protein sequence, function, variants | `https://rest.uniprot.org/uniprotkb/<accession>.json` | open |
| AlphaFold DB and RCSB PDB | Predicted and experimental structures | `https://alphafold.ebi.ac.uk/api/prediction/<accession>`; `https://data.rcsb.org/rest/v1/core/entry/<id>` | open |
| InterPro | Domains and families | `https://www.ebi.ac.uk/interpro/api/` | open |
| Gene Ontology | Functional annotation | `geneontology.org`; `https://api.geneontology.org/api/` | open |
| Reactome | Pathways | `https://reactome.org/ContentService/` | open |
| KEGG | Pathways and modules | `https://rest.kegg.jp/` | open for academic use; license terms apply |
| STRING | Protein interaction networks | `https://string-db.org/api/` | open |
| GTEx | Tissue expression and eQTL | `https://gtexportal.org/api/v2/` | open |
| ENCODE | Functional genomics assays | `https://www.encodeproject.org/search/?type=Experiment&format=json` | open |
| Human Protein Atlas, Expression Atlas | Protein and gene expression | `proteinatlas.org`; `ebi.ac.uk/gxa` | open |
| GEO and ArrayExpress | Expression datasets | `ncbi.nlm.nih.gov/geo/`; `ebi.ac.uk/biostudies/arrayexpress` | open |
| GWAS Catalog | Published associations (use REST v2; the legacy path returns HTTP 410) | `https://www.ebi.ac.uk/gwas/rest/api/v2/` | open |
| PGS Catalog | Published polygenic scores | `https://www.pgscatalog.org/rest/` | open |
| Open Targets | Target-disease evidence | Web `platform.opentargets.org`; GraphQL `https://api.platform.opentargets.org/api/v4/graphql` (POST) | open |
| OpenGWAS | Summary statistics for Mendelian randomization | `gwas.mrcieu.ac.uk` (check the current token requirement) | key |
| 1000 Genomes, HGDP | Open reference panels | `internationalgenome.org`; gnomAD | open |
| Biobank Japan PheWeb, FinnGen | Public summary results | `pheweb.jp`; `finngen.fi` | open |
| UK Biobank, All of Us, TOPMed, Taiwan Biobank and other national biobanks | Individual-level data | `ukbiobank.ac.uk` (blocks scripts), `researchallofus.org`, `topmed.nhlbi.nih.gov`, `twbiobank.org.tw` | controlled |

Notes: eQTL and GWAS signals come from specific ancestries and tissues; state them. Use summary statistics from the build you analyze, and lift over only with a stated chain file.
