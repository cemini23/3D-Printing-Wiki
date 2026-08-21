# 3D Printing Wiki

A local knowledge base for **FDM / FFF 3D printing** — research, materials, slicers, and production workflows. Curated from academic papers, vendor docs, and a Phase-0 toolchain audit. Built to be read in [Obsidian](https://obsidian.md) (free) or directly on GitHub.

The core thesis is **Bambu Labs as a practical production stack** for hobby + Etsy / MakerWorld work. There is also a first-time-owner path for the **Flashforge Adventurer 5M**.

Welcome — whether you are setting up a first printer or tightening a small production workflow, start with the links below.

---

## Start here

**Flashforge Adventurer 5M reader?** → [`FRIEND-SETUP.md`](FRIEND-SETUP.md) — clone, Obsidian + **Cursor Pro**, first-night reading order.

**Bambu reader?** Continue below.

1. **Open this folder in Obsidian** as a vault — or browse on GitHub.
2. **Read [`wiki/concepts/wiki-navigation.md`](wiki/concepts/wiki-navigation.md)** — a short meta-guide to the schema and navigation conventions.
3. **Then [`wiki/index.md`](wiki/index.md)** — the catalog of every page. Skim, then drill into what you need.

If you only have time for one document: read [`wiki/concepts/bambu-ecosystem-closed-loop.md`](wiki/concepts/bambu-ecosystem-closed-loop.md) — the load-bearing thesis for why this wiki rejects most “install Klipper / OctoPrint / random slicer” forum advice on Bambu.

---

## What's in here

Rough scale as of **2026-08-09** (see [`wiki/index.md`](wiki/index.md) for the live catalog):

| Kind | Count (approx.) | What’s covered |
|------|----------------:|----------------|
| **Source pages** | ~88 | Papers, vendor docs, audits, digest stubs (heavy on 2023–2026 FDM literature + Bambu primary sources) |
| **Concept pages** | ~28 | FDM physics, extrusion, fault detection, side-channels / IP, print farms, MaaS, materials baseline, VLMs, Bambu closed-loop ecosystem, AI design tooling, novice CAD, wiki navigation |
| **Materials** | 5 | PLA · PETG · ABS · ASA · TPU |
| **Printers** | 4 | Bambu X1C · P1S · A1 (+ mini) · Flashforge Adventurer 5M |
| **Slicers** | 2 | Bambu Studio (native daily driver) · OrcaSlicer (advanced calibration) |
| **Tools** | ~10 | Obsidian, Cursor, FDM Test V4, AI mesh tools, OpenVCAD, reBot-DevArm, and related |

Daily research sweeps live under `wiki/sweeps/` (operator cadence notes — not required reading for day one).

---

## What's NOT in here

- **`raw-sources/`** — PDFs and similar primary files. Local-only (gitignored); mostly copyrighted. Source pages cite filename + page / DOI / arXiv; fetch originals yourself when you need the full paper.
- **`research to be indexed/`** — transient drop zone before ingest (gitignored).
- **`briefs/`** — one-off deliverables staged for other tools (gitignored).
- **`hot.md`** — ephemeral session-state cache (gitignored).
- **`.env`** — secrets (Brave / Exa / Context7 / DeepSeek, etc.). Copy `.env.example` and use your own keys.

---

## Conventions

Every wiki page has YAML frontmatter (`title`, `type`, `tags`, `keywords`, `related`, `maturity`, `created`, `updated`) plus structured body sections. Cross-links use `@path/to/page.md` (not Obsidian `[[wikilinks]]` — see the navigation guide for why).

Confidence tags in body text:

- `[CONFIRMED]` — ≥2 independent sources, or personally tested
- `[TENTATIVE 2026-05-07]` — single source or circumstantial; treat as “probably true”
- `[NEEDS VERIFICATION 2026-05-07]` — plausible but unchecked
- `[RETRACTED]` — disproven; kept for context

**Most pages are `maturity: draft`.** Synthesis comes from primary sources; cross-validation is incremental. For buying decisions, double-check the cited source.

---

## Schema enforcement

```bash
python3 scripts/wiki_lint.py
```

Catches orphans, broken cross-links, and frontmatter issues. Other helpers in `scripts/`:

- `preingest_check.py` — duplicate detection before a new source (sha256 / arXiv / DOI / URL / filename / title)
- `wiki_gap_detect.py` — cited-unread stubs, stale `[NEEDS VERIFICATION]` tags, thin concept pages

---

## Day-1 toolchain (Bambu)

If you are new to Bambu and setting up a printer for the first time:

**Install**

1. **Bambu Studio** — [`bambulab/BambuStudio`](https://github.com/bambulab/BambuStudio) (AGPL-3.0). Mandatory native slicer.
2. **OrcaSlicer** — [`OrcaSlicer/OrcaSlicer`](https://github.com/OrcaSlicer/OrcaSlicer) (AGPL-3.0). Advanced calibration only — not the daily driver. ([Why?](wiki/entities/slicers/orcaslicer.md))
3. **Kickstarter Autodesk FDM Test V4** — [`kickstarter/kickstarter-autodesk-3d`](https://github.com/kickstarter/kickstarter-autodesk-3d) (Apache-2.0). One-time standardized calibration print.
4. **Obsidian** — [obsidian.md](https://obsidian.md) (free for personal use). Comfortable reader for this wiki.

**Skip on Bambu** (when forums push them): Klipper, Marlin, OctoPrint, PrusaSlicer-as-daily, Cura, Voron CAD repos, and most of the rest of the 25-repo audit’s NO-GO set. See [`wiki/concepts/bambu-ecosystem-closed-loop.md`](wiki/concepts/bambu-ecosystem-closed-loop.md) or [`wiki/sources/2026-bambu-toolchain-audit.md`](wiki/sources/2026-bambu-toolchain-audit.md).

Flashforge Adventurer 5M owners: use **Orca-Flashforge** and start at [`FRIEND-SETUP.md`](FRIEND-SETUP.md) — not the Bambu Studio path above.

---

## Cemini wiki federation

**Eight** wikis + private **Cemini Financial Suite**. Cross-links: `@<alias>/path/to/page.md` (see `CLAUDE.md` → Related Wikis).

| Alias | Repository | Visibility | Focus |
|-------|------------|------------|--------|
| **`3d-printing-wiki`** | **This repo** ([3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki)) | **Public** | FDM/FFF, Bambu, slicers, print farms |
| `gambling-wiki` | [Gambling-wiki](https://github.com/cemini23/Gambling-wiki) | **Public** | Sports betting, casino, poker, DFS |
| `game-dev-wiki` | [Game-Dev-wiki](https://github.com/cemini23/Game-Dev-wiki) | **Public** | Hobby game dev — castle/RTS, Godot evals |
| `ccc-wiki` | [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC) | **Public** | Cursor / Claude Code workflow, MCP |
| `image-gen-wiki` | [uncensored-image-gen-wiki](https://github.com/cemini23/uncensored-image-gen-wiki) | Public | Image / video generation |
| `seo-wiki` | [SEO-GEO-B-M-Wiki](https://github.com/cemini23/SEO-GEO-B-M-Wiki) | Public | Local SEO, GEO/AEO |
| `cybersecurity-wiki` | [Cybersecurity-wiki](https://github.com/cemini23/Cybersecurity-wiki) | Public | Pentest; physical-security / RFID overlap |
| `osint-wiki` | `llm-wiki-by-cemini` *(private)* | **Private** | Financial research |
| *Cemini Financial Suite* | `Cemini-Financial-Suite` *(private)* | **Private** | Trading stack (not a wiki) |

**Privacy:** **`ccc-wiki` is public.** **`osint-wiki`** and **Cemini Financial Suite** are private.

---

## Support

Thank you for using this wiki — forks, stars, corrections, and quiet reading all help keep the research public.

If you want to go further, optional tips fund open research and tooling. **Donation-only addresses** — not trading or production wallets.

| Chain family | Address |
|--------------|---------|
| **X Money** (fiat, US) | Request [@Cemini23](https://x.com/Cemini23) in the X app — scan the Request QR |
| **EVM** (Ethereum, Polygon, Base, Arbitrum, …) | `0x444C5C2eC439E0382aa5a17F70313c536BcC5D58` |
| **Solana / SVM** | `J4zNn4hK9jTrKBFY8sbAGJHLoZvXvQf4B9pQSbSrocZE` |
| **Polymarket** (referral) | [polymarket.com/?r=Cemini23](https://polymarket.com/?r=Cemini23) |
| **Hyperliquid** (referral) | [app.hyperliquid.xyz/join/CEMINI23](https://app.hyperliquid.xyz/join/CEMINI23) |

**Projects & writing** (also a great way to support the work):

| Project | Link | What it is |
|---------|------|------------|
| **Outlier Weekly** | [outlierweekly.substack.com](https://outlierweekly.substack.com) | Methodology newsletter — markets, research systems, and open tooling notes |
| **Atto** | [youratto.com](https://youratto.com) | Private desktop organizer for Italian family / citizenship document packets |
| **GuruWatcher** | [guruwatcher.com](https://guruwatcher.com) | Local app: newsletter price levels → Discord alerts (alert-only; never trades) |
| **YouTube** | [@Cemini23](https://www.youtube.com/@Cemini23) | Walkthroughs and demos |

Canonical donation copy across the federation: [SUPPORT.md](https://github.com/cemini23/cemini-claude-code-CCC/blob/main/SUPPORT.md) on CCC.

---

## License

[MIT](LICENSE) — wiki content, scripts, and configuration are free to use, modify, and redistribute. Built so any hobbyist or small-business owner getting into 3D printing can lift it, fork it, or contribute back.

Cited primary sources (academic papers, vendor docs) remain under their original licenses and copyrights — they are not redistributed here (see `.gitignore`). To verify a claim, use the title / DOI / arXiv ID on the source page.

---

## Status

- Wiki: **~138 core pages** (+ daily sweeps under `wiki/sweeps/`); ~990 outbound `related:` edges as of 2026-08-09
- Inbox: empty (auto-fetch arXiv-only; news off — triage in the morning)
- Schema: HEAVY-mode (full bidirectional cross-link enforcement)
- Maturity: mostly `draft`; iterating with each ingest

See [`ROADMAP.md`](ROADMAP.md) for active workstreams and [`wiki/log.md`](wiki/log.md) for ingest history.

## Related

- Newsletter: [Outlier Weekly](https://outlierweekly.substack.com)
- Products: [Atto](https://youratto.com) · [GuruWatcher](https://guruwatcher.com)
- YouTube: [@Cemini23](https://www.youtube.com/@Cemini23)
- Wiki federation hub: [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC)
- Agent toolkit: [wikilint](https://github.com/cemini23/wikilint) · [vet](https://github.com/cemini23/vet) · [ara-schema](https://github.com/cemini23/ara-schema)
- Sibling wikis: [SEO/GEO](https://github.com/cemini23/SEO-GEO-B-M-Wiki) · [Cybersecurity](https://github.com/cemini23/Cybersecurity-wiki) · [Image Gen](https://github.com/cemini23/uncensored-image-gen-wiki) · [Gambling](https://github.com/cemini23/Gambling-wiki) · [Game Dev](https://github.com/cemini23/Game-Dev-wiki)
