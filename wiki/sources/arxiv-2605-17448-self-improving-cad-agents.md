---
title: Self-improving CAD generation agents (arXiv:2605.17448)
type: source
tags: [source, arxiv, cad, agents, k95, FEA, CadQuery]
keywords: [2605.17448, Hephaestus-CCX, CalculiX, CadQuery, GPT-5.5, Claude Code, engineering validation]
related:
  - concepts/self-improving-cad-generation-agents.md
  - concepts/ai-design-tools.md
  - concepts/novice-cad-workflows.md
maturity: draft
read_status: deep-read
created: 2026-06-03
updated: 2026-06-05
---

## Relations

@concepts/self-improving-cad-generation-agents.md @concepts/ai-design-tools.md @concepts/novice-cad-workflows.md

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Self-Improving CAD Generation Agents with Finite Element Analysis as Feedback |
| **Authors** | Guijin Son, Jehyun Park, Seyeon Park, Sunghee Ahn, Youngjae Yu (SNU, OneLineAI, SKKU, Ewha) |
| **arXiv** | 2605.17448v2 (cs.GR), 27 May 2026 |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2605.17448-self-improving-cad-generation-agents-with-finite.pdf` |
| **Retrieved** | 2026-06-03 |
| **Read-status** | deep-read (2026-06-05) |

## Narrative

**What it is.** Reframes CAD generation as an **engineering validation** task: a free-form brief → **assembled multi-part STEP** (ISO AP242) → pass/fail against **typed requirement checkers** run through **CalculiX FEA** (Gmsh mesh, Abaqus-style input deck). Not mesh-for-printing, not slicer integration.

**Agent loop.** LLM coding agents write **CadQuery** programs, export STEP, receive structured feedback from (1) optional **schema-v4 blueprint** (text-only design commitments), (2) **21-view** mesh renders (vs typical 4–6 in prior VLM CAD evals), (3) **CalculiX** stress/displacement/modal/buckling/clearance checks. Up to **10 retry attempts** per brief; production harnesses use **OpenAI Codex (GPT-5.5)** and **Claude Code (Opus-4.7)**.

**Headline results [CONFIRMED from paper].** Main first-attempt sweep: **400 first attempts, zero strict-passing artifacts**. One FEA-feedback round across 400 revised submissions adds **one** strict pass. Partial credit improves with feedback: GPT-5.5/xhigh mean requirement pass on Hephaestus-CCX rises **19.4% → 29.3%** with 21-view feedback; Fusion360 Box-IoU **0.397 → 0.505**; S2O Box-IoU **0.444 → 0.592** with blueprinting. Longest GPT-5.5/high run: **~68 min/item** (vs ~10 min two-attempt baseline) → **9/50 strict passes**, **60.5%** mean requirement pass.

**Benchmark.** **Hephaestus-CCX (H-CCX)**: 50 curated briefs (20 single-part, 30 multi-part) from a 466-case pool (patents, datasheets, NASA/ECSS/AISC/MIL-STD, competitions). MIT license release planned for benchmark assets; CadQuery **Apache-2.0**, CalculiX **GPL**.

**Wiki / store-ops boundary.** [CONFIRMED] **No consumer FDM workflow change** — targets load-bearing mechanical assemblies validated in FEA, not decorative STL for Etsy. Overlap with @concepts/ai-design-tools.md is **watch-list only** (agent + CadQuery loops). Friend handoff: **skip** (same tier as print-farm / robotics hubs). Distinct from Meshy/image-to-STL decorative pipelines in @concepts/novice-cad-workflows.md.

**Phase-0 verdict.** **REFERENCE / NO-GO for adopt** as a production design tool — paper explicitly warns generated artifacts need independent professional review; not certified for safety-critical manufacture. Useful as a **research signal** for where agentic CAD + simulation feedback is heading.

## Snippets

> "In the main Codex and Claude Code sweep, 400 first attempts do not produce a single strict-passing artifact, and one FEA-feedback round adds only one strict pass across another 400 revised submissions."
[Source: arxiv-2605.17448-self-improving-cad-generation-agents-with-finite.pdf p.2]

> "An LLM agent writes a CadQuery program, executes it to export a STEP artifact, receives structured feedback from rendering, validation, and simulation tools, and revises the program and selector metadata before the next attempt."
[Source: arxiv-2605.17448-self-improving-cad-generation-agents-with-finite.pdf p.2]

> "Hephaestus-CCX and the released harness are evaluation assets, not a certified design tool. Generated artifacts should not be used for safety-critical, regulated, or manufactured designs without independent professional engineering review."
[Source: arxiv-2605.17448-self-improving-cad-generation-agents-with-finite.pdf p.30]
