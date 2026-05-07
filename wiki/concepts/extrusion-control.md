---
title: Extrusion Control
type: concept
tags: [control, extrusion, feedforward, closed-loop]
keywords: [pressure advance, linear advance, force-controlled printing, FCP, LQR, G-code optimization, flow rate]
related:
  - concepts/fdm-printing.md
  - concepts/high-speed-fdm.md
  - concepts/vlm-in-manufacturing.md
  - entities/slicers/orcaslicer.md
  - entities/tools/kickstarter-autodesk-fdm-protocol.md
  - sources/2025-lin-camera-extrusion-optimization.md
  - sources/2025-hoteit-closed-loop-extrusion-lqr.md
  - sources/2025-margadji-cipher.md
  - entities/printers/x1c.md
  - entities/printers/p1s.md
  - entities/printers/a1.md
maturity: draft
created: 2026-05-06
updated: 2026-05-08
---

## Relations

@concepts/fdm-printing.md @concepts/high-speed-fdm.md @concepts/vlm-in-manufacturing.md @entities/slicers/orcaslicer.md @entities/tools/kickstarter-autodesk-fdm-protocol.md @sources/2025-lin-camera-extrusion-optimization.md @sources/2025-hoteit-closed-loop-extrusion-lqr.md @sources/2025-margadji-cipher.md @entities/printers/x1c.md @entities/printers/p1s.md @entities/printers/a1.md

## Raw Concept

Why corners and speed transitions look bad even when positioning is dead-on, what the dial is called on a consumer Bambu, how to tune it, and where the research is going next.

## Narrative

### What's actually wrong

The extruder commands a flow rate, but the filament is a viscoelastic fluid behind a nozzle — it has **pressure dynamics**. The melt zone in the hotend acts like a spring-damper between the gear-driven push and the molten output. When the toolhead accelerates into a corner, commanded flow drops, but actual flow lags (over-extrusion at the corner exit, leaving a glossy bulge). When it decelerates back to cruise, the reverse — under-extrusion at the start of the next segment, leaving a thin/transparent line.

This isn't a positioning problem. The motor moved exactly where the G-code told it. The filament didn't agree.

### What you'll see on a print

Symptoms a reader can identify visually before reaching for tooling:

- **Glossy blobs at outer-perimeter corners** — over-extrusion on the deceleration side
- **Gaps or thin spots at travel-move starts** — pressure drained during the travel; first millimeter is starved
- **Seam blobs (Z-seam)** — extruder pressure didn't fully unload at the seam end-point
- **Corner shadowing on outer walls** — chronic mistuning of the pressure-response model

Print [@entities/tools/kickstarter-autodesk-fdm-protocol.md] and inspect the corner / pressure-advance witness features; the symptoms map to specific subsystem issues.

### What the dial is called

Same control idea, three names depending on firmware:

| Firmware | Parameter | Range (PLA, 0.4 nozzle) |
|---|---|---|
| Bambu Studio | **K value** (pressure advance) | ~0.02 to ~0.05 |
| Klipper | `pressure_advance` | ~0.02 to ~0.10 |
| Marlin | `linear_advance` | ~0.02 to ~0.20 (different units) |

Bambu auto-calibrates K-value per filament for first-party Bambu filaments and exposes a manual K-cal print for third-party rolls. OrcaSlicer's calibration suite [@entities/slicers/orcaslicer.md] is the more thorough manual workflow when chasing a stubborn filament.

[TENTATIVE 2026-05-08] Specific K-value ranges are typical-from-community reports, not Bambu vendor docs. Per-filament drift is real — high-flow PLA, silk PLA, glow-in-the-dark PLA, and PETG variants all want different K. Re-tune when changing brand or color, even within the same chemistry.

### Three mitigation classes (research direction)

In increasing instrumentation cost:

1. **Pressure / linear advance** (what consumer firmware ships today). Open-loop feedforward — model the extruder's pressure response and pre-compensate the flow command. Tuned per filament. Bambu, Klipper, and Marlin all ship this. The model itself is simple (typically first-order); per-filament tuning is the work.
2. **Camera-based G-code optimization.** Print a calibration object, photograph it, back out the per-segment errors offline, rewrite the G-code [Source: 2025-lin-camera-extrusion-optimization.pdf]. Cheap to deploy — no printer hardware change. The Lin 2025 ETH Zurich result demonstrates ~2× speed gain on an Ender-3 V2 at quality parity (1600 → 3600 mm/min). [TENTATIVE 2026-05-08] Generalization to Bambu-tier hardware not directly tested in the paper — Bambu cruises 5-10× faster than the Ender, where dynamics may dominate differently.
3. **Closed-loop force-controlled printing (FCP).** Add a force sensor to the extruder; close the loop on extrusion force itself rather than commanded flow. Adding LQR on top of FCP delivers 39.57% RMS error reduction and 83.7% settling-time reduction [Source: 2025-hoteit-closed-loop-extrusion-lqr.pdf p.1]. Research-only — no consumer printer ships a force sensor today. [TENTATIVE 2026-05-08] Hoteit's hardware is research-grade (5-axis, ROS2/Duet/Kalman); consumer translation is not direct.

A fourth direction is starting to appear: **VLM-driven flow regression**. Margadji+Pattinson 2025 (Cambridge CIPHER) uses an endoscope camera + Llama-3.2 + ResNet-152 to regress flow rate from process-camera images at 5× MAE reduction over baselines [Source: 2025-margadji-cipher.pdf]. See [@concepts/vlm-in-manufacturing.md].

### Where Bambu sits

Bambu ships #1 (productized as auto-K-cal + manual K-cal print) and *part of* #3 (the lidar inspection on first layer is closed-loop on layer height, not on extrusion force directly). #2 and #3-extrusion-force-direct are research-only. The reader's day-1 dial is the K-value calibration print — run it whenever switching to a non-Bambu filament.

### Reading-order cross-links

- Up: [@concepts/fdm-printing.md] (the four open problems)
- Sibling control problem: [@concepts/input-shaping.md] (vibration, not extrusion)
- Speed regime: [@concepts/high-speed-fdm.md] (extrusion control matters more above ~150 mm/s)
- Practical: [@entities/tools/kickstarter-autodesk-fdm-protocol.md] (calibration print)
- Research adjacent: [@concepts/vlm-in-manufacturing.md] (CIPHER VLA process expert)

## Snippets

> "The optimized G-code yields print speeds approximately twice the baseline."
[Source: 2025-lin-camera-extrusion-optimization.pdf p.1]

> "39.57% RMS error reduction and 83.7% settling-time reduction over baseline FCP."
[Source: 2025-hoteit-closed-loop-extrusion-lqr.pdf p.1]
