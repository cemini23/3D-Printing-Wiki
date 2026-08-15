---
title: "Manufacturing Complex Airtight Soft Pneumatic Actuators (arXiv:2608.13233)"
type: source
tags: [paper, soft-robotics, pneumatic, TPU, FDM, process-window]
keywords: [airtight, soft pneumatic actuator, TPU Bowden, Ultimaker, wall-line architecture, moisture control, DLP, heat-shrink, silicone casting]
related:
  - concepts/soft-robotics-fdm-diw.md
  - concepts/shape-changing-fdm-interfaces.md
  - entities/materials/tpu.md
  - concepts/fdm-printing.md
  - concepts/novice-cad-workflows.md
  - sources/2026-li-duomorph-fdm-pneumatic.md
  - sources/2026-chen-hybrid-rigid-soft-gripper.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
read_status: skimmed
---

## Relations

@concepts/soft-robotics-fdm-diw.md @concepts/shape-changing-fdm-interfaces.md @entities/materials/tpu.md @concepts/fdm-printing.md @concepts/novice-cad-workflows.md @sources/2026-li-duomorph-fdm-pneumatic.md @sources/2026-chen-hybrid-rigid-soft-gripper.md

## Raw Concept

- **Title:** Manufacturing Complex Airtight Soft Pneumatic Actuators for Soft Robotics: Process Evaluation and Optimization
- **Author:** Mohammed Abboodi (mabbo103@uottawa.ca; ORCID 0009-0002-4645-0026); advisor Dr. Marc Doumit; funded by Dr. Marc Doumit and the University of Ottawa
- **arXiv:** 2608.13233 [cs.RO]
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2608.13233-manufacturing-complex-airtight-soft-pneumatic-ac.pdf`
- **Retrieved:** 2026-08-15 ingest pass 30 (overnight digest)
- **Pages:** 15
- **Read-status:** skimmed (abstract, methods, all process sections, Table 1–2, discussion, conclusion)

## Narrative

Manufacturing-focused evaluation of **five fabrication routes** for a geometrically complex, flexible, **airtight** soft pneumatic actuator (SPA) — the soft sleeve actuator architecture previously published by Abboodi & Doumit (IEEE Access 2024) [26]. The paper treats manufacturing as the research problem, not a supporting step, and asks: *which manufacturing technique, under what conditions, can reliably produce geometrically complex, flexible, airtight SPAs?* Method is a four-stage funnel: process screening → baseline fabrication → failure analysis → process improvement/validation, separating **inherent process limitations** from **correctable manufacturing defects**.

### Route comparison

| Route | Setup tested | Dominant limitation | Verdict |
|-------|--------------|---------------------|---------|
| **Heat-shrink forming** | 3M FP-301 tube (4:1 shrink), boiling-water bath, modular mold (ABS → polycarbonate) | 4:1 shrink ratio cannot conform to deep corrugation valleys — tube bridges gaps between peaks; air leakage; rigid ABS end-caps stiffen the actuator | Excluded |
| **Silicone casting** | Dragon Skin (Smooth-On), multi-part PLA FDM molds, vacuum degassing | Bonded interfaces fail above ~200 kPa; walls ~5 mm needed to cast defect-free → bulky/stiff; voids and trapped air in narrow cavities | Excluded |
| **Powder AM (SLS / MJF)** | Concept-level | Residual powder trapped in enclosed passages / cavities as small as ~1 mm | Excluded |
| **DLP** | Elegoo Mars 2; Liqcreate Premium Flex (63A) / Flexible-X (55A); 45° orientation + vent holes; ethanol wash + 45 min UV post-cure | Geometry reproduced, but cured-resin elongation <150% limits large deformation; high material cost + ventilation + multi-step post-processing | Excluded (not retained) |
| **FDM TPU** | Prusa i3 MK3S (direct-drive) dropped; **Ultimaker 3 Extended + Ultimaker S3 (Bowden)** retained | Dominant defects were **correctable** via process optimization | **Retained** |

### FDM framework (retained route)

1. **Extrusion system.** The direct-drive Prusa i3 MK3S was dropped — long complex prints suffered vibration, layer misalignment, filament entanglement, repeated nozzle clogs, and head-mass accuracy loss. The **Bowden** Ultimaker pair was retained after stabilization: stepwise extruder-tension tuning, a **shorter low-friction PTFE tube**, regular cold-pull / hot nozzle cleaning, and **retraction disabled** (retraction of viscoelastic TPU destabilizes nozzle pressure; stringing controlled via temp/speed/travel).
2. **Moisture control.** Dehumidifier held **RH <20%** around the printer; TPU dried **5 h @ 50 °C** with silica gel. Airtightness depends on filament condition, not only wall thickness — moisture→vapor disrupts flow, creates bubbles/pores/weak interlayer bonds → leakage paths.
3. **Support-free design.** PVA soluble supports (stringing, gaps) and TPU supports (damage on mechanical removal from narrow spaces) both rejected for enclosed networks. Adopted a **30° overhang criterion** — explicitly lab-specific (material/printer/geometry/deposition), **not a universal limit**.
4. **Build-plate adhesion.** Washable glue stick + brim; first-layer speed/temperature tuned together.

### Process window (Table 2 — Ultimaker lab; transfer caveat)

| Parameter | Value | | Parameter | Value |
|-----------|-------|-|-----------|-------|
| Nozzle diameter | 0.4 mm (0.25 clogged; 0.8 too coarse) | | Print temp | 235 °C (first layer 257 °C) |
| Layer height | 0.1 mm (initial 0.27 mm) | | Bed temp | **40 °C (table) vs 50 °C (prose)** [NEEDS VERIFICATION 2026-08-15] |
| Line width | 0.32 mm | | Flow | 110% (infill 125%) |
| Wall line count | **3** | | Speed | 15 mm/s (initial 11; top/bottom 12) |
| Infill | 100% zigzag | | Fan | 30% (30–40% window) |
| Retraction / supports | disabled | | Adhesion | brim (table lists both 9 and 10 mm [NEEDS VERIFICATION 2026-08-15]) |
| Line overlap | 20–25% | | — | — |

The paper stresses these are a **coupled process window, not independent optimal values** — transferring one or two settings to another printer/TPU will not reproduce the outcome [Source: arXiv:2608.13233 §3.4.3.7, §4].

### Headline finding [CONFIRMED paper]

A **0.96 mm wall from three 0.32 mm lines sealed better than a 1.6 mm wall from two 0.8 mm lines**. Airtightness depends on **extrusion-path architecture**, not nominal wall thickness alone; more, narrower lines create several interfaces that reduce the chance of a continuous leakage path. Four–five lines improved sealing but added stiffness/time; three was the balance point. The "aligned local defects form a continuous leak path" mechanism is the author's interpretation — leakage paths were **not directly visualized** → [TENTATIVE].

>100 actuator models of different geometries were fabricated on the Ultimaker pair.

### Phase-0 (2026-08-15)

| Check | Result |
|-------|--------|
| Public repo | **None** found (Brave 2026-08-15; web search 2026-08-15) |
| License / BOM | Paper-only; no SPDX, no BOM |
| Hobby adopt | **NO-GO** — pneumatics + controlled-environment lab window |
| Verdict | **REFERENCE** — airtight TPU FDM background for the soft-robotics / pneumatics cluster |

### Wiki hooks

- **TPU airtight FDM** — how to make TPU walls that hold pressure; pairs with the DuoMorph heat-seal pneumatics row in @concepts/shape-changing-fdm-interfaces.md and the hybrid-gripper membrane-pneumatics entry in @concepts/soft-robotics-fdm-diw.md.
- **Bowden-TPU nuance vs @entities/materials/tpu.md** — the wiki's TPU page says *direct-drive strongly preferred*; this paper shows Bowden can work **with conditioning** (dried filament, low-friction PTFE, disabled retraction). [TENTATIVE] transfer; does **not** overturn the Bambu direct-drive default for the friend reader.
- **Friend reader: skip.** Pneumatics / 4D territory; week-1 skip list (@concepts/novice-cad-workflows.md). Do **not** copy Table 2 numbers to a Flashforge Adventurer 5M or Bambu as day-1 settings.

## Snippets

> "The results further showed that airtightness depends not only on nominal wall thickness but also on extrusion-path architecture, while support-free geometry is important when access for internal post-processing is limited."
[Source: arXiv:2608.13233 abstract]

> "A 1.6-mm wall formed from two 0.8-mm lines showed poorer airtightness than a 0.96-mm wall formed from three 0.32-mm lines."
[Source: arXiv:2608.13233 §3.4.3.6 (wall-line configuration)]

> "Values to verify before submission: The chapter text reports an optimal build-plate temperature of 50 °C, whereas Table 2 reports 40 °C. Table 2 also lists brim widths of both 9 and 10 mm."
[Source: arXiv:2608.13233 p.12 — authors' own pre-submission note]
