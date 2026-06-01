---
title: Daily research sweep template
type: brief
tags: [meta, sweep, template, automation]
keywords: [daily-research-digest, sweep-template, exa]
related:
  - meta/daily-research-digest-cadence.md
maturity: core
created: 2026-06-01
updated: 2026-06-01
---

## Relations

@meta/daily-research-digest-cadence.md

# Daily Research Digest — YYYY-MM-DD

Discovery-only. Window: last 7 days. Exa queries from `scripts/daily_research_config.yaml`. **Does NOT ingest wiki pages.**

Reference: @meta/daily-research-digest-cadence.md

---

## Active topics (sync from ROADMAP)

- Inbox ingest pass — cluster picks
- Consumer FDM — Bambu / Flashforge / slicers
- Materials baseline
- AI design tools / generative 3D
- Store ops (background)

---

## Inbox (`research to be indexed/`)

_List pending manual drops + overnight arXiv fetches._

---

## Exa candidates

### Q1: bambu-slicer-news

| Pick | Date | Title | Cluster | URL |
|------|------|-------|---------|-----|
| [ ] R1 | | | bambu-slicer-news | |

---

## Wiki gap detect

Run: `python3 scripts/wiki_gap_detect.py` if stale `[NEEDS VERIFICATION]` tags pile up.

---

## Social pass (manual — Cursor session)

- **opencli-reader**: HackerNews / r/3Dprinting — Bambu, Flashforge, filament, slicer last 24h

---

## Ingest session prompt (copy into Cursor)

```
Ingest selected rows from wiki/sweeps/YYYY-MM-DD-daily.md:
- Run preingest_check on inbox
- Discuss takeaways before writing
- Touch 3–15 wiki pages; lint; update ROADMAP + log
```

---

## Summary

| Metric | Count |
|--------|-------|
| Exa hits (deduped) | 0 |
| Inbox files | 0 |

### Discard

`rm wiki/sweeps/YYYY-MM-DD-daily.md` if nothing worth acting on.
