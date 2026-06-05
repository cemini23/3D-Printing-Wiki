---
title: Novice CAD Workflows — What to Use When You're Just Starting
type: concept
tags: [beginner, CAD, design, workflow, day-1, Tinkercad]
keywords: [novice, first prints, Tinkercad, STL download, Orca-Flashforge, design workflow, beginner]
related:
  - concepts/fdm-printing.md
  - concepts/filaments-baseline.md
  - concepts/ai-design-tools.md
  - concepts/vlm-in-manufacturing.md
  - concepts/shape-changing-fdm-interfaces.md
  - concepts/open-source-legged-robotics.md
  - entities/printers/flashforge-adventurer-5m.md
  - sources/2025-arslan-tinkerxr-ar-cad-novices.md
  - entities/tools/cursor.md
  - concepts/niche-fdm-applications.md
  - sources/2025-tran-3d-printed-acoustic-guitars.md
  - sources/2026-faulkner-lithographs-microscopy.md
  - concepts/self-improving-cad-generation-agents.md
  - sources/arxiv-2605-17448-self-improving-cad-agents.md
maturity: draft
created: 2026-05-23
updated: 2026-06-01
---

## Relations

@concepts/fdm-printing.md @concepts/filaments-baseline.md @concepts/ai-design-tools.md @concepts/vlm-in-manufacturing.md @concepts/open-source-legged-robotics.md @entities/printers/flashforge-adventurer-5m.md @sources/2025-arslan-tinkerxr-ar-cad-novices.md

## Raw Concept

Friend-handoff gap: the wiki is heavy on research clusters (print farms, security, shape-changing) that a **first-week Flashforge owner should skip**. This page is the **design-side counterpart** to `FRIEND-SETUP.md` — what to use to get models onto the bed, in order.

## Narrative

### Week 1 — don't design, print

Your first jobs are **calibration and trust-building**, not CAD:

1. Bundled test print + stock PLA (@entities/printers/flashforge-adventurer-5m.md day-1 list).
2. [@entities/tools/kickstarter-autodesk-fdm-protocol.md] FDM Test V4 on stock PLA profile.
3. Download someone else's proven STL (Printables, Thingiverse, MakerWorld) before you model anything original.

**Skip entirely in week 1:** @concepts/print-farm-operations.md, @concepts/am-as-a-service.md, @concepts/shape-changing-fdm-interfaces.md, @concepts/open-source-legged-robotics.md, security/MaaS pages.

### Week 2–4 — simple CAD without new hardware

| Tool | Cost | When | Output |
|------|------|------|--------|
| **Download STLs** | $0 | Always first choice | Import into **Orca-Flashforge** |
| **[Tinkercad](https://www.tinkercad.com)** | $0 browser | First original parts (hooks, brackets, boxes) | Export STL → Orca-Flashforge |
| **Cursor Chat + `@` wiki files** | Cursor Pro ($20/mo) | Troubleshoot prints, pick filament | No geometry — advice only (@concepts/vlm-in-manufacturing.md, @entities/tools/cursor.md) |

Tinkercad is the baseline in @sources/2025-arslan-tinkerxr-ar-cad-novices.md's user study — good enough for key hangers, cable clips, and dimensioned holders. You do **not** need Fusion 360, Blender, or AI generators yet.

### Month 2+ — optional upgrades

| Tool | Prerequisite | Notes |
|------|--------------|-------|
| **Meshy / RodinAI / 3DAIStudio** | Willing to fix manifold errors | Decorative models only → @concepts/ai-design-tools.md |
| **TinkerXR** | Meta Quest 3 + dev appetite | AR CAD experiment; CC BY-NC; exports STL — @sources/2025-arslan-tinkerxr-ar-cad-novices.md |
| **Fusion 360 / FreeCAD** | Need precise mechanical fits | Functional parts, not day-1 |

### Slicing rule (Flashforge 5M)

Every path ends in **Orca-Flashforge** with a profile matched to your filament. Never Bambu Studio. Never run G-code you didn't slice yourself or download from a trusted profile unless you've read it (@concepts/ai-design-tools.md hallucinated-G-code rule applies to random internet `.gcode` too).

### What "running a print farm" means here (not you yet)

Print-farm pages describe **many printers, scheduling, and cloud manufacturing economics**. One Adventurer 5M on a desk is a **hobby printer**, not a farm. Ignore those pages until you have multiple machines and a revenue reason to optimize utilization.

## Snippets

> "Platforms like Tinkercad have made CAD more accessible to novices and educational users." [Source: 2025-arslan-tinkerxr-ar-cad-novices.pdf p.2 — context for why Tinkercad is the right week-2 default]
