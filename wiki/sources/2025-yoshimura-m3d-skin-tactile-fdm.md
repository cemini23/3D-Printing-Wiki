---
title: M3D-skin — Multi-Material FDM Tactile Sensor via Infill
type: source
tags: [paper, robotics, tactile-sensing, FDM, multi-material, TPU, conductive-filament]
keywords: [M3D-skin, piezoresistive infill, conductive TPU, hierarchical infill, JSK Tokyo, pressure sensing]
related:
  - concepts/open-source-legged-robotics.md
  - concepts/fdm-printing.md
  - entities/materials/tpu.md
  - sources/2025-pattabiraman-eflesh-magnetic-tactile.md
  - sources/2024-kawaharazuka-mevius-quadruped.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
read_status: skimmed
---

## Relations

@concepts/open-source-legged-robotics.md @concepts/fdm-printing.md @entities/materials/tpu.md @sources/2025-pattabiraman-eflesh-magnetic-tactile.md @sources/2024-kawaharazuka-mevius-quadruped.md

## Raw Concept

- Title: M3D-skin: Multi-material 3D-printed Tactile Sensor with Hierarchical Infill Structures for Pressure Sensing
- Authors: Shunnosuke Yoshimura, Kento Kawaharazuka, Kei Okada (University of Tokyo / JSK)
- Type: arXiv:2510.12419
- Location: `raw-sources/2025-yoshimura-m3d-skin-tactile-fdm.pdf`
- Retrieved: 2026-06-01
- Read-status: skimmed (abstract + Fig. 1)
- Open source: not verified in skim [NEEDS VERIFICATION 2026-06-01]

## Narrative

**Sensing principle.** Uses **FDM infill patterns** as the sensor: alternating **conductive** and **non-conductive flexible** filaments in a **hierarchical infill** structure. Pressure deforms the lattice → **resistance change** → tactile signal. No separate molding step.

**Materials (Fig. 1).** Red = **TPU**; black = **conductive TPU** — multi-material printer required.

**Demonstrations.** Multi-tile sensors; foot-sole motion measurement; **robotic hand integration**; tactile manipulation tasks.

**Reader fit.** Directly uses **consumer FDM modalities** (TPU + specialty conductive filament) that a multi-toolhead or MMU owner might explore. Same research group as MEVIUS/MEVITA. Contrast magnetic @sources/2025-pattabiraman-eflesh-magnetic-tactile.md — M3D-skin needs **dual-extrusion or multi-material**, eFlesh needs **magnet pause-insert**. Flashforge 5M is **single-nozzle** — M3D-skin is **not hardware-compatible without upgrades** [TENTATIVE].

## Snippets

> "We propose a tactile sensor—M3D-skin—that can be easily fabricated with high versatility by leveraging the infill patterns of a multi-material fused deposition modeling (FDM) 3D printer as the sensing principle." [Source: 2025-yoshimura-m3d-skin-tactile-fdm.pdf p.1]

> "This method employs conductive and non-conductive flexible filaments to create a hierarchical structure with a specific infill pattern." [Source: 2025-yoshimura-m3d-skin-tactile-fdm.pdf p.1]
