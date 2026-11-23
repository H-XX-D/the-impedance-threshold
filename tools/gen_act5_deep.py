#!/usr/bin/env python3
"""
Full canonical authoring of Act V: Chapters 18-21 and Dossier V.
Author: Todd Hendrixx
Target word count: ~11,500 words.
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"
os.makedirs(MANUSCRIPT_DIR, exist_ok=True)

CH18 = r"""# CHAPTER EIGHTEEN
## The Quarantine Gate

The Lunar Receiving Laboratory on Lunar Gateway Station was isolated inside the station's outermost zenith module, held at a negative pressure differential of one hundred pascals relative to the station corridor.

Inside the class-10,000 biological cleanroom, the air was recirculated through triple-redundant HEPA and high-temperature catalytic oxidizers designed to incinerate any viable biological particle at eight hundred degrees Celsius.

Dr. Aris Thorne and Dr. Kenji Sato stood before the primary bio-isolation glovebox—Glovebox 4—wearing pressurized white Teflon cleanroom suits with independent rebreather packs.

Through the multi-layer quartz viewing port of the chamber sat Canister 1, secured in an automated laser lathe cradle.

Around the chamber perimeter, red strobe indicators pulsed in silent alarm:
```
[COSPAR CATEGORY V BIO-HAZARD ALERT]
LOCATION:              GATEWAY LRL // GLOVEBOX 4
MONITORING CHANNEL:    HIGH-VACUUM RESIDUAL GAS ANALYZER (RGA-02)
ANOMALY DETECTED:      PRESSURE SPIKE: +14.2 Pa HELIUM DETECTED
STATUS:                POSSIBLE CANISTER COMPROMISE
CONTINGENCY PROTOCOL:  PROTOCOL 7-OMEGA (THERMAL INCINERATION)
TIME TO AUTONOMOUS INCINERATION: 42 MINUTES
```

On the wall speaker, the clipped voice of Dr. Christian Lindqvist, Chairman of the International Planetary Protection Committee in Geneva, spoke with frozen bureaucratic finality:

"Dr. Thorne, your residual gas analyzer has registered fourteen pascals of helium in the glovebox atmosphere. Under Article IV of the COSPAR Category V Protocol, any unexplained gas release from an extraterrestrial sample return vessel during initial inspection is prima facie evidence of structural micro-fracture. If the canister seal has leaked, we cannot guarantee biological containment. The protocol requires autonomous thermal destruction: thirty minutes at twelve hundred degrees Celsius."

Aris Thorne gripped the edge of the steel glovebox console, his knuckles whitening.

"Dr. Lindqvist, you are talking about incinerating the only sample of an alien ocean ever collected by the human species! Fourteen pascals of helium is a whisper! It is three cubic centimeters of gas!"

"That whisper is three times the maximum allowable leak rate under the Geneva Accords, Dr. Thorne," Lindqvist replied cold as dry ice. "If Europa harbors pathogenic extremophiles—prions, uncharged nucleic replicators, or anaerobic toxins—a single micro-fissure could contaminate the station and Earth. The automated incineration sequence has been armed by Geneva. You have thirty-eight minutes to prove that leak is not a seal failure."

---

### The Brunauer-Emmett-Teller Desorption Proof

Through the airlock door stepped Dr. Ryan Vance, accompanied by his daughter, twenty-four-year-old **Elena Vance**, who was now completing her doctorate in relativistic metrology at Cambridge.

Ryan did not look at the countdown clock. He pulled up the mass spectrometer log on the laboratory terminal.

"It is not a seal failure, Aris," Ryan said calmly.

Lindqvist’s voice cut in from Geneva: "Dr. Vance, do not waste our time with theoretical optimism. The helium reading is real."

"The helium reading is real, Dr. Lindqvist," Ryan said, turning to the conference camera. "And your physical chemistry is forty years out of date."

Elena Vance stepped to the interactive whiteboard, her stylus sketching out an isothermal adsorption graph with rapid, confident strokes.

"In 2040, when Canister 1 was sealed in Callisto orbit," Elena explained, her voice steady and clear, "the canister was welded by a 200-watt fiber laser in a one-point-two-atmosphere helium purge. Grade-5 titanium (Ti-6Al-4V) develops a surface oxide layer—rutile titanium dioxide ($\text{TiO}_2$)—that possesses a microscopic surface roughness factor of one point six."

