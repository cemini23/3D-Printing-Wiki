---
title: Spatiotemporal Graph Transformer for LPBF Quality Prediction
type: source
tags: [paper, LPBF, graph-transformer, quality-monitoring, industrial, background]
keywords: [2606.10227, STGT, melt-pool, NIST AMMT, graph neural network, cross-layer interaction]
related:
  - concepts/industrial-am-monitoring.md
  - concepts/fault-detection.md
  - sources/2025-banerjee-neuromorphic-lpbf.md
maturity: draft
created: 2026-06-12
updated: 2026-06-12
read_status: skimmed
---

## Relations

@concepts/industrial-am-monitoring.md @concepts/fault-detection.md @sources/2025-banerjee-neuromorphic-lpbf.md

## Raw Concept

- Authors: Joyce Karen Pelaez, Siqi Zhang*, Hoo Sang Ko (Southern Illinois University Edwardsville)
- arXiv: 2606.10227v1 (cs.LG), 8 Jun 2026
- Location: `raw-sources/2026-pelaez-stgt-lpbf-quality-prediction.pdf`
- Retrieved: from `research to be indexed/` 2026-06-12
- Read-status: skimmed (abstract + methodology + results + conclusion)

## Narrative

Industrial **LPBF / metal powder bed fusion** quality monitoring paper — not consumer FDM. Proposes **STGT (spatiotemporal graph transformer)** for pointwise ex-situ quality prediction from in-situ melt-pool images.

**Problem:** Layerwise melting/solidification/reheating creates 3D thermal history; pointwise quality at a fusing location depends on neighbors in prior layers, not just local melt-pool snapshots. Image-only (ViT) and sequence (ViViT) models miss cross-layer coupling.

**Method (two parts):**
1. **Weighted k-NN network** — each fusing point is a node; edges weighted by spatial proximity (Gaussian on 3D distance / hatching space) × process similarity (Gaussian on laser power, scan speed vectors). k-NN chosen over fixed-radius balls to keep degree tractable (avg degree 20.39 at k≈1 hatching space vs 139.06 at 2× radius on benchmark).
2. **Dual-attention STGT** on 1-hop neighborhood subgraphs per query node: (a) within-node patch self-attention on melt-pool image tokens, (b) cross-node neighborhood attention with graph-spectral node positional encodings. Future-layer nodes excluded at inference (only past layers available in-situ).

**Benchmark:** NIST AMS 100-69 overhang part (Lane & Yeung 2020; Yang et al. 2025) — 16 layers, 88,825 fusing locations; melt-pool coaxial camera + registered micro-XCT ex-situ quality targets; train/val/test on layers 31–38 / 39–42 / 43–46.

**Headline results (R² on test set):**
| Setting | GAT | STGT (ours) |
|---------|-----|-------------|
| Within-layer only | 0.471 | 0.451 |
| Within + cross-layer | 0.587 | **0.719** |

Cross-layer interactions lift STGT R² by +0.268 vs within-only; GAT gains +0.116. Best STGT config: neighborhood size 20, node PE dim 30 under cross-layer setting. Attention weights peak at layer offset +1 (immediately preceding layer), decaying with distance — physically plausible thermal-history emphasis. Region-wise RMSE drops up to **45.98%** in geometric-transition zones when cross-layer context is added.

**Reader relevance:** Background for factory-tier LPBF monitoring research trajectory. Complements @sources/2025-banerjee-neuromorphic-lpbf.md (SNN on photodiode) and @concepts/fault-detection.md industrial branch. No Bambu/FFF action item.

## Snippets

> "In this paper, we develop a novel spatiotemporal graph transformer for modeling 3D neighborhood interactions and learn their effects on build quality in metal additive manufacturing."
[Source: 2026-pelaez-stgt-lpbf-quality-prediction.pdf p.1]

> "For STGT, [R²] increases more substantially from 0.451 to 0.719. This can be largely attributed to the introduction of node positional encoding as additional structural details."
[Source: 2026-pelaez-stgt-lpbf-quality-prediction.pdf p.16]

> "The median of the attention weight increases from layer offset 0 to layer offset 1, and then gradually decreases as the layer offset further increases."
[Source: 2026-pelaez-stgt-lpbf-quality-prediction.pdf p.17]
