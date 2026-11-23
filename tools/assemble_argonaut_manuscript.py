#!/usr/bin/env python3
"""
Assemble the complete physical novel master manuscript for
THE IMPEDANCE THRESHOLD: ARGONAUT
A Novel of Relational Spaceflight & First Life
(Canonical Prequel to the Exospecies Survey Series)
Author: Todd Hendrixx
"""

import os
import sys

PROJECT_ROOT = "/Users/hendrixx./The_Impedance_Threshold"
MANUSCRIPT_DIR = os.path.join(PROJECT_ROOT, "manuscript")
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "The_Impedance_Threshold_Master_Manuscript.md")

ACT_DIVIDERS = {
    1: r"""
# ACT I: THE PULSAR BENCH
### Chapters 1–4 | Green Bank, The Shape Sphere, Giles County, and Plum Brook
> *"The universe contains no background grid. Space is not an empty room; it is the physical impedance between things that touch."*

---
""",
    5: r"""
# ACT II: THE CISLUNAR CRUCIBLE
### Chapters 5–8 | The Artemis Flare, Covariance Starvation, Coast-Lock, and Gateway Laser Lock
> *"When a Kalman filter becomes convinced of its own absolute perfection, it ceases to listen to reality. In cislunar space, mathematical overconfidence is fatal."*

---
""",
    9: r"""
# ACT III: THE CALLISTO STAGING
### Chapters 9–12 | Project ARGONAUT, The Canister Dilemma, The August 2033 Launch, and The Radiation Haven
> *"To park a mothership at Europa is suicide. Callisto is dead, silent, and cold—and precisely because it is dead, it is the only sanctuary in the Jovian furnace."*

---
""",
    13: r"""
# ACT IV: THE EUROPA SKIMMER
### Chapters 13–17 | The Plume Dive, Aerogel Capture, The Laser Weld, The Ghost Run, and Manifold Capture
> *"Fourteen thousand grains of an alien ocean, frozen into silica smoke at eighty Kelvin, flying silent across six hundred million kilometers of darkness."*

---
""",
    18: r"""
# ACT V: THE LIVING GRAIN
### Chapters 18–21 | The Cleanroom, Inevitable Biology, The Entropy Ladder, and The Keel of Daedalus
> *"Life is simple. It will fight for every scrap of free energy in the dark. It is the ladder above it that tests whether a species can climb to the stars."*

---
"""
}

ACT_DOSSIERS = {
    4: "Dossier_Act_I.md",
    8: "Dossier_Act_II.md",
    12: "Dossier_Act_III.md",
    17: "Dossier_Act_IV.md",
    21: "Dossier_Act_V.md",
}

CANONICAL_CHAPTER_FILES = [
    (1, "Chapter_01_The_Gridless_Sky.md"),
    (2, "Chapter_02_The_Weight_of_Relations.md"),
    (3, "Chapter_03_Tides_in_the_Granite.md"),
    (4, "Chapter_04_The_Seven_Watt_Partition.md"),
    (5, "Chapter_05_Flare_State.md"),
    (6, "Chapter_06_The_Negative_Variance.md"),
    (7, "Chapter_07_Dead_Mans_Trajectory.md"),
    (8, "Chapter_08_Light_Across_the_Blind_Spot.md"),
    (9, "Chapter_09_The_Ocean_Beyond_the_Ice.md"),
    (10, "Chapter_10_Catching_Smoke.md"),
    (11, "Chapter_11_Fire_on_the_Water.md"),
    (12, "Chapter_12_The_Cold_Sanctuary.md"),
    (13, "Chapter_13_The_Dive_into_the_Belt.md"),
    (14, "Chapter_14_Forty_Two_Seconds.md"),
    (15, "Chapter_15_The_Glass_Seam_in_the_Dark.md"),
    (16, "Chapter_16_The_Silent_Arc.md"),
    (17, "Chapter_17_Gravitys_Needle.md"),
    (18, "Chapter_18_The_Quarantine_Gate.md"),
    (19, "Chapter_19_Life_Is_Simple.md"),
    (20, "Chapter_20_The_Rungs_Above_the_Water.md"),
    (21, "Chapter_21_The_North_Sea_Horizon.md"),
]

def assemble_manuscript():
    print("Assembling THE IMPEDANCE THRESHOLD: ARGONAUT Master Manuscript...")
    front_matter_path = os.path.join(MANUSCRIPT_DIR, "Front_Matter.md")
    exhibits_path = os.path.join(MANUSCRIPT_DIR, "Exhibits_and_Appendices.md")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        with open(front_matter_path, "r", encoding="utf-8") as f_in:
            out.write(f_in.read().strip())
        out.write("\n\n---\n\n")
        
        for ch_num, filename in CANONICAL_CHAPTER_FILES:
            if ch_num in ACT_DIVIDERS:
                out.write(ACT_DIVIDERS[ch_num].strip())
                out.write("\n\n---\n\n")
            
            filepath = os.path.join(MANUSCRIPT_DIR, filename)
            if not os.path.exists(filepath):
                print(f"Error: Chapter file missing: {filepath}")
                sys.exit(1)
                
            with open(filepath, "r", encoding="utf-8") as ch_in:
                content = ch_in.read().strip()
                out.write(content)
                out.write("\n\n---\n\n")
                
            if ch_num in ACT_DOSSIERS:
                dossier_file = ACT_DOSSIERS[ch_num]
                dossier_path = os.path.join(MANUSCRIPT_DIR, dossier_file)
                if os.path.exists(dossier_path):
                    with open(dossier_path, "r", encoding="utf-8") as d_in:
                        out.write(d_in.read().strip())
                    out.write("\n\n---\n\n")
        
        with open(exhibits_path, "r", encoding="utf-8") as ex_in:
            out.write(ex_in.read().strip())
        out.write("\n")
        
    word_count = 0
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        word_count = len(f.read().split())
        
    print(f"Successfully generated: {OUTPUT_FILE}")
    print(f"Total Master Manuscript Word Count: {word_count:,} words")

if __name__ == "__main__":
    assemble_manuscript()
