---
title: Real time fault detection in 3D printers using Convolutional Neural Networks and acoustic signals
type: source
tags: [paper, fault-detection, CNN, acoustic, ML]
keywords: [convolutional neural network, spectrogram, nozzle clog, filament breakage, pulley skipping, FAMU, IEEE 2023, Makerbot Method X, SparkFun]
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

- Title: Real time fault detection in 3D printers using Convolutional Neural Networks and acoustic signals
- Authors: Sajid Waheed, Shonda Bernadin (Florida A&M University)
- Type: IEEE conference paper, 2023
- Location: `raw-sources/2023-waheed-acoustic-cnn-fault-detection.pdf`
- Retrieved: 2026-05-06
- Pages: 6
- Read-status: deep-read

## Narrative

Records audio of an FDM machine printing, converts it to spectrograms, and trains a CNN classifier. Hardware: Makerbot Method X with ABS material, SparkFun MEMS microphone, bandpass filter 100-1200 Hz. Dataset: 256 audio samples, 80/20 train/test split.

[TENTATIVE — important caveat] The paper introduces the system as targeting three failure modes (nozzle clog, filament breakage, stepper-pulley skipping), but the experiment as actually run only contrasts **with-material** (printing) vs **without-material** (filament not feeding) audio. The "three failure modes" is the paper's framing of the problem space, not what the published metrics measure. The CNN is trained as a binary classifier in the experiment as run [NEEDS VERIFICATION 2026-05-06].

Reported results on the held-out test set: 91% accuracy, 88% precision, 85% recall, 86.5% F1 — for the binary task.

**Practical bearing**: a microphone-only failure-detection baseline is plausible at consumer-printer cost (Bambu's enclosure already has microphones for the AI failure-detection feature). But this paper does not validate end-to-end three-way classification; consumer firmware that distinguishes clog vs. breakage vs. spaghetti is solving a harder problem than this baseline addresses. Read this as a binary "is the printer extruding?" floor, not as evidence the failure-mode taxonomy is acoustically separable.

## Snippets

> "We present a Convolutional Neural Network (CNN) based approach for real-time fault detection in 3D printers using acoustic signals. The system classifies three common failure modes: nozzle clog, filament breakage, and pulley skipping."
[Source: 2023-waheed-acoustic-cnn-fault-detection.pdf p.1]
