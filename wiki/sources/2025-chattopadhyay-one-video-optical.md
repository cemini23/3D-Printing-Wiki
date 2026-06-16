---
title: "One Video to Steal Them All: 3D-Printing IP Theft through Optical Side-Channels"
type: source
tags: [paper, security, attack, optical, side-channel, ml-attack, ResNet, LSTM]
keywords: [ResNet-50, LSTM, oriented bounding polygon, OBP, DTW, Geeetech A20T, Marlin, Georgia Tech, CCS25, optical side-channel, IP camera]
related:
  - concepts/side-channel-attacks.md
  - concepts/ip-theft-3d-printing.md
  - concepts/g-code-protection.md
  - concepts/fdm-printing.md
  - sources/2026-asgar-quietprint-acoustic-defense.md
  - sources/2025-jamarani-acoustic-magnetic-decoding.md
  - sources/2025-dolgavin-hearsay-pbf-power.md
  - sources/2026-yocam-amnc-bambu-side-channel.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
read_status: deep-read
---

## Relations

@concepts/side-channel-attacks.md @concepts/ip-theft-3d-printing.md @concepts/g-code-protection.md @concepts/fdm-printing.md @sources/2026-asgar-quietprint-acoustic-defense.md @sources/2025-jamarani-acoustic-magnetic-decoding.md @sources/2025-dolgavin-hearsay-pbf-power.md

## Raw Concept

- Title: One Video to Steal Them All: 3D-Printing IP Theft through Optical Side-Channels
- Authors: Twisha Chattopadhyay, Fabricio Ceschin, Marco E. Garza, Dymytriy Zyunkin, Animesh Chhotaray, Aaron P. Stebner, Saman Zonouz, Raheem Beyah (Georgia Institute of Technology, UTSA, Todyl Inc.)
- Type: ACM CCS '25 proceedings paper, arXiv:2506.21897, DOI 10.1145/3719027.3744837
- Location: `raw-sources/2025-chattopadhyay-one-video-optical.pdf`
- Retrieved: 2026-05-06
- Pages: 17
- Read-status: deep-read

## Narrative

First end-to-end optical-side-channel attack that recovers a *printable* G-code IP from a video recording — not just a 3D trajectory. The attack assumes only an IP-camera compromise; no planted hardware. Demonstrates a fully functional counterfeit padlock key and a counterfeit gear printed from the recovered G-code.

**Threat model.** Adversary compromises the existing IP camera that the operator already runs for remote-monitoring / failure detection (Liang 2022 [NDSS] required a planted hidden camera; this is more realistic). Adversary knows nothing about the original G-code, slicer parameters, or coordinate frame.

**Architecture.**
- **Backbone**: ResNet-50 + LSTM. ResNet-50 extracts features from each of N=30 frames per G-code instruction (224×224 px); LSTM aggregates to a single embedding capturing nozzle motion + extrusion-timing context.
- **Two heads**: (a) binary classifier G0 vs G1 (downsampled because 88% of training instructions were G1), trained with cross-entropy; (b) coordinate regressor, trained with MSE, sigmoid·250 output to clip to printer bed (250 mm).
- **Z-axis discretization**: PELT change-point detector + 0.3 mm layer height to convert the continuous Z regression into discrete layer indices.
- **Sliding window inference**: 60-frame batches, 30-frame stride. Adversary doesn't know where G-code instructions begin/end so the network has to infer from the video stream itself.
- **Extrusion + feed rate**: deterministic post-processing using `E = (4·h·s·l·dn)·d_f² / π` (h=0.3 mm, s=100%, dn=0.4 mm, df=1.75 mm, l = segment length); feed rate looked up from the predicted G0/G1 label (G0 ≈ 7740, G1 ≈ 3600 in their dataset).

