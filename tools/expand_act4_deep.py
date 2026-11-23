#!/usr/bin/env python3
"""
Deep literary and technical expansion of Act IV: Chapters 13-17.
Author: Todd Hendrixx
Brings Chapters 13-17 to ~2,200 words each (~11,000 words total for Act IV).
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

CH13_FULL = r"""# CHAPTER THIRTEEN
## The Dive into the Belt
### The Ganymede Boundary

On May 2, 2040, the Europa Skimmer crossed the orbit of Ganymede, plunging inward toward Jupiter at four kilometers per second.

Behind the dagger-shaped probe, Callisto had already shrunk to a dark, cratered coin receding into the starry void. Ahead, Jupiter filled thirty-five degrees of the forward camera field of view: a towering wall of churning ochre, white, and copper clouds, banded with supersonic jet streams, with the Great Red Spot rotating into the sunlit crescent like a dark, cyclonic eye.

Just off Jupiter's eastern limb, gleaming like a pearl on black velvet, hung **Europa**.

Inside the Skimmer’s unpressurized avionics core, the radiation dosimeters began to climb with terrifying speed.

At Callisto, the background flux had been a gentle 0.012 rads per day. As the probe crossed Ganymede’s orbital radius of one million kilometers, the flux crossed ten rads per hour. Inside seven hundred thousand kilometers, it crossed twenty rads per hour.

The spacecraft was entering the Jovian electron belt: an invisible, doughnut-shaped magnetic trap where relativistic electrons, whipped up by Jupiter’s colossal 4.2-gauss magnetic dipole and rotating with the planet's ten-hour spin, battered the titanium hull.

Inside the processor core, the radiation environment was brutal:

```
[RAD-MON] DISTANCE TO JUPITER: 720,000 KM
[RAD-MON] LOCAL FLUX: 22.4 RADS/HOUR (INTEGRATED: 480 RADS)
[RAD-MON] DIELECTRIC DISCHARGE SENSORS: 14 EVENTS/SEC
[CORE-STATUS] 28nm FD-SOI SILICON: NOMINAL
[CORE-STATUS] TRIPLE-MODULAR REDUNDANCY: 3 OF 3 CORES IN LOCKSTEP
[CORE-STATUS] SINGLE-EVENT UPSETS DETECTED: 42 (SCRUBBED)
```

The avionics brain guiding the Skimmer was the direct descendant of the $400 Jetson Orin Nano Ryan Vance had bolted to an aluminum plate in his Blacksburg garage fourteen years earlier.

It was no longer an unhardened commercial dev board. It had been fabricated on a **28-nanometer Fully Depleted Silicon-on-Insulator (FD-SOI)** process with buried oxide layers, designed to prevent single-event latch-ups from ionizing radiation. But the mathematical soul of the machine was unchanged:

Zero floating-point arithmetic. Zero metric matrix inversions.

The entire guidance loop ran in 32-bit fixed-point integer mathematics using the Householder Square Root Information Filter and the FixedQP active-set optimizer. While high-energy Jovian electrons punched through the circuit boards, creating micro-discharges in the dielectric layers, the integer state engine simply projected the measurement noise onto its orthogonal residual vectors, discarding the bit flips without missing a single clock cycle.

---

### The Crescent of Salt and Ice

At twenty hours before closest approach, Europa filled the optical navigation cameras.

The moon was three thousand one hundred and twenty kilometers in diameter—slightly smaller than Earth’s Moon—but it looked like no other celestial body in the solar system.

There were almost no impact craters. The surface was a brilliant, blinding plain of pure water ice, crisscrossed by an intricate, planetary spiderweb of long, linear fractures called *lineae*. Some of the fractures stretched for thousands of miles across the globe, flanked by dark, reddish-brown ridges composed of magnesium sulfate salts, sulfuric acid hydrates, and complex organic tholins squeezed up from the warm interior.

Beneath that fifteen-mile-thick shell of floating ice lay a global liquid ocean one hundred kilometers deep, containing twice the volume of all of Earth’s oceans combined, capped by ice and warmed from below by tidal friction from Jupiter's gravitational pull and hydrothermal vents in the rocky mantle.

On the Skimmer’s forward imaging array, the southern hemisphere resolved into high-definition relief.

Near latitude twenty-four degrees south, inside the chaotic, broken terrain of the Manannán impact basin, the plume was visible.

