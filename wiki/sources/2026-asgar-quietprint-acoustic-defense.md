---
title: "QuietPrint: Protecting 3D Printers Against Acoustic Side-Channel Attacks"
type: source
tags: [paper, security, defense, acoustic, g-code-rewrite, side-channel]
keywords: [Stealth Head Movement, SHM, convex hull, Procrustes, Elegoo Neptune 3, Texas A&M, side-channel defense, FDM]
related:
  - concepts/side-channel-attacks.md
  - concepts/ip-theft-3d-printing.md
  - concepts/g-code-protection.md
  - concepts/fdm-printing.md
  - sources/2025-chattopadhyay-one-video-optical.md
  - sources/2025-jamarani-acoustic-magnetic-decoding.md
  - sources/2025-dolgavin-hearsay-pbf-power.md
  - sources/2026-yocam-amnc-bambu-side-channel.md
maturity: draft
created: 2026-05-06
updated: 2026-06-16
read_status: deep-read
---

## Relations

@concepts/side-channel-attacks.md @concepts/ip-theft-3d-printing.md @concepts/g-code-protection.md @concepts/fdm-printing.md @sources/2025-chattopadhyay-one-video-optical.md @sources/2025-jamarani-acoustic-magnetic-decoding.md @sources/2025-dolgavin-hearsay-pbf-power.md @sources/2026-yocam-amnc-bambu-side-channel.md

## Raw Concept

- Title: QuietPrint: Protecting 3D Printers Against Acoustic Side-Channel Attacks
- Authors: Seyed Ali Ghazi Asgar, Narasimha Reddy (Texas A&M University)
- Type: arXiv preprint, arXiv:2602.02198
- Location: `raw-sources/2026-asgar-quietprint-acoustic-defense.pdf`
- Retrieved: 2026-05-06
- Pages: 10
- Read-status: deep-read
- Funding: NSF Grant CCRI 2234972

## Narrative

The first software-only defense against acoustic side-channel IP theft on consumer FDM printers. Rather than mask the noise (Stańczak 2023's €1000 speaker approach) the paper rewrites the G-code so that the obfuscated trajectory the attacker recovers is geometrically different from the original.

**Threat model.** Adversary has access to a microphone near the printer — a compromised device, an insider's smartphone, or a planted recorder. Asgar uses the *built-in mic of a Microsoft Surface Pro 7+ laptop* to make the attack realistic; prior work [Faruque 2016, Kubiak 2020] used Zoom H6 / Behringer C-1U pro mics, which is unrealistic for an opportunistic attacker. Hardware: Elegoo Neptune 3 FDM printer.

**Defense landscape update (2026):** Bambu AMNC is a **hardware** acoustic countermeasure on shipping printers; QuietPrint SHM remains the primary **software-only** research defense. AMNC validated on Bambu; SHM validated on Elegoo Neptune 3 — different deployment models [@sources/2026-yocam-amnc-bambu-side-channel.md].

**Three acoustic leakage sources** identified:
1. **Power-supply cooling fan** — uncorrelated with motion, noise.
2. **Stepper motors** — energizing coils sequentially generates motion-correlated peaks at 100-600 Hz; sudden direction changes produce sharp spikes.
3. **Nozzle cooling fans** — produce a high-pitch ~8 kHz tone whose energy is linearly correlated with horizontal distance to the microphone (closer = louder), giving the attacker a deterministic distance estimate.

**Reconstruction baseline (the attack):** filter audio 100-600 Hz, detect peaks via Savitzky-Golay smoothing, multiply time-difference by constant feed rate (1200 mm/min), toggle direction sign — recovers the X-axis trajectory of the test object.

**Defense — Stealth Head Movement (SHM):**
1. Bound the original shape in a rectangle; extend every motion to the rectangle boundary by adding a collinear point in the same direction. The attacker recovers only the rectangle, not the shape.
2. Naive bounding triples the print time (the rectangle area equals the triangle area + 2× return motion).
3. Optimize via convex-hull rewriting: maximize R(x) = D(x) − A(x) where D is **Procrustes dissimilarity** between original and obfuscated shape and A is the count of added obfuscation points. Add random rectangles intersecting the convex hull, record (area, dissimilarity), pick the shape with max reward, apply binary closing.
4. Penalty: ~55% print-time overhead on a 258-second three-layer key-shaped object.

**Validation that the obfuscation works**: trained an XGBoost regressor (300 segments, 30% test, 90/10 frequency-flattened spectrograms) to detect the boundary transition between normal and extended motion → 33.79% mean absolute percentage error, Pearson r = 0.4. The transition points are not detectable. Tested on a key blade: the teeth (the security-critical bitting) are obfuscated.

**Practical bearing for a Bambu user with proprietary designs**: SHM-class defenses are software-only and require no printer hardware change. Asgar publishes the algorithm; productizing as a slicer plugin is plausible. **Caveat**: this defends only against acoustic leakage. Optical [@sources/2025-chattopadhyay-one-video-optical.md], magnetic [@sources/2025-jamarani-acoustic-magnetic-decoding.md], and power [Gatlin 2021] side channels are unaffected. A holistic defense requires per-channel mitigations.

**Limitations** [TENTATIVE]:
- Validated only on simple shapes (triangle, key) printed on one printer (Elegoo Neptune 3). Whether SHM generalizes to multi-extruder, multi-axis, or CoreXY topologies (Bambu X1C is CoreXY) is open.
- 55% time overhead is on a tiny three-layer specimen; real prints (hours) have not been benchmarked.
- Asgar assumes the *attacker* doesn't anticipate SHM. A model trained on SHM-obfuscated traces could in principle re-decode the original shape; not tested.

## Snippets

> "We propose the concept of Stealth Head Movement (SHM). In this method, we extend the normal motion of the 3D printer's head in such a way that even if the attacker can decode the acoustic signal and recover the shape, the recovered shape will be different than the original one."
[Source: 2026-asgar-quietprint-acoustic-defense.pdf p.5]

> "The normal print time for this three-layer object was approximately 258 seconds. SHM Approach added around 143 seconds, resulting in a 55% increase in print time."
[Source: 2026-asgar-quietprint-acoustic-defense.pdf p.7]

> "[XGBoost regressor on transition points] The model showed a high mean absolute percentage error of 33.79% and a low Pearson correlation coefficient of 0.4. These results suggest that it is not feasible for an attacker to identify the transition points."
[Source: 2026-asgar-quietprint-acoustic-defense.pdf p.5]

> "We selected Procrustes analysis as the metric to measure dissimilarity between two shapes. … higher values indicate greater differences between the two shapes."
[Source: 2026-asgar-quietprint-acoustic-defense.pdf p.7]
