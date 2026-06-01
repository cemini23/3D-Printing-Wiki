---
title: MEVITA — Open-Source Bipedal Robot (E-Commerce + Sheet Metal)
type: source
tags: [paper, robotics, bipedal, open-source, sheet-metal, reinforcement-learning]
keywords: [MEVITA, JSK Tokyo, sheet metal welding, e-commerce robot, sim-to-real, open hardware]
related:
  - concepts/open-source-legged-robotics.md
  - sources/2024-kawaharazuka-mevius-quadruped.md
  - sources/2025-chi-berkeley-humanoid-lite.md
  - concepts/fdm-printing.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
read_status: skimmed
---

## Relations

@concepts/open-source-legged-robotics.md @sources/2024-kawaharazuka-mevius-quadruped.md @sources/2025-chi-berkeley-humanoid-lite.md @concepts/fdm-printing.md

## Raw Concept

- Title: MEVITA: Open-Source Bipedal Robot Assembled from E-Commerce Components via Sheet Metal Welding
- Authors: Kento Kawaharazuka, Shogo Sawaguchi, Ayumu Iwata, Keita Yoneda, Temma Suzuki, Kei Okada (University of Tokyo / JSK)
- Type: arXiv:2508.17684
- Location: `raw-sources/2025-kawaharazuka-mevita-bipedal.pdf`
- Retrieved: 2026-06-01
- Read-status: skimmed (abstract + intro)
- Open source: https://github.com/haraduka/mevita

## Narrative

**Design thesis.** Minimal viable **open-source biped** built entirely from **e-commerce parts**, using **sheet-metal welding** to merge complex geometry into fewer parts — easier assembly than metal robots with hundreds of machined pieces.

**Critique of 3D-print-only bipeds.** Most open bipeds target **3D printing**, which the authors argue **limits scale** and yields **fragile structures**. MEVITA deliberately trades away print-at-home convenience for **robustness** and **maintainability**.

**Control.** RL in simulation + **Sim-to-Real** → robust walking in varied environments.

**Reader fit.** Not an FDM-only project — needs welding/machining access. Pairs with @sources/2024-kawaharazuka-mevius-quadruped.md (same lab, quadruped variant) and contrasts @sources/2025-chi-berkeley-humanoid-lite.md (FDM-heavy humanoid). For Etsy sellers: background on why **functional robots** rarely stay on hobby printers alone.

## Snippets

> "Most existing open-source bipedal robots are designed to be fabricated using 3D printers, which limits their scalability in size and often results in fragile structures." [Source: 2025-kawaharazuka-mevita-bipedal.pdf p.1]

> "We utilized sheet metal welding to integrate complex geometries into single parts, thereby significantly reducing the number of components and enabling easy assembly for anyone." [Source: 2025-kawaharazuka-mevita-bipedal.pdf p.1]
