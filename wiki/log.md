# Wiki Log

Append-only chronological operations log. Each entry: date + operation + summary + pages touched.

---

## [2026-05-20] cross-printer expansion | Flashforge Adventurer 5M entity + friend day-1 brief

User's friend just got a Flashforge Adventurer 5M (his first 3D printer) and will set up the wiki this weekend. He has never used AI before. Two deliverables: (1) an entity page for the non-Bambu printer so the friend has a single read that says which wiki advice applies to his machine; (2) a paste-friendly brief covering AI + Obsidian setup, sourced from CCC wiki.

### Created (2 pages)

- `wiki/entities/printers/flashforge-adventurer-5m.md` — non-Bambu CoreXY; 220×220×220 mm, 600mm/s, 280°C, Orca-Flashforge slicer, **ships Klipper firmware** which inverts the closed-firmware-as-feature thesis; 5M (open-frame, ~$300-400) vs 5M Pro (enclosed + camera + HEPA, ~$500-600). Applies/does-not-apply table for which wiki sections transfer. Day-1 setup priorities (stock-firmware-first, do NOT install xblax Klipper mod or Bambu Studio). [CONFIRMED via Flashforge product page + retailer listing + community Klipper-mod GitHub repo, retrieved 2026-05-20].
- `briefs/2026-05-20_friend-day1-ai-obsidian-setup.md` — friend-facing brief (paste into claude.ai OR follow standalone). Steps: (0) why AI at all; (1) install Obsidian + recommended plugins; (2) Claude.ai web account + structured-prompt template + numeric-hallucination warning + hallucinated-G-code prohibition; (3) paste-then-ask workflow with the wiki; (4) optional Claude Code CLI install (week 2+); (5) first-week wiki reading order; (6) escalation path. Sources from this wiki (Flashforge entity, Obsidian entity, vlm-in-manufacturing, ai-design-tools, filaments-baseline) + CCC wiki (claude-code, claude-desktop-vs-claude-code, token-economics, context-engineering, claude-obsidian DO-NOT-ADOPT note).

### Updated (1 page)

- `wiki/index.md` — Printers section gets Flashforge Adventurer 5M row beneath the Bambu A1 entry, with non-Bambu / Klipper caveat in the summary.

### Notes

- Brief lives in `briefs/` (gitignored) as a one-off deliverable; not indexed in `wiki/index.md`.
- Flashforge entity page is `maturity: draft` — only one external verification pass (Brave search → vendor + retailer + community-mod GitHub); specific pricing and AMS-equivalent accessory lineup tagged [TENTATIVE 2026-05-20].
- CCC wiki cross-references (`@ccc-wiki/...`) in the brief are bibliographic — friend may or may not have a synced copy; brief is self-contained without them.
- No raw source moved to `raw-sources/` (no PDF/docx ingested — this was a friend-facing expansion, not a new-source ingest).

---

## [2026-05-07] ingest | 25-repo Bambu toolchain audit (Phase-0 source audit)

Sixth ingest pass — full ingest of `GitHub Repo Audit for 3D Printing.docx` (Gemini-DR-style audit of 25 GitHub repos for laptop-only Bambu workspace). Substance preserved fully rather than trimmed to GO repos only. 6 wiki pages = within schema bound (3-15).

### Created (6 pages)

- `sources/2026-bambu-toolchain-audit.md` — full source page; 25-repo verdict structure (2 GO / 1 CONDITIONAL-GO / 22 NO-GO); 4 verbatim Snippets; Dead Ends section listing all 22 NO-GO repos with rejection rationales; specific [TENTATIVE 2026-05-07] flags on bug claims (1500°C preset, OrcaSlicer 2.3.1 flow calibration, hallucinated commit SHAs)
- `entities/slicers/bambu-studio.md` — GO-tier; AGPL-3.0 PrusaSlicer fork; AMS / 3MF / lidar / MakerWorld integration; LAN-only fallback for cloud resilience
- `entities/slicers/orcaslicer.md` — CONDITIONAL-GO; isolate to advanced material calibration only; profile schema divergence as daily driver; written-down-values workflow recommended over profile-copying
- `entities/tools/kickstarter-autodesk-fdm-protocol.md` — GO-tier; FDM Test V4 calibration print (`ksr_fdmtest_v4.stl`); Apache-2.0; 8-year staleness doesn't matter (static `.stl` design)
- `concepts/bambu-ecosystem-closed-loop.md` — concept hub formalizing closed-firmware-as-feature thesis; the four NO-GO patterns (firmware retrofits / scratch-build hardware repos / abandoned slicers / queue-managers requiring USB-serial); the lidar/motor-resonance/vision/AMS edge-AI features that depend on closed firmware
- `concepts/ai-design-tools.md` — concept hub for Meshy/RodinAI/3DAIStudio → 3MF → Bambu Studio → AMS pipeline; decorative-only restriction (functional/load-bearing parts must use traditional CAD); hallucinated-G-code prohibition (physical-damage risk); manifold-geometry check before slicing

### Updated (8 existing pages — backlinks)

