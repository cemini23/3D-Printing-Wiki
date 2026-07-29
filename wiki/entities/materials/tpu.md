---
title: TPU (Thermoplastic Polyurethane)
type: entity
tags: [material, filament, FDM, baseline, flexible, elastomer]
keywords: [TPU, thermoplastic polyurethane, TPU 95A, TPU 95A HF, TPU 90A, TPU 85A, flexible, rubber, shore hardness, dedicated AMS port]
related:
  - concepts/filaments-baseline.md
  - concepts/fdm-printing.md
  - sources/2026-bambu-filament-guide.md
  - entities/materials/pla.md
  - entities/materials/petg.md
  - entities/materials/abs.md
  - entities/materials/asa.md
  - entities/tools/rebot-devarm.md
  - concepts/shape-changing-fdm-interfaces.md
  - concepts/open-source-legged-robotics.md
  - sources/2026-li-duomorph-fdm-pneumatic.md
  - sources/2025-yoshimura-m3d-skin-tactile-fdm.md
  - sources/2025-pattabiraman-eflesh-magnetic-tactile.md
  - concepts/soft-robotics-fdm-diw.md
  - sources/2026-hansen-tendon-actuated-tpu-backbone.md
  - sources/2025-miyama-soft-hand-skin-skeleton.md
  - sources/2026-wade-slicer-project-compilation.md
  - concepts/slicer-project-compilation.md
maturity: draft
created: 2026-05-06
updated: 2026-07-29
---

## Relations

@concepts/filaments-baseline.md @concepts/fdm-printing.md @concepts/shape-changing-fdm-interfaces.md @concepts/open-source-legged-robotics.md @concepts/soft-robotics-fdm-diw.md @sources/2025-yoshimura-m3d-skin-tactile-fdm.md @sources/2025-pattabiraman-eflesh-magnetic-tactile.md @sources/2026-bambu-filament-guide.md @sources/2026-li-duomorph-fdm-pneumatic.md @sources/2026-hansen-tendon-actuated-tpu-backbone.md @sources/2025-miyama-soft-hand-skin-skeleton.md @entities/materials/pla.md @entities/materials/petg.md @entities/materials/abs.md @entities/materials/asa.md @entities/tools/rebot-devarm.md @sources/2026-wade-slicer-project-compilation.md @concepts/slicer-project-compilation.md

## Raw Concept

The flexible filament. **TPU (thermoplastic polyurethane)** is the rubber-like, flexible elastomer. Print phone-case skins, gaskets, vibration dampers, watch bands, jar lids, wheel tires for RC cars. Different from rigid filaments in every important workflow dimension: slow-print only, drying required, dedicated AMS port (only the 95A HF variant), no glue stick, no enclosure.

## Narrative

### What "Shore hardness" means

TPU comes in different stiffness grades, labeled by **Shore A hardness** — a standard scale where higher number = harder/less-flexible:

| Shore | Feels like | Bambu SKU available? | AMS-compatible? |
|---|---|---|---|
| **85A** | Very soft (rubber band, soft sneaker sole) | Bambu TPU 85A | **No** (too soft to feed reliably) |
| **90A** | Soft (tire sidewall, mouse pad) | Bambu TPU 90A | **No** |
| **95A** | Firm (skateboard wheel, phone case) | Bambu TPU 95A, **TPU 95A HF** | TPU 95A HF: yes (dedicated port). TPU 95A: ? — check |
| Shore D scale starts | Rigid plastics begin | — | — |

**Practical translation:** for AMS multi-color flexible work, only **TPU 95A HF** is supported. Softer grades (90A, 85A) must be printed manually-fed or single-spool-only. The reader's first TPU spool should be **95A or 95A HF** for compatibility.

### Foaming / graded Shore TPU (research)

**ColorFabb VarioShore TPU** (and similar temperature-responsive foaming TPUs) can vary density and Shore A via nozzle temperature + flow compensation — used as the process-state target in OpenVCAD slicer-project compilation [@sources/2026-wade-slicer-project-compilation.md]. Printed Shore gradient 65A→85A achieved MAE **0.5 Shore A** in that paper's calibration. **Not** a Bambu AMS day-1 SKU; specialty research filament. [CONFIRMED — paper calibration; [TENTATIVE] for other brands]

### When TPU is the right choice

- **Phone cases.** TPU is what 90% of commercial drop-protection cases are molded from.
- **Gaskets, seals, jar lids with tight fit.** Flex deforms to seal small gaps.
- **Vibration-damping mounts.** Camera mounts, drone landing gear pads, machine-tool isolation.
- **Wearable / strap items.** Watch bands, wristbands, backpack clips that need to flex without snapping.
- **Tires for RC cars / scaled toys.** TPU 90A or 95A; brittleness of PLA / PETG fails immediately on impact at scale-RC speeds.
- **Living-hinge designs.** Where two parts join via a thin flexing strip.

### When TPU is the wrong choice

