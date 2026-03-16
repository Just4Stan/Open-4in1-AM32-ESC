# Pin-Compatible Alternatives — 4in1 ESC

Supply chain redundancy guide. All parts verified pin-compatible with the current PCB layout unless noted.

## Gate Drivers (QFN-24, 4x4mm)

All FD6288Q-family clones share **identical pinout** with the NSG2065Q. No PCB changes needed.

| Pin | Function |
|-----|----------|
| 1-3 | LIN1-3 (low-side inputs) |
| 4 | VCC (5-20V supply) |
| 5 | NC (MODE on DRV8300) |
| 6 | COM/GND |
| 7-8 | NC |
| 9-11 | LO3-LO1 (low-side outputs) |
| 12-14 | VS3, HO3, VB3 (phase 3 high-side) |
| 15-17 | VS2, HO2, VB2 (phase 2 high-side) |
| 18-20 | VS1, HO1, VB1 (phase 1 high-side) |
| 21 | NC (DT on DRV8300) |
| 22-24 | HIN1-3 (high-side inputs) |
| EP | GND |

### Drop-in Replacements (zero changes)

| Part | LCSC | Mfg | Source/Sink | Stock | Price | Datasheet |
|------|------|-----|-------------|-------|-------|-----------|
| **NSG2065Q** | C41414478 | WXNSIC | 1.5A/1.2A | ~225 | $0.44 | NSG2065Q_datasheet.pdf |
| **6288Q-MNS** | C49424413 | Minos | 1.3A/1.0A | **9,890** | $0.30 | 6288Q-MNS_Minos_datasheet.pdf |
| **SD6288Q** | C44606223 | JSMSEMI | 1.5A/1.0A | 5,045 | $0.31 | SD6288Q_JSMSEMI_datasheet.pdf |
| **EG2124** | C2856308 | EG Micro | 0.8A/1.2A | 3,821 | $0.23 | EG2124_datasheet.pdf |
| **HL6288Q** | C50331902 | HL | 1.5A/1.8A | 3,272 | $0.19 | HL6288Q_datasheet.pdf |
| **YC6288Q** | C54157432 | YLPTEC | — | 2,946 | $0.42 | YC6288Q_YLPTEC_datasheet.pdf |
| **JSM6288Q** | C19077370 | JSMSEMI | 1.5A/1.8A | 1,989 | $0.46 | JSM6288Q_JSMSEMI_datasheet.pdf |

**Combined stock: ~27,000+ units** across all clones.

### DRV8300 (TI) — Layout-Compatible with Caveats

| Part | LCSC | Stock | Price |
|------|------|-------|-------|
| **DRV8300DRGER** | C3655801 | 53 | $0.38 |

Pin differences vs FD6288Q family:
- **Pin 5 = MODE** (internal 200k pulldown → floats to non-inverting = same behavior as FD6288 family). **Safe to leave NC.**
- **Pin 21 = DT** (floating = fixed ~215ns deadtime). **Safe to leave NC.**
- Source current only 750mA (vs 1.5A on most clones) — slower MOSFET turn-on
- Max 100V (vs 250V on FD6288 family) — fine for LiPo, less transient headroom
- LCSC stock is terrible (53 units)

**Verdict:** Works on the same pads, no PCB changes needed. Not recommended as primary due to low stock and weaker drive. Good as emergency fallback.

### FD6288Q (Fortior, original) — Discontinued

All QFN-24 variants OOS on LCSC. Only FD6288T (TSSOP-20, C97683, 34k stock) available — wrong package.

### NSG20652Q — NOT Compatible

QFN-24 4x4mm but **completely different pinout** with added SD pin. For 30x30 variant only (separate repo/board).

---

## MOSFETs — 20x20 Variant (3x3mm / 3.3x3.3mm DFN-8)

Current part: **SP40N03GNJ** (C22466709) — 40V, 75A, 2.9mΩ, $0.10

### 40V Alternatives — Sorted by Performance

| Part | LCSC | Mfg | RDS(on) | Id | Pkg (mm) | Stock | Price |
|------|------|-----|---------|----|----------|-------|-------|
| **BSZ018N04LS6** | C534643 | Infineon | **1.8mΩ** | 158A | 3.3x3.3 | 935 | $0.81 |
| **NCEP4065QU** | C502974 | Wuxi NCE | **2.2mΩ** | 65A | 3.1x3.2 | **6,152** | $0.44 |
| **AON7140** | C2758662 | AOS | **2.3mΩ** | 148A | 3.3x3.3 | 3,767 | $0.96 |
| **BSZ025N04LS** | C534648 | Infineon | 2.5mΩ | 22A | 3.3x3.3 | 3,834 | $0.87 |
| **APG035N04Q** | C5443653 | ALLPOWER | 2.8mΩ | 100A | 3.0x3.0 | 3,608 | $0.48 |
| **BSZ028N04LS** | C534649 | Infineon | 2.8mΩ | 40A | 3.3x3.3 | 1,595 | $0.88 |
| **SP40N03GNJ** | C22466709 | Siliup | 2.9mΩ | 75A | 3.0x3.0 | 2,125 | **$0.10** |

### 30V Premium Alternative — FDMC8010DC

| Part | LCSC | Mfg | RDS(on) | Id | Qg | Pkg (mm) | Stock | Price |
|------|------|-----|---------|----|-----|----------|-------|-------|
| **FDMC8010DC** | C555489 | onsemi | **1.28mΩ@10V** | 157A | 67nC | PQFN-8 (3.3x3.3) | 2,965 | $0.90 |

