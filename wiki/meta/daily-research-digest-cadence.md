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
  - sweeps/2026-06-06-daily.md
  - sweeps/2026-06-07-daily.md
  - sweeps/2026-06-08-daily.md
  - sweeps/2026-06-09-daily.md
  - sweeps/2026-06-10-daily.md
  - sweeps/2026-06-11-daily.md
  - sweeps/2026-06-12-daily.md
  - sweeps/2026-06-13-daily.md
  - sweeps/2026-06-14-daily.md
  - sweeps/2026-06-15-daily.md
  - sweeps/2026-06-16-daily.md
  - sweeps/2026-06-17-daily.md
  - sweeps/2026-06-18-daily.md
  - sweeps/2026-06-19-daily.md
  - sweeps/2026-06-20-daily.md
  - sources/2026-arxiv-lane-noise-triage-jun20.md
  - sources/2026-arxiv-lane-noise-triage-jun21.md
  - sources/2026-arxiv-lane-noise-triage-jun22.md
  - sources/2026-arxiv-lane-noise-triage-jul15.md
  - sweeps/2026-06-21-daily.md
  - sweeps/2026-06-22-daily.md
  - sweeps/2026-06-23-daily.md
  - sweeps/2026-06-24-daily.md
  - sweeps/2026-06-25-daily.md
  - sources/2026-digest-sweep-triage-jun23-25.md
  - sources/2026-arxiv-lane-noise-triage-jul16.md
  - sources/2026-arxiv-lane-noise-triage-jul17.md
  - sources/2026-reject-arxiv-2607-07958-soft-exogloves.md
  - sources/2026-reject-arxiv-2607-06740-soft-robot-continual-learning.md
maturity: draft
created: 2026-06-01
updated: 2026-07-17
cross-wiki-source: "@osint-wiki/concepts/federated-daily-research-digest.md"
---

## Relations

@sources/2026-reject-arxiv-2607-06740-soft-robot-continual-learning.md @sources/2026-reject-arxiv-2607-07958-soft-exogloves.md @sources/2026-arxiv-lane-noise-triage-jul17.md @sources/2026-arxiv-lane-noise-triage-jul16.md @concepts/fdm-printing.md @concepts/ai-design-tools.md @concepts/print-farm-operations.md @sweeps/_daily-template.md @sweeps/2026-06-01-daily.md @sweeps/2026-06-02-daily.md @sweeps/2026-06-03-daily.md @sweeps/2026-06-04-daily.md @sweeps/2026-06-05-daily.md @sweeps/2026-06-06-daily.md @sweeps/2026-06-07-daily.md @sweeps/2026-06-08-daily.md @sweeps/2026-06-09-daily.md @sweeps/2026-06-10-daily.md @sweeps/2026-06-11-daily.md @sweeps/2026-06-12-daily.md @sweeps/2026-06-13-daily.md @sweeps/2026-06-14-daily.md @sweeps/2026-06-15-daily.md @sweeps/2026-06-16-daily.md @sweeps/2026-06-17-daily.md @sweeps/2026-06-18-daily.md @sweeps/2026-06-19-daily.md @sweeps/2026-06-20-daily.md @sweeps/2026-06-21-daily.md @sources/2026-arxiv-lane-noise-triage-jun20.md @sources/2026-arxiv-lane-noise-triage-jun21.md @sources/2026-arxiv-lane-noise-triage-jun22.md @sources/2026-arxiv-lane-noise-triage-jul15.md @sweeps/2026-06-22-daily.md

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

**Fix applied (2026-06-19):** four parallel `*-arxiv` paper queries with `site:arxiv.org` plus quoted AM/FDM terms (no Exa `category:` filter) added alongside the four broad `*-paper` discovery queries. Overnight fetch verified same day (0 → 5 PDFs). **Relevance caveat:** Exa still returns some off-topic arXiv hits — triage inbox before full ingest; tighten queries again if noise persists.

**Pass 20 triage (2026-06-20):** all 5 overnight PDFs rejected (medical 3D, HCI motion, construction 3DGS, robot nav, LLM RL env). Queries tightened again — FDM lane drops bare `FDM`; VLM lane requires LPBF/SLM/SLS not standalone `"3D printing"`. Record: @sources/2026-arxiv-lane-noise-triage-jun20.md.

**Pass 21 triage (2026-06-21):** second reject-all batch (VLM nav, stats, GNN/drones, remote sensing, egocentric video). On-topic AM papers appeared as **publisher URLs** in digest (`skipped-no-arxiv`) while arXiv lane still fetched noise. Fix: `fetch: false` on all `*-arxiv` queries (digest-only); operator manual-fetch from sweep. Record: @sources/2026-arxiv-lane-noise-triage-jun21.md.

**Pass 22 triage (2026-06-22):** third reject-all; noise now from broad `*-paper` lane arXiv URLs. **Global `fetch.enabled: false`** — digest-only until title-keyword filter or manual publisher workflow. Record: @sources/2026-arxiv-lane-noise-triage-jun22.md.

**Auto-fetch re-enabled (2026-07-14):** operator restored `fetch.enabled: true` + `fetch: true` on all `*-paper` and `*-arxiv` clusters. Cap still `max_downloads: 5`.

**Pass 24 triage (2026-07-15):** overnight fetch 1/5 accept (Firewall3D) + 4 noise rejects. Keep fetch on; revisit keyword gate if next nights return 0/5. Record: @sources/2026-arxiv-lane-noise-triage-jul15.md.

**Pass 25 triage (2026-07-16):** 2/4 accept (AgentsCAD + multimaterial soft-robotics background); 2 soft-robot control/medical rejects. News lane still off. Record: @sources/2026-arxiv-lane-noise-triage-jul16.md.

**Pass 26 triage (2026-07-17):** 1/2 accept (hybrid rigid-soft gripper); exoglove **re-fetched** after pass-25 reject without wiki ID — added REJECT stubs for `2607.07958` + `2607.06740` so fetch dedupes. Record: @sources/2026-arxiv-lane-noise-triage-jul17.md.

## Snippets

> "Tier 3 autonomous ingest remains NO-GO." — Source: @osint-wiki/concepts/cemini-wiki-ingest-workflow.md (via federated-daily-research-digest)
