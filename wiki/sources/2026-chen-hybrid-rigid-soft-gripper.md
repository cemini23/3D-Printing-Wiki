---
title: "Hybrid Rigid-Soft Robotic Gripper — shape adaptation + self-locking (arXiv:2607.14730)"
type: source
tags: [paper, soft-robotics, gripper, FDM, agriculture, hybrid]
keywords: [ratchet-pawl, pneumatic membrane, PLA, self-locking, Ya Xiong, 4200g payload]
related:
  - concepts/soft-robotics-fdm-diw.md
  - concepts/fdm-printing.md
  - entities/materials/pla.md
  - sources/2026-luo-multimaterial-e2e-optimization.md
  - sources/2026-arxiv-lane-noise-triage-jul17.md
maturity: draft
created: 2026-07-17
updated: 2026-07-17
read_status: skimmed
---

## Relations

@concepts/soft-robotics-fdm-diw.md @concepts/fdm-printing.md @entities/materials/pla.md @sources/2026-luo-multimaterial-e2e-optimization.md @sources/2026-arxiv-lane-noise-triage-jul17.md

## Raw Concept

- **Title:** Hybrid Rigid-Soft Robotic Gripper with Shape Adaptation, Uniform Force Distribution, and Self-Locking Capabilities
- **Authors:** Xi Chen, Yun Wang, Lichao Yang, Haitao Li, Ya Xiong
- **arXiv:** 2607.14730
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2607.14730-hybrid-rigid-soft-robotic-gripper-with-shape-ada.pdf`
- **Retrieved:** 2026-07-17 overnight digest
- **Pages:** 8
- **Read-status:** skimmed (abstract, design, experiments, conclusion)

## Narrative

Agricultural hybrid gripper: **membrane pneumatic soft chambers** + **3D-printed dual ratchet–pawl** joints for energy-free self-locking after grasp. Claims vs continuous-pressure soft gripper: ~**4200 g** destructive load capacity (vs 45–210 g), more uniform contact force ratios, **~50% lower energy** per cycle (~42.6 J vs 85.28 J) by cutting continuous pneumatics once locked. Fruit/object demos (peach, pear, apple, kiwi, etc.).

**FDM wiki hook [CONFIRMED]:** PLA FDM (15% infill) used for spherical test artifacts; additive manufacturing for ratchet parts + COTS pneumatic chambers — low-cost fab story. Not a Bambu/Flashforge consumer print guide.

### Phase-0 (2026-07-17)

| Check | Result |
|-------|--------|
| Public repo | **None** in PDF |
| License / BOM | Paper-only |
| Hobby adopt | **NO-GO** — pneumatics + custom assembly; agricultural research |
| Verdict | **REFERENCE** — soft-robotics / hybrid gripper background |

No tipdrop / poker / prod brief — no agent-harness or image-gen steal.

## Snippets

> "The combination of additive manufacturing for ratchets and commercially available materials for pneumatic chambers ensured a low-cost and easily fabricated design."
[Source: arXiv:2607.14730 abstract]

> "The spherical models used in the experiments were fabricated using FDM 3D printing with diameters of 50 mm, 60 mm, and 70 mm. PLA basic filament was used, and the infill was set to 15%."
[Source: arXiv:2607.14730 §III.A]