- `concepts/fdm-printing.md` — +6 edges (1 source + 3 entities + 2 concepts)
- `concepts/print-farm-operations.md` — +2 (bambu-ecosystem-closed-loop, ai-design-tools)
- `concepts/vlm-in-manufacturing.md` — +1 (ai-design-tools — analytical/generative pair)
- `concepts/am-as-a-service.md` — +1 (ai-design-tools — content-pipeline tie)
- `concepts/extrusion-control.md` — +2 (orcaslicer, kickstarter-autodesk-fdm-protocol)
- `concepts/filaments-baseline.md` — +1 (kickstarter-autodesk-fdm-protocol — calibration companion)
- `wiki/index.md` — populated empty Slicers section (Bambu Studio + OrcaSlicer); new Tools section (Kickstarter Autodesk FDM Test V4); AI design tools section points at concept hub (deferring per-platform entities until reader selects); +1 source row + 2 concept rows

### Lint

- Lint clean: 35 → **41 pages**, 228 → **274 outbound edges**
- Zero orphans, zero bidirectional gaps, zero dangling, zero missing-page mentions

### Reader impact (the why)

Closes the slicer + AI-design-tools sections of the wiki that were empty before this ingest — now answers "what slicer do I install?" and "is Meshy / RodinAI / 3DAIStudio safe to use?" with primary-source-backed concept hubs. Pre-bakes the day-1 toolchain decision so reader doesn't fall into the Klipper-on-Bambu / OctoPrint-on-Bambu rabbit holes that dominate online forum recommendations.

### Audit trustworthiness caveats

The audit's structural recommendations are sound (don't flash Klipper, don't run OctoPrint, do use Bambu Studio + Kickstarter calibration + OrcaSlicer-for-tuning). But specific bug version-pins (Bambu Studio 1500°C preset, OrcaSlicer 2.3.1 flow calibration) and any commit SHAs are tagged [TENTATIVE 2026-05-07] — they're sourced from Reddit/forum citations, not primary verification, and should be cross-checked before becoming canonical.

### Inbox / raw-sources

- `research to be indexed/`: 43 → **42** (audit docx moved to raw-sources)
- `raw-sources/`: 16 → **17** PDFs/docx

---

## [2026-05-06] init | workspace scaffolded

Workspace scaffolded HEAVY-mode (adapted from a sibling research-librarian workspace). Empty wiki ready for first ingest pass.

### Created

- `CLAUDE.md` — schema (domain-rewritten for 3D printing)
- `.gitignore` — adapted from sibling-workspace pattern
- `.env.example` — DEEPSEEK_API_KEY / BRAVE_API_KEY / EXA_API_KEY placeholders (no real keys)
- `.claude/settings.local.json` — minimal allowlist (Brave, Exa, Context7, Playwright, stash-librarian)
- `ROADMAP.md`, `LESSONS.md`, `hot.md` skeletons
- `wiki/index.md`, `wiki/log.md` skeletons
- Empty folders: `wiki/{sources,entities,concepts}/`, `scripts/`, `briefs/`, `research to be indexed/`, `raw-sources/`

### Pending

- First ingest pass on the 40+ docs user dropped today (waiting on script adaptation)
- Port + genericize lint scripts from sibling research workspace

---

## [2026-05-06] artifact | github-repo-eval prompt shipped

`prompts/github-repo-eval.md` created. Reusable Phase-0 audit prompt template for GitHub-repo evaluation, adapted from the Phase-0 audit pattern in `CLAUDE.md`. Tool-class-specific failure-mode checks for AI design tools, slicer plugins, modeling libs, print-farm tools, marketplace tools, and firmware mods. Output format includes a draft entity-page block ready to drop into `wiki/entities/tools/<slug>.md`. Unblocks user dropping the GitHub URLs sitting in browser tabs.

### Created

- `prompts/github-repo-eval.md` — the prompt template + usage notes
- `prompts/` folder (added to CLAUDE.md folder layout)

### Updated

- `CLAUDE.md` — folder layout now lists `prompts/`
- `ROADMAP.md` — W1 status reflects 40+ docs dropped; `github-repo-eval` removed from backlog and added to done log
- `hot.md` will be updated at session end

---

## [2026-05-06] tooling | lint + preingest scripts ported

`scripts/wiki_lint.py`, `scripts/wiki_gap_detect.py`, `scripts/preingest_check.py` ported from a sibling research workspace. Lint scripts are domain-agnostic — they validate the wiki schema (frontmatter, bidirectional `related:`, `[NEEDS VERIFICATION]` freshness, narrative word count) which is identical regardless of subject domain. Only docstring tweak: dropped the source-workspace reference in `wiki_lint.py`.

Preingest dedup signals (sha256 / arXiv / DOI / URL / filename / title) all apply unchanged. Earlier ROADMAP claim that 3D-printing source mix wouldn't need arXiv/DOI was wrong — the actual inbox is ~58 academic papers. Smoke test on the 62-file inbox: 59 NEW verdicts, arXiv IDs and DOIs correctly extracted from PDF first pages.

Ingest workflow now unblocked.

### Created

