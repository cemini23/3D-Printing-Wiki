---
title: PLA (Polylactic Acid)
type: entity
tags: [material, filament, FDM, baseline, biodegradable]
keywords: [PLA, polylactic acid, PLA Basic, PLA Matte, PLA Tough, PLA Silk, PLA Aero, PLA-CF, PLA Wood, PLA Marble, PLA Sparkle, PLA Glow, biodegradable, low-temperature]
related:
  - concepts/filaments-baseline.md
  - concepts/fdm-printing.md
  - sources/2026-bambu-filament-guide.md
  - entities/materials/petg.md
  - entities/materials/abs.md
  - entities/materials/asa.md
  - entities/materials/tpu.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

@concepts/filaments-baseline.md @concepts/fdm-printing.md @sources/2026-bambu-filament-guide.md @entities/materials/petg.md @entities/materials/abs.md @entities/materials/asa.md @entities/materials/tpu.md

## Raw Concept

The default filament. **PLA (polylactic acid)** is the easiest-printing, cheapest, most-color-varied, and most-Etsy-friendly filament. ~80-90% of a typical hobbyist's print volume is PLA. The reader should buy 4-6 spools of PLA (varied colors) before considering anything else.

## Narrative

### Why PLA is the default

- **Easiest to print.** Prints flat without warping on bare PEI build plate at 45-65°C bed; doesn't need an enclosure; no significant fume issue (mild sweet smell, food-grade source material).
- **Widest variant catalog.** Plain PLA Basic, plus aesthetic variants: Matte (no surface gloss, hides layer lines), Silk (high-gloss), Marble / Wood / Sparkle / Glow / Metal (cosmetic fillers), Tough (polymer modified for higher impact), Aero (low-density foam-print for lightweight RC parts), and Carbon-Fiber-reinforced (PLA-CF) for stiff structural parts.
- **Cheapest per kg.** Bambu Basic PLA is $14.99/spool (1kg); third-party brands (Hatchbox, Polymaker, Sunlu, Esun) sell at $14-22/kg [TENTATIVE — pricing fluctuates; check at purchase time].
- **Bambu compatibility is universal.** Works on all Bambu printers (X1, X1C, X1E, P1S, P1P, A1, A1 mini), all AMS / AMS lite units, all build plates (Cool Plate / PLA Plate / Engineering Plate / Smooth PEI / Textured PEI / High-Temperature Plate), all nozzle materials (brass / stainless steel / hardened steel — the latter only needed for PLA-CF). [Source: https://wiki.bambulab.com/en/general/filament-guide-material-table (retrieved 2026-05-06)]

### When PLA is the wrong choice

- **Hot environments.** PLA softens around 50°C and starts to deform under load. A part left in a parked car on a summer day **will sag**. PLA HDT (heat deflection temperature at 0.45 MPa load) is **57°C** — lowest of any common filament. Use PETG / ABS / ASA for anything that lives outside a climate-controlled room.
- **High-stress functional parts.** PLA is rigid but **brittle**. Impact strength XY = 26.6 kJ/m² (lowest of the rigid filaments). A drone arm, a bicycle mount, or a tool handle should be PETG or ABS.
- **Outdoor / UV-exposed.** PLA degrades in sustained UV. ASA is the right choice.
- **Anything that needs to flex.** TPU.
- **Food-contact (claimed).** "PLA is corn-based and biodegradable" is true; "PLA prints are food-safe" is **not** trivially true — layer lines trap residue, additives vary by brand, and the nozzle wear deposits brass particles. Don't use printed PLA for repeated food contact without a food-grade epoxy seal. [Source: https://help.prusa3d.com/filament-material-guide (retrieved 2026-05-06)]

### Specs (Bambu Basic PLA) [Source: https://bambulab.com/en-us/filament/guide (retrieved 2026-05-06)]

| Property | Value |
|---|---|
| Impact strength XY / Z (kJ/m²) | 26.6 / 13.8 |
| Bending strength XY (MPa) | 76 |
| Bending modulus XY (MPa) | 2750 |
| HDT @ 0.45 MPa (°C) | 57 |
| Saturated water absorption (25°C, 55% RH) | 0.43% |
| Nozzle temperature | 190-230°C |
| Bed temperature (PEI plate) | 45-65°C |
| Print speed | <300 mm/s |
| Part cooling fan | 50-100% |
| Drying before use | Optional (50°C, 8h) |
| Annealing | 50-60°C, 6-12h (improves heat resistance) |
| Enclosure | Not required |
| AMS / AMS lite | Both compatible |
| Nozzle material | Any (hardened only for PLA-CF) |

### Variants the reader will encounter

| Variant | Difference vs Basic | When to pick it |
|---|---|---|
| **PLA Basic** | The reference | Default for everything |
| **PLA Matte** | Matte surface; better at hiding layer lines | Anywhere appearance matters more than gloss |
| **PLA Silk** | High-gloss, slight color shift | Premium decorative pieces, jewelry boxes |
| **PLA Tough** | Modified for higher impact resistance | Light functional parts where ABS isn't worth the enclosure |
| **PLA-CF** | Carbon-fiber reinforced | Stiff structural parts; needs hardened nozzle |
| **PLA Marble / Wood / Sparkle / Glow** | Aesthetic fillers | Decorative; AMS lite **not recommended** for these |
| **PLA Aero** | Foamed / low density | Lightweight RC airplane parts (specialty) |

### Storage and shelf life

PLA is mildly hygroscopic (0.43% saturated water absorption) but tolerates casual storage. Wet PLA causes stringing and rough surfaces; dry it at 50°C for 8 hours if a print looks worse than usual. A cardboard box with a single desiccant pack inside is sufficient for storage in a normal-humidity home environment. **Don't overspend on a drying chamber for PLA-only use** — that money goes further into a third-party PETG / ABS / TPU starter pack.

### What "biodegradable" actually means

PLA is bioplastic (corn / sugarcane derived), and *industrially compostable* — meaning a commercial composting facility (60-70°C + microbial activity) will break it down in months. **In a backyard compost or landfill, PLA degrades over decades, similar to other plastics.** The marketing "biodegradable" claim is technically true but practically misleading for hobbyist-discard purposes. [Source: https://help.prusa3d.com/filament-material-guide (retrieved 2026-05-06)] [TENTATIVE — composting timeline varies by facility; rough estimate]

[CONFIRMED] PLA is the right starter filament for a Bambu user. [CONFIRMED] PLA is unsuitable for hot or load-bearing or outdoor parts. [TENTATIVE] Cross-brand quality comparison (Bambu vs Polymaker vs Hatchbox vs Sunlu) requires independent benchmark data not in scope here.

## Snippets

(none — entity page; underlying data lives on @sources/2026-bambu-filament-guide.md)
