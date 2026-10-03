---
title: VLMs in Manufacturing — Sensing / Manipulation / Control / Deployment
type: concept
tags: [VLM, VLA, AI, manufacturing, foundation-models, zero-shot, perception, planning, control, deployment, failure-modes]
keywords: [vision-language model, vision-language-action, CLIP, Llama-3.2, GPT-4o, OpenVLA, foundation model in manufacturing, zero-shot, prompt ensembling, schema-anchored prompting, process expert, hybrid reasoning, additive manufacturing AI, action chunking, embodiment adaptation, illumination robustness]
related:
  - concepts/fdm-printing.md
  - concepts/fault-detection.md
  - concepts/extrusion-control.md
  - concepts/ai-design-tools.md
  - sources/2026-mahjourian-vlm-iris.md
  - sources/2025-chen-tau-schema-vlm.md
  - sources/2025-margadji-cipher.md
  - sources/2026-liu-chunkvla-am-vla-deployment.md
  - concepts/novice-cad-workflows.md
  - entities/tools/cursor.md
  - sources/2025-khod-xray-ct-am-protocol-ai.md
maturity: draft
created: 2026-05-07
updated: 2026-10-03
---

## Relations

@concepts/fdm-printing.md @concepts/fault-detection.md @concepts/extrusion-control.md @concepts/ai-design-tools.md @sources/2026-mahjourian-vlm-iris.md @sources/2025-chen-tau-schema-vlm.md @sources/2025-margadji-cipher.md @sources/2026-liu-chunkvla-am-vla-deployment.md @concepts/novice-cad-workflows.md @entities/tools/cursor.md @sources/2025-khod-xray-ct-am-protocol-ai.md

## Raw Concept

Vision-Language Models (and their action-emitting cousins, Vision-Language-Action models) are the dominant 2024-2026 research story in AI applied to manufacturing. This page is the hub for that research as it touches consumer-grade FDM 3D printing — synthesized from a 3-paper cluster ingested 2026-05-07 covering three orthogonal angles of application, plus a 2026-10-03 addition covering **deployment** (the fourth angle, and the first paper in the cluster that reports failures).

## Narrative

### What's a VLM, what's a VLA?

- **VLM (Vision-Language Model)**: maps images + text into a shared embedding space, or generates text grounded in image content. Examples: CLIP, LLaVA, GPT-4o (multi-modal), Claude with vision, Gemini Vision. Trained on internet-scale image-caption pairs.
- **VLA (Vision-Language-Action)**: a VLM with an action head — outputs not just text but executable commands (robot trajectories, machine instructions). Examples: PaLM-E, RT-2, OpenVLA, **CIPHER** [@sources/2025-margadji-cipher.md].

The promise for manufacturing: **one model that perceives the workpiece, explains what it sees, plans an intervention, and emits the machine instructions for that intervention** — replacing today's brittle pipeline of (vision model → rule engine → motion controller).

### The four angles — what the 2025-2026 research is actually doing

The cluster of papers ingested into this wiki covers four distinct application angles:

| Angle | Question | Representative paper |
|---|---|---|
| **Sensing / perception** | Can a foundation model classify manufacturing imagery without retraining? | VLM-IRIS [@sources/2026-mahjourian-vlm-iris.md] |
| **Manipulation / planning** | Can a VLM produce safe, parameter-explicit plans for robot intervention? | τ-schema [@sources/2025-chen-tau-schema-vlm.md] |
| **Control / end-to-end** | Can a single VLA do perception + reasoning + machine-instruction emission, including quantitative regression? | CIPHER [@sources/2025-margadji-cipher.md] |
| **Deployment** | What breaks when you actually put one in a workcell — and what does it cost? | ChunkVLA-AM [@sources/2026-liu-chunkvla-am-vla-deployment.md] |

Each angle has its own load-bearing technique:

