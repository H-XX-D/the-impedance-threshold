#!/usr/bin/env python3
"""
Generate Act IV: Chapters 13-17 and Dossier IV from scratch.
Author: Todd Hendrixx
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

CH13 = r"""# CHAPTER THIRTEEN
## The Dive into the Belt

The separation burn at Callisto had dropped the Europa Skimmer onto a steeply plunging transfer ellipse.

For one hundred and twelve hours, the twelve-hundred-kilogram robotic dart fell inward toward Jupiter, crossing two million kilometers of gravitational gradient. With every passing hour, the giant planet grew larger in the forward navigation cameras—a terrifying, striated marble of ochre, cream, and rust-colored ammonia clouds, its Great Red Spot churning like an open wound against the south tropical zone.

Inside the skimmer's sealed central avionics vault, behind twenty-five millimeters of graded aluminum-boron shielding, the radiation sensors began ticking.

At seventy hours into the dive, crossing the orbit of Ganymede, the ambient dose rate was four millirads per hour.

At ninety-six hours, plunging past the orbit of Europa itself into the inner Jovian magnetosphere, the dose rate exploded. Relativistic electrons trapped in Jupiter’s multi-Tesla dipolar magnetic field slammed into the skimmer's titanium skin, creating a blistering shower of secondary bremsstrahlung X-ray photons:

```
[RADIATION MONITOR: SENSOR BAY 01]
MAGNETIC FIELD STRENGTH: 412 MICROTESLA
TRAPPED ELECTRON FLUX (> 10 MeV): 2.4e+08 cm^-2 s^-1
AMBIENT IONIZING DOSE RATE: 480 RADS / HOUR
INTEGRATED MISSION DOSE: 8.42 KILORADS
SILICON JUNCTION LEAKAGE CURRENT: +1.2% (WITHIN NOMINAL)
AVIONICS STATUS: NO SINGLE-EVENT LATCHUP DETECTED
```

The skimmer’s guidance core—fabricated on a 28-nanometer Fully Depleted Silicon-on-Insulator (FD-SOI) radiation-hardened process—did not blink. Its registers, hardened by dual-interlocked storage cells, shrugged off the ionizing proton strikes.

Every six minutes, the Square-Root Information Filter updated the state vector. It did not use star trackers; the optical sensors were shuttered behind motorized tantalum shields to protect their microchannel plates from radiation damage. Instead, the skimmer tracked its descent using its internal fiber-optic gyro platform and high-frequency radar altimeter bounces off Europa’s fractured ice ridges.

At 02:14 UTC on May 4, 2040, Europa filled the entire sky.

Through the forward terrain cameras, the ice world was breathtaking, desolate, and cruel. An unbroken crust of brilliant white water ice, crisscrossed by thousands of miles of reddish-brown linear fractures—cycloids, ridges, and bands of mineral salts extruded from the abyss below.

Two hundred kilometers ahead, illuminated by the harsh, distant slant of sunlight, the plume rose into the black sky: a towering, ghostly pillar of ice crystals venting from the Manannán Chaos.

The flight computer initiated the braking burn.

At 02:41:10 UTC, forty seconds before plume entry, the 4.4-kilonewton bipropellant main engine roared to life. A continuous, violent deceleration of fourteen hundred and two meters per second bled off the hyperbolic approach speed, tailoring the encounter to precisely **two thousand two hundred and fourteen meters per second**.

The engine shut down. The fuel lines purged with high-pressure nitrogen.

`APPROACH ALTITUDE: 50.18 KILOMETERS`  
`RELATIVE VELOCITY: 2,214.2 METERS / SECOND`  
`TARGET: PLUME_03 CORE CONDUIT`  
`TIME TO INTERCEPT: T-MINUS 42 SECONDS`  
`COLLECTOR SHUTTER: COMMAND OPEN`  

