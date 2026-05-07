---
title: "Bambu Lab Official Filament Comparison Guide + Wiki Material Table"
type: source
tags: [reference, materials, vendor-doc, baseline, bambu]
keywords: [Bambu Lab, filament guide, PLA, PETG, ABS, ASA, PC, PA, TPU, AMS, AMS lite, AMS HT, X1C, P1S, A1, build plate, PEI, hardened steel nozzle, HDT, impact strength, water absorption]
related:
  - concepts/filaments-baseline.md
  - concepts/fdm-printing.md
  - entities/materials/pla.md
  - entities/materials/petg.md
  - entities/materials/abs.md
  - entities/materials/asa.md
  - entities/materials/tpu.md
maturity: validated
created: 2026-05-06
updated: 2026-05-06
read_status: deep-read
---

## Relations

@concepts/filaments-baseline.md @concepts/fdm-printing.md @entities/materials/pla.md @entities/materials/petg.md @entities/materials/abs.md @entities/materials/asa.md @entities/materials/tpu.md

## Raw Concept

- Title: Bambu Lab official filament comparison guide + Bambu Lab Wiki "Filament guide - Printer, Nozzle, AMS, Build Plate, Glue Compatibility and Required Parameters"
- Author: Bambu Lab (vendor)
- Type: vendor reference documentation
- Locations:
  - <https://bambulab.com/en-us/filament/guide> — comparison-table tool with mechanical/thermal data per filament
  - <https://wiki.bambulab.com/en/general/filament-guide-material-table> — printer / nozzle / AMS / build-plate compatibility tables + drying schedules
- Retrieved: 2026-05-06 (via Exa crawl)
- Pages: web pages, multi-table content captured in full
- Read-status: deep-read on retrieved snapshot

This is the **canonical vendor reference** for any Bambu Lab user. Used as the primary source for the materials baseline entity pages (PLA / PETG / ABS / ASA / TPU). Treated as `validated` maturity because it's first-party manufacturer data, but every datapoint is a single-source vendor claim — cross-validation against independent benchmarks (CNC Kitchen, My Tech Fun, Filabase) is on the backlog if a specific claim becomes load-bearing for a reader decision.

## Narrative

The two pages together cover roughly the dataset the reader will actually need before buying any specific filament SKU:

- **Mechanical**: Impact Strength (XY and Z direction, kJ/m²), Bending Strength (MPa), Bending Modulus (MPa). All from Bambu's own ISO-standard test data on their own filaments.
- **Thermal**: Heat Deflection Temperature at 0.45 MPa load (HDT). The number that determines whether a part survives in a hot car or near a window.
- **Hygroscopy**: Saturated Water Absorption Rate at 25°C, 55% relative humidity. The number that determines whether you need a desiccant box.
- **Process**: Nozzle temperature range, recommended print speed, bed temperature, build-plate compatibility (Cool Plate / PLA Plate / Engineering Plate / Smooth PEI / Textured PEI / High-Temperature Plate), part-cooling-fan percentage, glue-stick / liquid-glue requirement.
- **Hardware compatibility**: Whether the filament works on open-frame printers (P1P / A1 / A1 mini) or requires an enclosed printer (X1 / X1C / X1E / P1S). Whether AMS or AMS lite supports it.
- **Drying**: Whether drying is "Optional" or "Required" before use. Drying time and temperature for blast-drying oven, AMS 2 Pro chamber, and AMS HT chamber.
- **Annealing**: Post-printing heat-treatment time and temperature, where applicable.

### Key cross-cutting findings

**Enclosure rule.** PLA / PETG / TPU are open-frame-OK. ABS / ASA / PC / PA / fiber-reinforced engineering filaments need an enclosed printer (X1, X1C, P1S) to suppress warping and ensure interlayer Z-strength. The A1, A1 mini, and unsealed P1P are explicitly **not recommended** for the high-temperature engineering filaments. **This is a hardware constraint, not a tuning constraint** — without a heated chamber, ABS prints crack and warp regardless of bed/nozzle settings.

