---
title: PETG (Polyethylene Terephthalate Glycol-modified)
type: entity
tags: [material, filament, FDM, baseline, functional]
keywords: [PETG, PETG HF, PETG Translucent, PETG-CF, polyethylene terephthalate, glycol-modified, functional, hygroscopic]
related:
  - concepts/filaments-baseline.md
  - concepts/fdm-printing.md
  - sources/2026-bambu-filament-guide.md
  - sources/2026-mahjourian-vlm-iris.md
  - entities/materials/pla.md
  - entities/materials/abs.md
  - entities/materials/asa.md
  - entities/materials/tpu.md
maturity: draft
created: 2026-05-06
updated: 2026-05-07
---

## Relations

@concepts/filaments-baseline.md @concepts/fdm-printing.md @sources/2026-bambu-filament-guide.md @sources/2026-mahjourian-vlm-iris.md @entities/materials/pla.md @entities/materials/abs.md @entities/materials/asa.md @entities/materials/tpu.md

## Raw Concept

The functional default. **PETG (polyethylene terephthalate glycol-modified)** sits between PLA and ABS — easier to print than ABS (no enclosure required), tougher than PLA, higher-temperature tolerant. The right choice for any part that needs to *do something* (mounts, organizers, brackets, tool handles, lamp shades) rather than just *look like something*.

## Narrative

### The pitch

PETG inherits the chemistry of the plastic that water bottles and food containers are made of (PET), modified with glycol to lower the print temperature and avoid crystallization on cooling. **Practical translation:** PETG is the closest a hobbyist gets to "PLA's printability with ABS's properties." Strong layer adhesion, modest heat resistance, doesn't shatter on impact. Prints fine on the open-frame Bambu A1 / A1 mini — no enclosure needed.

Prusa Research famously prints the orange plastic parts of their own MK4 / MK4S printers in PETG. If a self-replicating 3D printer's structural parts can be PETG, the friend's Etsy mount product probably can be too.

### When PETG is the right choice

- **Functional parts on an A1 / A1 mini.** Open-frame printer + need higher-than-PLA strength = PETG. ABS would warp; PETG won't.
- **Lamp / lighting shades.** PETG Translucent is specifically marketed for diffused-light fixtures and is genuinely good at it.
- **Outdoor parts that don't see direct UV.** PETG handles temperature swings without warping; UV degradation is slower than PLA but still happens — for direct sun exposure, prefer ASA.
- **Watertight or near-watertight prints.** PETG layer adhesion is solid; small parts can be printed close to watertight, especially with extra perimeters and overlapping infill.
- **Replacement for "ABS without an enclosure."** Most jobs that historically meant ABS now go to PETG by default among hobbyists with open-frame printers.

### When PETG is the wrong choice

