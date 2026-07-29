---
title: A Cost-Benefit Analysis of Additive Manufacturing as a Service
type: source
tags: [paper, business, MaaS, cloud, economics, cost-benefit, distributed-manufacturing, FDM]
keywords: [Cloud Crafting Platform, Manufacturing as a Service, MaaS, profit sharing, Microsoft Azure, OctoPi, Ultimaker 2+, Creality K1 MAX, Prusa MK4, Lancaster, Burgenland, Service-Oriented Architecture, SOA]
related:
  - concepts/am-as-a-service.md
  - concepts/print-farm-operations.md
  - concepts/ip-theft-3d-printing.md
  - concepts/g-code-protection.md
  - concepts/fdm-printing.md
  - sources/2025-wang-collaborative-parameter-recommender.md
  - sources/2025-surynek-sequential-printing-cegar.md
  - sources/2026-hatton-parallelobox-aabb-decomposition.md
  - sources/2026-corn-optimistic-verifiable-claims.md
maturity: draft
created: 2026-05-06
updated: 2026-07-29
read_status: deep-read
---

## Relations

@concepts/am-as-a-service.md @concepts/print-farm-operations.md @concepts/ip-theft-3d-printing.md @concepts/g-code-protection.md @concepts/fdm-printing.md @sources/2025-wang-collaborative-parameter-recommender.md @sources/2025-surynek-sequential-printing-cegar.md @sources/2026-hatton-parallelobox-aabb-decomposition.md @sources/2026-corn-optimistic-verifiable-claims.md

## Raw Concept

- Title: A Cost-Benefit Analysis of Additive Manufacturing as a Service
- Authors: Igor Ivkić (Lancaster University, UK), Tobias Buhmann (UAS Burgenland / Forschung Burgenland, AT), Burkhard List (b&mi, Wiesmath, AT)
- Type: arXiv preprint, arXiv:2502.05586v1 [cs.ET], 8 Feb 2025
- Location: `raw-sources/2025-ivkic-cost-benefit-maas.pdf`
- Retrieved: 2026-05-06
- Pages: 12
- Read-status: deep-read

## Narrative

Operational cost model for **on-demand, locally-distributed 3D printing as a service**. The "Cloud Crafting Platform" connects web-shops to small/medium 3D-print operators near the customer; product is printed *after* purchase, removing inventory risk. Tested end-to-end on Microsoft Azure with three real printers; gives concrete per-unit costs, profit-share split, and break-even thresholds.

**Five stakeholders:**
1. **Customer** — places the order
2. **Web-shop operator** — runs the storefront (e.g. Shopify Basic at €29/month + 2% transaction fee)
3. **Cloud Crafting Platform operator** — runs the SOA infrastructure on Azure (~€175/month all-in for API Gateway + Load Balancer + 4 core App Services)
4. **CAD model designer** — provides the product geometry
5. **3D printer operator (SME)** — produces the physical product locally

**Architecture (SOA on Azure)** [Source: 2025-ivkic-cost-benefit-maas.pdf p.6-7]:

- **API Gateway** — entry point for web shops
- **Cloud Gateway** — entry point for printer operators
- **Load Balancer** + **Discovery Service** — eliminate hardcoded service locations
- **Order Service** — order lifecycle management
- **Authentication/Authorization Service** — role-based access control
- **Printer Service** — schedules + queues print jobs, monitors connected printers
- **Billing Service** — transactions + profit-sharing distribution
- **Central database** — user profiles / orders / printer config / billing / promo codes

**Testbed** [Source: 2025-ivkic-cost-benefit-maas.pdf p.7]: three networked printers, each behind a Raspberry Pi running **OctoPi** OS for remote control + monitoring + secure Cloud-Gateway communication:

| Printer | Make/Model |
|---|---|
| Printer 1 | Ultimaker 2+ CONNECT |
| Printer 2 | Creality K1 MAX |
| Printer 3 | Prusa MK4 |

**Test product:** a **ring**. Per-printer production cost breakdown [Source: 2025-ivkic-cost-benefit-maas.pdf p.10 Table 2]:

