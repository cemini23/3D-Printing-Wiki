---
title: OrcaSlicer 2.4 Alpha — Digest News (verified against GitHub release)
type: source
tags: [news, OrcaSlicer, slicer, vendor-adjacent, digest]
keywords: [OrcaSlicer 2.4, Z anti-aliasing, gyroid infill, Orca Cloud, GitHub release]
related:
  - entities/slicers/orcaslicer.md
  - entities/slicers/bambu-studio.md
  - concepts/bambu-ecosystem-closed-loop.md
maturity: draft
created: 2026-06-02
updated: 2026-06-05
read_status: deep-read
---

## Relations

@entities/slicers/orcaslicer.md @entities/slicers/bambu-studio.md @concepts/bambu-ecosystem-closed-loop.md

## Raw Concept

- Type: web news (digest lane Q1, 2026-06-02) + **GitHub release notes verification** (2026-06-05)
- URLs: [All3DP OrcaSlicer 2.4](https://all3dp.com/4/massive-orcaslicer-update-lands-with-z-anti-aliasing-stronger-gyroid-infill-and-a-cloud-of-its-own/) (2026-05-27); [OrcaSlicer V2.4.0 Alpha release](https://github.com/OrcaSlicer/OrcaSlicer/releases) (2026-05-25); [3druck Prusa license story](https://3druck.com/en/industry-2/prusa-accuses-several-chinese-slicer-manufacturers-of-license-violations-06157691/) (2026-05-28)
- Retrieved: 2026-06-02; verified: 2026-06-05

## Narrative

### OrcaSlicer V2.4.0 Alpha [CONFIRMED — GitHub release 2026-05-25]

Pre-release tag **V2.4.0 Alpha**. Headline features match All3DP digest:

| Feature | Detail |
|---------|--------|
| **Orca Cloud** | Optional sync at [cloud.orcaslicer.com](https://cloud.orcaslicer.com) — profile sync, version history, preset bundles, community explore. **Local profiles still work without login.** Data hosted USA; optional future regional servers. |
| **Z Anti-Aliasing (ZAA)** | Expert-mode quality setting; raycasts extrusion points against mesh to micro-adjust Z on curved/sloped top surfaces (`zaa_enabled`, `zaa_min_z`, etc.). |
| **Optimized Gyroid infill** | Experimental per-region wavelength/amplitude tuning via Euler-Bernoulli buckling physics (CRAMP project); off = byte-identical to standard gyroid. |
| **Other** | Expert user mode, native Wayland (Linux), Machine Input Shaping, Prusa-style combined brims, fuzzy-skin ripple mode, redesigned printer picker. |
| **Known issues** | Release points to GitHub issue **#13828** for alpha regressions. |

**Workflow guidance [CONFIRMED].** @entities/slicers/orcaslicer.md **CONDITIONAL-GO** unchanged: use 2.4 alpha for **calibration experiments** (ZAA on domes, gyroid tuning), not as daily Bambu Studio replacement — profile schema divergence + alpha stability risk.

### Prusa vs Chinese slicers [TENTATIVE]

Industry press (3druck) reports Prusa accusing Chinese forked slicers of **license violations** — relevant AGPL lineage context for OrcaSlicer. **Primary Prusa statement not deep-read** — treat as background, not actionable for Flashforge reader.

### Bambu wiki churn

Digest also flagged Bambu wiki updates — cross-check filament claims against @sources/2026-bambu-filament-guide.md when upgrading profiles.

## Snippets

> "This is the OrcaSlicer V2.4.0 Alpha release. The headline feature is Orca Cloud — a new centralized platform for profile sync, preset bundle sharing, and community discovery at cloud.orcaslicer.com."
[Source: https://github.com/OrcaSlicer/OrcaSlicer/releases (retrieved 2026-06-05)]

> "Z Anti-Aliasing (ZAA) reduces visible stair-stepping on curved and sloped top surfaces by raycasting each extrusion point against the original 3D mesh and micro-adjusting the Z height to follow the actual surface geometry."
[Source: https://github.com/OrcaSlicer/OrcaSlicer/releases (retrieved 2026-06-05)]

> "Note: Orca Cloud is optional. Local profiles and existing OrcaSlicer workflows continue to work as before."
[Source: https://github.com/OrcaSlicer/OrcaSlicer/releases (retrieved 2026-06-05)]