- **VLM-IRIS** — *modality bridging via colormap preprocessing.* CLIP was trained on RGB; thermal IR is single-channel. Convert IR to magma colormap → CLIP's RGB-trained filters work on it → 100% zero-shot accuracy on build-plate object presence (Prusa MK3S, room temp). **No retraining.** Plus centroid prompt ensembling (average N hand-written prompts to make the classifier robust to phrasing).
- **τ-schema** — *schema-anchored prompting.* Generic VLM plans for robot manipulation are SOP-shaped (open lid, grasp, place) but omit the parameters that make plans executable (approach vector, force limits, tolerances). Render an 8-field τ tuple ⟨obj, iface, pre, contact, prim, traj, tol, dyn⟩ into the prompt and the VLM produces plans that score 35→89% on contact/tolerance specificity.
- **CIPHER** — *process expert + foundation model hybrid.* LLMs/VLMs are bad at quantitative regression (continuous-value prediction). Bolt a small ResNet-152 alongside the LLM to produce a single dedicated start token of regression-grade features → MAE 82.92 → 17.62 (5× reduction) on flow rate prediction from nozzle endoscope images.
- **ChunkVLA-AM** — *embodiment adaptation + action chunking + robot-side safety filtering.* A pre-trained VLA does not transfer to a new robot in a constrained cell; LoRA-adapt it on that robot's demonstrations, predict 8-step action chunks, and clamp every command against workspace and clearance limits before it reaches the controller. → zero-shot MAE 179.60–650.12 mm collapses to **1.74 mm** open-loop; **39/42 (92.9%)** physical transfers.

### Deployment — what the failure data actually says

This is the angle the first three papers could not supply. [@sources/2026-liu-chunkvla-am-vla-deployment.md] put a 7B OpenVLA-OFT model on a FAIRINO FR3 doing post-print part retrieval, and reported what went wrong.

| Configuration | MAE (mm) | Reading |
|---|---|---|
| OpenVLA / OpenVLA-OFT, zero-shot | **179.60–650.12** | Unusable. Pre-trained backbones do not transfer to a constrained workcell. |
| Single-step adapted | 9.50 avg, **16.90 on X** | *"easily causes collisions with the build plate or printed parts"* |
| Adapted + 8-step chunks | 1.74 avg | 0.37 X / 0.97 Y / **3.87 Z** |

Five findings that generalize beyond this one workcell:

1. **Adaptation is mandatory.** Zero-shot failed by hundreds of millimetres. Notably, the **chunked zero-shot model failed just as badly** as the single-step one — the paper's conclusion is that *"temporal action chunking alone cannot compensate for the lack of spatial semantics."* Chunking is a **temporal** device; it does not supply missing **spatial** grounding.
2. **A 16.90 mm lateral error is a collision, not a quality defect.** Errors in a workcell are judged by what they hit, not by their magnitude in a chart.
3. **Z was the dominant error axis all the way through** (3.87 mm vs 0.37/0.97). The same imbalance showed up physically: **all 3 of the 42 trials that failed did so at terminal placement**, when release-height control let the object topple. Vertical precision is the hard part.
4. **Lighting is a deployment variable with a measurable safe band.** A 10-trial × 181-level luminance sweep found minimum error at luminance 95, a low-error band of **85–125**, and degradation of **+31.2%** / **+20.9%** at the darkest and brightest endpoints. Extreme glare hurt most; colour temperature barely mattered. Crucially, **luminance 95 is not a universal optimum** — per-trial optima ranged from 36 to 198. The recommendation is lighting augmentation for reflective AM workspaces, not a fixed lamp setting.
5. **Safety filtering is where the engineering lives.** Workspace bounds, a build-plate clearance floor, per-step clamps (5 mm / 0.05 rad), and rejection of NaN, stale, timed-out, and post-e-stop commands. The authors are careful that these are **deployment parameters, not safety guarantees**.

**Two caveats to carry before quoting the numbers.** First, the 1.74 mm figure is **open-loop trajectory consistency on logged frames** — the paper states it *"describe[s] open-loop trajectory consistency, not final task success."* The closed-loop number is 92.9%. Second, the comparison **is not a clean ablation**: the four configurations differ in both adaptation *and* horizon, so the paper explicitly does not attribute the gain to chunking alone.

**Cost.** Model-side inference was 0.06–0.08 s per request on an RTX 6000 Ada — and that **excludes** capture, network, and robot execution. The 7B model cannot run on the robot's CPU-only workstation, which is why the architecture splits cloud and edge. This is server-class inference, confirming the cost concern already raised for CIPHER below.

### Common limitations across the cluster