With a crisp mechanical click, the heavy titanium protective shield on the skimmer’s nose swung back into its recessed housing.

The graded silica aerogel cassette was exposed directly to the oncoming vacuum.
"""

CH14 = r"""# CHAPTER FOURTEEN
## Forty-Two Seconds

The encounter was silent, violent, and brief.

At 02:42:00 UTC, traveling at two point two kilometers per second, the Europa Skimmer punched through the outer vapor sheath of Plume #3 at an altitude of fifty point two kilometers above the shattered ice of Manannán Chaos.

Inside the aerogel collector bay, three piezoelectric micro-acoustic sensors mounted on the titanium backplate registered the immediate, drumming impact of incoming cryogenic brine particles.

*Ping. Ping-ping. P-p-p-ping.*

It was the sound of an alien ocean striking silica smoke.

Fourteen thousand eight hundred and twelve discrete grains of ice—ranging from ten to two hundred microns in diameter, frozen at seventy Kelvin in the vacuum above the plume vent—slammed into the open face of the graded aerogel cassette.

As Ryan Vance had derived at Plum Brook, the physics of graded deceleration held true.

When a fifty-micron ice grain entered the aerogel at twenty-two hundred meters per second, it did not hit a solid wall. It struck a mesoporous matrix of silica nanoparticles with an initial density of just two point one milligrams per cubic centimeter—ninety-nine point eight percent vacuum.

The grain carved a microscopic, conical track into the gel. The outer skin of the ice grain instantly sublimated into vapor along the track walls, absorbing the kinetic shock through latent heat of phase change.

The core of the grain—the inner twenty microns containing preserved cellular material—decelerated over five millimeters in less than six microseconds. The peak core temperature never exceeded two hundred and fourteen Kelvin: negative fifty-nine degrees Celsius.

The ocean stayed frozen.

Beside the aerogel cassette, the miniature quadrupole mass spectrometer sampled the ambient gas entering the intake horn during the core transit:

```
[QUADRUPOLE MASS SPECTROMETER: FLASH SPECTRUM]
MASS CHANNEL 18 (H2O):  PEAK PARTIAL PRESSURE 4.2e-07 mbar
MASS CHANNEL 28 (CO/N2): 8.1e-09 mbar
MASS CHANNEL 34 (H2S):   1.4e-08 mbar [REDUCED SULFUR DETECTED]
MASS CHANNEL 44 (CO2):   6.2e-08 mbar
MASS CHANNELS 74-112:    DISTINCT ALIPHATIC FRAGMENTS DETECTED
```

At 02:42:42 UTC—precisely forty-two seconds after entry—the skimmer emerged from the eastern edge of the plume back into the clean, hard vacuum of space.

`PLUME TRANSIT COMPLETE: DURATION 42.0 SECONDS`  
`TOTAL GRAIN IMPACTS RECORDED: 14,812`  
`AEROGEL MATRIX INTEGRITY: 99.4%`  
`COLLECTOR SHUTTER: COMMAND SEAL AND LATCH`  

The titanium protective shutter snapped shut, its dual micro-latches engaging with an audible click through the frame. Liquid nitrogen cooling loops circulating through the aerogel cassette baseplate chilled the matrix to seventy-one point four Kelvin.

Twenty seconds later, the bipropellant main engine ignited for the climb burn.

A thirteen-hundred-and-eighty-meter-per-second acceleration boosted the skimmer out of Europa's gravity well, placing the precious cargo onto the long, arcing climb back toward the cold radiation sanctuary of Callisto.
"""

CH15 = r"""# CHAPTER FIFTEEN
## The Glass Seam in the Dark

May 12, 2040.

Eight days after skimming the plume of Europa, the Europa Skimmer glided into the shadow of the Callisto Carrier Depot, closing at five centimeters per second.

In the dead stillness of Callisto orbit, under the cold light of Jupiter, the skimmer’s docking probe slid into the depot’s forward capture cone. Mechanical latches engaged, drawing the two craft together into a rigid structural lock.

