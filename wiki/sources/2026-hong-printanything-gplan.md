---
title: "PrintAnything: Geometric Plan Map for Point-Cloud → G-code (mesh-free)"
type: source
tags: [paper, AI, G-code, point-cloud, FDM, Bambu, PrusaSlicer, Slice-100K]
keywords: [PrintAnything, G-plan map, occupancy region flow, Point Transformer V3, mesh-free slicing, Hong, SNU, Kairoba, unoriented point cloud]
related:
  - entities/tools/printanything.md
  - concepts/ai-design-tools.md
  - concepts/novice-cad-workflows.md
  - concepts/fdm-printing.md
  - entities/slicers/bambu-studio.md
  - entities/printers/x1c.md
  - concepts/self-improving-cad-generation-agents.md
maturity: draft
created: 2026-07-31
updated: 2026-07-31
read_status: skimmed
---

## Relations

@entities/tools/printanything.md @concepts/ai-design-tools.md @concepts/novice-cad-workflows.md @concepts/fdm-printing.md @entities/slicers/bambu-studio.md @entities/printers/x1c.md @concepts/self-improving-cad-generation-agents.md

## Raw Concept

- **Title:** PrintAnything: Learning Geometric Plan Map for 3D Printing G-code Generation from Unoriented Point Clouds (arXiv HTML title variant: Intermediate Representation for G-code Generation)
- **Authors:** Sangmin Hong, Daniel Sungho Jung, Heewon Kim (Soongsil / Kairoba), Kyoung Mu Lee (SNU)
- **Type:** arXiv preprint, arXiv:2607.27729v1 [cs.CV]
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2607.27729-printanything-learning-an-intermediate-represent.pdf`
- **Retrieved:** 2026-07-31 overnight digest
- **Pages:** 32
- **Read-status:** skimmed (abstract, method, Slice-100K tables, X1C real prints, limitations/societal, code availability)
- **Claimed code:** https://github.com/Sangminhong/PrintAnything — **empty stub as of 2026-07-31** (README title only; size 0; no LICENSE)

## Narrative

**Problem:** FDM slicers want watertight meshes. Point clouds (LiDAR, RGB-D, generative 3D) are common but incompatible; mesh reconstruction often injects holes / bad topology that break slicing. [CONFIRMED — §1]

**PrintAnything** predicts a slice-wise **Geometric plan (G-plan) map** — occupancy `M`, region `R`, flow `Q` at 256×256 — then a deterministic compiler emits perimeters + infill G-code. Mesh reconstruction is skipped. Encoder: Point Transformer V3; per-slice U-Net with FiLM height conditioning; multi-slice context. Trained on **Slice-100K** (STL + GT G-code). [CONFIRMED — §3–4]

### Quantitative (Slice-100K held-out) [CONFIRMED — Table 1]

| Method | CD↓ | F1₃D↑ | F1₂D↑ |
|--------|-----|-------|-------|
| Poisson → PrusaSlicer | 0.088 | 0.682 | 0.587 |
| DWG → PrusaSlicer | 0.062 | 0.712 | 0.496 |
| MeshAnything → PrusaSlicer | 0.157 | 0.480 | 0.356 |
| **PrintAnything (G-plan)** | **0.047** | **0.741** | **0.677** |

Multi-slice conditioning: CD 0.059→0.047 (−20.3%). Mean inference **0.33 s** (vs Poisson ~124 s, MeshAnything ~114 s). [CONFIRMED — Tables 2, S1]

### Real hardware [CONFIRMED — §5.8]

Authors print raw generated G-code on a **Bambu Lab X1 Carbon** with no post-edit; show gears / thin structures. Simulation preview uses PrusaSlicer. [TENTATIVE] single-lab printer set; physics / material inductive bias explicitly **not** modeled (§S11).

### Wiki / safety posture

This pipeline **emits executable G-code** — directly conflicts with the audit’s hallucinated-G-code red line on [@concepts/ai-design-tools.md]. Treat as research demonstration of a **structured intermediate + deterministic compiler** pattern, **not** a hobby/day-1 tool. Friend / Flashforge: **NO-GO** — never run unreviewed model G-code. Prefer mesh/3MF → Orca-Flashforge / Bambu Studio.

### Phase-0 (2026-07-31)

| Check | Result |
|-------|--------|
| Repo | Stub only — no weights, no code, no LICENSE |
| Cloud / GPU | Paper: Quadro RTX 8000 train; inference claimed fast once model exists |
| Failure mode | Empty release; raw G-code risk; no physics bias; misuse called out by authors |
| Friend / store | **NO-GO** |
| Verdict | **REFERENCE** |
| Local adopt (&lt;500 MB) | **Skipped** — nothing substantive to clone |

## Snippets

> "we propose PrintAnything, a novel framework that learns to produce executable 3D printing G-code directly from 3D point clouds without requiring mesh reconstruction."
[Source: arXiv:2607.27729v1 abstract]

> "All objects were fabricated using a Bambu Lab X1-Carbon printer without any additional post-processing of the generated G-code"
[Source: arXiv:2607.27729v1 §5.8]

> "automated generation of printable G-code from geometric inputs could be exploited to produce unauthorized or harmful objects"
[Source: arXiv:2607.27729v1 §S11]
