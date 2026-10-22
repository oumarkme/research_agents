# bioinfo-lab

A bioinformatics, genetics, and breeding lab as a Claude plugin. Ten agents play lab roles (bioinformatician, statistician, breeder, clinical geneticist, writer, and others), each on the cheapest model and effort that does the job. Twenty-one skills hold the shared methods, from quantitative genetics and genomic prediction to variant interpretation, data stewardship, and ethics.

The plugin runs no hooks, starts no MCP servers, and sends no data anywhere. Skills load in chat, Cowork, and Claude Code; agents load in Cowork and Claude Code. Install:

```text
/plugin install bioinfo-lab --marketplace <owner>/<repo>
```

See the repository README for the roster, the efficiency design, and setup.
