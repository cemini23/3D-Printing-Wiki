---
title: Bambu Lab H2D
type: entity
tags: [printer, bambu, h2d, dual-nozzle, corexy, enclosed, heated-chamber, large-format]
keywords: [H2D, Bambu H2D, dual nozzle, dual toolhead, IDEX, 350x320x325, heated chamber, 65C chamber, 350C nozzle, laser module, BirdsEye camera, AMS 2 Pro, H2D Pro, H2S, H2C, X2D]
related:
  - concepts/fdm-printing.md
  - concepts/soft-robotics-fdm-diw.md
  - concepts/filaments-baseline.md
  - entities/printers/x1c.md
  - entities/materials/tpu.md
  - sources/2026-qin-cosserat-trimmed-helicoid.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
wire_status: wont_wire
wire_target: "Purchase-decision reference only; 3D-printing Phase-1 local wires off"
---

## Relations

@concepts/fdm-printing.md @concepts/soft-robotics-fdm-diw.md @concepts/filaments-baseline.md @entities/printers/x1c.md @entities/materials/tpu.md @sources/2026-qin-cosserat-trimmed-helicoid.md

## Raw Concept

Created by ingest pass 34 (2026-09-30). Trigger: [@sources/2026-qin-cosserat-trimmed-helicoid.md] printed a multi-section TPU 95A continuum arm on an **H2D** — the first H2D sighting in this wiki. The H2D is the top of Bambu's current line and is the only consumer Bambu with a **heated chamber**, which changes the ABS/ASA/PA story that [@entities/printers/x1c.md] currently owns. **Purchase-decision page — treat every number below with the provenance tag attached.**

## Narrative

### What the H2D is

