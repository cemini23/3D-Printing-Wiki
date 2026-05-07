---
title: Advancing Industry 4.0 - Multimodal Sensor Fusion for AI-Based Fault Detection in 3D Printing
type: source
tags: [paper, fault-detection, sensor-fusion, AI, multimodal]
keywords: [acoustic, vibration, thermal, sensor fusion, FAMU, IJ Engineering Research Innovation, ADXL335, FLIR One Pro, Google Teachable Machine, Raspberry Pi]
related:
  - concepts/fault-detection.md
  - concepts/fdm-printing.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
read_status: deep-read
---

## Relations

@concepts/fault-detection.md @concepts/fdm-printing.md

## Raw Concept

- Title: Advancing Industry 4.0 - Multimodal Sensor Fusion for AI-Based Fault Detection in 3D Printing
- Authors: Sajid Waheed, Shonda Bernadin, Tarek Hassan (Florida A&M University)
- Type: Journal article — International Journal of Engineering Research and Innovation, vol. 17 no. 2, Fall/Winter 2025
- Location: `raw-sources/2025-waheed-multimodal-sensor-fusion.pdf`
- Retrieved: 2026-05-06
- Pages: 10
- Read-status: deep-read

## Narrative

Extends the 2023 acoustic-CNN paper to multimodal sensor fusion. Two experimental configurations:

- **Acoustic Baseline** — stereo USB microphones; Google Teachable Machine for classifier; Raspberry Pi PCB for inference.
- **Hybrid Fusion** — acoustic + vibration (ADXL335 accelerometer mounted on the gantry) + thermal (FLIR One Pro thermal camera).

[TENTATIVE — important caveat] The accelerometer channel **did not yield significant results** in their test setup because the static-extrusion bench involved very little gantry motion (the failure modes tested are stationary blockages, not speed-transition errors). The paper's "fused outperforms single-modality" claim is therefore largely **expected** rather than **measured** — the authors project 90-95% fused accuracy from per-modality performance, but do not report end-to-end fused-classifier metrics on a held-out test set [NEEDS VERIFICATION 2026-05-06].

Acoustic-alone reaches results comparable to the 2023 paper. Thermal-camera distinguishes hot-end normal-vs-anomalous well in static testing.

**Practical bearing**: useful framing for the multi-sensor fault-detection direction Bambu-class printers are heading. But the paper itself does not yet validate that multimodal fusion *outperforms* the 2023 audio-only baseline on a consumer-printer-relevant test, and the vibration channel is unlikely to add value on a stationary-fault test set regardless. Best read as a research-program declaration, not a finished result.

## Snippets

> "We propose a multimodal sensor fusion framework that combines acoustic, vibration, and thermal signals for AI-based fault detection in 3D printing. The fused model outperforms any single-modality baseline in robustness and accuracy."
[Source: 2025-waheed-multimodal-sensor-fusion.pdf p.1]

> "The accelerometer channel did not yield significant results during the initial tests, as the extrusion process involved very little movement in each axis."
[Source: 2025-waheed-multimodal-sensor-fusion.pdf p.8]