The automated transfer sequence began immediately.

Inside the depot's central bay, the environment was held at the vacuum of deep space: $10^{-11}$ torr. No human hands were there to assist; every motion was driven by titanium servomotors running under autonomous microcode.

A robotic transfer arm extended into the skimmer’s collector housing, unlatching the rectangular graded aerogel cassette. The arm retracted smoothly, carrying the frozen sample across the vacuum gap into the open throat of **Canister 1**.

The cassette slid home into its internal titanium retention fingers with a soft, positive metallic click.

Chilled heat pipes coupled instantly to the cassette baseplate, maintaining the sample at eighty Kelvin.

Then, a motorized manipulator lifted the circular Ti-6Al-4V titanium lid from its sealed storage caddy and positioned it over the canister opening. A pure gold crush gasket, zero point five millimeters thick, sat between the mating flanges.

The lid pressed down under eight hundred newtons of pneumatic force, seating the gold gasket against the knife-edge rim.

---

### The Laser Weld

Through the depot's internal inspection cameras, the focusing head of the two-hundred-watt **ytterbium fiber laser** swung into position directly above the seam, its optical collimator positioned three millimeters from the titanium joint.

Inside the avionics bay, the welding executive verified the pre-weld telemetry:

`WELD CHAMBER PRESSURE: 1.2e-11 TORR [ULTRA-HIGH VACUUM]`  
`SAMPLE TEMPERATURE: 74.2 KELVIN`  
`OPTICAL PYROMETER CALIBRATION: NOMINAL`  
`HELIUM-4 TRACER INJECTION: READY`  

The injection micro-valve clicked open for two hundred milliseconds, admitting precisely fifty standard cubic centimeters of ultra-pure helium-4 tracer gas into the canister cavity, bringing its internal pressure to half an atmosphere.

The laser fired.

An intense, brilliant pinprick of pure infrared light—ten hundred and seventy nanometers—ignited along the circular seam. A narrow, molten pool of titanium-aluminum-vanadium alloy formed instantly in the hard vacuum, vaporizing microscopic surface contaminants without spatter.

The collimator head tracked around the circumference of the canister at twenty-four millimeters per second.

In precisely **twenty-eight seconds**, the laser completed the full three-hundred-and-sixty-degree circle, overlapping the start point by three millimeters to ensure complete weld penetration.

The beam shut down. The molten titanium froze in the vacuum in less than half a second, forming a smooth, silvery, hermetic bead with zero porosity.

Then came the trial of truth.

A miniature quadrupole mass spectrometer sniffer head swung down to within two millimeters of the freshly solidified weld seam. The sensor chamber pumped down, sniffing for the single molecule that would betray a failure: helium-4.

On Earth, forty-five light-minutes away, the telemetry stream plotted on the screens in Building 30:

```
[POST-WELD QUALIFICATION SNIFFER SCAN]
HE-4 BACKGROUND PARTIAL PRESSURE: < 1.0e-13 mbar
SEAM TRANSIT VELOCITY: 5.0 mm / s
PEAK HELIUM-4 SIGNAL DETECTED: NONE (< 1.0e-12 mbar*L/s)
CALCULATED HERMETIC LEAK RATE: < 1.0e-11 mbar*L/s
STRUCTURAL EVALUATION: ZERO PORES // ZERO MICRO-CRACKS
CANISTER 1 CERTIFICATION: HERMETICALLY SEALED
```

In Houston, Kenji Sato bowed his head, his hands trembling slightly on the edge of the console.

"The seam is solid," Kenji said. "The ocean is locked in a vault of titanium. It can fly to Earth."
"""

CH16 = r"""# CHAPTER SIXTEEN
## The Silent Arc

January 20, 2041. Mission Day 0.

In orbit around Callisto, the two-stage storable-bipropellant Return Stack detached from the carrier depot.