- **Stringing-sensitive jobs.** PETG is the worst rigid filament for stringing. Long retract distance, slower travel, well-tuned temperature, dry filament — all required to get clean prints. PLA is much more forgiving on the stringing front.
- **Hot-car parts.** HDT 69°C (PETG) / 87°C (PETG HF). Sustained 90°C+ environments need ABS / ASA / PC.
- **Aesthetic-first prints with lots of overhangs.** PETG's surface finish is glossier than PLA Matte but worse on overhangs because of the higher viscosity and poorer cooling-driven freeze.
- **AMS multi-color with PETG support.** Important caveat: **PVA is not compatible as support filament for PETG.** [Source: https://wiki.bambulab.com/en/filament/support (retrieved 2026-05-06)] Bambu's "Support for PLA/PETG" is the right pairing.

### Specs (Bambu PETG vs PETG HF) [Source: https://bambulab.com/en-us/filament/guide (retrieved 2026-05-06)]

| Property | **PETG** | **PETG HF** |
|---|---|---|
| Impact strength XY / Z (kJ/m²) | 31.5 / 10.6 | 39.3 / 7.4 |
| Bending strength XY (MPa) | 64 | 62 |
| Bending modulus XY (MPa) | 2050 | 1880 |
| HDT @ 0.45 MPa (°C) | 69 | 87 |
| Saturated water absorption | 0.40% | 0.65% |
| Nozzle temperature | 230-260°C | 230-260°C |
| Bed temperature (PEI) | 60-80°C | 60-80°C |
| Print speed | <300 mm/s | <300 mm/s |
| Part cooling fan | 0-80% | 0-80% |
| Drying before use | Optional (65°C 8h) | **Required** (65°C 8h) |
| Enclosure | Not required (recommended for low-ambient) | Same |
| AMS / AMS lite | Both compatible | Both compatible |
| Nozzle material | Any | Any |

**PETG HF** ("High Flow") is Bambu's faster-printing PETG variant — same chemistry, tuned rheology for higher throughput. The notable trade-off: **HDT jumps from 69°C to 87°C** (good), but **drying becomes required** (HF absorbs more moisture) and **layer adhesion in Z drops from 10.6 to 7.4 kJ/m²** (worse). For load-bearing parts oriented with stress in Z, regular PETG is the safer pick.

### Variants

| Variant | Difference | When to pick it |
|---|---|---|
| **PETG Basic** | The reference | Default functional filament |
| **PETG HF** | Higher flow, higher HDT, requires drying | Speed-prioritized prints; HDT-critical parts |
| **PETG Translucent** | Light-diffusing | Lamp shades, light covers |
| **PETG-CF** | Carbon-fiber reinforced | Stiff structural parts; hardened nozzle required; AMS lite **not recommended** |

### Workflow gotchas

1. **Bed adhesion.** PETG sticks *too well* to bare PEI — without glue the part can rip out a chunk of plate coating. **Use a glue stick or Bambu Liquid Glue every print.** Liquid glue is reusable across many prints; glue stick must be reapplied.
2. **Stringing.** Default Bambu profiles are generally clean but if a part comes out stringy, the failure cascade is: dry the filament → enable longer retract distance → reduce nozzle temp by 5-10°C → increase travel speed.
3. **Enclosure benefit.** Even though PETG is open-frame-OK, an enclosed printer (X1C / P1S) gives better interlayer Z-strength when the ambient is cold. The wiki specifically calls this out: *"for PETG and PETG-CF/GF, in order to avoid the low ambient temperature causing the low interlayer strength of the model, it is more recommended to use a enclosed printer."* [Source: https://wiki.bambulab.com/en/general/filament-guide-material-table (retrieved 2026-05-06)]
4. **Top-layer cooling.** PETG's optimal part-cooling-fan range is 0-80%, lower than PLA's 50-100%. Default profiles handle this.

### PETG-CF — when carbon fiber actually helps

PETG-CF replaces some matrix polymer with chopped carbon fiber. Stiffness jumps significantly (bending modulus 3950 vs 2050 MPa for plain PETG). But **bending strength drops** (89 vs 64 — the fiber reinforcement helps stiffness more than strength) and the surface gets a matte technical finish that some find aesthetically nice and some find ugly.

The community-tested observation [TENTATIVE — Bambu forum reference]: in real-world tensile tests, plain PETG and PETG-CF often perform similarly because the fibers introduce micro-defects that offset the reinforcement gain. **Pick PETG-CF for stiffness and aesthetic, not for absolute strength.** [Source: https://forum.bambulab.com/t/lets-talk-tested-filaments/56930 (retrieved 2026-05-06)]

[CONFIRMED] PETG is the workhorse functional filament for the friend's likely use cases on any Bambu model. [CONFIRMED] PETG-CF is more about stiffness and finish than strength gain. [TENTATIVE] Brand-to-brand variability is significant (per Bambu forum cross-brand testing); Bambu's own SKUs are known-good but more expensive than Polymaker / Sunlu equivalents.

## Snippets

(none — entity page; underlying data lives on @sources/2026-bambu-filament-guide.md)
