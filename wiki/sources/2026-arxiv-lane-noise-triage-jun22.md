---
title: arXiv lane noise triage — overnight fetch 2026-06-22 (5 PDFs)
type: source
tags: [meta, triage, arxiv, digest, noise, reject]
keywords: [2606.16333, 2606.18055, 2606.18247, 2606.20495, 2606.20561, exa, broad-paper-lane]
related:
  - meta/daily-research-digest-cadence.md
  - sources/2026-arxiv-lane-noise-triage-jun20.md
  - sources/2026-arxiv-lane-noise-triage-jun21.md
  - sources/2026-arxiv-lane-noise-triage-jun20.md
  - sources/2026-arxiv-lane-noise-triage-jul15.md
  - sources/2026-digest-sweep-triage-jun23-25.md
maturity: draft
created: 2026-06-22
updated: 2026-07-15
read_status: skimmed
---

## Relations

@meta/daily-research-digest-cadence.md @sources/2026-arxiv-lane-noise-triage-jun21.md @sources/2026-arxiv-lane-noise-triage-jun20.md @sources/2026-arxiv-lane-noise-triage-jul15.md @sources/2026-digest-sweep-triage-jun23-25.md

## Raw Concept

- **Trigger:** overnight run after pass 21 disabled `*-arxiv` fetch; noise now enters via **broad `*-paper` queries** that occasionally return arXiv URLs mixed into Exa results.
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2606.*.pdf` (Jun 22 triage batch).
- **Retrieved:** from `research to be indexed/` 2026-06-22.
- **Read-status:** skimmed (titles, sweep metadata; no linked repos).

## Narrative

**Ingest pass 22 verdict: reject all five for FDM/AM wiki pages.** Third consecutive reject-all batch. On-topic AM papers remain in sweep as **publisher URLs** (`skipped-no-arxiv`).

| arXiv | Title (short) | Matched lane (likely) | Verdict |
|-------|---------------|----------------------|---------|
| 2606.16333 | Differentiable packing of irregular 3D objects | `fdm-print-quality-paper` / `vlm-*` (semantic "3D") | **REJECT** — container packing / graphics |
| 2606.18055 | MERMAID-v1 PET scanner prototype | broad paper (semantic) | **REJECT** — medical imaging |
| 2606.18247 | Visual verification for inference-time VLA steering | `vlm-manufacturing-paper` | **REJECT** — robotics policy improvement |
| 2606.20495 | Continuum robot resilience via motion planning | `soft-robotics-am-paper` (semantic) | **REJECT** — continuum robotics, not AM |
| 2606.20561 | TimeProVe — long-video temporal reasoning (ADL) | `vlm-manufacturing-paper` | **REJECT** — video understanding |

**Follow-up (2026-06-22):** disable **all** overnight PDF auto-fetch (`fetch.enabled: false`). Digest discovery continues; operator manual-fetch from sweep `P*` publisher rows. Future: optional title-keyword gate in `daily_research_fetch.py`.

## Snippets

> "Tier 3 autonomous ingest remains NO-GO." — @osint-wiki/concepts/cemini-wiki-ingest-workflow.md (via @meta/daily-research-digest-cadence.md)
