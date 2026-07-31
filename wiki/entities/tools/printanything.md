---
title: PrintAnything
type: entity
tags: [tool, AI, G-code, point-cloud, phase-0, research]
keywords: [PrintAnything, G-plan, mesh-free, point cloud to G-code, SNU, Kairoba]
related:
  - sources/2026-hong-printanything-gplan.md
  - concepts/ai-design-tools.md
  - concepts/novice-cad-workflows.md
  - concepts/fdm-printing.md
  - entities/slicers/bambu-studio.md
  - entities/printers/x1c.md
maturity: draft
created: 2026-07-31
updated: 2026-07-31
---

## Relations

@sources/2026-hong-printanything-gplan.md @concepts/ai-design-tools.md @concepts/novice-cad-workflows.md @concepts/fdm-printing.md @entities/slicers/bambu-studio.md @entities/printers/x1c.md

## Raw Concept

SNU / Kairoba research system: unoriented point cloud → G-plan maps → compiled FDM G-code (mesh-free). Paper arXiv:2607.27729. Public “code” URL is an empty GitHub stub as of ingest.

## Narrative

### Phase-0 verdict (2026-07-31)

| Check | Result |
|-------|--------|
| Maturity | 1★ empty repo; paper claims code public |
| License | None published |
| G-code risk | **Hard NO-GO** for day-1 / friend / store — violates hallucinated-G-code red line |
| Local adopt | Skipped (&lt;500 MB irrelevant — nothing to install) |
| Overall | **REFERENCE** — cite G-plan intermediate pattern only |

### When it matters

- Research: point-cloud / generative-3D → fabrication without Poisson/MeshAnything detour
- Harness steal: structured intermediate + deterministic compiler beats free-form G-code generation

### When not

- Flashforge / Orca-Flashforge week-1
- Any unattended run of model-emitted G-code on a real printer

## Snippets

See [@sources/2026-hong-printanything-gplan.md].