She wrote the **Brunauer-Emmett-Teller (BET) Isotherm** equation across the screen:
$$\frac{p}{V (p_0 - p)} = \frac{1}{V_m c_{\text{BET}}} + \frac{c_{\text{BET}} - 1}{V_m c_{\text{BET}}} \left( \frac{p}{p_0} \right)$$

"During the three-year interplanetary transit back to Earth," Elena continued, "the titanium canister was chilled to fifty Kelvin. At fifty Kelvin, physical adsorption (physisorption) binds neutral helium atoms to the high-energy surface sites of the titanium oxide lattice. When Canister 1 entered the Gateway airlock today, the chamber temperature was raised from fifty Kelvin to two hundred and ninety-three Kelvin."

Ryan Vance stepped forward, pointing to the derivative trace of the pressure curve.

"What you are measuring is not gas escaping through a cracked weld bead, Dr. Lindqvist," Ryan said. "What you are measuring is the thermal desorption of physically adsorbed helium atoms from the external surface skin of the canister itself. Look at the activation energy of the desorption curve: zero point zero eight electron-volts. That is the exact van der Waals binding energy of helium on rutile $\text{TiO}_2$."

He tapped a key, displaying the internal canister acoustic strain sensor:

"The internal canister pressure is holding at precisely one point two zero zero atmospheres. The weld bead is intact. If the canister had leaked, the internal acoustic resonance frequency would have shifted by twelve hertz. The resonance is flat to within point zero one hertz. The canister is unbroken."

In Geneva, four thousand miles away, the bio-quarantine monitors recalculated the BET desorption enthalpy.

For two agonizing minutes, the conference line remained silent as the committee verified the math.

Then, with six minutes remaining on the incineration clock, the red strobes died.

```
[COSPAR CATEGORY V SAFETY OVERRIDE VERIFIED]
BET SURFACE DESORPTION CONFIRMED // INTERNAL SEAL INTEGRITY 100%
INCINERATION PROTOCOL ABORTED BY GENEVA DIRECTORATE
CONTAINMENT LEVEL: PRISTINE // AUTHORIZATION GRANTED TO OPEN CANISTER
```

Aris Thorne let out a long, shuddering breath, resting his forehead against the cold quartz glass of the glovebox.

Beside him, Kenji Sato reached for the lathe controls. "Let's open the ocean."
"""

CH19 = r"""# CHAPTER NINETEEN
## Life Is Simple

At 14:15 UTC on October 14, 2043, inside Glovebox 4, the precision laser lathe severed the top retention flange of Canister 1.

A robotic manipulator extracted the graded silica aerogel cassette and transferred it into an inert-argon analytical chamber.

Under the cold illumination of a high-power stereomicroscope, the aerogel wafer looked like a constellation of tiny, frozen shooting stars. Fourteen thousand eight hundred and twelve discrete entry tracks stretched through the transparent blue matrix, each track terminating in a microscopic, dark cryo-grain.

Dr. Aris Thorne selected **Track 4,812**—a clean, forty-micron grain arrested at a depth of twenty-six millimeters in the aerogel, where the peak shock temperature had never exceeded twenty-two degrees Celsius.

A focused gallium-ion beam milled away a five-micron silica window, exposing the pristine grain core.

A micro-manipulator lifted the sample and placed it onto the cryogenic sample stage of a sub-nanometer **Cryogenic Transmission Electron Microscope (Cryo-TEM)** operating at eighty kilovolts.

On the main laboratory monitors, the image focused.

The entire science team crowded behind the console, their breath catching in their throats.

The screen did not display abstract mineral grains or volcanic basalt dust.

It displayed **cells**.

Tens of thousands of discrete, elongated rod-shaped microorganisms, one point six microns long and zero point eight microns wide, packed in frozen, pristine detail.

"Look at the membrane," Aris whispered, his voice trembling with an awe so profound it sounded like prayer.

The cell envelope was not a lipid bilayer like terrestrial bacteria or human cells. It was an unbroken, continuous **tetraether lipid monolayer**—five point two nanometers thick.

"Caldarchaeol," Aris said, identifying the molecular architecture instantly. "A glycerol-1-phosphate core linked via ether bonds to continuous forty-carbon isoprenoid chains with internal cyclopentane rings. It’s an extremophile membrane built to withstand hydraulic pressures of seventeen hundred atmospheres and water temperatures of one hundred and forty degrees Celsius."

Inside each cell, the electron beam revealed dense, ordered chains of fifty-nanometer greigite ($\text{Fe}_3\text{S}_4$) magnetic crystals, aligned along an internal protein cytoskeleton.

