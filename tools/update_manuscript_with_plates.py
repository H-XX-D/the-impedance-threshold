#!/usr/bin/env python3
"""
Updates manuscript markdown files to replace bleeding ASCII boxes
with clean, publication-grade image plates.
"""

import os
import re

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

# 1. Front_Matter.md
front_matter_path = os.path.join(MANUSCRIPT_DIR, "Front_Matter.md")
with open(front_matter_path, "r", encoding="utf-8") as f:
    fm_content = f.read()

fm_replaced = re.sub(
    r"```\s*={10,}.*?={10,}\s*```",
    lambda m: "![Sol Navigation Directorate: Master Mission Architecture](assets/plate_01_front_matter_architecture.png)",
    fm_content,
    flags=re.DOTALL
)
with open(front_matter_path, "w", encoding="utf-8") as f:
    f.write(fm_replaced)
print("Updated Front_Matter.md")

# 2. Dossier_Act_I.md
dossier_1_path = os.path.join(MANUSCRIPT_DIR, "Dossier_Act_I.md")
with open(dossier_1_path, "r", encoding="utf-8") as f:
    d1_content = f.read()

d1_replaced = re.sub(
    r"```\s*={10,}\s*PROJECT DESIGNATION:.*?={10,}\s*```",
    lambda m: "![PSR J0337+1715 Timing & Montgomery Shape Sphere](assets/plate_02_dossier_1_pulsar_bench.png)",
    d1_content,
    flags=re.DOTALL
)
d1_replaced = re.sub(
    r"```\s*={10,}\s*BAND ID.*?={10,}\s*```",
    lambda m: "*Multi-Frequency Timing Data (P-Band 820 MHz: 3.712 µs; L-Band 1400 MHz: 3.711 µs; S-Band 2100 MHz: 3.713 µs) confirms zero chromatic dispersion ($\Delta t \\propto f^0$), establishing that the residual is strictly geometric rather than plasma-induced. See Plate QRC-GBO-0226 above.*",
    d1_replaced,
    flags=re.DOTALL
)
with open(dossier_1_path, "w", encoding="utf-8") as f:
    f.write(d1_replaced)
print("Updated Dossier_Act_I.md")

# 3. Dossier_Act_II.md
dossier_2_path = os.path.join(MANUSCRIPT_DIR, "Dossier_Act_II.md")
with open(dossier_2_path, "r", encoding="utf-8") as f:
    d2_content = f.read()

d2_replaced = re.sub(
    r"```\s*={10,}\s*INCIDENT ID:.*?={10,}\s*```",
    lambda m: "![Artemis-7 (Prometheus) Cislunar Anomaly & Autonomous Recovery](assets/plate_03_dossier_2_artemis_recovery.png)",
    d2_content,
    flags=re.DOTALL
)
d2_replaced = re.sub(
    r"```\s*TIME \(UTC\)\s+SUBSYSTEM.*?--------------------------------------------------------------------------------------------------\s*```",
    lambda m: "*Sequence of Events Summary: 03:14 UTC X8.4 Solar Flare; 03:40 UTC DSN Carrier Loss; 04:12 UTC GEONS Covariance Starvation (predicted perilune -42.8 km); 04:14 UTC Backup Coast-Lock (0x7E14); 04:47 UTC Gateway Laser Lock; 04:48 UTC QRC Jetson Override Burn (188.4 m/s); 05:39 UTC Perilune Cleared at 112.4 km into NRHO. Complete timeline mapped in Plate ART-REC-0711 above.*",
    d2_replaced,
    flags=re.DOTALL
)
with open(dossier_2_path, "w", encoding="utf-8") as f:
    f.write(d2_replaced)
print("Updated Dossier_Act_II.md")

# 4. Chapter_09_Project_ARGONAUT.md
ch9_path = os.path.join(MANUSCRIPT_DIR, "Chapter_09_Project_ARGONAUT.md")
with open(ch9_path, "r", encoding="utf-8") as f:
    ch9_content = f.read()

ch9_replaced = re.sub(
    r"```\s*={10,}\s*PROJECT ARGONAUT: MASTER LIFECYCLE.*?={10,}\s*```",
    lambda m: "![Project ARGONAUT Flight Architecture & Lifecycle Schedule](assets/plate_04_ch09_argonaut_flight_plan.png)",
    ch9_content,
    flags=re.DOTALL
)
with open(ch9_path, "w", encoding="utf-8") as f:
    f.write(ch9_replaced)
print("Updated Chapter_09_Project_ARGONAUT.md")

# 5. Dossier_Act_III.md
dossier_3_path = os.path.join(MANUSCRIPT_DIR, "Dossier_Act_III.md")
with open(dossier_3_path, "r", encoding="utf-8") as f:
    d3_content = f.read()

