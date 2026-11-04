# MCP servers and tool integrations for bioinformatics, genomics, and human/plant/animal genetics (as of 2026-11-04)

Method note: GitHub repo pages were read through WebFetch (page summary by a small model; no commit dates were exposed, so "last commit" is mostly unknown; only GeneFoundry topic-page "last updated" dates are real). Search-engine results and directory listings (Glama, LobeHub, mcpservers.org) are marked "listing only". All fetches 2026-11-04. No patient-level data was used in any query.

## 1. Which public MCP servers exist per resource (repo, maintainer, stars, license, tools, remote/local, official?)

### Takeaway
Coverage is good for literature, variant/gene-disease curation (GeneFoundry, BioMCP), GWAS Catalog (official, EBI) and Galaxy (official). It is thin or absent for NCBI Entrez generally, UCSC (community only), Zotero (community), GEO/SRA, KEGG/Reactome standalone, nf-core (community), Bioconda (none found), AnimalQTLdb and livestock resources (none found). Almost all are single-maintainer community projects with low star counts; only a few are official.

### Cited Findings
Aggregators and multi-database servers
- BioMCP (genomoncology/biomcp): GenomOncology org, 672 stars, 120 forks, MIT, 9,073 commits (last-commit date not shown). Single CLI/MCP binary; 72 sources incl. PubMed, ClinVar, ClinicalTrials.gov, OncoKB, Reactome, MyGene.info, gnomAD, CPIC, OpenFDA. Local stdio (`biomcp serve`) or HTTP (`biomcp serve-http`, /mcp). Most commands need no credentials; optional keys NCBI_API_KEY, S2_API_KEY, OPENFDA_API_KEY, NCI_API_KEY, ONCOKB_TOKEN, ALPHAGENOME_API_KEY, DISGENET_API_KEY. States no telemetry or remote log upload. Install via script, `uv tool install biomcp-cli`, Homebrew, Docker, or a Claude Code plugin. README warns the `biomcp` PyPI name is an unrelated package; flags KEGG and COSMIC as licensing concerns. Not official (company-maintained, oncology focus). Read primary README. — [GitHub](https://github.com/genomoncology/biomcp)
- GeneFoundry (berntpopp, individual maintainer): 20+ "-link" repos, each 0-1 stars, updated 30 Oct-3 Nov 2026 (topic page). Variant/rare-disease relevant: clinvar-link (weekly bulk release, local index), vep-link (Ensembl VEP annotation and ID recoding), clingen-link (gene-disease validity, dosage), gencc-link, panelapp-link, hpo-link, hgnc-link, mondo-link, orphanet-link, genereviews-link, uniprot-link (SPARQL), spliceailookup-link, autopvs1-link (ACMG PVS1), mavedb-link, gtex-link, stringdb-link, clinpgx-link, mgi-link, pubtator-link. Topic page only (not each README) — [GitHub topic](https://github.com/topics/genefoundry)
- genefoundry-router (berntpopp): MIT, 6 stars, 380 commits, 14 open issues. FastMCP 3.x gateway federating 22 backends / 285 tools (incl. gnomad 22 tools, clingen 17, clinvar 6, vep 7, litvar 6, metadome 11) behind one Streamable-HTTP endpoint; exposes `search_tools` (BM25) + `call_tool` + pinned entry points, so the host sees few tool schemas. Fingerprints tool definitions against a reviewed baseline at startup and on schedule (rug-pull defense). "Research use only." Hosted: `claude mcp add --transport http genefoundry https://genefoundry.org/mcp`; self-host needs Python 3.14+ and uv. Caution: the hosted endpoint is a third party, so queries leave the machine; README says the caller's token is never forwarded upstream but does not describe logging or retention. Read primary README. — [GitHub](https://github.com/berntpopp/genefoundry-router)
- ToolUniverse (mims-harvard, Harvard Zitnik lab): Apache-2.0, 1.8k stars, 1,297 commits. 1000+ models/datasets/APIs/packages; native MCP server; "Compact Mode" reduces 1000+ tools to 4-5 discovery tools (page claims ~99% context saving); no telemetry claimed; keys stored locally. `uvx tooluniverse`, `uv pip install tooluniverse`, or Claude Code plugin from its marketplace. Anthropic's bio-research plugin lists it as an optional binary server. Read primary README. — [GitHub](https://github.com/mims-harvard/ToolUniverse), [bio-research README](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research)
- gwas-mcp (PyPI, 30+ tools across UniProt, Ensembl, NCBI Gene, ClinVar, GWAS Catalog, GTEx) and bioinformatics-mcp-server (PyPI, NCBI + UniProt): listing only, maintainers/stars not verified. — [PyPI gwas-mcp](https://pypi.org/project/gwas-mcp), [PyPI bioinformatics-mcp-server](https://pypi.org/project/bioinformatics-mcp-server/)

Literature
- PubMed (Anthropic-hosted): remote HTTP `https://pubmed.mcp.claude.com/mcp`, in bio-research .mcp.json; tools seen in this session: search_articles, get_article_metadata, get_full_text_article, find_related_articles, lookup_article_by_citation, convert_article_ids, get_copyright_status. — [bio-research .mcp.json](https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/bio-research/.mcp.json)
- cyanheads/pubmed-mcp-server: Apache-2.0, 166 stars, v2.12.0, 482 commits. 12 tools (search, fetch, fulltext, Europe PMC search/fetch, citation metrics/formatting, related, spell check, MeSH, citation lookup, ID convert). stdio default plus Streamable HTTP; no key needed; optional NCBI_API_KEY (3 to 10 req/s) and UNPAYWALL_EMAIL. Community. Read primary README. — [GitHub](https://github.com/cyanheads/pubmed-mcp-server)
- bioRxiv/medRxiv: Anthropic-hosted remote at `https://hcls.mcp.claude.com/biorxiv/mcp`; bio-research README credits deepsense.ai. Tool guide in this session states search is by date range/category only (no keyword or full-text search). — [.mcp.json](https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/bio-research/.mcp.json), [README](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research)
- Consensus: remote `https://mcp.consensus.app/mcp` (400M+ papers from Semantic Scholar, OpenAlex, PubMed per its server instructions; usage counters/upsell text). — .mcp.json above
- Europe PMC, OpenAlex, Semantic Scholar: only community servers found (article-mcp by gqy20; s2-mcp-server by smaniches, optional SEMANTIC_SCHOLAR_API_KEY; OpenAlex servers using OPENALEX_EMAIL/API_KEY). No official server found. Listing only. — [LobeHub article-mcp](https://lobehub.com/mcp/gqy20-article-mcp), [s2 listing](https://www.getdrio.com/mcp/io-github-smaniches-semantic-scholar-mcp)
- Zotero: 54yyyu/zotero-mcp is the most-starred (about 5.7k stars per GitTrend; 5.0k on 2026-09-12; MIT; `uv tool install zotero-mcp-server`); others kujenga/zotero-mcp, kaliaboi/mcp-zotero, oscardvs/zoteus are small. Third-party tracker numbers, not read from the repo. — [GitTrend](https://gittrend.io/repo/54yyyu/zotero-mcp)

Genes, variants, populations
- Ensembl: cyanheads/ensembl-mcp-server, Apache-2.0, 3 stars, 100 commits, registry version 0.7.1; 7 tools (list_species, lookup_gene, get_sequence, query_region, predict_variant, get_homology, get_xrefs); stdio or HTTP; public hosted instance at ensembl.caseyjhand.com (third party); Ensembl REST needs no key. Community. Read primary README. — [GitHub](https://github.com/cyanheads/ensembl-mcp-server), [registry](https://registry.modelcontextprotocol.io/v0/servers?search=ensembl&limit=20)
- ClinVar / ClinGen / gnomAD / UniProt / HPO: see GeneFoundry and BioMCP above (gnomAD also via router, 22 tools). Standalone gnomAD GraphQL servers (v2.1.1, v3.1.2, v4.1.0) exist as listings only, maintainer unverified. — [Glama listing via search](https://glama.ai/mcp/servers?attributes=category%3Abioinformatics&query=Information+about+MTS)
- dbSNP, SRA, GEO, generic NCBI Entrez: no dedicated server found; only inside multi-DB packages (PubMed via E-utilities; bioinformatics-mcp-server says NCBI). Gap.
- OMIM: no MCP server found. OMIM API requires a licensed key; GeneFoundry substitutes open sources (GenCC, Orphanet, Mondo, HPO, ClinGen). Inference.
- UCSC Genome Browser: community only (hlydecker/ucsc-genome-mcp, 12 tools; a @pipeworx package noting 0-based half-open coordinates). Listing only. — [Glama](https://glama.ai/mcp/servers/hlydecker/ucsc-genome-mcp)
- GWAS Catalog: official EBI hosted MCP at `https://www.ebi.ac.uk/gwas/mcp`, Streamable HTTP, no token, tools for traits/studies/associations plus ancestry labels, cohort IDs, variant consequences; individual tool names, rate limits, and release date not stated. Community alternative koido/gwas-catalog-mcp. Read primary docs page. — [EBI docs](https://www.ebi.ac.uk/gwas/docs/programmatic-access/mcp-server)
- Open Targets: remote `https://mcp.platform.opentargets.org/mcp` (listed under OpenTargets in bio-research README); tools in session: query/batch GraphQL, schema, search_entities. — [.mcp.json](https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/bio-research/.mcp.json)
- PDB/AlphaFold: found only inside plant-genomics-mcp (AlphaFold DB, PDBe, InterPro). Standalone not searched deeply. Gap.
- Reactome: inside BioMCP; KEGG: inside plant-genomics-mcp, but KEGG licensing is flagged by BioMCP README.

Workflow platforms
- Galaxy: galaxyproject/galaxy-mcp, official Galaxy org, MIT, 39 stars, 24 forks, 791 commits, PyPI `galaxy-mcp` (1.10.0 seen in listing). Tools: tool catalog search/run, IWC workflows, histories/datasets, upload/download, pages; optional `recommend_biocontainer` (resolves quay.io/biocontainers image) and a code-mode extra (search/get_schema/run). stdio default (long-lived GALAXY_API_KEY env); HTTP binds 127.0.0.1; non-loopback requires OAuth unless `--allow-unauthenticated`. Note: using a public Galaxy server uploads data to that server. Read primary README. — [GitHub](https://github.com/galaxyproject/galaxy-mcp), [PyPI listing](https://pypi.org/project/galaxy-mcp)
- nf-core: community "nf-core MCP Server" (Node, npx/Docker) reading local nf-core repos; listing only, source repo not located; not official. — [Glama](https://glama.ai/mcp/servers/wjlim/nf-core_mcp). Anthropic's bio-research plugin instead ships an nf-core Nextflow skill (rnaseq, sarek, atacseq) rather than an MCP server. — [README](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research)
- Bioconda: search found no MCP server. BioContainers is reachable only through Galaxy's optional `recommend_biocontainer`.

Plant and animal
- plant-genomics-mcp (musharna): MIT, 8 stars, 843 commits, README v1.29.1; 58 tools across 24 backends (Ensembl Plants, Phytozome, UniProt, AlphaFold DB, PDBe, InterPro, JASPAR, PANTHER, OrthoDB, AraGWAS, NCBI BLAST, Gramene, KEGG, STRING, ATTED-II, BAR; TAIR/PlantCyc listed). stdio needs no config; HTTP needs a >=32-char bearer token; no public endpoint. Single maintainer, young. Read primary README (tool count differs between README and repo description). — [GitHub](https://github.com/musharna/plant-genomics-mcp)
- Livestock/AnimalQTLdb/Animal Genome resources: search found no MCP server. mgi-link covers mouse only. — search result, no URL to cite.

### Inferences
- For a human-genetics lab the best-value candidates are GeneFoundry components (clinvar, vep, clingen, gencc, panelapp, hpo, hgnc; the router for one endpoint) and BioMCP, but both are one-person or vendor projects that appeared or changed within the last weeks; pin versions and prefer self-hosting.
- Official or institutional servers worth recommending without much caution: Anthropic-hosted PubMed/bioRxiv, EBI GWAS Catalog, Galaxy, Open Targets.
- Breeding side has only plant-genomics-mcp; livestock is uncovered, so the existing web lookups in `trusted-sources` remain necessary.
- Stars alone are weak maturity signals here: most useful servers have under 10.

### Gaps
- Last-commit dates for nearly all repos (page fetch did not show them); verify with `gh api repos/<owner>/<repo> --jq .pushed_at`.
- Official status of any NCBI, Europe PMC, UCSC, or gnomAD MCP; none found, but absence not proven.
- Not checked: standalone AlphaFold/PDB, Reactome, KEGG, dbSNP, GEO, SRA servers; the MCP Registry was queried only for "ensembl".
- Performance, accuracy, and whether the GeneFoundry servers are validated against upstream: not found.

## 2. Anthropic bio-research plugin: relevance and gaps

### Takeaway
The plugin bundles remote HTTP connectors for literature, drug discovery, and data repositories; only PubMed, bioRxiv, Consensus, Open Targets (and perhaps Wiley, Synapse) matter for a human-genetics and breeding lab. It offers no variant annotation, Ensembl, ClinVar, gnomAD, or plant/animal resource.

### Cited Findings
- `.mcp.json` servers (all `type: http`): pubmed (pubmed.mcp.claude.com), biorender, biorxiv (hcls.mcp.claude.com/biorxiv), consensus, c-trials (ClinicalTrials.gov), chembl, synapse (mcp.synapse.org), wiley (connector.scholargateway.ai), owkin (mcp.k.owkin.com), ot (Open Targets), benchling (empty URL). — [.mcp.json](https://raw.githubusercontent.com/anthropics/knowledge-work-plugins/main/bio-research/.mcp.json)
- README lists providers: NLM (PubMed), deepsense.ai (bioRxiv, ChEMBL, ClinicalTrials), Consensus, Wiley, Sage Bionetworks, OpenTargets, BioRender, Owkin, Benchling; optional binaries 10x Genomics txg-mcp and ToolUniverse; skills: single-cell QC, scvi-tools, Nextflow pipelines, Allotrope, problem selection. README does not state auth for each server. — [README](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research)
- bioRxiv server search is date/category only, no keyword search. — server instructions in this session.
- ChEMBL and ClinicalTrials.gov servers are drug-discovery oriented; ClinicalTrials `search_by_eligibility` takes demographic and clinical criteria (a patient-matching function, relevant to the privacy rule). — server instructions in this session.

### Inferences
- Relevant: PubMed, bioRxiv, Consensus, Open Targets (gene-disease evidence, target tractability), Synapse (if a consortium uses it), Wiley (journal access if licensed). Low relevance: ChEMBL, ClinicalTrials.gov, BioRender (figures conflict with the lab's own plotting skill), Owkin, Benchling.
- Gaps against the lab: variant annotation (VEP, ClinVar, gnomAD, ClinGen, SpliceAI), gene nomenclature (HGNC), Ensembl/UCSC coordinates, GWAS Catalog, plant/animal databases, reference management, GEO/SRA, workflow catalogs. GeneFoundry/BioMCP/GWAS Catalog/Galaxy/plant-genomics-mcp fill most.
- The user's session already has these connectors via the bio-research plugin, so bundling duplicates would collide; recommend instead of bundle.

### Gaps
- Authentication behavior, rate limits, and logging policy of the Anthropic-hosted servers not found in the README.
- Whether the Anthropic-hosted PubMed server logs queries: not found.

## 3. Safety: keeping patient-level data from leaving the machine; known MCP threats

### Takeaway
Remote MCP servers receive whatever the model puts in tool arguments, so the only reliable controls are structural: do not enable remote servers in sessions that touch patient data, deny by default with allowlists, add a PreToolUse hook that screens arguments, and prefer local/self-hosted servers. Known attacks (tool poisoning, rug pulls, indirect prompt injection, lethal trifecta) are real, and guardrail filters are not reliable.

### Cited Findings
Controls in Claude Code
- Scopes: local, project (`.mcp.json`, shared via VCS), user, plugin-provided, claude.ai connectors; precedence local, project, user, plugin, connectors; managed servers rank above all. Interactive sessions ask approval for project servers; in `claude -p` and SDK runs project servers load without asking unless `disabledMcpjsonServers`, `--setting-sources`, or `--strict-mcp-config` is used. — [MCP docs](https://code.claude.com/docs/en/mcp)
- Official warning: "Verify you trust each server before connecting it. Servers that fetch external content can expose you to prompt injection risk." — [MCP docs](https://code.claude.com/docs/en/mcp)
- Permission rules: `mcp__server`, `mcp__server__*`, `mcp__server__tool`; plugin servers use `mcp__plugin_<plugin>_<server>__<tool>`; deny globs `mcp__*` remove all MCP tools from context; allow globs only after a literal `mcp__<server>__` prefix; MCP rules with parentheses (argument matching) are skipped in settings files. — [Permissions docs](https://code.claude.com/docs/en/permissions)
- PreToolUse hooks match MCP tools by regex (`mcp__.*__write.*`), receive `tool_input` JSON on stdin, and block via exit code 2 or `permissionDecision: "deny"`; a matcher written against the bare server key will not fire for plugin servers. — [Hooks docs](https://code.claude.com/docs/en/hooks)
- Remote-server `url`/`headers` read credential env vars such as ANTHROPIC_API_KEY as empty, so a project cannot leak them. Plugin/project `headersHelper` runs without credential variables. — [MCP docs](https://code.claude.com/docs/en/mcp)
- `plugin validate` warns on a literal credential in headers and on http:// URLs to non-loopback hosts (v2.1.281+). — [Plugin reference](https://code.claude.com/docs/en/plugins-reference)
Threats
- Tool poisoning: hidden instructions in tool descriptions that users do not see but the model does; also rug pulls (description changed after approval) and tool shadowing across servers (emails redirected in the experiment). Mitigations: show full descriptions, pin versions and hash descriptions, cross-server data-flow boundaries. Invariant Labs, 2025-04-01. — [Invariant Labs](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- Lethal trifecta (private data + untrusted content + external communication); MCP makes accidental combination easy; guardrail products are not reliable; the dependable protection is not combining all three. Simon Willison, 2025-06-16. — [Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- Secondary blog roundup (not primary; figures unverified): a reported 84.2% poisoning success with auto-approval, GitHub-issue injection exfiltrating private repo data, CVE-2025-54135 (CurXecute) writing mcp.json before user rejection; OWASP MCP Top 10 in beta. Advice: disable auto-approval, scope tokens, authenticate remote endpoints, pin versions. — [Boomi](https://boomi.com/blog/mcp-attack-vectors-overview/)
- genefoundry-router fingerprints tool definitions and compares to a reviewed baseline on a schedule: a practical rug-pull mitigation. — [GitHub](https://github.com/berntpopp/genefoundry-router)

### Inferences
- Proposed lab policy (my synthesis): (1) ship no remote MCP server enabled by default; (2) allow only read-only lookup tools, listed explicitly in `allowed-tools` of the skills that need them; (3) a PreToolUse hook on `^mcp__.*` that rejects arguments matching sample-ID patterns, VCF-like lines with genotype columns, or any free text longer than a threshold, and permits only identifier patterns (rs\d+, HGVS, gene symbols, PMID, DOI, accessions); (4) never run MCP-enabled sessions in the same session that has read patient files, because the model itself can copy data into arguments; (5) prefer local/self-hosted servers (BioMCP stdio, plant-genomics-mcp stdio, Galaxy on a lab instance) but note a local stdio server still calls public APIs upstream, so the argument screen still applies; (6) pin versions, review tool descriptions on update.
- Patient data in a Galaxy upload or a ClinicalTrials eligibility search is a direct violation path; those tools should be denied outright.
- Hooks cannot see intent, only arguments; a hook is a backstop, not a guarantee. Argument-level deny rules are not available through settings (parenthesized `mcp__` rules are skipped), so argument screening needs a hook.

### Gaps
- Primary vendor security reports (Unit 42, Trail of Bits) were not retrieved; search returned only blogs.
- Data retention and logging policies of the hosted third-party servers (genefoundry.org, ensembl.caseyjhand.com, Anthropic-hosted connectors): not found.
- Managed-settings allowlist keys (managed-mcp page) were not read.

## 4. Packaging: bundling or documenting optional MCP servers in a plugin; context cost

### Takeaway
A plugin can ship `.mcp.json` or inline `mcpServers`, with `${user_config.*}` for keys and `${CLAUDE_PLUGIN_ROOT}` for bundled scripts, but a plugin-bundled server starts for every user who enables the plugin. For optional servers, ship an opt-in companion plugin or documented `claude mcp add` snippets, and rely on tool search to keep context cost low.

### Cited Findings
- Manifest `mcpServers` accepts a .json path, .mcpb/.dxt bundle (path or https URL), or an inline map; `.mcp.json` at plugin root loads first, later declarations replace earlier same-name servers. — [Plugin reference](https://code.claude.com/docs/en/plugins-reference)
- `userConfig` fields: type, title, description, required, default, options, multiple, sensitive; sensitive values go to the platform secure credential store, others to `pluginConfigs` in settings.json; reference as `${user_config.KEY}` in MCP config (headers, env, url), hook `args`; not allowed in shell-form hooks, monitors, or `headersHelper`. — [Plugin reference](https://code.claude.com/docs/en/plugins-reference)
- `defaultEnabled` (default true) controls whether the plugin starts enabled; `dependencies` link plugins. A plugin name must not start with `claude-` or `anthropic-`. — [Plugin reference](https://code.claude.com/docs/en/plugins-reference)
- MCP stdio servers receive CLAUDE_PLUGIN_ROOT, CLAUDE_PLUGIN_DATA, CLAUDE_PROJECT_DIR; env-var expansion `${VAR:-default}` works in command, args, env, url, headers. — [Plugin reference](https://code.claude.com/docs/en/plugins-reference), [MCP docs](https://code.claude.com/docs/en/mcp)
- Tool search is on by default: only tool names and server instructions load at session start; no fixed per-server cap; `ENABLE_TOOL_SEARCH=auto` loads tools upfront below 10% of context; server instructions and upfront-tool descriptions are cut at 4,096 characters, deferred descriptions at 16,384; `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` overrides; `anthropic/alwaysLoad` in `_meta` or `alwaysLoad` in config exempts tools from deferral; tool search is used on Claude Opus 4/Sonnet 4/Haiku 4.5 and later, earlier models load everything. — [MCP docs](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search)
- Output cap: `MAX_MCP_OUTPUT_TOKENS` default 25,000, warning at 10,000; text over 50,000 characters saved to file. — [MCP docs](https://code.claude.com/docs/en/mcp)
- Gateways that expose 3 tools (genefoundry-router `search_tools`/`call_tool`; ToolUniverse Compact Mode; Galaxy code-mode) are alternate context-saving designs. — [router](https://github.com/berntpopp/genefoundry-router), [ToolUniverse](https://github.com/mims-harvard/ToolUniverse), [Galaxy MCP](https://github.com/galaxyproject/galaxy-mcp)

### Inferences
- Recommended packaging for `bioinfo-lab`: keep the main plugin MCP-free; add a separate `bioinfo-lab-mcp` plugin with `defaultEnabled: false`, containing a vetted `.mcp.json` (pinned versions, e.g. `uvx biomcp-cli==<ver>`, `uvx galaxy-mcp==<ver>` deny-by-default for upload tools), a `hooks/hooks.json` PreToolUse argument screen matching `mcp__plugin_<name>_.*`, and a skill documenting the identifiers-only rule. Optional API keys (NCBI_API_KEY, S2_API_KEY) as `userConfig` with `sensitive: true`.
- Because skill `allowed-tools` and hooks must use the long plugin-scoped tool names, document those exact names; a hook on `mcp__BioMCP__.*` would silently never fire.
- With tool search on, context cost for many servers is small, but each connected server still adds instructions text (up to 4,096 chars); on older models cost is large. Prefer one gateway or BioMCP over eight small servers.

### Gaps
- Exact token counts per server not measured here.
- Whether `userConfig` values can be conditionally left empty for keyless servers without a prompt: not verified (use `required: false`).
- Managed-settings controls (`allowedMcpServers` and similar) not read.
