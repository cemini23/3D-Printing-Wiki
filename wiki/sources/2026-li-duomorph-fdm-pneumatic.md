---
title: DuoMorph — Synergistic FDM Printing and Pneumatic Actuation for Shape-Changing Interfaces
type: source
tags: [paper, CHI, shape-changing, pneumatic, FDM, 4D-printing, heat-sealing, HCI]
keywords: [DuoMorph, FDM, pneumatic, heat sealing, TPU film, Bambu A1, shape-changing interface, 4D printing, Rhino Grasshopper]
related:
  - concepts/shape-changing-fdm-interfaces.md
  - concepts/fdm-printing.md
  - entities/materials/pla.md
  - entities/materials/tpu.md
  - entities/printers/a1.md
  - sources/2026-abboodi-airtight-spa-fdm.md
maturity: draft
created: 2026-05-23
updated: 2026-08-15
read_status: read
---

## Relations

@concepts/shape-changing-fdm-interfaces.md @concepts/fdm-printing.md @entities/materials/pla.md @entities/materials/tpu.md @entities/printers/a1.md @sources/2026-abboodi-airtight-spa-fdm.md

## Raw Concept

- Title: DuoMorph: Synergistic Integration of FDM Printing and Pneumatic Actuation for Shape-Changing Interfaces
- Authors: Xueqing Li, Danqi Huang, Tianyu Yu, Shuzi Yin, Bingjie Gao, Anna Matsumoto, Zhihao Yao, Yiwei Zhao, Shiqing Lyu, Yuchen Tian, Lining Yao, Haipeng Mi, Qiuyu Lu (corresponding)
- Type: CHI '26 conference paper; arXiv:2602.22604v1 [cs.HC]; DOI 10.1145/3772318.3791040; CC BY 4.0
- Location: `raw-sources/2026-li-duomorph-fdm-pneumatic.pdf`
- Retrieved: 2026-05-23
- Pages: 14
- Read-status: read (pages 1–8 — design space, fabrication, applications; performance quant sections referenced but not line-extracted)

## Narrative

HCI fabrication paper presenting **DuoMorph**: a unified workflow where a **standard single-nozzle FDM printer** both **heat-seals** thin-film pneumatic bladders and **prints** structural / 4D / sensing layers on top—avoiding separate casting, manual gluing, or SLA elastic resins for reversible soft actuation.

**Core idea.** Printed PLA/TPU structures and heat-sealed airbags are **co-designed** so each constrains the other: passive-deformation structures, constraint structures (bend angle / direction), pre-shaping 4D structures (hot-water activation), and function-extending structures (conductive touch sensing, friction tuning).

**Fabrication hardware (validated).** Bambu Lab **A1 Series** single-nozzle printer; manual filament swap or AMS for multi-material. Design tool: Rhino 8 + Grasshopper + HumanUI GUI—exports merged heat-seal + print G-code. 3D components sliced in **Cura or Bambu Studio** (STL export with alignment marker); heat-seal paths generated in DuoMorph tool (0.5 mm sampling, 5 mm/s seal speed).

**Materials.**

| Layer | Material | Notes |
|-------|----------|-------|
| Airbag film | 0.2 mm TPU film **or** 0.2 mm nylon + 0.03 mm TPU coating | TPU film softer → easier 4D pre-shape; coated fabric stiffer → better support for printed structures when deflated |
| Heat seal | Nozzle 250–280 °C, bed 50–70 °C (fabric-dependent), 5 mm/s | PTFE protective fabric on TPU film; Z-homing force sufficient—no extra press in G-code |
| FDM on film | PLA, TPU (Bambu), conductive TPU (Qie feng) | **Bed off / room temp** during FDM on film—heated bed softens TPU substrate; exception ~30 °C bed noted for one pneumatic case |
| 4D pre-shape | PLA on TPU film + hot water | Dissolvable supports for large concave arches; dissolve 30–40 °C then hot-water trigger |

**Design-space primitives (four categories).** (1) Passive deformation—printed structures steer inflation direction (simultaneous / async / multi-direction). (2) Constraint—tune bend angle, reverse bend, connect multiple bladders. (3) Pre-shaping—4D-printed PLA contracts on heat while TPU film stays stable; convex bending requires discontinuous arch pattern (TPU film must stay bottom layer). (4) Function-extending—conductive filament touch→bend→auto-deflate demo; dot-array friction tuning.

**Applications demonstrated.** Kinetic sculpture (mimosa touch-deflate), Venus-flytrap biomimetic gripper (constraint + conductive spikes + friction dots), customized 4D-framed massage neck pillow, hedgehog desktop toy (4D shell + inflatable body).

**Reader translation (Bambu / Flashforge FDM).** [CONFIRMED] Workflow is consumer FDM + sheet stock, not a new printer class. [TENTATIVE 2026-05-23] Orca-Flashforge / non-Bambu printers should work if they can run custom low-speed heat-seal G-code and cold-bed PLA-on-film profiles—only **Bambu A1** validated in paper. Labor and Rhino toolchain are high; best fit is **interactive art / kinetic Etsy niche**, not production jigs.

**Contrast — no-film airtight TPU:** @sources/2026-abboodi-airtight-spa-fdm.md prints the pressure boundary as **monolithic TPU walls** (wall-line architecture + dried filament) instead of heat-sealed film. DuoMorph wins on consumer-printer + 4D pre-shape; Abboodi is lab **REFERENCE** only.

## Snippets

> "the entire hybrid structure can be fabricated through a single, seamless process using only a standard FDM printer—including both heat-sealing and 3D/4D printing." [Source: 2026-li-duomorph-fdm-pneumatic.pdf p.1]

> "we used a standard single-nozzle Bambu Lab A1 Series 3D printer for integrated heat sealing and printing." [Source: 2026-li-duomorph-fdm-pneumatic.pdf p.5]

> "it is recommended to keep the bed at room temperature (i.e., turn off bed heating)" for FDM on sealed film. [Source: 2026-li-duomorph-fdm-pneumatic.pdf p.6]
