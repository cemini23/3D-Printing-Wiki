---
title: Soft Robotics — FDM, DIW, and Tactile Tooling
type: concept
tags: [soft-robotics, DIW, tactile, TPU, advanced]
keywords: [soft hand, tendon robot, DIW sensors, 3D Cal, ionic actuator]
related:
  - concepts/open-source-legged-robotics.md
  - concepts/fdm-printing.md
  - entities/materials/tpu.md
  - sources/2025-miyama-soft-hand-skin-skeleton.md
  - sources/2026-hansen-tendon-actuated-tpu-backbone.md
  - sources/2025-clancy-magnetic-soft-microrobots.md
  - sources/2025-truempler-ionic-polymer-diw.md
  - sources/2025-cha-diw-stretchable-strain-sensors.md
  - sources/2025-kota-3d-cal-tactile-calibration.md
  - sources/2025-yoshimura-m3d-skin-tactile-fdm.md
  - sources/2025-pattabiraman-eflesh-magnetic-tactile.md
  - concepts/fdm-research-tools.md
  - sources/2026-mohammadi-rce-lqr-extrusion.md
  - sources/2026-luo-multimaterial-e2e-optimization.md
  - sources/2026-chen-hybrid-rigid-soft-gripper.md
  - sources/2026-abboodi-airtight-spa-fdm.md
  - sources/2026-jang-monorigami-sla-origami-pneumatic.md
  - sources/2026-hebbalmanjunath-prc-pneumatic-soft-arm.md
  - sources/2026-kashef-multi-vine-working-channel.md
  - sources/2026-huang-mfps-monolithic-force-proprioception.md
  - sources/2026-qin-cosserat-trimmed-helicoid.md
  - entities/printers/bambu-h2d.md
  - sources/2026-zhong-pneutac-mpm-gaussian-tactile.md
maturity: draft
created: 2026-06-01
updated: 2026-10-03
---

## Relations

@sources/2026-chen-hybrid-rigid-soft-gripper.md @sources/2026-luo-multimaterial-e2e-optimization.md @sources/2026-abboodi-airtight-spa-fdm.md @sources/2026-jang-monorigami-sla-origami-pneumatic.md @sources/2026-hebbalmanjunath-prc-pneumatic-soft-arm.md @sources/2026-kashef-multi-vine-working-channel.md @sources/2026-huang-mfps-monolithic-force-proprioception.md @sources/2026-qin-cosserat-trimmed-helicoid.md @entities/printers/bambu-h2d.md @sources/2026-zhong-pneutac-mpm-gaussian-tactile.md @concepts/open-source-legged-robotics.md @concepts/fdm-printing.md @entities/materials/tpu.md @sources/2025-miyama-soft-hand-skin-skeleton.md @sources/2026-hansen-tendon-actuated-tpu-backbone.md @sources/2025-clancy-magnetic-soft-microrobots.md @sources/2025-truempler-ionic-polymer-diw.md @sources/2025-cha-diw-stretchable-strain-sensors.md @sources/2025-kota-3d-cal-tactile-calibration.md @sources/2025-yoshimura-m3d-skin-tactile-fdm.md @sources/2025-pattabiraman-eflesh-magnetic-tactile.md

## Raw Concept

Ingest pass 11 — extends pass 9 (@concepts/open-source-legged-robotics.md) with soft hands, continuum TPU robots, DIW sensors/actuators, and **3D Cal** calibration tooling.

## Narrative

### Fabrication modalities

| Modality | Examples | Hobbyist fit |
|----------|----------|--------------|
| **Single-material flexible FDM** | Soft hand skin-skeleton | Advanced |
| **Single-material self-sensing FDM** | Conductive-TPU actuator + sensor (MFPS) | Research only — conductive TPU + prosumer printer |
| **TPU FDM structure** | Tendon continuum backbone; trimmed-helicoid arm on Bambu H2D | Advanced + TPU skill |
| **Airtight TPU pneumatics** | Abboodi SPA process eval | Research only — lab window |
| **Multi-material FDM sensing** | M3D-skin, eFlesh (pass 9) | MMU or pause-insert |
| **DIW on silicone** | Cha strain sensors; Trümpler ionic actuators | Custom hardware |
| **PolyJet soft body + tactile tip** | PneuTac soft finger (Agilus30 + Digit) | **Not FDM** — PolyJet machine class |
| **Printer as robot** | 3D Cal probing | Clever repurposing |

