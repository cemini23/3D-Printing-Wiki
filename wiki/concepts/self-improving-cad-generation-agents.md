---
title: Self-improving CAD generation agents (REFERENCE)
type: concept
tags: [concept, cad, agents, k95, FEA, reference]
keywords: [2605.17448, Hephaestus-CCX, CadQuery, CalculiX, engineering CAD agents]
related:
  - sources/arxiv-2605-17448-self-improving-cad-agents.md
  - sources/2026-george-agentscad-fdm-dfm.md
  - concepts/fdm-printing.md
  - concepts/ai-design-tools.md
  - concepts/novice-cad-workflows.md
  - sources/2026-hong-printanything-gplan.md
maturity: draft
created: 2026-06-03
updated: 2026-07-31
---

## Relations

@sources/2026-hong-printanything-gplan.md @sources/arxiv-2605-17448-self-improving-cad-agents.md @sources/2026-george-agentscad-fdm-dfm.md @concepts/fdm-printing.md @concepts/ai-design-tools.md @concepts/novice-cad-workflows.md

## Raw Concept

Deep-read of @sources/arxiv-2605-17448-self-improving-cad-agents.md (2026-06-05). Engineering-grounded **agent + CadQuery + CalculiX** loop — not a slicer plugin or Etsy design path.

## Narrative

### Task shape

| Stage | Tooling |
|-------|---------|
| Brief → blueprint (optional) | Schema-v4 text commitments |
| Blueprint → geometry | **CadQuery** → STEP assembly |
| Visual QA | 21-view renderer |
| Engineering QA | **CalculiX** via Gmsh mesh + typed pass/fail rubric |
| Retry | Agent revises CadQuery + selector metadata (≤10 attempts) |

### Why REFERENCE, not adopt

- **Near-zero first-shot success** on strict engineering rubric (0/400 first attempts in main sweep) [CONFIRMED].
- **Compute-heavy**: longest reported run ~68 min/item with partial pass rate still 9/50 strict.
- **Scope**: mechanical FEA assemblies — orthogonal to FFF slice prep, Bambu cloud, or decorative generative mesh tools.
- **License mix**: CadQuery Apache-2.0 OK locally; CalculiX GPL; benchmark harness MIT — fine for research, not a packaged consumer workflow.

### Where it might matter later

- If **OpenSCAD/CadQuery agent loops** with **simulation feedback** migrate down-market from aerospace briefs to **parametric jigs/fixtures**, revisit against @concepts/ai-design-tools.md Phase-0 pattern.
- Contrast with @concepts/novice-cad-workflows.md (mock → refine → slice): this paper's "refine" step is **FEA failure codes**, not slicer preview or print test.

**Friend handoff:** skip — no day-1 Orca-Flashforge relevance.

### Related — AgentsCAD FDM DFM (2026-07)

@sources/2026-george-agentscad-fdm-dfm.md is a **complementary** agent CAD lane: multi-agent **printability DFM** on STEP (overhangs → reorient / teardrop) with **MCP geometry tools**, not FEA. Same REFERENCE / no-local-repo stance; stronger signal for harness design (tool-grounded spatial reasoning vs confident hallucination).

## Snippets

> "Together these signals move CAD programs toward artifacts that are not only visually plausible but also checked against physical and structural requirements."
[Source: arxiv-2605.17448-self-improving-cad-generation-agents-with-finite.pdf p.1 abstract]
