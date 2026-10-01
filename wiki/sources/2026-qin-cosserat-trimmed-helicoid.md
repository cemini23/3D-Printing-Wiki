---
title: "Cosserat Modeling of Trimmed Helicoid Soft Arms — separated-section law (arXiv:2609.25264)"
type: source
tags: [paper, soft-robotics, TPU, Bambu, H2D, continuum, modeling, tendon-driven]
keywords: [Cosserat rod, trimmed helicoid, separated-section constitutive law, sparse fusion, GVS, geometric variable strain, tendon-driven, TPU 95A, Bambu H2D, continuum robot, OptiTrack]
related:
  - concepts/soft-robotics-fdm-diw.md
  - entities/materials/tpu.md
  - entities/printers/bambu-h2d.md
  - concepts/fdm-printing.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: deep-read
wire_status: wont_wire
wire_target: "Soft-robotics modeling REFERENCE; 3D-printing Phase-1 local wires off"
---

## Relations

@concepts/soft-robotics-fdm-diw.md @entities/materials/tpu.md @entities/printers/bambu-h2d.md @concepts/fdm-printing.md

## Raw Concept

- **Title:** Cosserat Modeling of Trimmed Helicoid Soft Arms with a Separated-Section Constitutive Law
- **Authors:** Zhihang Qin, Linxin Hou, Zeyu Zhong, Yuchen Sun, Wenci Xin, Yueheng Zhang, Ji Qi, Jie Wang, Muhammad Sunny Nazeer, Yu Jun Tan, Federico Renda, Cecilia Laschi
- **Affiliations:** National University of Singapore (Mechanical Engineering + Advanced Robotics Centre), KU Leuven, Khalifa University
- **Type:** Journal-format paper (IEEE-style, cs.RO)
- **arXiv:** 2609.25264v1 [cs.RO] — 21 Sep 2026
- **Pages:** 8
- **Location:** `raw-sources/arxiv-2609.25264-cosserat-modeling-of-trimmed-helicoid-soft-arms.pdf` — **egress archive pending.** SSH to `cemini-egress-fi` was blocked in this session. Run `bash "../OSINT WORKSPACE/scripts/archive_raw_to_egress.sh" --wiki-id 3d-printing "raw-sources/arxiv-2609.25264-cosserat-modeling-of-trimmed-helicoid-soft-arms.pdf"` from a normal terminal, then update this field.
- **Read-status:** deep-read

## Narrative

A **modeling** paper, not a printing paper — but it matters here for one concrete reason: the validation hardware is **TPU 95A printed on a Bambu Lab H2D**, with rigid **PLA** connectors [Source: 2026-qin-cosserat-trimmed-helicoid.pdf §III.A]. That is a direct datapoint that a current consumer Bambu can produce a working three-section continuum manipulator.

### The modeling problem

**Cosserat rod theory** reduces a soft arm to a one-dimensional backbone. The model needs a **sectional stiffness** — how much force and moment the cross-section returns for a given strain. Standard practice builds that stiffness by **summing material properties over a common cross-section** ("summed-section" baseline).

That assumption breaks for a **trimmed helicoid** arm. A backbone-normal cut through the structure hits **several separate load-bearing helix domains**, and those domains touch only at **sparse fused crossings**. Neighbouring domains can move relative to each other. A single rigid common section cannot represent that [CONFIRMED paper, §I].

### The fix, in two steps

1. **Separated-section mapping.** Each helix domain is evaluated in **its own local frame**, then its constitutive response is **pulled back** to the backbone by energy equivalence, giving an effective backbone stiffness **K_V(s)** — with **no fitted parameter** in it [Source: ...pdf §II.A.1, Eq. 6].
2. **Sparse-fusion correction.** A second term adds the compliance released by relative motion between domains at the fused crossings. This yields per-channel reduction factors **η_c** for bending, torsion, and extension [Source: ...pdf §II.A.2].

### The headline result: strong anisotropy

| Channel | Reduction η_c | Meaning |
|---|---|---|
| Extension | **0.10** | ~10× softer than the rigid-transport value |
| Bending | **0.11** | ~10× softer |
| Torsion | **0.98** | Almost unchanged |