At 06:14 UTC, its four-thousand-newton main engine ignited for the departure burn. Burning for one thousand and sixty-four continuous seconds, the engine accelerated Canister 1 out of the Jovian system on an escape hyperbola of **four point eight kilometers per second**, aiming directly across the solar system toward the inner worlds.

Once the burn was complete, the empty departure stage detached with a pyrotechnic severing collar, drifting away into the deep dark.

What remained was the cruise vehicle: a compact, one-hundred-and-sixty-five-kilogram stack comprising Canister 1, its cold-gas attitude control thrusters, an X-ray pulsar timing array, and an onboard guidance computer running CislunarOS.

And then, the radio fell completely silent.

To conserve its limited lithium-carbon-monofluoride batteries, Canister 1 was designed to operate in total autonomous radio silence across its entire **nine-hundred-and-eighty-day cruise** from Jupiter to Earth. It would receive zero commands from ground controllers. It would request no Doppler tracking from the Deep Space Network.

It was a ghost in the void.

---

### The Senate Crucible

In the spring of 2042, four hundred and fifty days into the silent cruise, the political storm broke over Washington.

In a crowded, wood-paneled hearing room on Capitol Hill, Senator Thomas Sterling, Chairman of the Senate Subcommittee on Space, leaned toward his microphone, glaring across the witness table at Dr. Ryan Vance and Dr. Elena Rostova.

"Dr. Vance," Senator Sterling’s voice echoed off the marble columns. "Your agency has spent one point six billion dollars of taxpayer money on Project ARGONAUT. And according to the testimony we heard this morning from the Government Accountability Office, NASA has had zero radio communication with that canister for fourteen continuous months."

Ryan sat upright in his chair, wearing a dark gray suit that felt stiff and uncomfortable on his frame.

"That is correct, Senator," Ryan replied calmly. "The mission architecture is fully autonomous by design."

"Autonomous?" Sterling scoffed, waving a thick sheaf of audit papers. "In plain English, Dr. Vance, you launched a ten-kilogram box of frozen slush from Jupiter, aimed it at the planet Earth, and threw away the steering wheel! You have no radar tracking. You have no telemetry downlink. For all anyone in this room knows, Canister 1 suffered an attitude thruster failure a year ago and is currently tumbling into the Sun!"

"It is not tumbling into the Sun, Senator," Elena Rostova interjected, her voice icy and sharp. "The vehicle carries an autonomous Square-Root Information Filter. Every forty-eight hours, it takes an eight-hour integration fix on three millisecond pulsars—PSR J0437-4715, B1937+21, and B1821-24. It measures its position in relational phase space to within three kilometers, calculates its trajectory trims using a receding-horizon quadratic planner, and fires its cold-gas thrusters only when a correction is mathematically required."

"And what if your software has a bug, Dr. Rostova?" Sterling countered. "What if an unexpected force pushes it off course and nobody on Earth is there to see it?"

---

### The Sixteen-Year-Old’s Discovery

Two days after the hearing, in the quiet study of Ryan’s house in Blacksburg, sixteen-year-old **Elena Vance** sat cross-legged on the floor, surrounded by printed telemetry dumps from Canister 1’s pre-departure checkout logs.

She had her father’s intense focus, her dark hair pulled back into a ponytail, pencil shavings littering the rug beside her laptop.

"Dad," she said, looking up as Ryan walked in with two cups of cider. "Look at the reaction control logs from Mission Day forty-two."

Ryan set down the mugs, kneeling beside her. "What did you find, Ellie?"

"The cold-gas thrusters fired twice on Day forty-two," she said, pointing a slender finger at a column of micro-pulse timestamps. "A total impulse of point one eight meters per second. But look at the pitch-axis angular acceleration between the burns. There's an unmodeled angular acceleration: plus zero point zero zero four degrees per hour."

