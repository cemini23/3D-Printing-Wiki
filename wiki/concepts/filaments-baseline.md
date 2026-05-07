---
title: Filaments Baseline (PLA / PETG / ABS / ASA / TPU)
type: concept
tags: [materials, filament, FDM, baseline, reference]
keywords: [PLA, PETG, ABS, ASA, TPU, PC, polylactic acid, polyethylene terephthalate glycol, acrylonitrile butadiene styrene, polycarbonate, thermoplastic polyurethane, hygroscopy, HDT, glass transition, layer adhesion, enclosure, AMS]
related:
  - concepts/fdm-printing.md
  - sources/2026-bambu-filament-guide.md
  - entities/materials/pla.md
  - entities/materials/petg.md
  - entities/materials/abs.md
  - entities/materials/asa.md
  - entities/materials/tpu.md
  - entities/tools/kickstarter-autodesk-fdm-protocol.md
  - entities/printers/x1c.md
  - entities/printers/p1s.md
  - entities/printers/a1.md
maturity: draft
created: 2026-05-06
updated: 2026-05-07
---

## Relations

@concepts/fdm-printing.md @sources/2026-bambu-filament-guide.md @entities/materials/pla.md @entities/materials/petg.md @entities/materials/abs.md @entities/materials/asa.md @entities/materials/tpu.md @entities/tools/kickstarter-autodesk-fdm-protocol.md @entities/printers/x1c.md @entities/printers/p1s.md @entities/printers/a1.md

## Raw Concept

The five filament types a Bambu user actually buys in their first year: PLA, PETG, ABS, ASA, TPU. This page is the decision matrix — when each is the right answer, what each costs in printer-hardware terms, what each costs in workflow terms (drying / enclosure / nozzle wear). Engineering filaments (PC, PA, fiber-reinforced) are out of scope here — they show up only when a specific application demands them, and at that point the reader should read the dedicated source pages.

