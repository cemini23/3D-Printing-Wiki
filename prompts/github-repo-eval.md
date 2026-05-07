# GitHub Repo Eval Prompt — Phase-0 Audit for 3D Printing Tools

A reusable prompt template for evaluating a list of GitHub repositories before adopting any of them into the 3D printing workspace. Adapted from the Phase-0 audit pattern in `CLAUDE.md`.

## How to use

1. Paste the list of GitHub URLs at the bottom of the prompt (one per line) under `## Repos to audit`
2. Send the whole thing to Claude (in this workspace, claude.ai, or DeepSeek)
3. Claude runs the audit per repo and returns structured output
4. For GO / CONDITIONAL-GO repos: save the draft entity page section to `wiki/entities/tools/<slug>.md` (or whichever entity subfolder fits — `printers/`, `slicers/`, etc.)
5. NO-GO repos still get logged — paste the verdict block into `wiki/log.md` so future-you doesn't re-evaluate the same dud six months later

## The prompt (copy from here down)

---

You are auditing a list of GitHub repositories for adoption into a 3D printing workspace. The workspace is a knowledge hub for a hobbyist who's investing in a Bambu Labs printer and wants AI-assisted design + materials research + Etsy/MakerWorld store ops. The workspace is laptop-only (no remote server, no team distribution).

For EACH repo in the list, run a Phase-0 audit (~5 min per repo) and produce a structured report.

### Tools to use (preferred order)

1. `mcp__exa__get_code_context_exa` — primary tool. Pulls README, file structure, recent commits, key files.
2. `mcp__exa__crawling_exa` — fallback for the LICENSE file or specific docs pages if `get_code_context_exa` is incomplete.
3. `mcp__brave-search__brave_web_search` — for community signal: search "<repo name> review", "<repo name> issues", "<repo name> Reddit". Borderline verdicts only — skip for clear GO or NO-GO.

### Audit checklist (run for every repo)

**1. License**
- What is the SPDX identifier? (MIT / Apache-2.0 / GPL-2.0 / GPL-3.0 / AGPL-3.0 / BSD / proprietary / unknown)
- **Red flag — AGPL on hosted slicer servers**: triggers source-disclosure obligations if used server-side. For local laptop use, AGPL is usually fine.
- **Red flag — proprietary or unknown**: assume "all rights reserved" by default; cannot legally redistribute or fork.

**2. Maturity**
- Star count
- Last commit date (red flag: >12 months stale, *unless* the repo is feature-complete and stable — note this distinction)
- Open vs closed issue ratio (red flag: many open issues with no maintainer responses)
- Maintainer activity (recent comments in issues / PRs)

**3. Domain fit** — does this repo fit one of these slots:
- **AI design tool** — text-to-3D, image-to-3D, parametric generation, AI-assisted modeling
- **Slicer plugin / slicer fork** — extension or alternative to Bambu Studio / PrusaSlicer / OrcaSlicer
- **Modeling library/plugin** — OpenSCAD libs, FreeCAD macros, Blender add-ons for 3D printing
- **Print-farm / queue management** — multi-printer orchestration, OctoPrint plugins, etc.
- **Marketplace tool** — Etsy / MakerWorld / Printables / Cults3D automation, listing generators, SEO tools
- **Custom firmware / hardware mod** — Klipper config, Marlin fork, hardware modifications
- **3D-printing-adjacent** — slicer profile share, filament database, calibration tool
- **Doesn't fit** → NO-GO (note category and skip remaining audit steps)

**4. Failure mode for class** (run the matching one based on §3)
- **AI design tools**: Model-locked (only OpenAI / only Claude)? Cloud-only (no self-host option)? Bambu cloud dependency? Heavy GPU requirements? Output quality — printable models, or just visual generation?
- **Slicer plugins / forks**: Hardcoded to one slicer? Breaks on Bambu Studio or Orca? Profile-schema mismatch? Last-known-compatible slicer version?
- **Modeling libs/plugins**: Software-version locked (only specific Blender / FreeCAD)? Active maintenance? Docs quality?
- **Print-farm tools**: Printer-specific lock-in (only Bambu, only Prusa)? Cloud-required? Self-hosted complexity?
- **Marketplace tools**: Marketplace-specific (only Etsy)? API key with policy / ToS risk? Rate-limit handling?
- **Firmware / hardware mods**: Voids printer warranty? Bricking risk on partial flash? Vendor lock-in? Roll-back path documented?

**5. Wiki coverage check** — if the workspace already has any `wiki/entities/tools/*.md` pages, scan them for parallel implementations or prior NO-GO rejections of the same tool. (Skip if `wiki/entities/tools/` is empty — early in the wiki's life this section is unused.)

### Output format (per repo)

```
=== <repo-owner>/<repo-name> ===
URL: https://github.com/<owner>/<repo>
License: <SPDX or "unknown">
Last commit: <YYYY-MM-DD>
Stars: <N> | Open issues: <N>
Domain fit: <category from §3, or "doesn't fit">

Failure-mode-for-class check:
- <bullet 1>
- <bullet 2>
- <bullet 3 if relevant>

Wiki coverage: <"no parallel" | "duplicates @path" | "prior NO-GO @path">

Verdict: GO | CONDITIONAL-GO | NO-GO

Reasoning (1-3 sentences): <...>

--- DRAFT ENTITY PAGE (only if GO or CONDITIONAL-GO) ---
File: wiki/entities/<category>/<slug>.md

---
title: <Tool Name>
type: entity
tags: [3d-printing, <category-tag>]
keywords: [<3-5 fine-grained search terms>]
related: [<any wiki page that should backlink — leave empty if none>]
maturity: draft
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

## Raw Concept
Sourced from Phase-0 GitHub audit on <YYYY-MM-DD>. Repo: https://github.com/<owner>/<repo> @ <commit-sha>.

## Narrative
<2-4 sentence summary: what it does + key strengths + key risks + verdict reasoning>

## Snippets
[Source: github.com/<owner>/<repo> — README]
> <key README quote, if useful>
```

### Important rules

- **Be skeptical of README claims**: READMEs are marketing. Verify against issue threads + commit activity before accepting any feature claim as real.
- **Flag single-source claims**: if a feature is only in the README and not corroborated externally, mark `[NEEDS VERIFICATION YYYY-MM-DD]` in the Narrative.
- **Do not adopt parallel implementations**: if Repo B does what Repo A already does (and A is in the wiki), only one goes GO. Justify which.
- **License-unknown defaults to NO-GO**: unless the maintainer can be contacted to clarify within reasonable time.
- **Cost discipline**: max 2 Exa calls per repo (one `get_code_context_exa`, optional one `crawling_exa` for LICENSE). For lists >10 repos, skip the Brave community-signal step on rounds 2+ unless the verdict is borderline.
- **Order of report**: list all GO repos first, then CONDITIONAL-GO, then NO-GO. Sort within each tier by domain fit + maturity.

### When all repos are processed, end with a summary block

```
=== Summary ===
Total: <N>
GO: <count> — list of names
CONDITIONAL-GO: <count> — list (with the conditions)
NO-GO: <count> — list (with one-line reason each)
Most interesting finding: <one-sentence note>
```

---

## Repos to audit

(Paste GitHub URLs below, one per line — example format:)

```
https://github.com/example/foo
https://github.com/example/bar
```
