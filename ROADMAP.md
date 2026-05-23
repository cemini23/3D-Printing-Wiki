# 3D Printing Workspace — ROADMAP

Active workstreams, open decisions, and the done log. Read at session start; update at session end.

---

## Active workstreams

### W1 — Initial research ingest pass

**Status:** Ingest passes 1–6 complete through 2026-05-07; **ingest pass 7** (shape-changing / 4D FDM cluster, 4 papers) done 2026-05-23. **38 PDFs/docx remaining** in inbox. Wiki has **55 pages** (22 source + 19 concept + …).

Source-mix surprise (still applies): ~58 of original 62 are academic AM/3D-printing papers. Curation surfaces practical takeaways for the reader; some papers may go in as background-context one-liners rather than full pages.

**Cluster picked first:** print-quality control on consumer-grade FDM (input shaping, extrusion control, fault detection, high-speed FDM). Reasoning — directly relevant to a reader buying a Bambu, and the 5 papers cross-reference cleanly into a connected cluster.

**Scope still to populate (subsequent passes):**
- Printers: Bambu X1C (or whichever model the reader chooses), comparable printers for context
- Materials: PLA / PETG / ABS / TPU baseline pages; specialty materials as sources warrant
- Slicers: Bambu Studio, OrcaSlicer (Bambu fork)
- AI design tools: any GitHub repos in the source drop
- Store ops: Etsy, MakerWorld, Printables — listing patterns, pricing, shipping
- Security: side-channel IP-theft attacks (3+ papers in inbox — relevant if reader wants to protect commercial designs)
- Volumetric AM, neuromorphic anomaly detection, photonics (likely background-only; reader won't be running these)

---

## Open decisions

- Reader's specific Bambu model (X1C? P1S? A1?) — defer until reader chooses; entity pages can stay generic-Bambu until then
- Whether to track filament inventory inside the wiki (entity pages) or as a separate tracked CSV — defer until after first ingest

---

## Done log

| Date | What | Why it mattered |
|------|------|-----------------|
| 2026-05-06 | Workspace scaffolded (HEAVY mode) | Reader's primary research hub for Bambu Labs printer purchase + design + store ops; populated before handoff |
| 2026-05-06 | `prompts/github-repo-eval.md` shipped | Reusable Phase-0 audit prompt for GitHub-repo evaluation; unblocks user dropping browser-tab links |
| 2026-05-06 | Lint + preingest scripts ported | `wiki_lint.py` / `wiki_gap_detect.py` / `preingest_check.py` ported in (lint scripts are domain-agnostic; preingest's arXiv/DOI/URL/sha256/filename/title dedup signals all apply since the inbox is heavily academic). Smoke-tested: 59 NEW verdicts on the inbox, arXiv IDs and DOIs correctly extracted. Ingest workflow now unblocked. |
| 2026-05-06 | Ingest pass 1 — 5-paper print-quality control cluster | First real ingest. 5 source pages + 5 concept pages. Cluster: input shaping (Aung 2025), camera-based extrusion optimization (Lin 2025 / ETH Zurich), acoustic-CNN fault detection (Waheed 2023), closed-loop FCP+LQR (Hoteit 2025 / ETH Zurich), multimodal sensor fusion (Waheed 2025). Lint clean: 0 orphans / 0 asymmetric / 0 dangling. PDFs moved to `raw-sources/` with slug-renames. Inbox down to 54. |
| 2026-05-06 | Deep-read pass — 4 of 5 first-cluster papers | Caught 4 corrections that the first-2-pages skim missed: Aung's "RLS" abstract claim doesn't match Algorithm 1's response-feature method; Waheed 2023's "three failure modes" is framing, not what the metrics measure (binary with/without-material only); Waheed 2025's accelerometer "did not yield significant results" and fused 90-95% is *expected* not *measured*; Hoteit's research-grade hardware (5-axis, ROS2/Duet/Kalman) added with not-consumer caveat. 4 source pages + 2 concept pages updated. Lin paper deep-read deferred — `pdftoppm` not installed. |
| 2026-05-06 | Ingest pass 2 — 4-paper security side-channel cluster | 4 source + 3 concept pages = 7 within schema bound. Asgar 2026 (QuietPrint / first SHM defense), Chattopadhyay 2025 CCS (ResNet-50+LSTM optical attack from IP-cam video → functional counterfeit key), Jamarani 2025 (smartphone acoustic+magnetic GBDT, 98.80%/4.47% MTE), Dolgavin 2025 (first industrial PBF side-channel; Differential Voxelization on Sintratec S2; 90.29% TP voxel volume; "encryption is futile" against MATE). Concept hubs: side-channel-attacks (six modalities + threat tiers), ip-theft-3d-printing (Tier 1 Etsy seller / Tier 2 commercial / Tier 3 industrial MATE), g-code-protection (defense coverage matrix). pypdf workaround validated for missing-poppler-utils. fdm-printing hub updated with security backlinks. Inbox 54 → 50. |
| 2026-05-06 | Deep-read pass — Lin 2025 (final 1 of 5 first-cluster paper) | First-2-pages skim missed substantive errors caught on deep-read: (1) author names were wrong — actual authors are Yufan Lin / Xavier Guidetti / Yannick Nagel (not Yi-An / Riccardo / Luca); (2) hardware is Ender-3 V2 with 0.4mm nozzle and Fillamentum PLA, not generic Bambu/Prusa/Voron — the latter is now [TENTATIVE]; (3) framework uses TWO calibration prints (extrusion-dynamics ID + cornering ID), not one photo; (4) speed range is 1600→3600 mm/min ≈ 27→60 mm/s on a budget printer — well below Bambu's 200-500 mm/s cruise, so contribution is *technique generalization* not Bambu-tier speed; (5) snippet quote was a paraphrase passed off as verbatim — replaced with actual abstract + contributions verbatims. high-speed-fdm.md updated to add the speed-context qualifier. First-cluster deep-read pass now 5 of 5 complete. |
| 2026-05-06 | Ingest pass 3 — 4-paper print-farm / production-economics cluster | 4 source + 3 concept pages = 7 within schema bound. Wang 2025 (collaborative parameter recommender, ALS+spectral clustering on 10-printer farm), Ivkic 2025 (Cloud Crafting Platform on Azure SOA, 3-printer testbed via OctoPi RPis, €2.12-€2.24/ring at 400-600% margin, 40/30/20/10% profit share), Surynek+Prusa Research 2025 (SEQ-PACK+S formal problem; Z3 + CEGAR refinement; ships in PrusaSlicer 2.9.1), Hatton 2026 (Parallelobox AABB height-field decomposition; dominates Symmetry Slicer and matches/beats Cube Skeleton on complex geometry). Concept hubs: print-farm-operations (per-machine variability + scheduling + MaaS productization+security), print-job-scheduling (sequential vs parallel; multi-color purge math), am-as-a-service (economics deep-dive + distribution-channel comparison + explicit cross-link to security cluster's threat model). pypdf workaround used again. Inbox 50 → 46; raw-sources 9 → 13; wiki 17 → 24 pages. Lint clean: 0 orphans / 0 asymmetric / 0 dangling. |
| 2026-05-06 | Ingest pass 4 — Bambu materials baseline cluster (vendor-doc, no PDF inbox) | External-source ingest via Exa MCP — pulled Bambu Lab's two canonical filament-reference pages (`bambulab.com/en-us/filament/guide` + `wiki.bambulab.com/en/general/filament-guide-material-table`). Closes the materials gap that was the highest-friction day-1 question for reader's Bambu purchase. 1 source page (Bambu vendor doc, `maturity: validated` first-party data, single-source caveat noted) + 1 concept hub (`filaments-baseline.md` — decision matrix + mechanical/process tables + 4 cross-cutting hardware-compat rules: enclosure / drying / AMS-lite / hardened-nozzle) + 5 materials entity pages (PLA / PETG / ABS / ASA / TPU) = 7 pages within schema bound. Key insight surfaced: A1/A1 mini hobbyists are double-disqualified for ABS (no enclosure + AMS lite). PETG positioned as the practical default for functional parts on open-frame Bambu. Lint clean: 24 → 31 pages, 146 → 202 outbound edges. |
| 2026-05-07 | Ingest pass 5 — 3-paper VLM-in-manufacturing cluster (sensing / manipulation / control) | First AI-design cluster. 3 source pages + 1 concept hub = 4 within schema bound. Mahjourian + Nguyen 2026 ASME (VLM-IRIS — CLIP ViT-B/32 + magma colormap + centroid prompt ensembling; 100% zero-shot IR build-plate object presence on Prusa MK3S, no retraining). Chen + Guo 2025 (τ schema — 8-field knowledge primitive ⟨obj, iface, pre, contact, prim, traj, tol, dyn⟩ injected into GPT-4o prompts; spool-removal case study; 35→89% contact/tolerance specificity). Margadji + Pattinson 2025 Cambridge (CIPHER — VLA with Llama-3.2 + ResNet-152 process expert + LoRA + RAG; 5× MAE reduction 82.92→17.62 on flow-rate regression from endoscope images). Concept hub `vlm-in-manufacturing.md` synthesizes around three orthogonal angles. Cross-links: fdm-printing + fault-detection + extrusion-control + petg (VLM-IRIS used PETG parts). Practical translation for reader: structured prompts beat freeform when using chat VLMs; never trust VLM-generated numeric parameters. CIPHER pages 13+ deep-read deferred. Lint clean: 31 → 35 pages, 202 → 228 outbound edges. |
| 2026-05-07 | Ingest pass 6 — 25-repo Bambu toolchain audit (full ingest, not trimmed) | Sixth ingest pass. 1 source + 3 entities + 2 concepts = 6 within schema bound. Source: `2026-bambu-toolchain-audit.md` (Gemini-DR-style audit, ~40k chars). 25-repo verdict: 2 GO + 1 CONDITIONAL-GO + 22 NO-GO across 4 rejection patterns (firmware retrofits / scratch-build hardware / abandoned slicers / queue-managers needing USB-serial). New entity pages: `bambu-studio.md` (GO; mandatory native; AMS+3MF+MakerWorld+lidar; LAN-only fallback), `orcaslicer.md` (CONDITIONAL-GO; advanced calibration only; profile-schema-divergence warning), `kickstarter-autodesk-fdm-protocol.md` (GO; FDM Test V4 static `.stl`; Apache-2.0). New concept hubs: `bambu-ecosystem-closed-loop.md` (closed-firmware-as-feature thesis; the four NO-GO patterns formalized), `ai-design-tools.md` (Meshy/RodinAI/3DAIStudio → 3MF → Bambu Studio → AMS pipeline; decorative-only restriction; hallucinated-G-code prohibition). Audit's specific bug claims tagged [TENTATIVE 2026-05-07] (1500°C Bambu Studio preset, OrcaSlicer 2.3.1 flow calibration, hallucinated commit SHAs) — Reddit/forum-sourced, needs primary verification. Closes empty Slicers and AI-design-tools sections of wiki. Lint clean: 35 → 41 pages, 228 → 274 outbound edges. Inbox 43 → 42; raw-sources 16 → 17. |
| 2026-05-23 | Ingest pass 7 — shape-changing / 4D FDM cluster (4 papers) | Cluster A from inbox triage. 4 source + 1 concept = 5 pages. DuoMorph, FluxLab (SLA, not FFF), Iqbal PvP, NAT-LCE stub. Hub: `shape-changing-fdm-interfaces.md`. Inbox 42 → 38. |
| 2026-05-23 | Ingest pass 8 — TinkerXR + novice CAD workflows | Beginner handoff path (not print-farm). 1 source + 1 concept; `FRIEND-SETUP.md` week-2 Tinkercad pointer. Inbox 38 → 37. |

---

## Backlog

**Higher priority — next ingest passes:**

- Pick next cluster from remaining 43 PDFs. Candidates: volumetric / neuromorphic AM (likely background-only); robotics / soft-robotics cluster (Berkeley Humanoid Lite, MEVITA, MEVIUS, tendon-actuated robots, eFlesh, M3D-skin) — adjacent to reader's Etsy product but not core; smart-fabric / shape-changing cluster (DuoMorph, FluxLab, single-material 4D-printed); a `process-parameter-tuning` concept page (pressure advance / linear advance / Klipper auto-calibration) referenced from `print-farm-operations.md` but not yet written.
- CIPHER pages 13+ deferred deep-read — methods + extended figures (out-of-distribution validation; end-to-end autonomous fabrication demo). Pages 1-12 deep-read 2026-05-07 covers headline metric + ablation. Revisit if a question arises about VLA out-of-distribution behavior.
- Tier-2 sweep target: VLM-in-manufacturing **failure-mode** papers — current cluster is all successful demos; production-deployment failure analysis would round it out (called out as missing in `vlm-in-manufacturing.md`).
- Bambu-specific entity pages (X1C / P1S / A1 / A1 mini) once reader chooses model — completes the printer-vs-material compatibility hop that materials cluster currently leaves at the table-row level.
- Lin 2025 pages 16-32 deferred deep-read — full-part validation results (specific test geometries, surface-roughness numbers, photographs). Pages 1-15 deep-read 2026-05-06 covers method + headline metric. Revisit only if a question arises.

**Lower priority:**

- Reader handoff: README + first-run walkthrough + `.env` setup walk-through (do this only after ingest is well underway and core entity/concept pages exist)
- Extract `wiki-template/` skeleton from this scaffolding (so the next domain wiki — fitness? home automation? — can spin up faster)
