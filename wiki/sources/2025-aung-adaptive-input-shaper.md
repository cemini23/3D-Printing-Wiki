---
title: Adaptive Input Shaper Design for Unknown Second-Order Systems with Real-Time Parameter Estimation
type: source
tags: [paper, control, input-shaping, vibration]
keywords: [input shaper, time delay filter, parameter estimation, FDM gantry, second-order system, Weierstrass substitution, peak time, settling time]
related:
  - concepts/input-shaping.md
  - concepts/high-speed-fdm.md
  - concepts/fdm-printing.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
read_status: deep-read
---

## Relations

@concepts/input-shaping.md @concepts/high-speed-fdm.md @concepts/fdm-printing.md

## Raw Concept

- Title: Adaptive Input Shaper Design for Unknown Second-Order Systems with Real-Time Parameter Estimation
- Authors: Phyo Aung, Brittany Wight, Jeffrey Stein (Louisiana State University)
- Type: Conference paper / preprint
- Location: `raw-sources/2025-aung-adaptive-input-shaper.pdf`
- Retrieved: 2026-05-06
- Pages: 6
- Read-status: deep-read

## Narrative

Designs a feedforward Time Delay Filter (TDF) input shaper that adapts to a system's natural frequency (ωn) and damping ratio (ζ) without prior knowledge — targeting 3D-printer toolheads and gantry cranes whose payload mass / dynamic stiffness drift mid-print.

[TENTATIVE] The abstract advertises Recursive Least Squares (RLS) for parameter estimation, but Algorithm 1 (§III) actually estimates parameters from observed response features — max overshoot Mp, 2% settling time Ts, peak time TMp. For the undamped case the paper derives a closed-form solution via Weierstrass substitution; for the damped case it solves numerically. The "RLS" framing in the abstract does not match the recursive-update method described in the body [NEEDS VERIFICATION 2026-05-06].

Tested in simulation across ζ ∈ [0, 1], ωn ∈ [π, 3000π] rad/s under a step input (K = 0.01) with 0.1% measurement noise. **Simulation only — no hardware test.** Future work flagged: replace the hand-derived closed-form with a regression model trained on the response-features → parameter mapping.

Reference implementation released at https://github.com/NyiNyi-14/A-TDF.git [Source: 2025-aung-adaptive-input-shaper.pdf p.1].

**Practical bearing for a Bambu owner**: fixed input shaping is what consumer firmware ships today (Klipper, Bambu "Active Tuning"). This is the research direction that lets future printers tolerate variable payload (heavy spools, attached tools) without re-tuning. Not in any consumer firmware as of late 2025.

## Snippets

> "We propose an adaptive Time Delay Filter (TDF) input shaper for second-order systems with unknown natural frequency and damping ratio. The proposed scheme uses Recursive Least Squares (RLS) for online parameter estimation."
[Source: 2025-aung-adaptive-input-shaper.pdf p.1]

> "All models and implementations used in this work are made publicly available at https://github.com/NyiNyi-14/A-TDF.git."
[Source: 2025-aung-adaptive-input-shaper.pdf p.1]
