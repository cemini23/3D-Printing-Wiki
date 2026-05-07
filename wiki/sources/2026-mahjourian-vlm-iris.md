---
title: "VLM-IRIS — Vision-Language Models for Infrared Industrial Sensing in Additive Manufacturing"
type: source
tags: [paper, VLM, CLIP, infrared, thermal, zero-shot, perception, prusa-mk3s]
keywords: [VLM-IRIS, CLIP, ViT-B/32, FLIR Boson, magma colormap, centroid prompting, zero-shot classification, infrared, thermal infrared, prompt engineering, Prusa MK3S, additive manufacturing monitoring]
related:
  - concepts/fdm-printing.md
  - concepts/fault-detection.md
  - concepts/vlm-in-manufacturing.md
  - entities/materials/petg.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
read_status: read
---

## Relations

@concepts/fdm-printing.md @concepts/fault-detection.md @concepts/vlm-in-manufacturing.md @entities/materials/petg.md

## Raw Concept

- Title: Vision-Language Models for Infrared Industrial Sensing in Additive Manufacturing Scene Description
- Authors: Nazanin Mahjourian, Vinh Nguyen — Michigan Technological University, Department of Mechanical and Aerospace Engineering
- Type: ASME conference paper (2026 copyright)
- File: `raw-sources/2026-mahjourian-vlm-iris.pdf`
- Pages: 10
- Read-status: read (full paper)
- Retrieved: from `research to be indexed/` 2026-05-06

What it studies: can off-the-shelf vision-language foundation models (CLIP) be adapted to thermal infrared imagery without retraining, for zero-shot scene classification in additive manufacturing — specifically detecting whether a printed part is present on the build plate.

## Narrative

### The framework: VLM-IRIS

CLIP and other VLMs are trained on RGB image-text pairs from the public web. Thermal infrared images don't fit that distribution — they're single-channel intensity maps, and the kind of "scene" they describe (heat gradients) isn't in the training set. **VLM-IRIS is a preprocessing wrapper that bridges the modality gap**:

1. Capture IR via FLIR Boson thermal camera mounted top-down above print bed
2. Convert raw single-channel thermal data → 3-channel RGB representation. Three preprocessing options tested: grayscale, magma colormap, viridis colormap
3. Center-crop region of interest (0.50 fraction of smaller image dimension) to focus on build plate
4. Build a "prompt bank" — multiple natural-language descriptions per class (e.g. for `present`: "an infrared image showing a bright surface with a solid shape on it"; for `absent`: "infrared photo of a flat bright surface that is completely empty")
5. Encode all prompts and images into shared embedding space via CLIP ViT-B/32
6. Average prompt embeddings to form **class centroids** (prompt ensembling — reduces sensitivity to wording)
7. Classify image by max cosine similarity to centroid

The model is **never retrained or fine-tuned**. All inference runs on CPU.

### Hardware setup

- Prusa MK3S 3D printer (consumer-grade desktop)
- FLIR Boson thermal infrared camera mounted above build plate (top-down view)
- Test parts printed in **PETG** filament, nozzle 230°C, bed 85-110°C
- 200 images total, balanced across two classes × two thermal conditions:
  - Hot bed (~85°C) — 100 images
  - Room temperature bed (~34°C) — 100 images
- Parts varied in size (50-150 mm planar, 4-70 mm tall) and geometry

### Headline results

**Best configuration**: CLIP ViT-B/32 + magma colormap + centroid prompting at room temperature → **100% accuracy** (50/50 absent + 50/50 present, no errors).

| Condition | Preprocessing | Prompting | Accuracy |
|---|---|---|---|
| Hot bed | Grayscale | Centroid | 83% |
| Hot bed | Magma | Centroid | **92%** |
| Hot bed | Viridis | Centroid | 88% |
| Room temp | Grayscale | Centroid | 99% |
| Room temp | **Magma** | **Centroid** | **100%** |
| Room temp | Viridis | Centroid | 95% |

**Two consistent findings**:

1. **Centroid prompting > single-prompt** in every condition. Prompt ensembling reduces sensitivity to phrasing variation; this matters because zero-shot prompts are hand-written and inherently fragile.
2. **Hot bed is harder than room-temp**. When the bed and the part are both hot, the temperature contrast is small and gradual — boundaries appear soft. Room-temp bed has sharper contrast (cold bed, warm part still cooling) which CLIP's RGB-trained filters can recognize.

### Why magma > grayscale > viridis

- **Grayscale** preserves the true thermal signal but lacks color cues — CLIP's RGB-trained filters under-respond to single-channel grayscale unless contrast is sharp.
- **Magma colormap** introduces a structured RGB color gradient (dark purple → bright yellow) that mimics the kind of color statistics CLIP saw during pretraining. This produces more stable embeddings.
- **Viridis colormap** also helps but tends to introduce false positives — its green-yellow gradient creates artificial textures that CLIP misinterprets as object edges.

### Limitations

- **Binary task only.** Object present vs absent is a deliberately simple isolation of the modality-adaptation question. Doesn't address defects, multi-class scenarios, or geometric reasoning.
- **Fixed-camera assumption.** Top-down view of build plate; center-crop assumes known build-plate region. Generalizing to mobile or off-axis cameras requires localization mechanisms.
- **No fine-tuning baseline.** Authors don't compare zero-shot CLIP to a domain-fine-tuned thermal CLIP (would be expected to outperform but require data + compute).
- **Single backbone tested.** Only CLIP ViT-B/32. Authors acknowledge other VLMs (OpenCLIP, SigLIP, EVA-CLIP) may behave differently.
- **PETG-only material tested.** [TENTATIVE 2026-05-06] Different filaments (PLA, ABS) have different thermal emissivity which may affect results.

### Why this matters for a Bambu hobbyist

[TENTATIVE 2026-05-06] Practical translation: a cheap thermal camera (~$300 FLIR Boson, much less for non-radiometric sensors) plus a laptop running pretrained CLIP could provide **automation-grade build-plate monitoring without any model retraining**. For an Etsy-print-farm workflow this would mean: print finishes → IR camera confirms part is present → robot or operator removes part → next print queued. **Bambu's own AI failure detection is camera-based but RGB; this kind of zero-shot IR pipeline would extend monitoring to enclosed / dim chambers where RGB cameras struggle.**

[CONFIRMED] CLIP can be adapted to thermal IR data with magma preprocessing without retraining. [CONFIRMED] Centroid prompt ensembling is robust improvement over single prompts. [TENTATIVE] Generalization to non-PETG materials and other VLM backbones is plausible but not validated.

## Snippets

> "VLM-IRIS converts the infrared images to magma representation and applies centroid prompt ensembling with a CLIP ViT-B/32 encoder to achieve high accuracy on infrared images without any model retraining."
[Source: 2026-mahjourian-vlm-iris.pdf p.1 (abstract)]

> "Among all tested configurations, the best performance was achieved using magma preprocessing with centroid prompting on the room-temperature dataset, reaching 100% accuracy, precision, and recall."
[Source: 2026-mahjourian-vlm-iris.pdf p.6 (Section 4 Results)]

> "Across all preprocessing methods, the centroid prompting strategy performed better than using a single prompt. By averaging multiple text descriptions into one combined representation, the model becomes less sensitive to how each sentence is worded and produces more stable results."
[Source: 2026-mahjourian-vlm-iris.pdf p.7 (Section 5 Conclusions)]