### 3D Cal pattern [CONFIRMED single source]

@sources/2025-kota-3d-cal-tactile-calibration.md — use desktop printer as **motion stage** for calibration data collection, not just part fabrication.


### Hybrid rigid–soft gripper (2026-07)

@sources/2026-chen-hybrid-rigid-soft-gripper.md — agricultural gripper with membrane pneumatics + **FDM/AM ratchet–pawl self-locking**; PLA spheres for bench tests. **REFERENCE** only (no public BOM). Complements multimaterial topology work (@sources/2026-luo-multimaterial-e2e-optimization.md).

### Airtight TPU pneumatic FDM (2026-08)

@sources/2026-abboodi-airtight-spa-fdm.md — uOttawa process evaluation of **five routes** for a complex airtight SPA (heat-shrink / silicone casting / powder AM / DLP / FDM). **FDM TPU retained** because its dominant defects were correctable. Headline [CONFIRMED paper]: a **0.96 mm wall from three 0.32 mm lines sealed better than a 1.6 mm wall from two 0.8 mm lines** — extrusion-path architecture matters more than nominal thickness (mechanism [TENTATIVE]). Bowden (Ultimaker pair) worked **with conditioning** — a nuance vs the direct-drive default in @entities/materials/tpu.md. Phase-0 **REFERENCE**; do not copy the Ultimaker lab window to consumer printers.

### Pass 32 cluster (2026-09-11) — origami SLA, PRC sensing, vine robots

| Paper | Stack | Verdict |
|-------|-------|---------|
| @sources/2026-jang-monorigami-sla-origami-pneumatic.md | **SLA** (Form 3 + Flexible 80A) monolithic origami vacuum actuators; composable multi-DoF | **REFERENCE** — not FDM; adjacent to kirigami + DuoMorph pneumatics |
| @sources/2026-hebbalmanjunath-prc-pneumatic-soft-arm.md | Fabric arm; sealed vs coupled pouch topology for PRC state estimation | **REFERENCE** — sensing architecture background |
| @sources/2026-kashef-multi-vine-working-channel.md | Dual eversion vines + external tool channel; colon phantom steering | **REFERENCE** — medical vine robots; not AM |

### Pass 34 cluster (2026-09-30) — single-material self-sensing, and a Cosserat arm on an H2D

| Paper | Stack | Verdict |
|-------|-------|---------|
| @sources/2026-huang-mfps-monolithic-force-proprioception.md | **FDM**, commercial **conductive TPU**, Raise3D Pro2 Plus. One material, one step: origami (AOB) pneumatic chamber + resistance-based force sensor | **REFERENCE** — prosumer printer + specialty filament; the transferable idea is **geometric strain concentration**, not the recipe |
| @sources/2026-qin-cosserat-trimmed-helicoid.md | **TPU 95A on a Bambu Lab H2D** + PLA rigid connectors; three-module tendon-driven continuum arm | **REFERENCE** — a **modeling** paper; notable here as the wiki's first **Bambu H2D** fabrication datapoint |

**Single-material self-sensing (Huang).** The paper's contribution is closing the assembly step: no glued-on or embedded sensor, no multimaterial interface, no stress concentration at a material joint. Sensing comes from **conductive TPU** whose particle spacing — and therefore resistance — changes under compression. The design lesson is that a solid block barely strains (FPS-1 gave almost no signal, max strain 0.019); a **creased contact surface** (FPS-3, max strain 0.079) gave **35%** resistance change and won. Same 1 g of material across all three designs. Main weakness: **TPU hysteresis** — the authors call it unfinished.

