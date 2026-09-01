---
title: PyKirigami
type: entity
tags: [tool, kirigami, simulation, Python, research, phase-0]
keywords: [PyKirigami, kirigami simulator, hinge joints, deployment, CUHK, Jiang, Choi]
related:
  - sources/2026-jiang-unified-kirigami-design.md
  - concepts/shape-changing-fdm-interfaces.md
maturity: draft
created: 2026-09-01
updated: 2026-09-01
wire_status: wont_wire
wire_target: "REFERENCE clone only; no 3D-printing runtime wire"
---

## Relations

@sources/2026-jiang-unified-kirigami-design.md @concepts/shape-changing-fdm-interfaces.md

## Raw Concept

Interactive Python simulator for kirigami metamaterial deployment (arXiv:2508.15753). Companion to Jiang & Choi kirigami design papers including @sources/2026-jiang-unified-kirigami-design.md. Phase-0 audit 2026-09-01.

## Narrative

### Phase-0 verdict (2026-09-01)

| Check | Result |
|-------|--------|
| Repo | https://github.com/andy-qhjiang/PyKirigami |
| License | **Apache-2.0** |
| Size | ~29 MB on disk (under 500 MB adopt cap) |
| Stars / activity | 16★; last push 2026-08-07 |
| Role | Kinematic deployment simulator (hinge joints); not FDM slicer |
| Friend / store | **NO-GO** — research tooling |
| Local adopt | **REFERENCE** optional — no runtime install on prod harness |
| Phase-1 | **wont_wire** |

### When it matters

- Validate kirigami deployment paths before cutting/printing tile layouts
- Cited for intermediate deployed states in 3D-to-3D examples (arXiv:2608.30032 Fig. 5)

### When not

- Consumer FDM workflow (@concepts/novice-cad-workflows.md week-1 path)
- Replacement for Orca-Flashforge / Bambu Studio

## Snippets

> "Data Availability The code and data are available on GitHub at https://github.com/andy-qhjiang/PyKirigami."
[Source: arXiv:2508.15753 HTML]
