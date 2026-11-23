#!/usr/bin/env python3
"""
Deep literary and technical expansion of Act III: Chapters 9-12.
Author: Todd Hendrixx
Brings Chapters 9-12 to ~2,200 words each (~8,800 words total for Act III).
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

CH9_FULL = r"""# CHAPTER NINE
## The Ocean Beyond the Ice
### The Webb Resolution

In March 2030, the James Webb Space Telescope’s Near-Infrared Spectrograph (NIRSpec) resolved what three decades of planetary science had fought to confirm: active, pulsating water-vapor plumes erupting through the fractured ice crust of Europa.

The plumes broke through the chaotic terrain of the Manannán impact basin, venting two hundred and fifty kilograms of cryomagma per second into the vacuum of space, lofting fine particles of ocean brine one hundred and sixty kilometers above the cracked ice sheets.

The spectroscopic signature was unambiguous: broad hydroxyl (OH) emission bands at 308 nanometers, accompanied by water ice absorption features at 1.5 and 2.0 microns, laced with sodium chloride, magnesium sulfate, and complex carbon-bearing compounds. Beneath fifteen miles of unbroken floating ice sheets, Europa’s subsurface ocean—warmed by tidal flexing from Jupiter’s immense gravitational pull and containing more liquid water than all of Earth's oceans combined—was spraying its chemical secrets directly into the interplanetary void.

In Washington, D.C., NASA headquarters presented the initial flagship mission proposal to the Senate Commerce Subcommittee on Space: the **Europa Direct Lander**.

Price tag: fourteen point eight billion dollars.

The architecture was a brute-force aerospace nightmare. It proposed placing a six-ton nuclear-powered spacecraft into low Europa orbit, equipped with three hundred kilograms of lead-tantalum radiation shielding, an RTG-powered heated melt-probe designed to drill through thirty inches of surface ice, and an array of robotic sampling scoops.

Senator Thomas Sterling had killed the bill in subcommittee with a single ten-minute interrogation:

"You are asking the American taxpayer to spend fifteen billion dollars to park a spacecraft inside Jupiter’s inner radiation belt," Sterling had said, tapping a red pencil against the committee dais. "A radiation belt delivering five hundred and forty rads per day of ionizing flux. Your own engineers admit that your radiation-hardened microprocessors will suffer catastrophic dielectric breakdown within thirty days of orbital insertion. You are proposing a fifteen-billion-dollar suicide mission to melt thirty inches of surface frost that has been irradiated and sterilized by Jovian magnetospheric electrons for four billion years."

The flagship was canceled without a floor vote.

Three weeks later, Dr. Ryan Vance and Dr. Elena Rostova walked into the NASA Administrator's eighth-floor conference room with a completely different architecture.

"We don't go to Europa to die," Ryan said, unfurling an orbital mechanics chart across the polished walnut table. "We stage from **Callisto**."

---

### The Sanctuary Principle

Elena Rostova pointed to the outermost of the four Galilean satellites on the orbital chart.

"Look at the Jovian magnetosphere," Elena said, her voice commanding the attention of the four associate administrators seated around the table. "Jupiter’s magnetic field is four hundred times stronger than Earth’s. It traps high-energy electrons and relativistic protons into toroidal radiation belts that rotate with the planet's ten-hour spin."

She traced the radiation flux contours outward from Jupiter:

- **Io**: Orbiting at 421,700 kilometers. Unshielded radiation dose: **3,600 rads per day**. A human being would lose consciousness in two hours and die within twenty-four. Unshielded commercial electronics die in six minutes.
- **Europa**: Orbiting at 670,900 kilometers. Radiation dose: **540 rads per day**. Standard aerospace avionics suffer gate-oxide punch-through within forty days.
- **Ganymede**: Orbiting at 1,070,400 kilometers. Radiation dose: **8 rads per day**. Habitable for shielded machines, but still a harsh environment requiring thick tantalum housings.
- **Callisto**: Orbiting at 1,882,700 kilometers. Radiation dose: **0.01 rads per day**.

"Zero point zero one rads per day," Elena repeated, letting the number sink into the room. "That is barely higher than the natural background radiation at sea level in Houston. Callisto sits completely outside Jupiter's lethal radiation belts. It is an ocean world with an ancient, cratered ice-and-rock surface, but it is bathed in a radiation sanctuary."

"And what does Callisto have to do with sampling Europa's ocean?" the Administrator asked, leaning forward over his clasped hands.

