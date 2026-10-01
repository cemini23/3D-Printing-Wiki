---
title: "Monolithic Force-Proprioception Soft Actuator — single-material FDM (arXiv:2609.24499)"
type: source
tags: [paper, soft-robotics, TPU, FDM, pneumatic, conductive, origami]
keywords: [MFPS, conductive TPU, force proprioception, AOB chamber, Yoshimura origami, self-sensing actuator, FPS sensor, Raise3D Pro2 Plus, hysteresis]
related:
  - concepts/soft-robotics-fdm-diw.md
  - entities/materials/tpu.md
  - concepts/fdm-printing.md
  - concepts/shape-changing-fdm-interfaces.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: deep-read
wire_status: wont_wire
wire_target: "Soft-robotics research REFERENCE; 3D-printing Phase-1 local wires off"
---

## Relations

@concepts/soft-robotics-fdm-diw.md @entities/materials/tpu.md @concepts/fdm-printing.md @concepts/shape-changing-fdm-interfaces.md

## Raw Concept

- **Title:** A Monolithic Force-Proprioception Soft Actuator Enabled by Single-Material 3D printing
- **Authors:** Nan Huang, Lele Liu, Junfeng Lu, Yipan Zhu, Jiansheng Dai, Sicong Liu (Southern University of Science and Technology + Shenzhen Technology University)
- **Type:** Conference-format paper (IEEE-style, cs.RO)
- **arXiv:** 2609.24499v1 [cs.RO] — 21 Sep 2026
- **Pages:** 8
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2609.24499-a-monolithic-force-proprioception-soft-acutuator.pdf`
- **Read-status:** deep-read

## Narrative

The paper builds a **pneumatic soft actuator that senses its own grip force** — and prints the whole thing from **one material on one FDM printer**. Actuation and sensing live in the same continuous body, so there is no glued-on sensor and no multimaterial interface.

The problem it attacks: soft actuators normally get sensing by **attaching** a sensor to the surface or **embedding** one inside. Both need extra assembly. Multimaterial printing solves the assembly problem but creates a new one — the joint between stiff and soft material concentrates stress and needs a printer that can handle both materials [CONFIRMED paper, §I].

### The two modules

| Module | Role | Principle |
|---|---|---|
| **AOB chamber** (Asymmetric Origami Bending) | Actuation — bends under air pressure | Derived from the **Yoshimura origami** pattern; asymmetric creases on opposite sides unfold unequally, which forces a bend |
| **FPS sensor** (Force-Proprioception Soft) | Sensing — reports grip force | **Conductive TPU**: squeezing it changes the spacing of conductive particles, which changes resistance |

The AOB chamber reuses a design the same group published earlier [Source: 2026-huang-mfps-monolithic-force-proprioception.pdf §III.A, ref [29]].

### The sensing mechanism

Resistance rises as the structure compresses. Because plain solid TPU barely strains, the paper tests **three sensor geometries** and picks the one that concentrates strain [CONFIRMED paper, §III.C]:

| Design | Form | Max strain (sim, 95 N) | Result |
|---|---|---|---|
| FPS-1 | Solid cuboid | 0.019 | Nearly no response — **rejected** |
| FPS-2 | Zigzag | 0.058 | Strong 0–10 N response, but only ~1.8% resistance change — noise-prone |
| **FPS-3** | **Creased contact surface** | **0.079** | **35% resistance change, widest working range — selected** |

All three were tuned to the same **1 g** of material, so the comparison is like-for-like [CONFIRMED paper, §III.C].

Simulation used **Abaqus 2020** with hexahedral C3D8R elements under a 95 N load [Source: ...pdf §III.C].

### Headline numbers

| Quantity | Value | Note |
|---|---|---|
| Bending angle | −10° at 50 kPa → 30° at 220 kPa | Abstract/conclusion state 40°; the 40° is the **total swing** across that pressure range [TENTATIVE — reconciliation inferred, paper does not say so explicitly] |
| Output force | 12.5 N at 300 kPa | Linear with pressure |
| Resistance change | 26.9% (0 → 45 N) | 0.5 MΩ |
| Zero drift | 0.05% no-load (0.01 MΩ) | Rises to 5.0% / 5.6% at 16 N / 26 N |
| Repeatability error | ~7% minimum | Across geometric sweeps |
| Effective working zone | up to [1.0 N, 86.3 N] at m = 4 | Grows ~linearly with unit count m |
| Airtightness | 10 / 6 / 6 kPa drop over 120 s | At 220 / 160 / 50 kPa |
| Gripper grip force | ~12 N at 220 kPa | 2-finger; 0–90 mm range; 21.5% resistance change |

### Fabrication — the part a printer owner will care about

Printed on a **Raise3D Pro2 Plus** with **commercial conductive TPU** filament, using a **purpose-designed support structure**. The authors report a real FDM trade-off [CONFIRMED paper, §IV.A]:

- **Lower fan speed and smaller layer height improve airtightness** of the pressure chamber.
- **Too low a fan speed** → extruded material does not solidify in time.
- **Too small a layer height** → the nozzle drags the print; the **weak sensor region moves with the nozzle** and the sensor fails.

So the two goals pull against each other. The paper's own failure photo shows FPS sensor print failure and loss of sensing function [Source: ...pdf §IV.A, Fig. 4(c)].

### What is weak

**Hysteresis.** TPU is viscoelastic, so the resistance response lags the force. The authors suppress it partly by changing geometry (the w = 3 sample) but call the residual hysteresis out as unfinished work [CONFIRMED paper, §VI]. They also leave open how the AOB chamber affects sensing once integrated [Source: ...pdf §VI].

**Not consumer hardware.** A Raise3D Pro2 Plus is a prosumer machine, and conductive TPU is a specialty filament — not a Bambu day-1 spool. Treat this as a **method reference**: single-material self-sensing is a viable pattern, and the geometric strain-concentration trick (FPS-3) is the transferable idea.

### Where this sits in the wiki

- Continues the **soft-robotics cluster** [@concepts/soft-robotics-fdm-diw.md] — and is the first entry there to use **single-material** printing rather than multimaterial or DIW.
- Adjacent to [@sources/2026-abboodi-airtight-spa-fdm.md] (FDM TPU airtightness) — same problem (sealing a printed pressure chamber), different route. Abboodi varies **wall-line architecture**; Huang varies **fan speed and layer height**. Neither is a consumer-printable recipe yet.
- Uses **conductive TPU** for sensing, like [@sources/2025-yoshimura-m3d-skin-tactile-fdm.md] — but M3D-skin needs multimaterial FDM, whereas this is single-nozzle.
- Sits beside [@sources/2026-hansen-tendon-actuated-tpu-backbone.md] as a TPU soft-robot with an integrated sensing story (Hansen: tendon tension; Huang: grip force).

**Phase-0:** no repository, no code, no dataset. **REFERENCE** only — nothing adoptable. **Phase-1:** `wont_wire` (3D-printing local wires are off by policy).

## Snippets

> "The MFPS actuator achieves a bending angle of 40°, an output force of 12.5 N, and a resistance change of 26.9% as the applied external force increased from 0 to 45 N." [Source: 2026-huang-mfps-monolithic-force-proprioception.pdf p.1]

> "a lower fan speed and smaller layer height are beneficial for improving the airtightness of the actuator, an excessively low fan speed prevents the extruded material from solidifying in time, while an excessively small layer height increases the friction between the nozzle and the printed material, causing the relatively weak sensor region to move with the nozzle during printing." [Source: 2026-huang-mfps-monolithic-force-proprioception.pdf p.5]

> "the FPS sensor exhibits noticeable hysteresis, and further investigation is required to reduce the hysteresis through geometric design." [Source: 2026-huang-mfps-monolithic-force-proprioception.pdf p.7]
