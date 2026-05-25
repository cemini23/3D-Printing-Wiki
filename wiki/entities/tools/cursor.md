---
title: Cursor — IDE with AI Chat for This Wiki
type: entity
tags: [tool, cursor, IDE, AI, chat, friend-handoff]
keywords: [Cursor, Cursor Pro, Agent, Chat, @file references, Open Folder, Flashforge friend]
related:
  - concepts/novice-cad-workflows.md
  - concepts/vlm-in-manufacturing.md
  - concepts/wiki-navigation.md
  - entities/tools/obsidian.md
  - entities/printers/flashforge-adventurer-5m.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
---

## Relations

@concepts/novice-cad-workflows.md @concepts/vlm-in-manufacturing.md @concepts/wiki-navigation.md @entities/tools/obsidian.md @entities/printers/flashforge-adventurer-5m.md

## Raw Concept

Friend-handoff entity (2026-05-23): the non-Bambu beginner uses **Cursor Pro** ($20/mo) instead of Claude.ai or Claude Code CLI. `FRIEND-SETUP.md` is the canonical install guide; this page records why Cursor fits the wiki workflow.

## Narrative

### What Cursor is here

**Cursor** is a code editor (VS Code–based) with built-in **Chat** and **Agent**. For this wiki, it replaces:

- **claude.ai** paste-then-ask (no longer the friend path)
- **Claude Code CLI** (not required; primary maintainer may still use it separately)

The friend **opens the cloned `3D-Printing-Wiki/` folder** in Cursor and references pages with **`@wiki/...`** in Chat so the model reads files directly.

### Day-1 setup (friend)

1. Install from [cursor.com](https://cursor.com); sign in to **Pro**.
2. **File → Open Folder** → `3D-Printing-Wiki/`.
3. Use **Chat** (`Cmd+L` / `Ctrl+L`) — prefer over **Agent** for Q&A (Agent can edit repo files).
4. Optional: **Obsidian** on the same folder for comfortable reading — see @entities/tools/obsidian.md.

### Settings — keep minimal

| Area | Recommendation |
|------|----------------|
| **Mode** | **Chat / Ask** for troubleshooting and wiki questions |
| **Models** | **Auto** or default — sufficient for markdown wiki Q&A |
| **MCP** | None on day 1 |
| **Rules** | Repo ships `.cursor/rules/friend-flashforge-reader.mdc` + root `AGENTS.md` |
| **Privacy** | User preference in Cursor Settings |

### Workflow vs Obsidian

| Tool | Role |
|------|------|
| **Obsidian** | Browse, search, read long pages |
| **Cursor Chat** | Ask questions with `@` file context + print photos |
| **Orca-Flashforge** | Slice STLs — outside Cursor |

### What not to adopt (friend)

- **Claude Code CLI** — different product; not needed with Cursor Pro
- **claude-obsidian** Obsidian plugin — @entities/tools/obsidian.md flags DO NOT ADOPT
- **MCP / `.env` keys** — maintainer tooling (Brave, Exa, etc.)
- **@ccc-wiki** advanced harness — optional for power users only

### Pro plan expectations [TENTATIVE 2026-05-23]

Cursor Pro (~$20/mo) includes extended Agent usage and frontier models; exact credit pools change — verify on [cursor.com/pricing](https://cursor.com/pricing). Typical wiki Q&A + occasional print-debug chats are light usage vs all-day coding Agent loops.

[TENTATIVE 2026-05-23] Friend handoff assumes individual Pro, not Teams ($40/seat).

## Snippets

> "Type `@` and start typing a path — pick files from the list. The model reads them from your folder; no copy-paste from Obsidian required." [Source: FRIEND-SETUP.md]
