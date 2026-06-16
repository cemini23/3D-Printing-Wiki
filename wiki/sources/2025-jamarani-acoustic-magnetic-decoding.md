---
title: "Practitioner Paper: Decoding Intellectual Property — Acoustic and Magnetic Side-Channel Attack on a 3D Printer"
type: source
tags: [paper, security, attack, acoustic, magnetic, side-channel, ml-attack, GBDT]
keywords: [Gradient Boosted Decision Trees, GBDT, MFCC, ZCR, Galaxy S22 Plus, LULZBOT TAZ, mean tendency error, MTE, smartphone attack, UL Lafayette, Auburn]
related:
  - concepts/side-channel-attacks.md
  - concepts/ip-theft-3d-printing.md
  - concepts/g-code-protection.md
  - concepts/fdm-printing.md
  - sources/2026-asgar-quietprint-acoustic-defense.md
  - sources/2025-chattopadhyay-one-video-optical.md
  - sources/2025-dolgavin-hearsay-pbf-power.md
  - sources/2026-yocam-amnc-bambu-side-channel.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
read_status: deep-read
---

## Relations

@concepts/side-channel-attacks.md @concepts/ip-theft-3d-printing.md @concepts/g-code-protection.md @concepts/fdm-printing.md @sources/2026-asgar-quietprint-acoustic-defense.md @sources/2025-chattopadhyay-one-video-optical.md @sources/2025-dolgavin-hearsay-pbf-power.md

## Raw Concept

- Title: Practitioner Paper: Decoding Intellectual Property — Acoustic and Magnetic Side-Channel Attack on a 3D Printer
- Authors: Amirhossein Jamarani, Yazhou Tu, Xiali Hei (University of Louisiana at Lafayette; Auburn University)
- Type: Springer International Conference on Security and Privacy in Cyber-Physical Systems and Smart Vehicles 2025, pp. 54-74; arXiv:2411.10887
- Location: `raw-sources/2025-jamarani-acoustic-magnetic-decoding.pdf`
- Retrieved: 2026-05-06
- Pages: 22
- Read-status: deep-read

## Narrative

A **two-channel** side-channel attack (acoustic + magnetic) on a desktop FDM printer using only a stock smartphone. Improves on prior single-channel acoustic attacks by adding magnetic-field measurements (the smartphone's magnetometer) and by using Gradient Boosted Decision Trees (GBDT) instead of CNN/regression baselines, and by demonstrating effectiveness *at greater distances from the printer* — addressing the "you have to plant a recorder right next to the machine" critique that limits real-world relevance of prior acoustic-only attacks.

**Threat model.** Adversary places a Galaxy S22 Plus near the printer (greater distance than prior work — exact figures not given in the read pages but the paper's positioning is non-intrusive). The phone uses an app that records audio and magnetic field simultaneously to a CSV. No physical contact with the printer. Pure physical-to-cyber exploitation.

**Hardware**:
- Target: LULZBOT TAZ (open-frame, single Y-axis bed motion, dual Z-axis steppers at edges, X-axis stepper coupled to the Z carriage). Single-extruder, no enclosure.
- Recorder: Samsung Galaxy S22 Plus — built-in mic + magnetometer.

**Pipeline (training)**:
1. Record audio + magnetic data labeled by G-code commands during nozzle moves on each axis.
2. **Acoustic feature extraction**: ZCR (Zero-Crossing Rate), Short-Time Energy (STE), RMS, Spectral Centroid, Spectral Bandwidth, Gaussian smoothing, **MFCCs** (Mel-Frequency Cepstral Coefficients) — the dominant acoustic feature for distinguishing motor states.
3. **Per-axis hierarchical model** following [31]'s five-layer scheme: (a) Z-axis vs not, (b) header (no-extrusion travel) vs print, (c) X vs Y, (d) X-left vs X-right, (e) Y-up vs Y-down. Each layer is a GBDT classifier.
4. **Side-Channel Reconstruction of G-code (SCReG)** technique: combines per-movement predictions to rebuild the G-code instruction sequence.

**Headline metrics**:
- **98.80% mean accuracy** across all axial movements + stepper / nozzle / rotor speeds.
- **4.47% Mean Tendency Error (MTE)** on a "plain G-code design" — improving over [31]'s 5.87% MTE, [9]'s 17.82% length error, and [10]'s 11.11% length error.

**Comparison with prior work** (Section 6.1, not in deep-read pages but cited throughout): [9] = Faruque et al. 2016 acoustic-only ICCPS = 78.35% axis accuracy / 17.82% length error; [31] = a prior multilayer scheme = 5.87% MTE; [15] = regression-only acoustic = 98.55% classification + 3.13% MAPE on a square (a simple shape only). Jamarani's contribution: combine acoustic + magnetic, scale to non-trivial G-code, GBDT classifier, smartphone recording from distance.

**Background context** the paper provides on AM lifecycle and threat surface (Section 3 and 4): STL → CAM/slicer → G-code → motors. Authors cite blockchain-based G-code storage [27], encryption-at-rest [28], and physical-hash quality-control [7] as defenses. Also discusses "weaponizing" angle [36] — minor IP modifications producing dangerous parts.

**Limitations** [TENTATIVE]:
- Recording distance and noise tolerance: paper claims "greater distances" but the deep-read pages don't give the exact distance. This is a likely critical real-world limit; [NEEDS VERIFICATION 2026-05-06] from later pages.
- LULZBOT TAZ is open-frame; enclosed printers (Bambu X1C, Prusa XL with enclosure) attenuate acoustic emission — generalization to enclosed printers not tested.
- "Plain G-code design" — the test object isn't characterized in the abstract; complexity bound unclear from pages 1-10.
- Magnetic side-channel works only at close range (magnetic field falls off as 1/r³); real-world covert deployment likely needs the phone within ~30 cm.

**Practical bearing for a Bambu user**: a co-worker / cleaner / family member with a phone in the same room could in principle deploy SCReG against an open-frame Bambu A1. The X1C's full enclosure is acoustic mitigation by accident, not by design — but the magnetic side-channel still leaks through the enclosure walls. **Recommended defense**: physical isolation (lockable print room) for genuinely sensitive IP, plus G-code-level obfuscation for residual acoustic leakage [@sources/2026-asgar-quietprint-acoustic-defense.md].

## Snippets

> "By training models using Gradient Boosted Decision Trees, our prediction results for each axial movement, stepper, nozzle, and rotor speed achieve high accuracy, with a mean of 98.80%, without any intrusiveness. We effectively deploy the model in a real-world examination, achieving a Mean Tendency Error (MTE) of 4.47% on a plain G-code design."
[Source: 2025-jamarani-acoustic-magnetic-decoding.pdf p.1]

> "We illuminate the procedure of how to use a smartphone to collect data from 3D printer in an effective way."
[Source: 2025-jamarani-acoustic-magnetic-decoding.pdf p.3]

> "Authors in [9] completed a thesis on cyber-physical attacks in additive manufacturing systems… restored test objects with 78.35% axis prediction accuracy and 17.82% length prediction error."
[Source: 2025-jamarani-acoustic-magnetic-decoding.pdf p.3]