d3_replaced = re.sub(
    r"```\s*={10,}\s*DOCUMENT NUMBER:\s+ARG-CDR-2032-03.*?={10,}\s*```",
    lambda m: "![Project ARGONAUT Jovian Radiation Profile & Mission Stages](assets/plate_04_ch09_argonaut_flight_plan.png)",
    d3_content,
    flags=re.DOTALL
)
d3_replaced = re.sub(
    r"```\s*={10,}\s*SUBSYSTEM ELEMENT\s+DRY MASS.*?={10,}\s*```",
    lambda m: """| Subsystem Element | Dry Mass (kg) | Prop Mass (kg) | Wet Mass (kg) | Power (W) |
| :--- | :--- | :--- | :--- | :--- |
| **Callisto Carrier Depot** | 23,780.0 | 18,400.0 | 42,180.0 | 200,000 W (Fission) |
| **Europa Skimmer** | 516.0 | 684.0 | 1,200.0 | 350 W |
| **Return Canister 1** | 8.00 | 2.00 | 10.00 | 8.0 W |""",
    d3_replaced,
    flags=re.DOTALL
)
d3_replaced = re.sub(
    r"```\s*={10,}\s*MOON / REGION\s+ORBITAL RADIUS.*?={10,}\s*```",
    lambda m: """| Region | Orbital Radius | Electron Flux (>3 MeV) | Dose Rate | 5-Year Dose |
| :--- | :--- | :--- | :--- | :--- |
| **Io (Torus)** | 5.9 $R_J$ | $2.4 \\times 10^8\\text{ cm}^{-2}\\text{s}^{-1}$ | 1,840 rad/hr | 80.5 Mrad (Fatal) |
| **Europa (Plumes)** | 9.4 $R_J$ | $8.4 \\times 10^7\\text{ cm}^{-2}\\text{s}^{-1}$ | 540 rad/hr | 23.6 Mrad (Fatal) |
| **Ganymede** | 15.2 $R_J$ | $4.2 \\times 10^6\\text{ cm}^{-2}\\text{s}^{-1}$ | 18.4 rad/hr | 0.8 Mrad (Unsafe) |
| **Callisto (Depot)** | 26.3 $R_J$ | $1.1 \\times 10^4\\text{ cm}^{-2}\\text{s}^{-1}$ | **7.1 rad/hr** | **0.03 Mrad (Safe)** |""",
    d3_replaced,
    flags=re.DOTALL
)
with open(dossier_3_path, "w", encoding="utf-8") as f:
    f.write(d3_replaced)
print("Updated Dossier_Act_III.md")

# 6. Dossier_Act_IV.md
dossier_4_path = os.path.join(MANUSCRIPT_DIR, "Dossier_Act_IV.md")
with open(dossier_4_path, "r", encoding="utf-8") as f:
    d4_content = f.read()

d4_replaced = re.sub(
    r"```\s*={10,}\s*SPACECRAFT:\s+Europa Skimmer.*?={10,}\s*```",
    lambda m: "![Europa Plume Encounter & 980-Day Autonomous Ghost Run](assets/plate_05_dossier_4_plume_ghost_run.png)",
    d4_content,
    flags=re.DOTALL
)
d4_replaced = re.sub(
    r"```\s*={10,}\s*TIME \(UTC\)\s+ALTITUDE\s+PLUME REGION.*?={10,}\s*```",
    lambda m: "*Manannán Chasma Plume Encounter Log: Altitude 50.18 km, Velocity 2,214.2 m/s, Intercept duration 42.0 seconds. 14,812 discrete ice grains captured at T < 220 K without thermal alteration. Detailed density and acoustic profile documented in Plate ARG-ENC-1443 above.*",
    d4_replaced,
    flags=re.DOTALL
)
d4_replaced = re.sub(
    r"```\s*={10,}\s*BURN #\s+DATE\s+HELIOCENTRIC.*?TOTAL DELTA-V EXPENDED ACROSS 980 DAYS: 6.8240 METERS PER SECOND.*?={10,}\s*```",
    lambda m: "*980-Day Ghost Run Autonomous Navigation Ledger: 47 pulsed micro-burns executed by QRC XNAV ASIC without Earth contact; total delta-v delivered: 6.824 m/s; 580 g GN2 propellant expended; 1.42 kg reserve remaining at Lunar Gateway docking. See Plate ARG-ENC-1443.*",
    d4_replaced,
    flags=re.DOTALL
)
with open(dossier_4_path, "w", encoding="utf-8") as f:
    f.write(d4_replaced)
print("Updated Dossier_Act_IV.md")

# 7. Chapter_20_The_Entropy_Ladder_Revealed.md
ch20_path = os.path.join(MANUSCRIPT_DIR, "Chapter_20_The_Entropy_Ladder_Revealed.md")
with open(ch20_path, "r", encoding="utf-8") as f:
    ch20_content = f.read()

ch20_replaced = re.sub(
    r"```\s*={10,}\s*THE ENTROPY LADDER: COSMIC THERMODYNAMIC BOTTLENECKS.*?={10,}\s*```",
    lambda m: "![The Thermodynamic Entropy Ladder: Dissipation Attractors](assets/plate_06_ch20_entropy_ladder.png)",
    ch20_content,
    flags=re.DOTALL
)
with open(ch20_path, "w", encoding="utf-8") as f:
    f.write(ch20_replaced)
