# Literature and identifiers

Link check 2026-10-22: every API row below returned data. Web pages that block scripts are marked.

| Resource | Use | Query | Access |
|---|---|---|---|
| PubMed | Biomedical literature, retraction and correction flags | NCBI E-utilities `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/` (the PubMed web page returns a cookie or bot notice to scripts) | open; free key raises the rate limit |
| PubMed Central | Full text of open articles | Web page `pmc.ncbi.nlm.nih.gov`; ID converter `https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=<id>&format=json` | open |
| Europe PMC | Literature search, full text, preprint records | `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=<q>&format=json` | open |
| Crossref | Resolve and verify a DOI, title, year | `https://api.crossref.org/works/<DOI>` | open |
| OpenAlex | Citations, authors, journals | `https://api.openalex.org/works/doi:<DOI>` | open |
| bioRxiv and medRxiv | Preprints (label `preprint`) | `https://api.biorxiv.org/details/<server>/<from>/<to>/<cursor>/json` | open |
| ICMJE | Authorship and AI-use policy | `https://www.icmje.org/` | open |

Notes: search PubMed with at least two wordings and MeSH terms. A DOI that does not resolve in Crossref is not a verified reference. Check the journal's own page for the final version and corrections.
