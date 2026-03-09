# Open 4-in-1 ESC

An open-source 4-in-1 Electronic Speed Controller (ESC) for FPV drones, designed in KiCad 9.

<img width="622" height="678" alt="Screenshot 2026-03-09 at 21 01 59" src="https://github.com/user-attachments/assets/40ab86d7-e7c2-46e8-b2fc-61c8ba19fa80" />
<img width="604" height="640" alt="Screenshot 2026-03-09 at 21 02 12" src="https://github.com/user-attachments/assets/c0d8b194-cb31-4f07-9650-9fd69ad4cd7d" />

## Specs

| Parameter | Value |
|---|---|
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

## Architecture

The design uses a hierarchical schematic: `4in1ESC.kicad_sch` is the main sheet containing power supply, current sensing, and the connector. `ESC.kicad_sch` is a single ESC channel instantiated 4 times.

Each ESC channel has:
- AT32F421G8U7 MCU running Betaflight firmware
- NSG2065Q 3-phase gate driver
- 6x SP40N03GNJ MOSFETs (3 half-bridges for 3-phase output)
- Back-EMF feedback network for sensorless commutation

## Ordering from JLCPCB

Production files are in the `production/` folder:
- `v0.3.zip` - Gerber files for the PCB
- `bom.csv` - Bill of Materials with LCSC part numbers
- `positions.csv` - Component placement file for PCBA

## Known Issues

- Current sensing circuit (INA199A1DCKR) needs debugging - not functional on v0.3

## Project Structure

```
4in1ESC.kicad_sch     - Main schematic (power, sensing, connector)
ESC.kicad_sch         - Single ESC channel (used 4x as sub-sheet)
4in1ESC.kicad_pcb     - PCB layout
4in1ESC.pretty/       - Custom footprint library
components.kicad_sym  - Custom symbol library (gate driver, connector, etc.)
production/           - JLCPCB fabrication files
```

## License

This hardware design is licensed under [CERN-OHL-S-2.0](https://ohwr.org/cern_ohl_s_v2.txt).