- `scripts/preingest_check.py` (verbatim copy)
- `scripts/wiki_lint.py` (one docstring line tweaked)
- `scripts/wiki_gap_detect.py` (verbatim copy)

### Removed

- `scripts/.gitkeep` (no longer needed)

### Updated

- `ROADMAP.md` — W1 status updated (62 docs, scripts ported, ingest unblocked); done log entry added; backlog "higher priority" item removed

---

## [2026-05-06] ingest | 5-paper FDM control / fault-detection starter cluster

First real ingest pass. Cluster theme: print-quality control on consumer-grade FDM — input shaping (vibration), extrusion control (corner / speed-transition errors), fault detection (acoustic / multimodal), high-speed regime. Picked these 5 from the 59-PDF inbox because (a) they're directly relevant to a reader buying a Bambu, (b) they collectively define the four open problems and their research trajectory, (c) they cross-reference cleanly into a connected cluster rather than a star around one hub.

5 source pages + 5 concept pages = 10 pages touched. Within the 3-15 schema bound.

### Created

- `wiki/sources/2025-aung-adaptive-input-shaper.md` — adaptive TDF input shaper with RLS parameter estimation
- `wiki/sources/2025-lin-camera-extrusion-optimization.md` — smartphone-photo G-code optimization for high-speed FFF
- `wiki/sources/2023-waheed-acoustic-cnn-fault-detection.md` — CNN + acoustic spectrogram for nozzle clog / filament breakage / pulley skip
- `wiki/sources/2025-hoteit-closed-loop-extrusion-lqr.md` — LQR over Force-Controlled Printing; 39.57% RMS reduction
- `wiki/sources/2025-waheed-multimodal-sensor-fusion.md` — acoustic + vibration + thermal sensor-fusion fault classifier
- `wiki/concepts/fdm-printing.md` — hub page synthesizing all 4 open problems
- `wiki/concepts/input-shaping.md` — feedforward vibration suppression
- `wiki/concepts/extrusion-control.md` — three mitigation classes (pressure advance / camera-based / closed-loop FCP)
- `wiki/concepts/fault-detection.md` — acoustic → multimodal trajectory
- `wiki/concepts/high-speed-fdm.md` — regime shift from positioning-bound to dynamic-mismatch-bound

### Updated

- `wiki/index.md` — populated Sources and Concepts sections (Entities still empty pending Bambu model selection)

### Raw sources moved

5 PDFs renamed to slug match and moved from `research to be indexed/` to `raw-sources/`. Inbox down to ~54 PDFs.

### Pending

- Run `python3 scripts/wiki_lint.py` to verify bidirectional cross-links
- Update ROADMAP.md (W1 advances; ingest pass 1 of N done)
- Continue ingesting next cluster from remaining 54 PDFs

---

## [2026-05-06] deep-read | 4 of 5 first-cluster papers

Deep-read pass on the 5-paper print-quality control cluster ingested earlier today (originally first-2-pages skimmed). Read 4 of 5 fully via Read tool's text-extraction path. Lin paper deep-read deferred — `pdftoppm` / poppler not installed locally, blocking the `pages` parameter on a 32-page 33MB PDF.

### Corrections found and applied

