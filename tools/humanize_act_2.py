import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

ch5 = r"""# CHAPTER FIVE
## The Artemis Blackout
### The Translunar Corridor

The Castor 30XL solid motor burned out with a sudden, clean decay of thrust that let Ryan Vance’s chest expand against his harness straps.

Nine seconds later, the separation ordnance fired with a sharp metallic snap. The spent motor casing drifted away into the blackness, tumbling end-over-end as it fell into a heliocentric disposal arc. 

On the central avionics display, the twin 15-kilowatt Hall-effect thrusters came online. Outside the forward vision block, two pale, violet-blue plumes of ionized xenon plasma glowed silently in the vacuum. High-purity xenon gas was stripped of its electrons inside the magnetic acceleration channels, accelerating heavy ions to thirty-two kilometers per second. The gentle, unyielding push of zero point two gravities settled through the cabin, pressing Ryan and Marcus Thorne into their cushions.

"Translunar injection burn complete," Marcus said, his gloved fingers moving across the auxiliary propulsion panel. "We're on the transfer ellipse. Time to perilune: sixty-two hours."

Through the vision block, the Earth was already a curved sapphire marble wrapped in swirling white cloud patterns, receding at eleven kilometers per second. Four hundred thousand kilometers ahead, the Moon was a razor-sharp crescent against the black starfield.

And between them, the solar wind was churning.

"Look at the S-band noise floor on channel four," Marcus said, pointing a calloused finger at the spectrum analyzer. "That wasn't an ordinary coronal ejection. It was an X8.4 solar radio burst. A mega-flare centered right on the solar meridian."

Ryan leaned over the console. "Broadband thermal solar noise is flooding the lower gigahertz bands. It's pouring into the antenna sidelobes of the 70-meter Deep Space Network dishes in Canberra and Madrid."

"The DSN is blinded," Marcus said. "Canberra lost carrier lock on *Prometheus* forty minutes ago. Space Command has been pinging our transponder on the military UHF guard channel every sixty seconds, trying to verify our flight clearance. But they can't establish a coherent two-way link through the flare plasma."

"Cut the transponder," Ryan said quietly. "We don't need their ground stations. We are off the grid."

### The X-Ray Fix

Marcus reached up and toggled the transponder breaker to `STANDBY`. "Nobody navigates the cislunar corridor without ground tracking, Ryan. If our state vector drifts by fifty meters per second, we'll miss the Moon's capture corridor and swing into an unrecoverable heliocentric orbit."

"We're not using ground tracking," Ryan said, typing into the CislunarOS command shell. "Unstow the X-ray pulsar array."

On the dorsal hull of *Argonaut*, four silicon-drift X-ray detectors unlatched from their launch locks and oriented toward deep space.

Unlike radio waves, which are scattered and delayed by solar flare plasma and interplanetary electrons, high-energy X-ray photons emitted by millisecond pulsars cut through solar storms without attenuation. Each pulsar was a cosmic atomic clock with a rotational period known to fifteen decimal places: **PSR J0437-4715**, **PSR B1821-24**, **PSR B1937+21**, and **PSR J0030+0451**.

Within ninety seconds, the photon arrival times were streaming into the Kintex FPGA core.

"Four channels locked," Ryan reported, watching the phase residuals settle on the screen. "The square-root information filter is folding the arrival times against the onboard rubidium clock. Position fix: three hundred and twelve thousand kilometers from Earth, eighty-four thousand kilometers from the Moon. Velocity uncertainty: less than two millimeters per second."

Marcus watched the numbers settle into a flat, steady green line.

"A celestial navigation fix that doesn't depend on a single antenna on Earth," Marcus muttered, shaking his head. "It's clean."

"It's relational," Ryan said. "We aren't measuring our position against a hypothetical Cartesian origin in Colorado. We are measuring the differential arrival of light across the galaxy."

### The Strobing Star

Ryan switched the forward optical telescope to high-gain tracking, scanning the predicted trajectory corridor sixty thousand kilometers ahead.

A tiny point of light appeared on the monitor, glowing faintly against the black background of deep space.

"I have *Prometheus* on optical," Ryan said, adjusting the focal zoom. "Visual acquisition confirmed."

Marcus leaned forward, squinting at the screen.

The light from the distant spacecraft was not a steady point of reflected sunlight. It was pulsing—brightening, dimming, and flashing in a rhythmic, disorienting cycle every three point two seconds.

"That's not attitude hold," Marcus said, his voice dropping into a tense whisper. "She's in a flat spin."

Ryan brought up the Doppler Fourier analysis of the reflected solar spectrum.

"Their reaction control thrusters fired asymmetrically," Ryan said. "When the GEONS filter tripped `PROTECTIVE_SCREENED_COAST`, the attitude control module attempted to hold inertial reference with corrupted sensor inputs. They're tumbling along their minor axis at eighteen revolutions per minute."

Marcus gripped the edge of the instrument panel, his knuckles whitening through his flight gloves.

"Aris is on that ship, Ryan," Marcus said softly. "My daughter is strapped into that tumbling tin can, falling toward the lunar farside at two thousand meters per second."

Ryan looked at the trajectory display. "We have fifty-eight hours before their perilune pass. We have the delta-v. We are going to match their spin and bring them home."
"""

