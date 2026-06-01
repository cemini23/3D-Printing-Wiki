---
title: Neuromorphic Anomaly Detection in Laser Powder Bed Fusion
type: source
tags: [paper, LPBF, neuromorphic, anomaly-detection, industrial, background]
keywords: [SNN, Loihi, LPBF, photodiode, Ti-6Al-4V, i-FORM]
related:
  - concepts/volumetric-additive-manufacturing.md
  - concepts/industrial-am-monitoring.md
  - concepts/fault-detection.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
read_status: skimmed
---

## Relations

@concepts/volumetric-additive-manufacturing.md @concepts/industrial-am-monitoring.md @concepts/fault-detection.md

## Raw Concept

- Authors: Shreyan Banerjee et al. (UCD; i-FORM)
- Location: `raw-sources/2025-banerjee-neuromorphic-lpbf.pdf`
- Retrieved: 2026-06-01
- Read-status: skimmed

## Narrative

First **spiking neural network (SNN)** application for LPBF anomaly detection — laser energy drop during Ti-6Al-4V lattice prints detected via in-process **photodiode** (plasma + IR). Implemented on CPU, FPGA, and **Intel Loihi** neuromorphic chip. Industrial metal AM; no FDM reader action — maps to @concepts/fault-detection.md themes at factory tier.

## Snippets

> "This study is the first application of spiking neural networks (SNNs) for anomaly detection in the Laser Powder Bed Fusion (LPBF) additive manufacturing process." [Source: 2025-banerjee-neuromorphic-lpbf.pdf p.1]
