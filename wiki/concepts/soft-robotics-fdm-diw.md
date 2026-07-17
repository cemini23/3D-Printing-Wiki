---
title: Soft Robotics — FDM, DIW, and Tactile Tooling
type: concept
tags: [soft-robotics, DIW, tactile, TPU, advanced]
keywords: [soft hand, tendon robot, DIW sensors, 3D Cal, ionic actuator]
related:
  - concepts/open-source-legged-robotics.md
  - concepts/fdm-printing.md
  - entities/materials/tpu.md
  - sources/2025-miyama-soft-hand-skin-skeleton.md
  - sources/2026-hansen-tendon-actuated-tpu-backbone.md
  - sources/2025-clancy-magnetic-soft-microrobots.md
  - sources/2025-truempler-ionic-polymer-diw.md
  - sources/2025-cha-diw-stretchable-strain-sensors.md
  - sources/2025-kota-3d-cal-tactile-calibration.md
  - sources/2025-yoshimura-m3d-skin-tactile-fdm.md
  - sources/2025-pattabiraman-eflesh-magnetic-tactile.md
  - concepts/fdm-research-tools.md
  - sources/2026-mohammadi-rce-lqr-extrusion.md
  - sources/2026-luo-multimaterial-e2e-optimization.md
  - sources/2026-chen-hybrid-rigid-soft-gripper.md
maturity: draft
created: 2026-06-01
updated: 2026-07-17
---

## Relations

@sources/2026-chen-hybrid-rigid-soft-gripper.md @sources/2026-luo-multimaterial-e2e-optimization.md @concepts/open-source-legged-robotics.md @concepts/fdm-printing.md @entities/materials/tpu.md @sources/2025-miyama-soft-hand-skin-skeleton.md @sources/2026-hansen-tendon-actuated-tpu-backbone.md @sources/2025-clancy-magnetic-soft-microrobots.md @sources/2025-truempler-ionic-polymer-diw.md @sources/2025-cha-diw-stretchable-strain-sensors.md @sources/2025-kota-3d-cal-tactile-calibration.md @sources/2025-yoshimura-m3d-skin-tactile-fdm.md @sources/2025-pattabiraman-eflesh-magnetic-tactile.md

## Raw Concept

Ingest pass 11 — extends pass 9 (@concepts/open-source-legged-robotics.md) with soft hands, continuum TPU robots, DIW sensors/actuators, and **3D Cal** calibration tooling.

## Narrative

### Fabrication modalities

| Modality | Examples | Hobbyist fit |
|----------|----------|--------------|
| **Single-material flexible FDM** | Soft hand skin-skeleton | Advanced |
| **TPU FDM structure** | Tendon continuum backbone | Advanced + TPU skill |
| **Multi-material FDM sensing** | M3D-skin, eFlesh (pass 9) | MMU or pause-insert |
| **DIW on silicone** | Cha strain sensors; Trümpler ionic actuators | Custom hardware |
| **Printer as robot** | 3D Cal probing | Clever repurposing |

### 3D Cal pattern [CONFIRMED single source]

@sources/2025-kota-3d-cal-tactile-calibration.md — use desktop printer as **motion stage** for calibration data collection, not just part fabrication.


### Hybrid rigid–soft gripper (2026-07)

@sources/2026-chen-hybrid-rigid-soft-gripper.md — agricultural gripper with membrane pneumatics + **FDM/AM ratchet–pawl self-locking**; PLA spheres for bench tests. **REFERENCE** only (no public BOM). Complements multimaterial topology work (@sources/2026-luo-multimaterial-e2e-optimization.md).

## Snippets

(none — synthesis page)