| Printer | Pre-print | Print | Post-print | Total cost |
|---|---|---|---|---|
| Ultimaker 2+ CONNECT | 3:18 | 35:05 (77.93 W; €0.17 material) | 5:52 | **€0.197** |
| Creality K1 MAX | 4:14 | 9:06 (22.06 W; €0.07 material) | 0:10 | **€0.081** |
| Prusa MK4 | 4:47 | 10:40 (34.29 W; €0.09 material) | 0:46 | **€0.105** |

**Total cost per ring** = web-shop overhead (€0.29 amortized over 100 rings/month) + Azure infrastructure (€1.75 amortized) + production cost. Comes out to:
- Ultimaker route: **€2.237**
- Creality K1 MAX route: **€2.121**
- Prusa MK4 route: **€2.145**

At a market price of €10–15/ring, **profit margin ≈ 400–600%** [Source: 2025-ivkic-cost-benefit-maas.pdf p.10]. At 100 rings/month: monthly TCO €212–224, monthly revenue (at €10/ring) €1000, monthly profit ≈ €776–788.

**Profit-share model (weighted by responsibility / investment):**

| Stakeholder | Share | At 100 rings/mo |
|---|---|---|
| Cloud platform operator | **40%** | €310–315 |
| 3D printer operator | **30%** | €233–236 |
| Web-shop operator | **20%** | €155–158 |
| CAD model designer | **10%** | €78–79 |

[CONFIRMED] These are direct numbers from the paper's testbed. [TENTATIVE] Whether 100 rings/month is realistic on a single SME-operator basis depends on the product mix; rings are small and fast, larger goods would amortize the platform overhead differently.

**Bearing on the reader.** This is the closest published analog of the reader's eventual Etsy/MakerWorld store ops. Specific takeaways:
1. **Production cost per item is low** (€0.08–0.20 for a small PLA ring). The material is the big variable, not electricity.
2. **Cloud overhead (~€2 amortized) dominates production cost at small volumes** — only above ~50–100 prints/month does the per-unit cloud cost drop below the production cost.
3. **Profit share favors infrastructure providers, not designers.** A pure-designer Etsy seller (like the reader's likely starting position — designs but doesn't run a fleet) gets ~10% of value if they license through a MaaS platform vs ~100% if they sell STLs directly. **Direct-sale STLs > MaaS licensing for individual designers.**
4. **The Creality K1 MAX is meaningfully cheaper to operate** than the Ultimaker for the same product. Maps to the high-speed-FDM trend (faster machines = less time = less power).

**Security implications** [@concepts/ip-theft-3d-printing.md]: This MaaS architecture *is the threat model* of the security cluster. G-code travels over Azure to remote SME printers; a malicious printer-operator (Tier-2 or Tier-3 attacker per @concepts/ip-theft-3d-printing.md) has G-code in plaintext on their hardware. Ivkic doesn't address this. The matching defense is direct streaming + chunked STL [@concepts/g-code-protection.md] but the paper doesn't implement either.

## Snippets

> "The Cloud Crafting Platform follows a Service-Oriented Architecture (SOA) designed to ensure scalability, reliability, and seamless integration between web shops and 3D print shops. The architecture consists of two gateways, a central load balancer, and five core services that work together to enable the MaaS ecosystem."
[Source: 2025-ivkic-cost-benefit-maas.pdf p.6]

> "With a reasonable market price of €10-15 per ring, this results in a significant profit margin of around 400-600%, making it attractive to all stakeholders."
[Source: 2025-ivkic-cost-benefit-maas.pdf p.10]

> "Cloud Crafting Platform Operator (40%): receives the highest share due to platform maintenance and core service delivery. … 3D Printer Operator (30%): receives the second highest share for providing equipment and expertise including managing physical production and quality control. … Web Shop Operator (20%): … CAD Model Designer (10%): receives a share for creating the initial product designs (one-off contribution per product)."
[Source: 2025-ivkic-cost-benefit-maas.pdf p.10]
