---
title: "Parallelobox: Improved Decomposition for Optimized Parallel Printing using Axis-Aligned Bounding Boxes"
type: source
tags: [paper, decomposition, parallel-printing, AABB, mesh-clipping, FDM, simulation]
keywords: [Parallelobox, axis-aligned bounding box, AABB, height field, k-means++, metaheuristic, Cube Skeleton Segmented Shell, Symmetry-Based Decomposition, Symmetry Slicer, Chopper, parallel partitioning, Hull, Wolverhampton, Huddersfield, Thingi10K]
related:
  - concepts/print-job-scheduling.md
  - concepts/print-farm-operations.md
  - concepts/fdm-printing.md
  - sources/2025-surynek-sequential-printing-cegar.md
  - sources/2025-wang-collaborative-parameter-recommender.md
  - sources/2025-ivkic-cost-benefit-maas.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
read_status: deep-read
---

## Relations

@concepts/print-job-scheduling.md @concepts/print-farm-operations.md @concepts/fdm-printing.md @sources/2025-surynek-sequential-printing-cegar.md @sources/2025-wang-collaborative-parameter-recommender.md @sources/2025-ivkic-cost-benefit-maas.md

## Raw Concept

- Title: Parallelobox: Improved Decomposition for Optimized Parallel Printing using Axis-Aligned Bounding Boxes
- Authors: Hayley Hatton (corresponding via Khalid email), Muhammed Khalid (Univ Hull, m.khalid@hull.ac.uk), Umar Manzoor (Univ Wolverhampton), John Murray (Univ Huddersfield)
- Type: arXiv preprint, arXiv:2603.29579v1 [cs.GR], 30 Jan 2026
- Location: `raw-sources/2026-hatton-parallelobox-aabb-decomposition.pdf`
- Retrieved: 2026-05-06
- Pages: 18
- Read-status: deep-read (pages 1-12 — abstract, related work, full method through metaheuristic, experimental design, full results comparison; pages 13-18 contain extended limitation discussion + appendices)

## Narrative

Decomposes a single 3D model into pieces that **multiple printers print in parallel**, then physically assemble. Distinct from sequential printing (Surynek above) — that's *one printer, multiple objects, one at a time*; this is *one model, split across many printers, simultaneously*. Both approaches converge on "use multiple machines or a longer-time-but-multiple-objects workflow to get a complete deliverable faster."

**Problem framing [Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.1]:** classic mesh-decomposition algorithms (Chopper, BSP-based) optimize *aggregate* printing time and *fit-on-plate*. Parallel printing inverts the priority: total wall-clock time = max(per-piece time), so aggregate-time can grow if it shortens the longest single piece. The decomposition objective should be **even printer utilization across N printers** rather than minimizing total volume.

**Algorithm core (AABB height-field growth) [Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.2]:**

1. **Symmetry pre-cut.** Detect axis-aligned symmetry; split the model along it. Keeps subsequent box growth simpler when geometry permits.
2. **k-means++ seeding.** Cluster surface samples to determine *N* initial seed-block locations.
3. **Height-field block growth.** Each axis-aligned bounding box is treated as a height-field column on the surface. Boxes grow simultaneously per an objective that rewards even printing-time distribution and penalizes overhang + internal-volume + parallel-printing-time disparity.
4. **Conflict resolution.** When two boxes overlap, resolve by the objective scoring.
5. **Mesh-clipping** (cheap, off-the-shelf operation) applies the final box layout to actually decompose the mesh into N pieces.
6. **Metaheuristic outer loop.** Two nested loops [Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.10]: outer reduces the printer count from initial N down (in case fewer printers gives better results); inner tries different clustering configs per outer iteration.

**Why AABBs vs OBBs.** Oriented bounding boxes would allow tighter fits but are expensive to position. Axis-aligned boxes constrain implementation complexity sharply while still giving enough degrees of freedom to track non-trivial geometry as height fields.

**Comparison baselines:**

1. **Cube Skeleton Segmented Shell** [Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.10] — paper has no native implementation available; Hatton et al. faithfully reimplemented it in C++ with CGAL (with minor errors corrected). Note: this baseline doesn't take printer count as input — it just produces *some* number of partitions, so direct comparison requires a "matchup" bracket.
2. **Symmetry-Based Decomposition / "Symmetry Slicer"** — recursive symmetry-based partitioning; aware of printer count.

**Test setup [Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.10-12]:**

| Parameter | Value |
|---|---|
| Infill | 5% |
| Sample tries | 3 |
| Granularity | Very fine (~15³ cells) |
| Overhang tolerance | 1° |
| Printer volume | 250 × 250 × 250 mm |
| Shell speed | 20 mm/s |
| Infill speed | 20 mm/s |
| Printer counts | 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 |

Real-printer reference machine: 0.4mm nozzle / 200 °C, glass bed 50 °C, build volume 223×223×205 mm, gantry XY at 12.5 µm precision, bed Z at 5 µm, print 30–300 mm/s, travel 30–350 mm/s [Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.12].

Test geometries: standard test objects, Thingiverse models, Thingi10K samples, plus "Brain Left" — an MRI of a friend's left brain hemisphere converted to STL with permission.

**Results [Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.12]:**

- **Strictly dominates Symmetry Slicer** in every matchup. Symmetry Slicer is geometry-agnostic; Parallelobox is geometry-aware via AABB growth.
- **Comparable-or-better than Cube Skeleton Segmented Shell.** Parity on simple convex shapes; clear wins on complex / less-convex / large geometry (3DBenchy, Brain Left dramatic improvements).
- **Cost: minutes of compute** vs ms for Cube Skeleton Segmented Shell. For a job that takes hours of parallel printing time, this overhead is acceptable.
- **Limitations** [Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.12]: stochastic noise (sometimes more printers gives a worse result), and occasional failures to find valid decompositions until the printer count rises sufficiently. The algorithm's objective penalty was sometimes over-constraining growth.

**Bearing on the friend.** Niche-but-real if the friend grows into a multi-printer farm operating on commission work that includes large objects (e.g. cosplay armor, large display props, architectural models). At 1–2 printers, irrelevant. At 4+ printers with a steady stream of large jobs, this kind of parallel decomposition saves wall-clock time more than buying additional printers does (because parallel cuts the longest critical path, where buying more printers only helps when objects actually fit on a single plate to begin with).

[CONFIRMED] Pure simulation results — no physical assembled-print validation in the paper. [TENTATIVE] Assembly fidelity (how well do AABB-cut pieces actually mate after printing?) is asserted as adequate but not deeply tested.

## Snippets

> "Where other algorithms may freely tolerate the production of decomposed parts with large disparities in size and surface area (should this be acceptable in pursuit of their own objectives), and may instead focus on reducing the aggregate printing time, in the case of parallel printing, printer utilization is most important. What this means is that a longer aggregate printing time is perfectly acceptable if it is translated into a shorter parallel printing time."
[Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.1]

> "Cube Skeleton Segmented Shell may be able to run in milliseconds whereas Parallelobox requires several minutes to complete, but several minutes is still not a massive expenditure in the context of many hours of parallel printing time savings."
[Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.12]

> "AgainstSymmetry Slicer, the results are very apparent: Parallelobox all but strictly dominates it. … AgainstCube Skeleton Segmented Shell, the results also speak for themselves. Parallelobox's decomposition set was almost always at least equivalent withCube Skeleton Segmented Shell, but was usually superior."
[Source: 2026-hatton-parallelobox-aabb-decomposition.pdf p.12]
