#!/usr/bin/env python3
import os
import re

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

plates = {
    "Dossier_Act_I.md": "![PSR J0337+1715 Timing & Montgomery Shape Sphere](assets/plate_02_dossier_1_pulsar_bench.png)",
    "Dossier_Act_II.md": "![Artemis-7 (Prometheus) Cislunar Anomaly & Autonomous Recovery](assets/plate_03_dossier_2_artemis_recovery.png)",
    "Dossier_Act_III.md": "![Project ARGONAUT Jovian Radiation Profile & Mission Stages](assets/plate_04_ch09_argonaut_flight_plan.png)",
    "Dossier_Act_IV.md": "![Europa Plume Encounter & 980-Day Autonomous Ghost Run](assets/plate_05_dossier_4_plume_ghost_run.png)",
    "Dossier_Act_V.md": "![IAS Daedalus Architecture & 400-Year Technology Cascade](assets/plate_07_dossier_5_daedalus_cascade.png)"
}

for fname, plate_tag in plates.items():
    fpath = os.path.join(MANUSCRIPT_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the top code block (lines starting with ``` and ending with ```)
    # The first code block in each dossier is the header block
    parts = content.split("```")
    if len(parts) >= 3:
        # parts[0] is before first ```
        # parts[1] is the header box
        # parts[2:] is the rest
        new_content = parts[0].rstrip() + "\n\n" + plate_tag + "\n\n" + "```".join(parts[2:]).lstrip()
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Replaced top header box in {fname}")
    else:
        print(f"Could not split {fname}")

