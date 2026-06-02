---
title: Physics-Informed Dynamical Modeling of Extrusion-Based 3D Printing
type: source
tags: [paper, extrusion, control, CFD, reduced-order-model, DIW]
keywords: [Navier-Stokes, reduced-order model, extrusion dynamics, real-time control, CFD validation, DIW]
related:
  - concepts/extrusion-control.md
  - concepts/fdm-printing.md
  - sources/2026-mohammadi-rce-lqr-extrusion.md
  - sources/2025-lin-camera-extrusion-optimization.md
maturity: draft
created: 2026-06-02
updated: 2026-06-02
read_status: skimmed
---

## Relations

@concepts/extrusion-control.md @concepts/fdm-printing.md @sources/2026-mohammadi-rce-lqr-extrusion.md @sources/2025-lin-camera-extrusion-optimization.md

## Raw Concept

- Title: Physics-Informed Dynamical Modeling of Extrusion-Based 3D Printing Processes
- Authors: Mandana Mohammadi Looey, Marissa Loraine Scalise, Amrita Basak, Satadru Dey
- Type: arXiv:2512.11048 (Dec 2025); ASME J. Manuf. Sci. Eng. DOI 10.1115/1.4071622 [TENTATIVE link from arXiv metadata]
- Location: `raw-sources/2025-looey-physics-informed-extrusion-dynamical.pdf`
- Retrieved: 2026-06-02 (manual fetch after daily digest flagged Springer mirror, not arXiv)
- Read-status: skimmed (abstract + intro)
- Discovered via: `wiki/sweeps/2026-06-02-daily.md` paper lane P1

## Narrative

**Problem.** High-fidelity CFD models extrusion AM well but are too heavy for **online control**. Consumer FFF control (pressure advance, camera calibration) uses empirical heuristics — this paper targets **control-oriented reduced-order models** grounded in **Navier–Stokes** with spatial averaging and input-dependent parameters.

**Method.** Nonlinear least-squares identification on CFD simulation data; validated in nozzle, nozzle–substrate gap, and deposited-layer regions.

**Modality caveat.** Primary motivation and examples are **cementitious DIW** (same author group as @sources/2026-mohammadi-rce-lqr-extrusion.md), not desktop PLA on a Bambu. The **flow-dynamics abstraction** still relates to @concepts/extrusion-control.md and @sources/2025-lin-camera-extrusion-optimization.md (FFF extrusion transients) at research depth only.

**Reader fit.** Skip unless building custom closed-loop extrusion research — not a slicer setting. Pairs with LQR cementitious control paper from same lab.

## Snippets

> "The proposed reduced-order model successfully captures the dominant flow dynamics of the process while maintaining a level of simplicity compatible with real-time control and optimization." [Source: 2025-looey-physics-informed-extrusion-dynamical.pdf p.1]

> "Dynamical modeling tailored for online, control-oriented applications is still significantly under-developed." [Source: 2025-looey-physics-informed-extrusion-dynamical.pdf p.1]
