---
title: Fault Detection
type: concept
tags: [ML, monitoring, sensors, fault-detection]
keywords: [acoustic, vibration, thermal, CNN, spectrogram, sensor fusion, nozzle clog, filament breakage, layer separation]
related:
  - concepts/fdm-printing.md
  - concepts/vlm-in-manufacturing.md
  - sources/2023-waheed-acoustic-cnn-fault-detection.md
  - sources/2025-waheed-multimodal-sensor-fusion.md
  - sources/2026-mahjourian-vlm-iris.md
  - sources/2025-margadji-cipher.md
maturity: draft
created: 2026-05-06
updated: 2026-05-07
---

## Relations

@concepts/fdm-printing.md @concepts/vlm-in-manufacturing.md @sources/2023-waheed-acoustic-cnn-fault-detection.md @sources/2025-waheed-multimodal-sensor-fusion.md @sources/2026-mahjourian-vlm-iris.md @sources/2025-margadji-cipher.md

## Raw Concept

What's behind Bambu's "AI failure detection" feature — what's it watching, how does it know, and what's research adding next?

## Narrative

A consumer FDM printer running unattended for 8+ hours can fail in three economically important modes:

- **Nozzle clog** — filament stops flowing; gantry keeps moving; you get a "ghost" print of the planned shape with no material laid down
- **Filament breakage / runout** — same outcome from a different cause; some printers have a runout sensor for this
- **Layer separation / spaghetti** — print warps off the bed; subsequent layers print into open air

**Detection signals** in increasing order of fanciness:

1. **Acoustic** — microphone + spectrogram + CNN classifier. Works at zero hardware cost beyond a mic [Source: 2023-waheed-acoustic-cnn-fault-detection.pdf]. [TENTATIVE — the published 2023 result only contrasts with-material vs without-material on a Makerbot Method X; three-way clog / breakage / pulley-skip discrimination is the paper's framing, not what the metrics validate.]
2. **Multimodal sensor fusion** — combine acoustic + vibration (accelerometer on the gantry) + thermal (IR camera) into a single classifier [Source: 2025-waheed-multimodal-sensor-fusion.pdf]. [TENTATIVE — the 2025 paper's accelerometer channel "did not yield significant results" on a static-extrusion bench, and the headline 90-95% fused-accuracy figure is *expected* (projected from per-modality performance) rather than *measured*. Treat as a research-program declaration, not a validated result.]
3. **Visual** — fixed enclosure camera + image classifier. The Bambu X1 / X1C ships with this; trained on labeled "spaghetti" failures [TENTATIVE — Bambu marketing materials, not research paper] [NEEDS VERIFICATION 2026-05-06].

The research trajectory is from single-modality (audio-only, CNN-only) toward multimodal fusion with cheaper sensors aggregated into a single classifier — but as of late 2025 the published end-to-end multimodal results have not yet caught up with the framing.

## Snippets

> "We present a CNN based approach for real-time fault detection in 3D printers using acoustic signals. The system classifies three common failure modes: nozzle clog, filament breakage, and pulley skipping."
[Source: 2023-waheed-acoustic-cnn-fault-detection.pdf p.1]

> "The fused model outperforms any single-modality baseline in robustness and accuracy."
[Source: 2025-waheed-multimodal-sensor-fusion.pdf p.1]
