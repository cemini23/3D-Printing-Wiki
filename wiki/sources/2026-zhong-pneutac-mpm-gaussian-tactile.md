---
title: "PneuTac — MPM + Gaussian splatting simulator for tactile soft robots (arXiv:2609.38418)"
type: source
tags: [paper, soft-robotics, tactile, simulation, MPM, Gaussian-splatting, pneumatic, PolyJet]
keywords: [PneuTac, material point method, 3D Gaussian splatting, Digit sensor, GelSight, sim-to-real, behaviour cloning, demonstration augmentation, Genesis, CMA-ES, Agilus30, PolyJet]
related:
  - concepts/soft-robotics-fdm-diw.md
  - concepts/fdm-printing.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
read_status: deep-read
wire_status: wont_wire
wire_target: "Simulation/sim-to-real REFERENCE; 3D-printing Phase-1 local wires off"
---

## Relations

@concepts/soft-robotics-fdm-diw.md @concepts/fdm-printing.md

## Raw Concept

- **Title:** PneuTac: Tactile Manipulation with Soft Pneumatic Robots via Unified MPM-Gaussian Splatting Simulation
- **Authors:** Shaohong Zhong, Marco Pontin, Joe Watson, Perla Maiolino, Ingmar Posner
- **Affiliation:** Oxford Robotics Institute, Department of Engineering Science, University of Oxford
- **Type:** Conference-format paper (IEEE-style, cs.RO)
- **arXiv:** 2609.38418v1 [cs.RO] — 29 Sep 2026
- **Pages:** 8
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2609.38418-pneutac-tactile-manipulation-with-soft-pneumatic.pdf`
- **Read-status:** deep-read

## Narrative

A **simulation** paper about learning tactile manipulation on soft pneumatic robots. Its value here is the **sim-to-real methodology** and one unusually clean experimental result about simulator fidelity.

### The problem

Training a tactile policy on real soft hardware is slow and destroys the parts. Simulation should help — but existing tools model the soft robot and the tactile sensor **separately**, and both need heavy calibration that drifts as materials degrade [CONFIRMED paper, §I].

PneuTac's claim is that **nobody had jointly modelled a compliant actuator and a compliant gel-based tactile sensor** in one policy-learning pipeline before.

### How it works

| Piece | Method |
|---|---|
| Soft-body dynamics | **Material point method (MPM)** — particle–grid scheme, handles large deformation and contact |
| Gel (sensor) dynamics | MPM as well, at higher resolution |
| Appearance / rendering | **3D Gaussian Splatting (3DGS)** coupled to the MPM particles |
| Actuation | A rigid multi-joint spine along the finger's neutral axis drives the pneumatic chamber |
| Material model | Neo-Hookean, via the Genesis simulator |
| Calibration solver | CMA-ES (population 7, 84 evaluations) |

Particles: **~4k** for the soft robot, **~60k** for the gel — the gel needs the higher resolution to deform believably under contact [CONFIRMED paper, §V.A].

### The calibration claim is the interesting one

The paper reports real-to-sim calibration from **one** image for the robot and **one** indentation image for the tactile sensor:

- Robot: actuate at 6 preset pressures (0–15 kPa), compare a 3DGS render to a segmented photo. Loss = masked appearance loss + silhouette IoU (λ=2) [Source: ...pdf §IV.A.1].
- Tactile: train 3DGS on **one** rest image, then fit a slope- and depth-dependent contact photometric model from **one** indentation image [Source: ...pdf §IV.A.2].

Identified parameters came out physically plausible, and the paper notes the Young's modulus sits in the range expected from the printer [Source: ...pdf §V.A]:

| Parameter | Value | Meaning |
|---|---|---|
| G | 0.01114 rad/kPa | Pressure-to-bending gain |
| α, β | 0.0313, 0.2974 | Per-joint gain distribution |
| p₀ | 10.70 kPa | Residual rest pressure (absorbs gravity-induced curl) |
| E_s | 0.945 MPa | Young's modulus |
| ν_s | 0.460 | Poisson's ratio |

**Tip tracking:** 4.2 ± 0.4 mm for the finger (<4% of length) and 4.9 ± 1.0 mm for a three-chamber arm (4.2%) — on **held-out pressure levels** never used in calibration [CONFIRMED paper, §V.A.1].

### Surrogate models make it fast

Running full MPM is too slow for policy learning, so two learned surrogates replace it [CONFIRMED paper, §V.B]:

| Surrogate | Job | Speedup |
|---|---|---|
| MLP (2×128), residual joint torque | Match full-MPM actuation | **5×** (~10 ms vs ~50 ms) |
| UNet, probe → MPM indentation | Map a fast probe grid to MPM depths | **3000×** (~50 ms vs ~150 s) |

The MLP leaves a mean joint position error of 0.051 ± 0.006°; the UNet maps indentation with 0.077 ± 0.005 mm MAE against a mean depth of 1.4 mm.

### Hardware — and it is not FDM

The soft finger was printed on a **Stratasys PolyJet**: **Agilus30** for the soft body and **Vero** for the rigid part. The tactile sensor is a **Digit** sensor with an **Ecoflex 00-31 Near Clear** gel [CONFIRMED paper, §IV].

So like MONORIGAMI in [@concepts/soft-robotics-fdm-diw.md], this is a **non-FDM** process. PolyJet is a material-jetting photopolymer process — a different machine class from a Bambu. Do not file this as a printable-on-a-Bambu result.

For scale it also ran on a structurally different **three-chamber soft arm** and on an **unmodified Digit sensor** to test cross-device generalization.

### The result worth remembering

Ten real demonstrations per task, bootstrapped to **100 simulated** demonstrations each, then behaviour cloning with real-world fine-tuning. Three tasks: **switch flipping**, **egg carton opening**, **card pulling** [CONFIRMED paper, §IV.C/§V.C]:

| Task | Sim+Real | Real (10 demos) | Real-20 | No-Tac | PPO |
|---|---|---|---|---|---|
| Switch | 83.3 ± 3.3 | 60.0 ± 5.8 | **90.0 ± 5.8** | 30.0 ± 5.8 | 63.3 ± 3.3 |
| Egg carton | **90.0 ± 5.8** | 26.7 ± 8.8 | 40.0 ± 10.0 | 56.7 ± 3.3 | 80.0 ± 5.8 |
| Card pulling | **66.7 ± 3.3** | 33.3 ± 8.8 | 50.0 ± 5.8 | 63.3 ± 3.3 | **10.0 ± 5.8** |

Three findings, each with a different lesson:

1. **Simulation-augmented data beats real-only data** — but not everywhere. On the **switch** task, simply doubling the real demonstration count (**Real-20**, 90.0%) **matched or beat** the simulation pipeline (83.3%). The paper reads this as: where 10 real demos are already informative, real data wins on cost. Simulation pays off **where real data under-samples the success manifold** — the egg and card tasks [CONFIRMED paper, §V.C].
2. **Tactile feedback helps contact-dominated tasks, not position-dominated ones.** Removing it (No-Tac) collapsed the switch (30.0%) and hurt the egg (56.7%), but barely moved card pulling (63.3%) — consistent with card pulling being **position-** rather than contact-dominated [Source: ...pdf §V.C].
3. **A weak simulator punishes reinforcement learning harder than imitation learning.** PPO scored **10.0%** on card pulling, far below the behaviour-cloning pipeline. The authors attribute this to reduced simulator fidelity for **card-on-card contact** — and note PPO's reward-driven exploration is more exposed to that than a BC policy anchored on real demonstrations [Source: ...pdf §V.C].

Finding 3 is the transferable one. If your simulator is wrong about a contact mode, exploration will find and exploit the error; an imitation policy stays anchored to real behaviour. Cheap simulators are not neutral between RL and IL.

### Honest limits

- **No direct comparison to another simulator is available** for the full pipeline. The paper states this openly: few existing frameworks natively model the paired devices, so baselines were compared per-component (tactile rendering, appearance) rather than end-to-end [Source: ...pdf §V.C].
- **Tactile rendering baselines:** PneuTac RMSE 10.18 vs Tacchi 10.86, DOT-Sim 14.14, Taxim 14.13 (NCC 0.982). Real gains, but Tacchi is close.
- **Calibration does not transfer between sensor units.** A second, unmodified Digit sensor scored well when re-calibrated (RMSE 8.12), but **reusing the original calibration gave RMSE 22.96** [Source: ...pdf §V.A.2]. Devices differ; recalibrate per unit.
- The card task's poor PPO result is a **fidelity** limitation the authors acknowledge, not a solved problem.

### Where this sits in the wiki

- Extends the soft-robotics cluster [@concepts/soft-robotics-fdm-diw.md] with its first **simulation/sim-to-real** entry.
- Another **non-FDM** soft-robotics paper (PolyJet), alongside MONORIGAMI (SLA) — reinforcing that consumer-FDM soft robotics is a research-adjacent activity, not a day-1 one.
- Vision-based tactile sensing (Digit/GelSight family) connects to the tactile cluster in [@concepts/open-source-legged-robotics.md] (eFlesh, M3D-skin), though those are printed sensors, not simulated ones.

**Phase-0:** no repository, no code release. Uses open-source Genesis + off-the-shelf 3DGS, but ships neither. **REFERENCE** only. **Phase-1:** `wont_wire`.

## Snippets

> "To our knowledge, no prior work has been able to jointly model compliant actuation and compliant tactile sensing for policy learning." [Source: 2026-zhong-pneutac-mpm-gaussian-tactile.pdf p.1]

> "The soft part of the finger is 3D printed using a Stratasys printer with Agilus30 material, whereas the rigid part is printed using Vero." [Source: 2026-zhong-pneutac-mpm-gaussian-tactile.pdf p.4]

> "The no-tactile result shows that tactile feedback substantially improves success on switch and egg carton opening, but the observed difference on card pulling is small, consistent with card pulling being position- rather than contact-dominated." [Source: 2026-zhong-pneutac-mpm-gaussian-tactile.pdf p.7]

> "Its failure on card is consistent with the simulator's reduced fidelity for card-on-card contact, to which PPO's reward-driven exploration is likely more exposed than the BC policy anchored on real demonstrations." [Source: 2026-zhong-pneutac-mpm-gaussian-tactile.pdf p.7]
