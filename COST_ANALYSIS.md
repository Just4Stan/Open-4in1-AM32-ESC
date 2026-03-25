# 4-in-1 ESC Cost Analysis (JLCPCB)

Generated: 2026-03-17

## Board Specs
- 6-layer PCB, 30.5 × 32.2 mm
- 187 components (21 unique part types)
- Both-sides assembly

---

## Complete BOM (all 21 parts, 500 boards)

| # | Component | LCSC | Qty/board | Total qty | Unit Price | 500-board Total | % of BOM |
|---|-----------|------|-----------|-----------|------------|-----------------|----------|
| 1 | SP40N03GNJ (MOSFET) | C22466709 | 24 | 12,000 | €0.110 | €1,320.00 | 30.0% |
| 2 | AT32F421G8U7 (MCU) | C2765098 | 4 | 2,000 | €0.414 | €827.41 | 18.8% |
| 3 | 10uF 0805 50V (cap) | C440198 | 33 | 16,500 | €0.037 | €606.29 | 13.8% |
| 4 | NSG2065Q (gate driver) | C41414478 | 4 | 2,000 | €0.231 | €462.74 | 10.5% |
| 5 | LMR51420YDDCR (buck) | C7296200 | 1 | 500 | €0.770 | €384.84 | 8.8% |
| 6 | INA186A3IDCKR (CSA) | C2058245 | 1 | 500 | €0.509 | €254.73 | 5.8% |
| 7 | 0.2mΩ 2512 (shunt) | C695806 | 1 | 500 | €0.194 | €96.95 | 2.2% |
| 8 | SM08B-SRSS-TB (JST) | C160407 | 1 | 500 | €0.163 | €81.26 | 1.8% |
| 9 | TLV76733DRVR (LDO) | C2848334 | 1 | 500 | €0.115 | €57.36 | 1.3% |
| 10 | 100nF 0201 (cap) | C181043 | 22 | 11,000 | €0.005 | €54.54 | 1.2% |
| 11 | XRIM 470nH (inductor) | C48391583 | 1 | 500 | €0.073 | €36.44 | 0.8% |
| 12 | 22uF 0402 (cap) | C105226 | 2 | 1,000 | €0.026 | €26.26 | 0.6% |
| 13 | 22uF 0603 (cap) | C2762594 | 2 | 1,000 | €0.025 | €25.30 | 0.6% |
| 14 | BLM03PX121SN1D (ferrite) | C525479 | 4 | 2,000 | €0.010 | €20.28 | 0.5% |
| 15 | 100nF 0402 (cap) | C307331 | 12 | 6,000 | €0.002 | €14.10 | 0.3% |
| 16 | 10kΩ 0201 | C473048 | 33 | 16,500 | €0.0008 | €12.93 | 0.3% |
| 17 | 15Ω 0201 | C473542 | 24 | 12,000 | €0.0004 | €5.22 | 0.1% |
| 18 | 1kΩ 0201 | C270365 | 13 | 6,500 | €0.0005 | €3.40 | 0.1% |
| 19 | 220Ω 0201 | C473535 | 4 | 2,000 | €0.0006 | €1.19 | 0.0% |
| 20 | 124kΩ 0201 | C423759 | 1 | 500 | €0.0007 | €0.35 | 0.0% |
| | **BOM TOTAL** | | **187** | | | **€4,291.49** | **100%** |

**Per-board BOM: €8.58**

Note: U4 (4in1ESC module) is a schematic reference, not a purchasable part. Test points are bare pads.

---

## Full Cost Breakdown @ 500 boards

| Category | Cost | Per Board |
|----------|------|-----------|
| **PCB Fabrication** | €212.86 | €0.43 |
| — Engineering fee | €28.68 | |
| — Board | €54.93 | |
| — Min via hole size/diameter | €50.88 | |
| — Large size | €29.55 | |
| — 4-wire Kelvin test | €20.18 | |
| — Surface finish | €11.82 | |
| — Board outline tolerance | €10.84 | |
| — Material type | €5.08 | |
| — Confirm production file | €0.90 | |
| **Assembly (non-BOM)** | €397.83 | €0.80 |
| — SMT placement | €176.67 | |
| — Nitrogen reflow | €85.26 | |
| — Large size surcharge | €49.57 | |
| — Setup fee | €44.10 | |
| — Feeders loading (Extended parts) | €19.82 | |
| — Stencil | €14.17 | |
| — Photo confirmation | €7.08 | |
| — Board cleaning | €0.70 | |
| — Packaging | €0.45 | |
| **Build time surcharge** | €42.49 | €0.08 |
| **BOM (all 21 parts)** | €4,291.49 | €8.58 |
| | | |
| **GRAND TOTAL** | **€4,944.67** | **€9.89** |

### Cost Distribution

- BOM (materials): 86.8%
- Assembly (labor): 8.0%
- PCB (bare board): 4.3%
- Build time: 0.9%

---

## Scaling Analysis

| Quantity | PCB | Assembly | BOM | Total | Per Board |
|----------|-----|----------|-----|-------|-----------|
| 100 | ~€150 | ~€300 | ~€858 | ~€1,308 | **~€13.08** |
| 250 | ~€180 | ~€350 | ~€2,146 | ~€2,676 | **~€10.70** |
| **500** | **€213** | **€440** | **€4,292** | **€4,945** | **€9.89** |
| 1,000 | ~€350 | ~€650 | ~€8,200 | ~€9,200 | **~€9.20** |
| 2,500 | ~€650 | ~€1,200 | ~€19,000 | ~€20,850 | **~€8.34** |
| 5,000 | ~€1,100 | ~€2,000 | ~€35,000 | ~€38,100 | **~€7.62** |
| 10,000 | ~€1,800 | ~€3,500 | ~€62,000 | ~€67,300 | **~€6.73** |