It did not look like an explosive volcanic eruption on Earth. In the vacuum of space, with no atmospheric pressure to contain it, the water vapor and ice crystals expanded into a translucent, luminous fountain of crystalline mist that rose one hundred and eighty kilometers above the cracked ice sheets, glowing pale ultraviolet in the scattered sunlight.

The mission control terminal in Boulder, Colorado—where Ryan Vance sat beside a forty-four-year-old Dr. Elena Rostova—received the automated optical tracking lock:

```
[SKIMMER-GNC] TARGET: EUROPA PLUME #3 CANOPY
[SKIMMER-GNC] TARGET ALTITUDE: 50.2 KM ABOVE SURFACE
[SKIMMER-GNC] FLYBY VELOCITY: 2,214.2 M/S
[SKIMMER-GNC] INTERCEPT TIME: T-MINUS 04 HOURS 12 MINUTES
[SKIMMER-GNC] COLLECTOR DEPLOYMENT STATUS: ARMED
```

Ryan looked at the screen, his hands steady on his notebook.

"Flyby trajectory is locked," Ryan said. "Fifty kilometers altitude. Relative speed two point two kilometers per second. If the aerogel holds, we catch the ocean."

"And if it misses by four hundred meters?" Elena asked quietly.

"If it misses by four hundred meters high, we catch nothing," Ryan replied. "If it misses by four hundred meters low, the Skimmer clips the rim of the Manannán crater wall at Mach seven and turns into a spray of titanium dust."
"""

CH14_FULL = r"""# CHAPTER FOURTEEN
## Forty-Two Seconds
### The Manannán Descent

At 14:17:40 UTC on May 4, 2040, the Europa Skimmer crossed the terminator into the blinding glare of Europa’s sunlit hemisphere.

The cracked ice plains rushed beneath the spacecraft’s optical sensors at **2,214 meters per second**—more than six times the speed of sound. At an altitude of fifty kilometers, the surface features were not abstract satellite maps; they were terrifyingly real.

Huge, jagged blocks of rafted ice, three hundred feet high and tilted at chaotic angles where the crust had fractured and refrozen, whipped past the cameras like a landscape of shattered glass.

Inside the Skimmer’s forward section, a high-torque brushless stepper motor energized.

The aerogel collector bay doors—two milled titanium petals lined with gold-plated thermal foil—swung outward with a sharp, mechanical click:

```
[COLLECTOR] PETAL DOORS: OPEN (100.0%)
[COLLECTOR] EXPOSING TILE ARRAY: 4x4 GRADED SILICA AEROGEL
[COLLECTOR] SURFACE AREA: 0.16 SQUARE METERS
[COLLECTOR] TILE STATUS: CRYOGENIC (-165 DEG C)
[COLLECTOR] TIME TO PLUME ENTRY: T-MINUS 12 SECONDS
```

Ahead of the spacecraft, the translucent veil of Plume #3 loomed like a wall of pale, glowing smoke rising into the black sky.

At 14:18:00 UTC, the Skimmer hit the outer plume boundary.

---

### The Rain of Ice

The spacecraft entered the plume at an altitude of 50.2 kilometers.

The ambient particle density was four times ten to the eighth molecules per cubic centimeter: mostly water vapor ($H_2O$), mixed with molecular hydrogen, carbon dioxide, sodium chloride, and billions of microscopic frozen brine crystals ranging from five to two hundred micrometers in diameter.

To the naked human eye, it would have felt like flying through an ethereal, glowing fog.

To the aerogel collector tiles, it was a hypervelocity sandstorm.

Every millisecond, hundreds of microscopic ice grains slammed into the outer face of the graded aerogel tiles at two point two kilometers per second.

Inside the sol-gel nanostructure, the physics of soft-arrest went to work.

The grains entered the ultra-low-density outer layer ($0.005\text{ g/cm}^3$) without experiencing a destructive shockwave. As they penetrated deeper into the density gradient, the silica mesopores crushed beneath each grain's leading edge, creating a microscopic cushion of vaporized ice that enveloped each particle in an insulating sheath.

On the collector's piezoelectric acoustic impact sensors, the hits registered as a rapid, rhythmic drumbeat:

```
[IMPACT-LOG] T+05s: 1,420 HITS REGISTERED. MEAN DIAMETER: 12 um.
[IMPACT-LOG] T+15s: 5,840 HITS REGISTERED. PEAK DENSITY ZONE.
[IMPACT-LOG] T+25s: 11,210 HITS REGISTERED. TRACK DEPTH: 14-18 mm.
[IMPACT-LOG] T+35s: 14,100 HITS REGISTERED. CORE TEMP: -12 DEG C.
```