Ryan frowned, leaning closer. "Outgassing from the multi-layer insulation?"

"No," Elena said, shaking her head. "I calculated the outgassing decay curve; it drops as one over square-root of time and should have hit zero by Day thirty. Look at the solar aspect angle. When the canister crossed three point two astronomical units, the Sun's rays hit the asymmetric bevel of the diamond X-ray sensor windows."

She pulled over her notebook, covered in neat, elegant derivations:

$$\boldsymbol{\tau}_{\text{photon}} = \frac{\Phi_{\text{solar}}}{c} A \left[ (1 - \rho_s) \hat{\mathbf{s}} + 2 \rho_s (\hat{\mathbf{s}} \cdot \hat{\mathbf{n}}) \hat{\mathbf{n}} \right] \times \mathbf{r}_{\text{offset}}$$

"The photon radiation pressure on the diamond window," Elena explained, her eyes shining with quiet certainty, "is producing a net torque of **plus six point one two micronewton-meters**. It's tiny, but over nine hundred days, the cumulative momentum will saturate the pitch-axis cold-gas budget by Day eight hundred. The vehicle will run out of nitrogen before it reaches Earth."

Ryan stared at his sixteen-year-old daughter. A deep, prideful chill ran through his chest.

"You're right," Ryan whispered.

Within twenty-four hours, the calculation was verified by NASA Flight Dynamics. A single, short, one-way command patch was prepared and transmitted across the Deep Space Network at maximum transmitter power, timed to intersect Canister 1’s scheduled bi-monthly wake-up window.

The patch offset the solar trim attitude by two point four degrees, balancing the photon torque against the solar panel reflex.

The nitrogen was saved. The ghost continued its silent, unswerving flight toward home.
"""

CH17 = r"""# CHAPTER SEVENTEEN
## Gravity's Needle

September 27, 2043. Mission Day 980.

After two point seven years of silent, uncommanded cruise across six hundred and twenty-eight million kilometers of interplanetary void, Canister 1 crossed the orbit of the Moon.

It was closing on the Earth-Moon system at nine point seven two kilometers per second.

In Mission Control, Houston, the flight loop was packed with representatives from NASA, ESA, JAXA, and the United Nations Office for Outer Space Affairs. Standing beside Flight Director Sarah Lin were Ryan Vance, Elena Rostova, Kenji Sato, and seventeen-year-old Elena Vance.

At 14:12 UTC, a high-frequency telemetry carrier burst onto the Goldstone display:

```
[DEEP SPACE NETWORK: GOLDSTONE DSS-14]
SIGNAL ACQUISITION: CANISTER 1 RETURN STACK
CARRIER FREQUENCY: 8.412 GHz [X-BAND] | SNR: +18.4 dB
TELEMETRY STATUS: AUTONOMOUS CAPTURE SEQUENCE ARMED
TRAJECTORY INTEGRATION: DAY 980.41
TIME TO PERIGEE: 02 HOURS 14 MINUTES
ESTIMATED MISS DISTANCE FROM TARGET CORRIDOR: 412 METERS
```

"Four hundred meters," Marcus Thorne breathed, his hands resting lightly on the FIDO console. "After nine hundred and eighty days and six hundred million kilometers without a human touching the stick. The square-root filter held the corridor to four hundred meters."

---

### The Perigee Burn

At 16:26 UTC, Canister 1 reached its periapsis altitude: six hundred kilometers above the blue curve of the South Pacific Ocean.

The capture stage bipropellant engine ignited with a silent, blinding thrust of three thousand eight hundred and sixty meters per second. The burn lasted three hundred and twelve seconds, curving the hyperbolic trajectory into an eccentric capture ellipse that arced outward toward the Moon.

At burnout, the capture engine stage detached, its residual propellant safely venting to ensure it would never collide with the vehicle.

What remained was the final jewel: Canister 1, weighing nine point nine eight kilograms.