- **Anything load-bearing in compression.** TPU compresses; doesn't hold a load. Brackets, mounts, and structural parts must be rigid (PLA / PETG / ABS / ASA).
- **High-temperature environments.** TPU softens around 80°C — lower than HDT of any rigid filament. Don't put TPU parts in cars in summer.
- **High-precision, high-detail prints.** TPU's flexibility means small features (text, sharp corners, fine threads) print noticeably softer/blurred than on PLA.
- **Beginner first-month prints.** TPU is the highest-friction filament to feed — bowden tubes, sharp PTFE bends, and rapid travel moves all cause feeding failures. **Direct-drive extruder strongly preferred** (Bambu's printers are direct-drive — good).

**Research note:** @sources/2025-yoshimura-m3d-skin-tactile-fdm.md pairs **TPU + conductive TPU** infill for printed pressure sensors — requires **multi-material FDM**, not a typical single-nozzle first printer (@concepts/open-source-legged-robotics.md).

### Specs (Bambu TPU 95A HF) [Source: https://bambulab.com/en-us/filament/guide (retrieved 2026-05-06)]

| Property | Value |
|---|---|
| Impact strength XY / Z (kJ/m²) | 124.3 / 86.3 |
| Bending strength XY (MPa) | N/A (elastomer; doesn't break in standard test) |
| Bending modulus XY (MPa) | N/A |
| HDT @ 0.45 MPa (°C) | N/A (softens gradually) |
| Saturated water absorption (25°C, 55% RH) | **1.08%** — highest of the baseline filaments |
| Nozzle temperature | 220-240°C |
| Bed temperature | 30-35°C (yes, room-temperature; TPU sticks at low bed temp) |
| Print speed | **<200 mm/s** (lower than rigid filaments) |
| Part cooling fan | 0-50% |
| **Drying before use** | **Required** (70°C 8h) |
| Drying schedule | 70°C 8h |
| Enclosure | Not required |
| **AMS / AMS lite compatibility** | TPU 95A HF: dedicated AMS port (single-port only) / not on AMS lite |
| Build plate compatibility | PEI plates, no glue needed |
| Nozzle material | Any |

**Why drying is required, not optional**: TPU's saturated water absorption (1.08%) is **2.5x higher than PLA, ABS, ASA**. Wet TPU prints with stringing, popping/crackling sounds, surface bubbles, and very weak layer bonds. **Bambu's recommendation is to dry every spool before use, not just visibly-damp ones.** A blast-drying oven or AMS HT chamber is the right tool.

### The "dedicated AMS port" thing

Bambu's AMS (the full unit) has 4 filament ports. **One of those 4 is configurable as a TPU port** — it bypasses the transmission gear path that would mangle soft filament. **Only TPU 95A HF is supported** in this slot, and **only one slot at a time can be the TPU port**. So:

- Multi-color TPU printing: limited to one TPU spool per AMS. No 2-color TPU prints from a single AMS.
- AMS lite: no TPU support at all (no port can be reconfigured for it).
- TPU 90A and TPU 85A: AMS-incompatible regardless of slot.

Practical impact for the reader: TPU is workable as a single-color filament on the AMS by allocating one slot for it. TPU multi-color is essentially out of reach without two AMS units chained together. [Source: https://wiki.bambulab.com/en/general/filament-guide-material-table (retrieved 2026-05-06)]

### Workflow gotchas

1. **Slow speed.** 100-200 mm/s, lower than rigid filaments' 250-300 mm/s defaults. A multi-hour print can become significantly longer.
2. **Bowden vs direct drive.** Bambu's printers are direct-drive (good for TPU). Older Ender / printers with long bowden tubes feed TPU poorly because flexible filament buckles in the tube.
3. **Retraction tuning.** TPU strings if retraction is too aggressive; jams if retraction is too long. Default Bambu profiles handle 95A HF; manual tuning needed for 90A / 85A.
4. **Storage and drying.** Buy TPU in vacuum-sealed packaging (with desiccant). Once opened, store in a sealed box with desiccant. Dry before every print if not used within a few days.
5. **Layer adhesion is uniformly excellent.** Z impact (86.3) is much closer to XY impact (124.3) than for any rigid filament — because TPU's elastic modulus is low, the layer-bond strength dominates. **TPU prints don't have a Z-axis weakness.** Print orientation matters less than for rigid filaments.

### TPU variants the reader might encounter

| Variant | Difference | When to pick |
|---|---|---|
| **TPU 95A HF** | "High Flow" 95A; AMS-compatible via dedicated port | Default flexible filament; phone cases, mounts |
| **TPU 95A** | Standard 95A; AMS compatibility limited | Backup if 95A HF out of stock |
| **TPU 90A** | Softer, more flexible | Tires, watch bands, soft grip parts |
| **TPU 85A** | Very soft, gel-like | Gaskets, very-soft seals (rare hobbyist use) |
| **TPU for AMS** | Specifically formulated for reliable AMS feeding | Bambu's recommended TPU SKU for multi-spool work |

[CONFIRMED] TPU 95A HF is the only TPU variant fully AMS-compatible (on the regular AMS, single-port only — not AMS lite). [CONFIRMED] TPU drying is non-optional (1.08% absorption). [CONFIRMED] TPU layer adhesion is uniformly strong; no Z-axis weakness like rigid filaments. [TENTATIVE] TPU brand variability is significant; Bambu and Polymaker are reliably-printable; cheaper brands often feed unreliably even on direct-drive extruders.

## Snippets

(none — entity page; underlying data lives on @sources/2026-bambu-filament-guide.md)