**AMS rule.** TPU 95A HF and TPU for AMS work on the regular AMS via a dedicated TPU port; TPU 85A and TPU 90A are too soft and **not** AMS-compatible. AMS lite is more restrictive — many materials that work on AMS (PETG-CF, PLA Glow, ABS, PC, PA fillers) are **not recommended** on AMS lite, mainly because AMS lite lacks the AMS's transmission gear that helps push rough/soft filament through. This is an actual purchase-decision input: a reader buying an A1 mini gets AMS lite, restricting their multi-material options.

**Drying rule.** PVA, BVOH, PETG HF, PC, PA, PA-CF/GF, PET-CF/GF, TPU all *require* drying before use. Bambu sells the AMS 2 Pro and AMS HT specifically as drying chambers; alternative is a dedicated blast drying oven (e.g., FilaDry) at 50-140°C for 8-12 hours.

**Hardened-steel-nozzle rule.** Pure (un-filled) PLA / PETG / ABS / ASA / TPU work fine with stainless-steel or brass nozzles. Anything CF or GF reinforced (PLA-CF, PETG-CF, ABS-GF, PA-CF, PAHT-CF, PET-CF, PPA-CF, PPS-CF) requires a hardened steel nozzle — abrasive fibers wear soft nozzles fast (Bambu doesn't publish a half-life but consumer experience suggests <100 print-hours for brass on CF).

**Layer-adhesion gotcha.** Impact Strength Z (interlayer / Z-bonding) is consistently 5-10× lower than Impact Strength XY for non-TPU materials. This is the dominant FDM weakness for any load-bearing part: orient prints so the Z-axis is *not* the load axis whenever possible. PETG HF Z = 7.4 kJ/m² vs XY = 39.3 kJ/m². ABS Z = 4.9 vs XY = 41. The data is real and consistent across all rigid filaments — orientation matters more than material choice for thin parts.

### Single-source caveat

Every number on these pages is from Bambu's own labs, on their own filaments, under their own test conditions. **For relative comparison between Bambu's own filaments this is reliable.** For absolute comparison against third-party brands (Polymaker, Hatchbox, Prusament, Esun, Sunlu) the data is only directional — a "Bambu Basic PLA at 76 MPa bending strength" doesn't predict "Sunlu PLA at X MPa." Independent benchmark databases (Filabase, My Tech Fun, CNC Kitchen) handle the cross-brand comparison; out-of-scope for this baseline reference but accessible via [@concepts/filaments-baseline.md] when a specific claim needs cross-validation.

## Snippets

> "ABS, ASA, PC, PA, and their CF/GF reinforced materials, such as ABS-GF, PC-CF, PA-CF/GF, PA6-CF/GF, PAHT-CF/GF and other filaments need to be printed at higher heatbed temperature and chamber temperature to suppress model warping, shedding and ensure high enough interlayer (Z-bonding) strength, so when using them to print models, especially models with large size and high filling density, it is recommended to use a enclosed printer, such as Bambu X1, X1C, P1S, etc, and it is not recommended to use open-frame printers, such as unsealed Bambu P1P, Bambu A1 mini, Bambu A1, etc."
[Source: https://wiki.bambulab.com/en/general/filament-guide-material-table (retrieved 2026-05-06)]

> "AMS has transmission gear which can work together with the extruder gear to make sure some rough and / or soft filaments can be loaded and unloaded successfully despite the greater resistance, but the AMS lite does not, so some certain kinds of filaments like PLA Glow (Glow-in-the-dark), PETG-CF, PLA LW (low weight), PLA Wood and etc. can be compatible with AMS but may not be compatible with AMS lite."
[Source: https://wiki.bambulab.com/en/general/filament-guide-material-table (retrieved 2026-05-06)]

> "Every kind of filament has a tendency to absorb moisture from the air, resulting in getting damp. During the printing process, this moisture can rapidly vaporize when the filament is heated to high temperatures within the nozzle. As a consequence, the melt filament gets expansion, increased fluidity, and air holes in it. This can result in various issues during printing, such as stringing, lack of material, holes, rough surfaces, and reduced strength."
[Source: https://wiki.bambulab.com/en/general/filament-guide-material-table (retrieved 2026-05-06)]
