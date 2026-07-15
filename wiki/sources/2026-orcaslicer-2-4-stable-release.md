---
title: OrcaSlicer V2.4.0 stable — release notes (wiki verified)
type: source
tags: [news, OrcaSlicer, slicer, vendor-adjacent, digest]
keywords: [OrcaSlicer 2.4, stable release, Orca Cloud, 3MF send, Microsoft Store, ZAA, gyroid]
related:
  - entities/slicers/orcaslicer.md
  - entities/slicers/bambu-studio.md
  - sources/2026-06-02-digest-orcaslicer-2-4-news.md
  - concepts/bambu-ecosystem-closed-loop.md
  - sources/2026-orcaslicer-2-4-2-release.md
maturity: validated
created: 2026-06-25
updated: 2026-07-15
read_status: deep-read
---

## Relations

@entities/slicers/orcaslicer.md @entities/slicers/bambu-studio.md @sources/2026-06-02-digest-orcaslicer-2-4-news.md @concepts/bambu-ecosystem-closed-loop.md @sources/2026-orcaslicer-2-4-2-release.md

## Raw Concept

- **Type:** official release notes (digest R1, 2026-06-25 sweep)
- **URL:** https://www.orcaslicer.com/wiki/releases/release_2_4_0.html
- **Prior coverage:** @sources/2026-06-02-digest-orcaslicer-2-4-news.md documented **V2.4.0 Alpha** (2026-05-25 GitHub)
- **Retrieved / verified:** 2026-06-25

## Narrative

**V2.4.0 stable** ships everything from Alpha + Beta. @entities/slicers/orcaslicer.md **CONDITIONAL-GO unchanged** — calibration / advanced tuning instrument, not daily Bambu Studio replacement.

### Stable-only deltas vs Alpha [CONFIRMED — Orca wiki 2026-06-25]

| Feature | Detail |
|---------|--------|
| **Send as packaged 3MF** | Per-printer option "Use 3MF instead of G-code" (off default); sends `.gcode.3mf` with slice metadata; export-only toggle (no re-slice). Fixes #11173. |
| **Microsoft Store channel** | MSIX for Windows 11 Smart App Control; submission under Microsoft review at release time — classic NSIS/portable unchanged until Store listing live. |
| **Orca Cloud offline login** | Session in keystore / encrypted local store — profiles usable offline; downgrading Orca version logs out (session format change). |
| **Subscribed preset update notification** | Plater notification when cloud preset has update. |
| **Sync conflict fix** | Cloud sync no longer silently deletes locally recreated preset with same name as deleted cloud preset. |
| **Slice-to-preview speed** | Cached G-code post-processing patterns; ~37% single Benchy / ~65% 16-Benchy plate on Klipper-flavor printers (author benchmark; byte-identical G-code claimed). |
| **Skirt overhaul** | Collision-aware per-object skirts; correct skirt→brim print order. |
| **Bug-fix batch** | Tree supports clearance, multi-color preview view persistence, motion-ability settings on multi-variant printers (U1/H2D), YOLO flow tile order, Creality non-ASCII upload filenames, Flatpak config migration ID fix. |

### Carried from Alpha/Beta (unchanged summary)

Orca Cloud, Z Anti-Aliasing (ZAA), Optimized Gyroid infill, Machine Input Shaping, Realistic View, bridging overhaul, Troubleshoot Center, Moonraker / 3DPrinterOS hosts, Creality K-series profiles.

### Flashforge / Orca-Flashforge note

Release notes target upstream OrcaSlicer. **Orca-Flashforge** fork may lag — pin fork version and check fork release notes before adopting ZAA / 3MF-send on Adventurer 5M workflows.

## Snippets

> "This is the OrcaSlicer V2.4.0 release. It focuses on bug fixes, a smoother Orca Cloud experience, and new features such as sending sliced jobs to the printer as a packaged 3MF."
[Source: https://www.orcaslicer.com/wiki/releases/release_2_4_0.html (retrieved 2026-06-25)]

> "Note: Everything from the 2.4.0 Alpha and 2.4.0 Beta is included in this build."
[Source: https://www.orcaslicer.com/wiki/releases/release_2_4_0.html (retrieved 2026-06-25)]
