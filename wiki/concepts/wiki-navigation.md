---
title: Wiki Navigation — Reading This Knowledge Base
type: concept
tags: [meta, navigation, obsidian, wiki, conventions, schema, friend-handoff]
keywords: [wiki navigation, Obsidian vault, cross-link convention, @path syntax, frontmatter, tag pane, command palette, graph view, search, index page]
related:
  - entities/tools/obsidian.md
maturity: draft
created: 2026-05-07
updated: 2026-05-07
---

## Relations

@entities/tools/obsidian.md

## Raw Concept

How to actually use this wiki on a laptop. Covers the schema conventions (frontmatter / `@path` cross-links / confidence tags) plus Obsidian-specific navigation tricks. Read this once on day 1; the rest of the wiki becomes self-explanatory after.

## Narrative

### Where to start

**Always start at `wiki/index.md`.** It's the catalog — every page has a one-line summary plus tags, organized by type (Sources / Entities / Concepts). Skim the index first, drill into individual pages second. **Do not try to navigate via the file explorer alone** — folder browsing doesn't surface the relationships between pages.

### The four page types

Every wiki page is one of four types, declared in YAML frontmatter (`type:`):

| Type | What it is | Where it lives |
|---|---|---|
| **Source** | A page-per-ingested-research-paper or external doc | `wiki/sources/` |
| **Entity** | A specific thing: printer, material, slicer, tool, marketplace | `wiki/entities/<category>/` |
| **Concept** | A topic / methodology / synthesis: "how X works", "the four problems with Y" | `wiki/concepts/` |
| **Brief** | One-off deliverable for distribution (claude.ai or external) | `briefs/` (gitignored — local only) |

Read concepts first when learning a topic; read sources only when you need the primary-source backing for a specific claim.

### Frontmatter — what the YAML at the top means

Every page starts with:

```yaml
---
title: Human-readable page title
type: source | entity | concept
tags: [coarse, category, labels]
keywords: [fine, grained, search, terms]
related:
  - path/to/another/page.md
  - path/to/yet/another.md
maturity: draft | validated | core
created: 2026-05-06
updated: 2026-05-07
---
```

The fields the friend will use most:

- **`tags:`** — coarse categorization. Click a tag in Obsidian's tag pane → see every page with that tag. Examples: `slicer`, `material`, `security`, `bambu`, `paper`.
- **`maturity:`** — how trustworthy is this page?
  - `draft` — first synthesis; cross-references not yet stress-tested. **Most pages today.**
  - `validated` — claims cross-referenced against ≥2 sources or vendor docs.
  - `core` — battle-tested, treated as source-of-truth.
