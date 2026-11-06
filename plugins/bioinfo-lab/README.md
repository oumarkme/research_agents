# bioinfo-lab

A complete research group for bioinformatics, genetics, genomics and breeding across all organisms (research use only), as a Claude plugin. You are the PI and decide; the main session is the deputy PI who plans, splits work, briefs members, and checks results. Fourteen agents are the group members (bioinformatician, microbial genomicist, evolutionary genomicist, statistician, breeder, clinical geneticist, writer, literature reviewer, figure maker, and others), each on the cheapest model and effort that does the job. 84 skills are capabilities that look up current methods (`current-methods-lookup`) and verify results, from quantitative genetics and genomic prediction to pathogen epidemiology, phylogenetics, variant interpretation, data stewardship, research ethics, and the daily work of calling, annotation, omics assays, and cluster jobs.

The plugin runs no hooks, starts no MCP servers, and has no telemetry; the network is used only for lookups you request, the update check, and the slide-template download. Skills load in chat, Cowork, and Claude Code; agents load in Cowork and Claude Code. Install:

```text
/plugin marketplace add oumarkme/research_agents
/plugin install bioinfo-lab@research_agents
```

See the repository README for the roster, the efficiency design, and setup.
