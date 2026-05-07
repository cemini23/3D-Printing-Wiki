---
title: "Turning Hearsay into Discovery: Industrial 3D Printer Side-Channel Information Translated to Stealing the Object Design"
type: source
tags: [paper, security, attack, power, side-channel, industrial, PBF, Sintratec]
keywords: [Powder Bed Fusion, PBF, Sintratec S2, galvanometer, NI USB-6363, Fluke i310, differential voxelization, DPA, voxel pruning, industrial AM, Auburn, Google, Columbia]
related:
  - concepts/side-channel-attacks.md
  - concepts/ip-theft-3d-printing.md
  - concepts/g-code-protection.md
  - sources/2026-asgar-quietprint-acoustic-defense.md
  - sources/2025-chattopadhyay-one-video-optical.md
  - sources/2025-jamarani-acoustic-magnetic-decoding.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
read_status: deep-read
---

## Relations

@concepts/side-channel-attacks.md @concepts/ip-theft-3d-printing.md @concepts/g-code-protection.md @sources/2026-asgar-quietprint-acoustic-defense.md @sources/2025-chattopadhyay-one-video-optical.md @sources/2025-jamarani-acoustic-magnetic-decoding.md

## Raw Concept

- Title: Turning Hearsay into Discovery: Industrial 3D Printer Side-Channel Information Translated to Stealing the Object Design
- Authors: Aleksandr Dolgavin, Jacob Gatlin (Auburn), Moti Yung (Google / Columbia), Mark Yampolskiy (Auburn)
- Type: arXiv preprint, arXiv:2509.18366
- Location: `raw-sources/2025-dolgavin-hearsay-pbf-power.pdf`
- Retrieved: 2026-05-06
- Pages: 18
- Read-status: deep-read

## Narrative

**The first side-channel attack demonstrated against an industrial 3D printer.** All prior demonstrated side-channel reconstructions [Faruque 2016, Hojjati 2020, Song 2016, Gao 2024, Gatlin 2021, Stańczak 2021, Pearce 2022, Jamarani 2025, Chattopadhyay 2025] used desktop FDM printers — which the paper bluntly notes "play a negligible role in manufacturing of valuable designs." Dolgavin et al. take the attack to **Powder Bed Fusion (PBF)** — the dominant technology for net-shaped industrial parts in polymers and metals — proving that the AM industrial outsourcing ecosystem (>2000 service providers, $21.9B market 2024 → projected $114.5B in 10 years) cannot rely solely on file-level IP protection.

**Why this matters.** The industrial-AM threat model is **Man-At-The-End (MATE)**: a malicious manufacturer or insider has physical access to the printer. DRM-based and TPM-based design protection ([5][6][10][11]), encrypted streaming (Identify3D, Assembrix), and chunked-STL streaming all assume the printer itself is trustworthy. Power-side-channel attacks defeat that assumption — **encryption is futile** if the actuator-level signals leak the design.

**Target machine**: Sintratec S2 polymer PBF. Selected because (a) its actuator topology mirrors metal PBF (galvanometers + recoater + powder cells + print bed) so the result generalizes, (b) polymer powder isn't combustible (metal powder is hazardous; severe injuries are documented).

**Instrumentation (11 probes total)**:
- 1× laser power supply — Fluke i310 inductive current probe (clamped, non-intrusive).
- 2× X- and Y-galvanometers — voltage divider on the Eye Magic galvanometer control board's "Position Out" test point (-10 V to +10 V analog signal mapping to mirror angle and laser target). Inductive clamps on the galvo ribbon cable failed because those carry digital logic; the analog control is internal, forcing the voltage-tap approach.
- 6× stepper motors — print bed, two powder cells, recoater steppers — Fluke i310 clamps, both phases each.
- DAQ: National Instruments USB-6363 / 782258-01, 16 BNC channels, 20 kHz sampling per channel (intentional Nyquist oversampling), TDMS file format, NI FlexLogger / DIADEM.
- Top of S2 enclosure redesigned with safe cable routing while preserving laser containment.

