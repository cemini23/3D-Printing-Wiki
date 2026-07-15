---
title: Side-Channel Attacks Bypass Protection in 3D Printers (AMNC eval)
type: source
tags: [paper, security, side-channel, acoustic, vibration, bambu, AMNC, defense]
keywords: [2606.13952, Active Motor Noise Cancellation, P1P, A1 Mini, vibration side channel, Madamopoulos dataset]
related:
  - concepts/side-channel-attacks.md
  - concepts/g-code-protection.md
  - concepts/ip-theft-3d-printing.md
  - concepts/fdm-printing.md
  - entities/printers/a1.md
  - entities/printers/p1s.md
  - sources/2026-asgar-quietprint-acoustic-defense.md
  - sources/2025-jamarani-acoustic-magnetic-decoding.md
  - sources/2025-chattopadhyay-one-video-optical.md
  - sources/2026-asgar-firewall3d-firmware-hardware.md
maturity: draft
created: 2026-06-16
updated: 2026-07-15
read_status: skimmed
---

## Relations

@sources/2026-asgar-firewall3d-firmware-hardware.md @concepts/side-channel-attacks.md @concepts/g-code-protection.md @concepts/ip-theft-3d-printing.md @concepts/fdm-printing.md @entities/printers/a1.md @entities/printers/p1s.md @sources/2026-asgar-quietprint-acoustic-defense.md @sources/2025-jamarani-acoustic-magnetic-decoding.md @sources/2025-chattopadhyay-one-video-optical.md

## Raw Concept

- Authors: Eric Yocam (Cal Poly SLO), Varghese Vaidyan (Dakota State), Micah Flack (INL), Gurcan Comert (NC A&T), Judith L. Mwakalonge (SC State)
- arXiv: 2606.13952v1 (cs.CR), 15 Jun 2026
- Location: `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/2026-yocam-amnc-bambu-side-channel.pdf`
- Retrieved: from `research to be indexed/` 2026-06-16
- Read-status: skimmed (abstract + threat model + results)

## Narrative

**First empirical evaluation of a deployed hardware countermeasure** against FDM acoustic side-channel IP theft — Bambu Lab **Active Motor Noise Cancellation (AMNC)** on **P1P** (core-XY) and **A1 Mini** (bed-slinger).

**Dataset:** Madamopoulos–Tsoutsos 2024 public corpus (Zenodo 10.5281/zenodo.13329934) — synchronized iPhone audio + Teensy 4.0 triaxial accelerometer; 12 object classes; 6 paired recordings per object per printer (144 pairs). Closed-set identification threat model (not full G-code reconstruction).

**Headline findings:**

| Channel | AMNC status | Attack accuracy |
|---------|-------------|-----------------|
| **Acoustic** | AMNC active | **~8.33%** (= 1/12 random baseline) — countermeasure works |
| **Vibration** (summary stats) | Not targeted by AMNC | **~31%** pooled; 36–47% within-printer |
| **Vibration** (full-sequence temporal model) | Not targeted | **~61%**; order-shuffle control **~33%** → sequential geometry signal |
| **Cross-printer transfer** | — | Near chance — per-device calibration required |

Frequency-only vibration features at chance; **amplitude** carries the coarse leak. Authors conclude AMNC is **acoustic-only**; vibration remains a partial geometry-correlated channel but **does not support full geometric reconstruction** on this dataset. Reconstruction-grade attacks still require magnetic or power channels (also outside AMNC scope).

**Contrast with @sources/2026-asgar-quietprint-acoustic-defense.md:** QuietPrint SHM is a **software** G-code obfuscation (~55% time overhead); AMNC is **firmware/hardware** adaptive current control suppressing motor resonance. Neither covers optical (IP camera) or power side channels.

**Reader action:** AMNC-equipped Bambu owners get real acoustic-channel protection; do not treat it as complete IP defense — see `briefs/2026-06-16_bambu-amnc-vibration-side-channel.md` and @concepts/g-code-protection.md operational table.

## Snippets

> "AMNC fully neutralizes the acoustic channel: classification accuracy is indistinguishable from the 8.33% random baseline."
[Source: 2026-yocam-amnc-bambu-side-channel.pdf p.1]

> "AMNC is an acoustic-only defense: vibration remains a partial, geometry-correlated side channel it does not address, but one that does not, on this dataset, support full geometric reconstruction."
[Source: 2026-yocam-amnc-bambu-side-channel.pdf p.1]

> "A classifier trained on one printer transfers near chance to the other, showing the vibration signal is architecture-specific."
[Source: 2026-yocam-amnc-bambu-side-channel.pdf p.1]
