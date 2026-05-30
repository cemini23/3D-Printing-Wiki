# 3D Printing Wiki — Bambu Labs Production Workflow

A local knowledge base for setting up and operating a Bambu Labs 3D printer for hobby + Etsy / MakerWorld production. Curated from academic papers, vendor docs, and a 25-repo Phase-0 toolchain audit. Designed to be read in [Obsidian](https://obsidian.md) (free) or directly on GitHub.

---

## Start here

**Flashforge Adventurer 5M reader?** → [`FRIEND-SETUP.md`](FRIEND-SETUP.md) — clone, Obsidian + **Cursor Pro**, first-night reading order.

**Bambu reader?** Continue below.

1. **Open this folder in Obsidian** as a vault — or just browse on GitHub.
2. **Read [`wiki/concepts/wiki-navigation.md`](wiki/concepts/wiki-navigation.md)** — five-minute meta-guide to the schema and navigation conventions.
3. **Then [`wiki/index.md`](wiki/index.md)** — the catalog of every page. Skim, then drill into whatever interests you.

If you only have time for one document: read [`wiki/concepts/bambu-ecosystem-closed-loop.md`](wiki/concepts/bambu-ecosystem-closed-loop.md) — it's the load-bearing thesis for why this wiki rejects most 3D-printing forum advice.

---

## What's in here

50 wiki pages, organized into:

- **18 source pages** — one per ingested research paper / vendor doc / audit. Heavy on 2023-2026 academic FDM literature plus Bambu Labs primary sources.
- **18 concept pages** — synthesis hubs covering FDM physics, extrusion control, fault detection, side-channel attacks, IP theft, print farms, manufacturing-as-a-service, materials baseline, VLMs in manufacturing, the Bambu closed-firmware ecosystem, AI-design tooling, and wiki navigation.
- **5 materials entity pages** — PLA / PETG / ABS / ASA / TPU.
- **5 printer entity pages** — Bambu X1C / P1S / A1 (+ mini) + Flashforge Adventurer 5M (friend reader).
- **2 slicer entity pages** — Bambu Studio (mandatory native), OrcaSlicer (advanced calibration only).
- **4 tools entity pages** — Obsidian, FDM Test V4 calibration print, reBot-DevArm, markdown-preview-pluk (cross-wiki stub).

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

## Cemini wiki federation

**Six** wikis + private **Cemini Financial Suite**. Cross-links: `@<alias>/path/to/page.md` (`CLAUDE.md` → Related Wikis).

| Alias | Repository | Visibility | Focus |
|-------|------------|------------|--------|
| **`3d-printing-wiki`** | **This repo** ([3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki)) | **Public** | FDM/FFF, Bambu, slicers, print farms |
| `ccc-wiki` | [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC) | **Public** | Cursor / Claude Code workflow, MCP |
| `image-gen-wiki` | [uncensored-image-gen-wiki](https://github.com/cemini23/uncensored-image-gen-wiki) | Public | Image / video generation |
| `seo-wiki` | [SEO-GEO-B-M-Wiki](https://github.com/cemini23/SEO-GEO-B-M-Wiki) | Public | Local SEO, GEO/AEO |
| `cybersecurity-wiki` | [Cybersecurity-wiki](https://github.com/cemini23/Cybersecurity-wiki) | Public | Pentest; physical-security / RFID overlap |
| `osint-wiki` | `llm-wiki-by-cemini` *(private)* | **Private** | Financial research |
| *Cemini Financial Suite* | `Cemini-Financial-Suite` *(private)* | **Private** | Trading stack (not a wiki) |

**Privacy:** **`ccc-wiki` is public.** **`osint-wiki`** and **Cemini Financial Suite** are private.

---

## License

[MIT](LICENSE) — wiki content, scripts, and configuration are free to use, modify, and redistribute. Built so any hobbyist or small-business owner getting into 3D printing can lift it, fork it, or contribute back.

Cited primary sources (academic papers, vendor docs) remain under their original licenses and copyrights — they are not redistributed in this repo (see `.gitignore`). To verify a specific claim against its primary source, find the paper via the title or DOI in the source page's frontmatter.

---

## Status

- Wiki: **57 pages**, 401 cross-links, lint clean as of 2026-05-23
- Inbox: 37 PDFs/docx awaiting ingest
- Schema: HEAVY-mode (full bidirectional cross-link enforcement)
- Maturity: `draft` for most pages; iterating

See [`ROADMAP.md`](ROADMAP.md) for active workstreams and [`wiki/log.md`](wiki/log.md) for full ingest history.

## Related

- Methodology newsletter: [Outlier Weekly](https://outlierweekly.substack.com)
- YouTube: [@Cemini23](https://www.youtube.com/@Cemini23)
- Wiki federation hub: [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC)
- Agent toolkit: [wikilint](https://github.com/cemini23/wikilint) · [vet](https://github.com/cemini23/vet) · [ara-schema](https://github.com/cemini23/ara-schema)
- Sibling wikis: [SEO/GEO](https://github.com/cemini23/SEO-GEO-B-M-Wiki) · [Cybersecurity](https://github.com/cemini23/Cybersecurity-wiki) · [Image Gen](https://github.com/cemini23/uncensored-image-gen-wiki)
