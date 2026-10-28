# Design basis

Where the design choices of this plugin come from. Anthropic items are vendor engineering and documentation pages: they justify design, not scientific claims. All were fetched on 2026-10-28.

| Choice | Source and what it says | Where used |
|---|---|---|
| Delegate rarely; brief precisely | Anthropic Engineering, "How we built our multi-agent research system": multi-agent runs use about 15 times the tokens of a chat; give each subagent an objective, output format, tool and source guidance, and boundaries; vague briefs caused duplicated work; embed effort rules; poor fit when agents share context or depend on each other. https://www.anthropic.com/engineering/multi-agent-research-system | `lab-team` |
| Short skills, load detail on demand | Anthropic Engineering, "Effective context engineering for AI agents": smallest set of high-signal tokens; right altitude; just-in-time retrieval; structured notes outside the context window; sub-agents return condensed summaries. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents. Claude Code docs: keep `SKILL.md` under 500 lines; descriptions are cut at 1,536 characters. https://code.claude.com/docs/en/skills.md | all skills |
| Progress file, claims ledger, one step at a time, verify before marking done | Anthropic Engineering, "Effective harnesses for long-running agents": progress notes plus git history bridge sessions; a JSON feature list that agents may only mark pass or fail; one feature per session; end-to-end verification before done. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | `analysis-log` |
| Distinct, well-described skills | Anthropic Engineering, "Writing effective tools for agents": distinct purposes, descriptions written for a new team member, refine from evaluation results. https://www.anthropic.com/engineering/writing-tools-for-agents | skill descriptions |
| Verify AI output; trace results to source | Anthropic Science blog introduction: AI can hallucinate results, can be too agreeable, and can get stuck on trivial problems for experts; feature posts state the role AI played. https://www.anthropic.com/research/introducing-anthropic-science | `lab-rules`, `analysis-log`, `research-ethics` |
| Enforce with hooks, not prose | Claude Code docs, best practices: instructions are advice; a rule with no exceptions belongs in a hook, deny rule, or managed setting. https://code.claude.com/docs/en/best-practices | README (limits) |

Not adopted: hooks shipped in the plugin (a false block on a stranger's machine costs more than a missed reminder), per-agent persistent memory (patient-level notes could be stored), and non-portable skill frontmatter such as `paths`, which fails on upload outside Claude Code.
