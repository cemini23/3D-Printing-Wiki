---
title: Kickstarter / Autodesk FDM Test V4 Protocol
type: entity
tags: [calibration, benchmark, witness-features, FDM, Apache-2.0, GO-tier, materials-research]
keywords: [Kickstarter Autodesk 3D, FDM test, witness features, calibration test print, benchmark, ksr_fdmtest_v4.stl, materials research, deterministic baseline]
related:
  - concepts/fdm-printing.md
  - concepts/extrusion-control.md
  - concepts/filaments-baseline.md
  - sources/2026-bambu-toolchain-audit.md
maturity: draft
created: 2026-05-07
updated: 2026-05-07
---

## Relations

@concepts/fdm-printing.md @concepts/extrusion-control.md @concepts/filaments-baseline.md @sources/2026-bambu-toolchain-audit.md

## Raw Concept

A standardized FDM calibration test print designed to fail in known ways — generating discrete "witness features" that surface specific extruder, motion-system, and bridging failures. Apache-2.0; 8 years stale but the staleness doesn't matter (it's a static `.stl` + `.f3d` design, not executable software). Phase-0 verdict: **GO** — control asset for repeatable baseline material profiles [Source: 2026-bambu-toolchain-audit.docx (GO-Tier Repositories)].

## Narrative

### What it is

A 2018-vintage collaboration between Kickstarter and Autodesk that produced the **FDM Test V4** standardized calibration print. The repo (`github.com/kickstarter/kickstarter-autodesk-3d`) contains:

- `FDM-protocol/ksr_fdmtest_v4.stl` — the canonical test geometry
- `.f3d` Fusion 360 source files
- Detailed documentation of what each "witness feature" tests

The geometry is engineered to **stress the printer to the point of failure** — overhangs, bridging, fine details, sharp corners, dimensional-accuracy features — all in a single non-self-interfering print. When the print fails (and it's designed to fail), the failure mode pinpoints which subsystem is the bottleneck:

- Bridging failure → cooling or first-layer adhesion issue
- Overhang collapse → cooling fan / part-cooling tuning
- Fine-feature loss → nozzle-flow or pressure-advance issue
- Dimensional drift → motion-system calibration / stepper backlash
- Surface artifacts → flow-rate / acceleration tuning

### Why GO-tier despite 8 years stale

The audit's argument: **staleness doesn't matter for a geometry-only repo.** It's not executable software — it's a static `.stl` design. Modern slicers (Bambu Studio, OrcaSlicer, PrusaSlicer, Cura) all import it identically. The Apache-2.0 license is permissive and uncontroversial. There's no security surface, no runtime, no API to deprecate.

The only minor caveat: the print's calibration thresholds were defined for 2018-era hardware. Modern high-speed CoreXY machines (Bambu X1C / P1S at 500+ mm/s, properly tuned Voron/RatRig) may **clear all the test features without breaking a sweat** — meaning the test bottoms out as "everything works." That's a reasonable failure mode (ceiling > capability), not a usability problem.

### How to use it on a Bambu

Workflow for characterizing a new filament:

1. Slice `ksr_fdmtest_v4.stl` in Bambu Studio with the filament's default profile
2. Print on the actual Bambu printer
3. Inspect the witness features against the documented expected behavior
4. For any feature that fails: tune the relevant slicer parameter (cooling fan, retract, K-value, speed) and reprint
5. Once the test passes: document the tuned profile as the canonical baseline for that filament

This produces a **repeatable, deterministic baseline** — every filament in the friend's inventory gets characterized via the same standardized print. Cross-filament comparison becomes possible.

### Cross-link to filament baseline cluster

The FDM Test V4 protocol is the practical companion to [@concepts/filaments-baseline.md] — the materials baseline gives the *expected* mechanical / thermal / process specs from Bambu's vendor data, and FDM Test V4 lets the friend *verify* the actual printer-on-this-filament behavior matches the spec.

For a friend running an Etsy print farm with multiple filament brands, this is the standardized characterization protocol that prevents per-filament tuning drift.

[CONFIRMED] FDM Test V4 is a static, universally-compatible calibration geometry. [CONFIRMED] Apache-2.0; no licensing concerns. [TENTATIVE] Some features may be too easy for modern fast Bambu hardware to fail at — limits the diagnostic value at the high end of the printer's capability.

## Snippets

> "Although the repository has remained unmaintained for years, it represents a feature-complete, standardized benchmarking protocol rather than an evolving executable binary. Adopting this repository provides the local knowledge hub with a rigorous, deterministic geometric standard for evaluating the thermal and rheological limits of experimental filaments during materials research."
[Source: 2026-bambu-toolchain-audit.docx (GO-Tier — Kickstarter Autodesk reasoning)]

> "The geometry stresses the printer's system to the point of failure. These failures generate 'witness features' that allow users to evaluate the performance of the slicer, the extruder, and the motion system."
[Source: github.com/kickstarter/kickstarter-autodesk-3d README, retrieved 2026-05-07 via 2026-bambu-toolchain-audit.docx]
