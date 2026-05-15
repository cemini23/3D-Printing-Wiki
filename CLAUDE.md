# 3D Printing Research Workspace — Schema

This file is the **schema**: it tells you (the LLM) how to operate this workspace. Everything else is either a raw source, a wiki page, or a meta file. Read this on every session start. Active workstreams + open decisions live in `ROADMAP.md`, not here.

## Purpose

Local knowledge hub for 3D printing research, design, and store ops — a librarian that **manages, curates, and applies** that knowledge.

- **Manage** — inventory raw sources (PDFs, GitHub repos, slicer manuals, YouTube transcripts, blog posts); track what's been read, extracted, and applied
- **Curate** — pull relevant fragments out of raw sources; structure them as interlinked wiki pages on materials, printers, slicers, AI design tools, and store operations
- **Apply** — route findings to a real workflow:
  - **claude.ai / DeepSeek** — context for design generation, troubleshooting, materials selection, store-ops decisions
  - **Local laptop workflows** — print queues, design libraries, filament/material inventory, store SKU lists, listing copy

This is a laptop-only workspace. No remote servers, no team distribution. Everything lives on this MacBook Pro.

## Architecture — three layers

1. **Raw sources** — immutable. You read them, never modify them. Live locally in `raw-sources/` (gitignored — too large/copyrighted to track).
   - PDFs (slicer manuals, Bambu docs, technical papers)
   - GitHub repos (cloned snapshots of 3D-printing-AI tools, OpenSCAD libraries, custom firmware)
   - Articles, blog posts, YouTube transcripts saved as `.md`
   - Slicer profile exports (Bambu Studio, PrusaSlicer, OrcaSlicer)
   - **Drop pattern**: drop new sources into `research to be indexed/` (transient drop zone). Ingest pipeline reads + synthesizes, then move to `raw-sources/`.

2. **The wiki** — LLM-written, human-read. Lives in `wiki/`. Structured pages on materials, printers, designs, store ops.

3. **The schema** — this file.

Staging/output lives outside the wiki:
- `briefs/` — one-off deliverables (gitignored): a print-ready design brief, a comparison of filament vendors, a store listing draft
- `research to be indexed/` — transient drop zone for new raw sources (gitignored)
- `LESSONS.md` — meta-lessons about *how we work* (distinct from `wiki/log.md`)
- `hot.md` — ephemeral session-state cache (gitignored)
- `ROADMAP.md` — active workstreams + open decisions (tracked)

## Folder layout

```
3D printing/
  CLAUDE.md                    # this file — the schema
  LESSONS.md                   # meta-lessons (how we work)
  ROADMAP.md                   # active workstreams + decisions + done log
  hot.md                       # session-state cache (gitignored)
  .env.example                 # env-var template (commit this)
  .env                         # actual keys (gitignored — never commit)
  research to be indexed/      # transient drop zone (gitignored)
  raw-sources/                 # archived raw source corpus (gitignored)
  briefs/                      # staging for distribution → claude.ai or local apps (gitignored)
  wiki/                        # canonical wiki
    index.md                   # content-oriented catalog of all wiki pages
    log.md                     # append-only chronological operations log
    sources/                   # one page per ingested source
    entities/                  # printers, materials, slicers, AI tools, designs, marketplaces
    concepts/                  # techniques, methodologies, workflows, business strategies
  scripts/                     # wiki_lint.py, preingest_check.py, etc. (TBD)
  prompts/                     # reusable prompt templates (e.g. github-repo-eval.md)
  .claude/                     # Claude Code per-project state (gitignored)
```

Pages can be nested inside `entities/` when `Domain > Topic > Subtopic` hierarchy is warranted (e.g. `entities/printers/bambu-x1c.md`, `entities/materials/pla-pro.md`, `entities/tools/openscad.md`, `entities/marketplaces/etsy.md`). `concepts/` and `sources/` are flat by convention.

## Wiki page format

Every wiki page is a markdown file with YAML frontmatter + structured sections.

### Frontmatter (required)

```yaml
---
title: Human-readable page title
type: source | entity | concept | brief
tags: [coarse, category, labels]
keywords: [fine, grained, search, terms]
related:
  - entities/printers/bambu-x1c.md
  - concepts/example-concept.md
maturity: draft | validated | core
created: 2026-05-06
updated: 2026-05-06
---
```

