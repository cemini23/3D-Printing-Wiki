# Agent instructions — 3D Printing Wiki

## Friend reader (Flashforge Adventurer 5M)

If the user is a **beginner** on a **Flashforge Adventurer 5M** using **Cursor Pro** (not Claude Code):

1. Read `FRIEND-SETUP.md` and `@wiki/entities/printers/flashforge-adventurer-5m.md` before giving printer advice.
2. **Slicer endpoint is Orca-Flashforge**, not Bambu Studio. Ignore Bambu AMS / MakerWorld-native flows unless explicitly comparing.
3. **Do not invent** nozzle temps, retraction, flow %, or G-code — point to datasheets, Orca profiles, and wiki sources. Use structured prompts (printer / filament / slicer / symptom / tried).
4. **Skip** print-farm, MaaS, shape-changing / 4D, and security topics unless the user asks.
5. Prefer **Chat-style answers**; do not edit wiki files unless the user asks for documentation changes.
6. For design: week 1 = download STLs; week 2 = Tinkercad — see `wiki/concepts/novice-cad-workflows.md`.

## Primary maintainer

Full schema: `CLAUDE.md`. Wiki catalog: `wiki/index.md`. Lint: `python3 scripts/wiki_lint.py`.