**Trade-offs vs SP40N03GNJ:**
- **56% lower RDS(on)** — 1.28mΩ vs 2.9mΩ. Per-phase MOSFET loss drops from 5.8mΩ (2×2.9) to 2.56mΩ (2×1.28)
- **36% lower total phase resistance** — ~5.8mΩ vs ~9.0mΩ including ~3.2mΩ copper (3mm wide × 10mm, 1oz)
- **9× more expensive** — $0.90 vs $0.10 per FET, $21.60 vs $2.40 for all 24
- **30V Vds** — max 7S LiPo (29.4V) vs 40V on SP40N03GNJ which handles 8S+ with margin. Limits battery voltage headroom and transient margin on 6S
- **3.3x3.3mm package** — needs footprint update from current 3.0x3.0mm POWERPAK-1212-8
- **Higher Qg** (67nC vs ~35nC) — more gate charge means slightly higher switching losses, partially offsets conduction gains at high PWM frequencies

**Verdict:** Advertise as an optional premium build for users who want maximum efficiency on 3-6S and are willing to pay more. Not the default due to cost and reduced voltage headroom. Requires footprint change to 3.3x3.3mm PQFN-8.

### Other 30V Low-RDS Alternatives (3.3x3.3mm DFN-8)

| Part | LCSC | Mfg | RDS(on) | Id | Qg | Stock | Price |
|------|------|-----|---------|----|-----|-------|-------|
| **BSZ0901NS** | C534685 | Infineon | **1.7mΩ@10V** | 145A | 23nC | 4,035 | $0.74 |
| **NCEP3065QU** | C502964 | Wuxi NCE | **1.9mΩ@10V** | 65A | 34.8nC | 2,356 | $0.40 |
| **BSZ019N03LS** | C152374 | Infineon | 1.9mΩ@10V | 22A | — | 2,654 | $1.25 |

All 30V parts share the same trade-off: lower RDS(on) but reduced voltage headroom (max 7S) and require 3.3x3.3mm footprint.

### Verify Footprint Fit

The current footprint (POWERPAK-1212-8) is 3.0x3.0mm. All 3.3x3.3mm parts (BSZ, AON, FDMC8010DC, NCEP3065QU) need footprint verification — pad pitch and layout could differ slightly. **Check datasheets before assuming drop-in compatibility with 3.3mm parts.**

### Ohmic Loss Analysis (3mm trace width, 10mm trace length, 1oz copper, 80°C)

Per-phase current path: copper (bat + GND ≈ 3.2mΩ) + 2 MOSFETs (high + low side).

**SP40N03GNJ @ 35A (1oz):**

| Loss Source | Resistance | Power |
|-------------|-----------|-------|
| 2x MOSFET (2.9mΩ each) | 5.8 mΩ | 7.1W (64%) |
| Copper (bat + GND) | 3.2 mΩ | 3.9W (36%) |
| **Total** | **9.0 mΩ** | **11.0W** |

**FDMC8010DC @ 35A (1oz):**

| Loss Source | Resistance | Power |
|-------------|-----------|-------|
| 2x MOSFET (1.28mΩ each) | 2.56 mΩ | 3.1W (44%) |
| Copper (bat + GND) | 3.2 mΩ | 3.9W (56%) |
| **Total** | **5.8 mΩ** | **7.1W** |

FDMC8010DC saves ~3.9W per phase at 35A (36% reduction). MOSFETs are the dominant loss in both cases on this board geometry. 2oz outer copper (JLCPCB supports 2oz/2oz outers on 6-layer) would further reduce copper losses but requires all B.Cu traces to meet 0.15mm minimum width.

---

## MOSFETs — 30x30 Variant (larger packages OK)

### PSMN1R6-40YLC (Nexperia) — Target Part

| Parameter | Value |
|-----------|-------|
| Vds | 40V |
| RDS(on) | **1.25mΩ** @10V, **1.55mΩ** @4.5V |
| Id | 100A |
| Qg | 59nC @4.5V |
| Package | **LFPAK56 (5x6mm)** — NOT 3x3mm |
| LCSC | **Not stocked** |

**Status: Discontinued/unavailable on LCSC.** Closest available:

| Part | LCSC | RDS(on) | Qg | Stock | Price |
|------|------|---------|----|-------|-------|
| PSMN1R8-40YLC | C88071 | 1.8mΩ @4.5V | 45nC | 94 | $1.33 |
| PSMN1R5-40YSDX | C553230 | 1.5mΩ @10V | 99nC | 50 | — |

Stock is terrible for all Nexperia 40V LFPAK56 on LCSC. May need to source from DigiKey/Mouser for the 30x30 variant, or find Chinese equivalents in LFPAK56.

---

## Design Changes for Universal Gate Driver Support

**Current state:** Pins 5, 7, 8, 21 are NC with no copper on all 4 gate driver instances (U3, U7, U9, U11). VCC on +8V, COM/EP on GND.

**Required changes: NONE.** The current PCB already supports all listed gate drivers:
- FD6288Q clones: Pins 5/7/8/21 = NC → no conflict
- DRV8300: Pin 5 (MODE) floats low via internal pulldown → non-inverting (correct). Pin 21 (DT) floating → fixed 215ns deadtime (acceptable)
- All signal pins (1-3, 9-20, 22-24) are functionally identical across all parts

**Optional improvement:** Add unpopulated 0402 resistor pad from pin 21 to GND. This enables variable deadtime when using DRV8300 without affecting other drivers. Low priority.

---

*Last updated: 2026-03-14. Stock numbers are approximate — verify on lcsc.com before ordering.*
