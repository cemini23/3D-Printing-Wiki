---
title: FDM / FFF Printing
type: concept
tags: [process, FDM, FFF, fundamentals]
keywords: [fused deposition modeling, fused filament fabrication, extrusion AM, layer adhesion, nozzle, gantry]
related:
  - concepts/input-shaping.md
  - concepts/extrusion-control.md
  - concepts/fault-detection.md
  - concepts/high-speed-fdm.md
  - concepts/side-channel-attacks.md
  - concepts/ip-theft-3d-printing.md
  - concepts/g-code-protection.md
  - concepts/print-farm-operations.md
  - concepts/print-job-scheduling.md
  - concepts/am-as-a-service.md
  - concepts/filaments-baseline.md
  - concepts/vlm-in-manufacturing.md
  - concepts/bambu-ecosystem-closed-loop.md
  - concepts/ai-design-tools.md
  - entities/slicers/bambu-studio.md
  - entities/slicers/orcaslicer.md
  - entities/tools/kickstarter-autodesk-fdm-protocol.md
  - entities/materials/pla.md
  - entities/materials/petg.md
  - entities/materials/abs.md
  - entities/materials/asa.md
  - entities/materials/tpu.md
  - sources/2025-aung-adaptive-input-shaper.md
  - sources/2025-lin-camera-extrusion-optimization.md
  - sources/2023-waheed-acoustic-cnn-fault-detection.md
  - sources/2025-hoteit-closed-loop-extrusion-lqr.md
  - sources/2025-waheed-multimodal-sensor-fusion.md
  - sources/2026-asgar-quietprint-acoustic-defense.md
  - sources/2025-chattopadhyay-one-video-optical.md
  - sources/2025-jamarani-acoustic-magnetic-decoding.md
  - sources/2025-wang-collaborative-parameter-recommender.md
  - sources/2025-ivkic-cost-benefit-maas.md
  - sources/2025-surynek-sequential-printing-cegar.md
  - sources/2026-hatton-parallelobox-aabb-decomposition.md
  - sources/2026-bambu-filament-guide.md
  - sources/2026-mahjourian-vlm-iris.md
  - sources/2025-chen-tau-schema-vlm.md
  - sources/2025-margadji-cipher.md
  - sources/2026-bambu-toolchain-audit.md
maturity: draft
created: 2026-05-06
updated: 2026-05-07
---

## Relations

@concepts/input-shaping.md @concepts/extrusion-control.md @concepts/fault-detection.md @concepts/high-speed-fdm.md @concepts/side-channel-attacks.md @concepts/ip-theft-3d-printing.md @concepts/g-code-protection.md @concepts/print-farm-operations.md @concepts/print-job-scheduling.md @concepts/am-as-a-service.md @concepts/filaments-baseline.md @concepts/vlm-in-manufacturing.md @concepts/bambu-ecosystem-closed-loop.md @concepts/ai-design-tools.md @entities/slicers/bambu-studio.md @entities/slicers/orcaslicer.md @entities/tools/kickstarter-autodesk-fdm-protocol.md @entities/materials/pla.md @entities/materials/petg.md @entities/materials/abs.md @entities/materials/asa.md @entities/materials/tpu.md @sources/2025-aung-adaptive-input-shaper.md @sources/2025-lin-camera-extrusion-optimization.md @sources/2023-waheed-acoustic-cnn-fault-detection.md @sources/2025-hoteit-closed-loop-extrusion-lqr.md @sources/2025-waheed-multimodal-sensor-fusion.md @sources/2026-asgar-quietprint-acoustic-defense.md @sources/2025-chattopadhyay-one-video-optical.md @sources/2025-jamarani-acoustic-magnetic-decoding.md @sources/2025-wang-collaborative-parameter-recommender.md @sources/2025-ivkic-cost-benefit-maas.md @sources/2025-surynek-sequential-printing-cegar.md @sources/2026-hatton-parallelobox-aabb-decomposition.md @sources/2026-bambu-filament-guide.md @sources/2026-mahjourian-vlm-iris.md @sources/2025-chen-tau-schema-vlm.md @sources/2025-margadji-cipher.md @sources/2026-bambu-toolchain-audit.md

## Raw Concept

What a Bambu (or any consumer 3D printer at the ~$300-$1500 tier today) actually is: a Fused Deposition Modeling / Fused Filament Fabrication machine. This is the hub page — defines the process, lists the dominant failure modes, and points to the four research directions reshaping it. Synthesized from the 5-paper starter cluster ingested 2026-05-06.

## Narrative

**FDM / FFF** (terms used interchangeably; FFF is the patent-free variant of the same process) deposits a thermoplastic filament through a heated nozzle, layer by layer, onto a build plate. XY motion is driven by a gantry; Z by a bed or column.

The four open problems on consumer-grade FDM today, in rough order of how much they limit print speed and quality:

1. **Vibration / ringing at the toolhead.** High-acceleration moves excite the gantry's resonant mode, leaving visible ripples in the part. Mitigated by **input shaping** [@concepts/input-shaping.md] — Bambu's "Active Tuning" feature is a productized version of this idea.
2. **Extrusion under-/over-shoot at corners and speed transitions.** Open-loop extrusion assumes the filament melts and flows at a fixed rate, but at high speed it doesn't. Mitigated by **extrusion control** [@concepts/extrusion-control.md], either feedforward (camera-based G-code rewrite [Source: 2025-lin-camera-extrusion-optimization.pdf]) or closed-loop (force feedback [Source: 2025-hoteit-closed-loop-extrusion-lqr.pdf]).
3. **Print failures mid-job.** Nozzle clogs, filament breakage, pulley skips, layer separation. Detected by **fault detection** [@concepts/fault-detection.md] — acoustic [Source: 2023-waheed-acoustic-cnn-fault-detection.pdf], vibration, or thermal sensors fed into a classifier [Source: 2025-waheed-multimodal-sensor-fusion.pdf]. Bambu's "AI failure detection" is in this category.
4. **High-speed regime is qualitatively different.** Above ~300 mm/s the dominant errors shift from positioning to dynamic mismatch. See [@concepts/high-speed-fdm.md].

[CONFIRMED] All four problems are active research areas with multiple papers in the 2023-2025 cluster. [TENTATIVE] Bambu specifically markets features that map to (1) and (3); (2) and (4) are not standard consumer features yet [NEEDS VERIFICATION 2026-05-06].

## Snippets

(none — synthesis page)
