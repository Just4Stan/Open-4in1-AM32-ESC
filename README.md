# Open 4-in-1 AM32 ESC

An open-source 4-in-1 ESC for FPV drones. Runs [AM32](https://github.com/AlkaMotors/AM32-MultiRotor-ESC-firmware) firmware, works with Betaflight over DShot. Designed in KiCad 9, ready to order from JLCPCB.

I made a video explaining how it works: https://www.youtube.com/watch?v=TwAmmPxOpTM

<img width="622" height="678" alt="Screenshot 2026-03-09 at 21 01 59" src="https://github.com/user-attachments/assets/40ab86d7-e7c2-46e8-b2fc-61c8ba19fa80" />
<img width="604" height="640" alt="Screenshot 2026-03-09 at 21 02 12" src="https://github.com/user-attachments/assets/c0d8b194-cb31-4f07-9650-9fd69ad4cd7d" />

## Specs

| Parameter | Value |
|---|---|
| Firmware | AM32 |
| Input voltage | 3-6S LiPo (11.1-25.2V) |
| Continuous current | 35A per channel |
| MCU | AT32F421G8U7 (ARM Cortex-M4, 120MHz) |
| Gate driver | NSG2065Q (3-phase) |
| MOSFETs | SP40N03GNJ (40V/75A, 2.9mOhm RDS(on)) |
| Current sensing | INA199A1DCKR + 0.2mOhm shunt |
| Protocol | DShot (Betaflight compatible) |
| Power supply | LMR51420YDDCR buck + TPS746-3.3DRV LDO |
| Connector | HC-1.0-8PWT (8-pin) |
| PCB | 6-layer, designed for JLCPCB PCBA |

## How it's built

The schematic is split into a main sheet and a sub-sheet that's reused 4 times — one per ESC channel.

The main sheet (`4in1ESC.kicad_sch`) has the power supply, current sensing, and the 8-pin connector. Each ESC channel (`ESC.kicad_sch`) has:
- AT32F421G8U7 running AM32 firmware
- NSG2065Q 3-phase gate driver with bootstrap caps
- 6x SP40N03GNJ MOSFETs in 3 half-bridges
- Back-EMF feedback network for sensorless commutation

## Ordering from JLCPCB

Production files are in the `production/` folder:
- `v0.3.zip` — Gerber files
- `bom.csv` — Bill of Materials with LCSC part numbers
- `positions.csv` — Component placement for PCBA

## Project structure

```
4in1ESC.kicad_sch     Main schematic (power, sensing, connector)
ESC.kicad_sch         Single ESC channel (used 4x)
4in1ESC.kicad_pcb     PCB layout
4in1ESC.pretty/       Custom footprints
components.kicad_sym  Custom symbols (gate driver, connector, etc.)
production/           JLCPCB fabrication files
```

## TODO

- [ ] Fix current sensing circuit (INA199A1DCKR)
- [ ] Get AM32 certified ([AM32 Discord](https://discord.gg/am32))
- [✓] Switch to [Betaflight Connector Standard](https://betaflight.com/docs/development/manufacturer/connector-standard) — 8-pin JST-SH with standard pinout (VBAT, GND, Current, Telemetry, Signal 1-4)
- [ ] Evaluate Betaflight 10-pin variant for dual power/ground pins

## License

Licensed under [CERN-OHL-S-2.0](https://ohwr.org/cern_ohl_s_v2.txt). You can use, modify, and sell this design, but any modifications must also be open-sourced under the same license.
