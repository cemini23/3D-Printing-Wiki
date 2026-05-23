---
title: Single-Material 4D-Printed Shape Morphing via Spatially Patterned Strain Trapping (PvP)
type: source
tags: [paper, 4D-printing, FDM, FFF, SMP, strain-trapping, metamaterial]
keywords: [Programming via Printing, PvP, shape memory polymer, MM3520, trapped strain, desktop FFF, Syracuse]
related:
  - concepts/shape-changing-fdm-interfaces.md
  - concepts/fdm-printing.md
  - entities/materials/pla.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
read_status: read
---

## Relations

@concepts/shape-changing-fdm-interfaces.md @concepts/fdm-printing.md @entities/materials/pla.md

## Raw Concept

- Title: Single-material 4D-printed shape-morphing structures via spatially patterned strain trapping
- Authors: S M Asif Iqbal, Hang Zhang, Lin Yang, Aoyi Luo, Joseph D. Paulsen, James H. Henderson (Syracuse University; ETH Zurich D-ARCH)
- Type: Research article (journal preprint PDF in inbox; no arXiv ID extracted from first pages)
- Location: `raw-sources/2025-iqbal-single-material-4d-pvp.pdf`
- Retrieved: 2026-05-23
- Pages: 30
- Read-status: read (pages 1–8 — PvP parameter study + contractile beam optimization; lattice unit cells introduced)

## Narrative

Extends **Programming via Printing (PvP)** on **desktop FFF**: tensile strain is trapped in extruded SMP fibers during deposition and fixed by vitrification—**no secondary mechanical programming step**. This paper pushes three claims: **~50% trapped strain** with commercial SMP, **spatial patterning** of strain within one print, and **expansion modes** via architected lattices that convert strut contraction into unit-cell / global expansion.

**Material & printer.** Commercial SMP filament **MM3520**; inexpensive hobbyist FFF printer (off-the-shelf per authors). Parameter sweep: nozzle **195–235 °C** (20 °C steps), speed **10–60 mm/s**. Recovery bath **70 °C** (Tg+35) for 30 min.

**Key process results (narrow strips, then thicker beams).**

| Finding | Detail |
|---------|--------|
| Max trapped strain | **48.7%** (195 °C, 60 mm/s) on thin strips; **~50–60%** on optimized 3.2 mm thick beams with negligible bending |
| Temperature vs speed | Lower nozzle temp dominates; speed effect plateaus ≥30 mm/s at 195/235 °C |
| Bending artifact | Faster print / thinner strips → unwanted curvature from layer reheating; mitigated by thicker (3.2 mm) beams |
| Speed ceiling | &gt;30 mm/s risks layer adhesion on TPU-based 4D per manufacturer guidance [cited in paper] |

**Expansion strategy.** PvP alone gives **contraction**; **uniaxial/biaxial expansion** requires lattice unit cells whose geometry maps strut shrink → cell expansion (analytical + experimental validation; larger proof-of-concept structures in later sections).

**Reader translation (consumer FFF).** [CONFIRMED] Most accessible cluster paper for **hobby FDM** readers—if you buy SMP filament and tune G-code/nozzle temp, you can prototype morphing structures without molds or pneumatics. [TENTATIVE 2026-05-23] Validated on generic hobbyist hardware, not Bambu X1C or Flashforge 5M specifically; SMP MM3520 ≠ everyday PLA/PETG inventory. Treat as **experimental maker niche** (soft robotics, deployable structures), not a slicer preset.

## Snippets

> "Large (up to 50%) and spatially controlled trapped tensile strain programming is achieved by PvP model design, geometric coding, and printing parameter optimization." [Source: 2025-iqbal-single-material-4d-pvp.pdf p.1]

> "The highest trapped strain of 48.7% was observed at the lowest printing temperature and highest printing speed tested (195°C and 60 mm/s)." [Source: 2025-iqbal-single-material-4d-pvp.pdf p.5]

> "Overall, we were able to achieve up to approximately 50% trapped strain while maintaining good print quality and minimal self-bending." [Source: 2025-iqbal-single-material-4d-pvp.pdf p.6]
