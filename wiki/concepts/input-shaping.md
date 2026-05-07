---
title: Input Shaping (Vibration Suppression)
type: concept
tags: [control, vibration, feedforward]
keywords: [time delay filter, ZV shaper, ZVD shaper, recursive least squares, ringing, ghosting]
related:
  - concepts/fdm-printing.md
  - concepts/high-speed-fdm.md
  - sources/2025-aung-adaptive-input-shaper.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

@concepts/fdm-printing.md @concepts/high-speed-fdm.md @sources/2025-aung-adaptive-input-shaper.md

## Raw Concept

What's behind Bambu's "Active Tuning" / Klipper's "input shaping" feature. Triggered by the question: when a printer leaves visible ripples next to sharp corners, what's actually happening, and what's the next research direction firmware will adopt?

## Narrative

**Input shaping** is a feedforward control technique: convolve the commanded motion profile with a filter (typically a Time Delay Filter — TDF, also called ZV / ZVD shaper) tuned to the resonant frequency of the gantry. The result cancels the gantry's residual oscillation when the toolhead changes direction sharply.

- **Cost**: the move takes slightly longer (you delay part of the impulse).
- **Benefit**: no ringing / ghosting on the part.

The catch is that the resonant frequency depends on the gantry's effective mass and stiffness, which drift mid-print as the build accumulates and as different toolheads / spools change the dynamic load. Fixed-parameter shaping (what most firmware ships today) detunes. The research direction is **adaptive input shaping** — estimate the parameters in real time and re-tune the shaper [Source: 2025-aung-adaptive-input-shaper.pdf].

[CONFIRMED] Input shaping is implemented in mainstream consumer-printer firmware (Klipper, Marlin, Bambu's "Active Tuning"). [TENTATIVE] Adaptive shaping is research-grade only as of late 2025 — the Aung 2025 reference paper validates only in simulation (no hardware test) and its future-work section flags replacing the hand-derived closed-form parameter estimator with a learned regression model. Reference implementation: https://github.com/NyiNyi-14/A-TDF.git [Source: 2025-aung-adaptive-input-shaper.pdf p.1] [NEEDS VERIFICATION 2026-05-06].

## Snippets

> "We propose an adaptive Time Delay Filter (TDF) input shaper for second-order systems with unknown natural frequency and damping ratio."
[Source: 2025-aung-adaptive-input-shaper.pdf p.1]