- **Aung 2025**: abstract advertises RLS for parameter estimation, but Algorithm 1 (§III) actually uses response-feature formulas (Mp, Ts, peak time) with closed-form Weierstrass substitution (undamped) and numerical solution (damped). Discrepancy flagged [TENTATIVE]. Added GitHub link (https://github.com/NyiNyi-14/A-TDF.git), simulation parameter ranges (ζ ∈ [0,1], ωn ∈ [π, 3000π]), explicit simulation-only caveat, future-work regression-model note.
- **Waheed 2023**: paper claims three failure modes (clog / breakage / pulley skip) but the experiment as run only contrasts with-material vs without-material — binary, not three-way. Now flagged [TENTATIVE]. Added metrics (91%/88%/85%/86.5%), hardware (Makerbot Method X, SparkFun MEMS mic, ABS), bandpass 100-1200 Hz, dataset size (256 samples 80/20).
- **Hoteit 2025**: added research-grade hardware (5-axis gantry, ROS2 supervisor, Duet motion board, Kalman state estimator), 3rd-order N4SID model, Q/R/K_LQR weights, builds-on-Guidetti-2024-FCP. Flagged simulation 69.81% vs experiment 39.57% RMSE gap as evidence of unmodeled dynamics. Strengthened not-consumer-hardware caveat.
- **Waheed 2025**: critical correction — the accelerometer channel "did not yield significant results" on the static-extrusion test bench, and the headline fused-accuracy 90-95% is *expected* (projected from per-modality performance) not *measured*. The "fused outperforms" claim flagged [TENTATIVE]. Added Google Teachable Machine + Raspberry Pi PCB hardware notes, two-configuration (Acoustic Baseline / Hybrid Fusion) framing.

### Updated

- 4 source pages: read-status `skimmed` → `deep-read`; narrative rewritten with corrections; +1 snippet on Aung and Waheed-2025
- `wiki/concepts/fault-detection.md`: added [TENTATIVE] caveats to bullets 1 (acoustic) and 2 (multimodal fusion) reflecting experiments-vs-framing gap
- `wiki/concepts/input-shaping.md`: strengthened [TENTATIVE] block with GitHub link and regression-model future-work note

### Pending

- **Lin 2025 deep-read deferred**: 32-page PDF, Read tool's `pages` parameter requires `pdftoppm` (poppler-utils) which isn't installed; revisit via `pypdf 6.10.2` text extraction on a future session. Lin source page narrative still accurate based on first-2-pages content from initial ingest.
- Run `python3 scripts/wiki_lint.py` to verify bidirectional cross-links
- Update ROADMAP.md done log + remove deep-read item from backlog
- Pick next cluster from remaining 54 PDFs

---

## [2026-05-06] ingest | 4-paper security side-channel cluster

Second ingest pass, security cluster — IP-theft / side-channel attacks on 3D printers and defenses. Picked these 4 from the remaining 54 PDFs because (a) they collectively define the attack surface (acoustic / optical / magnetic / power across FDM and PBF), (b) one of them is the first-ever published software-only defense (Asgar 2026 / SHM), (c) Tier 2 commercial-design IP theft is directly relevant if the reader ends up selling proprietary geometry on Etsy / MakerWorld. Used `pypdf` via Bash to extract first 10 pages of each PDF to `/tmp/3dp-security/*.txt` (workaround for missing poppler-utils on laptop).

4 source pages + 3 concept pages = 7 pages touched. Within the 3-15 schema bound.

### Created

- `wiki/sources/2026-asgar-quietprint-acoustic-defense.md` — Stealth Head Movement: convex-hull G-code rewriter, Procrustes dissimilarity optimization, ~55% print-time overhead, software-only defense. First-ever published software defense against acoustic side-channels.
- `wiki/sources/2025-chattopadhyay-one-video-optical.md` — ResNet-50 + LSTM recovers printable G-code from IP-camera video; 90.87% similarity; Oriented Bounding Polygon + Subsequence-Aligned DTW for rotation/translation invariance; functional counterfeit padlock key + gear printed from recovered G-code; Geeetech A20T → Ultimaker cross-printer transfer.
- `wiki/sources/2025-jamarani-acoustic-magnetic-decoding.md` — smartphone (Galaxy S22+) acoustic + magnetic dual-channel attack on LULZBOT TAZ; GBDT classifier; MFCC features; 98.80% accuracy / 4.47% MTE; non-intrusive at "greater distances" than prior work.
- `wiki/sources/2025-dolgavin-hearsay-pbf-power.md` — first side-channel attack on industrial PBF (Sintratec S2); 11-probe instrumentation (Fluke i310 current clamps + galvanometer voltage taps + NI USB-6363 DAQ at 20 kHz); Differential Voxelization (DPA-inspired) + voxel pruning + gap filling; 90.29% TP / 7.02% FP / 9.71% FN voxel volume on Gear; "encryption is futile" against MATE threat.
- `wiki/concepts/side-channel-attacks.md` — hub page: six modalities (acoustic / optical / magnetic / power / vibration / thermal), threat-tier continuum (compromised IP-cam → smartphone → planted recorder → MATE), defense classes summary.
- `wiki/concepts/ip-theft-3d-printing.md` — three threat tiers (Tier 1 hobbyist Etsy seller; Tier 2 commercial-designer with proprietary geometry; Tier 3 industrial outsourced AM / MATE). Bambu-specific guidance for the reader's use case.
- `wiki/concepts/g-code-protection.md` — defense-class inventory: file-level (encryption / streaming / TPM / blockchain) vs physical-level (SHM / acoustic masking / dummy commands) plus operational controls (LAN-only mode, camera-off, isolation). Coverage matrix shows no single defense covers all attack surfaces.

### Updated

- `wiki/concepts/fdm-printing.md` — added 3 concept + 3 source backlinks (omitting Dolgavin which is industrial PBF, not FDM). Frontmatter `related:` and inline `## Relations` both updated.
- `wiki/index.md` — 4 new Source rows + 3 new Concept rows.

### Raw sources moved

4 PDFs renamed to slug match and moved from `research to be indexed/` to `raw-sources/`. Inbox down from 54 to 50.

### Methodology note — pypdf workaround

Read tool's `pages` parameter requires `pdftoppm` (poppler-utils). Not installed on laptop. Bypass: `pypdf 6.10.2` is installed; ran `python3 -c "from pypdf import PdfReader; ..."` per PDF, sliced first 10 pages, wrote to `/tmp/3dp-security/<slug>.txt`, then Read those text files. Equivalent to deep-read for pages 1-10. Pages 11+ on the longer PDFs (Decoding IP 22 pages, Hearsay 18 pages, One Video 17 pages) still skim-only — should be fine, since methodology + headline metrics are all in the first 10 pages.

This same workaround unblocks the still-pending Lin 2025 deep-read.

### Pending

- Run `python3 scripts/wiki_lint.py` to verify bidirectional cross-links + read_status frontmatter
- Update ROADMAP.md done log + status line
- Pick next cluster from remaining 50 PDFs (candidates: AI-design / VLM-for-manufacturing, Bambu-specific entity pages once reader chooses model)

---

## [2026-05-06] deep-read | Lin 2025 (one-shot camera-based extrusion optimization)

Long-pending Lin 2025 deep-read — was deferred from first ingest pass on 2026-05-06 because the Read tool's `pages:` parameter requires poppler-utils / `pdftoppm`, which isn't installed on the laptop. With the `pypdf 6.10.2` workaround validated on the security cluster earlier today, ran it on Lin 2025 (32 pages → first 15 to `/tmp/3dp-lin/page-NN.txt`) and reviewed.

**Findings — first 2-pages skim missed substantive errors:**

1. **Author names were wrong.** First-pass page used "Yi-An Lin, Riccardo Guidetti, Luca Nagel" — actual authors per p.1 are **Yufan Lin, Xavier Guidetti, Yannick Nagel**, with Efe C. Balta and John Lygeros correct. Affiliations stand (ETH Zurich Automatic Control Lab + Inspire AG + NematX AG). Email addresses confirm: yuflin@student.ethz.ch, xaguidetti@control.ee.ethz.ch, yannick.nagel@nematx.com.
2. **Hardware was Ender-3 V2, not Bambu/Prusa/Voron.** First-pass narrative implied broad applicability to consumer fast printers. The actual experiment is on a budget Ender-3 V2 with a 0.4 mm nozzle, light-ivory PLA from Fillamentum, layer height 0.2 mm, bed 75 °C, nozzle 200 °C [p.6]. Bambu/Prusa/Voron generality is *plausible* but **not validated** — re-tagged [TENTATIVE] with [NEEDS VERIFICATION 2026-05-06].
3. **The framework uses TWO calibration prints, not one photo.** "One-shot" terminology refers to one identification iteration without firmware flashing, not a single photo. Print 1 = step-reference width pattern (extrusion dynamics ID, with separate τ_expand and τ_shrink time constants). Print 2 = four-corner high-speed pattern (cornering parameter ID for v_m^c and a). Then optimize G-code via QP and emit a third (production) print [p.6, p.9, p.13].
4. **Speed range needs context.** Headline "effectively doubling production speed" maps to **3600 mm/min ≈ 60 mm/s** matched against **1600 mm/min ≈ 26.7 mm/s** baseline on the Ender-3 V2. Bambu printers cruise at 200–500 mm/s (12 000–30 000 mm/min), so Lin's framework is *technique-generalization* (free post-process speed-up on a slow printer), not a Bambu-tier speed contribution.
5. **Snippet quote was a paraphrase, not a verbatim.** The page had: *"We propose a one-shot, camera-based extrusion optimization framework for high-speed Fused Filament Fabrication (FFF). A single smartphone image of a calibration print is sufficient..."* — this does **not** appear in the abstract or anywhere in pages 1-15. Replaced with actual verbatim from p.1 abstract and p.4 contributions list.

### Updated

- `wiki/sources/2025-lin-camera-extrusion-optimization.md` — full rewrite. Authors fixed; hardware corrected to Ender-3 V2; pipeline expanded to four-step description with proper citations; Bambu/Prusa/Voron generality re-tagged [TENTATIVE]; fabricated snippet replaced with two real verbatims (abstract + contributions) plus one supporting open-loop-limitations quote; `read_status` upgraded `skimmed` → `deep-read`.
- `wiki/concepts/high-speed-fdm.md` — corrected fabricated Lin snippet to actual abstract verbatim; added qualifier that Lin's Ender-3 V2 max (60 mm/s) and Hoteit's 5-axis research-grade hardware are below Bambu cruise speed — these papers contribute *technique generalization* rather than absolute-speed records.
- `wiki/index.md` — Lin row updated: "single-photo G-code rewrite" → "two calibration prints + phone camera → optimized G-code; 2× quality-equivalent speed on Ender-3 V2 (1600→3600 mm/min)".

### Pages not extracted (pages 16-32)

Pages 16-32 contain full-part validation results (specific test geometries, surface-roughness numbers, photographs of printed parts). Headline metric and methodology are fully captured in pages 1-15; further deep-read deferred unless a specific question arises.

### Inbox

Unchanged — Lin 2025 was already in `raw-sources/` from first ingest pass; this was a deep-read correction pass, not a new ingest.

### Lint

Clean: 0 orphans / 0 bidirectional gaps / 0 dangling / 0 missing-pages / frontmatter quality clean (17 pages, 92 outbound edges).

---

## [2026-05-06] ingest | 4-paper print-farm / production-economics cluster

Third ingest pass — print-farm operations + production economics. Cluster theme: what changes when you go from one printer to many, and the economic model around productizing a print fleet as a service. Picked these 4 from the remaining 50 PDFs because (a) they collectively define the multi-printer regime (per-machine tuning + scheduling sequential-vs-parallel + MaaS productization), (b) the MaaS architecture papers cross-link cleanly into the security cluster's threat model — Tier-2/Tier-3 attacks apply directly to cloud-distributed G-code, (c) sequential printing on a single printer is the highest-leverage scheduling technique for the reader's Etsy-batch use case (failure robustness + multi-color purge savings) before they ever own a second printer. Used `pypdf` workaround again for first 10-12 pages of each PDF.

4 source pages + 3 concept pages = 7 pages touched. Within the 3-15 schema bound.

### Created

- `wiki/sources/2025-wang-collaborative-parameter-recommender.md` — sequential matrix completion (ALS + spectral clustering + ridge regression) on a 10-printer FDM mini-farm; references industry-scale Prusa 600 / JinQi 2500 / Slant3D 800 fleets; significantly faster convergence than independent per-machine optimization.
- `wiki/sources/2025-ivkic-cost-benefit-maas.md` — Cloud Crafting Platform on Microsoft Azure SOA; testbed of 3 printers behind OctoPi RPis (Ultimaker 2+ CONNECT, Creality K1 MAX, Prusa MK4); per-ring cost €2.121-€2.237 vs €10-15 market price = 400-600% margin; profit share 40 (platform) / 30 (printer operator) / 20 (web shop) / 10 (designer); security gap acknowledged but no defenses implemented.
- `wiki/sources/2025-surynek-sequential-printing-cegar.md` — SEQ-PACK+S formal problem (NP-hard reduction from rectangle packing); Z3 SMT solver + CEGAR-inspired refinement loads PolygonLines-not-Intersect constraints lazily; ships in PrusaSlicer 2.9.1 (github.com/surynek/cegar-seq); Z3 ≫ Gecode CSP, CEGAR-SEQ ≫ eager.
- `wiki/sources/2026-hatton-parallelobox-aabb-decomposition.md` — AABB height-field decomposition with k-means++ seeds + metaheuristic outer loop over printer count + clustering configs; dominates Symmetry Slicer, comparable-or-better than Cube Skeleton Segmented Shell on complex geometry; minutes-of-compute trade against hours of saved parallel-printing time; "Brain Left" MRI test geometry.
- `wiki/concepts/print-farm-operations.md` — hub page; three problem classes that emerge above one printer (per-machine variability + tuning, scheduling, MaaS productization+security); reader-trajectory table by fleet size.
- `wiki/concepts/print-job-scheduling.md` — sequential-on-one-printer vs parallel-across-many comparison; multi-color purge math (10 obj × 3 colors × 100 layers: 30 sequential vs 3000 slice-by-slice changes); reader-relevance table.
- `wiki/concepts/am-as-a-service.md` — economics deep-dive; comparison table of distribution channels (Etsy direct STL ~95% / MakerWorld hybrid TBD / MaaS 10% / industrial Shapeways/Hubs/Xometry); explicit security gap analysis showing Tier-2/Tier-3 attacks from ip-theft cluster apply directly to MaaS architecture.

### Updated

- `wiki/concepts/fdm-printing.md` — added 3 concept + 4 source backlinks (all 4 sources are FDM-applicable, unlike security cluster where Dolgavin was PBF-only). Frontmatter `related:` and inline `## Relations` both updated.
- `wiki/concepts/ip-theft-3d-printing.md` — added backlink to am-as-a-service + ivkic source + print-farm-operations.
- `wiki/concepts/g-code-protection.md` — added backlink to am-as-a-service + ivkic source.
- `wiki/index.md` — 4 new Source rows + 3 new Concept rows.

### Raw sources moved

4 PDFs renamed to slug match and moved from `research to be indexed/` to `raw-sources/`. Inbox down from 50 to 46. `raw-sources/` now holds 13 PDFs (5 first-cluster + 4 security + 4 print-farm).

### Cross-cluster integration

`am-as-a-service.md` explicitly cross-links to `ip-theft-3d-printing.md` and `g-code-protection.md`: the Ivkic Cloud Crafting architecture distributes G-code over the public cloud to remote SME printers, which is *exactly* the Tier-2 (malicious SME operator) and Tier-3 (insider MATE) threat model from the security cluster. Ivkic acknowledges security as non-functional but implements **none** of the SHM / TPM-attestation / chunked-STL defenses cataloged in `g-code-protection.md`.

### Lint

Clean: 0 orphans / 0 bidirectional gaps / 0 dangling / 0 missing-pages / frontmatter quality clean (24 pages, 146 outbound edges).

### Pending

- Update ROADMAP.md done log + status line (24 pages, ingest pass 3 of N done)
- Pick next cluster from remaining 46 PDFs

---

## [2026-05-06] ingest | Bambu materials baseline cluster (vendor-doc, no PDF inbox)

External-source ingest. Pulled Bambu Lab's two canonical filament-reference pages via Exa MCP — the comparison-table tool at `bambulab.com/en-us/filament/guide` and the wiki material-table at `wiki.bambulab.com/en/general/filament-guide-material-table`. No raw PDFs consumed from inbox; this fills the materials gap that was identified in pass 3 and is the single highest-friction gap on day 1 of reader owning a Bambu printer.

### Created

- `wiki/sources/2026-bambu-filament-guide.md` — vendor-doc source page; `maturity: validated` (first-party manufacturer data); flagged single-source with cross-validation deferred to Filabase / CNC Kitchen / My Tech Fun if a specific claim becomes load-bearing.
- `wiki/concepts/filaments-baseline.md` — concept hub. 30-second decision matrix + mechanical comparison table (PLA / PETG / PETG HF / ABS / ASA / TPU 95A HF) + process comparison table + 4 cross-cutting rules (enclosure / drying / AMS-lite / hardened-nozzle) + decision tree + "what's NOT covered" (PC, PA, fiber-reinforced, specialty PLA).
- `wiki/entities/materials/pla.md` — default filament. Covers Basic + Matte / Silk / Tough / PLA-CF / Marble / Wood / Sparkle / Glow / Aero variants. Storage and biodegradability caveats.
- `wiki/entities/materials/petg.md` — functional default. PETG vs PETG HF comparison (HDT 69 vs 87°C; HF requires drying; HF has worse Z layer adhesion). PETG-CF caveats. Bed-adhesion glue requirement.
- `wiki/entities/materials/abs.md` — engineering filament. **Enclosure-required hardware constraint** (X1/X1C/P1S only — A1/A1 mini double-disqualified by enclosure + AMS-lite). Acetone-smoothing. Annealing.
- `wiki/entities/materials/asa.md` — UV-stable variant of ABS. ASA-vs-ABS choice table (ASA wins almost every dimension except marginal impact-XY). Better AMS-lite story than ABS.
- `wiki/entities/materials/tpu.md` — flexible elastomer. Shore-hardness ladder (95A / 90A / 85A). TPU 95A HF only AMS-compatible (dedicated port; not on AMS lite). Drying required (1.08% water absorption — highest of baseline).

### Updated

- `wiki/concepts/fdm-printing.md` — added backlinks to filaments-baseline + 5 material entities + bambu-filament-guide source. Hub now points at the materials cluster.
- `wiki/index.md` — 1 new Source row + 1 new Concept row + 5 new Materials entity rows (under Entities > Materials, replacing the "no pages yet" placeholder).

### Raw sources moved

None (vendor-doc pages, captured via Exa crawl directly into source page snippets). `raw-sources/` unchanged at 13 PDFs.

### Cross-cluster integration

Materials cluster is upstream of every functional-print decision the reader will make on day 1. Decision matrix in `filaments-baseline.md` covers the printer-vs-material question (A1 / A1 mini are open-frame so ABS / ASA out of reach; PETG covers most of what hobbyists historically used ABS for). Cross-link to `concepts/fdm-printing.md` hub completes the entity-vs-process-vs-source triangle for materials.

### Lint

Clean: 0 orphans / 0 bidirectional gaps / 0 dangling / 0 missing-pages / frontmatter quality clean. **31 pages, 202 outbound edges** (up from 24 / 146 before this ingest).

### Pending

- Update ROADMAP.md done log + status line (31 pages, ingest pass 4 done)
- Update hot.md
- Future: Bambu printer entity pages (X1C / P1S / A1 / A1 mini) — would tie the printer-vs-material compatibility into a single hop

## [2026-05-07] ingest | 3-paper VLM-in-manufacturing cluster (sensing / manipulation / control)

User selected option 1 from next-options list — AI-design / VLM-for-manufacturing cluster. Three arXiv-tier papers in inbox covering orthogonal angles of foundation-model application to manufacturing, ingested as a unified cluster.

### New source pages

- `wiki/sources/2026-mahjourian-vlm-iris.md` — VLM-IRIS (Mahjourian + Nguyen, Michigan Tech, ASME 2026). CLIP ViT-B/32 + magma colormap preprocessing + centroid prompt ensembling for zero-shot object presence on Prusa MK3S build plate via FLIR Boson thermal IR. Best 100% accuracy (room temp + magma + centroid), 92% (hot bed). PETG parts. **No model retraining.**
- `wiki/sources/2025-chen-tau-schema-vlm.md` — τ schema (Chen + Guo, HKUST GZ, arXiv 2512.11275v1). 8-field τ tuple ⟨obj, iface, pre, contact, prim, traj, tol, dyn⟩ as knowledge primitive injected into VLM prompts. Case study: 3D-printer empty-spool removal by Airbot MMK2 dual-arm robot. Plan-quality only (no hardware execution). Headline: contact/tolerance specificity 35→89% with τ-anchoring (GPT-4o, N=10).
- `wiki/sources/2025-margadji-cipher.md` — CIPHER (Margadji + Pattinson, Cambridge, arXiv 2506.08462v1). Vision-Language-Action (VLA) framework: Llama-3.2 + ResNet-152 process expert + LoRA + RAG. Endoscope-on-printhead. 5× MAE reduction (82.92→17.62) on flow rate regression vs naive VLM fine-tune. 35 pages — first 12 deep-read; methods + extended figures deferred.

### New concept hub

- `wiki/concepts/vlm-in-manufacturing.md` — synthesizes the three papers around three orthogonal angles: **Sensing** (VLM-IRIS), **Manipulation** (τ-schema), **Control** (CIPHER). Establishes that bare-prompt VLMs are insufficient for engineering applications — each angle requires a load-bearing technique (modality bridging / schema anchoring / process expert hybrid). Practical translation for the reader: structured prompts beat freeform; never trust VLM-generated numeric parameters.

### Updated

- `wiki/concepts/fdm-printing.md` — added 4 backlinks (3 sources + new concept hub).
- `wiki/concepts/fault-detection.md` — added 3 backlinks (VLM-IRIS + CIPHER + concept hub). Both papers extend the fault-detection conversation toward language-model-grounded reasoning.
- `wiki/concepts/extrusion-control.md` — added 2 backlinks (CIPHER + concept hub). CIPHER's flow-rate regression is the same regression problem extrusion-control's force-feedback approaches solve from the control side.
- `wiki/entities/materials/petg.md` — added VLM-IRIS source backlink (the paper used PETG parts as test artifacts).
- `wiki/index.md` — 3 new Source rows + 1 new Concept row.

### Raw sources moved

- `research to be indexed/VISION–LANGUAGE MODELS FOR INFRARED INDUSTRIAL SENSING IN ADDITIVE MANUFACTURING SCENE DESCRIPTION.pdf` → `raw-sources/2026-mahjourian-vlm-iris.pdf`
- `research to be indexed/Towards Logic-Aware Manipulation- A Knowledge Primitive for VLM-Based Assistants in Smart Manufacturing.pdf` → `raw-sources/2025-chen-tau-schema-vlm.pdf`
- `research to be indexed/Hybrid Reasoning for Perception, Explanation, and Autonomous Action in Manufacturing.pdf` → `raw-sources/2025-margadji-cipher.pdf`

`raw-sources/` now at 16 PDFs.

### Cross-cluster integration

Anchors a new vertical: foundation-model AI applied to FDM. Adjacent to the existing fault-detection cluster (CIPHER's process expert is what fault-detection's classifiers will look like in 3-5 years) and the extrusion-control cluster (CIPHER directly addresses flow-rate regression). The reader's Etsy-print-farm context maps onto VLM-IRIS most directly — automation-grade build-plate monitoring for unloading is the cleanest practical application. τ-schema and CIPHER are research-trajectory rather than productizable today.

### Lint

Clean: 0 orphans / 0 bidirectional gaps / 0 dangling / 0 missing-pages / frontmatter quality clean / 0 stale NEEDS VERIFICATION. **35 pages, 228 outbound edges** (up from 31 / 202 before this ingest).

### Brief staged

- `briefs/2026-05-07_vlm-prompt-discipline.md` — 2 actionable rules for the reader's day-1 chat-VLM workflow: (1) structured prompt template (printer / filament / symptom / what's-been-tried / ambient / photo) beats freeform with τ-schema empirical backing (35→89% specificity); (2) never trust VLM-generated numeric parameters with CIPHER process-expert backing (5× MAE reduction). Includes copy-pasteable prompt template + the "when chat VLMs are genuinely useful" guidance + a forward-looking note about VLM-IRIS as the most translatable paper for Etsy-print-farm automation.

