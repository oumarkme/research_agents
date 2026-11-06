# trusted-sources: routing

Read when you choose where to look or cannot reach a source.

## How to reach a source

Use what your setup allows, in this order: the official API through any HTTP client (curl, Python, R, a browser tool); an official client package; an MCP server; a bulk download with its release number; the web page. If a source is unreachable (offline, firewall, login, bot block), say so, use the next route, and record which. Some APIs accept POST only (gnomAD, Open Targets); without a POST-capable client, use the web page or a download. Respect rate limits and terms. Assume no server, conda, or containers.

## Which resource first

| Question | Start with |
|---|---|
| What is known about this variant? | ClinVar, then ClinGen, gnomAD, and the literature |
| Is this gene linked to a disease? | ClinGen, GenCC, OMIM, PanelApp |
| What does this gene or protein do? | HGNC, UniProt, Gene Ontology |
| Reference genome or annotation for a species | NCBI Datasets, Ensembl, or the species database |
| Published associations or polygenic scores | GWAS Catalog, PGS Catalog |
| Raw data of a published study | ENA, SRA, GEO, then controlled archives |
| A crop or livestock gene or QTL | The species database, Gramene, Animal QTLdb |
| Drug and gene | ClinPGx, CPIC |
| Does this DOI or citation exist? | Crossref, then PubMed |
