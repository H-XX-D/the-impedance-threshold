d3_path = "/Users/hendrixx./The_Impedance_Threshold/manuscript/Dossier_Act_III.md"
with open(d3_path, "r", encoding="utf-8") as f:
    c3 = f.read()

# Replace table 1 in Dossier 3
old_tab1 = """| Subsystem | Dry (kg) | Prop (kg) | Wet (kg) | Power |
| :--- | :--- | :--- | :--- | :--- |
| **Callisto Carrier Depot** | 23,780.0 | 18,400.0 | 42,180.0 | 200,000 W (Fission) |
| **Europa Skimmer** | 516.0 | 684.0 | 1,200.0 | 350 W |
| **Return Canister 1** | 8.00 | 2.00 | 10.00 | 8.0 W |"""

new_tab1 = """* **Callisto Carrier Depot:** Dry mass 23,780 kg; Xenon propellant 18,400 kg; Total wet mass 42,180 kg; Power 200 kW (Westinghouse space fission core + 12 AEPS Hall thrusters).
* **Europa Skimmer:** Dry mass 516 kg; MON-3/Hydrazine propellant 684 kg; Wet mass 1,200 kg; Power 350 W (Aerojet R-4D-11 bipropellant engine + graded aerogel cassette).
* **Return Canister 1:** Dry mass 8.00 kg; N2 cold-gas propellant 2.00 kg; Total launch mass 10.00 kg; Power 8.0 W cruise (Ti-6Al-4V laser-welded shell + QRC XNAV ASIC core)."""

c3 = c3.replace(old_tab1, new_tab1)

# Replace table 2 in Dossier 3
old_tab2 = """| Region | Radius | Flux (>3 MeV) | Dose Rate | 5-Yr Dose |
| :--- | :--- | :--- | :--- | :--- |
| **Io (Torus)** | 5.9 $R_J$ | $2.4 \\times 10^8\\text{ cm}^{-2}\\text{s}^{-1}$ | 1,840 rad/hr | 80.5 Mrad (Fatal) |
| **Europa (Plumes)** | 9.4 $R_J$ | $8.4 \\times 10^7\\text{ cm}^{-2}\\text{s}^{-1}$ | 540 rad/hr | 23.6 Mrad (Fatal) |
| **Ganymede** | 15.2 $R_J$ | $4.2 \\times 10^6\\text{ cm}^{-2}\\text{s}^{-1}$ | 18.4 rad/hr | 0.8 Mrad (Unsafe) |
| **Callisto (Depot)** | 26.3 $R_J$ | $1.1 \\times 10^4\\text{ cm}^{-2}\\text{s}^{-1}$ | **7.1 rad/hr** | **0.03 Mrad (Safe)** |"""

new_tab2 = """* **Io (Volcanic Torus, 5.9 $R_J$):** Flux $2.4 \\times 10^8\\text{ cm}^{-2}\\text{s}^{-1}$; Dose rate 1,840 rad/hr (80.5 Mrad 5-yr cumulative: immediate silicon destruction).
* **Europa (Cryo-Plumes, 9.4 $R_J$):** Flux $8.4 \\times 10^7\\text{ cm}^{-2}\\text{s}^{-1}$; Dose rate 540 rad/hr (23.6 Mrad 5-yr: requires fast kinetic skimming passes).
* **Ganymede (Mid-System, 15.2 $R_J$):** Flux $4.2 \\times 10^6\\text{ cm}^{-2}\\text{s}^{-1}$; Dose rate 18.4 rad/hr (0.8 Mrad 5-yr: unsafe for unshielded electronics).
* **Callisto (Depot Haven, 26.3 $R_J$):** Flux $1.1 \\times 10^4\\text{ cm}^{-2}\\text{s}^{-1}$; Dose rate **7.1 rad/hr** (0.03 Mrad 5-yr: long-term operational radiation haven)."""

c3 = c3.replace(old_tab2, new_tab2)
with open(d3_path, "w", encoding="utf-8") as f:
    f.write(c3)

# Replace table in Dossier 5
d5_path = "/Users/hendrixx./The_Impedance_Threshold/manuscript/Dossier_Act_V.md"
with open(d5_path, "r", encoding="utf-8") as f:
    c5 = f.read()

old_tab5 = """| Component | Dimension | Composition & Function |
| :--- | :--- | :--- |
| **Cell Envelope** | 1.6 µm × 0.8 µm | Continuous lipid bilayer (5.2 nm thick) |
| **Membrane Lipids** | Glycerol-1-Phosphate | Di-ether linked isoprenoid caldarchaeol macrocycles |
| **Catalytic Cores** | 50 nm Cubane Crystals | $[\\text{Fe}_4\\text{-S}_4]$ and $[\\text{Ni-Fe-S}]$ ferredoxin engines |
| **Energy Pathway** | Chemiosmotic Proton | Wood-Ljungdahl $\\text{H}_2$-oxidation & $\\text{SO}_4^{2-}$ reduction |
| **ATP Synthase** | Rotary Motor | Membrane-bound proton rotor ($4.0\\text{ H}^+ / \\text{ATP}$) |
| **Polymer** | Linear Double-Helix | Peptide Nucleic Acid (PNA) / Uncharged Polyamide |
| **Monomer** | 0.34 nm spacing | Poly-N-(2-aminoethyl)glycine repeating backbone |
| **Bases** | 4 Characters | Adenine (A), 2,6-Diaminopurine (D), Uracil (U), 5-Methylcytosine (M) |"""

new_tab5 = """* **Cell Envelope:** 1.6 µm × 0.8 µm continuous lipid bilayer (5.2 nm thick).
* **Membrane Lipids:** Glycerol-1-Phosphate di-ether linked isoprenoid caldarchaeol macrocycles.
* **Catalytic Cores:** 50 nm Cubane Crystals: $[\\text{Fe}_4\\text{-S}_4]$ and $[\\text{Ni-Fe-S}]$ ferredoxin engines.
* **Energy Pathway:** Chemiosmotic Proton: Wood-Ljungdahl $\\text{H}_2$-oxidation & $\\text{SO}_4^{2-}$ reduction.
* **ATP Synthase:** Rotary Molecular Motor: Membrane-bound proton rotor ($4.0\\text{ H}^+ / \\text{ATP}$).
* **Informational Polymer:** Linear Double-Helix Peptide Nucleic Acid (PNA) / Uncharged Polyamide.
* **Monomer Backbone:** 0.34 nm spacing: Poly-N-(2-aminoethyl)glycine repeating peptide backbone.
* **Heterocyclic Bases:** Adenine (A), 2,6-Diaminopurine (D), Uracil (U), 5-Methylcytosine (M)."""

c5 = c5.replace(old_tab5, new_tab5)
with open(d5_path, "w", encoding="utf-8") as f:
    f.write(c5)

print("Converted tables to clean bullet specifications.")