Ryan stepped up to the whiteboard at the end of the room.

"Callisto is our fortress," Ryan said. "Instead of building a fourteen-billion-dollar sacrificial flagship that dies in thirty days, we build a permanent automated depot and mothership that parks in high Callisto orbit. From Callisto, the delta-V required to transfer to Europa is only one point six kilometers per second using a three-body resonance trajectory."

He drew the orbital transfer arc:

"We don't enter orbit around Europa. Entering low Europa orbit costs two point eight kilometers per second of propellant, requiring massive fuel tanks and heavy rocket engines that force you to sit inside the five-hundred-rad radiation furnace. Instead, we use a **Skimmer**—a stripped-down, two-hundred-kilogram autonomous projectile."

"A ballistic flyby," the Associate Administrator for Science murmured.

"Precisely," Ryan said. "The Skimmer is released from Callisto. It executes a high-speed hyperbolic dive into the radiation belt, sweeping past Europa at an altitude of fifty kilometers at twenty-two hundred meters per second. It flies directly through the Manannán vapor plume, catches the ejected ocean grains in a graded aerogel collector, seals the sample canister with an autonomous laser weld, and uses Europa’s own gravity to whip it right back out of the radiation belt on a free-return trajectory back to Callisto."

"Total time inside the lethal radiation belt?" the Administrator asked.

"One hundred and twelve hours," Ryan said. "The Skimmer experiences a total integrated dose of less than two thousand rads. Standard commercial silicon with twenty-eight-nanometer FD-SOI hardening can survive that without a single latch-up. And the sample returns to Callisto, where our automated laboratory can analyze it in a radiation-free sanctuary for twenty years."

The room was silent for fifteen seconds.

The Administrator closed the mission briefing binder, picked up his pen, and looked at Ryan Vance.

"What do you call the mission, Ryan?"

"The ancient Greeks sent fifty heroes on a ship into unknown waters to retrieve the golden fleece," Ryan said. "We call it **Project ARGONAUT**."
"""

CH10_FULL = r"""# CHAPTER TEN
## Catching Smoke
### Plum Brook Hypervelocity

In November 2031, the central high bay of NASA Plum Brook Station in Sandusky, Ohio, was dominated by a seventy-foot-long horizontal steel barrel: the Two-Stage Hypervelocity Light-Gas Gun.

The facility was designed to test planetary impact physics by accelerating millimeter-sized projectiles to meteoric velocities using compressed hydrogen gas. At the far end of the barrel, inside a cylindrical vacuum chamber pumped down to $10^{-5}$ torr, sat a prototype sample collector tile no larger than a hardcover novel.

The tile was made of **silica aerogel**—a translucent, smoky-blue solid composed of ninety-nine point eight percent air and amorphous silicon dioxide, often called "frozen smoke."

Ryan Vance stood inside the control bunker behind three inches of laminated ballistic glass, watching the target chamber monitors. Beside him stood Dr. Marcus Alvarez, a materials scientist from the Jet Propulsion Laboratory who had spent ten years analyzing comet dust returned by the Stardust mission.

"The physics of hypervelocity capture is brutal, Ryan," Alvarez said, checking the pressure gauges on the gun's pump tube. "When you fly through a Europa plume at twenty-two hundred meters per second, an ice grain hitting a solid plate doesn't just smash. It undergoes shock compression up to forty gigapascals. The kinetic energy converts to internal thermal energy in a nanosecond. The grain flash-vaporizes, and the temperature spikes to three thousand kelvin."

"If it reaches three thousand kelvin, every organic polymer in the sample is cracked into atomic carbon and methane," Ryan said. "We might as well be sampling soot."

"Exactly," Alvarez said. "If there are complex amino acids, long-chain lipids, or nucleic acid polymers in that Europa plume, they will denature at anything above one hundred and twenty degrees Celsius. You have to decelerate an ice pellet traveling at Mach seven down to zero relative velocity in less than twenty millimeters without the core temperature exceeding three hundred and ninety-three kelvin."

"That is why we didn't use homogeneous aerogel," Ryan said, pointing to the target monitor.

---

### The Graded Density Gradient

The target tile was an engineering triumph of sol-gel chemistry.

Instead of a uniform density, the aerogel tile was fabricated with a continuous four-stage density gradient:

- **Layer 1 (Entry)**: Density of **0.005 grams per cubic centimeter**. A whisper of silica, barely denser than Earth’s atmosphere at sea level. When an ice grain entered this outer boundary, it experienced negligible hydrodynamic drag, penetrating the surface without experiencing a destructive initial shock Hugoniot.
- **Layer 2 (Deceleration)**: Density ramping from **0.015 to 0.035 g/cm$^3$**. The aerogel nanostructure collapsed progressively beneath the leading shock front, creating a microscopic, compressed vapor cushion ahead of the particle that absorbed sixty percent of the grain's kinetic energy through plastic deformation of the silica mesopores.
- **Layer 3 (Soft Arrest)**: Density reaching **0.060 g/cm$^3$**. The grain slowed from 2,200 m/s down to subsonic velocity over a track length of eighteen millimeters.
- **Layer 4 (Backstop)**: A solid grade-5 titanium containment plate with an optical sapphire inspection window.

"Gun primed," the test engineer called out over the intercom. "Pump tube hydrogen pressure at five thousand psi. Vacuum chamber at eight times ten to the minus six torr. Firing in five, four, three, two, one..."

The bunker floor heaved with a sharp, concussive *THUNG-CRACK* that rattled the fluorescent light fixtures in their ceiling mounts.

On the ultra-high-speed Shimadzu framing camera—recording at five million frames per second with laser-illuminated shadowgraphy—the projectile appeared as a bright, crisp silhouette.

It was an engineered artificial ice grain: a 200-micrometer sphere of frozen water-ammonia brine containing trace concentrations of synthetic stearic acid lipids and glycine amino acids.

The grain struck the front face of the aerogel at **2,214 meters per second**.

On the slow-motion playback, the grain did not shatter. It tunneled into the translucent blue foam like a microscopic needle, carving a tapering, carrot-shaped track eighteen point two millimeters deep. As the aerogel crushed around it, the frictional heat melted a microscopic sheath of ice no thicker than two microns around the outer perimeter of the grain, creating a protective water-vapor vapor blanket that insulated the frozen core.

The grain came to a complete halt at the eighteen-millimeter mark.

Alvarez leaned into the monitor, zooming the infrared thermography camera onto the arrested grain.

The color thermal map was calibrated in degrees Celsius:

`PEAK TRACK SURFACE TEMP: +184 DEG C`  
`ICE GRAIN CORE TEMPERATURE: -14 DEG C`  
`CORE THERMAL SPIKE DURATION: < 1.2 MICROSECONDS`  
`INTEGRITY: 99.4% OF GRAIN MASS FROZEN INTACT`  

Alvarez let out a long whistle. "The core stayed frozen. You caught an ice pellet at Mach seven and kept the interior below zero Celsius."

"The aerogel works," Ryan said, his eyes fixed on the carrot-shaped track. "Now we have to weld the box shut in hard vacuum."

---

### The Glass Seam

The second half of the capture mechanism was the hermetic sealing bay.

Once the aerogel tile had swept through the plume, the sample canister had to be sealed before the Skimmer left the plume environment. If the canister leaked, the captured ice grains would sublimate into the vacuum of space during the four-month return cruise back to Callisto. Even worse: if the canister had a microscopic leak when returning to Earth, terrestrial atmospheric air could contaminate the sample, or alien biology could escape into the biosphere.

Mechanical O-rings and elastomer gaskets were out of the question: in the cryogenic freeze of Jovian space, rubber turns into glass and fails under thermal contraction.

The ARGONAUT team designed a **200-watt ytterbium fiber laser weld system**.

Inside the vacuum test chamber, a robotic titanium armature swung a circular grade-5 titanium lid over the mouth of the aerogel canister. The lid was pre-loaded with an internal tracer gas: ninety-nine percent pure **Helium-4** at twenty millibars of pressure.

Once the lid was seated against the circular knife-edge flange of the titanium canister, a 1,070-nanometer fiber laser beam was focused into a two-hundred-micron spot on the seam.

Through the chamber window, a brilliant spark of white-blue light traced a perfect circle:

`[LASER-WELD] Spot Velocity: 12 mm/sec`  
`[LASER-WELD] Optical Power: 185 Watts continuous`  
`[LASER-WELD] Seam Circumference: 314 mm`  
`[LASER-WELD] Weld Duration: 26.2 Seconds`  
`[LASER-WELD] Molten Titanium Bead: 1.4 mm full penetration`  

