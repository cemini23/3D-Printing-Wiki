---
title: "Optimistic Verifiable Claims: Blockchain Protocol for Confidential Bidding in Decentralized Manufacturing"
type: source
tags: [paper, security, blockchain, IP, G-code, MaaS, decentralized-manufacturing, Solidity]
keywords: [OVC, Optimistic Verifiable Claim, Arrow paradox, confidential bidding, Arbitrum, opBNB, Ethereum, 3DBenchy, filament consumption claim, Ljubljana]
related:
  - concepts/g-code-protection.md
  - concepts/ip-theft-3d-printing.md
  - concepts/am-as-a-service.md
  - concepts/fdm-printing.md
  - sources/2025-ivkic-cost-benefit-maas.md
  - sources/2026-asgar-firewall3d-firmware-hardware.md
maturity: draft
created: 2026-07-29
updated: 2026-07-29
read_status: skimmed
---

## Relations

@concepts/g-code-protection.md @concepts/ip-theft-3d-printing.md @concepts/am-as-a-service.md @concepts/fdm-printing.md @sources/2025-ivkic-cost-benefit-maas.md @sources/2026-asgar-firewall3d-firmware-hardware.md
- @cybersecurity-wiki/sources/2026-corn-optimistic-verifiable-claims.md  (cross-wiki stub)

## Raw Concept

- **Title:** Optimistic Verifiable Claims: A Blockchain Protocol for Conditionally Confidential Bidding in Decentralized Manufacturing
- **Authors:** Marko Corn, Nejc Rožman, Primož Podržaj (University of Ljubljana, Faculty of Mechanical Engineering)
- **Type:** arXiv preprint, arXiv:2607.25517v1 [cs.CR]
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/3d-printing/arxiv-2607.25517-optimistic-verifiable-claims-a-blockchain-protoc.pdf`
- **Retrieved:** 2026-07-29 overnight digest
- **Pages:** 61
- **Read-status:** skimmed (abstract, intro/contributions, lifecycle table, cost projections, conclusion)
- **Code:** https://github.com/fsprojekti/optimistic-verifiable-claims (MIT reproducibility package; Solidity + Hardhat)
- **DOI artifacts:** Zenodo https://doi.org/10.5281/zenodo.20794987

## Narrative

**Problem (Arrow’s information paradox in DM):** a Provider cannot price a print job without inspecting the design (e.g. filament length), but a Consumer cannot share G-code without exposing IP. Existing access-control / fair-exchange schemes protect *who can read* or *atomic delivery*, not the *veracity of claims* about a concealed artifact. [CONFIRMED — §1]

**OVC (Optimistic Verifiable Claim):** Consumer publishes a **verifiable claim** about a concealed design (material consumption, etc.). Providers bid on the claim without seeing the file. Claim stands unless challenged; challenge triggers deterministic on-chain predicate. Design disclosed only on dispute path — never on the honest path. [CONFIRMED — abstract]

### Four claim instances (Solidity) [CONFIRMED — §3 / README]

| Instance | Asserts | Dispute predicate |
|----------|---------|-------------------|
| **OVC-Access** | Decryption key correctly wrapped for Provider | `keccak256(K ∥ providerKeyHash) == commitment` |
| **OVC-Identity** | Ciphertext is `G ⊕ K` | rolling hash of `G ⊕ K` |
| **OVC-Conformance** | Artifact is syntactically valid G-code | scan for `G0`/`G1` |
| **OVC-Feature** | Declared feature (e.g. filament consumption) matches G | machine-model net extrusion |

Lifecycle phases covered: **Bidding → Binding → Specification Handover** (pre-contractual). Execution / delivery / settlement left to surrounding marketplace. [CONFIRMED — Table 1]

### Economics (3DBenchy 6.41 MB) [CONFIRMED — abstract]

| Path | Ethereum | Arbitrum | opBNB |
|------|----------|----------|-------|
| No dispute | ~$7,207 / ≤9 h | ~$288 / 3 min | ~$2.87 / 2 min |
| Fully contested | ~$49,660 / ≤57 h | ~$1,988 / 19 min | ~$19.73 / 13 min |

50 MB industrial: undisputed ~$56k / 3 days on Ethereum vs ~$22 / 16 min on opBNB. **Verdict:** economically feasible on Arbitrum/opBNB; not on Ethereum at industrial scale. Material-consumption (**Feature**) check is costliest. [CONFIRMED — abstract + §5.1]

Segmentation across chunked txs is required: single-transaction gas ceiling ~tens of KB — far below real G-code sizes. [CONFIRMED — §5.1]

### Scope limits [CONFIRMED — §5–6]

- Confidentiality is **optimistic** — a counterparty forcing disclosure can compel witness reveal (Consumer may **Withhold** and forgo the contract).
- Predicates are lightweight (syntax / declared parameter), not full manufacturability or print quality.
- ZK adjudication called out as future work (disclosure-free dispute).

### Phase-0 (2026-07-29)

| Check | Result |
|-------|--------|
| Repo | https://github.com/fsprojekti/optimistic-verifiable-claims — 0★, MIT, ~3 MB, Hardhat/Solidity reproducibility |
| Domain fit | Pre-contractual IP confidentiality for MaaS / decentralized AM — high for security + MaaS hubs |
| Failure mode | Chain cost / L2 dependency; not a hobby LAN defense; disclosure under dispute |
| Hobby / friend | **NO-GO** — research smart contracts, not Bambu/Orca day-1 |
| Verdict | **REFERENCE** — cite for G-code protection / MaaS IP deadlock; do not deploy as Tier-1 defense |
| Local adopt (&lt;500 MB) | **Skipped** — Solidity repro only; no FDM tooling value from `npm install` |

Cross-wiki: cybersecurity stub for blockchain / smart-contract adjudication of manufacturing claims.

## Snippets

> "We introduce the Optimistic Verifiable Claim (OVC), a blockchain protocol that lets a Consumer publish a verifiable claim about a concealed design (such as the material it consumes) and a Provider price and bid on it without seeing the design."
[Source: arXiv:2607.25517v1 abstract]

> "OVC makes confidential, claim-based bidding economically feasible on Arbitrum and opBNB, but not on Ethereum at industrial scale."
[Source: arXiv:2607.25517v1 abstract]

> "The claim is committed when the service is posted and stands unless the selected Provider challenges it; a challenge triggers a deterministic on-chain check that exposes any dishonesty, and the design is disclosed only to settle a dispute, never on the honest path."
[Source: arXiv:2607.25517v1 abstract]
