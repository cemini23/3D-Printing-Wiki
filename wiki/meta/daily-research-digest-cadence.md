---
title: Daily research digest cadence (3d-printing)
type: concept
tags: [meta, automation, discovery, federation, k93]
keywords: [daily-research-digest, exa, sweep, inbox, federated-digest, launchagent]
related:
  - concepts/fdm-printing.md
  - concepts/ai-design-tools.md
  - concepts/print-farm-operations.md
  - sweeps/_daily-template.md
  - sweeps/2026-06-01-daily.md
  - sweeps/2026-06-02-daily.md
  - sweeps/2026-06-03-daily.md
  - sweeps/2026-06-04-daily.md
  - sweeps/2026-06-05-daily.md
maturity: draft
created: 2026-06-01
updated: 2026-06-05
cross-wiki-source: "@osint-wiki/concepts/federated-daily-research-digest.md"
---

## Relations

@concepts/fdm-printing.md @concepts/ai-design-tools.md @concepts/print-farm-operations.md @sweeps/_daily-template.md @sweeps/2026-06-01-daily.md @sweeps/2026-06-02-daily.md @sweeps/2026-06-03-daily.md @sweeps/2026-06-04-daily.md @sweeps/2026-06-05-daily.md

- @osint-wiki/concepts/federated-daily-research-digest.md — federation install kit (K93 canonical)

## Raw Concept

Cross-wiki automation installed 2026-06-01 from OSINT federation brief K93. Replicates the OSINT morning **discovery-only** loop: Exa search → dedupe vs wiki/inbox → optional arXiv PDF fetch to `research to be indexed/` → sweep report. **Does not write entity pages or commit** — Cursor ingest remains human-gated.

## Narrative

| Field | Value |
|-------|--------|
| **Cadence** | Daily @ 08:15 local (LaunchAgent) |
| **Install** | `bash "../../OSINT WORKSPACE/scripts/federation/daily_digest/install_federated_daily_digest.sh" "<repo>" 3d-printing` |
| **Runner** | `~/bin/cemini-daily-research-digest-3d-printing` → `python3 scripts/daily_research_digest_run.py` |
| **Config** | `scripts/daily_research_config.yaml` — topics synced to `ROADMAP.md` |
| **Report** | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| **Inbox** | `research to be indexed/` (gitignored) |
| **Secrets** | `EXA_API_KEY` in `.env` or `~/.cemini/exa-api-key` |

### Operator loop

1. **Morning:** read `wiki/sweeps/YYYY-MM-DD-daily.md` (or run wrapper manually).
2. **Triage:** check rows worth fetching; PDFs may already be in inbox overnight.
3. **Ingest:** open this repo in Cursor → `python3 scripts/preingest_check.py` → discuss → ingest cluster (3–15 pages).
4. **Weekly (optional):** `monokern_pipeline` block in config — one deep NotebookLM pass on top ROADMAP cluster.

### What the digest covers (domain)

- **Paper lane:** FDM quality, VLM-in-manufacturing, AM security side-channels, soft/4D printing (background).
- **News lane:** Bambu/slicer updates, marketplace/store-ops, filaments, generative-3D AI tools.
- **Not automated:** friend handoff pages, Flashforge-specific support — those stay manual.

### LaunchAgent

```bash
launchctl load ~/Library/LaunchAgents/com.cemini.daily-research-digest.3d-printing.plist
```

Label must stay unique across federation wikis (`com.cemini.daily-research-digest.3d-printing`).

[TENTATIVE 2026-06-01] LaunchAgent loaded status not verified in this session — operator should confirm `launchctl list | grep 3d-printing`.

**Exa paper-lane caveat (2026-06-02):** `category: research paper` often returns Springer/Nature/ScienceDirect URLs, not arXiv — auto-fetch downloads **zero** PDFs unless hits include `arxiv.org`. Manual arXiv hunt or add `site:arxiv.org` queries to `daily_research_config.yaml` for overnight PDF drops.

## Snippets

> "Tier 3 autonomous ingest remains NO-GO." — Source: @osint-wiki/concepts/cemini-wiki-ingest-workflow.md (via federated-daily-research-digest)
