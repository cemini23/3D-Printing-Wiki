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
updated: 2026-05-08
---

## Relations

@concepts/fdm-printing.md @concepts/input-shaping.md @concepts/extrusion-control.md @sources/2025-aung-adaptive-input-shaper.md @sources/2025-lin-camera-extrusion-optimization.md @sources/2025-hoteit-closed-loop-extrusion-lqr.md

## Raw Concept

Why "fast" Bambu printers (X1, P1, A1) actually print 5-10× faster than a 2018-era Prusa, why that change required new control techniques rather than just bigger motors, and where the marketed-speed-vs-realistic-speed gap shows up in practice.

## Narrative

### Two speed regimes

Below ~150 mm/s, FDM print quality is dominated by **positioning accuracy** — the toolhead has to be where the G-code says it should be. Stepper resolution, lead-screw backlash, belt tension dominate.

Above ~300 mm/s, the dominant error sources shift to **dynamic mismatch** — the toolhead can be exactly where commanded, but the rest of the system can't keep up:

- The gantry rings at its resonant frequency on every direction change. Mitigated by [@concepts/input-shaping.md] [Source: 2025-aung-adaptive-input-shaper.pdf].
- The extruder over- and under-shoots flow rate at corners and speed transitions. Mitigated by [@concepts/extrusion-control.md] — either G-code-side optimization [Source: 2025-lin-camera-extrusion-optimization.pdf] or closed-loop force feedback [Source: 2025-hoteit-closed-loop-extrusion-lqr.pdf].
- Layer cooling is bandwidth-limited at high deposition rates; insufficient cooling causes layer sag, drooping bridges, and overhang collapse. [TENTATIVE 2026-05-08] Not directly in the 5-paper academic cluster; common-knowledge from slicer-tuning communities.

### Marketed speed vs cruise speed vs feature speed

Three numbers get conflated in printer marketing:

- **Maximum / marketed speed** (e.g. Bambu's "500 mm/s on X1C") — peak speed achievable, usually on a long unobstructed straight infill move. Limited by stepper torque / driver current. Reality on most prints: rarely sustained for more than a few cm at a time.
- **Cruise speed** — sustained speed on outer perimeters and infill in a typical mid-size print. Limited by acceleration ramp-up time relative to segment length.
- **Feature speed** — per-feature speed the slicer assigns: outer perimeters slower than inner perimeters, infill faster than perimeters, supports faster than infill, overhangs much slower than perimeters, first layer slower still.

A reader watching their printer "fly" is mostly seeing the cruise number, not the marketed one. A reader frustrated by "why is my print taking 8 hours when it should take 2" is usually hitting feature-speed reality.

[TENTATIVE 2026-05-08] Specific Bambu cruise / feature speeds vary by model (X1C, P1S, A1) and slicer profile; precise per-printer numbers should be checked against the active Bambu Studio profile rather than a generalized table.

### Cooling as bottleneck

Once vibration and extrusion control are dialed in, the next limit is heat dissipation:

- The just-extruded bead must solidify enough to support the next layer before the next pass arrives. At 300 mm/s with 0.2 mm layers, that's a ~7 ms window per linear cm.
- The part-cooling fan blows ambient air across the freshly extruded line. Fan duty cycle, duct geometry, and ambient temperature all set the cooling rate.
- Symptoms of insufficient cooling: drooping bridges, sagging overhangs above ~45°, blurry corners on small features, "elephant foot" if the bed is hot enough to keep the first few layers molten.

Bambu's part-cooling on X1C / P1S is a single high-RPM fan with a custom duct optimized for the toolhead geometry. The A1 / A1 mini have a similar setup at lower deposition rates.

[TENTATIVE 2026-05-08] Cooling-bandwidth math is a common community heuristic; specific Bambu duct CFM / kelvin-per-second cooling rates are not publicly documented.

### Per-feature speed strategy in slicers

A typical Bambu Studio profile breaks the headline cruise speed into per-feature speeds, roughly:

| Feature | Typical fraction of cruise | Why |
|---|---|---|
| Outer perimeter | 50-60% | Dimensional accuracy + visible surface quality |
| Inner perimeter | 80-100% | Strength matters; surface doesn't |
| Sparse infill | 100-150% | No surface visibility; speed is the only constraint |
| Solid infill (top/bottom) | 80% | Surface visible if last layer |
| Overhang (>45°) | 30-50% | Cooling-limited |
| Bridges | 50% | Cooling + slack-rope dynamics |
| First layer | 30-50% | Adhesion |

[TENTATIVE 2026-05-08] Specific percentages are typical-from-default-profiles, not a Bambu-published spec — readers should check `Print Settings → Speed` in their active profile.

### Where the research is going

The 2025 ETH Zurich / Inspire AG cluster [Sources: 2025-lin-camera-extrusion-optimization.pdf, 2025-hoteit-closed-loop-extrusion-lqr.pdf] extends consumer-grade speed gains by 2× at quality parity — though both papers validate at speeds (≤60 mm/s for Lin's Ender-3 V2; research-grade 5-axis hardware for Hoteit) that are *below* what Bambu cruises at out-of-the-box. Their contribution is **technique generalization**, not absolute-speed records. The open question (which neither paper resolves) is whether their methods extend cleanly to 300+ mm/s regimes where dynamic effects dominate differently.

VLM-based feedback is a parallel research thread starting to apply to high-speed regimes — see [@concepts/vlm-in-manufacturing.md]. None of it ships in consumer firmware as of late 2025.

### Reading-order cross-links

- Up: [@concepts/fdm-printing.md] (the four open problems)
- Component problems: [@concepts/input-shaping.md] (vibration), [@concepts/extrusion-control.md] (flow lag)
- Practical: [@entities/slicers/bambu-studio.md] (per-feature speed UI), [@entities/tools/kickstarter-autodesk-fdm-protocol.md] (high-speed witness features)
- Research adjacent: [@concepts/vlm-in-manufacturing.md] (process-camera control loops)

## Snippets

> "Experiments show reduced width tracking error, mitigated corner defects, and lower surface roughness, achieving surface quality at 3600 mm/min comparable to conventional printing at 1600 mm/min, effectively doubling production speed while maintaining print quality."
[Source: 2025-lin-camera-extrusion-optimization.pdf p.1 (abstract)]
