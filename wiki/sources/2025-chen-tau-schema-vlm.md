---
title: "Towards Logic-Aware Manipulation — A Knowledge Primitive for VLM-Based Assistants in Smart Manufacturing"
type: source
tags: [paper, VLM, robot-manipulation, schema, knowledge-base, planning, GPT-4o, smart-manufacturing]
keywords: [tau schema, manipulation logic, object-centric, retrieval-augmented prompting, VLM planning, ChatGPT-4o, spool removal, dual-arm robot, Airbot MMK2, plan-quality metrics, Chen Guo HKUST]
related:
  - concepts/fdm-printing.md
  - concepts/vlm-in-manufacturing.md
maturity: draft
created: 2026-05-07
updated: 2026-05-07
read_status: read
---

## Relations

@concepts/fdm-printing.md @concepts/vlm-in-manufacturing.md

## Raw Concept

- Title: Towards Logic-Aware Manipulation: A Knowledge Primitive for VLM-Based Assistants in Smart Manufacturing
- Authors: Suchang Chen, Daqiang Guo — Hong Kong University of Science and Technology (Guangzhou)
- Type: arXiv preprint, 2512.11275v1 [cs.RO], 12 Dec 2025
- File: `raw-sources/2025-chen-tau-schema-vlm.pdf`
- Pages: 8
- Read-status: read (full paper)
- Retrieved: from `research to be indexed/` 2026-05-07

What it studies: how to anchor VLM-generated manipulation plans in a structured knowledge primitive (the τ tuple) so that off-the-shelf VLMs produce safer, more parameter-explicit, more constraint-respecting plans for collaborative manufacturing tasks. Case study: 3D-printer empty-spool removal by a dual-arm mobile robot.

## Narrative

### The schema: τ tuple

VLMs prompted with image + freeform instruction tend to produce plans that read like SOPs ("open lid, grasp spool, place in bin") but **omit execution-critical parameters** — approach vector, contact modality, force limits, tolerances, safety preconditions. The paper formalizes an **8-field object-centric manipulation logic schema**:

```
τ = ⟨ obj, iface, pre, contact, prim, traj, tol, dyn ⟩
```

| Field | What it carries |
|---|---|
| **obj** | Object class, target part, geometric features, frames |
| **iface** | Interface mechanism (button / knob / latch / lever / hinge / valve), operation mode (push / rotate / slide), admissible DoF |
| **pre** | Preconditions: interlocks, safety states, tool presence, required orderings |
| **contact** | Intermittent vs sustained, alignment, approach vector, fixture/compliance |
| **prim** | Primitive verb + direction (press / pull / slide / lift / twist cw/ccw); axis unit vector |
| **traj** | Trajectory phases (approach / engage / ramp / dwell / sweep / retreat) with parameters and event conditions |
| **tol** | Pose & clearance bands with SI units (mm, °) |
| **dyn** | Force/impedance numeric limits (`dyn.num`) + runtime checks (`dyn.checks`) |

Critical design choice: `dyn.num` (numeric force / torque / stiffness limits) is **never auto-labeled by VLMs** — must come from manuals, instrumented logs, or guarded calibration. This is an explicit anti-hallucination mechanism.

### How it's used (two modes)

1. **Train-time tagged augmentation**: demonstrations / logs are auto-labeled for non-`dyn` fields by pairing VLM proposals with rule templates. Schema-tagged augmentation feeds back into VLM training to teach the model to map visuals → manipulation logic.
2. **Test-time logic-aware prompting**: at runtime, perception detects `(obj.class, obj.part, iface.mechanism)`; a small KB (currently a hand-authored dictionary) is queried for the matching τ tuple; the τ is rendered into the VLM prompt; the VLM is instructed to ground its plan in those fields.

### Case study: 3D-printer spool removal

A desktop FDM 3D printer with a hinged top lid + passive spool spindle + nearby waste bin. Dual-arm mobile robot platform: **Airbot MMK2**. Routine task: "Remove the empty PLA filament spool from the printer and discard it in the waste bin."