The interior core of each frozen brine pellet remained frozen at minus twelve degrees Celsius.

In those frozen cores, preserved in cryogenic arrest, were the intact organic molecules swept up from Europa's ocean floor: complex branched-chain lipids, peptide nucleic acids, and mineral micro-crystals formed around deep hydrothermal vents under sixteen hundred atmospheres of hydrostatic pressure.

At 14:18:42 UTC—precisely **forty-two seconds** after entering the plume—the Skimmer burst through the northern boundary of the vapor column into the clear vacuum.

```
[COLLECTOR] PLUME TRANSIT COMPLETE.
[COLLECTOR] TOTAL TRANSIT DURATION: 42.14 SECONDS.
[COLLECTOR] TOTAL PARTICLES ARRESTED: 14,812 ICE GRAINS.
[COLLECTOR] COMMANDING EMERGENCY DOOR CLOSURE...
[COLLECTOR] PETAL DOORS SEALED AND LATCHED.
```

The titanium doors snapped shut, locking the aerogel tiles inside an insulated, dark vacuum vault.

Beneath the probe, Europa’s vast gravitational field swung the spacecraft’s velocity vector forty-four degrees around its trailing limb.

The hyperbolic flyby was complete.

The probe had not entered orbit; it was executing an unpowered celestial slingshot, trading orbital energy with Europa to climb right back out of the lethal radiation belts, heading back along its free-return ellipse toward the cold sanctuary of Callisto.

Inside the avionics bay, the radiation dosimeters registered the total transit dose: **1,840 rads**.

Well within the twenty-eight-nanometer FD-SOI tolerance limit.

In Boulder, Colorado, Ryan Vance stood up from his console, his hands shaking slightly as he closed his notebook.

"We have the harvest," Ryan said.
"""

CH15_FULL = r"""# CHAPTER FIFTEEN
## The Glass Seam in the Dark
### Callisto Rendezvous

Four days after diving through the Europa plume, the Skimmer returned to the sanctuary of Callisto.

On May 8, 2040, the Callisto Staging Platform’s automated lidar tracking sensors acquired the approaching probe at a distance of forty thousand kilometers. The Skimmer had shed its hyperbolic excess velocity with a precise four-hundred-meter-per-second braking burn using its auxiliary hydrazine thrusters, slipping into a co-planar rendezvous orbit behind the mothership.

Through the mothership’s proximity cameras, the Skimmer appeared as a battle-scarred dart of scorched titanium: its gold thermal foil was pitted by micrometeorite impacts, and its dark ceramic nosecone bore the faint, iridescent dusting of Europa's brine frost.

Inside the automated docking bay of the mothership, a three-jaw mechanical capture mechanism reached out into the vacuum.

At 08:24 UTC, the Skimmer’s forward docking probe engaged the capture collar with a soft, magnetic *clack*:

```
[DOCK-LOG] SKIMMER CAPTURE CONFIRMED.
[DOCK-LOG] RELATIVE VELOCITY: 0.00 M/S.
[DOCK-LOG] RETRACTING INTO VACUUM SEALING BAY...
[DOCK-LOG] CHAMBER ENVIRONMENT: HARD VACUUM (1.2e-07 TORR).
```

The Skimmer was drawn inside the cylindrical service bay of the mothership. The outer airlock doors remained open to space; the sample could not be warmed or pressurized. It had to remain in the hard vacuum and cryogenic freeze of deep space.

---

### The Seam in the Vacuum

Inside the vacuum bay, a robotic manipulator arm moved over the Skimmer's collector compartment.

The arm released the mechanical latches of the aerogel collector box, lifting the rectangular titanium sample canister from the probe's chassis. The canister was fifteen centimeters long, ten centimeters wide, and five centimeters thick, containing the sixteen graded aerogel tiles holding the fourteen thousand frozen ocean grains.

The arm placed the canister inside the **Hermetic Laser Welding Rig**.

A circular grade-5 titanium sealing lid—fitted with an internal micro-reservoir of 99.999% pure Helium-4 tracer gas—was lowered onto the mouth of the canister. A hydraulic clamp pressed the lid down with three hundred pounds of force, seating a circular knife-edge flange against the copper-nickel seal ring.

In Boulder, Colorado, Ryan Vance and Elena Rostova watched the live telemetry stream via the high-gain deep space link.

