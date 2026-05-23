# Friend setup — Flashforge Adventurer 5M + this wiki

**Cost: $0** for the wiki + Obsidian + Claude.ai free tier. No API keys, no terminal, no MCP servers on night one.

Your printer: **Flashforge Adventurer 5M** (CoreXY, Klipper firmware, Orca-Flashforge slicer). Most of this wiki was written for Bambu — start at the Flashforge page below; it tells you what applies to you and what to skip.

---

## Download (5 minutes)

### Option A — GitHub clone (recommended; gets updates)

```bash
git clone https://github.com/cemini23/3D-Printing-Wiki.git
cd 3D-Printing-Wiki
```

No GitHub account required for a public clone. If you don't have Git installed: download the green **Code → Download ZIP** button on [github.com/cemini23/3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki) and unzip.

### Option B — AirDrop / USB / Google Drive

If someone hands you a zip of the folder, that works too — you just won't get `git pull` updates later.

---

## Install Obsidian (10 minutes)

1. Download from [obsidian.md](https://obsidian.md) (free for personal use).
2. Open Obsidian → **Open folder as vault**.
3. Select the `3D-Printing-Wiki/` folder you cloned or unzipped.
4. Click **`FRIEND-SETUP.md`** (this file) or **`README.md`** in the left sidebar.

Optional plugins (Settings → Community plugins): Tag Wrangler, Dataview. Not required for reading.

---

## Claude.ai — your AI layer (5 minutes)

1. Sign up at [claude.ai](https://claude.ai) (free tier is fine for tonight).
2. Don't pay on day one — see if you hit the daily message cap first.

**How to use the wiki with Claude:**

1. Find a page in Obsidian (e.g. `wiki/entities/materials/petg.md`).
2. Copy the page text (Cmd+A → Cmd+C).
3. Paste into Claude.ai and add your question at the bottom.

**Structured prompt template** (paste this, fill in the blanks):

```
Printer:   Flashforge Adventurer 5M (open-frame, CoreXY, Klipper, 220×220×220 mm)
Filament:  [brand + type + color]
Slicer:    Orca-Flashforge [version]
Symptom:   [what you see]
Tried:     [what you already changed]
Question:  [your actual ask]
```

Attach a photo when the problem is visual.

**Two rules:**

1. **Never trust AI for specific numbers** (nozzle temp, retraction, flow %). Use filament datasheets and slicer profiles. AI is for diagnosis, not calibration values.
2. **Never run AI-generated G-code** without reading it line by line. AI-generated STL/3MF geometry is fine; `.gcode` is not.

---

## First-night reading order

Read in Obsidian, in this order:

1. [`wiki/entities/printers/flashforge-adventurer-5m.md`](wiki/entities/printers/flashforge-adventurer-5m.md) — **start here** (your printer; what in this wiki applies to you)
2. [`wiki/concepts/wiki-navigation.md`](wiki/concepts/wiki-navigation.md) — how pages link together (~5 min)
3. [`wiki/index.md`](wiki/index.md) — catalog of everything
4. [`wiki/concepts/fdm-printing.md`](wiki/concepts/fdm-printing.md) — FDM fundamentals
5. [`wiki/concepts/filaments-baseline.md`](wiki/concepts/filaments-baseline.md) — material decision matrix
6. [`wiki/entities/materials/pla.md`](wiki/entities/materials/pla.md) and [`wiki/entities/materials/petg.md`](wiki/entities/materials/petg.md) — your first two filaments
7. [`wiki/concepts/vlm-in-manufacturing.md`](wiki/concepts/vlm-in-manufacturing.md) — how to ask AI about prints safely

**Skip tonight (and probably all of month 1):** security, **print-farm**, MaaS, Bambu-closed-firmware, **shape-changing / 4D / pneumatics**, and anything requiring an AR headset. See [`wiki/concepts/novice-cad-workflows.md`](wiki/concepts/novice-cad-workflows.md) for when to start designing your own parts (spoiler: week 2, Tinkercad — not tonight).

---

## Week 2 — when you want to make your own parts

Read [`wiki/concepts/novice-cad-workflows.md`](wiki/concepts/novice-cad-workflows.md). Short version:

1. Keep downloading STLs until you've had ~10 good prints.
2. Sign up for **Tinkercad** (free, browser) — export STL → Orca-Flashforge.
3. Still skip AI model generators and print-farm wiki pages.

---

## What you do NOT need tonight

- DeepSeek / Exa / Brave API keys (`.env` — author tooling only)
- Claude Code CLI (optional week 2+; requires paid Claude)
- MCP servers, custom skills, or the CCC wiki
- PDFs in `raw-sources/` (not in the GitHub repo anyway — source pages cite them by name)

---

## Week 2+ (optional)

- **Claude Code CLI** — reads wiki files directly without copy-paste; needs Claude Pro (~$20/mo). See [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC) when ready.
- **Orca-Flashforge** — your slicer; install from Flashforge if you haven't already.
- **Tinkercad** — free browser CAD for first original designs (week 2+). See `wiki/concepts/novice-cad-workflows.md`.
- **AI design tools** (Meshy, RodinAI, etc.) — read `wiki/concepts/ai-design-tools.md` after you've shipped a few prints.

---

## Stuck?

1. Search the wiki in Obsidian (Cmd+Shift+F).
2. Paste-then-ask Claude.ai with the template above.
3. Ask the person who sent you this wiki — most pages are still `maturity: draft`.
