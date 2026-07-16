---
title: "AgentsCAD: Automated DFM of FDM Parts via Multi-Agent LLM + Geometric Features"
type: source
tags: [paper, CAD, agents, FDM, DFAM, MCP, CadQuery, overhang]
keywords: [AgentsCAD, Claude Sonnet, GPT-4o, GraphSAGE, MFCAD++, blackboard, STEP, teardrop, Carnegie Mellon]
related:
  - concepts/self-improving-cad-generation-agents.md
  - concepts/ai-design-tools.md
  - concepts/novice-cad-workflows.md
  - concepts/fdm-printing.md
  - sources/arxiv-2605-17448-self-improving-cad-agents.md
  - sources/2026-arxiv-lane-noise-triage-jul16.md
maturity: draft
created: 2026-07-16
updated: 2026-07-16
read_status: skimmed
---

## Relations

@concepts/self-improving-cad-generation-agents.md @concepts/ai-design-tools.md @concepts/novice-cad-workflows.md @concepts/fdm-printing.md @sources/arxiv-2605-17448-self-improving-cad-agents.md @sources/2026-arxiv-lane-noise-triage-jul16.md

## Raw Concept

- **Title:** AgentsCAD: Automated Design for Manufacturing of FDM Parts via Multi-Agent LLM Reasoning and Geometric Feature Recognition
- **Authors:** Emmanuel George, Christopher Keefe, Peter Pak, Amir Barati Farimani (Carnegie Mellon ME)
- **Type:** arXiv preprint, arXiv:2607.02448v2 [cs.MA]
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2607.02448-agentscad-automated-design-for-manufacturing-of.pdf`
- **Retrieved:** 2026-07-16 overnight digest
- **Pages:** 28
- **Read-status:** skimmed (abstract, architecture, birdhouse test, MCP ablation, conclusion)

## Narrative

**AgentsCAD** automates **FDM Design-for-AM (DFAM)** on **STEP / B-Rep** geometry: detect overhangs (&gt;45°), reason about reorientation / fillets / chamfers / teardrops, emit a modified STEP + human-readable report. Unlike slicers (which flag defects but do not rewrite CAD), this pipeline edits the solid.

### Architecture [CONFIRMED — paper §4]

| Stage | Role |
|-------|------|
| CadQuery / OCCT parser | Face features (type, area, normals, tilt, adjacency graph) → shared **blackboard** |
| Optional GraphSAGE | Semantic face labels from MFCAD++ (59,665 parts); UV-Net / GCN baselines |
| Claude Sonnet reasoner | DFM recommendations + tool calls |
| **MCP geometry tools** | `check_orientation_overhangs`, `lay_face_to_build_surface` — exact Euler angles |
| GPT-4o VLM verifier | Rendered views → geometric integrity flags |
| StrategyCouncil | Overrides spurious LLM picks (e.g. reject bad chamfers; prefer bore-side-lay) |

Blackboard pattern chosen over LangChain/CrewAI-style chat so phases stay ordered and models swappable.

### Birdhouse test [CONFIRMED — §5.2]

Nine-face birdhouse: two cylindrical bores as −90° overhangs. Pipeline: RAG injects FDM heuristics → six orientation tool probes → StrategyCouncil picks X=90° bore-side lay (eliminates one overhang) → teardrop on remaining bore (9→12 faces) → zero actionable overhangs; OCCT volume Δ −0.75%. VLM flagged wall thickness / cross-section as inconclusive (render resolution), not as hard fails.

### MCP ablation [CONFIRMED — §5.3] — load-bearing for harness briefs

Without MCP geometry tools, the LLM **hallucinated rotations** (e.g. +45° when −30° was correct) and asserted overhang-free with high confidence. With tools: coordinate-transform errors **eliminated** across test cases. Paper claim: MCP grounding is a **prerequisite**, not an enhancement.

### Phase-0 (2026-07-16)

| Check | Result |
|-------|--------|
| Public repo | **None found** (no GitHub URL in PDF) |
| Cloud deps | Claude Sonnet + GPT-4o — not DeepSeek-swappable without rewrite |
| Local pieces | CadQuery/OCCT, GraphSAGE weights — research code not released |
| Failure mode | Cloud-only reasoner; single-part only; face-count context blowup on large models |
| Hobby / friend | **NO-GO** day-1 — not Orca-Flashforge / Tinkercad path |
| Wiki / harness | **REFERENCE** — cite MCP tool-grounding + blackboard DFM pattern |
| Local adopt (&lt;500 MB) | **Skipped** — nothing to clone |

Contrast @sources/arxiv-2605-17448-self-improving-cad-agents.md (FEA / CalculiX loop): AgentsCAD is **printability DFM on B-Rep**, not stress validation.

## Snippets

> "Current slicers identify defects such as steep overhangs but are unable to modify the underlying geometry."
[Source: arXiv:2607.02448v2 abstract]

> "This ablation confirms that geometric grounding via MCP tools is not an optional enhancement but a prerequisite for reliable DFM reasoning."
[Source: arXiv:2607.02448v2 §5.3]

> "The system currently accepts only single parts with no assembly support."
[Source: arXiv:2607.02448v2 §7]