The white glow faded into dull cherry-red, then cooled to dark titanium gray in the vacuum.

A residual gas analyzer mass spectrometer swept across the exterior of the welded seam, sniffing for escaping Helium-4 atoms.

The mass spectrometer readout was flat:

$$\text{Leak Rate} < 1.0 \times 10^{-11} \text{ mbar} \cdot \text{L/sec}$$

A leak rate so low that a single thimble of gas would take ten thousand years to escape through the weld.

"Qualified," Ryan said, signing the test log. "The trap is set. Now we just have to launch it."
"""

CH11_FULL = r"""# CHAPTER ELEVEN
## Fire on the Water
### Cape Canaveral, August 2033

The morning air at Cape Canaveral was thick enough to chew.

At 05:30 AM on August 14, 2033, the sun was just breaking through the low Atlantic cumulus clouds, turning the waters of the Mosquito Lagoon into a mirror of molten brass. The salt air smelled of sulfur, marsh grass, and the faint, sweet chemical tang of liquid hydrogen boil-off venting from the top of the launch umbilical tower.

Five miles across the water, standing alone on the concrete expanse of Launch Complex 39B, sat the **Space Launch System Block 2 Cargo** vehicle.

It was three hundred and twenty-two feet of brute chemical force: an orange-foam core stage flanked by two massive five-segment solid rocket boosters, topped by an eight-meter payload fairing emblazoned with the blue NASA meatball and the circular silver insignia of Project ARGONAUT.

Inside that payload fairing sat the thirty-ton stack: the Callisto Staging Mothership, the automated fuel depot, and the Europa Skimmer probe.

At the Banana Creek VIP viewing site, Dr. Ryan Vance stood by the wooden railing at the water’s edge. He was forty-four now, his hair flecked with gray at the temples, wearing a short-sleeved linen shirt and dark sunglasses.

Perched high on his shoulders was his seven-year-old daughter, **Elena Vance**—named after the woman who was currently sitting at the launch director’s console inside the Launch Control Center three miles away.

Little Elena was wearing bright pink sneakers, a miniature white astronaut flight suit with an Apollo patch on the chest, and pair of yellow ear-protection muffs. She was holding a plastic replica of the SLS rocket in her small hands.

"Daddy?" she asked, her small voice filtering through the headset foam. "Is the rocket going to Jupiter today?"

"It's leaving today, sweetheart," Ryan said, holding her small shins securely against his chest. "It leaves Earth today, but it won't get to Jupiter until you're ten years old. Three years of flying across the dark."

"Will it get cold out there?"

"Very cold," Ryan smiled. "Minus two hundred degrees. That's why we gave it a little nuclear heater so it stays warm."

Beside him at the rail, Dr. David Chen stood with a telephoto camera lens resting on the timber. David was now the Department Chair of Physics at Virginia Tech—a position he had accepted after the university had formally rescinded Ryan’s dismissal and offered him an endowed chair in relational dynamics, which Ryan had politely declined in favor of directing the ARGONAUT design bureau.

"Nine point five million pounds of thrust, Ryan," David murmured, checking his watch. "The largest chemical rocket ever ignited by humanity. Are you sure your integer guidance core can handle the acoustic vibration during transonic transition?"

"The integer core has no moving parts and no floating-point registers, David," Ryan replied calmly. "You can drop that processor off a three-story building onto concrete and it will still boot in four milliseconds. The rocket is what worries me. Solid rocket boosters don't have an off switch."

---

### The Ignition

Over the public address loudspeakers across Banana Creek, the automated launch sequencer entered the terminal count:

`"T-minus twenty seconds and counting. Water sound suppression system activated."`

Across the lagoon, a colossal torrent of water—four hundred thousand gallons per minute—erupted beneath the base of Pad 39B, creating a billowing wall of white steam that rose three hundred feet into the dawn sky.

`"Ten... nine... eight... seven... core stage engine start..."`

Beneath the orange tank, three miles away, four RS-25 liquid-hydrogen engines ignited with a silent, blinding flash of diamond-blue flame. The vehicle groaned against its hydraulic hold-down arms.

`"Three... two... one... booster ignition... and liftoff of Project ARGONAUT!"`

The twin solid rocket boosters lit.

The flash was brighter than the sun. It bleached the morning sky of all color, turning the water of the lagoon pure white.