- **`related:`** — explicit links to other pages. Bidirectional: if A lists B as related, B lists A. Used for navigation and (by Obsidian's graph view) to draw the link map.

### The `@path` cross-link convention — important for Obsidian users

This wiki uses **two** cross-link styles:

1. **`related:` in frontmatter** — primary semantic links between pages. Listed once at the top.
2. **`@<path>.md` mentions in body text** — inline references where one page mentions another in prose.

**Important Obsidian gotcha:** the `@<path>.md` syntax is **not** Obsidian's native wikilink syntax (`[[page]]`). Obsidian renders `@<path>.md` as plain text — clicking it does nothing. To navigate from an `@path` mention:

- **`Cmd+O` (macOS) / `Ctrl+O` (Windows/Linux)** — opens the "Quick Switcher". Type the slug (e.g. `bambu-studio`) — Obsidian fuzzy-matches and the file pops up. Hit Enter to open.
- **`Cmd+P` / `Ctrl+P`** — Command Palette. Type "Quick Switcher" if you want the same effect via menu.
- **Use the file explorer** — slower, but works if you remember the folder.

**Why use the `@`-prefixed path style instead of `[[wikilinks]]` then?** The wiki was designed to be portable across tools (Obsidian, GitHub, VS Code, plain text editors). `[[wikilinks]]` are Obsidian-specific and don't render on GitHub or in most other tools. The `@`-prefixed style is plain text everywhere, and the trailing `.md` means a path-aware tool *can* link it if configured. The trade-off is: it's not auto-clickable in default Obsidian.

[NEEDS VERIFICATION 2026-05-07] Some Obsidian community plugins claim to parse `@path` references and turn them into clickable links. Friend may want to look for one ("Markdown Auto-link" or similar) — but this hasn't been audited.

### Confidence tags inside body text

When a claim in body text has a confidence qualifier, look for these inline tags:

| Tag | Meaning |
|---|---|
| `[CONFIRMED]` | ≥2 independent sources back this claim |
| `[TENTATIVE 2026-05-07]` | Single source or community-reported; treat as "probably true" not "verified" |
| `[NEEDS VERIFICATION 2026-05-07]` | Plausible but not yet checked. The date tells you when the claim was added — older = more suspicious |
| `[RETRACTED]` | Was believed; now disproven. Kept in place with a note so context survives |

**Friend's mental rule:** if a page recommends an action with a `[TENTATIVE]` or `[NEEDS VERIFICATION]` tag, cross-check before acting. The audit's specific bug claims (e.g. "Bambu Studio 1500°C preset bug") are tagged this way *for a reason*.

### Citation tags

When a page references a source:

- `[Source: filename.pdf p.5]` — quote/data from a specific page of a specific PDF in `raw-sources/`
- `[Source: https://example.com (retrieved 2026-05-07)]` — quote/data from a URL on a specific date
- `[Sources: file1.pdf p.3, file2.pdf p.12]` — multiple sources backing one claim

The `raw-sources/` folder containing the actual PDFs is **not** committed to GitHub (see `.gitignore`) — it's local-only on the laptop where the wiki was originally curated. If the friend needs a specific paper they can usually find it via the title or DOI in the source page's frontmatter.

### Five Obsidian navigation tricks worth memorizing

1. **`Cmd+O` (Quick Switcher)** — fuzzy file open. The single most-used shortcut. Type 3-4 chars of any page slug, hit Enter.
2. **`Cmd+Shift+F` (global search)** — full-text search across the whole vault. Useful for "where did we discuss PETG drying?".
3. **Tag pane** — right sidebar → tag icon. Click any tag to filter pages.
4. **Backlinks pane** — right sidebar → backlinks icon. Shows every page that links *to* the current page. Great for tracing how a concept ripples through the wiki.
5. **Graph view** — `Cmd+G` or sidebar. Visual map of all pages and their links. Will look sparse-ish for this wiki because it draws Obsidian-style wikilinks (which we don't use); the YAML `related:` edges should still be picked up.

### How the wiki is organized — at a glance

```
wiki/
├── index.md                    ← START HERE
├── log.md                      ← chronological history of every ingest
├── sources/                    ← one page per ingested research paper / external doc
├── entities/                   ← things
│   ├── materials/              ← PLA, PETG, ABS, ASA, TPU
│   ├── slicers/                ← Bambu Studio, OrcaSlicer
│   ├── tools/                  ← Kickstarter Autodesk FDM Test, Obsidian (this category)
│   └── printers/               ← Bambu X1C / P1S / A1 (when populated)
└── concepts/                   ← topics, methodologies, synthesis hubs
    ├── fdm-printing.md         ← top-level hub
    ├── bambu-ecosystem-closed-loop.md
    ├── ai-design-tools.md
    ├── filaments-baseline.md
    └── … (15+ concept pages)
```

### Adding new pages (when the friend wants to extend the wiki)

The schema is enforced via `scripts/wiki_lint.py`:

```bash
cd "~/Desktop/projects/3D printing"
python3 scripts/wiki_lint.py
```

Output flags orphans, asymmetric `related:` links, dangling links, missing pages, frontmatter errors. **Run lint before committing anything** to catch schema violations early. A clean lint = "0 orphans, 0 bidirectional gaps, 0 dangling related links."

For new pages, follow the existing pattern: copy frontmatter from a similar page, fill in the slots, add bidirectional `related:` links on both sides. The `@concepts/wiki-navigation.md` page (this one) is intentionally meta and lightly-related; most pages should have 5-15 `related:` edges.

### Reading on GitHub vs Obsidian — when each wins

| Use case | Best app |
|---|---|
| Quick read of a single page | GitHub web UI (no install needed) |
| Browsing many pages, following links | Obsidian (Quick Switcher beats clicking) |
| Reading on phone | GitHub web (Obsidian mobile is OK; web is simpler) |
| Editing pages | Obsidian or VS Code (both work) |
| Searching across the whole wiki | Obsidian (`Cmd+Shift+F`) |
| Sharing one page | GitHub (URL is shareable; Obsidian is local-only) |

[CONFIRMED] All conventions documented here match the schema in `CLAUDE.md`. [TENTATIVE] Specific Obsidian plugin recommendations should be re-verified at install time — the plugin ecosystem evolves.

## Snippets

(none — meta page; substantive material is in `CLAUDE.md` and `wiki/index.md` directly)
