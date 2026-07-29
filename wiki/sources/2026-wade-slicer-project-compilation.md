---
title: "Functionally Grading the Slicing Process by Compiling Design Intent into Slicer Projects"
type: source
tags: [paper, FFF, slicing, 3MF, functionally-graded, OpenVCAD, PrusaSlicer, OrcaSlicer]
keywords: [slicer project compilation, OpenVCAD, settings meshes, virtual extrusion, ColorMix, FullSpectrum, foaming TPU, LW-PLA, VarioShore, MacCurdy, Wade]
related:
  - concepts/slicer-project-compilation.md
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
read_status: skimmed
---

## Relations

@concepts/slicer-project-compilation.md @entities/tools/openvcad.md @entities/slicers/orcaslicer.md @entities/slicers/bambu-studio.md @concepts/fdm-printing.md @concepts/filaments-baseline.md @entities/materials/tpu.md @entities/materials/pla.md @concepts/ai-design-tools.md

## Raw Concept

- **Title:** Functionally Grading the Slicing Process by Compiling Design Intent into Slicer Projects
- **Authors:** Charles Wade (CU Boulder / Draper), Devon Beck (Draper), Robert MacCurdy (CU Boulder)
- **Type:** arXiv preprint, arXiv:2607.25326v1 [cs.GR]
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2607.25326-functionally-grading-the-slicing-process-by-comp.pdf`
- **Retrieved:** 2026-07-29 overnight digest
- **Pages:** 20
- **Read-status:** skimmed (abstract, method §3, foaming calibration §4.2, color/halftoning §4.3, availability)
- **Code:** https://github.com/MacCurdyLab/OpenVCAD-Public (PyPI `OpenVCAD`)

## Narrative

**Thesis:** functionally graded FFF is often framed as grading *geometry or material*, but many functional effects come from grading the *slicing/process* itself (infill, fuzzy skin, nozzle temp, flow, color recipes). Mainstream slicers already expose those knobs as per-region settings, but users must hand-partition meshes in the GUI. This paper automates that lowering: a **slicer project compiler** turns continuous attribute fields into slicer-native **`.3mf` projects** with embedded sub-meshes, settings, recipes, and process-state assignments — then PrusaSlicer / OrcaSlicer (etc.) do native toolpath planning, preview, supports, and printer profiles. [CONFIRMED — abstract + §1]

### Three compilation targets [CONFIRMED — §3.1]

| Target | What gets written into the `.3mf` | Downstream |
|--------|-----------------------------------|------------|
| **Settings meshes** | Per-region slicer settings (infill density, fuzzy-skin thickness/distance, …) | Native toolpath planning |
| **Virtual extrusion** | Logical tool IDs + custom toolchange templates → nozzle temp / flow (process state) | Toolchange emission |
| **Color / material halftoning** | Virtual mixed-filament recipes | Prusa **ColorMix** or Orca **FullSpectrum** |

Targets can combine (e.g. foaming bunny = fuzzy-skin settings + virtual-extrusion temp/flow).

### Foaming-filament calibration (load-bearing for materials) [CONFIRMED — §4.2]

Calibrated **ColorFabb VarioShore TPU** and **LW-PLA** so high-level density / Shore-A fields drive temperature + flow-rate compensation:

- Uncompensated foaming expands walls; flow multiplier restores ~0.45 mm target thickness across temp.
- Density vs temp characterized for inverse design (e.g. 200 mm bar with CoM offset 18 mm via density switch 0.413 ↔ 1.123 g·cm⁻³).
- Shore A vs temp on VarioShore TPU; gradient bar 65A→85A printed with **MAE 0.5 Shore A** at 11 sample points. [CONFIRMED — §4.2.3]
- SEM: microspheres intact at ~196 °C; gas-filled pores at ~250 °C.

### Color / halftoning [CONFIRMED — §4.3]

Same volumetric CMYKW design exported to ColorMix and FullSpectrum on Prusa XL. Mountain benchmark: ColorMix mean ΔE₀₀ **11.73** vs FullSpectrum **16.63**; excess texture 3.04 vs 6.69 — compiler is workflow-agnostic; fidelity depends on downstream slicer path. [TENTATIVE — single palette/printer]

### Manual-interaction claim [CONFIRMED — §4.4]

Compiler replaces **>2,500** repetitive slicer assignment interactions vs a favorable manual baseline (meshes already partitioned/aligned; count excludes mesh gen/import).

### Phase-0 (2026-07-29)

| Check | Result |
|-------|--------|
| Repo | https://github.com/MacCurdyLab/OpenVCAD-Public — 59★, last push 2026-04-01, examples + LICENSE |
| License | **Non-commercial** CU Boulder notice + pending patent — research/personal only; **not** store/commercial |
| Package | PyPI `OpenVCAD` 2.3.8 — macOS arm64 wheel ~**50 MB** |
| Slicer assumption | Emits PrusaSlicer / OrcaSlicer project dialects; not Bambu Studio day-1 path |
| Friend / Flashforge | **NO-GO** week-1 — volumetric CAD + foaming specialty filament |
| Verdict | **CONDITIONAL-GO (research)** — local adopt OK under non-commercial terms; cite for graded FFF + 3MF compilation |
| Local adopt (&lt;500 MB) | **Yes** — shallow clone `.adopted/OpenVCAD-Public` (~5 MB). Full `pip install` venv ballooned to ~975 MB (over cap) — skipped |

## Snippets

> "This paper presents slicer project compilation: a fully automated workflow that lowers heterogeneous implicit designs into slicer-native .3mf projects with embedded sub-meshes, settings, recipes, and process-state assignments."
[Source: arXiv:2607.25326v1 abstract]

> "The implementation, example projects, calibration data, and scripts used to produce the figures are available at: https://github.com/MacCurdyLab/OpenVCAD-Public"
[Source: arXiv:2607.25326v1 §A.1]

> "Across printed examples, the compiler generates ready-to-slice projects … replacing more than 2,500 repetitive manual slicer interactions."
[Source: arXiv:2607.25326v1 abstract]