**Reconstruction pipeline (Sintratec ASTM E8 + Gear test specimens)**:
1. **Identify Layer Sintering boundaries** via finite-state machine on the laser ON/OFF signal: thresholds 2.2 V (ON), 1.1 V (OFF); LS→LT transition only after 1000 consecutive OFF samples to handle scanning-strategy gaps within a layer. Counts layers automatically (101 for ASTM specimen).
2. **Galvanometer signal preprocessing**: 4th-order Butterworth low-pass at 6 kHz on raw GalvoX/GalvoY; aggressive 1 kHz LPF on layer 51 (the ASTM diameter-defining middle layer) to determine raster size.
3. **Determine raster size**: ASTM E8 cylinder is round → max layer diameter equals total height (101 layers × layer height) → raster = max GalvoXY deviation / 101 ≈ 0.001 V → cubical voxels. Adopted 0.0025 V instead to compensate for residual noise (trade-off: larger raster = larger positional error ±½ raster, but more robust to laser noise spikes).
4. **Rasterize per layer**: each (LayerNr, RasterX, RasterY) voxel gets a `HitCtr` (count of laser-ON samples falling inside).
5. **Differential Voxelization** — the paper's core conceptual contribution. Inspired by **Differential Power Analysis** [Kocher et al. 1999] for cryptographic key recovery: aggregate `HitCtr` across multiple voxelized traces of the same object (3 ASTM prints in their experiment). Random noise sums incoherently; real-signal voxels accumulate. Increases SNR and enables more aggressive voxel pruning.
6. **Voxel pruning** — two strategies in series:
   - **HitCtr threshold**: 0.0025 V raster → 41.75% of cells were 1-hit only; pruned (single-trace threshold = 1, differential threshold = 3).
   - **Neighborhood**: count "lit" voxels in a 3D box around each voxel. Single-trace: distance 5, min-neighbors 33 (slightly above ¼ of max 120); differential: distance 4, min-neighbors 22.
7. **Filling the gaps** — model-specific. For Gear (no overhangs): project all (x,y,*) voxels to highest z, prune by aggregated HitCtr (threshold 20), then re-fill below-projection voxels with HitCtr=1. For ASTM: project both up and down from middle.
8. **Distortion correction** — XY distortion matrix from Gear (known geometry); Z-axis scaling factor from ASTM (known proportions); proportion correction from physical part measurements.

**Headline metrics** (voxel-volumetric comparison, reconstructed model vs original STL):
- **90.29% True Positives**, **7.02% False Positives**, **9.71% False Negatives** on the more complex of the two designs.

**Why "differential voxelization" not "differential trace"**: paper considered aggregating raw traces (signal-domain DPA) but rejected it. LSi durations across 3 traces deviated by 1-6 polling intervals (50-300 µs at 20 kHz) — not aligned tightly enough. Voxelization happens *after* discretization, so misalignments don't matter.

**Limitations / scope** [TENTATIVE]:
- The Sintratec S2 is a polymer, not metal, PBF — galvanometer dynamics differ between polymer-laser-sintering and laser-powder-bed-fusion-of-metals; generalization claimed, not proven.
- Test specimens (ASTM E8 cylinder, Gear) are simple. The "Filling the Gaps" step is *not generalizable* per the paper's own admission — gap-fill heuristics depend on print orientation and geometry.
- The attack is "known design" — analogous to known-plaintext cryptanalysis. Adversary needs prior trace-design pairings to learn voltage-to-position mapping. This is realistic for a malicious AM-service insider who runs test prints, but constraints the threat model.
- Galvanometer voltage tap requires opening the printer enclosure once for instrumentation; afterwards, traces can be collected non-intrusively.

**Practical bearing**: this is a paper about industrial outsourced AM, not consumer FDM. **It does not directly affect a Bambu user's threat model** — Bambu printers don't have galvanometers, don't run laser PBF, and a hobbyist isn't sending a digital design to a third-party industrial bureau. **It does affect anyone outsourcing an SLS / DMLS / SLM design to a third party** for engineering-grade parts, especially in regulated sectors (aerospace, medical, defense). The takeaway: even if the digital design is encrypted end-to-end, the physical printer leaks the design through its actuator power profile.

## Snippets

> "We focus on the Powder Bed Fusion (PBF) AM process, which is popular for manufacturing net-shaped parts with both polymers and metals. We demonstrate how its individual actuators can be instrumented for the collection of power side-channel information during the printing process."
[Source: 2025-dolgavin-hearsay-pbf-power.pdf p.1]

> "For different models, we achieved as high as 90.29% of True Positives and as low as 7.02% and 9.71% of False Positives and False Negatives by voxel-based volumetric comparison between reconstructed and original designs."
[Source: 2025-dolgavin-hearsay-pbf-power.pdf p.1]

> "The lesson learned from our attack is that the security of AM design files cannot rely solely on protecting the files themselves in an industrial environment. Instead, it must also rely on ensuring that no leakage of power, noise, and similar signals can be detected by potential eavesdroppers in the printer's vicinity."
[Source: 2025-dolgavin-hearsay-pbf-power.pdf p.1]

> "We take our inspiration for the proposed differential voxelization from the work of Kocher et al. [26] who introduced Differential Power Analysis (DPA) for breaking cryptographic keys. The fundamental idea is that multiple traces collected for the execution of the same process can be aggregated to amplify the analyzed signal."
[Source: 2025-dolgavin-hearsay-pbf-power.pdf p.8]
