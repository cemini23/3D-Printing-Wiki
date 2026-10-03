---
title: "ChunkVLA-AM — VLA deployment for AM part retrieval (arXiv:2610.01856)"
type: source
tags: [paper, VLA, AM, robotics, deployment, failure-modes, OpenVLA, LoRA]
keywords: [ChunkVLA-AM, OpenVLA-OFT, action chunking, FAIRINO FR3, LoRA, cloud-edge inference, embodiment adaptation, illumination robustness, post-print retrieval, workcell automation]
related:
  - concepts/vlm-in-manufacturing.md
  - concepts/fdm-printing.md
  - concepts/print-farm-operations.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
read_status: deep-read
wire_status: wont_wire
wire_target: "VLA deployment REFERENCE; 3D-printing Phase-1 local wires off"
---

## Relations

@concepts/vlm-in-manufacturing.md @concepts/fdm-printing.md @concepts/print-farm-operations.md

## Raw Concept

- **Title:** ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing
- **Authors:** Zhugang Liu, Kaichuang Zhang, Jinman Zhang, Pu Sun, Martha Asare, Jose Hernandez, Maxim Ermolinsky, Efren Saenz, Qi Lu, Jinghao Yang (corresponding)
- **Affiliations:** University of Texas Rio Grande Valley (CS + ECE), University of South Florida, San Diego State University
- **Type:** Conference-format paper (IEEE-style, cs.RO)
- **arXiv:** 2610.01856v1 [cs.RO] — 1 Oct 2026
- **Pages:** 8
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2610.01856-chunkvla-am-parallel-action-chunking-for-vision.pdf`
- **Read-status:** deep-read
- **Funding:** NSF CREST MECIS (2112650), NSF Expand AI ARISE (2434916), NSF ACCESS (ELE250047), USDOT UTCRS

## Narrative

This is the **first deployment paper** in the wiki's VLA cluster. The other papers (VLM-IRIS, τ-schema, CIPHER) are successful demos. This one reports what happens when you **actually put a VLA on a robot arm in a manufacturing workcell** — including the parts that fail.

It directly answers the gap flagged in [@concepts/vlm-in-manufacturing.md]: *"Failure modes of VLM-in-manufacturing deployments — when these systems break in production, why, and what the operational risks look like."*

### What they built

A cloud–edge pipeline that lets a **7B OpenVLA-OFT** model drive a **FAIRINO FR3** arm doing **post-print part retrieval** (pick a coloured block at point A, place it at point B).

| Component | Choice |
|---|---|
| Base model | OpenVLA-OFT (7B) |
| Adaptation | **LoRA**, rank 32, zero dropout; lr 5×10⁻⁴; effective batch 32; ~30 epochs |
| Action interface | **H = 8** step action chunks |
| Action space | 7-D Cartesian end-effector delta + binary gripper: `[Δx,Δy,Δz,Δφ,Δθ,Δψ,g]` |
| Input | Monocular RGB, square-padded to 224×224, ~25 Hz |
| Split | 7B model on a remote RTX 6000 Ada; robot client **CPU-only** |
| Transport | FastAPI request per replan step |

The FR3 executes each 8-step chunk **open loop**, then captures a new observation — so feedback is **between chunks**, not within one [CONFIRMED paper, §IV.D].

### The headline: zero-shot VLA fails hard, and the failure is quantified

| Configuration | MAE (mm) | Verdict |
|---|---|---|
| OpenVLA (zero-shot) | 179.60–650.12 | **Unusable** — wild spatial deviation |
| OpenVLA-OFT (zero-shot) | 179.60–650.12 range | **Unusable** — chunking alone did not help |
| Single-step adapted baseline | 9.50 avg; **16.90 on X** | Better, but still dangerous |
| **ChunkVLA-AM (adapted + 8-step chunks)** | **1.74 avg** (X 0.37, Y 0.97, Z 3.87) | Sub-millimeter laterally |

Two results matter more than the winner:

1. **Pre-trained visual backbones do not transfer to a constrained workcell.** The paper's reading of the zero-shot failure: *"temporal action chunking alone cannot compensate for the lack of spatial semantics"* [Source: ...pdf §V.D]. Adaptation is not optional.
2. **A 16.90 mm lateral error is not a quality problem — it is a collision.** The authors state plainly that this offset *"easily causes collisions with the build plate or printed parts"* [Source: ...pdf §V.D]. That is the difference between "worse MAE" and "unsafe".

### The caveat that matters most

The paper is explicit that **the comparison is not a clean ablation**. The four configurations differ in **both** adaptation **and** prediction horizon:

> "Because the compared configurations differ in both adaptation and prediction horizon, these results support the combined FR3-adaptation and chunked-deployment configuration but do not by themselves attribute the improvement solely to action chunking." [Source: ...pdf §V.D]

And separately — the 1.74 mm figure is **open-loop trajectory consistency on logged frames**, computed by comparing predicted future positions to expert trajectories. It is **not** closed-loop task success. The authors say so directly: *"the metrics describe open-loop trajectory consistency, not final task success"* [Source: ...pdf §V.C].

Read those two caveats before quoting the 1.74 mm number anywhere.

### Physical trials: 92.9%, and the failures are informative

**39 of 42** A-to-B transfers succeeded (21 red, 21 blue targets) = **92.9%**.

All **three failures happened at the same place**: terminal placement at point B. The released object fell and toppled because **release-height control was insufficient**. The failures were kept in the reported rate [CONFIRMED paper, §V.E].

That is a useful pattern: the policy got the object *to* the destination but not *down* onto it cleanly. Note this lines up with the trajectory numbers — **Z is the dominant error axis throughout the paper** (3.87 mm vs 0.37/0.97 laterally).

### Illumination: a real deployment variable, with a measured safe band

The workcell was tested under controlled lighting: neutral, low-light, over-exposed, and colour temperatures of ~3000 K / 6500 K [CONFIRMED paper, §V.F].

| Condition | Mean luminance (0–255) | 3D L2 error (mm) |
|---|---|---|
| Baseline (neutral) | 109 | 4.01 |
| Low-light extreme | 30 | 4.26 |
| Low-light mild | 65 | 4.17 |
| Over-light mild | 165 | 4.00 |
| **Over-light extreme** | **190** | **5.22** (Y MAE 2.30) |
| Colour temp warm | 116 | 4.07 |
| Colour temp cold | 108 | 3.92 |

A denser sweep (10 trials × 181 luminance levels from 30 to 210) found:

- Minimum error **5.459 mm at luminance 95**, in a low-error band of **85–125**.
- Endpoints degrade: **+31.2%** at luminance 30, **+20.9%** at 210.
- **Luminance 95 is not a universal optimum.** Per-trial optima ranged from **36 to 198** (median 95). The paper warns against reading 95 as a target [Source: ...pdf §V.F].

Extreme glare was the worst condition. Colour temperature barely mattered. The authors' conclusion is a deployment recommendation: **add lighting augmentation for reflective AM workspaces** (build plates are reflective).

### Safety filtering — the part to copy

Every candidate action is checked client-side before execution. A rejected action discards the rest of the chunk [CONFIRMED paper, §IV.E]:

- End-effector position must stay inside the allowed workspace `B`.
- Height must stay above a minimum build-plate clearance `z_min`.
- Per-step translation `≤ 5 mm`; per-step rotation `≤ 0.05 rad`.
- Gripper command must be a valid binary state.

The client also rejects **NaN actions, network-timeout responses, stale chunks, and any command arriving after an emergency-stop flag**.

The paper is careful that these are **deployment parameters, not safety guarantees** — they bound the largest command, but physical safety still depends on validation, contact monitoring, and e-stop handling [Source: ...pdf §IV.B]. That distinction is worth keeping.

### Latency and cost

Model-side inference was **0.06–0.08 s per request** on an RTX 6000 Ada. That figure **excludes** image capture, network transmission, and robot execution — so end-to-end replan time is higher than it looks [CONFIRMED paper, §IV.E].

The 7B model does not fit on the robot's CPU-only workstation; the cloud–edge split exists precisely because *"the robot controller and VLA model cannot run on the same machine"* [Source: ...pdf §IV]. This is server-class inference, consistent with the cost concern already noted for CIPHER in [@concepts/vlm-in-manufacturing.md].

### What they did not do

The authors list their own gaps: no controlled **chunk-length ablation** (they note this explicitly as missing), no **contact-force monitoring**, and no broader task generalization. Future work targets **warped-part inspection** and **failed-print removal** — both genuinely AM-specific tasks [Source: ...pdf §VI], and both closer to [@concepts/fault-detection.md] territory than the coloured-block proxy used here.

### Reader relevance

Direct hands-on use for a Bambu owner in 2026: **none**. This needs a 6-axis industrial arm, a GPU server, and a trained policy.

The transferable content is conceptual:

1. **Adaptation is mandatory; the pre-trained model is not the product.** Zero-shot VLA in a real cell was off by hundreds of millimetres.
2. **Chunking is a temporal device, not a spatial one.** It cannot fix missing spatial grounding — the zero-shot chunked model failed just as badly.
3. **Ask what the error metric actually measures.** "1.74 mm" is open-loop consistency on logged frames. The physical success rate is 92.9%, and the 7.1% failure is a single repeated mode.
4. **Safety filtering is where the real engineering is.** Workspace bounds, clearance floors, per-step clamps, stale/NaN/timeout rejection. Any future AM automation needs this layer regardless of model quality.
5. **Lighting is a deployment variable, not a detail.** Extreme glare degraded tracking most; the paper recommends lighting augmentation for reflective AM workspaces.

**Phase-0:** no repository, no code release, no dataset link in the paper. **REFERENCE** only. **Phase-1:** `wont_wire`.

## Snippets

> "Both zero-shot models are unsuitable for the FR3 additive manufacturing environment. OpenVLA (Zero-Shot) and OpenVLA-OFT (Zero-Shot) produce extreme spatial deviations, with MAE values ranging from 179.60 mm to 650.12 mm." [Source: 2026-liu-chunkvla-am-vla-deployment.pdf p.5]

> "In physical AM workcells, a 16.90 mm lateral offset easily causes collisions with the build plate or printed parts." [Source: 2026-liu-chunkvla-am-vla-deployment.pdf p.6]

> "Across all 42 trials, 39 transfers were completed successfully, corresponding to an overall success rate of 92.9%. The three failures occurred during terminal placement at point B: the placement height was not sufficiently controlled, causing the released object to fall and topple." [Source: 2026-liu-chunkvla-am-vla-deployment.pdf p.6]

> "Although the across-trial curve reached its lowest value of 5.459 mm at luminance 95 and remained within 5% of this minimum from 58 to 200, the error-minimizing luminance of individual trials ranged from 36 to 198 (median 95). Thus, luminance 95 should not be interpreted as a universal optimum." [Source: 2026-liu-chunkvla-am-vla-deployment.pdf p.7]

> "These thresholds are deployment parameters and should not be interpreted as safety guarantees" [Source: 2026-liu-chunkvla-am-vla-deployment.pdf p.4]