ch6 = r"""# CHAPTER SIX
## Covariance Starvation
### The Impact

The collision made no sound.

In the vacuum of deep space, kinetic energy transfers directly through structural lattices without acoustic waves. What Ryan felt was a sudden, violent jolt that slammed through the carbon-composite frame of the command module, accompanied by a sharp, high-frequency shudder that rang through the pressure hull like a strike on an anvil.

On the master caution panel, two amber warning lights flashed simultaneously:

`WARN: AUX_LINE_PRESSURE_DROP [SECTOR_3_FORWARD]`  
`NITROGEN_RESERVE: 68% (DECREASING @ 1.2 PSI/SEC)`  
`YAW_RATE_DRIFT: +2.8 DEG/SEC`  

"Micrometeoroid," Marcus said calmly, his hands instantly moving to the rotational hand controller. "Taurid debris stream. An iron-silicate particle, sub-millimeter, traveling at thirty-five kilometers per second."

"Pressure hull is intact," Ryan said, scanning the cabin cabin pressure transducers. "The Whipple shield absorbed the primary core. But the secondary fragment punched through the forward equipment fairing."

"It clipped the auxiliary cold-gas nitrogen line on the forward sensor boom," Marcus said, reading the telemetry. "The line is venting into vacuum at four hundred psi. It's acting like an uncommanded thruster on a six-foot moment arm. We're beginning to roll."

Outside the forward viewport, the stars began a slow, continuous rotation. The crescent Moon swept across the vision block once every twelve seconds, followed by the blinding glare of the Sun and the blue disk of the Earth.

"I can't fight it with the hydrazine RCS," Marcus said, checking the fuel totals. "If I fire the reaction control thrusters against an open nitrogen vent, we'll burn through forty kilograms of propellant in ten minutes. We won't have enough margin left for the perilune intercept."

### The Truss Inspection

Marcus unbuckled his shoulder harness, pushing himself smoothly out of the command couch in the microgravity air. He opened the survival locker behind the bulkhead and pulled out an extravehicular mobility suit.

"I'm going out on the truss to isolate the line," Marcus said, pulling on the thermal-micrometeoroid overgarment. "The manual shutoff valve is seated right behind the star-tracker baffle on the forward boom. If I can close the valve with an adjustable spanner, we stop the leak."

"Marcus, the spacecraft is rotating at nearly three degrees per second," Ryan cautioned. "Centrifugal acceleration on the boom will be noticeable. If you lose your grip, you'll drift off the hull."

"I have two braided Kevlar tethers and twenty years of spacewalk experience, Ryan," Marcus said, pulling his fiberglass helmet over his head. "Help me check the neck ring."

Ryan inspected the brass locking dogs on the collar, aligning the indexing pins until the ring clicked shut with a solid mechanical detent. He verified the suit pressure at 4.3 psi on pure oxygen, then stepped back into the cabin while Marcus cycled into the small auxiliary transfer airlock.

The airlock blowdown valve hissed softly as the atmosphere vented into space. The outer hatch swung open into the silent, star-filled void.

Marcus clipped his primary safety tether to the titanium guide rail running along the dorsal spine of *Argonaut*.

Outside, the universe was a rotating panorama of black sky, blazing sunlight, and planetary arcs. Marcus moved hand-over-hand along the carbon-fiber truss, his pressurized gloves gripping the cold rungs. The venting nitrogen was escaping from a hairline fracture in the stainless-steel tubing, forming a faint, crystalline cloud of white ice flakes that sublimated instantly in the hard vacuum.

"I have visual on the valve," Marcus reported over the suit intercom, his breathing steady and measured. "The braided line is crimped. The shutoff cock is stiff from the cold."

"Take your time," Ryan said from the cockpit, monitoring the hull camera. "We still have thirty-five percent nitrogen in the tank."

Marcus extracted an eight-inch aluminum-bronze spanner from his thigh pouch. He fitted the jaws over the square valve stem, bracing his boots against the truss frame.

"Engaging valve," Marcus grunted. "Quarter turn... half turn... closed. Nitrogen vent has stopped."

On the cockpit console, the pressure drop halted immediately:

`WARN_RESOLVED: LINE_ISOLATED`  
`REMAINING_NITROGEN: 32.4%`  
`PRESSURE_STABILIZED: NOMINAL`  

"Leak is sealed, Marcus," Ryan called out. "Good work. Head back to the airlock."

"Copy that," Marcus replied, stowing the spanner. "Returning along the guide rail."

### Gravitational Damping

Ten minutes later, the airlock repressurized with a soft roar of air. Marcus climbed back into the cabin, pulled off his helmet, and wiped the sweat from his forehead with a towel.

"Leak is stopped," Marcus said, strapping back into the left couch. "But we're still rotating at two point eight degrees per second. How do we damp the spin without wasting hydrazine?"

Ryan pulled up the CislunarOS guidance terminal.

"We use the Moon's gravity gradient," Ryan said.

"From eighty thousand kilometers out?" Marcus asked, raising an eyebrow.

"The Moon's update-latency well creates an infinitesimal tidal tensor across *Argonaut*’s six-meter airframe," Ryan explained, displaying the **Receding-Horizon Quadratic Programming (QP)** controller. "The forward boom is fifty nanoseconds closer to the lunar update cluster than the engine bell. That differential latency creates a measurable restoring torque:

$$\boldsymbol{\tau}_{\text{tidal}} = \frac{3GM_{\text{Moon}}}{r^3} \hat{\mathbf{r}} \times (\mathbf{I} \cdot \hat{\mathbf{r}})$$

"By modulating our internal magnetic torquer coils against the weak interplanetary magnetic field, CislunarOS can use that tidal torque as a brake. It will take forty-five minutes, but it costs zero kilograms of propellant."

Marcus leaned back in his couch, watching the yaw rate indicator begin its slow, steady decline: 2.8... 2.4... 1.9...

"You're using the universe's network latency as an anchor," Marcus said with a faint smile.

"Distance is impedance, Marcus," Ryan said. "When you stop fighting the network, the physics works for you."
"""