- `type` determines section template
- `maturity`: `draft` → `validated` (cross-referenced + tested in real prints/sales) → `core` (battle-tested source of truth). Move up (occasionally down) as evidence warrants
- `related[]` is **bidirectional**: if A lists B, B must list A
- `created` / `updated`: ISO dates; bump `updated` on meaningful body changes

### Body sections (in order, include only what's relevant)

- `## Relations` — inline list of `@path/to/page.md` annotations matching `related:` frontmatter
- `## Raw Concept` — provenance. For source pages: title/author/retrieval-date/filename/URL. For entity/concept pages: what prompted this page, which sources synthesized into it
- `## Narrative` — the body. Prose, tables, structured data, diagrams. Concept pages: synthesized understanding, neutral, well-sourced — opinion belongs in briefs, not concept pages
- `## Snippets` — verbatim quotes / code / formulas / data with citations
- `## Dead Ends` (optional) — what was tried + why it failed + what was learned

### Page-type quick reference

- **Source page** (`wiki/sources/<slug>.md`) — one per ingested source. Raw Concept fields: title / author / type / location / retrieved / pages / read-status (skimmed | read | deep-read | unread-stub).
- **Entity page** (`wiki/entities/<category>/<slug>.md`) — printers, materials, slicers, AI design tools, marketplaces, software. Raw Concept: what prompted the page + which sources synthesize into it.
- **Concept page** (`wiki/concepts/<slug>.md`) — techniques (e.g. multi-material printing, tree supports), methodologies (e.g. design-for-manufacturing), business strategies (e.g. Etsy SEO, pricing models). Raw Concept: the question or topic the page answers.
- **Brief page** (`briefs/<YYYY-MM-DD>_<slug>.md`) — deliverable. Body sections: `## Target` (claude.ai | DeepSeek | local-app) / `## Summary` / `## Body` / `## Sources`.

## Cross-link + citation conventions

**Cross-links** (`@path` syntax):
- Use `@path/to/page.md` inline (no leading slash, relative to `wiki/`)
- Bidirectional: A → B and B → A both required
- Stub pages preferred over orphan mentions: if a topic comes up without a page, create a stub

**Citation tags**:
- Source page: `[Source: filename.pdf p.5]`
- External URL: `[Source: https://... (retrieved YYYY-MM-DD)]`
- GitHub repo: `[Source: github.com/owner/repo @ <sha>]`
- Multiple: `[Sources: filename.pdf p.5, github.com/foo/bar]`

**Claim confidence tags**:
- `[CONFIRMED]` — ≥2 independent sources, OR personally tested (printed it, sold it)
- `[TENTATIVE]` — single source or untested
- `[NEEDS VERIFICATION YYYY-MM-DD]` — plausible but untested. **Always include the date** so staleness can be flagged
- `[RETRACTED]` — previously believed, now disproven. Keep in place with a note; don't delete

## Related Wikis

When a query needs data from another wiki, reference it using the `@wiki-alias/path/to/page.md` syntax. The LLM resolves these by reading the other wiki's files directly.

Paths below are relative to this CLAUDE.md file's directory. Resolve `../` against this file's location to get the absolute path.

| Alias | Path | Description |
|-------|------|-------------|
| `osint-wiki` | `../../OSINT WORKSPACE/wiki/` | Financial research, quant finance, prediction markets, CeminiSuite, RL for trading |
| `image-gen-wiki` | `../Image gen/wiki/` | Uncensored image generation, model cataloging, ComfyUI, LoRA, persona/character ops |
| `seo-wiki` | `../SEO:GEO B&M Business/wiki/` | Local SEO, GBP optimization, GEO/AEO, web design, social media, creator marketing |
| `3d-printing-wiki` | `wiki/` | FDM/FFF printing, Bambu, materials, slicers, print farms, store ops |
| `cybersecurity-wiki` | `../Cybersecurity wiki/wiki/` | Cybersecurity research — offensive security, defensive operations, certifications, threat actors. Shared territory: hardware hacking when printed jigs / RFID enclosures / lock-pick aids overlap with physical-pentest tooling |

### Cross-wiki link syntax

- Use `@wiki-alias/path/to/page.md` for cross-wiki references (e.g., `@image-gen-wiki/concepts/tree-supports.md`)
- Bidirectional: if 3D Printing page A references another wiki's page B, add a matching `@3d-printing-wiki/...` backlink on page B
- When creating a stub in another wiki, note the cross-wiki dependency in `## Relations`

