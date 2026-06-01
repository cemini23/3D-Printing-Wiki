---
title: eFlesh — 3D-Printed Magnetic Tactile Sensors
type: source
tags: [paper, robotics, tactile-sensing, FDM, open-source, manipulation]
keywords: [eFlesh, magnetic tactile sensor, Hall effect, cut-cell microstructure, OBJ to STL, hobbyist printer]
related:
  - concepts/open-source-legged-robotics.md
  - concepts/fdm-printing.md
  - entities/materials/tpu.md
  - sources/2025-yoshimura-m3d-skin-tactile-fdm.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
read_status: skimmed
---

## Relations

@concepts/open-source-legged-robotics.md @concepts/fdm-printing.md @entities/materials/tpu.md @sources/2025-yoshimura-m3d-skin-tactile-fdm.md

## Raw Concept

- Title: eFlesh: Highly customizable Magnetic Touch Sensing using Cut-Cell Microstructures
- Authors: Venkatesh Pattabiraman, Zizhou Huang, Daniele Panozzo, Denis Zorin, Lerrel Pinto, Raunaq Bhirangi (NYU)
- Type: arXiv:2506.09994
- Location: `raw-sources/2025-pattabiraman-eflesh-magnetic-tactile.pdf`
- Retrieved: 2026-06-01
- Read-status: skimmed (abstract + Fig. 1 caption)
- Open source: https://e-flesh.com

## Narrative

**Fabrication stack.** Four ingredients: **hobbyist 3D printer**, off-the-shelf **magnets (< $5)**, CAD of target shape, **magnetometer PCB**. Tiled **cut-cell microstructures** tune geometry and mechanical response. Open tool converts **convex OBJ/STL → printable eFlesh STL**.

**Print workflow.** Pause at magnet pouches → insert magnets → resume → slot magnetometer board. Deformation changes magnetic flux read by Hall sensor.

**Reported performance (paper claims).** Contact localization RMSE **0.5 mm**; normal force RMSE **0.27 N**, shear **0.12 N**; slip detection **95%** on unseen objects; visuotactile policies **+40%** vs vision-only on sub-mm tasks.

**Reader fit.** Most accessible **robotics-adjacent FDM project** in this cluster — no full robot required. Still **advanced**: multi-material pause/resume, electronics, calibration. Complements resistive @sources/2025-yoshimura-m3d-skin-tactile-fdm.md (conductive TPU infill). Not day-1 for Flashforge beginners.

## Snippets

> "Building an eFlesh sensor requires only four components: a hobbyist 3D printer, off-the-shelf magnets (< $5), a CAD model of the desired shape, and a magnetometer circuit board." [Source: 2025-pattabiraman-eflesh-magnetic-tactile.pdf p.1]

> "We provide an open-source design tool that converts convex OBJ/STL files into 3D-printable STLs for fabrication." [Source: 2025-pattabiraman-eflesh-magnetic-tactile.pdf p.1]