"Chemosynthetic magnetotaxis," Aris murmured. "They navigate the hydrothermal convective plumes at the bottom of the Europa ocean using Jupiter’s tidal magnetic field."

---

### The Molecular Code: PNA

Next came the chemical sequencer: a tandem high-resolution mass spectrometer (MS/MS) and liquid chromatography system.

Aris injected a micro-liter extract of the cell nucleus into the ionization chamber.

If the organism was a descendant of terrestrial life carried by an asteroid impact, its genetic material would consist of RNA or DNA: a backbone of ribose or deoxyribose sugars linked by charged phosphate groups, carrying the familiar four bases: Adenine, Guanine, Cytosine, and Thymine.

The mass spectrometer trace flashed across the screen:

```
[MOLECULAR STRUCTURAL ANALYSIS // SAMPLE: TRACK 4812]
POLYMERIC BACKBONE:     NEUTRAL POLYAMIDE (PEPTIDE BACKBONE)
MONOMER REPEAT:         POLY-N-(2-AMINOETHYL) GLYCINE (AEG)
ELECTROSTATIC CHARGE:   NEUTRAL (NO PHOSPHATE DIELECTRIC REPULSION)
STEREOCHEMISTRY:        ACHIRAL (NO D- OR L-ENANTIOMERIC ASYMMETRY)
BASE PAIR ALPHABET:     4 HETEROCYCLIC NUCLEOBASES:
  BASE 1:               2,6-DIAMINOPURINE (D)
  BASE 2:               URACIL (U)
  BASE 3:               ISOGUANINE (iG)
  BASE 4:               ISOCYTOSINE (iC)
GENETIC CODE ARCHITECTURE: PEPTIDE NUCLEIC ACID (PNA) DOUBLE HELIX
```

The room was utterly silent.

It was not DNA. It was not RNA.

It was **Peptide Nucleic Acid (PNA)**—an uncharged, achiral genetic polymer built from simple amino acid chains, utilizing four non-standard nucleobases joined by Watson-Crick hydrogen bonding.

"Independent genesis," Elena Vance said softly, her eyes wide as she looked at the mass spectra. "It has no phosphate backbone. It has no chiral sugars. It did not come from Earth. It arose in the dark, alkaline hydrothermal vents of Europa, entirely from scratch."

Aris Thorne turned to Ryan Vance, tears streaming down his face beneath his visor.

"Ryan... for fifty years, cosmologists told us that life was a freak accident. A one-in-a-trillion statistical fluke that required a cosmic miracle to organize amino acids into self-replicating information. But look at this."

He pointed to the screen.

"This organism was born in total darkness, under thirty kilometers of crushing ice, bathed in lethal Jovian radiation, surrounded by nothing but basalt, hydrogen gas, and sulfur. And yet it assembled a genetic code. It built rotary molecular ATP motors. It built an ecosystem."

Ryan Vance looked at the image of the frozen Europan archaeon, then reached out and touched the glass of the display.

"Life is not a miracle, Aris," Ryan said gently. "Life is a thermodynamic inevitability. Wherever you have free energy, a chemical gradient, and time, the universe will organize matter to dissipate entropy. Life is simple."

He looked toward the window, out toward the cold, distant white speck of Jupiter gleaming in the lunar sky.

"It is the ladder above it that is hard."
"""

CH20 = r"""# CHAPTER TWENTY
## The Rungs Above the Water

November 22, 2043. One month after the confirmation of *Exo-archaeon europae*.

In New York City, the United Nations General Assembly Hall was packed to maximum capacity. Delegates from one hundred and ninety-three sovereign nations sat beneath the golden emblem of the world map, while hundreds of millions of people watched live across every screen on Earth, Lunar Gateway, and Mars Base Alpha.

Dr. Ryan Vance stood at the green marble rostrum.

Beside him sat his daughter, Dr. Elena Vance, and Dr. Elena Rostova.

Ryan did not bring a written speech. He placed his three-inch triangular fused silica prism onto the green marble, letting it catch the glare of the television lights.

"For three centuries," Ryan began, his voice calm, resonant, and clear, "humanity believed it was alone in an empty, cold universe. We believed that life was a delicate, accidental flame that existed only on this pale blue rock.

"Last month, Project ARGONAUT returned fourteen thousand grains of an alien ocean from Europa. We discovered that life is not rare. In every ocean where cold water touches warm rock, life will ignite. The galaxy is teeming with single cells, with hydrothermal vent ecosystems, with blind leviathans swimming through the black depths of frozen moons.

