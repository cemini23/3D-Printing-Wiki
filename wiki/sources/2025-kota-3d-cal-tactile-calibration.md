---
title: 3D Cal — Open-Source Tactile Sensor Calibration via 3D Printer
type: source
tags: [paper, tactile, open-source, FDM, tooling, robotics]
keywords: [3D Cal, DIGIT, GelSight Mini, TouchNet, G-code probing, Northwestern]
related:
  - concepts/soft-robotics-fdm-diw.md
  - concepts/fdm-research-tools.md
  - sources/2025-pattabiraman-eflesh-magnetic-tactile.md
  - sources/2025-morris-slug-mapper-ulfl-mri.md
maturity: draft
created: 2026-06-01
updated: 2026-06-05
read_status: deep-read
---

## Relations

@concepts/soft-robotics-fdm-diw.md @concepts/fdm-research-tools.md @sources/2025-pattabiraman-eflesh-magnetic-tactile.md @sources/2025-morris-slug-mapper-ulfl-mri.md

## Raw Concept

- Authors: Rohan Kota, Kaival Shah, J. Edward Colgate, Gregory Reardon (Northwestern ME)
- arXiv: 2511.03078; NSF NRI-2221571, HAND ERC 2330040
- Location: `raw-sources/2025-kota-3d-cal-tactile-calibration.pdf`
- Software: https://rohankotanu.github.io/3DCal
- Read-status: deep-read (2026-06-05)

## Narrative

**What it is.** **3D Cal** — Python library repurposing a **G-code FDM printer** as a 2-axis automated probe rig for **vision-based tactile sensors**. Workflow: print sensor holder on bed (defines sensor pose in printer coordinates) → mount **2 mm spherical probe** on toolhead → CSV-driven (x,y,z) probe grid → capture labeled images → train **TouchNet** CNN (RGB + xy positional embedding → surface gradients → Poisson-integrated depth maps).

**Hardware [CONFIRMED].** Implementation tested on **Creality Ender 3**; abstraction claims any G-code FDM printer. Built-in support for **DIGIT** and **GelSight Mini** (markerless geometry-focused variants).

**Data collection scale.**

| Sensor | Grid | Probe locations | Capture | Wall time |
|--------|------|-----------------|---------|-----------|
| DIGIT | 0.5 mm spacing | 1,221 | 30 images/indent | ~2 h |
| GelSight Mini | 0.5 mm spacing | 1,209 | 30 images/indent | ~2 h |

**Ablation [CONFIRMED].** High-quality depth on unseen test shapes (hemispheres, pill, pawn) with **~250 distinct spatial locations (~20% of grid)**; losses stabilize near **P=20%** of full grid. Full grid still improves edge regions.

**Benchmark errors (TouchNet, P=80% training).** Type 1 (no-contact) error **<20 µm** both sensors. Type 2 (contact) mean **65–296 µm** DIGIT, **153–290 µm** GelSight Mini — **~5–15% of max indentation depth**; adequate for many manipulation tasks per authors.

**Inference:** TouchNet **<30 ms** on laptop → ~30 fps depth maps.

**Consumer overlap.** Uses printer **as motion stage**, not as part producer — orthogonal to slicer tuning. Pairs with @concepts/fdm-research-tools.md "printer → precision stage" pattern alongside Slug-Mapper. Robotics/advanced hobbyist with DIGIT/GelSight only.

## Snippets

> "3D Cal transforms a low-cost 3D printer into an automated probing device capable of generating large volumes of labeled training data for tactile sensor calibration."
[Source: 2025-kota-3d-cal-tactile-calibration.pdf p.1 abstract]

> "The spatial variation of reconstruction losses stabilized when the models were trained with data captured from approximately 250 distinct spatial locations across the sensor surface (P = 20%)."
[Source: 2025-kota-3d-cal-tactile-calibration.pdf p.7 Discussion]

> "3D Cal is designed to work with any G-Code compatible FDM 3D printer. Our implementation currently supports the Ender 3."
[Source: 2025-kota-3d-cal-tactile-calibration.pdf p.4 §II-A]
