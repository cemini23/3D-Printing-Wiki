---
title: Obsidian — Local-First Markdown Knowledge-Base App
type: entity
tags: [tool, obsidian, knowledge-base, markdown, local-first, free-personal, navigation]
keywords: [Obsidian, vault, wikilinks, markdown editor, knowledge management, local-first, plugins, graph view, tags, dataview, command palette, file explorer]
related:
  - concepts/wiki-navigation.md
  - entities/tools/markdown-preview-pluk.md
maturity: draft
created: 2026-05-07
updated: 2026-05-21
---

## Relations

@concepts/wiki-navigation.md
@entities/tools/markdown-preview-pluk.md

## Raw Concept

The recommended app for reading this wiki on the reader's laptop. Free for personal use, local-first (no cloud account needed), reads any folder of markdown files as a "vault" — which is exactly what this wiki is. Page exists so the reader has a one-stop install + setup reference; navigation conventions for *this specific wiki* are on `@concepts/wiki-navigation.md`.

## Narrative

### What it is

Obsidian is a local-first markdown editor built around the idea of a "vault" — a folder of `.md` files on disk that the app indexes for cross-linking, graph view, search, and tag browsing. The files stay plain markdown; if Obsidian disappears tomorrow, every file in this wiki is still readable in any text editor or on GitHub.

Key facts:

- **License:** proprietary (closed-source) but **free for personal use.** Commercial-use license is $50/user/year. The reader's use (personal knowledge management) is free.
- **Platforms:** macOS / Windows / Linux / iOS / iPad / Android. The desktop apps are full-featured; mobile is read-mostly.
- **Storage:** local-only by default. No cloud account required. (Optional paid Obsidian Sync exists for multi-device sync, but iCloud Drive / Dropbox / Syncthing all work fine for free.)
- **File format:** plain `.md` files with YAML frontmatter — exactly what this wiki uses.

### Why Obsidian for this wiki specifically

Three reasons this wiki was scaffolded with Obsidian-compatibility in mind:

1. **Markdown frontmatter** — Obsidian reads YAML frontmatter (`title:`, `tags:`, `related:`) into its property panel, so the reader can browse / filter pages by tags or maturity without touching a terminal.
2. **Tag system** — every page has a `tags:` line in frontmatter. Obsidian's tag pane lets the reader click a tag (e.g. `slicer`, `material`, `security`) and see every page that uses it.
3. **Local-first + plain markdown** — no lock-in. If the reader wants to read this wiki on GitHub instead, every page is rendered correctly there too. If they want to switch to VS Code, Logseq, or Cursor, the files just work.

### Day-1 setup

1. **Install Obsidian:** download from `obsidian.md`. Free; just click "Get Obsidian for Mac" (or Windows/Linux).
2. **Open this folder as a vault:**
   - Launch Obsidian → "Open folder as vault" → select the cloned `3D-Printing-Wiki/` folder
   - Obsidian indexes the folder. The wiki appears in the file explorer (left sidebar).
3. **Start at `wiki/index.md`:** click it in the file explorer. This is the catalog of every page; clickable markdown links navigate from there.
4. **Optional: themes / appearance** — Settings → Appearance → pick a theme (the default is fine; "Minimal" and "Things" are popular).

### What's gitignored (per-user, not committed)

The `.obsidian/` folder (Obsidian's per-vault settings — themes, plugin choices, pane layouts, hotkey customizations) is gitignored. Each user gets their own customization on their own machine; nothing leaks into the shared wiki. **This is intentional.** If the reader customizes their workspace it stays local.

### Plugins worth knowing about [TENTATIVE 2026-05-07 — recommendations not validated against current Obsidian plugin ecosystem]

Obsidian's "Community Plugins" let users extend the app. For this wiki, the reader may want:

- **Tag Wrangler** — bulk rename / merge tags. Useful as the wiki grows and the reader wants to consolidate similar tags.
- **Templater** — auto-fill new-page templates. Useful if the reader starts adding their own pages following the schema.
- **Dataview** — query frontmatter as a database (e.g. "show me every page with `maturity: draft`"). Powerful but optional.
- **Folder Note** — make a folder click open a same-named `.md` (so clicking `concepts/` opens `concepts/index.md` if it exists). Optional.

These are not required. Default Obsidian works fine for read-only navigation. [NEEDS VERIFICATION 2026-05-07] Specific plugin names and current availability should be re-checked at install time — the Obsidian plugin ecosystem changes.

### When NOT to use Obsidian

- **Reading on GitHub** — GitHub's web UI renders markdown + frontmatter cleanly. No app needed. Read-only is fine for casual browsing or sharing a single page.
- **Quick text edits via terminal** — `vim`, `nano`, or `code` (VS Code) are faster for one-line tweaks. Obsidian is heavier than necessary for two-character edits.
- **Mobile editing** — the iOS/Android apps work but are awkward for the schema-rigorous editing this wiki uses (YAML frontmatter, table editing, related-link bidirectionality). Mobile is best for read-only.

### Cross-link to wiki-navigation conventions

This page covers Obsidian-the-app. **How to navigate *this specific wiki* in Obsidian** (including the `@path` cross-link convention which is *not* native Obsidian wikilink syntax) is on [@concepts/wiki-navigation.md](../../concepts/wiki-navigation.md).

[CONFIRMED] Obsidian is free for personal use; reads markdown vaults; works on macOS/Windows/Linux. [TENTATIVE 2026-05-07] Specific plugin recommendations need re-verification at install time.

## Snippets

> "A second brain, for you, forever. Obsidian helps you organize your thoughts, find new connections, and unlock your full potential."
[Source: obsidian.md homepage, retrieved 2026-05-07]

> "Your notes are stored as plain text Markdown files in local folders, no proprietary formats, no vendor lock-in."
[Source: obsidian.md (paraphrased product positioning), retrieved 2026-05-07]
