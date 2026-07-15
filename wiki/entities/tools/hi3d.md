---
title: Hi3D
type: entity
tags: [AI, generative-3D, SaaS, conditional-go-tier, image-to-3D]
keywords: [Hi3D, Sparc3D, Print by Parts, Auto Connectors, browser, segmentation, CC BY 4.0]
related:
  - concepts/ai-design-tools.md
  - sources/2026-hi3d-maker-toolkit-phase0.md
  - entities/tools/meshy.md
  - entities/tools/tripo-ai.md
maturity: draft
created: 2026-06-25
updated: 2026-07-15
---

## Relations

@entities/tools/tripo-ai.md @concepts/ai-design-tools.md @sources/2026-hi3d-maker-toolkit-phase0.md

## Raw Concept

Browser-based generative 3D platform (Sparc3D engine). Phase-0 audit 2026-06-25: **CONDITIONAL-GO** for decorative Etsy/MakerWorld pipeline when automatic part segmentation is load-bearing. See @sources/2026-hi3d-maker-toolkit-phase0.md.

## Narrative

### What it is

Hi3D runs entirely in the browser — text/image → 3D mesh with **Print by Parts** segmentation and **Auto Connectors** for assembly. Targets hobby makers and Etsy sellers who lack CAD skills.

### Pricing / license [TENTATIVE 2026-06-25]

- Free tier: limited monthly generations, **CC BY 4.0** license on outputs
- Paid: commercial rights, private asset storage

### When to consider

- Large character models that exceed build volume without manual Boolean cuts
- Multi-part figurines where orientation per piece matters more than single-mesh convenience

### When to skip

- Functional / load-bearing parts
- Bambu-native MakerWorld one-click flow (Meshy integration may be simpler)
- Offline / privacy-sensitive workflows (cloud-only)

## Snippets

> "A free tier supports limited monthly generations under a CC BY 4.0 license; paid plans unlock commercial rights and private asset storage."
[Source: https://3dprintingindustry.com/news/hi3d-enhances-its-maker-toolkit-targeting-the-gap-between-ai-and-printing-252390/ (retrieved 2026-06-25)]