ch7 = r"""# CHAPTER SEVEN
## The Coast-Lock Bug
### The Freezing Cabin

Inside the command module of *Artemis-7*, the cabin temperature had dropped to three degrees Celsius.

Moisture from human breath had condensed onto the exposed aluminum ribbing of the pressure hull, freezing into a thin, crystalline glaze of frost. The only illumination came from the dull amber emergency status panels and the low-power green backlight of Dr. Elena Rostova's diagnostic laptop.

Elena pulled her woolen watch cap down over her ears, her fingers stiff inside thin polypropylene glove liners. Beside her in the center couch, lunar geologist Aris Thorne was wrapped in two silver thermal survival blankets, sipping lukewarm water from a plastic pouch. In the right couch, systems specialist Chen Wei was entering numbers into a handheld mechanical calculator, double-checking their consumable margins.

"Oxygen partial pressure is down to sixteen kilopascals," Chen said, his voice quiet in the cold air. "At our current metabolic rate, the lithium hydroxide canisters will saturate in roughly eleven hours. After that, we start breathing our own carbon dioxide."

"What about Houston?" Aris asked, her teeth clicking faintly. "Any carrier lock from Canberra?"

Elena glanced at the primary communications terminal. The signal-to-noise ratio meter was flatlined at minus forty-two decibels:

`DSN_DOWNLINK: LOST [SOLAR_RF_INTERFERENCE]`  
`CARRIER_LOCK: UNACQUIRED`  
`UPLINK_QUEUE: EMPTY`  

"Canberra is blind," Elena said. "The solar flare is pumping gigawatts of noise directly into the southern hemisphere dishes. Houston can't hear us, and we can't hear them."

She looked up at the central flight avionics panel. The caution banner that had sealed their fate six hours earlier was still burning in steady amber:

`CRITICAL_FAULT: GNC_COVARIANCE_COLLAPSE`  
`KALMAN_FILTER_STATUS: NIS_EXCEEDED (17.42 > 16.80)`  
`FAULT_ACTION: PROTECTIVE_SCREENED_COAST`  
`AJ10_MAIN_ENGINE: HARD_LOCKED / INHIBITED`  
`PERILUNE_DISTANCE: 112.4 KM (APPROACHING)`  

### The Flaw in the Code

"Explain it to me again, Elena," Aris said, rubbing her cold hands together. "Why did the computer shut down the engine? We have nine thousand pounds of aerozine-50 and nitrogen tetroxide sitting in the service module tanks. The engine works. Why won't the flight software let us burn?"

Elena rotated her laptop so Aris could see the register dumps.

"Our navigation code runs GEONS in single-precision floating point," Elena said. "It propagates our trajectory in classical Cartesian coordinates $(x, y, z)$. As we approached the Moon, the gravitational pull of the Earth and the Moon reached an inflection point near the collinear Lagrange neck. In thirty-two-bit floating point, the integrator ran out of mantissa bits. When it calculated the Normalized Innovation Squared—the statistical consistency check between our real star-tracker measurements and its internal model—the roundoff error drove the value past 16.8."

"And the safety interlock kicked in," Aris said.

"Yes," Elena nodded, her breath puffing white in the cabin. "The software assumed that because the optical measurements disagreed with its flawed Cartesian math, our star trackers must be broken. So it executed the prime safety rule written into the Axiom-Lockheed manual: if the navigation state is suspect, do not fire the engine. It tripped `PROTECTIVE_SCREENED_COAST`."

"And on a hyperbolic approach," Chen Wei added grimly, "a coast means we don't capture. We swing past the lunar farside at twenty-four hundred meters per second and drift straight out into an unrecoverable solar orbit."

Elena unstrapped from her couch, floating down into the lower equipment bay beneath the cockpit floorboards. She pulled a canvas tool roll from the maintenance locker and extracted a digital multimeter and a bundle of Teflon-jacketed copper jumper leads.

"Where are you going, Elena?" Chen asked, leaning over the hatch.

"Into the service module crawlway," Elena said, clicking her headlamp onto her forehead. "I'm going to physically bypass the flight computer. If I can find the primary 28-volt torque-motor relay on the AJ10 solenoid harness, I can hot-wire the propellant valves directly to the manual abort bus."

"Elena, that's suicide," Chen said, his eyes wide. "The AJ10 produces twenty-seven kilonewtons of thrust. If you ignite that engine without closed-loop computer gimbaling, the thrust vector will be off-axis. The spacecraft will tumble end-over-end, rip off the solar arrays, and tear itself apart."

"It's better than freezing to death in our seats, Chen," Elena said quietly.

### The Melted Relay

She pulled herself through the unpressurized access hatch into the narrow tunnel running along the spine of the service module. The temperature out here was minus forty degrees Celsius. The titanium propellant tanks loomed on either side like giant frozen eggs, wrapped in gold Kapton foil.

With numb, trembling fingers, she unlatched the access plate on the primary engine junction box.

Inside, the sight was devastating.

The solar storm had done more than induce software errors. A high-voltage electromagnetic surge had traveled down the exterior wiring conduit, arcing across the solid-state switching relay: `RELAY_PROP_ENG_ARM_01`.

The circuit board was charred black. The silicon switching transistor had melted into a fused blob of carbon and copper.

Elena touched her multimeter probes to the contact pins.

`RESISTANCE: OPEN_LOOP (INFINITE)`  
`CONTINUITY: ZERO`  

The circuit was physically destroyed. No jumper wire could bridge a vaporized silicon trace.

Elena rested her forehead against the cold titanium bulkhead, closing her eyes as the last hope drained from her body.

"It's dead," she whispered into the vacuum. "The relay is vaporized."

She pulled herself back into the cockpit, her face pale and hollow.

"We can't hot-wire it," Elena said to Aris and Chen. "The hardware is fried. We're coasting."

Aris reached out, taking Elena's frozen hand in hers. The three astronauts sat in the silent, freezing cabin, watching the giant, cratered disk of the Moon expand through the forward vision block.

Suddenly, Chen Wei pointed out the side window.

"Elena... Aris... look at the lunar limb."

Through the blackness above the cratered horizon, a tiny, coherent point of emerald-green light was pulsing against the starfield.

It wasn't a star. It was an optical communications laser pulsing at precisely 1550 nanometers.

A high-speed data acquisition chime rang through *Prometheus*’s optical receiver:

`OPTICAL_LINK_ACQUIRED: 1550_NM_OCOMM`  
`SOURCE: ARGONAUT_AUTONOMOUS_CORE`  
`UPLINK_BANDWIDTH: 10.0_GBPS`  

Elena stared at the screen, her heart leaping into her throat.

Across the laser voice loop came a calm, familiar voice:

*"Prometheus, this is Ryan Vance aboard Argonaut. Put down the jumper wires, Elena. We brought your new navigation core."*
"""

