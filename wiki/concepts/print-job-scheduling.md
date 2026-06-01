---
title: Print Job Scheduling
type: concept
tags: [scheduling, packing, sequential-printing, parallel-printing, optimization, FDM]
keywords: [SEQ-PACK+S, sequential printing, parallel decomposition, AABB, mesh decomposition, Z3, SMT, CEGAR, PrusaSlicer, Parallelobox, multi-color, AMS, fail-safe]
related:
  - concepts/print-farm-operations.md
  - concepts/fdm-printing.md
  - sources/2025-surynek-sequential-printing-cegar.md
  - sources/2026-hatton-parallelobox-aabb-decomposition.md
  - concepts/industrial-am-monitoring.md
  - sources/2025-leet-ts-aces-smart-factory.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

@concepts/print-farm-operations.md @concepts/fdm-printing.md @sources/2025-surynek-sequential-printing-cegar.md @sources/2026-hatton-parallelobox-aabb-decomposition.md

## Raw Concept

Two complementary scheduling regimes for getting more out of one print job: **sequential printing** on a single printer, and **parallel decomposition** across many. Both formalize as optimization problems over collision-and-volume constraints.

## Narrative

### Sequential printing (one printer, multiple objects)

Standard FDM prints all objects on a plate slice-by-slice in lockstep — every object grows by one layer, then the toolhead moves on. **Sequential printing** instead completes object 1 entirely, then object 2, etc. The geometric challenge is collision avoidance: the gantry, print head, cables, and other moving parts of the printer body must not strike previously-completed objects when starting a new one.

**Three benefits over slice-by-slice [Source: 2025-surynek-sequential-printing-cegar.pdf p.1]:**

1. **Failure robustness.** Standard mode: one object delaminates → toolhead drags it across the next layer → entire batch ruined. Sequential: one fails, only that one is wasted. For a 10-print Etsy batch this is the difference between losing 10% and losing 100%.
2. **Speed.** Eliminates per-layer travel between objects. The toolhead stays on one object for its full Z extent before relocating.
3. **Multi-color economy.** Bambu AMS (and equivalent multi-material units) purges filament on every color change. Slice-by-slice multi-color = N color changes per layer × layer count. Sequential = N color changes per object × object count. For 10 objects each requiring 3 color changes printed at 100 layers, the difference is 30 purges (sequential) vs 3000 purges (slice-by-slice). **This is the largest single contributor to "wasted filament" complaints with multi-material printing.**

**Implementation** [@sources/2025-surynek-sequential-printing-cegar.md]: Surynek + Prusa Research (2025) formalize the problem as **SEQ-PACK+S** — find positions `(Xᵢ, Yᵢ)` and times `Tᵢ` for objects `O₁..Oₖ` such that all fit on plate `P_P` and the extruder body never collides with previously-completed objects. NP-hard by reduction from rectangle packing. Encoded as a linear-arithmetic formula, solved by **Z3 (SMT) with CEGAR-inspired refinement** that loads the expensive collision constraints lazily. Z3 dominates Gecode (CSP) in head-to-head comparison; CEGAR-SEQ ≫ eager constraint loading. Shipping in **PrusaSlicer 2.9.1**; code at <https://github.com/surynek/cegar-seq>.

**Bambu picture.** Bambu Studio (and OrcaSlicer, the Bambu fork of PrusaSlicer) inherits PrusaSlicer's sequential-printing UX. [TENTATIVE] Whether the OrcaSlicer fork pulls the CEGAR-SEQ code or uses an older sequential-printing implementation needs verification [NEEDS VERIFICATION 2026-05-06].

### Parallel printing (multiple printers, one model)

The opposite regime: take *one* model that's large enough to want to split, decompose it into N pieces sized for parallel printing across N printers, then physically assemble. Wall-clock time is now `max(per-piece time)` rather than `sum`.

**Decomposition objective inverts the classic priority** [Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.1]: traditional mesh decomposition (Chopper, BSP-based) optimizes total volume + assembly fidelity + aesthetic seams. Parallel printing optimizes **even printer utilization** — a longer aggregate time is fine if the longest piece shrinks.

**Approaches:**

| Algorithm | Style | Strength | Weakness |
|---|---|---|---|
| Cube Skeleton Segmented Shell | Top-down skeleton-based | Fast (ms) | No printer-count input; fixed output |
| Symmetry-Based Decomposition | Recursive symmetry | Fast; printer-count aware | Geometry-blind; weak on complex models |
| **Parallelobox** [@sources/2026-hatton-parallelobox-aabb-decomposition.md] | Bottom-up AABB height-field growth + k-means++ + metaheuristic | Geometry-aware; dominates baselines on complex models | Compute cost: minutes vs ms; stochastic noise |

Parallelobox [Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.12] uses axis-aligned bounding boxes as height-field columns. Six steps: symmetry pre-cut → k-means++ seed blocks → height-field block growth → conflict resolution → mesh-clipping → metaheuristic outer loop over printer count and clustering configs.

**Cost-benefit:** several minutes of compute is trivial against several hours of saved parallel-printing time, especially on large models (the Brain Left MRI / Stanford-Bunny-class examples in the paper).

### When does either matter for the reader?

| Scenario | Sequential | Parallel decomposition |
|---|---|---|
| One small Bambu, hobby | Maybe (multi-color savings) | No |
| One Bambu, Etsy batch of 10 small items | **Yes — failure-robust** | No |
| Multi-color AMS + AMS HT combo | **Yes — multi-color purge savings dominate** | No |
| One Bambu, large cosplay armor | No (one piece, fits on plate) | No |
| Two-three Bambus, large commission work | No | **Yes — wall-clock time** |
| Print farm | Both regimes complement each other |

[CONFIRMED] Both implementations exist and are open source. [CONFIRMED] Sequential printing is the more impactful for solo / small operators because it adds value at fleet size 1; parallel decomposition needs ≥2 printers to mean anything.

## Snippets

(none — synthesis page; raw quotes live on the source pages)