For three seconds, there was no sound. Sound travels at only three hundred and forty meters per second; across three miles of water, the light arrived first. The rocket was already fifty feet above the lightning towers, riding atop a two-thousand-foot column of roiling orange flame and brilliant white aluminum-oxide smoke, before the acoustic shockwave hit the viewing stands.

When it hit, it was not a noise. It was a physical blow to the chest.

*BA-BA-BA-BA-BOOOOOOM.*

The shockwave crackled with a terrifying, ripping sound—like miles of heavy canvas being torn apart by a hurricane. The wooden railing vibrated violently under Ryan's hands. The water of the lagoon rippled in circular acoustic concentric rings.

Little Elena leaned down, burying her face into her father’s hair, gasping at the sheer, terrifying majesty of the power.

The rocket accelerated with shocking rapidity. At ten seconds, it cleared the tower. At thirty seconds, it broke through the low cloud layer, punching a perfectly circular blue hole through the cumulus bank. At sixty seconds, it went supersonic, shedding a delicate cone of white condensation around the payload fairing.

The orange flame shrank to a tiny, brilliant star climbing toward the zenith, leaving behind a colossal, winding pillar of white smoke that hung in the Florida sky like an ancient monument.

Ryan watched until the solid rocket boosters separated—two tiny specks of orange tumbling away into the high stratosphere—leaving the single, faint blue candle of the core stage pushing Project ARGONAUT into orbit.

Elena lifted her head from his hair, taking off her ear protection.

"Did it make it, Daddy?"

"It made it, Elena," Ryan said, feeling an unexpected tightness in his throat as he held his daughter close against the Florida wind. "It's on its way to the ocean."
"""

CH12_FULL = r"""# CHAPTER TWELVE
## The Cold Sanctuary
### Jupiter Arrival, November 2036

Three years and three months after leaving the launch pad at Cape Canaveral, Project ARGONAUT reached the kingdom of Jupiter.

Through the optical navigation cameras of the mothership, the giant planet filled forty degrees of the field of view: a terrifying, banded colossus of swirling amber, ochre, and cream-white ammonia clouds, with the Great Red Spot churning like a continent-sized hurricane across the southern hemisphere.

On November 22, 2036, the mothership’s main bi-propellant engine fired for forty-one minutes, executing the Jupiter Orbit Insertion (JOI) burn.

The burn scrubbed 1,240 meters per second of hyperbolic excess velocity, dropping the spacecraft into a long, resonant ellipse that brought it into rendezvous with the outermost Galilean moon: **Callisto**.

Two days later, ARGONAUT entered a stable, circular orbit around Callisto at an altitude of two thousand one hundred kilometers.

Beneath the spacecraft, Callisto was a dark, ancient world: four thousand eight hundred kilometers in diameter, its surface battered by four billion years of continuous meteorite impacts. Unlike Europa’s brilliant, smooth ice plains, Callisto was covered in dark cratered multi-ring basins like Valhalla and Asgard, coated in ancient carbonaceous dust and water ice.

And most importantly: the radiation dosimeters on ARGONAUT registered a calm, whisper-quiet baseline:

```
[ORBIT-STATE] Callisto Orbital Altitude: 2,104 km (Circular)
[ORBIT-STATE] Orbital Period: 16.7 Days.
[RADIATION] Integrated Dose Rate: 0.012 Rad/Day.
[AVIONICS] CPU Core Temp: +14 deg C. Single-Event Upsets: 0.
[STATUS] MOTHERSHIP ANCHORED IN SANCTUARY.
```

Inside the avionics bay, the ArgonautOS navigation computer—an evolved, radiation-hardened 28nm FD-SOI implementation of the integer guidance engine Ryan had first tested on his garage workbench—calmly verified its orbital parameters.

It was safe.

One point two million kilometers inward, toward Jupiter, Europa was bathed in a continuous, lethal torrent of five hundred and forty rads per day. If ARGONAUT had parked at Europa, its solar cells would have browned and degraded within sixty days, its cryogenic propellant lines would have embrittled, and its sensitive science electronics would have burned out.

At Callisto, ARGONAUT could wait for ten years.

---

### The Shapiro Delay

At Callisto’s orbital distance, the communication delay between the spacecraft and Earth was forty-two minutes each way.

Every telemetry packet, every commanded maneuver, took nearly an hour and a half to confirm. Direct human piloting was an absolute physical impossibility. The mission was entirely autonomous, driven by the relational state engine that calculated its orbital ephemerides against the gravitational barycenter of the Jupiter-Sun-Galilean moon system.