So relaxing the domain-relative motion makes the arm far softer in bending and extension but barely touches torsion. One calibrated scalar (**κ_w**, identified once from a tendon-free hanging test) sets all three channels [CONFIRMED paper, §II.A.2].

### Validation — and a strong ablation

The arm is three tapered trimmed-helicoid modules separated by rigid platforms, tendon-driven, tracked with OptiTrack [Source: ...pdf §III.A].

| Case | Effective sectional law | Summed properties (baseline) |
|---|---|---|
| Deep bend | 1.5–9.7% error | 25.3–91.5% error |
| Combined deformation | ~1.5–2.8% | **83.5–85.7%** |
| Axial contraction | 4.3–10.3% | 74.8–79.7% |

Across **103 measured configurations** (309 platform-pose samples) the pooled normalized position errors were **7.7% / 6.7% / 7.8%** for Datasets 0 / A / B. Both models consumed the **same measured tendon inputs**, so the ablation isolates the constitutive law alone [CONFIRMED paper, §III.C].

### Computational cost

- **n_q = 108** generalized coordinates (3 modules × 30 + 3 transitions × 6).
- **~0.3 s per solve on one CPU core** (Intel Xeon Cascade Lake, 2.8 GHz). Median moves only 0.27 s → 0.31 s as n_q goes 63 → 144 [CONFIRMED paper, §III.E].

That is fast enough for model-based planning and state estimation, which is the authors' stated payoff [Source: ...pdf §IV].

### Notable method details

- **Geometric saturation:** large bending closes the gaps between domains. A **0.10 mm** compaction threshold (prescribed from lattice geometry, not fitted) locks that section's strain coordinates — an approximation of section locking without a contact model [Source: ...pdf §II.B.3].
- **Routed-tendon actuation** with channel friction: tension decays as T(s) = T₀·e^(−µ_c·Θ(s)), µ_c = 0.15 (band 0.10–0.20) [Source: ...pdf §II.B.2].
- Simulation used E = 30 MPa, ν = 0.48 [Source: ...pdf §II.A.2].
- Integration by fourth-order **Zanna–Magnus** [Source: ...pdf §II.B.4].

### What is weak / open

- The **local material response is assumed small-strain** even though the arm bends deeply. The authors state this assumption explicitly [Source: ...pdf §II.A.2].
- Off-diagonal sectional couplings are **neglected**, and transverse shear is treated as **rigid** — both stated simplifications, not validated claims [Source: ...pdf §II.A.2].
- The fusion scalar κ_w is calibrated on **one** hanging configuration. The paper notes no tendon-driven configuration was used for sectional fitting, which limits overfitting but also means the correction rests on a single measurement [Source: ...pdf §III.B].

### Where this sits in the wiki

- Extends the **soft-robotics cluster** [@concepts/soft-robotics-fdm-diw.md] with its first **modeling** entry — the rest of the cluster is fabrication and sensing.
- Directly extends [@sources/2026-hansen-tendon-actuated-tpu-backbone.md] (tendon-actuated **tapered TPU** continuum arm, also Cosserat-based). Hansen uses a tapered solid backbone; Qin uses a trimmed-helicoid lattice. Same problem class, two backbones.
- Is the **first source in this wiki that used a Bambu H2D** — see [@entities/printers/bambu-h2d.md].
- TPU 95A as a structural continuum material ties to [@entities/materials/tpu.md].

**Phase-0:** no repository, no code release. **REFERENCE** only. **Phase-1:** `wont_wire` (3D-printing local wires are off by policy).

## Snippets

> "Across 103 measured configurations, the three datasets give pooled normalized position errors of 7.7%, 6.7%, and 7.8%, while each full-arm solve requires approximately 0.3 s on one CPU core" [Source: 2026-qin-cosserat-trimmed-helicoid.pdf p.1]

> "The experimental platform consists of three tapered trimmed helicoid modules printed from TPU 95A using a Bambu Lab H2D printer, with rigid PLA connectors and mounting components." [Source: 2026-qin-cosserat-trimmed-helicoid.pdf p.6]

> "summed properties systematically overestimate the sectional stiffness and strongly underpredict all three deformation modes." [Source: 2026-qin-cosserat-trimmed-helicoid.pdf p.6]
