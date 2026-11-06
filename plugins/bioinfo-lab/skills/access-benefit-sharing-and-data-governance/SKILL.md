---
name: access-benefit-sharing-and-data-governance
description: 'Use when you sample, sequence, or share data from wild, germplasm, microbial, or community-held material across borders. Not for consent and authorship (research-ethics) or repository choice (data-stewardship).'
---

# Access, benefit sharing, and data governance

## Capability
Settle access permits and benefit-sharing terms before collecting, and carry provenance with every sequence you release. Law differs by country and changes; the current official text and the responsible office decide, not this skill.

## Decide
1. Origin: country, provider, collection date, collector, and whether the material is wild, held in a collection, or community-held.
2. Which national access measure applies in the provider country, and which user measure applies in ours.
3. Whether consent and agreed terms, or an exemption, exist for every sample group, and whether they cover sequencing, deposit, publication, export, and commercial use.
4. Whether a standard transfer agreement governs the material (for example, a crop in an international treaty system).
5. Whether sequence release is limited, and what the provider expects for digital sequence information (DSI).
6. For community data, who holds authority, agreed before collection.

## Find current information
Follow `current-methods-lookup`. Fetch and cite with retrieval date:
* Is the provider country a Party to the Nagoya Protocol, and which national measure applies? (CBD ABS Clearing-House, national focal point)
* What is the current DSI decision and its status? (CBD secretariat page)
* Which standard transfer agreement text applies? (treaty secretariat)
* What does your institution's research office require?
* Which community governance principles apply? (see `references/where-to-look.md`)

## Verify
Open the permit, certificate, or agreement. Check provider, sample group, dates, and permitted uses against the plan. A missing, expired, or narrower document (collection only, no export, no deposit) means stop and ask the institution's office or the national focal point.

## Failure modes
* Treating public archives as free of access rules.
* Permit covers collection but not export or commercial use.
* Archived sequence reused without provenance.
* Open data treated as community consent.

## Record and report
Store permit IDs, agreement references, provider contact, use limits, retrieval dates, and the responsible person in project metadata (`data-stewardship`) and the deposit. Report open gaps.
