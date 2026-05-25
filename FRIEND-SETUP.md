# Friend setup — Flashforge Adventurer 5M + this wiki + Cursor Pro

**Your stack:** Obsidian (free, reading) + **Cursor Pro** (~$20/mo, AI that reads the wiki folder) + Orca-Flashforge (slicer). No Claude.ai, no Claude Code CLI, no API keys, no MCP servers on night one.

Your printer: **Flashforge Adventurer 5M** (CoreXY, Klipper firmware, Orca-Flashforge slicer). Most of this wiki was written for Bambu — start at the Flashforge page below; it tells you what applies to you and what to skip.

---

## Download the wiki (5 minutes)

### Option A — GitHub clone (recommended; gets updates)

```bash
git clone https://github.com/cemini23/3D-Printing-Wiki.git
cd 3D-Printing-Wiki
```

No GitHub account required for a public clone. No Git? Use **Code → Download ZIP** on [github.com/cemini23/3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki) and unzip.

### Option B — AirDrop / USB / Google Drive

A zip of the folder works; you won't get `git pull` updates later.

---

## Install Cursor (10 minutes)

1. Download from [cursor.com](https://cursor.com) (Mac / Windows / Linux).
2. Sign in and activate **Pro** ($20/mo) — you already have this plan.
3. **File → Open Folder…** → select the `3D-Printing-Wiki/` folder you cloned or unzipped.
4. Open this file: **`FRIEND-SETUP.md`** (you're here).

**First-run settings (keep it simple):**

| Setting | What to do |
|---------|------------|
| **Default mode** | Use **Chat** (Ask) for questions — not **Agent** unless you want the AI to edit files in the repo |
| **Models** | Leave on **Auto** or default; no need to pick frontier models manually for wiki Q&A |
| **Privacy** | Your choice (Cursor Settings → Privacy). Fine for a personal wiki clone |
| **MCP** | **Off / ignore** for now — no Brave, GitHub, or custom MCP setup required |
| **Rules** | This repo includes `.cursor/rules/friend-flashforge-reader.mdc` — Cursor loads it automatically when the folder is open |

**Do not install:** Claude Code CLI, Claude Desktop as a separate daily driver, or the Obsidian *claude-obsidian* plugin (see `wiki/entities/tools/obsidian.md`).

---

## Install Obsidian (optional but nice for reading)

Obsidian is a comfortable **reader** for long wiki pages. Cursor is where you **ask questions** with `@` file references.

1. Download from [obsidian.md](https://obsidian.md) (free for personal use).
2. **Open folder as vault** → same `3D-Printing-Wiki/` folder.
3. Use Obsidian for reading; use Cursor for AI.

**Optional Obsidian plugins** (Settings → Community plugins): Tag Wrangler, Dataview. Not required.

---

## How to use Cursor with this wiki (main workflow)

### 1. Reference wiki pages with `@`

In **Chat** (sidebar or `Cmd+L` on Mac / `Ctrl+L` on Windows):

```
@wiki/entities/printers/flashforge-adventurer-5m.md
@wiki/entities/materials/petg.md

My first layer won't stick on the left side of the bed. I'm on stock PLA, Orca-Flashforge default profile.
What should I check first?
```

Type `@` and start typing a path — pick files from the list. The model reads them from your folder; **no copy-paste from Obsidian required**.

**Good first `@` targets:**

- `@FRIEND-SETUP.md` — this guide
- `@wiki/entities/printers/flashforge-adventurer-5m.md` — your printer
- `@wiki/concepts/novice-cad-workflows.md` — what to skip (print farm, scanners, etc.)
- `@wiki/concepts/vlm-in-manufacturing.md` — how to ask safely

### 2. Attach photos of failed prints

Drag an image into the chat or paste a screenshot. Combine with the structured template below.

### 3. Structured prompt template

```
Printer:   Flashforge Adventurer 5M (open-frame, CoreXY, Klipper, 220×220×220 mm)
Filament:  [brand + type + color]
Slicer:    Orca-Flashforge [version]
Symptom:   [what you see]
Tried:     [what you already changed]
Ambient:   [room temp; draft?]
Photo:     [attached if visual]
Question:  [your actual ask]
```

### 4. Chat vs Agent

| Mode | Use for |
|------|---------|
| **Chat / Ask** | Troubleshooting, "what filament?", "what does this wiki page mean?" — **default** |
| **Agent** | Only when you want it to edit markdown or run commands — skip until you understand git |

**Two rules (same as before):**

1. **Never trust AI for specific numbers** (nozzle temp, retraction, flow %). Use filament datasheets and Orca profiles.
2. **Never run AI-generated G-code** without reading every line. STL/3MF from trusted sources is fine; random `.gcode` is not.

More detail: `wiki/concepts/vlm-in-manufacturing.md`, `wiki/concepts/ai-design-tools.md`.

---

## First-night reading order

Read in **Obsidian** or **Cursor** (open the files in the editor), in this order:

1. `wiki/entities/printers/flashforge-adventurer-5m.md` — **start here**
2. `wiki/concepts/wiki-navigation.md` — schema (~5 min)
3. `wiki/index.md` — catalog
4. `wiki/concepts/fdm-printing.md` — fundamentals
5. `wiki/concepts/filaments-baseline.md` — materials
6. `wiki/entities/materials/pla.md` and `wiki/entities/materials/petg.md`
7. `wiki/concepts/vlm-in-manufacturing.md` — prompt discipline

**Skip month 1:** print-farm, MaaS, security, shape-changing / 4D, Bambu-only toolchain pages. See `wiki/concepts/novice-cad-workflows.md`.

---

## Week 2 — your own parts

1. ~10 good prints from downloaded STLs first.
2. **Tinkercad** (free) → export STL → Orca-Flashforge.
3. In Cursor: `@wiki/concepts/novice-cad-workflows.md` before buying gadgets (3D scanner, etc.).

---

## What you do NOT need

| Skip | Why |
|------|-----|
| Claude.ai / Claude Code | You're on **Cursor Pro** instead |
| MCP servers, `.env` API keys | Author tooling; not for beginners |
| CCC wiki / custom skills | Power-user layer for the person who maintains this repo |
| 3D scanner (month 1) | Calipers + phone photos + Cursor; see prior chat / `novice-cad-workflows` |
| PDFs in `raw-sources/` | Not in the GitHub repo |

---

## Stuck?

1. **Cmd+Shift+F** in Cursor — search the wiki.
2. **Chat** with `@` on the relevant page + template above + photo.
3. Ask the person who sent you this wiki.

**Cursor Pro tip:** If you burn through fast premium usage, use **Auto** model for routine questions or upgrade to Pro+ — only if you hit limits; normal wiki Q&A is light usage.
