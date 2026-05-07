# 3D Printing Wiki — Bambu Labs Production Workflow

A local knowledge base for setting up and operating a Bambu Labs 3D printer for hobby + Etsy / MakerWorld production. Curated from academic papers, vendor docs, and a 25-repo Phase-0 toolchain audit. Designed to be read in [Obsidian](https://obsidian.md) (free) or directly on GitHub.

---

## Start here

1. **Open this folder in Obsidian** as a vault — or just browse on GitHub.
2. **Read [`wiki/concepts/wiki-navigation.md`](wiki/concepts/wiki-navigation.md)** — five-minute meta-guide to the schema and navigation conventions.
3. **Then [`wiki/index.md`](wiki/index.md)** — the catalog of every page. Skim, then drill into whatever interests you.

If you only have time for one document: read [`wiki/concepts/bambu-ecosystem-closed-loop.md`](wiki/concepts/bambu-ecosystem-closed-loop.md) — it's the load-bearing thesis for why this wiki rejects most 3D-printing forum advice.

---

## What's in here

41 wiki pages, organized into:

- **18 source pages** — one per ingested research paper / vendor doc / audit. Heavy on 2023-2026 academic FDM literature plus Bambu Labs primary sources.
- **15 concept pages** — synthesis hubs covering FDM physics, extrusion control, fault detection, side-channel attacks, IP theft, print farms, manufacturing-as-a-service, materials baseline, VLMs in manufacturing, the Bambu closed-firmware ecosystem, and AI-design tooling.
- **5 materials entity pages** — PLA / PETG / ABS / ASA / TPU.
- **2 slicer entity pages** — Bambu Studio (mandatory native), OrcaSlicer (advanced calibration only).
- **1 tools entity page** — Kickstarter / Autodesk FDM Test V4 calibration print.
- **1 meta entity page** — Obsidian, the recommended reader.

See [`wiki/index.md`](wiki/index.md) for a one-line summary of every page.

---

## What's NOT in here

- **`raw-sources/`** — the actual PDF files of every ingested paper plus the Bambu toolchain audit `.docx`. These live local-only (gitignored): ~17 files, mostly copyrighted academic papers. Source pages cite them by filename + page number; if you need the full PDF, find it via DOI or arXiv ID in the source's frontmatter.
- **`research to be indexed/`** — transient drop zone for new sources before ingest (gitignored).
- **`briefs/`** — one-off deliverables staged for distribution to other tools (gitignored).
- **`hot.md`** — ephemeral session-state cache (gitignored).
- **`.env`** — secrets (API keys for Brave / Exa / Context7 / DeepSeek). Use `.env.example` as the template; supply your own keys.

---

## Conventions

Every wiki page has YAML frontmatter (`title`, `type`, `tags`, `keywords`, `related`, `maturity`, `created`, `updated`) plus structured body sections. Cross-links use `@path/to/page.md` syntax (NOT Obsidian's native `[[wikilinks]]` — see the navigation guide for why).

Confidence tags inside body text:

- `[CONFIRMED]` — ≥2 independent sources
- `[TENTATIVE 2026-05-07]` — single source or circumstantial; treat as "probably true"
- `[NEEDS VERIFICATION 2026-05-07]` — plausible but unchecked
- `[RETRACTED]` — disproven; kept for context

**Most pages are `maturity: draft`**. The synthesis is built from primary sources but cross-validation is incremental — if you act on a claim that drives a buying decision, double-check the source.

---

## Schema enforcement

The wiki has a lint script that catches orphan pages, broken cross-links, and frontmatter errors:

```bash
python3 scripts/wiki_lint.py
```

Clean output = 0 orphans, 0 bidirectional gaps, 0 dangling links.

Other scripts in `scripts/`:

- `preingest_check.py` — duplicate detection before adding a new source (sha256 / arXiv ID / DOI / URL / filename / title)
- `wiki_gap_detect.py` — flags cited-unread stubs, stale `[NEEDS VERIFICATION]` tags, thin concept pages

---

## Day-1 toolchain (the punchline)

If you're new to Bambu and reading this wiki to set up a printer for the first time:

**Install:**
1. **Bambu Studio** — `bambulab/BambuStudio` (AGPL-3.0). Mandatory native slicer.
2. **OrcaSlicer** — `OrcaSlicer/OrcaSlicer` (AGPL-3.0). Use for advanced calibration only — NOT daily driver. ([Why?](wiki/entities/slicers/orcaslicer.md))
3. **Kickstarter Autodesk FDM Test V4** — `kickstarter/kickstarter-autodesk-3d` (Apache-2.0). One-time download; standardized calibration print.
4. **Obsidian** — `obsidian.md` (free for personal use). To read this wiki.

**Ignore** (when 3D-printing forums tell you to install them on Bambu): Klipper, Marlin, OctoPrint, PrusaSlicer-as-daily, Cura, Voron CAD repos, and ~22 other repos in 4 rejection patterns. See [`wiki/concepts/bambu-ecosystem-closed-loop.md`](wiki/concepts/bambu-ecosystem-closed-loop.md) for the rationale or [`wiki/sources/2026-bambu-toolchain-audit.md`](wiki/sources/2026-bambu-toolchain-audit.md) for the per-repo table.

---

## License

The wiki content (everything in `wiki/`, this README, `CLAUDE.md`, `LESSONS.md`, `ROADMAP.md`) is the curator's synthesis and analysis — no explicit license set yet (default copyright applies). The scripts in `scripts/` likewise.

Cited primary sources (academic papers, vendor docs) remain under their original copyrights — not redistributed in this repo (see `.gitignore`).

---

## Status

- Wiki: **41 pages**, 274 cross-links, lint clean as of 2026-05-07
- Inbox: 42 PDFs/docx awaiting ingest
- Schema: HEAVY-mode (full bidirectional cross-link enforcement)
- Maturity: `draft` for most pages; iterating

See [`ROADMAP.md`](ROADMAP.md) for active workstreams and [`wiki/log.md`](wiki/log.md) for full ingest history.