print("Updated Chapter_20_The_Entropy_Ladder_Revealed.md")

# 8. Dossier_Act_V.md
dossier_5_path = os.path.join(MANUSCRIPT_DIR, "Dossier_Act_V.md")
with open(dossier_5_path, "r", encoding="utf-8") as f:
    d5_content = f.read()

d5_replaced = re.sub(
    r"```\s*={10,}\s*SAMPLE DESIGNATION:\s+EUROPA-01.*?={10,}\s*```",
    lambda m: "![IAS Daedalus Architecture & 400-Year Technology Cascade](assets/plate_07_dossier_5_daedalus_cascade.png)",
    d5_content,
    flags=re.DOTALL
)
d5_replaced = re.sub(
    r"```\s*={10,}\s*CELLULAR COMPONENT\s+MEASURED DIMENSION.*?={10,}\s*```",
    lambda m: """| Cellular Component | Dimension | Composition & Biochemical Function |
| :--- | :--- | :--- |
| **Cell Envelope** | 1.6 µm × 0.8 µm | Continuous lipid bilayer (5.2 nm thick) |
| **Membrane Lipids** | Glycerol-1-Phosphate | Di-ether linked isoprenoid caldarchaeol macrocycles |
| **Catalytic Cores** | 50 nm Cubane Crystals | $[\\text{Fe}_4\\text{-S}_4]$ and $[\\text{Ni-Fe-S}]$ ferredoxin engines |
| **Energy Pathway** | Chemiosmotic Proton | Wood-Ljungdahl $\\text{H}_2$-oxidation & $\\text{SO}_4^{2-}$ reduction |
| **ATP Synthase** | Rotary Motor | Membrane-bound proton rotor ($4.0\\text{ H}^+ / \\text{ATP}$) |
| **Polymer** | Linear Double-Helix | Peptide Nucleic Acid (PNA) / Uncharged Polyamide |
| **Monomer** | 0.34 nm spacing | Poly-N-(2-aminoethyl)glycine repeating backbone |
| **Bases** | 4 Characters | Adenine (A), 2,6-Diaminopurine (D), Uracil (U), 5-Methylcytosine (M) |""",
    d5_replaced,
    flags=re.DOTALL
)
d5_replaced = re.sub(
    r"```\s*={10,}\s*RESOLUTION OF THE GENERAL ASSEMBLY.*?={10,}\s*```",
    lambda m: "*United Nations Resolution 2043-UN-IAS-01: Passed unanimously June 20, 2043. Mandates the four-century technology development covenant across the Sol Navigation Grid, Unimodular Fusion Torches, Isochoric Vitrification, and the commissioning of IAS Daedalus to Acheron-Prime. Complete timeline mapped in Plate IAS-048-D-KEEL above.*",
    d5_replaced,
    flags=re.DOTALL
)
with open(dossier_5_path, "w", encoding="utf-8") as f:
    f.write(d5_replaced)
print("Updated Dossier_Act_V.md")

# 9. Exhibits_and_Appendices.md
exhibits_path = os.path.join(MANUSCRIPT_DIR, "Exhibits_and_Appendices.md")
with open(exhibits_path, "r", encoding="utf-8") as f:
    ex_content = f.read()

ex_replaced = re.sub(
    r"```\s*={10,}\s*PROJECT ARGONAUT: MASTER PROGRAMMATIC FLIGHT.*?={10,}\s*```",
    lambda m: "![Project ARGONAUT Flight Architecture & Master Schedule](assets/plate_04_ch09_argonaut_flight_plan.png)",
    ex_content,
    flags=re.DOTALL
)
ex_replaced = ex_replaced.replace(
    "## DIEGETIC EXHIBIT B: KINEMATIC BOUNDING FILTER",
    "![QRC Relational State Estimator & Autonomous Control Flow](assets/plate_08_exhibits_navigation_algorithm.png)\n\n## DIEGETIC EXHIBIT B: KINEMATIC BOUNDING FILTER"
)
ex_replaced = ex_replaced.replace(
    "## DIEGETIC EXHIBIT D: CANISTER 1 WELD INTEGRITY & MASS SPECTROMETRY",
    "![Canister 1 Cryogenic Laser Hermetic Seal Qualification](assets/plate_09_exhibits_canister_qualification.png)\n\n## DIEGETIC EXHIBIT D: CANISTER 1 WELD INTEGRITY & MASS SPECTROMETRY"
)

# For any remaining code blocks in Exhibits B and C, ensure long comments and lines wrap nicely
ex_replaced = re.sub(r"# ={10,}", "# ----------------------------------------", ex_replaced)

with open(exhibits_path, "w", encoding="utf-8") as f:
    f.write(ex_replaced)
print("Updated Exhibits_and_Appendices.md")

print("All manuscript markdown files updated with diegetic plates.")
