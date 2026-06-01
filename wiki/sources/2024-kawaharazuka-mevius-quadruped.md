---
title: MEVIUS — E-Commerce Quadruped (Sheet Metal, Not Plastic-Only)
type: source
tags: [paper, robotics, quadruped, open-source, sheet-metal, reinforcement-learning]
keywords: [MEVIUS, JSK Tokyo, quadruped robot, e-commerce, sim-to-real, outdoor durability]
related:
  - concepts/open-source-legged-robotics.md
  - sources/2025-kawaharazuka-mevita-bipedal.md
  - sources/2025-yoshimura-m3d-skin-tactile-fdm.md
  - concepts/fdm-printing.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
read_status: skimmed
---

## Relations

@concepts/open-source-legged-robotics.md @sources/2025-kawaharazuka-mevita-bipedal.md @sources/2025-yoshimura-m3d-skin-tactile-fdm.md @concepts/fdm-printing.md

## Raw Concept

- Title: MEVIUS: A Quadruped Robot Easily Constructed through E-Commerce with Sheet Metal Welding and Machining
- Authors: Kento Kawaharazuka, Shintaro Inoue, Temma Suzuki, Sota Yuzaki, Shogo Sawaguchi, Kei Okada, Masayuki Inaba (University of Tokyo / JSK)
- Type: arXiv:2409.14721
- Location: `raw-sources/2024-kawaharazuka-mevius-quadruped.pdf`
- Retrieved: 2026-06-01
- Read-status: skimmed (abstract + intro)
- Open source: https://github.com/haraduka/mevius

## Narrative

**Problem.** Commercial quadrupeds (ANYmal, Unitree Go1, etc.) are expensive and closed. Lab-scale **3D-printed** quadrupeds (Solo, PAWDQ cited) are cheap but **too fragile** for outdoor terrain, rubble, or aggressive gaits — and **many small parts** make maintenance painful.

**MEVIUS answer.** Metal quadruped from **e-commerce + machining + sheet-metal welding** only; minimal part count; simple electronics/software. RL + Sim2Real demonstrated on **rough outdoor terrains**.

**Three design requirements** (authors): (i) easy e-commerce/DIY assembly, (ii) low part count, (iii) durability in diverse environments.

**Reader fit.** Same JSK lineage as @sources/2025-kawaharazuka-mevita-bipedal.md and @sources/2025-yoshimura-m3d-skin-tactile-fdm.md. Background for anyone considering **robotics Etsy products** — printed plastic legs are a prototyping step, not the durability endpoint.

## Snippets

> "Most robots that can be built by research institutions are relatively small and made of plastic using 3D printers. These robots cannot withstand experiments in external environments such as mountain trails or rubble." [Source: 2024-kawaharazuka-mevius-quadruped.pdf p.1]

> "We develop a metal quadruped robot MEVIUS, that can be constructed and assembled using only materials ordered through e-commerce." [Source: 2024-kawaharazuka-mevius-quadruped.pdf p.1]
