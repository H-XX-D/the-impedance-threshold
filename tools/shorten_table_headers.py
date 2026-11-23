import re

d3_path = "/Users/hendrixx./The_Impedance_Threshold/manuscript/Dossier_Act_III.md"
with open(d3_path, "r", encoding="utf-8") as f:
    t3 = f.read()

t3 = t3.replace("| Subsystem Element | Dry Mass (kg) | Prop Mass (kg) | Wet Mass (kg) | Power (W) |",
                "| Subsystem | Dry (kg) | Prop (kg) | Wet (kg) | Power |")
t3 = t3.replace("| Region | Orbital Radius | Electron Flux (>3 MeV) | Dose Rate | 5-Year Dose |",
                "| Region | Radius | Flux (>3 MeV) | Dose Rate | 5-Yr Dose |")
with open(d3_path, "w", encoding="utf-8") as f:
    f.write(t3)

d5_path = "/Users/hendrixx./The_Impedance_Threshold/manuscript/Dossier_Act_V.md"
with open(d5_path, "r", encoding="utf-8") as f:
    t5 = f.read()

t5 = t5.replace("| Cellular Component | Dimension | Composition & Biochemical Function |",
                "| Component | Dimension | Composition & Function |")
with open(d5_path, "w", encoding="utf-8") as f:
    f.write(t5)

print("Shortened table header tokens.")
