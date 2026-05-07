---
title: High-Speed FDM
type: concept
tags: [process, high-speed, regime-shift]
keywords: [print speed, dynamic mismatch, corner over-extrusion, ringing, ghosting, gantry resonance]
related:
  - concepts/fdm-printing.md
  - concepts/input-shaping.md
  - concepts/extrusion-control.md
  - sources/2025-aung-adaptive-input-shaper.md
  - sources/2025-lin-camera-extrusion-optimization.md
  - sources/2025-hoteit-closed-loop-extrusion-lqr.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

@concepts/fdm-printing.md @concepts/input-shaping.md @concepts/extrusion-control.md @sources/2025-aung-adaptive-input-shaper.md @sources/2025-lin-camera-extrusion-optimization.md @sources/2025-hoteit-closed-loop-extrusion-lqr.md

## Raw Concept

Why "fast" Bambu printers (X1, P1, A1) actually print 5-10x faster than a 2018-era Prusa, and why that change required new control techniques rather than just bigger motors.

## Narrative

Below ~150 mm/s, FDM print quality is dominated by **positioning accuracy** — the toolhead has to be where the G-code says it should be. Above ~300 mm/s, the dominant error sources shift to **dynamic mismatch**:

- The gantry rings at its resonant frequency on every direction change. Mitigated by [@concepts/input-shaping.md] [Source: 2025-aung-adaptive-input-shaper.pdf].
- The extruder over- and under-shoots flow rate at corners and speed transitions. Mitigated by [@concepts/extrusion-control.md] — either G-code-side optimization [Source: 2025-lin-camera-extrusion-optimization.pdf] or closed-loop force feedback [Source: 2025-hoteit-closed-loop-extrusion-lqr.pdf].
- Layer cooling is bandwidth-limited at high deposition rates; insufficient cooling causes layer sag and bridging failures [TENTATIVE — not in the current 5-paper cluster] [NEEDS VERIFICATION 2026-05-06].

The pivot from "slow positioning-bound" to "fast dynamic-mismatch-bound" is what made Bambu's value proposition possible. The 2025 ETH Zurich / Inspire AG cluster [Sources: 2025-lin-camera-extrusion-optimization.pdf, 2025-hoteit-closed-loop-extrusion-lqr.pdf] is extending it further — though both papers validate at speeds (≤60 mm/s for Lin's Ender-3 V2; research-grade 5-axis hardware for Hoteit) that are below what Bambu cruises at out-of-the-box. Their contribution is *technique generalization* rather than absolute-speed records.

## Snippets

> "Experiments show reduced width tracking error, mitigated corner defects, and lower surface roughness, achieving surface quality at 3600 mm/min comparable to conventional printing at 1600 mm/min, effectively doubling production speed while maintaining print quality."
[Source: 2025-lin-camera-extrusion-optimization.pdf p.1 (abstract)]
