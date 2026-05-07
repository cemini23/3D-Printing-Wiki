---
title: Closed Loop Reference Optimization for Extrusion Additive Manufacturing
type: source
tags: [paper, control, extrusion, LQR, closed-loop]
keywords: [LQR, force-controlled printing, FCP, ETH Zurich, Inspire AG, RMS error, settling time, Kalman filter, ROS2, N4SID, reference governor]
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

- Title: Closed Loop Reference Optimization for Extrusion Additive Manufacturing
- Authors: Layth Hoteit, Andrea Balestra, Christian Mingard, Efe C. Balta, John Lygeros (ETH Zurich, Inspire AG)
- Type: Conference paper / preprint
- Location: `raw-sources/2025-hoteit-closed-loop-extrusion-lqr.pdf`
- Retrieved: 2026-05-06
- Pages: 6
- Read-status: deep-read

## Narrative

Adds a Linear-Quadratic Regulator (LQR) plus an offline reference governor (QP) on top of Force-Controlled Printing (FCP) — building on Guidetti et al. 2024's FCP scheme, which adds a force sensor on the extruder. The reference governor pre-shapes the force trajectory; the LQR closes the loop on the force-tracking error.

System identification: 3rd-order linear state-space model fitted via N4SID. LQR weights Q = diag(1656.2, 8.9, 1.6), R = 0.00995, yielding gain K_LQR = [323.8591, −113.4687, 23.2255]. State estimation by Kalman filter.

Hardware: 5-axis gantry running planar test prints, Duet motion board, ROS2 supervisory layer. **Research-grade — not consumer hardware.** Validation: simulation reports 69.81% RMSE reduction vs. baseline FCP; physical experiment reports 39.57% RMSE reduction and 83.7% shorter settling time. The simulation-vs-experiment gap (69.81% → 39.57%) is itself informative — it implies unmodeled dynamics dominate the closed-loop performance ceiling on real hardware.

**Practical bearing**: quantifies the size of the gap closed-loop extrusion control can close — about 40% of remaining force-tracking error on a single-axis task. **Not transferable to a Bambu-class consumer printer** without a force sensor on the extruder (added parts cost + a second servo loop). Useful as upper-bound calibration for what open-loop firmware leaves on the table.

## Snippets

> "We propose a closed-loop reference optimization scheme for extrusion additive manufacturing based on Linear Quadratic Regulator (LQR) control over Force-Controlled Printing (FCP). The method achieves 39.57% RMS error reduction and 83.7% settling-time reduction over baseline FCP."
[Source: 2025-hoteit-closed-loop-extrusion-lqr.pdf p.1]
