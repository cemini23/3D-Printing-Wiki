---
title: "Unified geometric design framework for kirigami (arXiv:2608.30032)"
type: source
tags: [paper, kirigami, metamaterials, shape-morphing, computational-design, soft-matter]
keywords: [kirigami, rotating squares, compact reconfigurability, rigid deployability, IPM, PyKirigami, TPU, 2D-to-3D, 3D-to-3D]
related:
  - concepts/shape-changing-fdm-interfaces.md
  - entities/tools/pykirigami.md
  - sources/2026-li-duomorph-fdm-pneumatic.md
  - sources/2025-iqbal-single-material-4d-pvp.md
  - sources/2026-abboodi-airtight-spa-fdm.md
  - concepts/novice-cad-workflows.md
maturity: draft
created: 2026-09-01
updated: 2026-09-01
read_status: skimmed
wire_status: wont_wire
wire_target: "3D-printing Phase-1 local wires off; PyKirigami REFERENCE only"
---

## Relations

@concepts/shape-changing-fdm-interfaces.md @entities/tools/pykirigami.md @sources/2026-li-duomorph-fdm-pneumatic.md @sources/2025-iqbal-single-material-4d-pvp.md @sources/2026-abboodi-airtight-spa-fdm.md @concepts/novice-cad-workflows.md

## Raw Concept

- **Title:** A unified geometric design framework for kirigami structures
- **Authors:** Qinghai Jiang, Gary P. T. Choi (Department of Mathematics, The Chinese University of Hong Kong)
- **arXiv:** 2608.30032 [cond-mat.soft]
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2608.30032-a-unified-geometric-design-framework-for-kirigam.pdf`
- **Retrieved:** 2026-09-01 ingest pass 31 (overnight digest)
- **Pages:** 25 (+ SI)
- **Read-status:** skimmed (abstract, methods §II, results §III, theory §IV, discussion §V, SI appendix skim)

## Narrative

Computational **inverse kirigami design** paper — not a slicer or printer workflow. Jiang & Choi unify prior case-specific kirigami methods into one **length-based constrained optimization** framework that solves for vertex coordinates in **multiple target states simultaneously** (compact, deployed, reconfigured compact). Topology focus: **quadrilateral tiles with rotating-squares kirigami** (standard slits + cutting angles). Solver: **interior-point method (IPM)** on sparse KKT systems; five edge-length equalities per quad (sixth diagonal omitted to avoid KKT singularity — proved in SI Appendix A).

### What the framework covers

| Morphing class | Example (paper) | Extra constraints |
|----------------|-----------------|-------------------|
| **2D→2D** | Circle→rainbow; rainbow→square; square→circle | Rigid deployability; compact reconfigurability |
| **2D→3D** | Rectangle→human face cap; half-vase negative space | Planarity constraints on 3D deployed tiles |
| **3D→3D** | Cube→sphere (six 2D→3D patches); square ring→torus; spherical cap↔saddle | Symmetry assembly; direct 3D vertex optimization |

Optional properties encoded as constraints: **compact reconfigurability** (two compact states linked by checkerboard ±π/2 tile rotation), **rigid deployability** (slit collinearity + angle inequalities so tiles rotate without deformation).

### Headline theory [CONFIRMED paper §IV]

- **Inertia transposition law** — for compact-reconfigurable patterns, central second moments transpose between two compact states (checkerboard rotation); yields **aspect-ratio law** linking compact rectangle W:H to target shape inertia ratio r_in.
- **Angle-defect limits** — positive-curvature 3D compact targets cannot maintain rectangular planar compact boundaries; e.g. **compact-cube→compact-sphere is impossible** via the Fig. 5a assembly trick (§IV).
- **Finite-grid correction** — non-square M×N resolutions need Corollary IV.5 fluctuation terms; square grids simplify to r_in(Ω1)r_in(Ω2) → 1 at high resolution.

### Physical validation [CONFIRMED §III Fig. 3e]

One **2D square→circle** rigid deployable + compact reconfigurable pattern was **fabricated in TPU by FDM** — small joints between adjacent tile corners, no film/heat-seal step. Demonstrates kinematics only; paper is **design/simulation-first**, not a consumer print recipe.

### Companion software

Deployment simulation cites **PyKirigami** [@entities/tools/pykirigami.md] (Apache-2.0; same author group; arXiv:2508.15753). **No code URL in this paper** for the optimization framework itself.

### Reader / wiki posture

| Audience | Verdict |
|----------|---------|
| Friend / Flashforge day-1 | **NO-GO** — research CAD + custom jointed sheets; see @concepts/novice-cad-workflows.md |
| Shape-changing hub | **Background** — complements PvP SMP and DuoMorph pneumatics as *computational metamaterial design* |
| Etsy / store | **NO-GO** — R&D-heavy; no turnkey toolchain |

### Phase-0 (2026-09-01)

| Check | Result |
|-------|--------|
| This paper's code | **None** cited for optimizer |
| PyKirigami | **GO REFERENCE** — Apache-2.0, ~29 MB, 16★; simulation only |
| Friend / store | **NO-GO** |
| Verdict | **REFERENCE** (design math + TPU demo) |
| Local adopt | Skip optimizer clone; PyKirigami optional REFERENCE shelf |
| Phase-1 | **wont_wire** — 3D-printing local harness wires off |

## Snippets

> "we develop a unified framework for kirigami design that encompasses a wide range of 2D-to-2D, 2D-to-3D, and 3D-to-3D shape-morphing effects"
[Source: arXiv:2608.30032 abstract]

> "The physical model is fabricated using TPU (Thermoplastic Polyurethane) 3D printing, with a small portion between the corners of adjacent tiles kept as joints."
[Source: arXiv:2608.30032 §III Fig. 3e caption]

> "a compact rectangular kirigami pattern cannot be reconfigured into an arbitrary (positively curved) surface with all vertices lying exactly on the target geometry"
[Source: arXiv:2608.30032 §IV angle-defect discussion]
