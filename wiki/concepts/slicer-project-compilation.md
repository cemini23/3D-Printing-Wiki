---
title: Slicer Project Compilation (Functionally Graded FFF)
type: concept
tags: [process, slicing, FFF, functionally-graded, 3MF, toolchain]
keywords: [slicer project compilation, settings meshes, virtual extrusion, ColorMix, FullSpectrum, graded infill, fuzzy skin, foaming filament, OpenVCAD]
related:
  - sources/2026-wade-slicer-project-compilation.md
  - entities/tools/openvcad.md
  - entities/slicers/orcaslicer.md
  - entities/slicers/bambu-studio.md
  - concepts/fdm-printing.md
  - concepts/filaments-baseline.md
  - entities/materials/tpu.md
  - entities/materials/pla.md
  - concepts/ai-design-tools.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
---

## Relations

@sources/2026-wade-slicer-project-compilation.md @entities/tools/openvcad.md @entities/slicers/orcaslicer.md @entities/slicers/bambu-studio.md @concepts/fdm-printing.md @concepts/filaments-baseline.md @entities/materials/tpu.md @entities/materials/pla.md @concepts/ai-design-tools.md

## Raw Concept

How do you turn continuous spatial design intent (density, Shore hardness, color, fuzzy skin) into something a production FFF slicer will actually slice — without manually painting hundreds of modifier meshes?

## Narrative

### The gap

Field-based / volumetric CAD can express gradients. Mature slicers (PrusaSlicer, OrcaSlicer, Bambu Studio) already support **per-region** settings and multi-tool recipes — but the UI expects discrete meshes the user authored. Hand-lowering continuous fields does not scale.

### The compilation pattern (Wade / MacCurdy 2026)

1. Represent design as typed spatial attributes (intent fields).
2. Optionally run **translation models** (e.g. Shore A → nozzle temp + flow for foaming TPU).
3. Partition fields into finite labeled regions; extract aligned sub-meshes.
4. Serialize into slicer-native **`.3mf` project** dialect (settings meshes / virtual extruders / mixture recipes).
5. Let the existing slicer own toolpaths, supports, preview, printer profiles.

Primary source: [@sources/2026-wade-slicer-project-compilation.md] (arXiv:2607.25326). Implementation: [@entities/tools/openvcad.md].

### Why it matters for this wiki

- **OrcaSlicer** is an explicit compilation target (FullSpectrum color path) — reinforces CONDITIONAL-GO advanced-calibration role vs Bambu daily driver.
- **Foaming TPU / LW-PLA** become first-class process materials when temp/flow are treated as spatial fields — extends [@concepts/filaments-baseline.md] beyond uniform SKUs.
- Contrasts with custom gradient-aware slicers that reimplement support/profile infrastructure — prefer **compile into ecosystem** over replace it. [CONFIRMED — paper §2.3 framing]

### Practical posture

| Audience | Posture |
|----------|---------|
| Friend / Flashforge week-1 | Skip — download STLs + stock Orca-Flashforge profiles |
| Research / advanced FFF | CONDITIONAL-GO OpenVCAD under non-commercial license |
| Etsy / store ops | **NO-GO** — CU non-commercial + patent notice |

## Snippets

See source page snippets for abstract + availability URL.
