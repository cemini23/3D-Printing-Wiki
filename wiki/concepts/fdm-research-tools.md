---
title: FDM Research Tools — Repurposed Printers and Hybrid Processes
type: concept
tags: [research, tooling, photogrammetry, repurposed, hybrid]
keywords: [3D Cal, Slug-Mapper, SplatOverflow, bed rotation, thermal drawing, STL simulation]
related:
  - concepts/fdm-printing.md
  - concepts/soft-robotics-fdm-diw.md
  - concepts/ai-design-tools.md
  - sources/2011-roberts-bed-rotation-photogrammetry.md
  - sources/2025-morris-slug-mapper-ulfl-mri.md
  - sources/2024-kwatra-splatoverflow-troubleshooting.md
  - sources/2026-cheng-stl-to-stokeslet.md
  - sources/2026-demircali-thermal-drawing-preforms.md
  - sources/2025-kota-3d-cal-tactile-calibration.md
maturity: draft
created: 2026-06-01
updated: 2026-06-05
---

## Relations

@concepts/fdm-printing.md @concepts/soft-robotics-fdm-diw.md @concepts/ai-design-tools.md @sources/2011-roberts-bed-rotation-photogrammetry.md @sources/2025-morris-slug-mapper-ulfl-mri.md @sources/2024-kwatra-splatoverflow-troubleshooting.md @sources/2026-cheng-stl-to-stokeslet.md @sources/2026-demircali-thermal-drawing-preforms.md @sources/2025-kota-3d-cal-tactile-calibration.md

## Raw Concept

Ingest pass 15 — printers and STLs used as **research infrastructure** (motion stages, QA rigs, scan-to-CAD debug) plus hybrid post-processing. Deep-read 2026-06-05: @sources/2025-kota-3d-cal-tactile-calibration.md.

## Narrative

| Pattern | Example |
|---------|---------|
| Printer → precision stage | **3D Cal** (G-code probe grid + TouchNet depth maps for DIGIT/GelSight; Ender 3 validated) — @sources/2025-kota-3d-cal-tactile-calibration.md; Slug-Mapper |
| Printer → process research bed | Roberts 2011 rotation + photogrammetry |
| Scan + CAD → remote debug | SplatOverflow |
| FDM preform → downstream process | Thermal fiber drawing |
| STL → simulation | Stokeslet mobility (not printing) |

**3D Cal practical note [CONFIRMED]:** ~250 probe locations (~20% of 0.5 mm grid) sufficient for usable depth calibration; ~2 h automated capture per sensor; any G-code FDM printer in principle.

## Snippets

(none — synthesis page)
