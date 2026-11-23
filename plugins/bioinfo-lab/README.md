# bioinfo-lab

A complete research group for bioinformatics, genetics, genomics and breeding across all organisms (research use only), as a Claude plugin. You decide and keep control of your data. Fourteen agents (bioinformatician, microbial genomicist, evolutionary genomicist, statistician, breeder, clinical geneticist, writer, literature reviewer, figure maker, and others) are optional helpers for parallel, bulk, or independent work. 85 skills are capabilities that look up current methods (`current-methods-lookup`) and verify results, from quantitative genetics and genomic prediction to pathogen epidemiology, phylogenetics, variant interpretation, data stewardship, research ethics, and the daily work of calling, annotation, omics assays, and cluster jobs.

The plugin runs no hooks, starts no MCP servers, and has no telemetry; the network is used only for lookups you request, the update check, and the slide-template download. Skills load in chat, Cowork, and Claude Code; agents load in Cowork and Claude Code. Install:

```text
/plugin marketplace add oumarkme/research_agents
/plugin install bioinfo-lab@research_agents
```

The plugin does not handle environment, safety, resource limits, privacy, or reply language; set those in your own `CLAUDE.md` (`/bioinfo-lab:claude-md-setup` helps). See the repository README for the roster, the design principles, and setup.
