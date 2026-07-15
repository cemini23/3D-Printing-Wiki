---
title: OrcaSlicer V2.4.2 — maintenance release (profiles / cloud / Bambu plugin)
type: source
tags: [news, OrcaSlicer, slicer, digest, release]
keywords: [OrcaSlicer 2.4.2, SoftFever, cloud sync, Bambu network plugin, pressure advance crash]
related:
  - entities/slicers/orcaslicer.md
  - sources/2026-orcaslicer-2-4-stable-release.md
  - sources/2026-06-02-digest-orcaslicer-2-4-news.md
  - entities/slicers/bambu-studio.md
maturity: validated
created: 2026-07-15
updated: 2026-07-15
read_status: skimmed
---

## Relations

@entities/slicers/orcaslicer.md @sources/2026-orcaslicer-2-4-stable-release.md @sources/2026-06-02-digest-orcaslicer-2-4-news.md @entities/slicers/bambu-studio.md

## Raw Concept

- **Type:** GitHub release notes (SoftFever / OrcaSlicer org)
- **Tag:** `v2.4.2` — published 2026-07-07
- **URL:** https://github.com/SoftFever/OrcaSlicer/releases/tag/v2.4.2
- **Digest:** 2026-07-15 sweep R1 (Tweakers mirror)
- **Retrieved:** 2026-07-15

## Narrative

Maintenance patch on **2.4.1**. Theme: dependable profiles, cloud sync, and printer connectivity — not a feature-major like 2.4.0.

### Notable fixes / additions [CONFIRMED — GitHub body 2026-07-15]

- Presets survive renames/removals of parent printer/filament (fewer “missing preset” warnings on upgrade)
- Cloud sync: disabled filaments no longer re-enable; clearer which preset is syncing; dual-instance same-account logout reduced
- **Bambu network plugin** install/update reliability (incl. Windows version switches)
- Crash fixes: prime-tower rotate, Measure tool, Pressure Advance calibration
- Slicing / print-time estimate fixes; Reload from Disk for STEP after project reopen
- New: `{first_object_name}` filename placeholder; clickable Wiki links in Preferences; add:north filament profiles
- Distribution: Microsoft Store + Flathub still advertised

Mac universal DMG ≈ **246 MB** (under 500 MB adopt budget) — **not installed on this laptop** at Phase-0 check (no `/Applications/OrcaSlicer*.app`); friend path remains **Orca-Flashforge**, which may lag SoftFever tags.

**Phase-0 verdict unchanged:** **CONDITIONAL-GO** for calibration instrument only (@entities/slicers/orcaslicer.md). Pin version; do not auto-chase every patch on Flashforge fork without fork changelog.

## Snippets

> "This is the OrcaSlicer V2.4.2 release — a maintenance update on top of 2.4.1, focused on making profiles, cloud sync, and printer connectivity more dependable."
[Source: https://github.com/SoftFever/OrcaSlicer/releases/tag/v2.4.2 (retrieved 2026-07-15)]
