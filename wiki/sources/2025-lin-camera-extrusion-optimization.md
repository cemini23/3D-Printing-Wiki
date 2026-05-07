---
title: One-Shot Camera-Based Extrusion Optimization for High Speed Fused Filament Fabrication
type: source
tags: [paper, vision, extrusion, high-speed-fdm, gcode-optimization]
keywords: [smartphone camera, G-code optimization, ETH Zurich, NematX, Inspire AG, Ender-3 V2, FFF, one-shot, optimal control, system identification]
related:
  - concepts/extrusion-control.md
  - concepts/high-speed-fdm.md
  - concepts/fdm-printing.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
read_status: deep-read
---

## Relations

@concepts/extrusion-control.md @concepts/high-speed-fdm.md @concepts/fdm-printing.md

## Raw Concept

- Title: One-Shot Camera-Based Extrusion Optimization for High Speed Fused Filament Fabrication
- Authors: Yufan Lin, Xavier Guidetti, Yannick Nagel, Efe C. Balta, John Lygeros (ETH Zurich Automatic Control Lab; Inspire AG; NematX AG)
- Type: arXiv preprint, arXiv:2512.24905v1 [eess.SY] — preprint submitted to *Additive Manufacturing*, 31 Dec 2025 / 1 Jan 2026
- Location: `raw-sources/2025-lin-camera-extrusion-optimization.pdf`
- Retrieved: 2026-05-06
- Pages: 32
- Read-status: deep-read (pages 1-15 — full method + identification + part of results; pages 16-32 not extracted, full-part validation results below the cut)

## Narrative

A camera-based offline pipeline that snaps phone-camera photos of **two calibration prints**, identifies the extrusion and corner dynamics, then rewrites the production G-code to compensate. Demonstrated on an **Ender-3 V2** budget printer to achieve surface quality at 3600 mm/min (60 mm/s) comparable to conventional printing at 1600 mm/min (26.7 mm/s) — i.e. effective ~2× speed at constant quality on this specific budget machine.

**Threat model / target user.** A typical hobbyist with a stock printer who wants more speed without firmware mods or hardware additions. The phone camera and printer are commodity; only the optimization framework is novel.

**Hardware.** Ender-3 V2 with 0.4 mm nozzle. Light-ivory PLA from Fillamentum (1.75 mm) on a dark print bed for measurement contrast. Layer height 0.2 mm fixed; bed 75 °C; nozzle 200 °C. Smartphone equipped with a 108-megapixel Samsung **S5KHMX** sensor (this is the back-camera sensor used in flagship phones such as the Galaxy S20 Ultra) [Source: 2025-lin-camera-extrusion-optimization.pdf p.6].

[TENTATIVE] The current source page previously claimed broad applicability to Bambu / Prusa / Voron — Lin only validated on Ender-3 V2. The framework should generalize to any FFF printer with G-code-level extrusion control, but per-printer calibration prints + identification are required, and the speed range Lin actually swept (1600–3600 mm/min ≈ 27–60 mm/s) is **slower than Bambu cruise speeds** (200–500 mm/s). [NEEDS VERIFICATION 2026-05-06]

**Pipeline (offline, two-pass):**

1. **Calibration print 1 — extrusion dynamics ID.** Print a step-reference width pattern. Photograph it. Fit a first-order model `w(s)/ξ(s) = α/(1+τs)` separately for width-expansion (`τ_expand`) and width-shrinkage (`τ_shrink`) transitions to capture viscous filament nonlinearity. Output: `α`, `τ_expand`, `τ_shrink`. [Source: 2025-lin-camera-extrusion-optimization.pdf p.6, p.13]
2. **Calibration print 2 — corner/cornering ID.** Print a four-corner high-speed pattern at a fixed extrusion ratio. Photograph it. Fit deceleration-induced over-extrusion at corner ends to identify printer-specific cornering parameters `v_m^c` and `a` [Source: 2025-lin-camera-extrusion-optimization.pdf p.13].
3. **Reference width construction.** Build a five-stage compensated-width reference per straight-line segment: (I) initial trim → (II) post-corner ramp-up → (III) constant-width steady → (IV) pre-corner ramp-down → (V) final trim. Concatenate segment-wise across the trajectory [Source: 2025-lin-camera-extrusion-optimization.pdf p.9].
4. **Constrained optimal control.** Discretize G-code path into `Δs` segments. Solve a quadratic program minimizing `Σ(w_k − w*_k)²` subject to (a) discretized first-order extrusion dynamics, (b) extrusion-ratio bounds `[ξ_low, ξ_high]`, (c) initial-condition continuity from preceding segment. Output: optimal `ξ*` per segment → emit `G0 X{...} Y{...} Z{...} E{ξ*·Δs}` G-code [Source: 2025-lin-camera-extrusion-optimization.pdf p.10].

**Headline result.** Surface quality at 3600 mm/min with optimization comparable to 1600 mm/min without optimization on the Ender-3 V2 — width tracking error reduced, corner defects mitigated, lower surface roughness [Source: 2025-lin-camera-extrusion-optimization.pdf p.1 abstract].

**Why this matters for the reader.** Wholly software, runs on existing G-code, no firmware mod. The closest published thing to "free 2× speed-up by post-processing your G-code" today. **Caveats**: only validated on Ender-3 V2; calibration is per-printer; the absolute speeds are still well below Bambu hardware-side capability — Lin's framework accelerates a *budget* printer, while Bambu already runs at 200–500 mm/s out of the box via input shaping + pressure advance + active flow control. Most useful for someone keeping a slower printer rather than for tuning a fast one.

[CONFIRMED] Single-source paper (Lin 2025 alone). The "two patterns / one-shot" terminology is consistent across abstract and main text. [TENTATIVE] Productizing as a slicer plugin is plausible but no published work exists; ETH Zurich + NematX may pursue this commercially.

## Snippets

> "Experiments show reduced width tracking error, mitigated corner defects, and lower surface roughness, achieving surface quality at 3600 mm/min comparable to conventional printing at 1600 mm/min, effectively doubling production speed while maintaining print quality."
[Source: 2025-lin-camera-extrusion-optimization.pdf p.1 (abstract)]

> "A practical one-shot identification and optimization pipeline that, from two simple calibration prints to identify parameters and automatically generates optimized G-code for most common 3D printers, facilitating high-speed printing optimization without specialized hardware or complex calibration."
[Source: 2025-lin-camera-extrusion-optimization.pdf p.4 (contributions)]

> "Currently, most desktop 3D printers utilize an open-loop control strategy, which produces acceptable results under ideal operation conditions. However, 3D printers have limited performance when the real machine behavior deviates from the expected one, for example when printing at very high speed."
[Source: 2025-lin-camera-extrusion-optimization.pdf p.2]
