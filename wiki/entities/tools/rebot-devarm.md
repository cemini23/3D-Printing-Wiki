---
title: reBot-DevArm — Open-Source 6-DOF Robotic Arm (Hybrid CNC + 3D-Print)
type: entity
tags: [tool, robotics, robotic-arm, open-hardware, hybrid-manufacturing, ROS2, steal-from, 6-dof]
keywords: [reBot-DevArm, Seeed Projects, 6-DOF arm, robotic arm, CERN-OHL-W-2.0, Apache-2.0, Motorbridge SDK, rebotarm_ros2, ROS2 Jazzy, CAN bus, Damiao, RobStride, Aluminum 5052, Bambu ABS, TPU 95+, soft fingers, MGN9, BOM, infill profile, hybrid CNC and print]
related:
  - entities/materials/abs.md
  - entities/materials/tpu.md
  - concepts/print-farm-operations.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
---

## Relations

@entities/materials/abs.md @entities/materials/tpu.md @concepts/print-farm-operations.md @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md

## Raw Concept

Cross-routed from OSINT workspace tool-eval ingest 2026-05-16 (`@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md`). The tool-eval iteration scored reBot-DevArm as **STEAL-FROM tier with primary fit in the 3D-printing wiki** — the project's value to this workspace is not the robot itself but its **documented hybrid CNC+print manufacturing methodology**: a real, shipping bill-of-materials that splits parts between CNC-machined aluminum and 3D-printed ABS/TPU, with concrete slicer infill profiles. Page exists to extract that BOM / infill-profile / hybrid-methodology content for store-ops and design reference; the robotics/ROS2 stack is recorded as context but is not the reason this page is in a 3D-printing wiki.

## Narrative

### What it is

reBot-DevArm is an open-source **6-DOF (six degrees of freedom) robotic arm** published by Seeed Projects on GitHub (`github.com/Seeed-Projects/reBot-DevArm`). It positions itself as a bridge between high-performance robotics and accessible, low-cost 3D-printing ecosystems — the design goal is that a hobbyist with a consumer FDM printer and access to a small CNC shop (or a machining service) can build a research-grade arm.

Headline specs:

| Spec | Value |
|---|---|
| Degrees of freedom | 6 |
| Payload | 1.5 kg |
| Repeatability / precision | < 0.2 mm |
| Control stack | ROS2 Jazzy + Python + C++ |
| GitHub stars / open issues | ~3,400 / ~10 |

[Source: github.com/Seeed-Projects/reBot-DevArm]

### Bisected ("hybrid") manufacturing architecture — the part worth stealing

The reason this project earned a 3D-printing-wiki page is its **bisected architecture**: the BOM explicitly splits every structural part into one of two manufacturing routes by load class.

- **CNC-machined route — Aluminum Alloy 5052, ±0.02 mm tolerances.** Reserved for critical load-bearing components: the joint structure that carries the 1.5 kg payload moment and that must hold positional precision under continuous stress. Aluminum 5052 is a workable, corrosion-resistant, non-heat-treatable alloy — chosen for machinability and dimensional stability rather than maximum strength.
- **3D-printed route — Bambu ABS and TPU 95+.** All remaining structural components are FDM-printed. Rigid printed parts (joint bases, covers, brackets) are Bambu ABS Black; the **Soft Fingers** of the gripper are printed in TPU 95+ to get compliant, grippy contact surfaces.

The methodological takeaway for this wiki: **don't print what must not deflect — print what only has to hold a shape.** The reBot-DevArm BOM is a concrete worked example of triaging a parts list by load class, which is directly transferable to print-farm product design (jigs, fixtures, enclosures with embedded metal inserts).

### Concrete BOM detail useful for store-ops

The repo's documentation ships several things that are directly reusable as 3D-printing reference material:

- **Infill profile:** joint-base parts in Bambu ABS Black are specified at **30–45% infill** — a documented, real-world data point for load-bearing FDM structural parts (vs the 15–20% typical of decorative prints). See `@concepts/print-farm-operations.md` for where per-part profile discipline matters at fleet scale.
- **Documented component substitutions** — the BOM lists alternative parts where the primary sourcing is hard to obtain, lowering build-reproduction risk.
- **Hardware STEP files** — CAD geometry is published as STEP, so the printed parts can be re-sliced in Bambu Studio / OrcaSlicer and the machined parts handed to any CNC service.

ABS choice implications carry over from `@entities/materials/abs.md`: ABS is **enclosed-printer-only** (X1C / P1S — not the open-frame A1 / A1 mini), and the joint bases at 30–45% infill are exactly the "large, high-fill" geometry where Bambu's own guidance most strongly demands chamber heat. TPU 95+ for the Soft Fingers follows the flexible-filament workflow in `@entities/materials/tpu.md` — slow print, drying required, direct-drive feed (all Bambu printers qualify).

### Control stack (context, not 3D-printing-relevant)

For completeness: the arm is driven by the **Motorbridge Python SDK**, which standardizes **CAN bus (`can0`)** communication across multiple motor vendors (Damiao, RobStride) behind a common interface, exposing control modes including **Position-Velocity** and **MIT torque control**. The ROS2 side is the `rebotarm_ros2` Jazzy workspace, which executes high-level commands such as `/rebotarm/move_to_pose`. This stack is recorded so the page is self-contained; it is not the reason the project is filed here.

### Licensing — clean for a print farm

reBot-DevArm uses a **split license**, and the split is favorable for this workspace's use case:

- **Hardware design — CERN-OHL-W-2.0** (CERN Open Hardware Licence, Weakly-reciprocal). This is a **copyleft** license, but the reciprocity trigger is **redistribution of the hardware design**. Building the arm and using it internally — including in a commercial print farm — does **not** trigger any source-disclosure obligation. The obligation only fires if you *distribute a modified hardware design*. Internal-use-only is clean.
- **Control software — Apache-2.0.** The Motorbridge Python SDK and the `rebotarm_ros2` workspace are both permissively licensed; Apache-2.0 imposes no copyleft and is safe to fork, modify, and embed.

[CONFIRMED] License split is hardware = CERN-OHL-W-2.0, software = Apache-2.0 [Source: github.com/Seeed-Projects/reBot-DevArm]. [TENTATIVE] CERN-OHL-W-2.0 copyleft triggers only on redistribution of the hardware design; purely internal use (e.g. a print farm building arms for its own line) avoids the reciprocity obligation — this is the standard reading of the W variant but a builder planning to *sell* arms or publish a derived design should read the licence text directly.

### Open question — printed-part durability under continuous load

The bisected architecture deliberately keeps load-bearing geometry on the CNC/aluminum side, but the BOM still routes some motion-system mounting through printed parts. [NEEDS VERIFICATION 2026-05-16] Long-term durability and deflection of **3D-printed MGN9 linear-slider brackets under continuous 1.5 kg payload stress** is not characterized in the repo documentation — ABS creep under sustained load is a real failure mode, and a printed slider bracket holding a moving payload is a candidate weak point. Anyone reproducing the build for production duty should bench-test these brackets or substitute machined equivalents.

## Snippets

> Project: reBot-DevArm — open-source 6-DOF robotic arm. 1.5 kg payload, < 0.2 mm precision. Critical load-bearing parts CNC-machined in Aluminum Alloy 5052 (±0.02 mm); remaining structure 3D-printed in Bambu ABS and TPU 95+ (TPU for the Soft Fingers).
[Source: github.com/Seeed-Projects/reBot-DevArm]

> Bambu ABS Black joint bases — infill 30–45%.
[Source: github.com/Seeed-Projects/reBot-DevArm — BOM / slicer profile]

> Hardware design licensed under CERN-OHL-W-2.0; control software (Motorbridge Python SDK + rebotarm_ros2 Jazzy workspace) under Apache-2.0.
[Source: github.com/Seeed-Projects/reBot-DevArm — LICENSE]
