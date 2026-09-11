---
title: "Multi-vine soft robot with accessible working channel (arXiv:2609.03758)"
type: source
tags: [paper, soft-robotics, vine-robot, eversion, medical, pneumatic, background]
keywords: [vine robot, eversion, colon phantom, EndoTheranostics, Queen Mary, steering, working channel]
related:
  - concepts/soft-robotics-fdm-diw.md
  - concepts/niche-fdm-applications.md
maturity: draft
created: 2026-09-11
updated: 2026-09-11
read_status: skimmed
wire_status: wont_wire
wire_target: "medical vine-robot REFERENCE; not AM print workflow"
---

## Relations

@concepts/soft-robotics-fdm-diw.md @concepts/niche-fdm-applications.md

## Raw Concept

- **Title:** A Multi-Vine Soft Robot Enabling Accessible Working Channel and Steering
- **Authors:** Reza Kashef, Cem Suulker, Mohammad Sheikh Sofla, Kaspar Althoefer (Queen Mary University of London)
- **arXiv:** 2609.03758
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2609.03758-a-multi-vine-soft-robot-enabling-accessible-work.pdf`
- **Retrieved:** 2026-09-11 ingest pass 32
- **Pages:** 2 (extended abstract / short paper)
- **Read-status:** skimmed (full text)

## Narrative

**Vine / eversion robot** architecture — not filament AM. Two thin flexible **inextensible tubes** fold inward and everts under pressure. This paper couples **two vines** to an **externally integrated working channel** via soft mounting tips so tools/sensors ride **outside** the vine bodies (avoiding embedded-channel friction limits).

### Control strategy [CONFIRMED paper]

- **Straight growth:** both vines pressurized equally; working channel advances freely
- **Left turn:** right vine pressurized; working channel locked → buckling → sharp leftward turn
- **Right turn:** reverse asymmetry
- Growth speed tied to working-channel advancement rate

### Results [CONFIRMED paper Fig. 2]

| Test | Outcome |
|------|---------|
| Single-vine growth pressure | 10 mm and 20 mm diameter vines; growth pressure ≪ burst pressure |
| Open environment | Forward growth, controlled turning, pipe entry |
| Colon phantom | **~90° bend** navigated with 10 mm vines + working channel (silicone phantom — higher friction than real colon) |

Funded by ERC **EndoTheranostics** (101118626) — minimally invasive medical motivation.

### Wiki posture

**Background REFERENCE** — no FDM/Bambu/Flashforge path. Relevant to soft robotics hub as **eversion / medical navigation** contrast to printed pneumatics (@sources/2026-abboodi-airtight-spa-fdm.md, @sources/2026-jang-monorigami-sla-origami-pneumatic.md). Friend reader: skip.

### Phase-0 (2026-09-11)

| Check | Result |
|-------|--------|
| Public repo / CAD | **None** in paper |
| AM relevance | **Low** — fabricated vine tubes, not desktop FFF |
| Friend / store | **NO-GO** |
| Verdict | **REFERENCE** (medical soft robotics background) |
| Phase-1 | **wont_wire** |

## Snippets

> "two vine robots are coupled to an externally integrated working channel via soft mounting tips. Independent vine actuation enables active tip steering while advancing the working channel without embedding it within the vine bodies."
[Source: arXiv:2609.03758 introduction]

> "the robot successfully passes a 90° bend while carrying the working channel along with it."
[Source: arXiv:2609.03758 results / colon phantom]