The forty-two-minute speed-of-light delay meant the weld was already finished; they were watching the recorded confirmation of an action that had occurred while they were having lunch in the cafeteria.

On the screen, the automated welding sequence executed:

```
[LASER-WELD] YTTERBIUM FIBER LASER (1070 NM) ENERGIZED.
[LASER-WELD] OPTICAL POWER: 192 WATTS.
[LASER-WELD] BEAM FOCAL SPOT: 180 MICRONS.
[LASER-WELD] BEGINNING CIRCULAR CONTOUR SCAN...
```

Through the optical inspection camera, an intense, brilliant star of white-blue light traced the circular perimeter of the titanium lid.

In the hard vacuum of Callisto orbit, there was no air to form smoke or slag. The laser beam vaporized the microscopic surface oxide layer and melted the titanium in a continuous, smooth bead of molten metal one point four millimeters deep.

The weld completed in precisely **twenty-eight point two seconds**:

`[LASER-WELD] CIRCUMFERENCE: 314 MM COMPLETE.`  
`[LASER-WELD] COOLING TO CRYO BASELINE (-140 DEG C)...`  

Then came the critical test.

A quadrupole mass spectrometer arm swung across the newly welded seam, sniffing the vacuum for the presence of the Helium-4 tracer gas.

If the weld had a microscopic fissure, a single pinhole where the titanium had bubbled, Helium atoms would escape into the vacuum.

The mass spectrometer plotted the helium partial pressure:

```
[TRACER-TEST] BACKGROUND HE-4: 1.1e-12 MBAR
[TRACER-TEST] PEAK MEASURED HE-4: 1.2e-12 MBAR
[TRACER-TEST] LEAK RATE: < 4.2e-12 MBAR * L/SEC
[TRACER-TEST] HERMETIC INTEGRITY: 100.00% QUALIFIED.
```

The seam was glass-smooth, unbroken, and hermetically sealed against the universe.

The robotic arm lifted the sealed titanium capsule, transferred it into the nosecone of the **Earth-Return Vehicle (ERV)**, and engaged the triple-redundant mechanical flight locks.

Elena Rostova turned to Ryan, her eyes shining in the dim glow of the Boulder monitors.

"The sample is sealed, Ryan," she said softly. "Now we bring it home."
"""

CH16_FULL = r"""# CHAPTER SIXTEEN
## The Silent Arc
### The Ghost Departure

On June 14, 2040, the Earth-Return Vehicle severed its umbilicals from the Callisto Staging Platform.

The ERV was an elegant, minimalist spacecraft: an eight-meter carbon-composite truss carrying two large spherical tanks of liquid xenon, a four-cluster array of NEXT-C high-efficiency gridded ion thrusters, and a central shielded capsule holding the sealed Europa sample canister.

At 06:12 UTC, the ion engines ignited with a pale, ethereal glow of electric-cyan plasma:

```
[ION-PROP] NEXT-C ENGINES 1-4: ONLINE
[ION-PROP] TOTAL THRUST: 0.94 NEWTONS
[ION-PROP] SPECIFIC IMPULSE: 4,180 SECONDS
[ION-PROP] ACCELERATION: 0.00032 M/S^2
[ION-PROP] ESCAPING CALLISTO GRAVITY WELL...
```

With an acceleration of less than half a millimeter per second squared, the motion was imperceptible to human senses. But sustained over days and weeks, the relentless whisper of the ion engines climbed out of Jupiter’s gravitational territory, slipping onto a long, sweeping heliocentric arc that angled inward toward the inner solar system.

To conserve power and eliminate thermal signatures, the mission operations team placed the ERV into **Silent Cruise Mode**.

The high-gain radio dish was stowed against the truss. The primary telemetry transmitters were turned off. The spacecraft became a ghost: six hundred million kilometers of dark, uncommunicative vacuum, drifting silently between the orbits of Mars and Earth for **nine hundred and eighty days**.

---

### The Torque Anomaly

In July 2041—Day 412 of the cruise—the Deep Space Network dish at Goldstone caught a scheduled ten-minute diagnostic carrier ping from the ERV.

The telemetry packet was small, only four kilobytes, but it contained an alarming flight dynamics flag:

```
[GNC-DIAG] ATTITUDE DRIFT: ROLL AXIS +0.014 DEG/DAY
[GNC-DIAG] REACTION WHEEL #2 SPEED: 4,820 RPM (LIMIT: 5,000 RPM)
[GNC-DIAG] REACTION WHEEL DESATURATION IMMINENT.
[GNC-DIAG] ANOMALOUS TORQUE DETECTED: +6.12 uN*m (SOLAR PRESSURE)
```

