---
title: "Firewall3D: A Hardware Firewall for Defending 3D Printers Against Firmware Attacks"
type: source
tags: [paper, security, defense, firmware, hardware, physical-layer, FDM]
keywords: [Firewall3D, STM32, bump-in-the-wire, stepper current, endstop, thermal runaway, Texas A&M, Ghazi Asgar, Reddy]
related:
  - sources/2026-asgar-quietprint-acoustic-defense.md
  - concepts/g-code-protection.md
  - concepts/side-channel-attacks.md
  - concepts/ip-theft-3d-printing.md
  - concepts/fdm-printing.md
  - sources/2026-yocam-amnc-bambu-side-channel.md
  - sources/2026-arxiv-lane-noise-triage-jul15.md
  - sources/2026-arxiv-lane-noise-triage-jul18.md
maturity: draft
created: 2026-07-15
updated: 2026-07-18
read_status: skimmed
---

## Relations
- @cybersecurity-wiki/sources/2026-asgar-firewall3d-firmware-hardware.md  (cross-wiki stub)

@sources/2026-asgar-quietprint-acoustic-defense.md @concepts/g-code-protection.md @concepts/side-channel-attacks.md @concepts/ip-theft-3d-printing.md @concepts/fdm-printing.md @sources/2026-yocam-amnc-bambu-side-channel.md @sources/2026-arxiv-lane-noise-triage-jul15.md

## Raw Concept

- **Title:** Firewall3D: A Hardware Firewall for Defending 3D Printers Against Firmware Attacks
- **Authors:** Seyed Ali Ghazi Asgar, Narasimha Reddy (Texas A&M ECE)
- **Type:** arXiv preprint, arXiv:2607.10484v1 [cs.CR]
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2607.10484-firewall3d-a-hardware-firewall-for-defending-3d.pdf`
- **Retrieved:** 2026-07-15 (overnight digest auto-fetch)
- **Pages:** 31
- **Read-status:** skimmed (abstract + threat model + hardware + defense scenarios + limitations)
- **Same lab as QuietPrint** (@sources/2026-asgar-quietprint-acoustic-defense.md) — follow-on from acoustic SHM to **firmware / physical-layer** defense

## Narrative

**Firewall3D** is a dedicated **bump-in-the-wire hardware firewall** that sits between a consumer FDM motherboard and its sensors/actuators. It independently measures stepper-motor currents, endstop switches, hotend/bed temperatures, and cooling-fan PWM, then checks that physical behavior matches intended G-code execution. On anomaly it can **alarm and halt** the print.

### Threat model [CONFIRMED — paper §3]

Assumes the motherboard may be compromised via supply-chain implant, malicious firmware update, or insider flash. Attacker goals: sabotage part strength (cavity tilt, extrusion-width variation), damage the machine (thermal runaway / fan-off nozzle melt), or leak IP via modulated physical channels (e.g. fan-speed acoustic encoding). Defense assumes physical access to install Firewall3D wiring; **does not** assume an attacker who can modify Firewall3D itself.

### Architecture [CONFIRMED — paper §4]

| Element | Role |
|---------|------|
| Custom PCB + MCU (STM32 in implementation) | Real-time ADC/timer sampling (~4 kHz on stepper channels) |
| Inline current sensors (200 mV/A class) | Decode coil currents → angle via `atan2` → displacement / speed |
| Buffer + pull-down sense on NTC | Hotend temp without disrupting mainboard PID |
| PWM→DC RC filter | Fan duty / bed heater duty |
| Optocoupler on LED/toggle pin | Motion start/stop framing (requires G-code `M355` toggle pattern — Listing 1.1) |
| Optional host PC (MCP2221A USB-serial) | Higher-level G-code sanity scripts; MCU stays real-time |

Speed estimation: &lt;1% max error at 2500 mm/min on 20 mm moves in their test set [TENTATIVE — single lab printer; topology not Bambu CoreXY].

### Attack classes demonstrated with detection [CONFIRMED — paper §6]

1. **Motion length** — commanded 30 mm square; attack executes 25 mm → Firewall3D flags mismatch (Fig. 11).
2. **Motion speed** — edge drop 1500→1000 mm/min detected (Fig. 12).
3. **Thermal setpoint** — firmware silently drops nozzle 210→150°C; alert when outside β≈10% band after expected wait `t_wait = γ(T_set−T_current)/α`.
4. **Cooling fan** — unexpected drop to 0% duty → alert.
5. **Endstop / homing cheat** — firmware claims calibrated without ON-OFF-ON-OFF endstop pattern → halt.

Not a software SHM / AMNC competitor: QuietPrint/AMNC address **emanation** side channels; Firewall3D addresses **compromised firmware lying about what the machine did**. Complementary layer on the coverage matrix (@concepts/g-code-protection.md).

### Phase-0 (tool / adoption audit) — 2026-07-15

| Check | Result |
|-------|--------|
| License / public repo | **None found** in paper — no GitHub URL; custom PCB research artifact |
| Domain fit | AM firmware / OT physical integrity — high wiki relevance |
| Failure mode | Requires invasive wiring; G-code must emit motion framing pin toggles; not plug-and-play on closed Bambu appliances |
| Hobby laptop adopt | **NO-GO** — no released firmware/BOM to install; &gt;research cost; voids typical consumer warranties |
| Verdict | **REFERENCE** — cite for defense landscape; do **not** local-clone or recommend building for day-1 friend reader / Bambu X1C |

Cross-wiki: also stubbed on `@cybersecurity-wiki` (embedded / OT hardware monitoring).

### Practical bearing

- **Bambu / Flashforge daily use:** stay on LAN-only, vendor firmware, no custom motherboard intercept. Firewall3D is research-grade for open Marlin/Klipper-class boards with accessible harnesses.
- **Print-farm / MaaS threat (Tier 2–3):** strongest conceptual match — independent physical attestation that G-code ≡ motion/thermal reality even when motherboard is untrusted.
- Follow QuietPrint lineage from same authors when synthesizing Asgar/Reddy defense stack.

## Snippets

> "Firewall3D continuously monitors physical layer signals, including stepper motor currents, end stop switches, nozzle and bed temperatures and cooling fans, to verify that the printer’s physical behavior matches the intended G-code execution."
[Source: arXiv:2607.10484v1 abstract]

> "Our approach does not require any modifications to the printer’s motherboard or firmware, as it operates using only minimal additional wiring."
[Source: arXiv:2607.10484v1 §3]

> "We do not consider an attacker capable of modifying our setup or altering the Firewall3D firmware."
[Source: arXiv:2607.10484v1 §7 Limitations]

## Dead Ends

- Local adoption attempt: **skipped** — no public BOM/gerbers/firmware release at Phase-0; building from paper figures alone is out of scope for this wiki.