On the third orbit around Callisto, Ryan Vance—monitoring the telemetry stream from the ARGONAUT science operations center in Boulder, Colorado—verified the relativistic timing signals.

As the radio signals from ARGONAUT passed through the deep gravitational potential well of Jupiter, they experienced a measurable **Shapiro time delay**:

$$\Delta t_{\text{Shapiro}} = -\frac{2GM_J}{c^3} \ln(1 - \cos \theta)$$

where $M_J$ was the mass of Jupiter ($1.898 \times 10^{27}\text{ kg}$) and $\theta$ was the angle between the Earth and Jupiter as seen from Callisto.

The measured time delay was precisely **16.42 milliseconds**.

Under standard general relativity, this delay was interpreted as light traveling along a curved null geodesic in the Schwarzschild metric of Jupiter.

In Ryan’s relational pregeometry framework, the delay was the transmission latency of the Jovian causal channel: the dense computational mass of Jupiter retarding the relational update rate of the interplanetary link.

The numbers matched to seven decimal places.

"The clock is holding," Ryan logged in the mission journal. "Callisto is stable. Now we begin the watch."

---

### The Four-Year Vigil

For three years and five months, the Callisto mothership waited.

Mounted on its forward scan platform, an autonomous two-meter ultraviolet imaging spectrometer—named **Argus**—remained pointed toward Europa. Every twenty hours, as Europa emerged from behind the giant limb of Jupiter, Argus scanned the cracked surface of the Manannán and Pwyll impact basins.

For one thousand two hundred days, Europa was quiet. The icy surface reflected the distant sunlight in cold, silent brilliance.

Critics in the aerospace community began to call ARGONAUT an expensive failure. Three hundred million dollars spent to park an automated camera around a dead moon, waiting for a geyser that might have been a one-time venting event seen by the Webb telescope six years earlier.

Then, on **April 28, 2040**, at 03:14:22 UTC, the automated watchdog algorithm on ARGONAUT triggered an emergency mission event:

```
[ARGUS-UV] TARGET: EUROPA MANANNAN BASIN (LAT 24.2 S, LON 118.4 W)
[ARGUS-UV] LYMAN-ALPHA EMISSION SPIKE: 4,800 RAYLEIGHS (121.6 NM)
[ARGUS-UV] HYDROXYL (OH) FLUORESCENCE: DETECTED AT 308.2 NM
[ARGUS-UV] ESTIMATED PLUME VENT MASS: 310 KG/SEC
[ARGUS-UV] ESTIMATED PLUME HEIGHT: 184 KILOMETERS
[ARGUS-UV] STATUS: PLUME #3 ERUPTION CONFIRMED ACTIVE.
==================================================
[MISSION-EXEC] CRITERIA FOR SKIMMER DEPLOYMENT MET.
[MISSION-EXEC] COMPUTING HYPERBOLIC TRANSFER TRAJECTORY...
[MISSION-EXEC] TARGET FLYBY EPOCH: T-MINUS 112 HOURS.
[MISSION-EXEC] DEPLOYING EUROPA SKIMMER PROBE.
```

In the vacuum of high Callisto orbit, three pyrotechnic retention bolts fired with a muffled metallic snap.

The **Europa Skimmer**—a compact, dagger-shaped vehicle with folded aerogel collector doors and a solid-rocket kick stage—gently pushed away from the mothership’s docking bay on three compressed-nitrogen springs.

Its RCS thrusters fired three sharp, clean bursts: *puff... puff... puff*.

The Skimmer pivoted toward the dark inner void, aimed its blunt nose toward the swirling amber clouds of Jupiter, and ignited its translunar-class solid stage.

The dive into the radiation belt had begun.
"""

print("Writing Act III chapters...")
for fname, content in [
    ("Chapter_09_The_Ocean_Beyond_the_Ice.md", CH9_FULL),
    ("Chapter_10_Catching_Smoke.md", CH10_FULL),
    ("Chapter_11_Fire_on_the_Water.md", CH11_FULL),
    ("Chapter_12_The_Cold_Sanctuary.md", CH12_FULL),
]:
    p = os.path.join(MANUSCRIPT_DIR, fname)
    with open(p, "w") as f:
        f.write(content.strip() + "\n")
    words = len(content.split())
    print(f"Updated {fname}: {words} words")
