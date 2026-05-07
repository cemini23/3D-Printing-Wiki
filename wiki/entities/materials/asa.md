---
title: ASA (Acrylonitrile Styrene Acrylate)
type: entity
tags: [material, filament, FDM, baseline, engineering, enclosed-only, UV-stable]
keywords: [ASA, acrylonitrile styrene acrylate, UV-stable, outdoor, weatherable, enclosure, ABS replacement]
related:
  - concepts/filaments-baseline.md
  - concepts/fdm-printing.md
  - sources/2026-bambu-filament-guide.md
  - entities/materials/pla.md
  - entities/materials/petg.md
  - entities/materials/abs.md
  - entities/materials/tpu.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

@concepts/filaments-baseline.md @concepts/fdm-printing.md @sources/2026-bambu-filament-guide.md @entities/materials/pla.md @entities/materials/petg.md @entities/materials/abs.md @entities/materials/tpu.md

## Raw Concept

The outdoor filament. **ASA (acrylonitrile styrene acrylate)** is the UV-stable cousin of ABS — same processing, same enclosure requirement, same impact tolerance, but the styrene-butadiene component is replaced with styrene-acrylate, which is **far more resistant to UV degradation**. If the part lives outdoors and the printer is enclosed (X1C, P1S), ASA is the right answer.

## Narrative

### The pitch

ASA is "ABS but UV-stable." Same printability profile, same hardware requirements, slightly different mechanical numbers (somewhat stiffer, slightly less impact-tolerant), but **dramatically better outdoor longevity**. ABS exposed to UV yellows visibly within months and embrittles within a year. ASA holds color and toughness for years of outdoor exposure. Used by industry for automotive exterior trim and outdoor signage for exactly this reason.

[Source: https://bambulab.com/en-us/filament/guide (retrieved 2026-05-06)] *Bambu's ASA spec advertises higher bending strength (108 vs 65 MPa) and modulus (2310 vs 1920 MPa) than ABS, plus higher HDT (117°C vs 100°C). The trade-off: slightly lower impact strength XY (34.8 vs 41.0 kJ/m²).*

### When ASA is the right choice

- **Outdoor parts.** Mailbox brackets, outdoor camera mounts, garden organizers, tree-fixture hardware, antenna mounts. Anything that sees sunlight.
- **Cars (parked outside).** Dashboard mounts, sunshade brackets, license-plate frames. ABS cracks, PETG warps, ASA holds.
- **Marine / pool / coastal.** Salt + UV is brutal on PLA, hard on PETG, fine on ASA.
- **Anywhere the reader would have used ABS** if the printer is enclosed (X1, X1C, P1S). The price difference is small; ASA is just better for most ABS use cases.

### When ASA is the wrong choice

- **Open-frame printer.** Same enclosure requirement as ABS — not viable on A1 / A1 mini / unsealed P1P. Use PETG; accept faster UV degradation.
- **Indoor parts where UV-stability is irrelevant.** ASA costs slightly more than ABS for no benefit indoors.
- **Maximum impact strength priority.** ABS edges ASA on impact XY (41 vs 34.8). Marginal — orient prints so impact is in XY for either material.
- **Aesthetic-first printing.** ASA's surface finish is good but not visibly different from ABS. PLA / PLA Silk / PETG Translucent have better aesthetic-effect range.

### Specs (Bambu ASA) [Source: https://bambulab.com/en-us/filament/guide (retrieved 2026-05-06)]

| Property | Value |
|---|---|
| Impact strength XY / Z (kJ/m²) | 34.8 / 9.0 |
| Bending strength XY (MPa) | 108 |
| Bending modulus XY (MPa) | 2310 |
| HDT @ 0.45 MPa (°C) | 117 |
| Saturated water absorption (25°C, 55% RH) | 0.25% (lowest of baseline filaments) |
| Nozzle temperature | 240-280°C |
| Bed temperature | 90-100°C |
| Print speed | <300 mm/s |
| Part cooling fan | 0-80% |
| Drying before use | Optional (80°C 8h) |
| Annealing | 80-90°C, 6-12h |
| **Enclosure** | **Required** (X1, X1C, P1S) |
| AMS / AMS lite | Both compatible (better AMS-lite story than ABS) |
| Build plate compatibility | Engineering / Smooth PEI / Textured PEI / High-Temp Plate. Cool Plate not recommended. |
| Glue | Bambu Liquid Glue or glue stick required |
| Nozzle material | Any (hardened only for ASA-CF / ASA-GF) |

### ASA vs ABS — the choice

| Dimension | ABS | ASA | Winner |
|---|---|---|---|
| HDT | 100°C | 117°C | ASA |
| Impact strength XY | 41.0 | 34.8 | ABS (marginal) |
| Impact strength Z | 4.9 | 9.0 | ASA |
| Bending strength | 65 | 108 | ASA |
| Bending modulus | 1920 | 2310 | ASA (stiffer) |
| Water absorption | 0.45% | 0.25% | ASA |
| UV stability | Poor | Excellent | **ASA (massive)** |
| Acetone-smoothable | Yes | Yes (slightly different result) | Tie |
| AMS lite compatible | Not recommended | Yes | ASA |
| Bambu spool price | Slightly cheaper | Slightly more expensive | ABS |
| Real-world hobbyist pick | Indoor only | Indoor or outdoor | **ASA** for any outdoor part |

**Conclusion:** if the reader has an enclosed printer (X1C / P1S), ASA is the better default than ABS for almost everything. Only stick with ABS if there's a specific reason (impact-XY load critical, or matching color to existing ABS hardware).

### Workflow gotchas

1. **Same enclosure / build-plate / glue rules as ABS.** No new gotchas there.
2. **Bambu's AMS-lite story is better for ASA than ABS.** ASA prints fine on AMS lite (whereas ABS isn't recommended). So a reader with a P1P or AMS lite has ASA as a workable option.
3. **No acetone-smoothing performance gap.** ASA acetone-smooths similarly to ABS — surface finish is glossy and good.
4. **Lower water absorption = less drying paranoia.** 0.25% saturated absorption is the lowest of the baseline filaments — a closed cardboard box with desiccant is sufficient indefinitely.

[CONFIRMED] ASA requires an enclosed Bambu (X1, X1C, P1S). [CONFIRMED] ASA outperforms ABS on UV-stable, water-absorption, HDT, and bending strength — the only ABS edge is marginal impact-XY. [TENTATIVE] If the reader has an enclosed printer and wants one engineering filament, ASA over ABS is probably the right default.

## Snippets

(none — entity page; underlying data lives on @sources/2026-bambu-filament-guide.md)
