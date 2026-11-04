# Domain-content gaps for a genomics, human genetics, and breeding lab assistant plugin (as of 2026-11-04)

Method note: about 17 web searches (snippet-level; full texts mostly not opened). Anything without a link is in Gaps as unverified. Repo not read, so "not reflected" is a candidate list to diff against bioinfo-lab, not a finding about it.

## 1. Standards and guidelines updated 2024-2026 that a variant-interpretation / clinical-genetics skill may lack

### Takeaway
Highest-value upgrades: (a) ACMG/AMP/CAP/ClinGen SVC v4.0 points-based Bayesian standard (in pilot; final release not confirmed), (b) ClinGen calibration of AlphaMissense/ESM1b/VARITY for PP3/BP4 (2025), (c) ACMG SF v3.3 (+ABCD1, CYP27A1, PLN; annual updates), (d) HGVS 21.1.x + MANE Select, (e) GA4GH VRS 2.0, (f) Taiwan PDPA 2025 amendment (effective date unset). CNV guideline: no 2025 revision found; 2020 ACMG/ClinGen points-based remains current.

### Cited Findings
- SVC v4.0 keeps P/LP/VUS/LB/B but moves to Bayesian points; one 2025 commentary describes a scale of <= -4 to >= 10 with VUS 0-5 split Low/Mid/High, gene-specific allele-frequency cutoffs, code names to change. Pilot in 2026: 17/20 variants reached >90% three-level concordance; earlier poster 28/30. Official release was "anticipated by mid-2026" with a year-long transition recommended; no final publication found by this search. — [Tempus pilot summary](https://www.tempus.com/publications/piloting-the-forthcoming-acmg-amp-cap-clingen-standards-for-sequence-variant-classification/); [zifornd v4 preview (secondary)](https://zifornd.com/?p=20577); [HUGO talk Apr 2026](https://www.hugo-international.org/wp-content/uploads/2026/04/Andreas-Laner-talk.-22April2026.pdf)
- Point-system precursor that skills can already encode: Tavtigian et al., naturally scaled point system for ACMG/AMP — [PMID 32720330](https://pubmed.ncbi.nlm.nih.gov/32720330/)
- Concern raised in commentary: new scale lets a variant reach LP from a single code, including benign side — same Tempus/zifornd sources (secondary; treat as opinion).
- ClinGen SVI PP3/BP4 calibration for 13 missense tools (Pejaver et al. 2022): pre-specify a single tool and use calibrated score thresholds, strength up to Strong — [PMC9748256](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9748256/); PMID 36413997.
- 2025 Genetics in Medicine brief report (Bergquist et al.) calibrated AlphaMissense, ESM1b, VARITY: each reaches Strong (pathogenic) and Moderate (benign) but only modest gain over earlier tools — [Bergquist 2025 PDF](https://www.ccs.neu.edu/home/radivojac/papers/bergquist_genetmed_2025.pdf); [UMN record](https://experts.umn.edu/en/publications/calibration-of-additional-computational-tools-expands-clingen-rec/). Exact thresholds not extracted.
- ACMG SF v3.3 (Genet Med 2025;27:101454; PMID 40568962): adds ABCD1, CYP27A1, PLN; GCK, RUNX1, SLC4A1 considered not added; ADA2 deferred; annual update cadence; Baylor effective 2026-01-12 — [ACMG release](https://www.acmg.net/acmg/UploadedPDFS/PDFDocuments/ACMG-Releases-2025-Update-to-Secondary-Findings-Gene-List-SF-v33final77.aspx); [PubMed](https://pubmed.ncbi.nlm.nih.gov/40568962/); [Baylor](https://www.baylorgenetics.com/product-updates/acmg-secondary-findings-v3-3/). Skill should say: check for a v3.4+ before use; the list is for opportunistic exome/genome reporting, not a Taiwan legal requirement.
- CNV: ACMG/ClinGen 2020 technical standards (Riggs et al., PMID 31690835) use a points-based framework; reviewer concordance 73.0% on 111 CNVs (64.9% in a 2022 study). No 2025 revision found — [PubMed](https://www.pubmed.gov/31690835/); [360dx](https://www.360dx.com/clinical-lab-management/acmg-clingen-publish-recommendations-interpretation-reporting-cnvs).
- HGVS: Hart et al., Genome Med 2024;16:149 (PMID 39702242): HVNC under HUGO, new site, versioning policy, EBNF grammar, recommends MANE Select, updated fusion guidance; point releases 21.1.0-21.1.4 exist — [PubMed](https://pubmed.ncbi.nlm.nih.gov/39702242/); [PMC11660784](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11660784/); [v21.1.4 announcement](https://groups.google.com/g/hgvs-nomenclature-announcements/c/bdp68oD9ARQ). Per-release changelog not verified.
- GA4GH VRS 2.0 approved 27 Mar 2025; Phenopackets and Beacon can adopt it (they currently use VRS 1.3) — [GA4GH news](https://ga4gh.org/news_item/variation-representation-specification-vrs-v2-0-is-an-approved-ga4gh-product); [VRS 2025 recap](https://groups.google.com/a/ga4gh.org/g/ga4gh-vr/c/PV5tEaqnGSw). 2025 approvals for Phenopackets/Beacon/htsget not confirmed.
- Reference resources: HPRC Release 2 announced 12 May 2025, 232 individuals, ~3x fewer misassemblies; preprint HPRC2 (2026) reports 460 haplotypes covering >99% of common variation in All of Us v8 — [HPRC R2](https://humanpangenome.org/hprc-data-release-2/); [IGSR](https://www.internationalgenome.org/data-portal/data-collections/hprc2); [preprint listing](https://sciety.org/articles/activity/10.64898/2026.07.21.739710). Peer-reviewed publication status not confirmed.
- Taiwan: TPMI >560,000 participants, 16 medical centers (Nature, Oct/Dec 2025) — [TPMI Nature PDF](https://tpmi.ibms.sinica.edu.tw/www/20251204_Nature_TPMI_Cohort.pdf); [EurekAlert](https://www.eurekalert.org/news-releases/1103946). TPMI says it operates under the Human Subjects Research Act; Taiwan Biobank under the Human Biobank Management Act (2010) — [Taipei Times 2023](https://www.taipeitimes.com/News/taiwan/archives/2023/02/11/2003794166). PDPA amendments passed 17 Oct 2025, promulgated 11 Nov 2025; new Personal Data Protection Commission; effective date set by the Executive Yuan and not confirmed; breach notification duties; government DPO requirement — [Baker McKenzie](https://www.bakermckenzie.com/en/insight/publications/alerts/2025/10/taiwan-amendment-to-personal-data-protection-act); [K&L Gates Jan 2026](https://www.klgates.com/New-Developments-in-the-Taiwan-Personal-Data-Protection-Act-1-13-2026). Sources disagree on whether the commission is already established.

### Inferences
- Candidate skill upgrade `variant-interpretation`: add a "v4 transition" block (points sum, gene-specific AF, pre-register tool and thresholds; record which framework version was used) and gate on checking ClinGen SVI for the final release.
- Candidate new skill `computational-predictors`: single pre-specified tool, calibrated thresholds, AlphaMissense/ESM1b/VARITY now calibrated; SpliceAI and AlphaGenome need separate treatment (see Q3).
- Candidate new skill `cnv-sv-interpretation` (2020 ACMG/ClinGen CNV points + SV-specific long-read issues).
- Candidate new skill/reference `taiwan-regulatory`: HSRA, Human Biobank Management Act, PDPA 2025 amendment, IRB/consent scope for long-read whole-genome data.
- Candidate `hgvs-and-identifiers`: HGVS 21.x syntax, MANE Select/Plus Clinical, VRS 2.0 IDs, Phenopackets for phenotype exchange.

### Gaps
- Final published SVC v4.0 text and point tables (not confirmed released).
- ClinGen SVI recommendations after 2025 (splicing, PVS1 v1.0 2018 refinements, PS3/BS3 functional 2019, PM2 downgrade to Supporting) not searched; those are from background knowledge, unverified here.
- CPIC / PharmVar current releases and Taiwan HLA-B*15:02 / HLA-A*31:01 guidance: search returned only nanopore HLA typing studies ([Siriraj 2023](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2023.1213457/full)); no CPIC/PharmVar primary source found.
- ACMG/AMP somatic (AMP/ASCO/CAP 2017; ClinGen/CGC/VICC oncogenicity SOP 2022) and mitochondrial (ClinGen MMG / ACMG-AMP mtDNA) guidance not searched.
- Human Subjects Research Act amendment status: no 2025 enacted amendment found; Taipei Times editorial (Jul 2025) only calls for review.
- ClinGen CNV/SV: no ClinGen long-read SV-specific guideline found.

## 2. Long-read (ONT) best practice

### Takeaway
No single 2025-2026 benchmark paper settles the germline ONT caller ranking from my searches. Version currency matters: Dorado is now at 2.x with v6.0 models, Sniffles2 recall improved sharply by v2.6.2, STRkit (Genome Res 2026) tops a GIAB TR benchmark on ONT. Skill should require pinning versions and re-benchmarking against GIAB HG002 on the lab's own chemistry.

### Cited Findings
- Dorado: v1.0.0 (21 May 2025) added v5.2 models and preview variant calling; GitHub releases show 2.0.0 with v6.0 DNA/RNA models, 2.0.1 (15 Jun 2026), 2.1.1 (30 Jul 2026); 1.3.3 bundled with MinKNOW 26.01 LTS. Nanopore's download history page appears stale — [Dorado releases](https://github.com/nanoporetech/dorado/releases); [Dorado v1.0.0](https://newreleases.io/project/github/nanoporetech/dorado/release/v1.0.0); [history page](https://nanoporetech.com/software/other/dorado/history).
- wf-human-variation 2.7.0 (May 2025): vendor-reported simulated 25 kb CNV recall 0.557 (Sniffles 2.0.7) to 0.903 (2.6.2); vendor result, not independent — [EPI2ME note](https://epi2me.nanoporetech.com/sniffles-262/).
- SV caller benchmarks: Helal et al. 2024 Sci Rep (5 callers, 4 aligners, HG002/NA12878, hg19, older versions) — [PMC10940726](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10940726/); Aydin et al. 2025 Sci Rep on somatic SV combinations (cuteSV 2.1.0, Sniffles2 2.2) — [Sci Rep 2025](https://rcastoragev2.blob.core.windows.net/1eaeba72849be7120df8c6e71a5add94/41598_2025_Article_92750.PMC11906795.pdf). A Genomics England poster dropped cuteSV for poor recall of clinically relevant SVs (conference poster, not peer reviewed) — [ONT poster](https://nanoporetech.com/api/assets/f/196663/f405d289f7/tim-freeman.pdf).
- Small variants: Clair3 and DeepVariant best on R10.4.1 bacterial data (14 species; SNP F1 99.99% sup); Clair3 v1.2.0 (Aug 2025) native GPU, ~5x faster — [eLife RP 98300](https://elifesciences.org/reviewed-preprints/98300v2); [Clair3 GitHub](https://github.com/HKU-BAL/Clair3). Bacterial, not human; reviewed preprint.
- Repeats: STRkit (Genome Res 2026, gr.280766.125; preprint bioRxiv 2025.03.25.645269) F1 0.9631 PacBio and 0.9544 ONT own benchmark; in GIAB TR benchmark on ONT beat LongTR (0.8786) and STRdust (0.7693); Straglr (Chiu 2021, PMC8361843) older — [Genome Res](https://genome.cshlp.org/content/early/2026/01/15/gr.280766.125); [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.03.25.645269.full.pdf); [Straglr](https://pmc.ncbi.nlm.nih.gov/articles/PMC8361843). Authors' own benchmark: weigh accordingly.

### Inferences
- Candidate skill `ont-long-read-variant-calling` (distinct from generic sequencing-pipelines): basecaller/model pinning (record Dorado version + model), POD5, modification calling in the same pass, kit/chemistry-to-model matching, GIAB HG002 truth sets with `truvari`/`hap.eval`-style comparison (names from background knowledge), phasing and haplotagging before SV/methylation, target-region/adaptive sampling QC.
- Candidate skill `repeat-expansion-calling`: choose caller by locus catalog, validate against orthogonal assay (repeat-primed PCR / Southern), report allele size + interruption + methylation.
- Candidate skill `long-read-methylation`: modkit pileup, strand/haplotype-aware, bedMethyl, CpG vs other contexts, imprinting and X-inactivation checks.

### Gaps
- No independent 2025-2026 human germline ONT SV benchmark identified (GIAB / Truvari-based head-to-head of Sniffles2, cuteSV, SVIM, pbsv, DeBreak, Severus). Needs a PubMed search on "GIAB HG002 ONT SV benchmark 2025".
- modkit, haplotype phasing (WhatsHap, LongPhase, HiPhase), Vamos, Straglr benchmarks, SMaHT, and T2T-based ONT variant calling not found. Current wf-human-variation and modkit version numbers not verified.
- Pangenome-aware calling (vg giraffe/DeepVariant, PanGenie) and GRCh38 vs T2T-CHM13v2.0 trade-offs: no sources collected.

## 3. Methods areas and AI/ML variant effect predictors

### Takeaway
Only the AI variant-effect area was covered by sources: AlphaGenome (Nature 2026) is a new regulatory/splicing predictor; ACMG-calibrated use is established only for missense tools (Q1). Single-cell, spatial, RNA-seq/isoform, metagenomics, proteomics were not researched.

### Cited Findings
- AlphaGenome (Avsec et al., Nature 649, online 28 Jan 2026; PMID 41606153): matches or exceeds best external models in 25 of 26 variant-effect evaluations; predicts 5,930 human tracks; non-commercial research license via GitHub/Kaggle/Hugging Face; 2026 commentary notes tissue-specific splicing remains challenging — [PubMed](https://pubmed.ncbi.nlm.nih.gov/41606153/); [Nature Asia release](https://www.natureasia.com/en/info/press-releases/detail/9222); [IJBS commentary](https://ijbs.com/v22p4144.htm).
- Existing bio-research plugin already provides scVI-tools and single-cell QC skills (from the available-skills list, not a web source), so single-cell is partly covered outside bioinfo-lab.

### Inferences
- Candidate `variant-effect-predictors` skill: table of tool, input, calibrated ACMG strength (only where ClinGen-calibrated), license limits (AlphaGenome non-commercial), and rule "no ACMG strength for uncalibrated tools (AlphaGenome, SpliceAI thresholds) without lab validation or ClinGen SVI splicing guidance."
- Candidate `rnaseq-isoform` skill (DESeq2/edgeR/limma-voom, long-read isoforms with IsoQuant/FLAMES/bambu, differential transcript usage) and `rna-for-diagnostics` (RNA-seq for VUS splicing): content not sourced here.

### Gaps
- SpliceAI/PrimateAI-3D/ESM current guidance, ClinGen splicing calibration; single-cell/spatial benchmark papers (e.g., scverse best practices), metagenomics (ONT, Kraken2/Bracken, MAGs), proteomics: not searched.

## 4. Breeding software and resources

### Takeaway
Little sourced progress; only GWAS tool original papers retrieved (no 2024-2026 comparison). Treat the list in the assignment as the candidate coverage set and verify versions and licenses via GitHub before encoding.

### Cited Findings
- REGENIE (Mbatchou et al., Nat Genet 2021) reported >150x faster than BOLT-LMM and >300x faster than SAIGE for step 1 on 50 UKB traits; SAIGE uses saddlepoint approximation for unbalanced case-control; fastGWA uses sparse GRM; Gurinovich 2022 found GENESIS, SAIGE, fastGWA-GLMM similar for binary traits in correlated data — [REGENIE](https://link.springer.com/10.1038/s41588-021-00870-7); [fastGWA preprint](https://www.biorxiv.org/content/10.1101/598110.full.pdf); [Gurinovich 2022](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.897210/pdf).

### Inferences
- Candidate upgrade to `association-studies`/`genomic-prediction`: a software-choice table (human biobank scale vs crop/livestock family structure: GCTA/fastGWA, REGENIE, SAIGE, PLINK 2, GAPIT/rMVP/sommer/BGLR/blupf90/ASReml-R/rrBLUP) plus a licensing column (ASReml commercial).

### Gaps
- No sources for BGLR, sommer, ASReml, blupf90+, rrBLUP, bigsnpr versions; crop/livestock reference genomes (e.g., Gramene, Ensembl Plants, AnimalGenome/FAANG), trait ontologies (Crop Ontology, Planteome, VT/ATOL, CO_xxx) and Taiwan-specific crops/livestock resources: not searched.

## 5. Research workflow gaps

### Takeaway
Only TRIPOD+AI verified. Other items below are untested leads.

### Cited Findings
- TRIPOD+AI: Collins et al., BMJ 2024;385:e078378, doi 10.1136/bmj-2023-078378; replaces TRIPOD 2015; applies to regression and ML models; one source reports a 27-item checklist plus an abstracts checklist; a fairness domain is claimed by a secondary blog (verify in the paper) — [PMC11025451](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11025451/); [blog (secondary)](https://www.journalmetrics.org/blog/tripod-ai-clinical-prediction-model-reporting).

### Inferences
- Candidate `reporting-checklists` skill: map study type to checklist (STREGA for genetic association, STARD, TRIPOD+AI for prediction/PRS, MI-CLAIM, CONSORT-AI) with a fill-in table. Only TRIPOD+AI sourced here.
- Candidate `peer-review-and-rebuttal`, `grants` (NSTC, NIH), `reproducible-environments` (conda-lock, Apptainer, Dockerfile), `power-and-sample-size`: need separate research.

### Gaps
- Sources for STREGA, STARD 2015, MI-CLAIM, CONSORT-AI, NSTC proposal formats, NIH 2025 data-sharing/DMS policy, bioRxiv/medRxiv deposit steps, power tools (e.g., GWAS power calculators, genpwr, gpower): not retrieved.
- Claims from a third-party "skills" site (AlphaMissense endorsed status "as of May 2026") are unverified and likely unreliable; not used.
