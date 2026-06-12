---
title: Industrial AM — Monitoring, Smart Factories, and Metal Processes
type: concept
tags: [industrial, LPBF, SLS, smart-factory, ML, background]
keywords: [SFE, noise-aware optimization, SLS control, CFRC-AM, cementitious extrusion]
related:
  - concepts/print-farm-operations.md
  - concepts/print-job-scheduling.md
  - concepts/fault-detection.md
  - concepts/extrusion-control.md
  - concepts/fdm-printing.md
  - sources/2025-leet-ts-aces-smart-factory.md
  - sources/2025-schenka-noise-aware-parallel-optimization.md
  - sources/2025-toshani-sls-laser-power-noise.md
  - sources/2025-liang-microscale-sls-cu-uv.md
  - sources/2025-parvaresh-cfrc-am-se-wdnn.md
  - sources/2026-mohammadi-rce-lqr-extrusion.md
  - sources/2025-khod-xray-ct-am-protocol-ai.md
  - sources/2025-banerjee-neuromorphic-lpbf.md
  - sources/2026-pelaez-stgt-lpbf-quality-prediction.md
  - concepts/volumetric-additive-manufacturing.md
maturity: draft
created: 2026-06-01
updated: 2026-06-12
---

## Relations

@concepts/print-farm-operations.md @concepts/print-job-scheduling.md @concepts/fault-detection.md @concepts/extrusion-control.md @concepts/fdm-printing.md @sources/2025-leet-ts-aces-smart-factory.md @sources/2025-schenka-noise-aware-parallel-optimization.md @sources/2025-toshani-sls-laser-power-noise.md @sources/2025-liang-microscale-sls-cu-uv.md @sources/2025-parvaresh-cfrc-am-se-wdnn.md @sources/2026-mohammadi-rce-lqr-extrusion.md @sources/2025-khod-xray-ct-am-protocol-ai.md @sources/2025-banerjee-neuromorphic-lpbf.md @sources/2026-pelaez-stgt-lpbf-quality-prediction.md

## Raw Concept

Ingest pass 13 — smart-factory formal methods, farm-scale noise modeling, SLS/LPBF/metal/composite AM beyond hobby FFF. Updated 2026-06-12 with graph-transformer LPBF quality prediction (@sources/2026-pelaez-stgt-lpbf-quality-prediction.md).

## Narrative

Bridges @concepts/print-farm-operations.md (heuristic fleet ops) with **formal** (@sources/2025-leet-ts-aces-smart-factory.md) and **statistical** (@sources/2025-schenka-noise-aware-parallel-optimization.md) factory-scale methods. Metal/SLS/LPBF papers are **background** — reader with one FDM machine can ignore until scaling.

### LPBF in-situ monitoring — two 2025–2026 angles

| Paper | Sensing | Model | Key metric |
|-------|---------|-------|------------|
| @sources/2025-banerjee-neuromorphic-lpbf.md | Photodiode (plasma + IR) | Spiking NN on Intel Loihi | Anomaly on laser energy drop |
| @sources/2026-pelaez-stgt-lpbf-quality-prediction.md | Coaxial melt-pool camera | STGT (dual-attention graph transformer) | R² 0.719 with cross-layer 3D neighborhood |

Pelaez et al. (arXiv 2606.10227) argues image/sequence models underperform because they ignore **cross-layer thermal history**. Their weighted k-NN graph connects fusing points in 3D; STGT's neighborhood attention peaks on the immediately preceding layer (layer offset +1), matching physical reheating intuition. Evaluated on NIST AMS 100-69 overhang benchmark (88k fusing locations, micro-XCT ground truth). [TENTATIVE] Single benchmark geometry — transfer to other parts unproven.

Contrast with consumer FDM (@concepts/fault-detection.md): Bambu's stack is gross-failure classification on enclosure camera + lidar; this LPBF work targets **spatially resolved ex-situ quality regression** from melt-pool dynamics — factory QA tier, not spaghetti detection.

## Snippets

(none — synthesis page)
