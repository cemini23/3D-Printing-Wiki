---
title: OpenVCAD
type: entity
tags: [tool, CAD, volumetric, FFF, open-source, non-commercial, phase-0]
keywords: [OpenVCAD, pyvcad, MacCurdyLab, volumetric CAD, multi-material, slicer project compilation, functionally graded]
related:
  - sources/2026-wade-slicer-project-compilation.md
  - concepts/slicer-project-compilation.md
  - entities/slicers/orcaslicer.md
  - entities/slicers/bambu-studio.md
  - concepts/ai-design-tools.md
  - concepts/fdm-printing.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
---

## Relations

@sources/2026-wade-slicer-project-compilation.md @concepts/slicer-project-compilation.md @entities/slicers/orcaslicer.md @entities/slicers/bambu-studio.md @concepts/ai-design-tools.md @concepts/fdm-printing.md

## Raw Concept

Volumetric multi-material geometry compiler from MacCurdy Lab (CU Boulder). Upstream of the 2026 slicer-project-compilation paper: design graded objects in Python (`pyvcad`), then (in the new work) emit ready-to-slice `.3mf` projects for PrusaSlicer / OrcaSlicer.

## Narrative

### What it is

- **Repo:** https://github.com/MacCurdyLab/OpenVCAD-Public (public examples + LICENSE; fuller source via request form)
- **Docs:** https://matterassembly.org/OpenVCAD-Docs/v2/
- **Install:** `pip install OpenVCAD` (v2.3.8 as of 2026-07-29; macOS arm64 wheel ~50 MB)
- **Prior paper:** Wade et al. 2024 *Additive Manufacturing* 79:103912 (geometry compiler); 2025 gradient-aware toolpaths; 2026 slicer project compilation (arXiv:2607.25326)

### Phase-0 verdict (2026-07-29)

| Check | Result |
|-------|--------|
| Maturity | 59★; commits through 2026-04; PyPI wheels for 3.11–3.14 |
| License | **Non-commercial** research/personal (CU + pending patent) — blocks store/commercial use |
| Cloud lock-in | Local Python; no cloud LLM required |
| Slicer lock-in | Compiles to Prusa/Orca project dialects — not a Bambu Studio replacement |
| Friend reader | **NO-GO** day-1 |
| Local adopt (&lt;500 MB) | **GO (research)** — shallow clone `.adopted/OpenVCAD-Public` (~5 MB); pip venv skipped (&gt;500 MB with deps) |
| Overall | **CONDITIONAL-GO (research only)** |

### When to reach for it

- Graded infill / fuzzy skin / foaming-TPU Shore or density fields → printable `.3mf`
- Comparing ColorMix vs FullSpectrum from one volumetric color design

### When not to

- Commercial store SKUs (license)
- Flashforge Adventurer 5M week-1 path (use Orca-Flashforge + downloaded STLs)
- Expecting Bambu AMS-native multi-color authoring

## Snippets

> "OpenVCAD is an open-source volumetric geometry compiler for the design and fabrication of functionally graded, multi-material objects."
[Source: github.com/MacCurdyLab/OpenVCAD-Public README (retrieved 2026-07-29)]
