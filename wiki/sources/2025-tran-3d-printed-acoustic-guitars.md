---
title: Production and Manufacturing of 3D Printed Acoustic Guitars
type: source
tags: [paper, FDM, PLA, musical-instrument, maker, thesis]
keywords: [acoustic guitar, PLA, Prusa MK4, Fusion 360, press-fit, Audacity, frequency]
related:
  - concepts/niche-fdm-applications.md
  - entities/materials/pla.md
  - concepts/novice-cad-workflows.md
maturity: draft
created: 2026-06-01
updated: 2026-06-05
read_status: deep-read
---

## Relations

@concepts/niche-fdm-applications.md @entities/materials/pla.md @concepts/novice-cad-workflows.md

## Raw Concept

- Author: Timothy Tran (Binghamton Univ.; advisor William Schiesser)
- Type: undergraduate research report, Aug 2025
- Location: `raw-sources/2025-tran-3d-printed-acoustic-guitars.pdf`
- Read-status: deep-read (2026-06-05)

## Narrative

**Design.** Full-size **classical acoustic guitar** (nylon strings — lower tension than steel) reverse-engineered from a measured instrument in **Fusion 360**. Modular sections sized for **Prusa MK4** bed (**10 × 9.5 in**). Reference inspiration includes 3D-printed acoustic instruments (e.g. LeFiddler violin) and Prusa **Prusacaster** electric guitar blog — this project is **acoustic classical**, not electric.

**Assembly [CONFIRMED].** **Press-fit** tolerances (**0.006 in** typical body joints; **0.01 in** clearance on reinforcement-to-front-plate); **cyanoacrylate** on top plate; nylon strings + generic classical tuners. Bottom plate press-fit throughout.

**Build issues observed.**

- **Fretboard joint bump** muted strings until sanded flat.
- **Tuning-head cracks** developed over time (summer heat + string tension) — PLA creep/fatigue under sustained load.
- Strings tuned without immediate visible damage, but long-term structural flex at tuner mount is a weakness.

**Tonal testing (Audacity FFT peaks vs open-string standards).**

| String | Target note (Hz) | Measured peak (Hz) | Assessment |
|--------|------------------|--------------------|------------|
| 1 | E4 (329.63) | 325 @ E4 | ~4 Hz low [CONFIRMED] |
| 2 | B3 (246.94) | 243 @ B3 | ~4 Hz low |
| 3 | G3 (196.00) | 193 @ G3 | ~3 Hz low |
| 4 | D3 (146.83) | **289 @ D4** | Correct pitch class, **~2× frequency** |
| 5 | A2 (110.00) | **214 @ A3** | ~2× frequency |
| 6 | E2 (82.41) | **164 @ E3** | ~2× frequency |

**Interpretation [TENTATIVE].** Treble strings (1–3) average **~3 Hz** deviation — author calls tuning "very similar." Bass strings (4–6) show **octave-higher partial dominance** in FFT (PLA body acoustics or string product — author lists both). Author still claims **subjective tonality** matches traditional guitar after tuning.

**Reader fit.** Ambitious **multi-day PLA project** after calibration — large bed segmentation, tolerance tuning, assembly QA. Not a beginner week-1 print. Alternative materials suggested for better spectral match. Useful cautionary tale for **large PLA structures under continuous mechanical load**.

## Snippets

> "The first, second, and third strings were very similar to the projected standard, with an average deviation of nearly three hertz. However, looking at the fourth, fifth, and sixth strings, frequencies were almost doubled for each of them."
[Source: 2025-tran-3d-printed-acoustic-guitars.pdf p.25]

> "The guitar body was divided into multiple sections joined with press-fit tolerances and minimal cyanoacrylate adhesive."
[Source: 2025-tran-3d-printed-acoustic-guitars.pdf p.2]

> "The Prusa Mark 4 printer's build plate dimensions of 10 × 9.5 inches require a division of the guitar into modular sections."
[Source: 2025-tran-3d-printed-acoustic-guitars.pdf p.12]
