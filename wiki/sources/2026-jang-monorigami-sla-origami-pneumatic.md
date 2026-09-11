---
title: "MONORIGAMI — monolithic SLA origami folding actuators (arXiv:2609.00751)"
type: source
tags: [paper, soft-robotics, origami, pneumatic, SLA, haptics, multi-DoF]
keywords: [MONORIGAMI, stiffness anisotropy, Formlabs, Flexible 80A, vacuum, composable actuator, CHARM, Stanford]
related:
  - concepts/shape-changing-fdm-interfaces.md
  - concepts/soft-robotics-fdm-diw.md
  - sources/2026-li-duomorph-fdm-pneumatic.md
  - sources/2026-jiang-unified-kirigami-design.md
  - sources/2026-abboodi-airtight-spa-fdm.md
  - concepts/novice-cad-workflows.md
maturity: draft
created: 2026-09-11
updated: 2026-09-11
read_status: skimmed
wire_status: wont_wire
wire_target: "SLA research REFERENCE; 3D-printing Phase-1 local wires off"
---

## Relations

@concepts/shape-changing-fdm-interfaces.md @concepts/soft-robotics-fdm-diw.md @sources/2026-li-duomorph-fdm-pneumatic.md @sources/2026-jiang-unified-kirigami-design.md @sources/2026-abboodi-airtight-spa-fdm.md @concepts/novice-cad-workflows.md

## Raw Concept

- **Title:** One Print, Many Moves: Monolithic Origami-inspired Folding Actuator for Composable Soft Multi-DoF Systems
- **Authors:** Jaehyung Jang†, Zhenish Zhakypov†, Jasmin E. Palmer, Melissa Klein, Jee-Hwan Ryu*, Allison M. Okamura* (KAIST IRiS + Stanford CHARM)
- **arXiv:** 2609.00751 [cs.RO]
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2609.00751-one-print-many-moves-monolithic-origami-inspired.pdf`
- **Retrieved:** 2026-09-11 ingest pass 32
- **Pages:** 26 (+ supplementary)
- **Read-status:** skimmed (abstract, intro, Fig. 2 fabrication, characterization sections)

## Narrative

**MONORIGAMI** (MONOlithic ORIGAMI-inspired actuator) is a soft folding actuator whose motion is constrained by **spatially programmed stiffness anisotropy** — thick facets resist off-axis bending while thin creases fold compliantly along prescribed directions. Actuation uses **negative pressure (vacuum)** on embedded fluidic channels. Each module is a **composable motion primitive**; serial/parallel linking mechanically programs multi-DoF trajectories.

### Fabrication [CONFIRMED paper §Results / Fig. 2]

| Item | Detail |
|------|--------|
| Process | **SLA** — single material, **single print**, no actuator-level assembly |
| Printer | **Formlabs Form 3** |
| Material | **Flexible 80A** resin |
| Monolithic features | Facets, creases, passive joints, embedded fluidic channels in one step |
| Min reliable crease thickness | **0.3 mm** (process limit cited) |

**Not FDM.** Despite "fully 3D-printable" language, validation is **resin SLA**, not filament FFF. Flashforge / Orca-Flashforge readers should treat this as an **adjacent SLA + pneumatics** reference — same design ideas as @sources/2026-jiang-unified-kirigami-design.md (kirigami geometry) but different stack from @sources/2026-li-duomorph-fdm-pneumatic.md (FDM + heat-seal film).

### Demonstrators [CONFIRMED abstract]

1. **4-DoF wearable VR haptic** — cutaneous feedback
2. **3-DoF teleoperation joystick** — kinesthetic feedback
3. **Modular underwater gripper** — geometry-encoded grasp trajectories

### Design contributions (paper framing)

1. **Directionally constrained soft actuation** — suppress undesired DoF while keeping compliant folds
2. **Composable multi-DoF architecture** — modules as building blocks
3. **Monolithic manufacturing** — deformation logic encoded in printed geometry (thickness tiers)

### Phase-0 (2026-09-11)

| Check | Result |
|-------|--------|
| Public repo / CAD | **None** found (Brave 2026-09-11; CHARM prior origami haptics papers also paper-only) |
| License / BOM | Paper + supplementary only |
| Stack | **SLA resin** — not validated on FDM |
| Friend / Flashforge | **NO-GO** — resin printer + vacuum pneumatics + R&D |
| Store / Etsy | **NO-GO** |
| Verdict | **REFERENCE** |
| Phase-1 | **wont_wire** |

## Snippets

> "The design is fully 3D-printable through a single-material, single-print process that requires no assembly."
[Source: arXiv:2609.00751 abstract]

> "devices were fabricated using a commercially available stereolithography (SLA) 3D printer with standard material (Formlabs Form 3 with Flexible 80A resin)"
[Source: arXiv:2609.00751 main text / Fig. 2 discussion]

> "Spatially programmed stiffness transforms a single-print soft folding actuator into a composable building block for multi-DoF robotic systems."
[Source: arXiv:2609.00751 one-sentence summary]