Synthesized 2026-05-06 from the Bambu Lab vendor reference [@sources/2026-bambu-filament-guide.md]. Single-source (Bambu's own labs); cross-validation against independent benchmarks (Filabase, CNC Kitchen, My Tech Fun) deferred unless a specific claim becomes load-bearing.

## Narrative

### The 30-second decision matrix

| If your part needs to… | Use | Why |
|---|---|---|
| Look good, print easy, low cost, hobby/decor | **PLA** | Easiest to print; widest color/effect selection; cheapest |
| Be functional, hold up to mild heat, take stress without shattering | **PETG** | Stronger layer adhesion than ABS; printable on open-frame Bambu A1; higher HDT than PLA |
| Survive in a hot car, hold up to high temperature, take impact | **ABS** | HDT 100°C; impact-resistant; **requires enclosed printer (X1C, P1S)** |
| Survive outdoors / UV exposure | **ASA** | UV-stable variant of ABS; same enclosure requirement |
| Bend, flex, or grip without breaking | **TPU** | Rubber-like; not rigid; needs slow-print + dedicated AMS port |

### Mechanical comparison (Bambu test data) [Source: https://bambulab.com/en-us/filament/guide (retrieved 2026-05-06)]

| Property | **PLA** | **PETG** | **PETG HF** | **ABS** | **ASA** | **TPU 95A HF** |
|---|---|---|---|---|---|---|
| Impact strength XY (kJ/m²) | 26.6 | 31.5 | 39.3 | 41.0 | 34.8 | 124.3 |
| Impact strength Z (kJ/m²) | 13.8 | 10.6 | 7.4 | 4.9 | 9.0 | 86.3 |
| Bending strength XY (MPa) | 76 | 64 | 62 | 65 | 108 | N/A |
| Bending modulus XY (MPa) | 2750 | 2050 | 1880 | 1920 | 2310 | N/A |
| HDT @ 0.45 MPa (°C) | 57 | 69 | 87 | 100 | 117 | N/A |
| Saturated water absorption % | 0.43% | 0.40% | 0.65% | 0.45% | 0.25% | 1.08% |

### Process comparison (Bambu defaults) [Source: same]

| Property | **PLA** | **PETG** | **PETG HF** | **ABS** | **ASA** | **TPU 95A HF** |
|---|---|---|---|---|---|---|
| Nozzle temp (°C) | 190-230 | 230-260 | 230-260 | 240-280 | 240-280 | 220-240 |
| Bed temp on PEI (°C) | 45-65 | 60-80 | 60-80 | 90-100 | 90-100 | 30-35 |
| Max recommended speed (mm/s) | <300 | <300 | <300 | <300 | <300 | <200 |
| Drying needed before use? | Optional | Optional | **Required** | Optional | Optional | **Required** |
| Drying schedule | 50°C 8h | 65°C 8h | 65°C 8h | 80°C 8h | 80°C 8h | 70°C 8h |
| Enclosure required? | No | No (recommended) | No (recommended) | **Yes** | **Yes** | No |
| AMS / AMS lite compatible? | Yes / Yes | Yes / Yes | Yes / Yes | AMS yes / **lite no** | Yes / Yes | dedicated TPU port (95A HF only) |
| Hardened steel nozzle? | No | No | No | No | No | No |

### The four rules that explain the table

1. **Enclosure rule.** Materials with a high glass transition (ABS / ASA / PC / PA) shrink as they cool. On an open-frame printer the bottom of a part has cooled and locked in by the time the top is being printed, and the differential shrinkage cracks the part vertically. An enclosed chamber holds the air at ~50°C, slowing cooling enough for the whole part to shrink uniformly. **Hardware constraint, not tuning.** No bed-temp / nozzle-temp combo fixes this on an A1 / A1 mini.
2. **Drying rule.** Hygroscopic materials (PETG HF / PC / PA / TPU) absorb water from air; water boils into bubbles in the nozzle, ruining surface finish and weakening layer bonds. Bambu sells the AMS 2 Pro and AMS HT specifically as drying chambers. Alternative: dedicated blast-drying oven (FilaDry, e.g.). The reader can probably skip a drying chamber on day 1 if they only print PLA + PETG basic, but if they buy TPU or PETG HF, drying is non-optional.
3. **AMS-lite rule.** Bambu's two AMS units differ: AMS has a transmission gear that helps push rough or soft filaments through; AMS lite doesn't. So PLA Glow, PETG-CF, PLA Wood, ABS, PC, PA — all listed as "AMS-compatible but **not recommended** on AMS lite." A reader buying an A1 mini gets only AMS lite. **Material restriction is real and not in marketing copy.** [Source: https://wiki.bambulab.com/en/general/filament-guide-material-table (retrieved 2026-05-06)]
4. **Hardened-nozzle rule.** Pure PLA / PETG / ABS / ASA / TPU print fine on stainless-steel or brass nozzles. CF or GF reinforced filaments (PLA-CF, PETG-CF, etc.) need hardened steel — abrasive fibers wear soft nozzles fast.

### Layer adhesion is the dominant FDM weakness

The Z impact-strength column collapses to 5-10× lower than the XY column for every rigid filament. ABS goes from 41 kJ/m² (XY) to 4.9 (Z) — a load-bearing part oriented with stress in the Z direction can fail at one-eighth the load it would survive in XY. **Print orientation matters more than material choice for thin load-bearing parts.** TPU is the exception: rubbery, layer-adhesion-dominated, high in both XY and Z because the elastic modulus is much lower than the layer-bond strength.

### Decision tree for the reader's likely first-year materials

```
Q1: Is the part going to live somewhere hot (car interior, near a window in summer, near a heat-emitting device)?
├── YES → ABS (or ASA if outdoor / UV-exposed). Requires X1C / P1S, not A1.
└── NO → continue to Q2.

Q2: Does the part need to bend or flex?
├── YES → TPU. Slow-print, dedicated AMS port, drying required.
└── NO → continue to Q3.

Q3: Is the part functional or load-bearing?
├── YES, light load (organizers, mounts, brackets) → PETG. Strong, easy to print.
└── NO, decorative or hobby → PLA. Easiest, cheapest, prettiest.
```

### What's NOT covered here

- **PC (Polycarbonate)**: HDT 113°C, very tough, requires enclosed printer + drying. Specialty engineering use. Bambu data sheet has full numbers; create a dedicated entity page when an application calls for it.
- **PA / Nylon and CF/GF reinforced filaments**: Engineering territory. HDT 186°C+. Need hardened nozzle, drying, enclosed printer, and slow speeds. Out of scope until reader has a specific use case.
- **Specialty PLA** (PLA Wood, PLA Marble, PLA Sparkle, PLA Glow, PLA Silk, PLA-CF): largely a *cosmetic* differentiation — same printer settings as PLA Basic but with abrasive or rough fillers that complicate AMS lite compatibility. The PLA entity page covers these as variants.

[CONFIRMED] All datapoints in this synthesis come directly from Bambu's vendor documentation (single-source). [TENTATIVE] The decision tree is opinionated synthesis tuned for a Bambu user starting hobby-and-Etsy work; an engineering or industrial user would weight differently.

## Snippets

(none — synthesis page; verbatim quotes live on `@sources/2026-bambu-filament-guide.md`)
