---
title: G-Code Protection
type: concept
tags: [security, defense, g-code, encryption, obfuscation, streaming]
keywords: [Stealth Head Movement, SHM, G-code encryption, streaming, blockchain, STL chunking, TPM, DRM, Identify3D, Assembrix, OctoPrint, LAN mode]
related:
  - concepts/side-channel-attacks.md
  - concepts/ip-theft-3d-printing.md
  - concepts/fdm-printing.md
  - concepts/am-as-a-service.md
  - sources/2026-asgar-quietprint-acoustic-defense.md
  - sources/2025-chattopadhyay-one-video-optical.md
  - sources/2025-jamarani-acoustic-magnetic-decoding.md
  - sources/2025-dolgavin-hearsay-pbf-power.md
  - sources/2025-ivkic-cost-benefit-maas.md
  - sources/2026-yocam-amnc-bambu-side-channel.md
maturity: draft
created: 2026-05-06
updated: 2026-06-16
---

## Relations

@concepts/side-channel-attacks.md @concepts/ip-theft-3d-printing.md @concepts/fdm-printing.md @concepts/am-as-a-service.md @sources/2026-asgar-quietprint-acoustic-defense.md @sources/2025-chattopadhyay-one-video-optical.md @sources/2025-jamarani-acoustic-magnetic-decoding.md @sources/2025-dolgavin-hearsay-pbf-power.md @sources/2025-ivkic-cost-benefit-maas.md @sources/2026-yocam-amnc-bambu-side-channel.md

## Raw Concept

What can a designer actually deploy today to keep their G-code secret? Inventories the four published defense classes and rates them against the four attack tiers from [@concepts/side-channel-attacks.md].

## Narrative

The defense landscape splits into **file-level** (protecting the bytes) and **physical-level** (protecting against side-channel emanations). File-level defenses are mature; physical-level defenses are still mostly research.

### File-level defenses

1. **G-code encryption at rest** (Tiwari 2020, ALM-encryption [28]). G-code stored encrypted; printer firmware decrypts in memory just before execution. Defeats malicious insiders / network sniffing during transfer. **Does not defeat side-channel attacks** because the printer still decrypts and acts on the plaintext physically.

2. **Direct G-code streaming** (Baumann 2017, Tiwari 2020). The designer holds the G-code file; sends it instruction-by-instruction over a secure channel to the printer at print time. No persisted G-code on the manufacturer's storage. Reduces the file-theft window. **Vulnerability**: stream-injection attack — an MITM injects malicious G-code commands during transmission, potentially damaging the machine [Source: 2026-asgar-quietprint-acoustic-defense.pdf p.1]. **Mitigation** (Asgar 2025 [6]): send chunked STL fragments instead of G-code, since STL contains only design data, not machine commands; the printer slices on its own.

3. **Blockchain-based G-code storage** (referenced in Jamarani 2025 [27]). Tamper-evident audit log of G-code modifications. Useful for provenance and anti-tampering, less so for confidentiality.

4. **DRM / TPM secure boot** (Identify3D / Materialise [12], Assembrix [14]). Industrial-grade. Designs are bound to specific printers via a TPM; the design file decrypts only inside an attested boot environment. **Defeats** file-level theft and most insider scenarios. **Does not defeat** Man-At-The-End (MATE) physical-side-channel attacks (Dolgavin 2025 [@sources/2025-dolgavin-hearsay-pbf-power.md]).

### Physical-level defenses (against side-channel attacks)

Far less mature. Three published approaches:

1. **Active acoustic masking** (Stańczak 2023, [29] in QuietPrint refs). Place an amplified speaker behind the printer, generate noise that swamps the SNR of the leaked signal. Cost: ~€1000 + space for the speaker. Effective for acoustic but doesn't help with optical / magnetic / power.

2. **Stealth Head Movement (SHM)** (Asgar 2026 [@sources/2026-asgar-quietprint-acoustic-defense.md]). G-code rewriter: bound the print path inside its convex hull, extend each motion to the hull boundary, optimize the dummy-motion area for max Procrustes dissimilarity vs min added area. The attacker recovers the convex hull, not the original part. ~55% print-time overhead on a small specimen. **Software-only**, no printer hardware change. **Coverage**: defeats acoustic + magnetic stepper-noise leakage simultaneously (both come from the motor). **Does not defend** against optical (camera sees the actual hull-boundary motion, not the obfuscated trajectory) or power side-channels.

3. **G-code obfuscation via dummy commands** (no published productized version; see "Hiding My Real Self" [Liang & Beyah, undated, cited in Asgar 2026 [19]]). Inject decoy moves that don't physically extrude. Less developed than SHM.

4. **Active Motor Noise Cancellation (AMNC)** — Bambu Lab firmware/hardware on P1P and A1 Mini [@sources/2026-yocam-amnc-bambu-side-channel.md]. Adaptive current control suppresses motor resonance frequencies targeted by acoustic SCAs. **First deployed consumer countermeasure empirically validated** (Jun 2026): acoustic closed-set ID drops to random chance. **Does not address** chassis vibration, optical, magnetic, or power channels.

### Operational defenses (deployable today on a Bambu)

For the reader's Tier 1-2 use case [@concepts/ip-theft-3d-printing.md]:

| Defense | What | Coverage |
|---|---|---|
| **Bambu LAN-only mode** | Disable cloud sync; OrcaSlicer / Bambu Studio over LAN only | Cuts the IP-camera-on-cloud attack surface (Chattopadhyay 2025) |
| **Disable AI failure-detection image upload** | Bambu Studio setting | Same |
| **Physical isolation** | Print in a locked room, no smartphones / mics in the room | Defeats Tiers 1-2 acoustic / magnetic / optical |
| **X1C enclosure** | Side benefit, not security feature | Acoustic attenuation [TENTATIVE — Bambu doesn't claim this] |
| **Local-only G-code** | USB-stick transfer instead of network | Defeats network-level G-code theft |
| **Watermark designs** | Subtle surface features that survive copying; recoverable in court | File-level piracy deterrent |

### Coverage matrix — what protects against what

| Defense | File theft | Acoustic | Optical | Magnetic | Power | MATE |
|---|---|---|---|---|---|---|
| G-code encryption at rest | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Direct streaming | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| TPM / Identify3D | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Active acoustic masking | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **SHM** (Asgar 2026) | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| **AMNC** (Bambu P1P/A1 Mini) | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Physical isolation | ❌ | ✅ | ✅ | ✅ | partial | ❌ |
| LAN-only / camera off | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| **Defense-in-depth** | ✅ | ✅ | ✅ | ✅ | partial | partial |

[CONFIRMED] No single defense covers all six attack surfaces. [CONFIRMED] No published defense covers MATE for industrial AM as of 2026-05-06. The strongest realistic posture is layered: file-level encryption + LAN-only / camera-off + isolated print room + SHM-class G-code obfuscation for residual leakage.

## Snippets

> "The main advantage of our approach is that it requires no additional hardware and is fully compatible with existing 3D printers. Implementation involves only minimal modifications to the G-code file to incorporate the SHM algorithm, eliminating the need for any extra setup such as noise-canceling or noise-generating devices."
[Source: 2026-asgar-quietprint-acoustic-defense.pdf p.8]

> "If an attacker intercepts the streaming process and begins injecting malicious G-code commands during transmission, it can result in damage to the AM machine. … Since these STL fragments contain only inert design data and no machine commands, this method also mitigates the manufacturer's concerns."
[Source: 2026-asgar-quietprint-acoustic-defense.pdf p.1]
