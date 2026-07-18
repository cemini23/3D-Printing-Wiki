# Wiki Index

Content-oriented catalog of every page in the wiki. Updated on every ingest. Read this first when answering a query — drill into pages only after scanning here.

Format: each row is `[title](path) — one-line summary — tags`. A ⚠ marker means the stub has quality flags (see the stub's frontmatter).

---

## Sources

Sources are ingested research material (PDFs, articles, GitHub READMEs, YouTube transcripts). One page per canonical source.

- [Adaptive Input Shaper Design for Unknown Second-Order Systems](sources/2025-aung-adaptive-input-shaper.md) — feedforward TDF input shaper with real-time RLS parameter estimation; simulation only — `paper, control, input-shaping, vibration`
- [Self-improving CAD generation agents (arXiv:2605.17448)](sources/arxiv-2605-17448-self-improving-cad-agents.md) — K95 REFERENCE — agent loops for parametric CAD — `paper, cad, agents, k95`
- [AgentsCAD: Multi-agent FDM DFM on STEP (arXiv:2607.02448)](sources/2026-george-agentscad-fdm-dfm.md) — Claude+GPT-4o+MCP overhang DFM; Phase-0 REFERENCE — `paper, cad, agents, FDM, MCP, DFAM`
- [Multimaterial e2e topology optimization (arXiv:2607.13174)](sources/2026-luo-multimaterial-e2e-optimization.md) — soft-gripper digital materials; soft-robotics background — `paper, multimaterial, soft-robotics, background`
- [Hybrid rigid-soft gripper with self-locking (arXiv:2607.14730)](sources/2026-chen-hybrid-rigid-soft-gripper.md) — AM ratchets + membrane pneumatics; PLA FDM test spheres — `paper, soft-robotics, gripper, FDM`
- [arXiv lane noise triage — overnight fetch 2026-07-16](sources/2026-arxiv-lane-noise-triage-jul16.md) — 2/4 accept (AgentsCAD + multimaterial) — `meta, triage, arxiv, digest, noise`
- [arXiv lane noise triage — overnight fetch 2026-07-17](sources/2026-arxiv-lane-noise-triage-jul17.md) — hybrid gripper accept; exoglove re-fetch → reject stubs — `meta, triage, arxiv, digest, noise`
- [arXiv lane noise triage — overnight fetch 2026-07-18](sources/2026-arxiv-lane-noise-triage-jul18.md) — empty inbox; reject-stub skipped-dup confirmed for 07958 — `meta, triage, arxiv, digest, noise`
- [REJECT stub — soft exogloves (arXiv:2607.07958)](sources/2026-reject-arxiv-2607-07958-soft-exogloves.md) — fetch-dedupe only — `meta, reject-stub`
- [REJECT stub — soft-robot continual learning (arXiv:2607.06740)](sources/2026-reject-arxiv-2607-06740-soft-robot-continual-learning.md) — fetch-dedupe only — `meta, reject-stub`
- [One-Shot Camera-Based Extrusion Optimization for High Speed FFF](sources/2025-lin-camera-extrusion-optimization.md) — two calibration prints + phone camera → optimized G-code; 2× quality-equivalent speed on Ender-3 V2 (1600→3600 mm/min) — `paper, vision, extrusion, high-speed-fdm`
- [Real time fault detection using CNN + acoustic signals](sources/2023-waheed-acoustic-cnn-fault-detection.md) — microphone + spectrogram + CNN classifier for clog / breakage / pulley skip — `paper, fault-detection, CNN, acoustic, ML`
- [Closed Loop Reference Optimization for Extrusion AM](sources/2025-hoteit-closed-loop-extrusion-lqr.md) — LQR over Force-Controlled Printing; 39.57% RMS error reduction — `paper, control, extrusion, LQR, closed-loop`
- [Multimodal Sensor Fusion for AI-Based Fault Detection](sources/2025-waheed-multimodal-sensor-fusion.md) — acoustic + vibration + thermal fusion; outperforms single-modality baselines — `paper, fault-detection, sensor-fusion, AI, multimodal`
- [QuietPrint: Protecting 3D Printers Against Acoustic Side-Channel Attacks](sources/2026-asgar-quietprint-acoustic-defense.md) — Stealth Head Movement: convex-hull G-code rewrite, ~55% time overhead — `paper, security, defense, acoustic, g-code-rewrite`
- [Firewall3D: Hardware Firewall vs Firmware Attacks](sources/2026-asgar-firewall3d-firmware-hardware.md) — bump-in-the-wire PCB; Phase-0 REFERENCE/NO-GO hobby — `paper, security, defense, firmware, hardware`
- [Side-Channel Attacks Bypass Protection in 3D Printers (AMNC eval)](sources/2026-yocam-amnc-bambu-side-channel.md) — first deployed AMNC eval on Bambu P1P/A1 Mini; acoustic at chance; vibration partial — `paper, security, side-channel, bambu, AMNC`
- [arXiv lane noise triage — overnight fetch 2026-06-20](sources/2026-arxiv-lane-noise-triage-jun20.md) — reject-all triage for 5 off-topic Exa arXiv hits; query tighten follow-up — `meta, triage, arxiv, digest, noise`
- [arXiv lane noise triage — overnight fetch 2026-06-21](sources/2026-arxiv-lane-noise-triage-jun21.md) — second reject-all; publisher URLs carry signal; arxiv auto-fetch disabled — `meta, triage, arxiv, digest, noise`
- [arXiv lane noise triage — overnight fetch 2026-06-22](sources/2026-arxiv-lane-noise-triage-jun22.md) — third reject-all; global auto-fetch disabled — `meta, triage, arxiv, digest, noise`
- [arXiv lane noise triage — overnight fetch 2026-07-15](sources/2026-arxiv-lane-noise-triage-jul15.md) — 1/5 accept (Firewall3D) after fetch re-enable — `meta, triage, arxiv, digest, noise`
- [OrcaSlicer V2.4.2 maintenance release](sources/2026-orcaslicer-2-4-2-release.md) — profiles/cloud/Bambu plugin reliability patch — `news, OrcaSlicer, release`
- [Bambu × Pop Mart MakerWorld IP settlement](sources/2026-bambu-popmart-makerworld-ip-settlement.md) — Labubu fan-models delisted; platform copyright risk — `news, MakerWorld, IP, Bambu`
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
- [DuoMorph — FDM + Pneumatic Shape-Changing Interfaces](sources/2026-li-duomorph-fdm-pneumatic.md) — CHI '26; heat-seal + FDM + 4D pre-shape on TPU film; validated on Bambu A1 — `CHI, pneumatic, FDM, 4D, shape-changing`
- [FluxLab — SLA Shape-Changing + SMA Inductive Sensing](sources/2026-lee-fluxlab-sma-sla.md) — TEI '26; FluxIO gyroid SLA + Nitinol spring; not consumer FFF — `TEI, SLA, SMA, sensing, shape-changing`
- [Single-Material 4D via PvP Strain Trapping](sources/2025-iqbal-single-material-4d-pvp.md) — desktop FFF + commercial SMP; ~50% trapped strain; lattice expansion unit cells — `4D, SMP, PvP, FFF, metamaterial`
- [NAT-LCE DIW with Hybrid Cooling](sources/2026-li-lce-nat-diw-hybrid-cooling.md) — DIW liquid-crystal elastomer; background-only for FFF wiki — `LCE, DIW, soft-robotics, background`
- [TinkerXR — AR CAD for Novices](sources/2025-arslan-tinkerxr-ar-cad-novices.md) — SCF '25; Quest 3 in-situ CSG; not day-1 — compare Tinkercad baseline in @concepts/novice-cad-workflows.md — `AR, CAD, novice, open-source`
- [Physics-Informed Extrusion Dynamical Model](sources/2025-looey-physics-informed-extrusion-dynamical.md) — arXiv:2512.11048; reduced-order flow model for control — `extrusion, control, CFD, DIW`
- [Daily digest — OrcaSlicer 2.4 news](sources/2026-06-02-digest-orcaslicer-2-4-news.md) — sweep news stub — `digest, OrcaSlicer, news`
- [Daily digest — Polymaker ABS Pro](sources/2026-06-02-digest-polymaker-abs-pro.md) — sweep vendor stub — `digest, ABS, Polymaker`
- [Berkeley Humanoid Lite — Open-Source 3D-Printed Humanoid](sources/2025-chi-berkeley-humanoid-lite.md) — cycloidal printed gearboxes; <$5k; RL sim-to-real — `robotics, humanoid, open-source, FDM`
- [MEVITA — Open-Source Bipedal Robot (Sheet Metal)](sources/2025-kawaharazuka-mevita-bipedal.md) — JSK Tokyo; critiques fragile print-only bipeds — `robotics, bipedal, open-source`
- [MEVIUS — E-Commerce Quadruped](sources/2024-kawaharazuka-mevius-quadruped.md) — metal quadruped for outdoor durability — `robotics, quadruped, open-source`
- [eFlesh — 3D-Printed Magnetic Tactile Sensors](sources/2025-pattabiraman-eflesh-magnetic-tactile.md) — hobby FDM + magnets + Hall PCB — `robotics, tactile, FDM`
- [M3D-skin — Multi-Material FDM Tactile Sensor](sources/2025-yoshimura-m3d-skin-tactile-fdm.md) — conductive TPU infill sensing — `robotics, tactile, TPU, multi-material`
- [Bed Rotation Mechanism for In-Situ Photogrammetric FDM QA](sources/2011-roberts-bed-rotation-photogrammetry.md) — ingest pass 10–16 — `paper, FDM, research-platform, photogrammetry, legacy`
- [SplatOverflow — Gaussian Splat Hardware Troubleshooting](sources/2024-kwatra-splatoverflow-troubleshooting.md) — ingest pass 10–16 — `paper, tooling, 3D-scan, CAD, HCI`
- [3D-Printed Canine Head Phantom for Veterinary Radiotherapy QA](sources/2024-rotoo-canine-head-phantom-vet.md) — ingest pass 10–16 — `paper, medical, polyjet, phantom, background`
- [THz EM Vortices from Commercial FDM Prints](sources/2025-adams-fdm-thz-em-vortices.md) — ingest pass 10–16 — `paper, photonics, FDM, THz, background`
- [Neuromorphic Anomaly Detection in Laser Powder Bed Fusion](sources/2025-banerjee-neuromorphic-lpbf.md) — ingest pass 10–16 — `paper, LPBF, neuromorphic, anomaly-detection, industrial, background`
- [Spatiotemporal Graph Transformer for LPBF Quality Prediction](sources/2026-pelaez-stgt-lpbf-quality-prediction.md) — STGT dual-attention; R² 0.719 with cross-layer 3D neighborhood on NIST AMMT — `paper, LPBF, graph-transformer, quality-monitoring, industrial, background`
- [Stretchable Strain Sensors via Direct Ink Writing on Silicone](sources/2025-cha-diw-stretchable-strain-sensors.md) — ingest pass 10–16 — `paper, DIW, sensors, soft-robotics`
- [Automated Fabrication of Magnetic Soft Microrobots](sources/2025-clancy-magnetic-soft-microrobots.md) — ingest pass 10–16 — `paper, soft-robotics, magnetic, DIW, background`
- [X-ray CT + AI for AM Process Protocol Prediction (MEX)](sources/2025-khod-xray-ct-am-protocol-ai.md) — ingest pass 10–16 — `paper, AI, X-ray-CT, MEX, process-parameter, background`
- [3D Cal — Open-Source Tactile Sensor Calibration via 3D Printer](sources/2025-kota-3d-cal-tactile-calibration.md) — ingest pass 10–16 — `paper, tactile, open-source, FDM, tooling`
- [TS-ACES — Scalable Smart Factory Embedding for 3D Print Farms](sources/2025-leet-ts-aces-smart-factory.md) — ingest pass 10–16 — `paper, smart-factory, scheduling, print-farm, formal-methods`
- [Microscale UV Nanosecond Laser Sintering of Cu Nanoparticles](sources/2025-liang-microscale-sls-cu-uv.md) — ingest pass 10–16 — `paper, SLS, metal, microscale, background`
- [Five-Finger Soft Hand — Skin and Skeleton 3D Printed as One Unit](sources/2025-miyama-soft-hand-skin-skeleton.md) — ingest pass 10–16 — `paper, soft-robotics, FDM, hand, JSK`
- [Mobile Food Printing in Professional Kitchens — Novice Chef Study](sources/2025-mobile-food-printing-kitchens.md) — ingest pass 10–16 — `paper, food-printing, 3DFP, HCI, background`
- [Slug-Mapper — 3D Printer Repurposed for ULF MRI Field Mapping](sources/2025-morris-slug-mapper-ulfl-mri.md) — ingest pass 10–16 — `paper, tooling, open-source, repurpose, MRI`
- [SE-WDNN Multi-Target Prediction for Continuous-Fiber AM Composites](sources/2025-parvaresh-cfrc-am-se-wdnn.md) — ingest pass 10–16 — `paper, ML, composites, Markforged, background`
- [Noise-Aware Optimization for Parallel Manufacturing Systems](sources/2025-schenka-noise-aware-parallel-optimization.md) — ingest pass 10–16 — `paper, print-farm, Bayesian-optimization, variability`
- [SLS Laser Power Control Sensitivity to Temperature Measurement Noise](sources/2025-toshani-sls-laser-power-noise.md) — ingest pass 10–16 — `paper, SLS, control, uncertainty, background`
- [Production and Manufacturing of 3D Printed Acoustic Guitars](sources/2025-tran-3d-printed-acoustic-guitars.md) — ingest pass 10–16 — `paper, FDM, PLA, musical-instrument, maker`
- [3D-Printed Biocompatible Ionic Polymer Membranes for Soft Actuators](sources/2025-truempler-ionic-polymer-diw.md) — ingest pass 10–16 — `paper, soft-robotics, DIW, actuator, background`
- [STL-to-Stokeslet — Hydrodynamics from Printable Mesh](sources/2026-cheng-stl-to-stokeslet.md) — ingest pass 10–16 — `paper, simulation, STL, background`
- [Thermal Drawing of Fibers from 3D-Printed Preforms](sources/2026-demircali-thermal-drawing-preforms.md) — ingest pass 10–16 — `paper, hybrid-process, fiber, FDM, background`
- [3D-Printed Lithographs for Microscopy Accessibility](sources/2026-faulkner-lithographs-microscopy.md) — ingest pass 10–16 — `paper, accessibility, lithograph, FDM, tactile-art`
- [Technomolecular Materials — 3D-Printed 2D Nanosheets](sources/2026-hamoudi-technomolecular-nanosheets.md) — ingest pass 10–16 — `paper, nanotechnology, DIW, background`
- [Tendon-Actuated Continuum Robots with Tapered TPU Backbone](sources/2026-hansen-tendon-actuated-tpu-backbone.md) — ingest pass 10–16 — `paper, soft-robotics, TPU, continuum, FDM`
- [TastePrint — Layer-Wise Taste via Airbrushed Seasoning](sources/2026-miyatake-tasteprint-food-printing.md) — ingest pass 10–16 — `paper, food-printing, 3DFP, HCI`
- [Robust LQR Control of Cementitious Material Extrusion (RCE/DIW)](sources/2026-mohammadi-rce-lqr-extrusion.md) — ingest pass 10–16 — `paper, extrusion, control, DIW, background`
- [High-Resolution 3D-Printed Plastic Scintillators](sources/2026-moore-plastic-scintillators-sla.md) — ingest pass 10–16 — `paper, SLA, materials, background`
- [Automatic Exposure Control for Tomographic VAM](sources/2026-orth-auto-exposure-vam.md) — ingest pass 10–16 — `paper, VAM, tomographic, process-control, background`
- [LOCABINACONN — 3D-Printable All-Dielectric Inverse Design](sources/2026-passia-locabinaconn-dielectric-sla.md) — ingest pass 10–16 — `paper, SLA, inverse-design, photonics, background`
- [3D-Printed Helical Waveguides for Smith-Purcell Radiation](sources/2026-taleb-helical-waveguide-2pp.md) — ingest pass 10–16 — `paper, photonics, 2PP, background`
- [Unified Multiscale Printer — TVAM + Two-Photon Polymerization](sources/2026-unlu-unified-tvam-2pp.md) — ingest pass 10–16 — `paper, VAM, TVAM, 2PP, volumetric, background`
- [Optical Phased Arrays on Lithium Tantalate (Background Stub)](sources/2026-yue-lithium-tantalate-opa.md) — ingest pass 10–16 — `paper, photonics, OPA, background, stub`
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
- [Cursor](entities/tools/cursor.md) — IDE + Chat with `@` file refs; **friend handoff AI** (Cursor Pro, not Claude Code) — `tool, cursor, IDE, AI, friend-handoff`
- [reBot-DevArm](entities/tools/rebot-devarm.md) — open-source 6-DOF robotic arm; bisected CNC-aluminum + 3D-print (ABS/TPU 95+) BOM; STEAL-FROM tier for hybrid-manufacturing methodology + infill profiles; CERN-OHL-W-2.0 hardware / Apache-2.0 software — `tool, robotics, robotic-arm, open-hardware, hybrid-manufacturing, ROS2, steal-from`
- [markdown-preview-pluk](entities/tools/markdown-preview-pluk.md) — native macOS markdown previewer with LaTeX + Mermaid; cross-wiki stub (canonical in OSINT wiki); tangential workflow tip for wiki authors — `tool, markdown, previewer, macOS, LaTeX, Mermaid, cross-wiki-stub`

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
- [Self-improving CAD generation agents](concepts/self-improving-cad-generation-agents.md) — K95 REFERENCE (2605.17448) — `cad, agents, k95`
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
- [Shape-Changing Interfaces — FDM and Adjacent Modalities](concepts/shape-changing-fdm-interfaces.md) — hub: PvP SMP 4D, DuoMorph pneumatics, FluxLab SLA contrast, LCE background — `shape-changing, 4D, pneumatic, SMP, maker`
- [Novice CAD Workflows — What to Use When You're Just Starting](concepts/novice-cad-workflows.md) — week-1 download STLs → week-2 Tinkercad; explicitly skips print-farm / shape-changing — `beginner, CAD, Tinkercad, day-1, workflow`
- [Open-Source Legged Robotics — FDM Platforms and Printed Tactile Sensing](concepts/open-source-legged-robotics.md) — humanoid/quadruped OS platforms + eFlesh/M3D-skin; advanced, not day-1 — `robotics, open-source, tactile, legged`
- [Volumetric Additive Manufacturing — Background Hub](concepts/volumetric-additive-manufacturing.md) — `VAM, TVAM, volumetric, LPBF, background, non-FFF`
- [Soft Robotics — FDM, DIW, and Tactile Tooling](concepts/soft-robotics-fdm-diw.md) — `soft-robotics, DIW, tactile, TPU, advanced`
- [Niche FDM Applications — Accessibility, Food, Music, Medical](concepts/niche-fdm-applications.md) — `applications, accessibility, food-printing, PLA, maker`
- [Industrial AM — Monitoring, Smart Factories, and Metal Processes](concepts/industrial-am-monitoring.md) — `industrial, LPBF, SLS, smart-factory, ML, background`
- [Printed Photonics and Metamaterials — Background](concepts/printed-photonics-background.md) — `photonics, SLA, 2PP, THz, background, stub-hub`
- [FDM Research Tools — Repurposed Printers and Hybrid Processes](concepts/fdm-research-tools.md) — `research, tooling, photogrammetry, repurposed, hybrid`
---

## Meta

- [Daily research digest cadence (3d-printing)](meta/daily-research-digest-cadence.md) — federated Exa/inbox discovery loop (K93); sweep reports in `wiki/sweeps/` — `meta, automation, federation, k93`
- [Daily research sweep template](sweeps/_daily-template.md) — copy scaffold for `wiki/sweeps/YYYY-MM-DD-daily.md` — `meta, template, sweep`
