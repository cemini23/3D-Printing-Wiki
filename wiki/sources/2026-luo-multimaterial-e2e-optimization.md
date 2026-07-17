---
title: Towards end-to-end optimization in multimaterial 3D printing (Cornell)
type: source
tags: [paper, multimaterial, topology-optimization, soft-robotics, background]
keywords: [FEniCSx, hyperelastic, digital materials, soft gripper, Bouklas, Shepherd]
related:
  - concepts/soft-robotics-fdm-diw.md
  - concepts/fdm-printing.md
  - sources/2026-arxiv-lane-noise-triage-jul16.md
  - sources/2026-chen-hybrid-rigid-soft-gripper.md
maturity: draft
created: 2026-07-16
updated: 2026-07-17
read_status: skimmed
---

## Relations

@sources/2026-chen-hybrid-rigid-soft-gripper.md @concepts/soft-robotics-fdm-diw.md @concepts/fdm-printing.md @sources/2026-arxiv-lane-noise-triage-jul16.md

## Raw Concept

- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2607.13174-towards-end-to-end-optimization-in-multimaterial.pdf`
- **Title:** Towards end-to-end optimization in multimaterial 3D printing
- **Authors:** Xue-Ling Luo, Steven Yang, Jingye Tan, Robert F. Shepherd, Noy Cohen, Nikolaos Bouklas (Cornell / USC / Technion / Pasteur Labs)
- **arXiv:** 2607.13174v1 [physics.comp-ph]
- **Retrieved:** 2026-07-16 digest
- **Pages:** 41
- **Read-status:** skimmed (abstract + intro)

## Narrative

Research framework: sparsified physics-augmented NNs → closed-form composition-aware hyperelastic laws → FEniCSx adjoint topology optimization of **digital-material** blends. Demo: soft robotic grippers with continuous composition + topology under stretch constraints.

**Wiki fit:** soft-robotics / advanced AM background — **not** Bambu AMS multi-color hobby workflow. No public code in skim. **Phase-0: REFERENCE** — no local adopt.

## Snippets

> "This methodology could replace laborious empirical prototyping, establishing interpretable machine-learning models as practical, robust design primitives for advanced multimaterial additive manufacturing."
[Source: arXiv:2607.13174v1 abstract]
