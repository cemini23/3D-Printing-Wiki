---
title: "Object Packing and Scheduling for Sequential 3D Printing: a Linear Arithmetic Model and a CEGAR-inspired Optimal Solver"
type: source
tags: [paper, optimization, scheduling, packing, sequential-printing, SMT, FDM, PrusaSlicer]
keywords: [SEQ-PACK+S, CEGAR, counterexample-guided abstraction refinement, Z3 theorem prover, SMT, satisfiability modulo theories, Gecode, CSP, linear arithmetic, Prusa Research, Czech Technical University, PrusaSlicer 2.9.1]
related:
  - concepts/print-job-scheduling.md
  - concepts/print-farm-operations.md
  - concepts/fdm-printing.md
  - sources/2026-hatton-parallelobox-aabb-decomposition.md
  - sources/2025-wang-collaborative-parameter-recommender.md
  - sources/2025-ivkic-cost-benefit-maas.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
read_status: deep-read
---

## Relations

@concepts/print-job-scheduling.md @concepts/print-farm-operations.md @concepts/fdm-printing.md @sources/2026-hatton-parallelobox-aabb-decomposition.md @sources/2025-wang-collaborative-parameter-recommender.md @sources/2025-ivkic-cost-benefit-maas.md

## Raw Concept

- Title: Object Packing and Scheduling for Sequential 3D Printing: a Linear Arithmetic Model and a CEGAR-inspired Optimal Solver
- Authors: Pavel Surynek (Faculty of Information Technology, Czech Technical University in Prague), Vojtěch Bubník, Lukáš Maťena, Petr Kubiš (Prusa Research)
- Type: arXiv preprint, arXiv:2503.05071v1 [cs.CG], 7 Mar 2025
- Location: `raw-sources/2025-surynek-sequential-printing-cegar.pdf`
- Retrieved: 2026-05-06
- Pages: 8
- Read-status: deep-read

## Narrative

Formalizes the **SEQ-PACK+S** problem (sequential object packing + scheduling) for Cartesian FDM printers and gives an SMT-based solver that ships in **PrusaSlicer 2.9.1**. Solver code: <https://github.com/surynek/cegar-seq>.

**Why sequential printing matters [Source: 2025-surynek-sequential-printing-cegar.pdf p.1]:**

1. **Failure robustness** — if one object fails, only that object is wasted. In standard slice-by-slice printing, if any of N objects fails (typical: one delaminates and gets knocked over by the toolhead), the *whole* batch is wasted because the toolhead now collides with the dislodged object on subsequent layers.
2. **Speed** — eliminates frequent inter-object travel moves between layers. The toolhead stays on one object for its entire height before moving to the next.
3. **Multi-color economy** — minimizes filament-change purges. In multi-color slice-by-slice, every layer change involves N color swaps (one per object); sequential printing does the swaps once per *object*.

**Trade-off:** the toolhead and gantry must avoid previously-completed objects on the bed. This makes object placement and order non-trivial — two valid sequences for the same object set can differ dramatically in whether they're physically printable.

**Problem statement (formal).** Set of objects `O = {O₁, …, Oₖ}` ⊂ R³. Extruder object `E` ⊂ R³ (extruder + print head + gantry + cables — abstracted as a fixed-shape moving body). Printing plate `P_P` ⊂ R². Find: positions `(Xᵢ, Yᵢ)` and times `Tᵢ` such that:
- All objects fit on `P_P` (rectangle-packing constraint)
- Earlier-printed objects don't collide with the extruder body when printing later ones (collision avoidance — Polygon-Lines-not-Intersect, "PLnI", on the Minkowski sum `E ⊕ Oⱼ`)
- Each pair has temporal ordering `Tᵢ < Tⱼ` or `Tⱼ < Tᵢ`

