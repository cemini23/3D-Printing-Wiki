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
maturity: draft
created: 2026-05-06
updated: 2026-05-07
---

## Relations

@concepts/fdm-printing.md @concepts/high-speed-fdm.md @concepts/vlm-in-manufacturing.md @entities/slicers/orcaslicer.md @entities/tools/kickstarter-autodesk-fdm-protocol.md @sources/2025-lin-camera-extrusion-optimization.md @sources/2025-hoteit-closed-loop-extrusion-lqr.md @sources/2025-margadji-cipher.md

## Raw Concept

Why corners and speed transitions look bad even when positioning is dead-on, and what's the research path to fixing it.

## Narrative

The extruder commands a flow rate, but the filament is a viscoelastic fluid behind a nozzle — it has pressure dynamics. When the toolhead accelerates into a corner, commanded flow drops, but actual flow lags (over-extrusion at the corner exit). When it decelerates back, the reverse (under-extrusion at the start of the next segment).

**Three mitigation classes**, in increasing instrumentation cost:

1. **Pressure / linear advance** (consumer firmware today). Open-loop feedforward — model the extruder's pressure response and pre-compensate the flow command. Tuned per filament. Bambu, Klipper, and Marlin all ship this.
2. **Camera-based G-code optimization.** Print a calibration object, photograph it, back out the per-segment errors, rewrite the G-code [Source: 2025-lin-camera-extrusion-optimization.pdf]. Cheap to deploy — no printer hardware change.
3. **Closed-loop force-controlled printing (FCP).** Add a force sensor to the extruder; close the loop on extrusion force. Adding LQR on top of FCP delivers 39.57% RMS error reduction [Source: 2025-hoteit-closed-loop-extrusion-lqr.pdf p.1]. Research-only — no consumer printer ships a force sensor today [TENTATIVE] [NEEDS VERIFICATION 2026-05-06].

## Snippets

> "The optimized G-code yields print speeds approximately twice the baseline."
[Source: 2025-lin-camera-extrusion-optimization.pdf p.1]

> "39.57% RMS error reduction and 83.7% settling-time reduction over baseline FCP."
[Source: 2025-hoteit-closed-loop-extrusion-lqr.pdf p.1]