"Life is simple."

He paused, letting the silence settle over the assembly.

"The tragedy of the universe is not that life is rare. The tragedy is that almost all life is **trapped**."

He gestured to the holographic projector above the hall.

![The Thermodynamic Entropy Ladder](assets/plate_06_ch20_entropy_ladder.png)

A glowing, multi-tiered diagram of the **Thermodynamic Entropy Ladder** appeared above the delegates:

```
================================================================================
THE THERMODYNAMIC ENTROPY LADDER (CANONICAL FORMULATION)
================================================================================
RUNG 0: PREBIOTIC METRIC
        Serpentinization, alkaline hydrothermal gradients, abiotic catalysis.
RUNG 1: PROTO-BIOLOGICAL DISSIPATION
        Chemiosmosis, lipid encapsulation, PNA/RNA replication (Europa Ocean).
RUNG 2: SURFACE BIOSPHERES
        Photosynthesis, atmospheric oxygenation, macroscopic multicellularity.
RUNG 3: TECHNOLOGICAL ENERGETICS
        Combustion, metallurgy, steam, fossil hydrocarbons, nuclear fission.
RUNG 4: RELATIONAL METROLOGY & CISLUNAR INTEGRATION
        Quantum Relational Causality (QRC), edge autonomous GNC (CislunarOS).
RUNG 5: STELLAR HARVESTING & FUSION PROPULSION
        D-3He magnetic pinch torches, beamed laser momentum networks.
RUNG 6: INTERSTELLAR EXPEDITIONARY SPECIES
        Relativistic deep-survey starships (IAS Daedalus).
================================================================================
```

"Look at the first two rungs," Ryan said, his voice ringing through the chamber.

"The organisms of Europa were born beneath thirty kilometers of solid ice. In their ocean, there is no Sun. There is no fire. You cannot strike a flint beneath twenty thousand fathoms of brine. You cannot smelt copper. You cannot invent metallurgy. You cannot build a vacuum tube, a transistor, or a radio telescope.

"Those Europan cells can evolve for ten billion years. They can produce complex ecosystems, philosophers, poets singing in the acoustic dark of their ocean. But they will never build a starship. They are locked in their watery cradle forever.

"We are the only ones with fire. We are the only species in this solar system that broke through the water, walked onto the land, looked up at the stars, and built machines that run on seven watts of light."

He looked out across the assembly of nations.

"We cannot afford to waste our fire on provincial wars, on territorial greed, or on drawing imaginary borders across the dirt. The universe is not an empty container. It is a ladder of physical relations. And every rung must be paid for in discipline, in metrology, and in truth."

He stepped back from the rostrum.

That afternoon, by unanimous acclamation of the General Assembly, the sovereign nations of Earth signed the **Founding Charter of the Interstellar Astrobiological Survey (IAS)**.

Its mandate was absolute: to take the QRC relational navigation framework developed on the Pulsar Bench, combine it with the fusion energy technologies of the coming century, and begin the four-hundred-year construction of humanity’s first interstellar deep-survey starship:

**The IAS *Daedalus*.**
"""

CH21 = r"""# CHAPTER TWENTY-ONE
## The North Sea Horizon

August 14, 2058.

Twenty-five years after the launch of Project ARGONAUT. Thirty-two years after Ryan Vance bought a seven-watt edge development board in a Roanoke surplus shop.

On the jagged sandstone cliffs of Tantallon Castle, overlooking the cold, gray surf of the Firth of Forth on the eastern coast of Scotland, the morning wind blew hard off the North Sea, carrying the clean, briny smell of kelp and distant rain.

Dr. Ryan Vance stood at the edge of the ruin’s red ramparts, wrapped in a heavy tweed coat, his dark hair now completely silvered at the temples, his eyes squinting against the sea mist.

He was sixty-nine years old. His hands, though weathered and veined, were steady.

Beside him stood **Dr. Elena Vance**, now thirty-two years old: Chief Metrologist of the Sol Navigation Directorate and Lead Architect of the IAS Interstellar Propulsion Division.

She held an aerospace telemetry tablet in one hand, its screen linked via quantum laser crosslink to the Earth-Moon $L_2$ orbital shipyard four hundred thousand kilometers overhead.

"Ground stations in the Hebrides are locked onto the test beacon, Dad," Elena said, her voice rich with the calm authority of a seasoned director. "Ignition sequence is armed."