This is **NP-hard** by reduction from rectangle packing [Source: 2025-surynek-sequential-printing-cegar.pdf p.1 — citing rectangle packing's NP-hardness in Related Work].

**Approach: SMT (Z3) with CEGAR refinement.** Encode the problem as a linear-arithmetic formula over rational variables. Use the **Z3 Theorem Prover** as the solver. Direct encoding (eager — all constraints loaded at once) is too slow on real instances. The contribution: **CEGAR-SEQ** algorithm [Source: 2025-surynek-sequential-printing-cegar.pdf p.6 Algorithm 1]:

1. Initial abstraction `F` omits the expensive PLnI (collision-with-prior-objects) constraints — keeps only temporal-ordering and rectangle-bounding-box constraints
2. Solve `F` with Z3
3. If satisfiable, geometrically check whether any polygon edges actually intersect under the temporal ordering (using Minkowski-summed extruder shape on the later object)
4. If a violation is found, add the violated PLnI constraint to `F` and re-solve
5. Repeat until SAT-without-violations or UNSAT
6. Wrap in binary search over plate-size scaling factor `σ` to find smallest plate that fits all objects

**Key empirical result [Source: 2025-surynek-sequential-printing-cegar.pdf p.7]:**

- **Z3 (SMT) dominates Gecode (CSP)** on random-cuboid instances. Z3 solves more instances, faster, and gives more accurate solutions because it works on rationals (not finite-domain mm-grid like Gecode).
- **CEGAR-SEQ ≫ eager** (loading all constraints upfront). The lazy/refinement approach saves significant runtime because in practice PLnI is violated for only a small fraction of edge pairs — most edges never need their full constraint generated.
- Tested on a 250×210 mm² printing plate (matches a real Prusa MK3S) with 1–32 cuboid objects, then on 34 real 3D-printable parts (the printer's own spare parts).

**Implementation.** C++, integrated into PrusaSlicer 2.9.1 (Prusa's official open-source slicer, also the basis of the OrcaSlicer fork that targets Bambu printers). The user's perspective: open multi-object job in PrusaSlicer, click "Sequential printing," and the algorithm packs + orders the objects so the gantry never collides.

[CONFIRMED] Implementation is open-source and shipping. The Prusa Research authorship + integration into the official slicer makes this the practical reference for sequential printing on consumer FDM. [TENTATIVE] OrcaSlicer (Bambu's preferred slicer fork) — does it import this? Worth checking when the reader chooses a printer [NEEDS VERIFICATION 2026-05-06].

**Bearing on the reader.** Directly useful — if the reader ever batch-prints anything (Etsy seller producing 10 copies of a small product across one print job), sequential printing on a single Bambu approximates running multiple printers without owning multiple printers. The first benefit (failure robustness — losing 1 of 10 instead of 10 of 10) is the biggest practical win. The third benefit (multi-color economy) matters once the reader gets the Bambu AMS multi-color unit.

## Snippets

> "Unlike the standard 3D printing, where all objects are printed slice by slice at once, in sequential 3D printing, objects are completed one after other. In the sequential case, it is necessary to ensure that the moving parts of the printer do not collide with previously printed objects."
[Source: 2025-surynek-sequential-printing-cegar.pdf p.1 (abstract)]

> "Sequential printing has far-reaching significance for modern 3D printing, it can help to tackle the following challenges: (i) increasing the rebustness of the printing process to errors (in case of failure, we do not have to repeat the entire print, but only the unfinished objects) (ii) maximize the printing speed (sequential printing eliminates frequent movements of the print head between objects) (iii) minimize the number of time consuming color changes during multi-color printing"
[Source: 2025-surynek-sequential-printing-cegar.pdf p.1]

> "CEGAR-SEQ has been written in C++ and integrated as part of Prusa Slicer 2.9.1, an open-source slicing software for 3D printers. The Z3 Theorem Prover, an SMT solver, has been used for solving the linear arithmetic model within CEGAR-SEQ."
[Source: 2025-surynek-sequential-printing-cegar.pdf p.7]

> "The results convincingly show that using CEGAR-style refinement represent a key technique for performance of the method as it provides significantly better performance than the eager variant."
[Source: 2025-surynek-sequential-printing-cegar.pdf p.7]