The reference τ instance covers: lid rotate-to-open, spool axial-pull off spindle, bin transfer, with full numeric parameters — approach speeds (60-200 mm/s), grip forces (4-8 N per finger), tolerances (coaxial error ≤ 2 mm; roll tilt |α| ≤ 5°), event conditions (no slip, force drop > 20% on extract).

**No physical execution.** The case study evaluates plan quality only — VLM prompted with image + instruction generates a numbered action plan; plan is scored against τ as the reference specification.

### Headline results — N=10 plans per condition, ChatGPT-4o backbone

| Metric | Baseline (no τ) | τ-anchored | Δ |
|---|---|---|---|
| Step coverage (%) | 68 | **94** | +26pp |
| Order validity (%) | 50 | **92** | +42pp |
| Safety/constraint coverage (%) | 66 | **88** | +22pp |
| Contact/tolerance specificity (%) | 35 | **89** | +54pp |
| Avg. steps per plan | 5.3 | 7.6 | +2.3 |

**Big wins on order validity and contact/tolerance specificity** — the dimensions where freeform LLM/VLM planning is weakest. Plans become explicit about safety preconditions (printer cooled, motors disabled), contact details (where on the spool to grasp), and tolerance bands (coaxial error during axial extract).

### Limitations

- **No hardware execution.** Plan-quality scored against τ as reference; not against actual robot success/failure rates. Authors flag deployment metrics (first-try success, force-limit violations, retries, time-to-completion) as future work.
- **Hand-authored KB.** Current prototype: small dictionary, exact-match lookup. No graph-based retrieval, no learning, no scale.
- **Single task.** Spool removal only. Generalizes only as far as the τ schema is reused; generalization claim is conceptual not empirical.
- **τ instance hand-authored too.** The reference τ tuple is constructed from machine docs + cell layout + operator experience. Auto-extraction from manuals is gestured at (Manual2Skill citation) but not implemented.

### Why this matters for a Bambu hobbyist

[TENTATIVE 2026-05-07] Direct relevance is low — reader will be removing spools by hand, not via dual-arm robot. But two indirect lessons:

1. **Schema-anchored prompting beats freeform.** When the reader uses a VLM (Claude, GPT-4o, Gemini) to advise on a 3D-printing problem, structured prompts that enumerate constraints (printer model, material, ambient conditions, what's been tried) get better answers than "what's wrong with my print?" with a photo. This paper is empirical evidence for that intuition.
2. **VLMs are weak on numeric / quantitative engineering parameters.** Don't trust a VLM's invented force limits, temperature ranges, or tolerances — those numbers must come from datasheets / manuals / actual measurements.

[CONFIRMED] τ-anchored prompts produce dramatically more constraint-respecting plans than freeform on the spool-removal task. [TENTATIVE] Generalization to other manipulation tasks is plausible (the paper argues schema-orthogonal-to-policy-class) but not empirically demonstrated.

## Snippets

> "We formalize an object-centric manipulation-logic schema, serialized as an eight-field tuple τ, which exposes object, interface, trajectory, tolerance, and force/impedance information as a first-class knowledge signal between human operators, VLM-based assistants, and robot controllers."
[Source: 2025-chen-tau-schema-vlm.pdf p.1 (abstract)]

> "Numeric interaction parameters dyn.num (e.g., torque bands, stiffness, dwell) are injected from synchronized F/T or joint-torque logs, disturbance-observer estimates, or retrieved manuals/datasheets; when unknown, values are discovered via guarded, impedance-limited calibration under collaborative safety limits. [...] dyn.num is never promoted [from auto-labeled tags]."
[Source: 2025-chen-tau-schema-vlm.pdf p.4 (Section 4.2)]

> "[Plan] coverage, order validity, and safety/constraint coverage are reported as percentages; contact/tolerance specificity is the fraction of manipulation steps with explicit parameterization. All values are averages over N=10 sampled plans per condition, scored using the metrics defined above with τ_spool_remove_discard as the reference specification."
[Source: 2025-chen-tau-schema-vlm.pdf p.6 (Table 3 caption)]