Instead of fighting the gravity of the Earth and the Moon with massive rocket stages, the autonomous guidance software used the natural phase-space topography of the three-body problem.

It targeted an **Invariant Manifold**: a delicate, chaotic gravitational corridor where the gravitational pull of the Earth, the Moon, and the Sun balanced to zero. Riding the manifold’s stable manifold tube, Canister 1 executed two small cold-gas trim burns—totaling just thirty-four meters per second—gliding gracefully into the **Near-Rectilinear Halo Orbit (NRHO)** of the Moon.

Ahead, gleaming in the harsh cislunar sunlight, hung the white pressurized modules, solar arrays, and radiator wings of the **Lunar Gateway Station**.

At 22:41 UTC, Canister 1 closed to within fifty meters of Gateway’s robotic capture arm.

The station’s Canadian-built robotic manipulator reached into the dark, its capture snare aligning with the canister’s grapple fixture.

With a soft, metallic chime that resonated through the station's pressurized hull, the snare closed.

`GATEWAY ROBOTIC SYSTEM: CAPTURE CONFIRMED`  
`CANISTER 1 SECURED IN AIRLOCK 01`  
`CONTAINMENT INTEGRITY: HERMETIC SEAL VERIFIED`  
`PROJECT ARGONAUT: SAMPLE RETURN COMPLETE`  

In Mission Control, Houston, four hundred engineers rose to their feet in a deafening, thunderous standing ovation. Paper flight logs were thrown into the air like confetti.

Ryan Vance stood motionless amidst the cheering crowd. He looked down at his daughter Elena, who was crying quiet tears of relief, her arms wrapped around his waist.

Beside them, Elena Rostova looked at Ryan, her dark eyes shining with vindication.

"The dart came home, Ryan," she whispered.

"It came home, Elena," Ryan said, his voice quiet against the roar of the room. "Now we find out who is waiting in the dark."
"""

DOSSIER4 = r"""# INTER-ACT DOSSIER IV
## The Europa Plume Harvest & The 980-Day Ghost Run
### Document Classification: NASA-JPL-ESA Project ARGONAUT Flight Operations Report
#### Date of Archival: October 1, 2043 | Location: Lunar Gateway Station & Goldstone DSN

![Europa Plume Encounter & 980-Day Autonomous Ghost Run](assets/plate_05_dossier_4_plume_ghost_run.png)

### 1.0 MANANNÁN REGION PLUME SAMPLING ACOUSTIC SPECTRUM

During the forty-two-second skimming pass through the core of Plume #3 on May 4, 2040, three piezoelectric micro-acoustic sensors mounted on the titanium backplate of the aerogel cassette registered the impact signature of incoming cryogenic brine particles.

*Manannán Region Plume Encounter Log: Altitude 50.18 km, Velocity 2,214.2 m/s after a 1,402.6 m/s braking burn (hyperbolic flyby; Europa escape speed at 50 km is 1,994 m/s), Intercept duration 42.0 seconds. 14,812 discrete ice grains captured with core temperatures below 220 K; grain skins ablated along the track walls. Detailed density and acoustic profile documented in Plate ARG-ENC-1443 above.*

#### 1.1 In-Situ Mass Spectrometer Rapid Flash Analysis
The miniature quadrupole mass spectrometer mounted beside the aerogel collector sampled ambient vapor molecules during the core transit:

* **Mass Channel 18 ($H_2O$):** Peak partial pressure $4.2 \times 10^{-7}\text{ mbar}$.
* **Mass Channel 28 ($CO / N_2$):** Partial pressure $8.1 \times 10^{-9}\text{ mbar}$.
* **Mass Channel 34 ($H_2S$):** Partial pressure $1.4 \times 10^{-8}\text{ mbar}$ (consistent with seafloor sulfur chemistry; not by itself proof of it).
* **Mass Channel 44 ($CO_2$):** Partial pressure $6.2 \times 10^{-8}\text{ mbar}$.
* **Mass Channels 74–112 (Aliphatic Fragments):** Significant organic signatures detected, including propylamine and glycine precursors.

