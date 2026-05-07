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
updated: 2026-05-08
---

## Relations

@concepts/fdm-printing.md @concepts/high-speed-fdm.md @sources/2025-aung-adaptive-input-shaper.md

## Raw Concept

What's behind Bambu's "Active Tuning" / Klipper's "input shaping" feature. Triggered by the question: when a printer leaves visible ripples next to sharp corners, what's actually happening, what does the calibration print actually tell you, and what's the next research direction firmware will adopt?

## Narrative

### What ringing is, physically

The gantry is a stiff structure with mass — and like any stiff-mass system, it has a **resonant frequency** (typically 30-80 Hz for consumer FDM). When the toolhead changes direction sharply at high acceleration, it kicks the gantry at that frequency and the structure rings: the toolhead position oscillates around the commanded path for ~100 ms after the corner. The hot extruded plastic faithfully traces those oscillations into the part as visible ripples.

The eye-catching name for the artifact is **ringing** or **ghosting** — repeated faint copies of a corner feature, fading as you move away from the originating direction-change.

### What input shaping does

**Input shaping** is a feedforward control technique: convolve the commanded motion profile with a filter (typically a Time Delay Filter — TDF, also called ZV / ZVD shaper) tuned to the gantry's resonant frequency. The filter splits each impulse into two impulses spaced half a resonant period apart — the second impulse cancels the residual oscillation from the first.

- **Cost**: the move takes slightly longer (you delay part of the impulse).
- **Benefit**: no ringing / ghosting on the part. Lets the printer push acceleration / speed limits higher without quality loss.

### Shaper variants

| Shaper | Robustness to frequency error | Latency cost | Notes |
|---|---|---|---|
| **ZV** | Brittle | Lowest | Sharpest cancellation but only at the exact tuned frequency |
| **ZVD** | Better | Slightly higher | Adds a derivative term; tolerates some drift |
| **MZV** | Better still | Slightly higher | Klipper's default for most printers |
| **EI** | Wide tolerance | Higher | Trades some peak cancellation for broad robustness |
| **2HUMP / 3HUMP EI** | Widest | Highest | For printers with multiple resonant modes |

[TENTATIVE 2026-05-08] Variant comparisons are common-knowledge from Klipper / Marlin docs and community testing, not vendor-doc material; specific peak-cancellation numbers vary by hardware.

### How Bambu does it

Bambu's **Active Tuning** (X1C / X1) uses on-toolhead accelerometers to measure the gantry response automatically — no test print required, calibration runs as part of standard print start. P1S / P1P use a similar accelerometer-driven flow but expose less of it to the user. A1 / A1 mini are bed-slingers (the bed moves, not the toolhead) and have qualitatively different resonance dynamics — Y-axis resonance scales with print mass on the bed, so an empty-bed calibration drifts as the print grows. [TENTATIVE 2026-05-08] Bambu's specific algorithm + which printers run mid-print recalibration are not publicly documented; treat as marketing-confirmed but not algorithmically transparent.

### How non-Bambu (Klipper) does it

Klipper's `RESONANCE_TEST` macro requires a USB-attached ADXL345 accelerometer mounted on the toolhead. The macro sweeps frequencies, records response, and outputs recommended `shaper_freq_x` / `shaper_freq_y` values plus a recommended shaper variant. Workflow is: install the accelerometer once → run the test → write the values to `printer.cfg` → remove the accelerometer. **This entire flow is not available on a stock Bambu printer** because Bambu's mainboard doesn't expose the Klipper API surface.

### Reading the ringing test print

Most slicers ship a "ringing tower" test STL: a column with rectangular protrusions printed at progressively increasing acceleration. Look for the acceleration band where ripples first appear next to the protrusion corners — that's your printer's resonance limit at the current shaper setting.

What you're looking at:
- **No ripples up the whole tower** — your shaper is well-tuned (or the tower's max acceleration didn't exceed your gantry's limits).
- **Ripples appear at high band** — shaper is okay but you're pushing past its tuned range; lower max acceleration in the slicer.
- **Ripples on every band** — shaper is detuned (wrong frequency, wrong variant) or off entirely.

### When to re-run input-shaping calibration

- After moving the printer to a different surface / table (resonance shifts with the support stand stiffness)
- After changing the toolhead (switching to a different hotend or adding a part-cooling fan duct)
- After installing a different build plate / bed (changes effective mass on bed-slinger printers)
- If ringing artifacts appear on prints that were previously clean

### Research direction: adaptive input shaping

The catch with fixed-parameter shaping is that the resonant frequency drifts mid-print: as the build mass accumulates on a bed-slinger, as different filaments change the toolhead damping, as the lead screws warm up. Fixed-parameter shaping (what most firmware ships today) detunes.

The research direction is **adaptive input shaping** — estimate the resonance parameters in real time and re-tune the shaper continuously [Source: 2025-aung-adaptive-input-shaper.pdf]. Aung 2025 proposes a Time Delay Filter for second-order systems with unknown natural frequency and damping ratio, validated **in simulation only** (no hardware test). Future-work section flags replacing the hand-derived closed-form parameter estimator with a learned regression model. Reference implementation: https://github.com/NyiNyi-14/A-TDF.git.

[CONFIRMED] Input shaping is implemented in mainstream consumer-printer firmware (Klipper, Marlin, Bambu's "Active Tuning"). [TENTATIVE 2026-05-08] Adaptive shaping is research-grade only as of late 2025 — the published validation is simulation-only. [NEEDS VERIFICATION 2026-05-08] Whether Bambu firmware does any in-flight re-calibration vs once-per-print-start is not publicly documented.

### Reading-order cross-links

- Up: [@concepts/fdm-printing.md] (the four open problems)
- Sibling control problem: [@concepts/extrusion-control.md] (flow, not vibration)
- Speed regime: [@concepts/high-speed-fdm.md] (vibration matters more above ~150 mm/s)

## Snippets

> "We propose an adaptive Time Delay Filter (TDF) input shaper for second-order systems with unknown natural frequency and damping ratio."
[Source: 2025-aung-adaptive-input-shaper.pdf p.1]
