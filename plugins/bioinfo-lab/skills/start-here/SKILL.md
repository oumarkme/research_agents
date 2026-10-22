---
name: start-here
description: 'Use when a user asks what this plugin can do, where to start, or which skill or agent to use, or when the request is vague.'
---

# Start here

Ask at most two questions, only if the answers change the route: what is the goal, and what data or files exist (none is fine). Infer the user's level from their words. No programming, server, or special software is required; web-tool routes exist for every step.

| If the user is | Example request | Route |
|---|---|---|
| Plant or animal breeder | "Rank my lines with genomic prediction" | `breeder`; `quantitative-genetics`, `genomic-prediction` |
| Physician or clinical geneticist | "Classify this variant" (public ID only) | `clinical-geneticist`; `variant-interpretation` |
| Wet-lab scientist or technician | "Plan QC and batches for 96 samples" | `sample-and-assay-planning`, `data-stewardship` |
| Bioinformatician | "Build and benchmark a calling pipeline" | `bioinformatician`; `sequencing-pipelines` |
| Statistician | "Check this mixed model" | `statistician`; `study-design` |
| Student or newcomer | "Explain GWAS, then show the steps" | `association-studies` in plain language |
| Project lead | "Plan aims; check my manuscript claims" | `research-planning`; `writer`, `reviewer` |
| Data manager or curator | "Document this dataset for sharing" | `data-steward`; `data-stewardship` |
| Anyone with a consent or privacy question | "Can I share these data?" | `research-ethics` (stop and ask the data owner) |
| Anyone needing a fact or reference | "What is known about this gene?" | `trusted-sources` |

Defaults: answer in the user's language and level, define each technical term once, give the next step, and say what you did not check. Never ask for patient-level data to be pasted into a prompt.