Bambu Lab's **large-format, dual-nozzle, enclosed** printer — the top of its consumer line at time of writing (2026-09). Where the [@entities/printers/x1c.md] is the single-nozzle flagship that defined Bambu's closed-loop feature set, the H2D changes the **mechanics**: two independent toolheads instead of one, on the biggest build volume Bambu sells [Source: https://us.store.bambulab.com/products/h2d (retrieved 2026-09-30)].

### Specs

[TENTATIVE — commercial listings, not first-party spec-sheet verification. Verify at https://bambulab.com/en/h2d/tech-specs before quoting in a purchase decision.]

| Property | Value | Provenance |
|---|---|---|
| Extruders | **2 independent toolheads**, dual hardened steel nozzles | Multi-source: Bambu store, 3D Printing Industry, MatterHackers |
| Build volume | **350 × 320 × 325 mm** (350-wide figure requires identical filament in both nozzles) | Multi-source: Bambu store, 3D Printing Industry, MatterHackers |
| Max nozzle temp | **350 °C** | Multi-source: Source Graphics, MatterHackers |
| Chamber | **Actively heated, 65 °C** | Multi-source: BambuHub, Geeky Inc |
| Toolhead speed | 1000 mm/s, 20,000 mm/s² acceleration | Single-source: 3D Printing Industry |
| Motion accuracy | 50 µm | Multi-source: 3D Printing Industry, MatterHackers |
| Enclosure | Fully enclosed | Bambu store |
| Laser option | Optional **10 W / 40 W** laser modules (all-in-one "Bambu Suite" workflow) | Multi-source: MatterHackers, BambuHub |
| Camera | **BirdsEye** top-view camera (laser edition / upgrade kit); AI nozzle camera with macro lens | Bambu store |
| Filaments | PLA, PETG, TPU, PVA, BVOH, ABS, ASA, PC, PA, PET, PPS, PPA + carbon/glass-fibre variants | Single-source: Source Graphics |
| AMS | Two new AMS systems with **integrated filament drying** | Single-source: 3D Printing Industry |
| Price | **~$1,549** (Bambu US store, Sept 2026); one reseller lists a $1,749 typical price | Conflicting — [NEEDS VERIFICATION 2026-09-30] |
| Released | Apr 2025 | Single-source: BambuHub |

### Why the dual nozzle matters

The X1C does multi-color through **one** nozzle by purging between filament changes — that purge is wasted material and time. The H2D's second toolhead removes the purge for two-material work, and enables things a single nozzle cannot do well [Source: https://3dprintingindustry.com/news/bambu-labs-new-h2d-3d-printer-technical-specifications-and-pricing-237763/ (retrieved 2026-09-30)]:

- **Soluble support** (PVA/BVOH) printed by the second nozzle and dissolved away.
- **Two mechanical materials** in one part — rigid + flexible, without a purge interface.
- **Two materials at different temperatures** in the same layer.

This is why the wiki's soft-robotics pages care: [@sources/2026-qin-cosserat-trimmed-helicoid.md] used the H2D to print **TPU 95A structure with PLA rigid connectors** — a rigid-plus-flexible build that is awkward on a single-nozzle machine.

### The heated chamber — the real differentiator vs X1C

The 65 °C actively heated chamber is the feature that most changes the **materials** story [@concepts/filaments-baseline.md]:

- [@entities/materials/abs.md] and [@entities/materials/asa.md] need a **warm, stable** chamber to avoid warping and layer splitting. The X1C's enclosure is passive; the H2D actively holds temperature.
- That extends Bambu's engineering-material range upward — PC, PA, PPS, PPA and their fibre-filled variants are listed as supported [Source: Source Graphics].
- Practical translation: if the reader's goal is **large engineering parts**, the H2D's chamber + volume + 350 °C nozzle is the meaningful step up from the X1C. If the goal is decorative PLA/PETG at moderate size, the premium buys nothing that the X1C or P1S does not already do.

### Caveats for a purchase decision

- **Prices in this page conflict** and were taken from reseller and aggregator pages, not a verified Bambu invoice. Confirm on the Bambu store before deciding. [NEEDS VERIFICATION 2026-09-30]
- **Model-line churn.** Third-party 2026 comparison pages reference sibling models (H2S, H2D Pro, H2C, X2D) with different prices and feature splits. These came from **single commercial sources** and are **not verified** here — the Bambu lineup moved several times through 2025–2026. [NEEDS VERIFICATION 2026-09-30]
- **Laser modules are a different risk class.** A 40 W laser in a consumer enclosure is a fire and fume-management concern, not a printing feature. The wiki has no coverage of laser safety; do not treat the "all-in-one" framing as risk-free.
- **Same closed-firmware constraints as every Bambu** [@concepts/bambu-ecosystem-closed-loop.md] — the Klipper / OctoPrint retrofit path does not exist here either.

### Where it sits in the wiki

- Sits above [@entities/printers/x1c.md] (single nozzle, passive enclosure, 256³ mm) and [@entities/printers/p1s.md] (mid-tier) in capability and price.
- [@entities/printers/a1.md] remains the entry bed-slinger; the H2D is not comparable to it.
- The heated chamber is the first Bambu feature that directly strengthens the enclosure-required argument for [@entities/materials/abs.md] / [@entities/materials/asa.md].
- First Bambu **H2D** fabrication datapoint in the wiki: [@sources/2026-qin-cosserat-trimmed-helicoid.md].

**Phase-0:** not applicable — no repo or tool. **Phase-1:** `wont_wire` (3D-printing local wires are off by policy). This page exists for the reader's purchase decision, not for a workflow wire.

## Snippets

> "The H2D's total 3D printing volume for two nozzles comes to 350 x 320 x 325 mm³. The new FDM 3D printer's dual hardened steel nozzles mark a shift from Bambu Lab's previous single-extruder, multi-material 3D printers." [Source: https://3dprintingindustry.com/news/bambu-labs-new-h2d-3d-printer-technical-specifications-and-pricing-237763/ (retrieved 2026-09-30)]

> "At $1,549 you need to be using the dual nozzle, LiDAR or the 40W laser to justify it... The H2D earns its price when the dual nozzle is doing real work: soluble supports and true multi-material parts." [Source: https://bambuhub.net/printers/h2d (retrieved 2026-09-30)]
