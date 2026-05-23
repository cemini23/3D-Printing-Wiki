---
title: FluxLab — 3D Printable Shape-Changing Devices with Integrated Deformation Sensing (SLA + SMA)
type: source
tags: [paper, TEI, shape-changing, SLA, SMA, inductive-sensing, HCI, prototyping]
keywords: [FluxLab, FluxIO, FluxEditor, FluxShaper, SLA, silicone resin, shape memory alloy, inductive sensing, Formlabs]
related:
  - concepts/shape-changing-fdm-interfaces.md
  - concepts/fdm-printing.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
read_status: read
---

## Relations

@concepts/shape-changing-fdm-interfaces.md @concepts/fdm-printing.md

## Raw Concept

- Title: FluxLab: Creating 3D Printable Shape-Changing Devices with Integrated Deformation Sensing
- Authors: Hsuanling Lee, Jiakun Yu, Shurui Zheng, Te-Yen Wu, Liang He
- Type: TEI '26; arXiv:2512.02911; DOI 10.1145/3731459.3773331; CC BY 4.0
- Location: `raw-sources/2026-lee-fluxlab-sma-sla.pdf`
- Retrieved: 2026-05-23
- Pages: 12
- Read-status: read (pages 1–8 — FluxIO method, tools, fabrication bounds, applications)

## Narrative

**Not an FDM paper.** FluxLab targets **consumer SLA** (Formlabs Form 4B + **Silicone 40A** elastic resin) with **post-print insertion** of a commercial **two-way Nitinol SMA spring** and wire for **dual-role actuation + inductive deformation sensing**.

**FluxIO structure (three layers).** (1) Central SMA channel—spring contracts when heated, acts as coil inductor under bend/compress/twist. (2) **Gyroid TPMS lattice** padding (11–15% solidity printable window; wall 1.0 mm min)—tunable compliance via FluxEditor elasticity slider. (3) **Parallel helix surface wireframe** (1.8 mm struts, 8 mm spacing, 45° slope)—preserves aesthetics, guides deformation; **anchoring** solid patches bias bend direction.

**Tools.** FluxEditor (Rhino 7 / Grasshopper / HumanUI)—converts body segment to FluxIO, previews strain heatmap. FluxShaper—collects inductive signatures, trains ML classifier (Resting / Compression / Extension / Twisting / Bending / combos), exports code snippets. Preload option for reference configurations.

**Fabrication limits (empirical).** Solidity &lt;11% fails print; &gt;15% too rigid for SMA. Cylinders &gt;60 mm diameter show localized actuation only. Twisting recognition weakest class in evaluation.

**Demo applications.** Self-deforming steamer bowl clip (steam heats SMA → grip rim), remote-controlled lab gripper twins (bend one → heat other), kids' dinosaur desk lamp.

**Reader translation.** [CONFIRMED] Requires SLA silicone workflow—**out of scope** for Bambu/Flashforge FDM-only readers on day 1. [TENTATIVE 2026-05-23] Conceptually useful for "integrated sensing + actuation in one printable structure" when evaluating future products; not a toolchain adoption candidate for this wiki's FFF focus.

## Snippets

> "FluxIO leverages a single SMA component to perform both functions—powering shape change and detecting deformation through inductive sensing." [Source: 2026-lee-fluxlab-sma-sla.pdf p.2]

> "models with solidity between 11% and 15% were both printable and capable of supporting SMA-driven deformation." [Source: 2026-lee-fluxlab-sma-sla.pdf p.7]

> "Formlabs Silicone 40A resin … consumer-grade SLA 3D printer (i.e., Form 4B)." [Source: 2026-lee-fluxlab-sma-sla.pdf p.7]
