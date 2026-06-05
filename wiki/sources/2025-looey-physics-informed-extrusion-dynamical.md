---
title: Physics-Informed Dynamical Modeling of Extrusion-Based 3D Printing
type: source
tags: [paper, extrusion, control, CFD, reduced-order-model, DIW, cement]
keywords: [Navier-Stokes, reduced-order model, ANSYS Fluent, DIW, cementitious, PSU]
related:
  - concepts/extrusion-control.md
  - concepts/fdm-printing.md
  - sources/2026-mohammadi-rce-lqr-extrusion.md
  - sources/2025-lin-camera-extrusion-optimization.md
maturity: draft
created: 2026-06-02
updated: 2026-06-05
read_status: deep-read
---

## Relations

@concepts/extrusion-control.md @concepts/fdm-printing.md @sources/2026-mohammadi-rce-lqr-extrusion.md @sources/2025-lin-camera-extrusion-optimization.md

## Raw Concept

- Title: Physics-Informed Dynamical Modeling of Extrusion-Based 3D Printing Processes
- Authors: Mandana Mohammadi Looey, Marissa Loraine Scalise, Amrita Basak, Satadru Dey (Penn State ME)
- Type: arXiv:2512.11048v2 (Dec 2025); ASME J. Manuf. Sci. Eng. DOI 10.1115/1.4071622
- Location: `raw-sources/2025-looey-physics-informed-extrusion-dynamical.pdf`
- Retrieved: 2026-06-02; deep-read: 2026-06-05
- Funding: NSF 2346650 (same lab as @sources/2026-mohammadi-rce-lqr-extrusion.md)

## Narrative

**Modality [CONFIRMED].** Title says "extrusion-based AM" generically, but **every application and validation target is cementitious DIW** — viscoplastic ink, pumping force inlet, moving build plate. **Not validated on desktop FFF/PLA.** Literature review cites FFF reduced-order work (Meng et al. thermo-viscoelastic filament) only as related prior art.

**Problem.** High-fidelity CFD (ANSYS Fluent) captures strand cross-section and nozzle-gap dynamics but is too slow for **online control**. Paper builds a **control-oriented reduced-order model (ROM)** from Navier–Stokes via spatial averaging → ODE-like structure → **nonlinear least-squares** fit to Fluent simulation trajectories.

**Three-subsystem decomposition.**

| Sub-system | Region | Model basis |
|------------|--------|-------------|
| 1 | Nozzle interior | First-principles averaged continuity/momentum |
| 2 | Nozzle–substrate gap | **Simplified algebraic relation** (weaker physics) |
| 3 | Deposited layer on moving plate | First-principles formulation |

**Identified inputs (CFD sweep).** Inlet **mass flow rate** 0.02475–0.03465 kg/s; substrate **surface velocity** 50–70 mm/s. Training on boundary cases, testing on interior interpolation and extrapolation.

**Accuracy [CONFIRMED].** Sub-systems 1 and 3: velocity errors mostly within **±0.005 m/s**; sub-system 2 shows wider error spread (expected — algebraic surrogate). ROM interpolates mass-flow conditions well; **high-end extrapolation** degrades when trained only on low-flow data (nonlinear coupled effects).

**Consumer FFF link.** Abstract flow-dynamics vocabulary (transient extrusion, gap region) **rhymes with** pressure-advance / corner-blob physics in @concepts/extrusion-control.md, but **no parameter port** to Bambu K-values or Orca flow tuning — different material (cement paste vs polymer melt), different actuation (pump force vs filament gear). Pair with @sources/2026-mohammadi-rce-lqr-extrusion.md for **closed-loop cement** research arc, not slicer presets.

**Reader fit.** Skip unless building custom extrusion control research. Store ops / friend setup: no action.

## Snippets

> "To the best of the authors' knowledge, no existing study has formulated a reduced-order model specifically for the flow dynamics in DIW."
[Source: 2025-looey-physics-informed-extrusion-dynamical.pdf p.2]

> "Across all operating conditions, the errors remain confined within approximately −0.005 m/s to 0.005 m/s, underscoring the model's excellent predictive accuracy and numerical stability." (sub-system 1, interpolative case)
[Source: 2025-looey-physics-informed-extrusion-dynamical.pdf p.13]

> "The model for sub-system 2 is based on a simplified algebraic relation rather than a first-principles formulation."
[Source: 2025-looey-physics-informed-extrusion-dynamical.pdf p.14]