Estimates based on JLCPCB volume pricing curves. BOM gets ~15-20% cheaper at 10k+ due to volume discounts on MOSFETs, MCUs, and caps.

Fixed costs (PCB+assembly) are noise above 500 units. BOM is 87-92% of total cost at production volumes.

---

## Top 5 Cost Drivers (72% of BOM)

1. **MOSFETs** (€1,320 / 30%) — 24 per board at €0.11 each
2. **MCUs** (€827 / 19%) — 4 per board at €0.41 each. Already cheapest AM32-compatible option.
3. **10uF 0805 caps** (€606 / 14%) — 33 per board. Already Basic part.
4. **Gate drivers** (€463 / 11%) — 4 per board at €0.23 each. Many clone alternatives exist.
5. **Buck converter** (€385 / 9%) — 1 per board at €0.77. Only SOT-23-6 option at 36V/2A.

---

## Supply Chain Status (JLCPCB Global Sourcing Needed)

| Part | Qty for 500 | JLCPCB Stock | LCSC Stock | Shortfall | Risk |
|------|-------------|-------------|------------|-----------|------|
| SP40N03GNJ | 12,000 | 2,340 | 12,014 | 9,674 | **Medium** — LCSC has enough total |
| 10kΩ 0201 | 16,500 | 536 | 1.1M+ | 15,979 | **Low** — massive LCSC stock |
| 220Ω 0201 | 2,000 | 67 | 10k+ | 1,943 | **Low** — adequate LCSC stock |
| NSG2065Q | 2,000 | 215 | ~225 | 1,785 | **High** — only ~225 on LCSC. Use clone 6288Q-MNS (9.9k stock) as fallback |
| LMR51420 | 500 | 416 | ~700 | 84 | **Medium** — tight but sourceable. Multiple variants. |

---

## Alternative Component Research

### MCU: AT32F421G8U7 — KEEP

Already the cheapest AM32-compatible MCU in QFN-28 4x4mm at ~$0.475/unit.
- GD32E230G8U6TR ($0.448) has only 8KB SRAM (insufficient, 16KB required)
- STM32G071G8U6 ($0.78) is 65% more expensive
- No alternatives are pin-compatible — switching requires full board redesign
- Stock: 11,330 units on LCSC, enough for multiple runs

### Buck: LMR51420YDDCR — KEEP (source via JLCPCB global)

Only SOT-23-6 buck converter at 36V input / 2A output on LCSC.
- LMR51420XDDCR (C5246146, 500kHz variant): pin-compatible, $0.82, 183 stock
- LMR51420YFDDCR (C7296200, JLCPCB variant): pin-compatible, $0.72
- AOZ1282CI (C111916): $0.22, 9k stock, 36V — but only 1.2A and different pinout (requires PCB rework)
- AP63200 family: $0.20-0.41, 2A — but only 32V max (unsafe for 6S with transients)
- Recommendation: keep LMR51420, order through JLCPCB global sourcing

### Current Sense Amp: INA186A3IDCKR — MONITOR

Stock critically low (74 units as of 2026-03-17). No Chinese clones exist.
- INA199A2DCKR (C131913): $0.248 (52% cheaper), same SC-70-6 footprint, 909 stock, bidirectional, zero-drift — but **26V common-mode limit** (tight for 6S at 25.2V, no transient margin)
- INA180A3IDBVR (C122882): $0.154 (70% cheaper), SOT-23-5 (different footprint), unidirectional only, 4,875 stock
- 3PEAK TP181A2-CR (C2902350): $0.10, SC-70-6, 36V CM, INA199 pinout — **currently OOS**, monitor for restock
- For V1: source INA186A3 via JLCPCB global. For V2: consider INA199A2 if 26V CM is acceptable.

### Passives — Minor Optimizations Available

All 0201 parts are Extended (no 0201 Basic parts exist on JLCPCB).

Potential drop-in savings (no layout change):
| Swap | From → To | Savings (500 boards) | Notes |
|------|-----------|---------------------|-------|
| 100nF 0201 35V → 6.3V | C181043 → C76928 | €73 | Murata, safe for 3.3V/5V decoupling |
| 22uF 0402 | C105226 → C415703 | €37 | Murata, same voltage, 63% cheaper |
| 22uF 0603 16V → 6.3V | C2762594 → C59461 | €24 | Samsung, BASIC. Verify voltage rail. |
| Shunt redesign | 0.2mΩ → 2mΩ + INA186A1 | €93 | Requires CSA gain change |
| **Total potential** | | **~€227** | |

These are minor (~5% of BOM) and require verification of voltage rails before implementing.

---

## Summary

| Metric | Value |
|--------|-------|
| Per-board cost @ 500 | **€9.89** |
| Per-board BOM only | **€8.58** |
| Per-board cost @ 1,000 | **~€9.20** |
| Per-board cost @ 5,000 | **~€7.62** |
| Per-board cost @ 10,000 | **~€6.73** |
| BOM as % of total | 87% |
| Unique Extended parts | 18 of 21 |
| Parts needing global sourcing | 5 of 21 |
| Highest risk part | NSG2065Q (gate driver) — 225 total LCSC stock |
