# Wiki Index

Content-oriented catalog of every page in the wiki. Updated on every ingest. Read this first when answering a query — drill into pages only after scanning here.

Format: each row is `[title](path) — one-line summary — tags`. A ⚠ marker means the stub has quality flags (see the stub's frontmatter).

---

## Sources

Sources are ingested research material (PDFs, articles, GitHub READMEs, YouTube transcripts). One page per canonical source.

- [Adaptive Input Shaper Design for Unknown Second-Order Systems](sources/2025-aung-adaptive-input-shaper.md) — feedforward TDF input shaper with real-time RLS parameter estimation; simulation only — `paper, control, input-shaping, vibration`
- [One-Shot Camera-Based Extrusion Optimization for High Speed FFF](sources/2025-lin-camera-extrusion-optimization.md) — two calibration prints + phone camera → optimized G-code; 2× quality-equivalent speed on Ender-3 V2 (1600→3600 mm/min) — `paper, vision, extrusion, high-speed-fdm`
- [Real time fault detection using CNN + acoustic signals](sources/2023-waheed-acoustic-cnn-fault-detection.md) — microphone + spectrogram + CNN classifier for clog / breakage / pulley skip — `paper, fault-detection, CNN, acoustic, ML`
- [Closed Loop Reference Optimization for Extrusion AM](sources/2025-hoteit-closed-loop-extrusion-lqr.md) — LQR over Force-Controlled Printing; 39.57% RMS error reduction — `paper, control, extrusion, LQR, closed-loop`
- [Multimodal Sensor Fusion for AI-Based Fault Detection](sources/2025-waheed-multimodal-sensor-fusion.md) — acoustic + vibration + thermal fusion; outperforms single-modality baselines — `paper, fault-detection, sensor-fusion, AI, multimodal`
- [QuietPrint: Protecting 3D Printers Against Acoustic Side-Channel Attacks](sources/2026-asgar-quietprint-acoustic-defense.md) — Stealth Head Movement: convex-hull G-code rewrite, ~55% time overhead — `paper, security, defense, acoustic, g-code-rewrite`
- [One Video to Steal Them All: 3D-Printing IP Theft through Optical Side-Channels](sources/2025-chattopadhyay-one-video-optical.md) — ResNet-50+LSTM recovers G-code from IP-camera video; functional counterfeit key — `paper, security, attack, optical, ResNet, LSTM`
- [Decoding IP — Acoustic and Magnetic Side-Channel Attack on a 3D Printer](sources/2025-jamarani-acoustic-magnetic-decoding.md) — smartphone (mic + magnetometer) + GBDT; 4.47% MTE — `paper, security, attack, acoustic, magnetic, GBDT`
- [Turning Hearsay into Discovery — Industrial PBF Side-Channel Attack](sources/2025-dolgavin-hearsay-pbf-power.md) — first attack on industrial PBF; differential voxelization on power traces; 90.29% TP voxel volume — `paper, security, attack, power, industrial, PBF`
- [A Collaborative Process Parameter Recommender System for Fleets of FDM 3D Printers](sources/2025-wang-collaborative-parameter-recommender.md) — sparse utility matrix + ALS + spectral clustering on 10-printer farm; per-machine tuning at fleet scale — `paper, print-farm, parameter-tuning, ALS, matrix-completion`
- [A Cost-Benefit Analysis of Additive Manufacturing as a Service](sources/2025-ivkic-cost-benefit-maas.md) — Cloud Crafting Platform on Azure; €2.12-€2.24/ring; 400-600% margin; 40/30/20/10% profit share — `paper, MaaS, business, cloud, Azure, distributed-manufacturing`
- [Object Packing and Scheduling for Sequential 3D Printing — CEGAR-inspired Solver](sources/2025-surynek-sequential-printing-cegar.md) — SEQ-PACK+S formalized; Z3 + CEGAR refinement; ships in PrusaSlicer 2.9.1 — `paper, scheduling, sequential-printing, SMT, Z3, CEGAR`
- [Parallelobox: AABB-based Decomposition for Optimized Parallel Printing](sources/2026-hatton-parallelobox-aabb-decomposition.md) — AABB height-field + k-means++ + metaheuristic; dominates Symmetry Slicer + matches/beats Cube Skeleton on complex geometry — `paper, parallel-printing, decomposition, AABB, mesh-clipping`
- [Bambu Lab Official Filament Comparison Guide + Wiki Material Table](sources/2026-bambu-filament-guide.md) — vendor-doc reference: mechanical / thermal / process / hardware-compat / drying tables for PLA/PETG/ABS/ASA/PC/PA/TPU+CF/GF — `vendor-doc, materials, baseline, bambu, reference`
- [VLM-IRIS — Vision-Language Models for Infrared Industrial Sensing in AM](sources/2026-mahjourian-vlm-iris.md) — CLIP ViT-B/32 + magma colormap + centroid prompt ensembling; 100% zero-shot IR build-plate object presence on Prusa MK3S — `paper, VLM, CLIP, infrared, thermal, zero-shot, perception, prusa-mk3s`
- [Towards Logic-Aware Manipulation — τ Knowledge Primitive for VLM Assistants](sources/2025-chen-tau-schema-vlm.md) — 8-field τ schema injects manipulation logic into GPT-4o prompts; 35→89% contact/tolerance specificity on spool-removal plans — `paper, VLM, robot-manipulation, schema, knowledge-base, planning, GPT-4o, smart-manufacturing`
- [CIPHER — Hybrid Reasoning for Perception, Explanation, and Autonomous Action](sources/2025-margadji-cipher.md) — Llama-3.2 + ResNet-152 process expert + LoRA + RAG; 5× MAE reduction (82.92→17.62) on flow rate regression from endoscope images — `paper, VLA, vision-language-action, hybrid-reasoning, RAG, chain-of-thought, regression, process-expert, cambridge`
- [Bambu Toolchain Audit — 25-Repo Phase-0 Evaluation](sources/2026-bambu-toolchain-audit.md) — Gemini-DR-style audit; 2 GO + 1 CONDITIONAL-GO + 22 NO-GO across 4 rejection patterns; closed-firmware-as-feature thesis — `audit, github, phase-0, bambu, toolchain, slicers, firmware, ecosystem-alignment`

---

## Entities

### Printers

- [Bambu Lab X1 Carbon (X1C)](entities/printers/x1c.md) — flagship CoreXY enclosed; lidar + AI camera + accelerometer; hardened nozzle; ABS/ASA/composites capable; ~$1,200 — `printer, bambu, x1c, corexy, enclosed, flagship`
- [Bambu Lab P1S](entities/printers/p1s.md) — mid-tier CoreXY enclosed; AI camera + accelerometer (no lidar); same build volume as X1C at ~$700 bare; ABS/ASA non-composite — `printer, bambu, p1s, corexy, enclosed, mid-tier`
- [Bambu Lab A1 (and A1 mini)](entities/printers/a1.md) — entry-level bed-slinger open-frame; AMS Lite; lidar + AI camera; ~$400 (A1) / ~$300 (mini); PLA/PETG/TPU only — `printer, bambu, a1, a1-mini, bed-slinger, open-frame, entry-level`
- [Flashforge Adventurer 5M (and 5M Pro)](entities/printers/flashforge-adventurer-5m.md) — non-Bambu CoreXY; **ships Klipper firmware** (inverts the Bambu closed-firmware thesis); Orca-Flashforge slicer; 220³ mm, 600mm/s; 5M open-frame / 5M Pro enclosed+camera; added for a friend, not the primary reader — `printer, flashforge, adventurer-5m, corexy, klipper, non-bambu, entry-level`

### Materials

- [PLA (Polylactic Acid)](entities/materials/pla.md) — default filament; easiest print, cheapest, widest variant catalog; brittle, low-HDT — `material, filament, FDM, baseline, biodegradable`
- [PETG (Polyethylene Terephthalate Glycol-modified)](entities/materials/petg.md) — functional default; PLA-printability with ABS-like properties; HDT 69°C / HF 87°C — `material, filament, FDM, baseline, functional`
- [ABS (Acrylonitrile Butadiene Styrene)](entities/materials/abs.md) — engineering filament; HDT 100°C, requires enclosed printer (X1C/P1S only) — `material, filament, FDM, baseline, engineering, enclosed-only`
- [ASA (Acrylonitrile Styrene Acrylate)](entities/materials/asa.md) — outdoor/UV-stable variant of ABS; HDT 117°C, same enclosure requirement — `material, filament, FDM, baseline, engineering, enclosed-only, UV-stable`
- [TPU (Thermoplastic Polyurethane)](entities/materials/tpu.md) — flexible elastomer; 95A HF only AMS-compatible (dedicated port); drying required — `material, filament, FDM, baseline, flexible, elastomer`

### Slicers

- [Bambu Studio](entities/slicers/bambu-studio.md) — mandatory native slicer; AGPL-3.0 PrusaSlicer fork; AMS / 3MF / MakerWorld / lidar-calibration integration; LAN-only mode for cloud resilience — `slicer, bambu, AGPL-3.0, GO-tier, ams-integration, 3mf, makerworld`
- [OrcaSlicer](entities/slicers/orcaslicer.md) — community AGPL-3.0 Bambu Studio fork; CONDITIONAL-GO for advanced material calibration only (profile-schema divergence as daily driver) — `slicer, AGPL-3.0, conditional-go-tier, calibration, advanced-tuning, bambu-studio-fork`

### Tools

- [Kickstarter / Autodesk FDM Test V4 Protocol](entities/tools/kickstarter-autodesk-fdm-protocol.md) — Apache-2.0 standardized calibration print (`ksr_fdmtest_v4.stl`); witness features fail in known patterns to surface specific extruder/motion failures — `calibration, benchmark, witness-features, FDM, Apache-2.0, GO-tier, materials-research`
- [Obsidian](entities/tools/obsidian.md) — local-first markdown knowledge-base app; free for personal use; recommended reader for this wiki — `tool, obsidian, knowledge-base, markdown, local-first, free-personal, navigation`
- [reBot-DevArm](entities/tools/rebot-devarm.md) — open-source 6-DOF robotic arm; bisected CNC-aluminum + 3D-print (ABS/TPU 95+) BOM; STEAL-FROM tier for hybrid-manufacturing methodology + infill profiles; CERN-OHL-W-2.0 hardware / Apache-2.0 software — `tool, robotics, robotic-arm, open-hardware, hybrid-manufacturing, ROS2, steal-from`

### AI design tools

(no individual entity pages yet — see [@concepts/ai-design-tools.md](concepts/ai-design-tools.md) for the Meshy / RodinAI / 3DAIStudio pipeline. Per-platform Phase-0 audits deferred until reader selects platform)

### Marketplaces

(no pages yet — Etsy / MakerWorld / Printables / Cults3D)

### Software

(no pages yet — modeling tools: OpenSCAD / FreeCAD / Blender / Fusion 360)

---

## Concepts

- [FDM / FFF Printing](concepts/fdm-printing.md) — hub page; defines the process and the four open problems on consumer FDM today — `process, FDM, FFF, fundamentals`
- [Input Shaping (Vibration Suppression)](concepts/input-shaping.md) — feedforward filter cancels gantry ringing on direction changes; behind Bambu "Active Tuning" — `control, vibration, feedforward`
- [Extrusion Control](concepts/extrusion-control.md) — pressure advance → camera-based G-code optimization → closed-loop force feedback — `control, extrusion, feedforward, closed-loop`
- [Fault Detection](concepts/fault-detection.md) — acoustic / vibration / thermal / visual sensors + ML classifier; behind Bambu "AI failure detection" — `ML, monitoring, sensors, fault-detection`
- [High-Speed FDM](concepts/high-speed-fdm.md) — above ~300 mm/s the dominant errors shift from positioning to dynamic mismatch; what makes Bambu fast — `process, high-speed, regime-shift`
- [Side-Channel Attacks on 3D Printers](concepts/side-channel-attacks.md) — six modalities (acoustic / optical / magnetic / power / vibration / thermal) and the attack-tier continuum — `security, side-channel, attack-surface`
- [IP Theft in 3D Printing](concepts/ip-theft-3d-printing.md) — three threat tiers from hobbyist Etsy seller to industrial outsourced AM (MATE) — `security, IP, threat-model, business`
- [G-Code Protection](concepts/g-code-protection.md) — file-level (encryption / streaming / TPM) vs physical-level (SHM / acoustic masking) defenses; coverage matrix — `security, defense, encryption, obfuscation`
- [Print Farm Operations](concepts/print-farm-operations.md) — hub page for the multi-printer regime; per-machine tuning + scheduling + MaaS productization+security — `operations, print-farm, fleet, distributed-manufacturing`
- [Print Job Scheduling](concepts/print-job-scheduling.md) — sequential printing (one printer, many objects) vs parallel decomposition (one model, many printers) — `scheduling, packing, sequential-printing, parallel-printing, optimization`
- [Additive Manufacturing as a Service (MaaS)](concepts/am-as-a-service.md) — economics + security gap of cloud-distributed AM (Cloud Crafting, Shapeways, Hubs, Xometry) vs direct-STL marketplaces (Etsy, MakerWorld) — `business, MaaS, cloud, distributed-manufacturing, economics`
- [Filaments Baseline (PLA / PETG / ABS / ASA / TPU)](concepts/filaments-baseline.md) — decision matrix + mechanical/process comparison + four hardware-compatibility rules (enclosure / drying / AMS-lite / hardened-nozzle) — `materials, filament, FDM, baseline, reference`
- [VLMs in Manufacturing — Sensing / Manipulation / Control](concepts/vlm-in-manufacturing.md) — hub for VLM/VLA research applied to FDM AM; three angles: zero-shot perception (VLM-IRIS), schema-anchored planning (τ), hybrid VLA control (CIPHER) — `VLM, VLA, AI, manufacturing, foundation-models, zero-shot`
- [Bambu Ecosystem — Closed-Firmware-as-Feature](concepts/bambu-ecosystem-closed-loop.md) — why Bambu's closed appliance architecture is load-bearing for its edge-AI features; the four NO-GO patterns from the 25-repo audit — `bambu, ecosystem, closed-firmware, vendor-lock-in, edge-AI, no-go-patterns`
- [AI Design Tools — Generative 3D for Etsy / MakerWorld Production](concepts/ai-design-tools.md) — Meshy / RodinAI / 3DAIStudio → 3MF → Bambu Studio → AMS pipeline; decorative-only restriction; hallucinated-G-code prohibition — `AI, generative-3D, text-to-3D, 3MF, AMS, MakerWorld, content-pipeline`
- [Wiki Navigation — Reading This Knowledge Base](concepts/wiki-navigation.md) — meta-guide; schema conventions (frontmatter / @path / confidence tags) + Obsidian navigation tricks; **read this on day 1** — `meta, navigation, obsidian, wiki, conventions, schema, reader-handoff`
- [gracia.ai — Gaussian Splatting volumetric video (3D-export angle)](concepts/2026-05-13_gracia-ai-volumetric-3d-export.md) — cross-wiki stub routed from ingest — `cross-wiki`
