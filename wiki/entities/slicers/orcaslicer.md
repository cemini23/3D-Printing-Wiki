---
title: OrcaSlicer
type: entity
tags: [slicer, AGPL-3.0, conditional-go-tier, calibration, advanced-tuning, bambu-studio-fork]
keywords: [OrcaSlicer, slicer, calibration, K-value, pressure advance, flow dynamics, material tuning, Bambu Studio fork, profile schema divergence]
related:
  - concepts/fdm-printing.md
  - concepts/bambu-ecosystem-closed-loop.md
  - concepts/extrusion-control.md
  - sources/2026-bambu-toolchain-audit.md
  - entities/slicers/bambu-studio.md
maturity: draft
created: 2026-05-07
updated: 2026-05-07
---

## Relations

@concepts/fdm-printing.md @concepts/bambu-ecosystem-closed-loop.md @concepts/extrusion-control.md @sources/2026-bambu-toolchain-audit.md @entities/slicers/bambu-studio.md

## Raw Concept

Community fork of Bambu Studio with deeper parametric controls (extended K-values, advanced flow tuning, built-in calibration test suite). AGPL-3.0. Phase-0 verdict: **CONDITIONAL-GO** — adopt for advanced material calibration only, not daily production [Source: 2026-bambu-toolchain-audit.docx (CONDITIONAL-GO-Tier Repositories)].

## Narrative

### What it is

OrcaSlicer is an enthusiast-driven AGPL-3.0 fork of Bambu Studio (which is itself a fork of PrusaSlicer). The fork chain: PrusaSlicer → Bambu Studio → OrcaSlicer.

OrcaSlicer's value-add over Bambu Studio:

- **Wider printer support** — slices for Bambu, Prusa, Voron, VzBoT, RatRig, Creality, generic CoreXY/Cartesian. (Bambu Studio is Bambu-only.)
- **Built-in calibration test print suite** — temperature tower / flow / pressure-advance / retract / tolerance / Volumetric Speed tests as one-click presets, with detailed step-by-step interpretation guides
- **Extended K-value range** — pressure advance K values can be tuned beyond the range Bambu Studio caps at
- **More-granular flow dynamics** — extra tuning hooks for extrusion-rate-vs-speed compensation, viscosity-aware ramping, advanced retract behaviors

### Why CONDITIONAL-GO (not GO)

The audit's argument: OrcaSlicer **does not lose** the Bambu integration (it inherits it from the Bambu Studio fork base), but **introduces profile schema divergence**. Profiles tuned in OrcaSlicer use parameter names and ranges that don't cleanly back-port into Bambu Studio's preset slots. If the reader uses both slicers daily, configuration drifts: the same filament has slightly different settings in each app, and the reader ends up not sure which is "canonical."

The CONDITIONAL: **isolate OrcaSlicer to advanced calibration only.** Use it when characterizing a new filament, troubleshooting an extrusion issue, or running a calibration test — then port the resulting tuned values back into Bambu Studio for daily production. Daily production stays in Bambu Studio.

### When to use OrcaSlicer

- Running the built-in calibration test suite on a new filament (temp tower / flow / PA tower)
- Diagnosing an extrusion problem that Bambu Studio's UI doesn't expose enough knobs for (corner blob / under-extrusion at speed transitions)
- Tuning K-values, retract distance/speed, or flow ratio on a non-Bambu filament that needs values outside Bambu Studio's defaults
- Slicing for a non-Bambu printer (if reader ever picks up a secondary Prusa / Voron / Creality)

### When NOT to use OrcaSlicer

- Daily production slicing of Etsy / MakerWorld store items — stay in Bambu Studio
- AMS multi-material work — Bambu Studio's AMS handling is more refined
- MakerWorld publishing — Bambu Studio has the direct upload integration

### Reported issues [TENTATIVE 2026-05-07 — sourced from audit's GitHub-issues + Reddit citations]

The audit cites recent OrcaSlicer instability:

- **Broken flow calibration in OrcaSlicer 2.3.1** [TENTATIVE — community-reported; specific commit / fix-version not given]
- **Arbitrary K-value caps** that don't match the documented range [TENTATIVE — Reddit + GitHub issue tracker references]
- General community sentiment: "buggy as hell" (per a Reddit thread cited in the audit)

The OrcaSlicer GitHub tracker has a regression-tracking issue (#12684 "Tracking issue: Regressions in OrcaSlicer 2.3.2 Release") confirming that recent versions have known regressions. Pin a known-stable version rather than auto-updating.

### Profile schema divergence — concrete consequence

If the reader tunes a Polymaker PETG profile in OrcaSlicer (say, K=0.045, retract 1.4mm, flow 0.96) and tries to copy those into Bambu Studio:

- **K value** transfers as-is (same parameter name)
- **Retract distance** transfers as-is
- **Flow ratio** transfers as-is
- **But**: cooling profile, layer speed ramps, perimeter ordering, and corner-acceleration tuning may have different parameter names or scaling — silent drift can cause the same physical filament to print differently in each slicer

Workflow recommendation: **calibrate in OrcaSlicer, *write down* the tuned values, then re-create the profile in Bambu Studio** — don't try to copy the entire profile. Treat OrcaSlicer's role as a tuning instrument, not a profile source-of-truth.

[CONFIRMED] OrcaSlicer's calibration test suite + extended tuning range is genuinely useful for material characterization. [CONFIRMED] Profile schema divergence is a real risk if used as daily driver alongside Bambu Studio. [TENTATIVE] Specific version-pin claims for bugs (2.3.1 / 2.3.2) need verification against current OrcaSlicer release notes.

## Snippets

> "OrcaSlicer represents an enthusiast-driven, AGPL-3.0 licensed fork of Bambu Studio designed to expose deep, granular calibration mechanisms that are obscured in the native software. Its core strength is its unparalleled suite of built-in calibration geometries and unlocked firmware parameters, making it an indispensable tool for characterizing experimental polymer filaments."
[Source: 2026-bambu-toolchain-audit.docx (CONDITIONAL-GO — OrcaSlicer reasoning)]

> "G-code generator for 3D printers (Bambu, Prusa, Voron, VzBot, RatRig, Creality, etc.)"
[Source: github.com/OrcaSlicer/OrcaSlicer README description, retrieved 2026-05-07 via 2026-bambu-toolchain-audit.docx]