- **Single-machine validation.** Each paper validates on one platform: Prusa MK3S (VLM-IRIS), Airbot MMK2 dual-arm (τ-schema), one commercial-grade FDM with custom endoscope (CIPHER). Cross-platform generalization is asserted but not exhaustively tested.
- **Regression and quantitative reasoning is the consistent weak spot.** Both τ-schema and CIPHER explicitly address it (τ-schema's `dyn.num` is "never auto-labeled by VLMs"; CIPHER bolts a ResNet on for regression). Bare VLMs do not produce trustworthy numbers for engineering applications.
- **Hardware integration assumed.** All three need camera or sensor data piped to the model in a structured way, and CIPHER assumes printer firmware exposes process parameters as labels. Bambu's consumer printers expose less of this than research-grade hardware.

### Why this matters for a Bambu hobbyist (today and in the next 3-5 years)

[TENTATIVE 2026-05-07] Direct hands-on relevance for the reader in 2026 is **low** — none of these systems is a downloadable consumer product. But the conceptual lessons are immediate:

1. **Bambu's "AI failure detection" is the simplest member of this family.** RGB camera + classifier for spaghetti / first-layer / clog. CIPHER points at where this likely goes: **a single agent that detects the failure, explains why, and proposes a fix in the same model.** Probable consumer-printer trajectory: 2027-2029.
2. **When the reader uses a chat VLM (Claude, GPT-4o, Gemini) to advise on a 3D-printing problem, structured prompts beat freeform.** The τ-schema result on plan quality is empirical evidence: *what's the printer model, what filament, what's the symptom, what have you tried, here's a photo* will get materially better answers than *"what's wrong with my print?"* + photo.
3. **Don't trust a chat VLM's invented numbers.** Both τ-schema (`dyn.num` can't be VLM-labeled) and CIPHER (process expert is the entire reason for the architecture) confirm it: VLMs hallucinate quantitative parameters. Force limits, temperature ranges, retract distances must come from datasheets, manuals, or tested measurements — not the model's "this seems reasonable" generation.
4. **When a robot eventually does touch your prints, judge it by what it hits.** The deployment paper's most useful frame is that a 16.90 mm lateral error is not a quality score — it is a collision with the build plate. And when their system did fail (3 of 42), it failed in one repeated way: vertical placement. Expect the last centimetre to be the hard part, not the first.

### What's missing from this cluster

Two of the three original gaps are now partly closed by [@sources/2026-liu-chunkvla-am-vla-deployment.md] (2026-10-03). Status:

| Gap | Status |
|---|---|
| **Failure modes of VLM-in-manufacturing deployments** | **Covered** — ChunkVLA-AM quantifies zero-shot failure (179.60–650.12 mm), single-step drift (16.90 mm X → collision), the 3/42 placement failures, and illumination sensitivity. Still only **one** deployment study, so treat the pattern as one data point rather than a law. |
| **Cost / latency at consumer-printer scale** | **Partly covered** — ChunkVLA-AM gives 0.06–0.08 s model-side inference on an RTX 6000 Ada, excluding capture/network/execution. Confirms server-class inference. Still no consumer-scale (sub-$1k) cost analysis. |
| **Comparison to the dedicated-CNN baseline** | **Still open.** CIPHER's 17.62 MAE on flow rate would plausibly be matched by a supervised CNN; the value-add is the language interface, not the perception number. No ingested paper isolates this. |

[NEEDS VERIFICATION 2026-05-07] Original flag: *adding 1-2 papers on consumer-printer VLM failure modes or cost analyses would round out the cluster.* One deployment paper now ingested (2026-10-03). A second independent deployment study, or a CNN-baseline comparison, would close this fully.

**Also still absent:** the deployment paper's task is coloured-block A-to-B transfer, not a real AM operation. The authors name the gap themselves — warped-part inspection and failed-print removal are listed as future work. So the wiki still has no VLA paper doing a genuinely AM-specific inspection or repair task.

[CONFIRMED] VLMs require either preprocessing tricks (VLM-IRIS), schema anchoring (τ-schema), hybrid architectures (CIPHER), or embodiment adaptation plus safety filtering (ChunkVLA-AM) to be useful for engineering tasks — bare-prompt VLMs are insufficient for all four angles. [CONFIRMED] Quantitative regression is the universal weak spot. [CONFIRMED] A pre-trained VLA does not transfer to an unseen robot embodiment: zero-shot error was 179.60–650.12 mm, and adaptation reduced it to 1.74 mm. [TENTATIVE — single deployment study] Action chunking improves temporal coherence but cannot supply missing spatial grounding. [TENTATIVE] Consumer-printer integration of any of these techniques is plausibly 2-3 years out, with the Bambu/Prusa/Creality cohort most likely to be first.

## Snippets

(none — synthesis page; underlying material is on the four source pages)
