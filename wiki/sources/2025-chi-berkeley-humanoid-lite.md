---
title: Berkeley Humanoid Lite — Open-Source 3D-Printed Humanoid
type: source
tags: [paper, robotics, humanoid, open-source, FDM, reinforcement-learning]
keywords: [Berkeley Humanoid Lite, cycloidal gearbox, 3D-printed actuator, democratization, sim-to-real, bipedal locomotion]
related:
  - concepts/open-source-legged-robotics.md
  - concepts/fdm-printing.md
  - entities/materials/pla.md
  - sources/2025-kawaharazuka-mevita-bipedal.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
read_status: skimmed
---

## Relations

@concepts/open-source-legged-robotics.md @concepts/fdm-printing.md @entities/materials/pla.md @sources/2025-kawaharazuka-mevita-bipedal.md

## Raw Concept

- Title: Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot
- Authors: Yufeng Chi, Qiayuan Liao, Junfeng Long, Xiaoyu Huang, Sophia Shao, Borivoje Nikolić, Zhongyu Li, Koushil Sreenath (UC Berkeley)
- Type: arXiv:2504.17249
- Location: `raw-sources/2025-chi-berkeley-humanoid-lite.pdf`
- Retrieved: 2026-06-01
- Pages: not counted (large PDF; abstract + intro skimmed)
- Read-status: skimmed (abstract, intro, Fig. 1)
- Open source: https://lite.berkeley-humanoid.org

## Narrative

**What it is.** A fully open-source **bipedal humanoid** whose structure and **modular cycloidal gearboxes** are **desktop-FDM printable**. Parts are sourced from e-commerce; total hardware **under $5,000** (U.S. pricing cited). Hardware, embedded code, and RL training/deployment stacks are released.

**Why cycloidal on plastic.** Metal harmonic drives dominate commercial humanoids but are expensive and closed. Cycloidal gears give a favorable form factor for **3D-printed plastic** despite lower strength vs machined metal — the paper reports durability testing on printed actuators.

**Research demo.** RL locomotion controller with **zero-shot sim-to-real** transfer on the physical platform.

**Reader fit (Flashforge / Bambu hobbyist).** [TENTATIVE] This is a **multi-month robotics project**, not a weekend print. Requires many printed gearboxes, electronics, and control stack — far beyond @concepts/novice-cad-workflows.md week-1 scope. Useful as a **reference design** for large functional FDM parts and open-hardware robotics economics. Contrast with @sources/2025-kawaharazuka-mevita-bipedal.md, which argues pure-3D-print bipeds scale poorly and moves to sheet-metal welding.

## Snippets

> "The core of this design is a modular 3D-printed gearbox for the actuators and robot body. All components can be sourced from widely available e-commerce platforms and fabricated using standard desktop 3D printers, keeping the total hardware cost under $5,000." [Source: 2025-chi-berkeley-humanoid-lite.pdf p.1]

> "We aim for Berkeley Humanoid Lite to serve as a pivotal step toward democratizing the development of humanoid robotics." [Source: 2025-chi-berkeley-humanoid-lite.pdf p.1]