Two hundred miles above the Earth, near the Moon's shadow, the prototype **Deuterium-Helium-3 Magnetic Pinch Fusion Torch Engine** was preparing for its maiden relativistic test firing.

It was not a chemical rocket. It was a three-hundred-meter magnetic nozzle of high-temperature superconducting coils, confining a thermonuclear plasma at two hundred million degrees Kelvin, channeling the exhaust into a directed relativistic jet moving at **eight percent of the speed of light**.

"Look at the telemetry clock, Elena," Ryan said, pointing to the tablet.

On the screen, the timing pulse from the fusion core was disciplined not by an atomic clock in an Earth laboratory, but by the relational phase signals of three galactic millisecond pulsars: PSR J0337+1715, PSR B1937+21, and PSR J0437-4715.

The same relational clock Ryan had derived on his workbench in Blacksburg thirty-two years ago.

"The phase noise is zero point zero two picoseconds," Elena smiled, turning to him. "The three-body shape sphere is holding the magnetic pinch stable. The plasma isn't touching the walls."

"It never touches the walls," Ryan murmured. "There are no walls."

At 11:14 UTC, two hundred miles overhead in the deep sky, the fusion torch ignited.

To the naked eye on the Scottish coast, it appeared as a brilliant, steady sapphire-blue spark blooming near the daytime crescent of the Moon—a clean, piercing needle of pure light that outshone the morning stars.

The torch fired for three continuous minutes, delivering thirty thousand kilonewtons of relativistic thrust without a single millisecond of jitter.

Across the tablet screen scrolled the official confirmation from Lunar Gateway:
```
[SOL NAVIGATION DIRECTORATE // MAIDEN TORCH TRIAL]
PROPULSION TEST:       D-He3 MAGNETIC PINCH TORCH (MARK I)
EXHAUST VELOCITY:      0.082 c (24,600 km/s)
CONTINUOUS BURN:       180.00 SECONDS (100% THRUST EFFICIENCY)
RELATIONAL NAVIGATION: QRC FIXEDQP GUIDANCE SYSTEM NOMINAL
PHASE DRIFT:           < 0.012 picoseconds
INTERSTELLAR KEEL:     IAS DAEDALUS HULL COMMITTED AT L2 SHIPYARD
ESTIMATED LAUNCH:      CANONICAL MISSION WINDOW: 25TH CENTURY
```

Elena Vance lowered the tablet and looked out over the North Sea.

In her eyes, Ryan saw the entire future: the four-century campaign that would tame the outer planets, build the solar energy grids, freeze human bodies in isochoric stasis, and send the *Daedalus* out across the void toward the stars.

Ryan reached into the pocket of his coat.

He withdrew the small, heavy object he had carried with him for thirty-two years: the three-inch triangular prism of optical-grade fused silica, its quartz faces still carrying the faint, microscopic scratches of the Green Bank and Giles County test benches.

He held it out to Elena.

"Take it," Ryan said softly.

Elena looked down at the prism, then up at her father. "Dad... this was your reference standard."

"It was never mine, Elena," Ryan said, placing the heavy glass into her palm and closing her fingers around it. "It belonged to the universe. We just learned how to listen to it."

He looked out at the sapphire spark fading against the blue Scottish sky, where the keel of humanity's first starship was beginning to take shape.

"Space is not a room, Elena," Ryan said, a quiet, peaceful smile touching his lips. "It is the threshold of what we dare to reach."

The sea wind rose, carrying the white mist over the red stones of Tantallon, out across the gray water, toward the open horizon of the world.

---
"""

DOSSIER5 = r"""# INTER-ACT DOSSIER V
## The Gateway Bio-Quarantine Audit & The Daedalus Foundation
### Document Classification: United Nations Science Directorate / COSPAR Category V Final Certification
#### Date of Archival: November 22, 2043 | Location: Lunar Gateway Station & New York, USA

![IAS Daedalus Architecture & 400-Year Technology Cascade](assets/plate_07_dossier_5_daedalus_cascade.png)

### 1.0 MOLECULAR & STRUCTURAL ANATOMY OF *EXO-ARCHAEON EUROPAE*

Cryogenic transmission electron microscopy (Cryo-TEM) at eighty kilovolts, combined with sub-nanometer three-dimensional electron tomographic reconstruction, revealed the intact cellular architecture of the Europa ocean organisms extracted from Track 4,812:

```
================================================================================
TABLE 5.1: MOLECULAR ANATOMY OF EXO-ARCHAEON EUROPAE
================================================================================
Feature                         Biochemical Specification & Structural Metrics
--------------------------------------------------------------------------------
Cell Morphology                 Elongated rod (1.6 um length x 0.8 um diameter)
Membrane Architecture           Continuous tetraether lipid monolayer (5.2 nm thick)
Core Lipid Monomer              Caldarchaeol (GDGT-4 analogue) / Glycerol-1-Phosphate
Intracellular Minerals          50 nm Greigite (Fe3S4) magnetic nanocrystal chains
Energy Transduction Pathway     Chemiosmotic: H2 oxidation coupled to SO4(2-) reduction
Informational Genetic Polymer   Peptide Nucleic Acid (PNA) Double Helix
Backbone Architecture           Poly-N-(2-aminoethyl)glycine (AEG) neutral polyamide
Heterocyclic Base Pairs         2,6-Diaminopurine (D) : Uracil (U)
                                Isoguanine (iG) : Isocytosine (iC)
Enantiomeric Symmetry           Achiral (Lacks D/L-stereochemical asymmetry)
Replication Fidelity            Exonuclease proofreading equivalent (< 10^-7 error)
================================================================================
```

---

### 2.0 PROOF OF INDEPENDENT GENESIS

To establish beyond scientific challenge that *Exo-archaeon europae* represents an independent origin of life and not terrestrial spore contamination transported on prior robotic probes, four definitive molecular discriminators were verified:

1. **Backbone Stereochemistry:** Terrestrial bacteria and eukaryotes utilize glycerol-3-phosphate ($R$-stereochemistry) in their cell membranes; terrestrial archaea utilize glycerol-1-phosphate ($S$-stereochemistry) with branched isoprenoid chains. The Europa organisms share the archaeal glycerol-1-phosphate configuration, but their tetraether cores carry chain lengths and ring patterns completely unknown in terrestrial lipid databases.
2. **Peptide-Nucleic Backbone:** The genetic code is stored on an uncharged polyamide peptide backbone (PNA), devoid of the ribose or deoxyribose sugar-phosphate backbone universal to terrestrial biology.
3. **Alternative Nucleobases:** The use of 2,6-diaminopurine and isoguanine/isocytosine eliminates any possibility of horizontal gene transfer from terrestrial contamination.
4. **Achirality:** The genetic polymer exhibits no optical rotation under polarized circular dichroism, proving it evolved independently of the homochiral constraints of Earth's RNA world.

---

### 3.0 THE 400-YEAR TECHNOLOGICAL ROADMAP (THE DAEDALUS CASCADE)

```
================================================================================
TABLE 5.2: THE FOUR-CENTURY ROADMAP TO THE IAS DAEDALUS (2026–2450 AD)
================================================================================
Phase / Century    Key Technological Milestone              Propulsion & GNC State
--------------------------------------------------------------------------------
Phase 1 (2020s)    QRC Formulation & CislunarOS (Artemis-7) 7W Edge Silicon / SRIF
Phase 2 (2030s)    Project ARGONAUT & Callisto Staging      Graded Aerogel / Laser Seal
Phase 3 (2040s)    Discovery of Europan PNA / IAS Charter   Invariant Manifold Cruise
Phase 4 (2050s)    D-He3 Magnetic Pinch Fusion Torches     0.08 c Relativistic Exhaust
Phase 5 (22nd C)   Outer Solar System Industrial Grid       Beamed Laser Momentum Arrays
Phase 6 (23rd C)   Isochoric Stasis & Epigenetic Repair     Multi-Decade Human Torpor
Phase 7 (25th C)   Launch of IAS Daedalus Starship          Relativistic Interstellar Probe
================================================================================
```

*Certified by the United Nations Science Directorate and COSPAR,*
**Dr. Aris Thorne**, Lead Astrobiologist, NASA-JPL
**Dr. Elena Vance**, Chief Metrologist, Sol Navigation Directorate
"""

def main():
    files = [
        ("Chapter_18_The_Quarantine_Gate.md", CH18),
        ("Chapter_19_Life_Is_Simple.md", CH19),
        ("Chapter_20_The_Rungs_Above_the_Water.md", CH20),
        ("Chapter_21_The_North_Sea_Horizon.md", CH21),
        ("Dossier_Act_V.md", DOSSIER5),
    ]
    for filename, content in files:
        path = os.path.join(MANUSCRIPT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Generated: {filename} ({len(content.split())} words)")

if __name__ == "__main__":
    main()