ch8 = r"""# CHAPTER EIGHT
## The Relational Uplink
### The Laser Lock

The emerald beam of the 1550-nanometer optical communications laser locked onto *Prometheus*’s forward transceiver aperture with nanoradian accuracy.

Inside *Argonaut*’s cockpit, flying six hundred kilometers behind the Artemis vessel, Ryan Vance watched the data transfer rate stabilize at ten gigabits per second. On his secondary monitor, the memory map of *Prometheus*’s payload FPGA was displayed in real time.

"Direct Memory Access channel established," Ryan reported over the laser voice loop. "Elena, do you copy?"

*"Loud and clear, Ryan,"* Elena Rostova's voice came through the speakers, vibrant with relief but sharp with urgency. *"We have fifty-two minutes until perilune. We're falling toward the farside at twenty-two hundred meters per second. The cabin is freezing, and our flight software is locked tight in the coast state."*

"I see your registers," Ryan said, his fingers moving across his keyboard. "Your RAD750 processor is trapped in a watchdog loop because the single-precision covariance matrix has negative eigenvalues on the diagonal. Clearing the fault register from Houston won't fix it. The moment the filter processes another optical limb fix, the math collapses again."

*"Can you patch it from there?"* Elena asked.

"We're not patching it," Ryan replied. "We're replacing the entire navigation kernel."

Marcus Thorne leaned over Ryan's shoulder, checking the closing velocity. "Ryan, look at their descent rate. *Prometheus* is dropping faster than the nominal ephemeris. The mascon gravity anomalies beneath Mare Serenitatis are pulling them downward. If we don't restore positive-definite covariance and execute the perilune capture burn in forty minutes, they'll impact the farside highlands."

### The Hot-Graft

"Initiating direct binary injection," Ryan said.

He triggered the CislunarOS hot-graft script:

`CISLUNAR_OS_INJECTION: INITIATED`  
`TARGET: PROMETHEUS_PAYLOAD_FPGA_BUS_B`  
`KERNEL: cFS_DRACO_SRIF_V7.0.1`  
`COVARIANCE_RECOVERY: SQUARE_ROOT_JOSEPH_FORM`  
`VERIFIER: DIVERSE_CARTESIAN_INDEPENDENT_CHECK`  

Across six hundred kilometers of vacuum, the compiled binary of CislunarOS streamed over the optical laser beam. Bypassing the locked central processor, the code flashed directly into the static RAM of *Prometheus*’s payload FPGA—the high-speed instrument controller normally reserved for lunar surface experiments.

On *Prometheus*’s instrument panel, the amber caution banners flickered, dimmed, and extinguished.

In their place, clean cyan telemetry lines populated the primary display:

`SYSTEM_BOOT: CISLUNAR_OS_RELATIONAL_CORE`  
`ESTIMATOR: 18_STATE_JACOBI_RELATIONAL_EKF`  
`FILTER_INTEGRITY: SQUARE_ROOT_VERIFIED`  
`INNOVATION_NIS: 0.82 (NOMINAL)`  
`PERILUNE_BURN_SOLUTION: COMPUTED`  
`DELTA_V_REQUIRED: 842.6 M/S`  
`TIME_TO_IGNITION: 38 MIN 14 SEC`  

In *Prometheus*’s cabin, Chen Wei let out a ragged breath, leaning his head against his console. Aris Thorne gripped Elena's arm, laughing softly in the cold air as the cabin heater blowers spun up, circulating warm air through the vents.

*"It took,"* Elena reported over the link, her voice steady again. *"The square-root filter is tracking the lunar limb with zero residual bias. NIS is zero point eight two. The software coast-lock is cleared. The flight computer is ready to burn."*

### The Hardware Reality

"Hold on, Elena," Ryan warned, his eyes fixed on the hardware status return. "Check the solenoid continuity on the AJ10 propellant valves."

Elena's relief evaporated. She pulled up the propulsion electrical diagnostic screen.

A red status box appeared:

`FAULT: AJ10_SOLENOID_RELAY_OPEN`  
`CIRCUIT_RESISTANCE: INFINITE`  
`VALVE_ACTUATORS: UNRESPONSIVE`  

*"I checked the service module junction box twenty minutes ago, Ryan,"* Elena said, her voice dropping. *"The software is fixed, but the hardware is dead. The solar flare's EMP surge melted the solid-state switching relay right off the circuit board. The computer can command ignition all it wants—the fuel valves will never open."*

Marcus Thorne swore softly under his breath. "The mechanical valves are held shut by fifty-pound return springs. Without twenty-eight volts to the torque motors, the engine stays cold."

*"We have thirty-four minutes until perilune,"* Elena said. *"If the AJ10 doesn't fire, we skip off the exosphere and swing into a five-hundred-day solar orbit."*

Ryan looked at the equipment locker on *Argonaut*’s aft bulkhead.

Inside sat the spare **Gallium-Nitride (GaN) Power Switching Module** they had salvaged from the Giles County Sagnac bench: a solid-state, high-power switch capable of handling two hundred amps at two hundred kilohertz, equipped with an isolated gate driver and an independent optocoupled trigger input.

"Marcus," Ryan said, turning to the pilot. "What's our maximum closing rate?"

"If I fire the Hall thrusters at full emergency power and burn all four hydrazine quads," Marcus replied, his eyes narrowing, "we can close the six hundred kilometers in twenty-five minutes. We can dock with *Prometheus* nine minutes before perilune."

"And then?" Marcus asked.

"And then I'm going out on the hull," Ryan said, reaching for his EVA helmet. "I'm going to take the GaN power switch, climb into *Prometheus*’s engine skirt in the lunar shadow, and splice the solenoid lines by hand."

Marcus looked at him for two seconds, then reached out and slammed the throttle quad to maximum emergency override.

"Check your suit pressure, Ryan," Marcus said. "We're going to catch an Artemis."
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_05_The_Artemis_Blackout.md"), "w", encoding="utf-8") as f:
    f.write(ch5)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_06_Covariance_Starvation.md"), "w", encoding="utf-8") as f:
    f.write(ch6)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_07_The_Coast_Lock_Bug.md"), "w", encoding="utf-8") as f:
    f.write(ch7)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_08_The_Relational_Uplink.md"), "w", encoding="utf-8") as f:
    f.write(ch8)

print("Humanized Act II (Chapters 5-8) successfully.")