**Hardware**: Geeetech A20T with Marlin 1.1.8 firmware, PLA filament, 0.4 mm nozzle, 250×250 mm bed, 0.3 mm layer height. Slicer: Repetier-Host 2.3.2 driving CuraEngine 15.01. Default infill: concentric (chosen because it's translation-invariant). **Cross-printer**: trained on Geeetech, also produced a counterfeit key successfully on an Ultimaker — robustness claim across printers.

**Equivalence checker — the second contribution.** Standard distance metrics (mean-squared error, normalized MSE) are *not* rotation- or translation-invariant; an adversary who recovers an identical object placed at a different point on the bed would be falsely scored as failed. The paper introduces an **Oriented Bounding Polygon (OBP)** — a generalization of Oriented Bounding Box that uses a convex hull instead of a rectangle. Two trajectories are aligned by (1) translating to common centroid, (2) brute-force rotating one polygon 1° at a time over 360°, picking the rotation that minimizes the area difference of the fused polygon. Then **Subsequence-Aligned Dynamic Time Warping (SA-DTW)** computes the dissimilarity. Result: average curve-checker similarity of **99.76% / 99.71% / 99.54%** for rotated / translated / both, vs nMSE's **74.65% / 28.39% / 73.83%** — nMSE rejects valid IP thefts.

**Headline accuracy**: 90.87% average curve-checker similarity across 16 objects (gears, keys, hex shapes). Best 97.3% (KE5), worst 83% (G16). Layer 1 (the brim, which is peeled off) is the largest dissimilarity contributor — not actually relevant to the printed object. **30.20% fewer instructions** than baseline (Liang 2022), meaning the recovered G-code is more compact and more directly executable.

**Datasets**:
- Dataset #1: 16 objects × 2 camera angles = 37,121 videos / 150 GB / ~48 hours. To synchronize video with G-code, paper uses OctoPrint REST API to send G-codes one-by-one, batched, with M300 beep markers at start/end. Largest existing G-code-to-video corpus in the literature.
- Dataset #2: same objects from a 60° clockwise camera offset, to test angle-invariance.
- Curve-checker dataset: 12 critical-infrastructure objects (hex wrench, drill bit plate, lidar mount, turbine impeller, prosthetic finger joint, satellite dish, etc.) with 4 infill patterns × {rotated, translated, both}.

**Limitations**:
- 3D printing is slow → dataset is small in object diversity (16 objects) [TENTATIVE: generalization to truly novel geometries unclear]
- Slicer-based rotation/translation also rotates infill pattern incoherently, so paper builds its own G-code manipulator.
- Defenses: noise injection on the optical channel (degrade video quality) — the paper claims this doesn't work because their model + post-processor is robust [NEEDS VERIFICATION 2026-05-06].

**Practical bearing for a Bambu user**: Bambu X1C ships an internal camera. If the camera stream is exposed (default Bambu Studio cloud, or a misconfigured LAN-mode setup), this attack class is directly applicable. **Defense candidates**: (1) keep the camera in LAN-only mode, (2) disable AI-failure-detection's image upload, (3) software-only G-code obfuscation (QuietPrint's SHM is acoustic-specific; an optical analog is open research). Strong industrial precedent for IP risk: this paper demonstrated functional padlock-key counterfeits from one video.

## Snippets

> "Our model achieves an average accuracy of 90.87% and generates 30.20% fewer instructions compared to the current state-of-the-art methods."
[Source: 2025-chattopadhyay-one-video-optical.pdf p.1]

> "When compared with nMSE (used in related works), our curve checker, on average, assigns 99.76%, 99.71%, and 99.54% similarity values to rotated, translated, and both rotated-and-translated variants of the same G-code, respectively; in comparison, average nMSE values on the same dataset are 74.65%, 28.39% and 73.83%."
[Source: 2025-chattopadhyay-one-video-optical.pdf p.2]

> "We use our model to reverse-engineer the 3D print instructions from a video recording and print a fully-functional counterfeit object."
[Source: 2025-chattopadhyay-one-video-optical.pdf p.1]

> "Defenses such as noise injection to degrade the quality of the optical side-channel are not applicable against our reverse-engineering solution that uses an ML model along with a post-processor to recover valid 3D printing instructions that encode the trajectory and the extrusion timing information of the nozzle."
[Source: 2025-chattopadhyay-one-video-optical.pdf p.3]