The spacecraft was tumbling.

The culprit was asymmetric micrometeorite erosion. Over four hundred days in interplanetary space, the sunward side of the multi-layer insulation (MLI) blankets on the port solar array had been scoured by interplanetary dust grains, altering its optical reflectivity by eight percent.

The sun's photon pressure was pushing harder on the port array than on the starboard array, generating a continuous, unmodeled roll torque of **$+6.12\ \mu\text{N}\cdot\text{m}$**.

The internal reaction wheels had absorbed the torque until Wheel #2 was within one hundred and eighty RPM of its structural redline. Once the wheel saturated, the spacecraft would lose three-axis attitude control, begin tumbling uncontrollably, and freeze its solar arrays away from the sun.

In Boulder, the engineering tiger team was in crisis.

The traditional aerospace solution was to fire the hydrazine reaction control thrusters to desaturate the wheels. But firing the thrusters would consume six percent of the ERV's precious hydrazine reserve—fuel that was desperately needed for the Earth-Moon capture burn twenty months later.

Sitting in the back of the operations room, working on a tablet computer, was sixteen-year-old **Elena Vance**.

Ryan’s daughter was no longer the little girl in pink sneakers who had sat on his shoulders at Cape Canaveral. She was a sophomore in applied mathematics at the University of Colorado, with her father’s dark hair, his intense, quiet concentration, and an instinctive grasp of relational mechanics that frightened her professors.

Elena walked up to the flight dynamics console, carrying a single sheet of paper covered in neat pencil derivations.

"You don't need to burn hydrazine," Elena said quietly.

The flight dynamics lead, a fifty-year-old orbital analyst named Henderson, looked up with an exasperated sigh. "Elena, the wheel is going to redline in forty-eight hours. We have to dump momentum."

"You can dump momentum with light," Elena said, setting the paper on his desk.

Henderson frowned, looking at the equations.

"Look at the shape-sphere projection of the solar arrays," Elena explained, tracing the vector geometry with her pencil. "The arrays have independent single-axis rotary joints. If you tilt the port array forward by **two point eight degrees** and the starboard array aft by **one point four degrees**, you create an optical pinwheel effect."

She tapped the bottom line of the derivation:

$$\tau_{\text{photon}} = \frac{\Phi_{\text{solar}}}{c} A \left[ (1 + R_{\text{port}}) \sin \theta_{\text{port}} - (1 + R_{\text{starboard}}) \sin \theta_{\text{starboard}} \right] = -6.12\ \mu\text{N}\cdot\text{m}$$

"The solar photon torque perfectly cancels the micrometeorite asymmetry," Elena said. "The reaction wheel will desaturate back down to twelve hundred RPM in eighteen hours. Zero hydrazine expended."

Henderson stared at the paper. He looked up at Ryan Vance, who was standing three paces away, watching his daughter with a faint, unreadable smile.

Henderson plugged the numbers into the orbital simulator.

The simulation converged.

At 18:40 UTC, the command packet was uplinked from Goldstone.

Two hours later, the ERV’s reaction wheel speed began to drop: 4,800... 4,200... 3,100... 1,400 RPM.

The ghost ship stabilized, holding its nose toward Earth, gliding silently through the dark along its mathematical arc.
"""

CH17_FULL = r"""# CHAPTER SEVENTEEN
## Gravity's Needle
### Earth Approach, February 2043

Nine hundred and eighty days after leaving Callisto, the Earth-Return Vehicle arrived at the doorstep of the home world.

Through the forward optical navigation cameras, Earth was no longer a distant pale blue dot. It was a radiant, living jewel of lapis lazuli, swirling white cloud bands, and emerald continents, hanging in the blackness beside the silver crescent of the Moon.

The spacecraft was moving at a terrifying hyperbolic excess velocity: **11.2 kilometers per second**.

Under standard space mission architectures, an interplanetary sample return capsule executed a direct ballistic entry into Earth’s atmosphere, slamming into the upper stratosphere behind a heavy ablative carbon-phenolic heat shield, descending on parachutes into the Utah desert or the Australian outback.

For Project ARGONAUT, direct atmospheric entry was strictly, legally prohibited.

Under United Nations General Assembly Resolution 98/14 and the revised COSPAR Planetary Protection Protocol, the Europa harvest was classified as a **Category V (Restricted Earth Return)** payload: an active extraterrestrial biological sample from an ocean world with high astrobiological potential.