#### 1.2 Graded Silica Aerogel Deceleration Mechanics
The capture of hypervelocity ice grains at $2,214\text{ m/s}$ left the grain cores thermally unaltered by utilizing a continuously graded mesoporous silica matrix:

```
[AEROGEL DENSITY & COMPRESSIVE PROFILE]
FRONT FACE DENSITY (z = 0 mm):    2.1 mg/cm^3 (Knudsen aerodynamic cushion)
MID-DEPTH DENSITY (z = 15 mm):    12.4 mg/cm^3 (Track collapse & energy absorption)
BASEPLATE DENSITY (z = 30 mm):    48.6 mg/cm^3 (Structural support & heat sink)
POROSITY FRACTION:                99.82% by volume
COMPRESSIVE STRENGTH:             0.04 MPa (front) to 2.8 MPa (base)
MEAN TRACK LENGTH MEASURED:       4.82 mm +/- 0.41 mm
MEAN GRAIN DECELERATION:          5.1 x 10^8 m/s^2 (Stopping time: ~5 microseconds)
CALCULATED PEAK CORE TEMP:        214.2 Kelvin (Core preserved; grain skin ablates along track)
```

---

### 2.0 CANISTER 1: 980-DAY RETURN LOG (SELECTED ENTRIES)

Across roughly 1.2 billion kilometers of flight from Callisto orbit to the Earth-Moon system, Canister 1 and its Return Stack operated in complete radio silence and received no ground commands. The stack made two autonomous main-engine burns (departure, Day 0; Earth capture, Day 973), each recorded in the journal before issue and cleared by the diverse Cartesian verifier. Between them, the flight computer woke every 48 hours, read an 8-hour X-ray pulsar integration into its square-root navigation filter, and commanded a cold-gas trim only when the receding-horizon planner found a correction worth making and the verifier cleared it:

```
========================================================================================
BURN #  MISSION DAY     SOLAR DIST (AU) LAST FIX        DURATION (S)    DELTA-V (M/S)   CUMULATIVE COLD GAS
========================================================================================
DEP     Day 000         5.45 AU         PSR J0437-4715  1,064 s (main)  4,800.0 m/s     (departure stage)
01      Day 004         5.45 AU         PSR B1937+21    2,883 s (cold)  2.0970 m/s      2.0970 m/s
05      Day 042         5.43 AU         PSR J0030+0451  248 s (cold)    0.1800 m/s      2.2779 m/s
09      Day 120         5.28 AU         PSR B1821-24    112 s (cold)    0.0814 m/s      2.3593 m/s
18      Day 412         4.12 AU         PSR J0437-4715  314 s (cold)    0.2280 m/s      2.5873 m/s
24      Day 780         2.18 AU         PSR B1937+21    184 s (cold)    0.1337 m/s      2.7210 m/s
CAP     Day 973         1.01 AU         PSR J0437-4715  312 s (main)    3,860.0 m/s     (capture stage)
31      Day 979         1.00 AU         Earth/Moon Limb 48 s (cold)     0.0348 m/s      2.7558 m/s
========================================================================================
```
"""

def main():
    files = [
        ("Chapter_13_The_Dive_into_the_Belt.md", CH13),
        ("Chapter_14_Forty_Two_Seconds.md", CH14),
        ("Chapter_15_The_Glass_Seam_in_the_Dark.md", CH15),
        ("Chapter_16_The_Silent_Arc.md", CH16),
        ("Chapter_17_Gravitys_Needle.md", CH17),
        ("Dossier_Act_IV.md", DOSSIER4),
    ]
    for filename, content in files:
        path = os.path.join(MANUSCRIPT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Generated: {filename}")

if __name__ == "__main__":
    main()
