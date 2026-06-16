---
title: Side-Channel Attacks on 3D Printers
type: concept
tags: [security, side-channel, attack-surface, fundamentals]
keywords: [acoustic, optical, magnetic, power, vibration, thermal, electromagnetic, eavesdropping, IP theft, FDM, PBF]
related:
  - concepts/ip-theft-3d-printing.md
  - concepts/g-code-protection.md
  - concepts/fdm-printing.md
  - sources/2026-asgar-quietprint-acoustic-defense.md
  - sources/2025-chattopadhyay-one-video-optical.md
  - sources/2025-jamarani-acoustic-magnetic-decoding.md
  - sources/2025-dolgavin-hearsay-pbf-power.md
  - sources/2026-yocam-amnc-bambu-side-channel.md
maturity: draft
created: 2026-05-06
updated: 2026-06-16
---

## Relations

@concepts/ip-theft-3d-printing.md @concepts/g-code-protection.md @concepts/fdm-printing.md @sources/2026-asgar-quietprint-acoustic-defense.md @sources/2025-chattopadhyay-one-video-optical.md @sources/2025-jamarani-acoustic-magnetic-decoding.md @sources/2025-dolgavin-hearsay-pbf-power.md @sources/2026-yocam-amnc-bambu-side-channel.md

## Raw Concept

A 3D printer's actuators (steppers, galvanometers, lasers, fans, extruders) produce physical emanations that correlate tightly with the G-code being executed. An adversary measuring those emanations can recover the design — even if the G-code itself is encrypted in transit and at rest. Hub page synthesizing the six side-channel modalities demonstrated against AM systems and the prior-attack landscape as of 2026-05-06.

## Narrative

A **side-channel** is an unintended physical emanation from a process that correlates with what the process is doing. In 3D printing, the process is "execute G-code instructions"; the emanations are acoustic, optical, magnetic, electrical, mechanical, and thermal. Whenever the correlation is tight, an adversary can reason backwards from the signal to the original instruction stream — and reconstruct the design.

### The six demonstrated side channels

| Modality | First demonstrated | Best-result reference | Notes |
|---|---|---|---|
| **Acoustic** | Faruque 2016 (FDM, Zoom H6) | Jamarani 2025: 4.47% MTE on a "plain G-code" with smartphone | Stepper motors and fan noise; MFCC + GBDT works well [@sources/2025-jamarani-acoustic-magnetic-decoding.md]. **Bambu AMNC (2026):** deployed countermeasure on P1P/A1 Mini — acoustic ID at random chance [@sources/2026-yocam-amnc-bambu-side-channel.md] |
| **Optical** | Liang 2022 NDSS (FDM, ResNet-50) | Chattopadhyay 2025 CCS: 90.87% similarity, functional counterfeit key from one IP-camera video | Bambu X1C internal camera is in scope [@sources/2025-chattopadhyay-one-video-optical.md] |
| **Magnetic** | Song 2016 (FDM, smartphone) | Jamarani 2025 fuses magnetic + acoustic | Magnetic falls off as 1/r³ — short range only |
| **Power** | Gatlin 2021 (FDM stepper currents, ~99% spatial accuracy) | Dolgavin 2025 (industrial PBF, 90.29% TP voxel volume) | Scales from FDM to industrial PBF [@sources/2025-dolgavin-hearsay-pbf-power.md]; defeats end-to-end design encryption |
| **Vibration / inertial** | Stańczak 2021 (FDM accelerometer chassis-mounted) | Gao 2024 (multimodal FDM); Yocam 2026: ~61% closed-set ID with temporal model on AMNC-equipped Bambu (vibration not cancelled) [@sources/2026-yocam-amnc-bambu-side-channel.md] | Effective, but requires physical contact with chassis; AMNC does not address |
| **Thermal** | Faruque 2018 (FDM, IR camera) | — | Lower-bandwidth than acoustic / optical; less mature |

Source: [Source: 2025-dolgavin-hearsay-pbf-power.pdf Table I] enumerates all FDM-side-channel attacks; 2025 Chattopadhyay et al. + 2025 Dolgavin et al. extend the table beyond FDM.

### The threat model continuum

From cheapest / most accessible to most invasive:

1. **Compromised existing IP camera** (Chattopadhyay 2025) — operator already runs a remote-monitoring camera; adversary just needs network access. Most realistic in commercial environments. Bambu X1C ships with one.
2. **Smartphone in proximity** (Jamarani 2025, Song 2016) — co-worker, cleaner, family member with their phone in the same room. No printer modification.
3. **Planted recorder** (Faruque 2016 / Zoom H6, Kubiak 2020 / Behringer C-1U) — adversary plants pro-grade audio gear. Less realistic for stealth but achievable on shared print farms.
4. **Insider with physical access** (Dolgavin 2025) — instrument actuator power supplies once, then collect non-intrusive traces during normal operation. The MATE (Man-At-The-End) threat. Realistic at outsourcing AM-service providers.

### Why this is hard to defend against

- **Single-channel defenses don't cover other channels.** QuietPrint's Stealth Head Movement [@sources/2026-asgar-quietprint-acoustic-defense.md] obfuscates acoustic *and* magnetic stepper emanations (because both come from the same motor) but leaves optical (camera), power (current taps), and thermal (IR cam) untouched. **Bambu AMNC** [@sources/2026-yocam-amnc-bambu-side-channel.md] is the inverse specialization: hardware acoustic cancellation only; vibration channel remains partially leaky.
- **Encryption alone is futile** when the printer itself leaks (Dolgavin 2025: "encryption is futile"). The actuators decode the G-code internally and act on it physically; that physical action is observable.
- **ML attacks are robust to noise-injection countermeasures.** Chattopadhyay 2025 explicitly argues that degrading the optical channel (e.g., reducing camera resolution or adding visual noise) doesn't stop a ResNet-50+LSTM that uses temporal context. [TENTATIVE — paper's own claim, not independently validated.]

### Defense classes (cross-references)

- **G-code obfuscation** [@concepts/g-code-protection.md] — Stealth Head Movement is the only published one.
- **Physical isolation** — locked print room; works against acoustic / magnetic / IP-camera but not against insiders.
- **Channel-specific masking** — speakers (Stańczak 2023, ~€1000) for acoustic; optical equivalents not yet productized.
- **Defense-in-depth** — combine the above.

## Snippets

> "Side-channels are (unintended) physical emanations produced by cyber or cyber-physical processes. … Whenever there is a tight correlation between the measured physical signal's property and the process that caused this emanation, it becomes possible to reason about this process by analyzing the side-channel data."
[Source: 2025-dolgavin-hearsay-pbf-power.pdf p.2]

> "The lesson learned from our attack is that the security of AM design files cannot rely solely on protecting the files themselves in an industrial environment."
[Source: 2025-dolgavin-hearsay-pbf-power.pdf p.1]