## Operations

### Ingest (adding a new source)

1. New source dropped into `research to be indexed/`
2. Read the source (or relevant sections for long PDFs / repo READMEs)
3. **Discuss key takeaways with the user before writing**
3b. **Cross-wiki routing check** — before writing pages, evaluate whether the source contains off-topic content more relevant to another wiki (@osint-wiki, @image-gen-wiki, or @seo-wiki). If so:
   - Call `python3 "/Users/claudiobarone/Desktop/OSINT WORKSPACE/scripts/cross_wiki_route.py"` to create a stub page or brief in the correct wiki, piping content via stdin
   - Use `--type page` for substantive material, `--type brief` for tangential material
   - **When in doubt, prefer a brief over a stub** — briefs are cheaper and don't create maintenance burden in the target wiki
4. Create `wiki/sources/<slug>.md` — frontmatter + Raw Concept + short Narrative
5. Identify entities + concepts the source touches. For each:
   - If page exists: update it, add `related:` backlink, bump `updated:`
   - If no page: create a stub. Real content accumulates over subsequent ingests
6. Update `wiki/index.md` — add rows for new pages
7. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source title>` with bullets of what changed
8. **Move raw source to `raw-sources/`**: `mv "research to be indexed/<filename>" raw-sources/`. Verify with `ls raw-sources/<filename>`
9. Update `ROADMAP.md` if the ingest opens new follow-ups; stage briefs in `briefs/` if the ingest produced something actionable
10. A single ingest must touch 3-15 pages. If it touches 0 new pages, ask whether the source is worth ingesting

### Query (answering a question)

1. Read `wiki/index.md` first to locate relevant pages
2. Read those pages; follow `@relations` where useful
3. Synthesize the answer with inline citations to source pages and raw sources
4. **OOD signal**: if the wiki doesn't contain a real answer, say so explicitly. Don't fabricate from tangential matches. Offer to ingest sources that would fill the gap
5. **File answers back**: if the query produced a valuable synthesis, file it as a new concept page or brief. Don't let insights die in chat
6. Append a query entry to `log.md` if substantive

### Lint (periodic health check)

Mechanical checks (`scripts/wiki_lint.py`):

- **Orphans** — pages with zero inbound `related:` references
- **Bidirectional gaps** — A lists B as related but B doesn't list A
- **Dangling links** — `related:` paths that don't resolve
- **Cited-unread stubs** — source pages with `read_status=unread-stub` and ≥1 inbound edge
- **Frontmatter quality** — missing `type`/`maturity`/mismatched `updated`
- **Stale `[NEEDS VERIFICATION YYYY-MM-DD]` tags** (≥7 days old by default)

Human/LLM judgment still needed for:
- **Contradictions** — two pages making incompatible claims (e.g. "PETG warps less than ABS" vs "PETG warps more than ABS"). Flag with `[NEEDS VERIFICATION]` and note on both pages
- **Stale claims** — superseded by newer firmware/slicer versions. Move to `[RETRACTED]` with pointer

## External research — MCP tools

When the wiki + raw sources can't answer, or when verifying an unverified URL:

| Tool | When to use |
|------|-------------|
| `mcp__brave-search__brave_web_search` | Quick targeted lookup — fact-check, find a primary source URL, find recent forum discussions |
| `mcp__brave-search__brave_news_search` | Recent news on materials, printer releases, regulatory changes |
| `mcp__exa__web_search_exa` | Higher-signal web search for technical content |
| `mcp__exa__crawling_exa` | Pull clean LLM-friendly content from a known URL — turns `[Source: https://...]` into verifiable text for `## Snippets` |
| `mcp__exa__get_code_context_exa` | GitHub repo context — README, structure, key files. Primary tool for repo evaluation. |
| `mcp__exa__deep_researcher_start` / `_check` | Async multi-step research — novel concept-page bootstrapping |
| `mcp__plugin_context7_context7__resolve-library-id` + `query-docs` | Up-to-date docs for slicers (Bambu Studio, PrusaSlicer, OrcaSlicer), modeling tools (OpenSCAD, FreeCAD, Blender), and AI libs |
| `mcp__playwright__browser_navigate` (+ snapshot, click, etc.) | Interactive browsing of MakerWorld, Printables, Thingiverse, GitHub when search isn't enough |

**Workflow integration**:
- **Ingest**: when a source cites a URL, prefer `crawling_exa` to pull cited page directly into `## Snippets`
- **Query (OOD)**: before declaring a wiki gap, run `web_search_exa` or Brave. If results converge, ingest the best 1-2 hits as new source pages
- **GitHub-repo eval**: `get_code_context_exa` + Phase-0 audit pattern (below)

Cost discipline: Exa is a paid API. Default `numResults: 3-5` for routine queries; `deep_researcher_*` reserved for genuine multi-source synthesis.

## Distribution rules

Material ready to leave the wiki goes through `briefs/` first:

- **→ claude.ai** — copy the relevant brief body into a Claude conversation for design help, troubleshooting, business decisions
- **→ DeepSeek** — same pattern, via DeepSeek API or web UI (see `.env.example` for `DEEPSEEK_API_KEY`)
- **→ Local apps** — paste filament inventory into Bambu Studio, paste design prompt into ChatGPT/Claude, paste listing copy into Etsy/MakerWorld. Manual transfer; no automation yet.

No remote server, no scp, no team distribution. Everything stays on this laptop.

## Working method

- Search the wiki first. Raw sources second. External sources last (via MCP)
- Prefer paraphrase + cite over raw quote. Quotes go in `## Snippets` with full citation
- When stress-testing a claim, actively look for disconfirming evidence (e.g. "PETG is easy to print" — find threads where it isn't)
- Flag single-source claims explicitly
- File insights into wiki pages or briefs before they disappear from chat
- If a claim involves a real-world purchase decision (printer, filament, software license), be extra rigorous about provenance — wrong calls cost real money

## Phase-0 audit pattern (before adopting an external tool)

Before adopting a 3D-printing-AI tool, slicer plugin, or GitHub repo into the workflow, run a Phase-0 source audit (~30 min):

1. Read the README + LICENSE + last-N-commits
2. Verify license — be careful with AGPL on hosted slicer servers (server-side use triggers source-disclosure obligations); GPL/MIT/Apache for local-only is fine
3. Verify maturity — stars, commits, last push, open issues, maintainer responsiveness
4. **Audit for the most-likely failure mode for this tool class**:
   - **AI design tools**: model-specific (only Claude/GPT, can't swap to DeepSeek)? Cloud-only (no local mode)? Bambu cloud dependency?
   - **Slicer plugins**: hardcoded slicer assumption (only PrusaSlicer)? Breaks on Bambu fork? Outdated profile schema?
   - **Custom firmware / hardware mods**: voids printer warranty? Vendor lock-in (only Bambu, only Prusa)? Bricks the printer if mid-update fails?
   - **Marketplace/store-ops tools**: marketplace-specific (only Etsy, no MakerWorld export)? Requires API key with policy risk?
5. Compare against existing wiki coverage (don't adopt parallel implementations of what we already have or know is bad)
6. Decide GO / CONDITIONAL-GO / NO-GO and record in the entity page

## Session-start ritual

On every new session, **before any other work**:

### 0. Resume from hot.md

Read `hot.md` (gitignored session-state cache). Report in one line:

> "Resuming from <last position>. Workspace idle. Next: your direction."

If `hot.md` is missing (first run, deleted), say:

> "No `hot.md` found — fresh session. Want me to rebuild session state from `wiki/log.md` + `ROADMAP.md`?"

At session end, rewrite `hot.md` with updated position, open decisions, pending actions.

### 1. Inbox check

```bash
ls -1 "research to be indexed/" 2>/dev/null | grep -v '^\.'
```

If items exist that the user hasn't asked you to address, mention briefly: "Btw, you have N items in `research to be indexed/`. Want me to triage them?"

### 2. (Future ritual hooks land here.)

Keep each check under 60 seconds.

## Related — environment + secrets

- **DeepSeek API**: required for AI-assisted design and research. Get a key at https://platform.deepseek.com/, put it in `.env` as `DEEPSEEK_API_KEY=`. Never commit `.env`. See `.env.example` for the template.
- **Brave Search API** / **Exa API**: optional (the MCPs work better with their own keys; alternatively, claude.ai's web tools are a fallback). Same `.env` pattern.

If you fork/clone this workspace to another machine: copy `.env.example` to `.env` and fill in your own keys. Never reuse anyone else's keys.
