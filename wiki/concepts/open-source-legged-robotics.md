---
title: Open-Source Legged Robotics — FDM Platforms and Printed Tactile Sensing
type: concept
tags: [robotics, open-source, humanoid, quadruped, tactile-sensing, FDM, advanced]
keywords: [legged robot, Berkeley Humanoid Lite, MEVITA, MEVIUS, eFlesh, M3D-skin, sim-to-real, democratization]
related:
  - concepts/fdm-printing.md
  - concepts/novice-cad-workflows.md
  - concepts/ai-design-tools.md
  - entities/materials/tpu.md
  - entities/printers/flashforge-adventurer-5m.md
  - sources/2025-chi-berkeley-humanoid-lite.md
  - sources/2025-kawaharazuka-mevita-bipedal.md
  - sources/2024-kawaharazuka-mevius-quadruped.md
  - sources/2025-pattabiraman-eflesh-magnetic-tactile.md
  - sources/2025-yoshimura-m3d-skin-tactile-fdm.md
  - concepts/soft-robotics-fdm-diw.md
  - sources/2026-hansen-tendon-actuated-tpu-backbone.md
  - sources/2025-miyama-soft-hand-skin-skeleton.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

@concepts/fdm-printing.md @concepts/novice-cad-workflows.md @concepts/ai-design-tools.md @entities/materials/tpu.md @entities/printers/flashforge-adventurer-5m.md @sources/2025-chi-berkeley-humanoid-lite.md @sources/2025-kawaharazuka-mevita-bipedal.md @sources/2024-kawaharazuka-mevius-quadruped.md @sources/2025-pattabiraman-eflesh-magnetic-tactile.md @sources/2025-yoshimura-m3d-skin-tactile-fdm.md

## Raw Concept

Ingest pass 9 (2026-06-01): five inbox papers on **open legged robots** and **FDM-fabricated tactile skins**. Synthesizes what desktop printing contributes vs where projects leave FFF for metal/welding — and what a beginner should **not** attempt on week 1.

## Narrative

### Two lanes in this cluster

| Lane | Papers | FDM role |
|------|--------|----------|
| **Full robots** | Berkeley Humanoid Lite; MEVITA; MEVIUS | Humanoid Lite is **FDM-centric** (cycloidal printed gearboxes). MEVITA/MEVIUS (JSK Tokyo) use FDM for **prototyping context** but ship **sheet-metal + e-commerce** for durability |
| **Tactile skins** | eFlesh; M3D-skin | **Sensor-only** prints on hobby FDM; integrate onto arms, feet, grippers |

### The durability split [CONFIRMED across MEVITA + MEVIUS abstracts]

Open **3D-printed** quadrupeds/bipeds exist (Solo, PAWDQ, many OS bipeds cited in MEVITA intro), but JSK authors argue plastic-only legs are **too fragile** for outdoor/aggressive use and **part-count** hurts maintenance. Berkeley Humanoid Lite pushes back by engineering **printed cycloidal drives** and testing actuator life — still a research platform, not a product.

**Practical takeaway for store ops:** printed robot **cosplay shells, mounts, and jigs** — yes; printed **load-bearing locomotion** at scale — expect metal upgrades or accept breakage.

### Tactile sensing on a desktop printer

| Approach | Source | Hardware | Beginner? |
|----------|--------|----------|-----------|
| **Magnetic cut-cell** | @sources/2025-pattabiraman-eflesh-magnetic-tactile.md | Single-nozzle FDM + magnet pause + Hall PCB | Advanced hobby |
| **Conductive TPU infill** | @sources/2025-yoshimura-m3d-skin-tactile-fdm.md | **Multi-material FDM** (TPU + conductive TPU) | Needs MMU/dual — not stock Adventurer 5M |

Both are **open-source robotics** paths more realistic than building a full humanoid on a first printer.

### Control stack (common thread)

All three robot platforms demo **reinforcement learning + Sim-to-Real**. That is **software + simulation** heavy — orthogonal to slicer tuning. Do not conflate "I have Klipper" with "I can train a biped policy."

### Explicit skip list (friend / novice readers)

See @concepts/novice-cad-workflows.md — add:

- Full humanoid/quadruped builds (Berkeley Lite, MEVITA, MEVIUS)
- Multi-material conductive-sensor prints unless hardware supports it
- eFlesh until comfortable with **pause-insert-resume** workflows and basic electronics

**When to revisit:** Etsy seller exploring **robot-themed accessories**, custom gripper pads (eFlesh), or after mastering TPU on @entities/materials/tpu.md.

## Snippets

> "Most existing open-source bipedal robots are designed to be fabricated using 3D printers, which limits their scalability in size and often results in fragile structures." [Source: 2025-kawaharazuka-mevita-bipedal.pdf p.1 via @sources/2025-kawaharazuka-mevita-bipedal.md]

> "Building an eFlesh sensor requires only four components: a hobbyist 3D printer, off-the-shelf magnets (< $5), a CAD model of the desired shape, and a magnetometer circuit board." [Source: 2025-pattabiraman-eflesh-magnetic-tactile.pdf p.1 via @sources/2025-pattabiraman-eflesh-magnetic-tactile.md]
