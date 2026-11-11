---
name: open-science-reproducible-paper
description: 'Use when you assemble the reproducibility package for a paper: code, environment, workflow, deposits with DOIs, preprint, and journal openness policy. Not for daily logs (analysis-log) or directory layout (data-stewardship).'
---

# Open science and the reproducible paper

## Capability
A stranger should rerun the analysis from raw data to every figure with one documented command. Journal and funder openness policies change; the target venue's current text decides what is required.

## Decide
1. Claims first: each figure, table, and number maps to a script and input (`analysis-log`).
2. Every step scripted from raw data, no manual edits, under version control with a tagged release.
3. Environment captured: tool versions, lock file or container digest, seeds, genome builds.
4. One entry command and a small test dataset.
5. Where data and code are deposited (archive with DOI), under which license, and which restrictions apply and why.
6. Whether to post a preprint, and when.

## Find current information
Follow `current-methods-lookup`. Fetch and cite with retrieval date:
* What are the target journal's data, code, and preprint policies? (journal author guidelines)
* What does the funder require? (funder policy page)
* Which archive fits the data type and issues DOIs? (`data-stewardship`; archive terms page)
* What is the current openness-standards framework and our level? (see `references/where-to-look.md`)
* Does the institution have deposit or license rules? (research office)

## Verify
Clone fresh on a clean machine, run the test dataset, and compare one output with a stored checksum. Check that deposit DOIs resolve, match the paper, and carry licenses, and that no absolute paths or credentials remain. A failed rerun, an unresolved DOI, or a statement that conflicts with journal policy means fix it or ask the journal editors before submission.

## Failure modes
* Code "available on request."
* Tool installable today, not in two years.
* Notebook run out of order.
* Deposit made after the paper, DOIs missing.

## Record and report
Store release tag, DOIs, license, environment digest, policy URLs with retrieval dates, and the responsible person in the README. Report the availability statement and any restriction with its reason.