FDM process tension worth noting: **lower fan speed and smaller layer height improve airtightness**, but too-low fan speed prevents solidification and too-small layer height lets the nozzle **drag the weak sensor region** and destroy it. That is the same sealing problem @sources/2026-abboodi-airtight-spa-fdm.md attacks from the **wall-line architecture** side — two papers, one problem, no consumer-ready recipe yet.

**Cosserat arm on a Bambu H2D (Qin).** Not a printing paper, but its validation rig is: three tapered **trimmed-helicoid** modules printed in **TPU 95A on a Bambu Lab H2D**, with rigid **PLA** connectors [@entities/printers/bambu-h2d.md]. The modeling result that matters conceptually: if you assume a **common cross-section** (the standard "summed properties" approach), you overestimate stiffness badly — errors of **25–92%** — because the load-bearing helix domains are separated and slide relative to each other. Modelling them separately drops the error to **~7–8%** across 103 configurations. Bending and extension soften ~10×, torsion barely changes.

### Pass 35 (2026-10-03) — simulating the soft robot and its tactile skin together

@sources/2026-zhong-pneutac-mpm-gaussian-tactile.md (Oxford Robotics Institute) is the cluster's first **simulation / sim-to-real** entry. It couples the **soft body** and the **tactile gel** in one physics model — **MPM** for both dynamics problems, **3D Gaussian Splatting** for rendering — because prior simulators modelled them separately and neither could handle the pair [@sources/2026-zhong-pneutac-mpm-gaussian-tactile.md].

**Process note: this is another non-FDM soft-robotics paper.** The finger was printed on a **Stratasys PolyJet** (Agilus30 soft / Vero rigid), with a **Digit** tactile sensor and an Ecoflex gel. Together with MONORIGAMI (SLA), that is now **two of the last three** soft-robotics papers running on non-FDM hardware — a clear signal that consumer FDM soft robotics remains research-adjacent.

The transferable result is not the simulator. It is what the **comparison table** teaches about when simulation-augmented data actually pays:

| Task | Sim+Real (10 real + 100 sim) | Real only (10) | Real-20 (20 real) | No tactile | PPO |
|---|---|---|---|---|---|
| Switch | 83.3% | 60.0% | **90.0%** | 30.0% | 63.3% |
| Egg carton | **90.0%** | 26.7% | 40.0% | 56.7% | 80.0% |
| Card pulling | **66.7%** | 33.3% | 50.0% | 63.3% | **10.0%** |

**Three lessons, none of them obvious:**

1. **Simulation augmentation is not free lunch — it competes with just collecting more real data.** On the switch task, doubling the real demonstrations (**Real-20, 90.0%**) **beat** the simulation pipeline (83.3%). Simulation won where real data **under-samples the success manifold** (egg, card). So the question is never "is sim useful," but "is my real set already representative?" [CONFIRMED paper, §V.C]
2. **Tactile feedback helps contact-dominated tasks, not position-dominated ones.** Removing it collapsed the switch (83.3 → 30.0%) but barely moved card pulling (66.7 → 63.3%) — card pulling is position-dominated, so touch adds little. Match the sensing modality to what the task actually depends on.
3. **A weak simulator punishes reinforcement learning harder than imitation learning.** PPO scored **10.0%** on card pulling where behaviour cloning scored 66.7%. The cause is the simulator's poor fidelity for **card-on-card contact** — and because PPO explores by reward, it finds and exploits that error, while a BC policy stays anchored on real demonstrations. **If your simulator is wrong about a contact mode, RL will discover it and you will not like what it does.**

Two practical caveats from the same paper: calibration does **not** transfer between sensor units (a second Digit unit scored RMSE 8.12 re-calibrated but **22.96** when reusing the original calibration), and the real-to-sim step still needed only **one** image per device — a genuinely light calibration burden.

## Snippets

(none — synthesis page)