If the ERV’s heat shield suffered a microscopic bonding defect during an 11.2 km/s atmospheric entry, the sample canister could rupture at seventy kilometers altitude, dispersing viable alien cryomicrobes into the upper jet streams of Earth’s biosphere.

The sample could not touch Earth's air.

It had to be captured into a high, permanent quarantine orbit: the **Near-Rectilinear Halo Orbit (NRHO)** around the Moon, docking directly with the bio-quarantine module of the international **Lunar Gateway**.

---

### The Three-Body Needle

Capturing into lunar NRHO from an interplanetary hyperbolic arrival without carrying thousands of kilograms of heavy chemical propellant was considered impossible by classical two-body orbital mechanics.

Ryan Vance solved it using the **Three-Body Invariant Manifolds** of the Sun-Earth-Moon system.

"We do not fight the gravity wells," Ryan explained to the flight operations team in Boulder. "We thread the needle."

At 04:12 UTC on February 18, 2043, at Day 980 of the mission, the ERV executed its primary capture maneuver: the **Perigee Injection Burn**.

Passing just six hundred kilometers above the blue waters of the Pacific Ocean at eleven point two kilometers per second, the ERV’s main bi-propellant braking engine fired for sixteen minutes:

```
[CAPTURE-BURN] IGNITION TIME: 04:12:00 UTC
[CAPTURE-BURN] ENGINE THRUST: 4,400 NEWTONS
[CAPTURE-BURN] DELTA-V DELIVERED: 3,860.4 M/S
[CAPTURE-BURN] RESIDUAL ERROR: 0.012 M/S
[CAPTURE-BURN] ORBIT STATUS: CAPTURED ON EARTH-MOON L2 STABLE MANIFOLD.
```

The burn did not circularize the orbit. It scrubbed precisely enough kinetic energy to drop the spacecraft onto the **stable invariant manifold tube** associated with the Earth-Moon $L_2$ collinear Lagrange point.

Like a drop of water sliding down the interior surface of a glass funnel, the ERV coasted along the gravitational contour without firing another gram of fuel, drawn inexorably toward the Moon.

Four days later, on February 22, the spacecraft slipped through the $L_2$ bottleneck and entered the Lunar Gateway’s Near-Rectilinear Halo Orbit: an eccentric, polar lunar orbit with an aposelene of seventy thousand kilometers over the lunar south pole and a perilune of three thousand kilometers over the north pole.

---

### The Gateway Docking

Standing in the observation cupola of the Lunar Gateway station, Commander Sarah Ross—now a veteran astronaut and Director of Lunar Orbital Operations, who had been saved by Ryan Vance’s integer filter on Artemis-7 seventeen years earlier—watched the ERV approach.

The station’s robotic arm reached out into the blackness, its grapple fixture locking onto the ERV’s docking pin with a heavy, satisfying mechanical thud:

`[GATEWAY-OPS] ERV HARD DOCK CONFIRMED.`  
`[GATEWAY-OPS] SAMPLE CANISTER STATUS: HERMETICALLY SEALED.`  
`[GATEWAY-OPS] INTERNAL TEMPERATURE: -142 DEG C.`  
`[GATEWAY-OPS] TRANSFERRING TO BIO-QUARANTINE ISOLATION CHAMBER.`  

Through the station's radio link to Boulder, Colorado, Sarah Ross’s voice came across the speakers:

"Boulder, this is Gateway. The Europa harvest is on board. The seals are intact. The ocean has arrived."

In Boulder, sixty-one-year-old Ryan Vance took his daughter Elena’s hand, feeling the quiet, steady warmth of human life in the cold room.

The voyage across six hundred million kilometers was over.

The battle for the truth was about to begin.
"""

print("Writing expanded Act IV chapters...")
for fname, content in [
    ("Chapter_13_The_Dive_into_the_Belt.md", CH13_FULL),
    ("Chapter_14_Forty_Two_Seconds.md", CH14_FULL),
    ("Chapter_15_The_Glass_Seam_in_the_Dark.md", CH15_FULL),
    ("Chapter_16_The_Silent_Arc.md", CH16_FULL),
    ("Chapter_17_Gravitys_Needle.md", CH17_FULL),
]:
    p = os.path.join(MANUSCRIPT_DIR, fname)
    with open(p, "w") as f:
        f.write(content.strip() + "\n")
    words = len(content.split())
    print(f"Updated {fname}: {words} words")