### Future / deferred

- Deep-read CIPHER pages 13+ to validate out-of-distribution + autonomous-fabrication claims
- Tier-2 sweep for VLM-failure-mode papers (called out as missing from cluster)

## [2026-05-15] cross-wiki route | gracia.ai — Gaussian Splatting volumetric video (3D-export angle)

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md`.
- Created wiki/concepts/2026-05-13_gracia-ai-volumetric-3d-export.md (stub)

## [2026-05-16] cross-wiki ingest | reBot-DevArm — open-source 6-DOF robotic arm (hybrid CNC + 3D-print)

Cross-routed from OSINT-workspace tool-eval ingest `@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md` — scored STEAL-FROM tier with primary fit in this wiki. Value to the 3D-printing workspace is the project's documented hybrid CNC+print manufacturing methodology, not the robot itself.

### Created (1 page)

- `wiki/entities/tools/rebot-devarm.md` — entity tool page. 6-DOF arm (1.5 kg payload, <0.2 mm precision); bisected architecture (CNC-machined Aluminum 5052 ±0.02 mm for load-bearing parts / 3D-printed Bambu ABS + TPU 95+ for the rest, TPU on Soft Fingers). Captures concrete BOM detail: 30–45% infill for ABS Black joint bases, documented component substitutions, hardware STEP files. License split: hardware CERN-OHL-W-2.0 (copyleft triggers only on hardware-design redistribution — internal print-farm use is clean), software Apache-2.0 (Motorbridge SDK + rebotarm_ros2 Jazzy workspace). One `[NEEDS VERIFICATION 2026-05-16]` flag on long-term durability/deflection of printed MGN9 slider brackets under continuous payload.

### Modified (4 pages)

- `wiki/entities/materials/abs.md` — added `rebot-devarm.md` backlink + Relations; bumped `updated`.
- `wiki/entities/materials/tpu.md` — added `rebot-devarm.md` backlink + Relations; bumped `updated`.
- `wiki/concepts/print-farm-operations.md` — added `rebot-devarm.md` backlink + Relations; bumped `updated`.
- `wiki/index.md` — added reBot-DevArm row under Tools.

Pages touched: 5 (1 created + 4 modified) — within schema bound. Not committed; left staged.
