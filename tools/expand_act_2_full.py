import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

ch5_full = r"""# CHAPTER FIVE
## The Artemis Blackout
### The Blind Translunar Run

The solid rocket booster did not separate gently. It blew off with an ear-splitting concussive slam that drove Ryan Vance's helmet into the Kevlar headrest of *Argonaut*’s command couch.

Outside the narrow, quartz-laminated vision blocks, the pitch-black void of deep space was suddenly illuminated by the blinding, incandescent violet-blue plasma plume of the twin 15-kilowatt Hall-effect electric thrusters. Inside the vacuum acceleration chambers of the magnetic nozzles, high-purity xenon gas was stripped of its electrons by a 300-volt radial electric field, accelerating heavy ions to thirty-two kilometers per second. The gentle, unyielding push of zero point two gravities pinned Ryan and Marcus Thorne into their harnesses.

"Translunar injection burn complete," Marcus called out, his gloved fingers flying across the auxiliary propulsion panel. "Booster staging confirmed. The spent Castor solid casing is tumbling away behind us into a heliocentric graveyard orbit. We are in the cislunar corridor."

On the central tactical navigation display, the Earth was already a swirling blue-and-white marble receding at eleven point two kilometers per second. Four hundred thousand kilometers ahead, the Moon was a pale, razor-sharp crescent hanging against the starfield like a curved bone.

And between them, an invisible wall of solar fury was tearing the cislunar communication grid to shreds.

"Look at the solar flux monitor on channel four," Marcus said, pointing at the spiking telemetry graph. "That wasn't a standard coronal mass ejection. It was an X8.4 solar radio burst. A mega-flare. The radio emission from the Sun is pumping gigawatts of broadband thermal noise directly into the lower gigahertz bands. It's pouring into the sidelobes of the 70-meter Deep Space Network parabolic dishes in Canberra, Goldstone, and Madrid."

"The DSN is blinded," Ryan said.

"Worse than blinded," Marcus replied grimly. "Space Command has been pinging our transponder on the emergency military frequency every forty seconds. They are trying to uplink an automated remote kill-command to our flight termination unit. They think we stole an orbital weapon."

"Let them ping," Ryan said with icy calm. He reached across the center console, flipped a red mechanical safety guard, and severed the RF receiver antenna bus with a physical toggle switch. "We don't need their ground stations. We are off the grid."

"Ryan, nobody flies cislunar space without the Deep Space Network!" Marcus shouted. "How do we navigate? If we drift by a hundredth of a degree, we will miss the Moon's capture corridor and fling ourselves into an unrecoverable solar orbit!"

"We navigate by reality, Marcus," Ryan said. He tapped a command into the secondary flight terminal. "Initialize the X-ray pulsar receiver."

### The X-Ray Sights

On the dorsal hull of *Argonaut*, an array of four silicon-drift X-ray detectors unlatched from their launch locks and oriented toward the galactic coordinates of four millisecond pulsars: **PSR J0437-4715**, **PSR B1821-24**, **PSR B1937+21**, and **PSR J0030+0451**.

Unlike radio signals, which can be swamped by solar plasma and ionospheric scintillations, high-energy X-ray photons emitted by millisecond pulsars cut through solar flares like diamond through glass. Each pulsar had a rotational period known to fifteen decimal places.

"We have pulse acquisition on all four channels," Ryan reported, watching the photon timestamps stream into the FPGA. "The Kintex core is folding the arrival times using the square-root information filter. Position fix: three hundred and twelve thousand kilometers from Earth, eighty-four thousand kilometers from the Moon. Velocity error: less than three millimeters per second."

Marcus stared at the display, the tension in his shoulders slowly releasing. "A celestial GPS that never relies on a ground station."

"It's not GPS," Ryan said. "GPS relies on an absolute Euclidean coordinate grid maintained by atomic clocks on Earth. Pulsar navigation is purely relational. We are measuring the differential phase arrivals of light emitted across the galaxy. We are locating *Argonaut* within the causal network of the universe."

"What about *Prometheus*?" Marcus asked, leaning forward. "Can you find them?"

Ryan retuned the narrow-band optical spectrometer. "Scanning the translunar corridor at their last known ephemeris."

On the long-range optical sensor, sixty thousand kilometers ahead, a tiny point of light was pulsing erratically against the blackness of space.

"I have them," Ryan said, zooming in on the optical track. "Visual acquisition confirmed. But look at their light curve."

The light reflected from *Prometheus* wasn't steady. It was strobing with a rhythmic, sickening flash every three point two seconds.

Marcus leaned in, his weathered face draining of color. "That's not attitude stabilization. She's in a flat spin."

"Their attitude control thrusters have fired asymmetrically," Ryan said, reading the Doppler shift on the reflected solar spectrum. "Elena and her crew are spinning out of control at eighteen revolutions per minute. And they are plunging toward the lunar farside at two point four kilometers per second."

### The Daughter in the Void

Marcus pressed his gloved hand against the instrument panel. His jaw was clenched so hard the muscles bunched beneath his weathered skin.

"Aris is on that ship, Ryan," Marcus whispered, his voice dropping into a register Ryan had never heard before—hollow, stripped of the cocky bravado of an Air Force test pilot. "My daughter is strapped into the center couch of that tumbling tomb."

Ryan looked up from the navigation terminal. "You never told me Aris was on Artemis-7."

"Why would I?" Marcus said, his eyes fixed on the strobing pixel of light. "She stopped speaking to me four years ago when I walked out of the astronaut office. She thought I was throwing my career away over academic paranoia. She told me the Axiom software was certified by the greatest aerospace engineers on Earth. She said I was chasing ghosts."

Marcus let out a ragged breath, blinking back moisture. "And now she's freezing to death forty thousand miles from home because those 'greatest engineers' couldn't invert a covariance matrix."

"We will reach them, Marcus," Ryan said quietly.

"How?" Marcus demanded, pointing at the propellant readouts. "Our Hall thrusters produce thirty-two kilometers per second of exhaust velocity, but they only give us point-two Gs of thrust! At this acceleration, it will take us thirty-eight hours to match their velocity vector! In thirty-eight hours, *Prometheus* will have skipped off the lunar exosphere and flung itself past the Moon into heliocentric graveyard orbit!"

"We don't match their velocity in flat space," Ryan answered, pulling up the Montgomery shape-sphere trajectory optimizer. "We use a chaotic three-body resonant capture. Look at the invariant manifolds of the Earth-Moon system."

### The Invariant Manifold

On the display, the classical straight-line trajectories of Newtonian orbital mechanics dissolved. In their place appeared a breathtaking, intricate web of swirling phase-space curves: the stable and unstable manifolds emanating from the collinear Lagrange points $L_1$ and $L_2$.

"Poincaré discovered this over a century ago," Ryan explained, tracing the glowing blue filaments with his stylus. "In a three-body gravitational field, space is threaded with invariant manifolds—invisible tube-like corridors in phase space that allow a spacecraft to transition from Earth-centered orbit to lunar orbit with almost zero expenditure of propellant."

"The ballistic capture corridors," Marcus said, his pilot's instinct grasping the geometry.

"Yes," Ryan said. "Because the Moon's update latency creates an effective refractive gradient, the stable manifold acts like a gravitational fiber-optic cable. If we fire our Hall thrusters for exactly eighteen minutes at an angle of thirty-four degrees to the ecliptic, we can inject *Argonaut* directly into the funnel of the lunar $L_1$ manifold."

"And that cuts our transit time?"

"It cuts our intercept time from thirty-eight hours to ninety-four minutes," Ryan said. "The manifold will accelerate us along a hyperbolic plunge, dropping us directly into *Prometheus*’s orbital plane eighty kilometers above the farside crater Antoniadi."

Marcus grabbed the manual throttle handle, his knuckles whitening through his pressurized gloves. "Upload the vector, Ryan. Let's ride the lightning."
"""

ch6_full = r"""# CHAPTER SIX
## Covariance Starvation
### The Taurid Swarm

The impact arrived without sound.

In the vacuum of deep space, kinetic collisions do not generate acoustic waves. What Ryan Vance felt was a sudden, violent shudder that vibrated through the carbon-composite frame of the command module, accompanied by a sharp, high-frequency ringing that echoed through the pressure hull like a tuning fork.

On the master caution panel, three red indicators flashed simultaneously:

`WARN: AUX_LINE_PRESSURE_DROP [SECTOR_3_FORWARD]`  
`NITROGEN_RESERVE: 68% (DECREASING @ 1.4 PSI/SEC)`  
`MOMENTUM_ACCUMULATION: +4.2 N-m-s`  
`SPIN_RATE_YAW: +2.8 DEG/SEC`  

"Micrometeoroid hit!" Marcus yelled, his hands instantly gripping the flight controls. "We just punched through a Taurid debris stream! An iron-nickel particle, millimeter-scale, traveling at thirty-five kilometers per second!"

"Hull integrity is holding," Ryan said, rapidly scanning the pressure transducers. "The command module inner Kevlar-aluminum Whipple shield stopped the projectile. But the secondary penetrator exited the forward equipment bay."

"It severed the auxiliary cold-gas nitrogen supply line to the forward reaction control thrusters," Marcus said, reading the telemetry. "The line is venting into vacuum at thirty atmospheres! It's acting like an unguided rocket nozzle on the forward boom! We're beginning to tumble!"

Outside the cockpit windows, the starfield began to rotate in dizzying, disorienting circles. The crescent Moon swept across the vision block once every twelve seconds, followed by the blinding glare of the Sun and the blue disk of the Earth.

"Compensate with the main RCS!" Ryan urged.

"I can't!" Marcus shouted back. "If I fire the hydrazine thrusters against an uncontrolled nitrogen vent, we'll drain our orbital insertion propellant in eight minutes! And when the nitrogen runs dry, we won't have enough delta-v left to intercept *Prometheus*!"

### The Truss EVA

Marcus unbuckled his shoulder harness, pushing himself up out of the command couch against the centrifugal force of the spin. He pulled open the locker behind the seats and dragged out a white, multi-layered extravehicular mobility unit.

"Marcus, what are you doing?" Ryan demanded.

"I'm going outside to crimp the line," Marcus said, pulling on the heavy thermal-micrometeoroid overgarment. "The rupture is twelve feet out on the forward sensor boom. If I can reach the manual isolation valve behind the star tracker assembly, I can shut off the leak with a pair of vise-grips."

"You can't go EVA while the ship is spinning at three degrees per second!" Ryan said. "The centrifugal force will peel you off the hull! If you lose your tether, you will drift into translunar space with forty minutes of life support!"

"If I don't go out there, Ryan, we run out of propellant and die anyway," Marcus said calmly, his voice settling into the steady, fatalistic cadence of an experimental test pilot. "Help me with the helmet ring."

Ryan stared at him for two seconds, then swallowed his fear. He grabbed the heavy fiberglass helmet, aligned the neck ring indexing pins, and twisted it until the brass locking dogs snapped shut with a heavy mechanical click.

"Comms check," Ryan said, plugging his headset into the intercom.

*"Loud and clear,"* Marcus's voice crackled inside Ryan's headset. *"Depressurize the airlock."*

Ryan operated the manual blowdown valve on the auxiliary transfer airlock. The hiss of venting air died into absolute silence as the cabin pressure dropped to zero. Marcus pushed open the outer hatch and stepped into the infinite, starry void.

Outside, the universe was a spinning kaleidoscope of black velvet, blinding solar glare, and rotating planetary crescents. Marcus hooked his primary Kevlar safety tether to the exterior guide rail, his gloved hands gripping the cold titanium rungs.

*"Centrifugal force is pulling me outward,"* Marcus reported, his breathing heavy and ragged in the comms loop. *"Moving along the truss toward the forward boom."*

"Watch your tether!" Ryan called out, monitoring the hull cameras from the cockpit. "The venting nitrogen is creating an icy crystalline cloud around the boom. Visibility is zero!"

*"I see the rupture,"* Marcus gasped. *"The braided stainless line is severed clean through. Liquid nitrogen is flashing into vapor at the fracture. The ice is coating the handrails like grease."*

On the navigation console, Ryan watched the nitrogen pressure plummet:

`NITROGEN_RESERVE: 41%`  
`SPIN_RATE_YAW: +4.1 DEG/SEC`  

*"I'm at the manual shutoff valve,"* Marcus said, his voice straining against the violent vibrations of the thruster boom. *"The valve wheel is jammed with ice! I can't turn it with pressurized gloves!"*

"Use the mechanical leverage tool from your pouch!" Ryan urged.

*"Trying... tool engaged... pulling with both hands... come on, you bastard..."*

A sharp grunt echoed over the radio, followed by the sound of metal tearing against frozen steel.

*"Valve is turning! Quarter turn... half turn... closed! Nitrogen vent stopped!"*

### The Tether Snap

On Ryan's console, the pressure drop halted at thirty-two percent.

`WARN_RESOLVED: LINE_ISOLATED`  
`REMAINING_NITROGEN: 32.4%`  

"Line is sealed!" Ryan yelled into the mic. "Marcus, get back inside!"

*"Copy that... returning along the guide rail—wait!"*

A sickening snap reverberated through the hull intercom.

On the forward camera monitor, Ryan watched in horror as the auxiliary carabiner on Marcus's safety tether caught against a jagged shard of meteoroid-shredded thermal blanketing. The braided Kevlar cord sheared through, whipping wildly into the vacuum.

Marcus's boots slipped from the titanium foot restraint. The centrifugal force of the spacecraft's rotation hurled him outward, off the truss, into the pitch-black void.

*"Tether failure!"* Marcus's voice was a ragged shout over the radio. *"I'm off the hull! Rolling in yaw! Distance opening—ten feet... twenty feet!"*

"Marcus!" Ryan threw off his restraints, lunging for the remote thruster console.

*"Do not fire the main thrusters, Ryan!"* Marcus gasped, his breathing ragged in his suit. *"Your exhaust plume will incinerate me! Deploy the mechanical grappling arm!"*

Ryan's hands flew across the auxiliary robotics panel. On the dorsal hull, the four-meter carbon-fiber capture boom swung outward, its three-jawed robotic end-effector expanding into the vacuum.

"Marcus, throw your tether line toward the wrist joint!" Ryan shouted.

Marcus twisted his body in mid-air, using the small cold-gas puffers of his SAFER emergency backpack to arrest his tumble. He unclipped his secondary steel carabiner, swung it in a wide arc, and threw the weighted line directly into the mechanical jaws of the boom.

The steel jaws snapped shut.

`GRAPPLE_LOCK: CONFIRMED`  
`TETHER_TENSION: 420 N`  

Ryan engaged the winch motor, hauling Marcus hand-over-hand back toward the airlock portal. Three minutes later, Marcus tumbled into the depressurized chamber, his chest heaving, his face pale as chalk beneath his gold-tinted visor.

### Gravity-Gradient Damping

The outer airlock hatch slammed shut. The airlock hissed as cabin air repressurized the compartment. Marcus pulled off his helmet, his face drenched in sweat, his hands shaking from adrenaline and the brutal cold of the vacuum.

"The leak is stopped," Marcus said, collapsing into the pilot's couch. "And I'm still breathing. But we're still tumbling at four degrees per second. How do we kill the spin without burning our remaining hydrazine?"

Ryan smiled, his fingers typing rapidly into the ArgonautOS command shell. "We don't use propellant. We use the Moon."

"The Moon?" Marcus frowned. "We're eighty thousand kilometers away!"

"The Moon is a gravitational quadrupole," Ryan said, activating the **Receding-Horizon Quadratic Programming (QP)** guidance module. "Its update-latency well creates a differential tidal tensor across *Argonaut*’s six-meter composite boom. The nose of the spacecraft is fifty nanoseconds closer to the lunar update well than the tail. That infinitesimal latency gradient exerts a physical restoring torque:

$$\boldsymbol{\tau}_{\text{tidal}} = \frac{3GM_{\text{Moon}}}{r^3} \hat{\mathbf{r}} \times (\mathbf{I} \cdot \hat{\mathbf{r}})$$

"By executing micro-adjustments with our magnetic torquer coils against the interplanetary magnetic field, ArgonautOS can harvest that tidal torque. In forty-five minutes, the Moon's own gravity will damp our spin to zero."

Marcus watched the telemetry display in stunned silence as the rotation rate began to smooth out, dropping tenth by tenth of a degree.

"You're using the universe's network latency as an orbital brake," Marcus said.

"Distance is impedance, Marcus," Ryan said. "When you understand the network, you never have to fight it."
"""

ch7_full = r"""# CHAPTER SEVEN
## The Coast-Lock Bug
### The Stranded Prometheus

Inside the command module of *Artemis-7*, the temperature had dropped to three degrees Celsius.

Condensation clung to the exposed aluminum ribbing of the pressure hull, dripping in slow, floating globules through the zero-gravity air. The only illumination came from the sickly amber glow of emergency status panels and the flickering blue light of Dr. Elena Rostova's diagnostic laptop.

Elena blew into her gloved hands, her breath hanging in the cabin like frozen smoke. Beside her in the center couch, lunar geologist Aris Thorne was shivering beneath two thermal survival blankets, her lips faintly blue. In the right couch, systems specialist Chen Wei was tapping a mechanical pencil against his flight kneeboard, tracking their consumable reserves with grim mathematical certainty.

"Oxygen partial pressure is down to sixteen kilopascals," Chen said, his voice flat and hoarse. "At half-rations, our lithium hydroxide scrubbers will saturate in nine hours. After that, carbon dioxide toxicity sets in."

"What about Houston?" Aris asked, her teeth chattering. "Has the Deep Space Network broken through the solar flare?"

Elena glanced at the primary communications terminal. The signal-to-noise ratio meter was flatlined at minus forty decibels.

`DSN_CARRIER_LOCK: LOST (CANBERRA_DSS-43)`  
`DOWNLINK_STATUS: BLINDED_BY_SOLAR_RF`  
`UPLINK_COMMAND_QUEUE: EMPTY`  

"Houston is gone," Elena said quietly. "The solar radio burst is pouring gigawatts of thermal noise into every ground receiver on Earth. We are completely on our own."

She looked up at the central flight avionics display. The warning banner that had sealed their fate six hours ago was still burning in stark, unforgiving amber:

`SYSTEM FAULT: GNC_COVARIANCE_COLLAPSE`  
`KALMAN_FILTER_STATUS: NIS_EXCEEDED (17.42 > 16.80)`  
`FAULT_ACTION: PROTECTIVE_SCREENED_COAST`  
`MAIN_ENGINE_STATUS: DISARMED / HARD_LOCKED`  
`MANUAL_OVERRIDE: INHIBITED_BY_SAFETY_INTERLOCK`  

"It's the coast-lock bug," Elena muttered, rubbing her aching temples. "The software defect Ryan warned us about."

### The Legacy Trap

"Explain it to me again, Elena," Aris said, pulling the blankets tighter around her shoulders. "Why did the engine shut down? We have twenty-two thousand pounds of aerozine-50 and nitrogen tetroxide sitting in the service module tanks! Why won't the computer let us burn?"

Elena pointed at the single-precision floating-point register displayed on her laptop.

"Our flight computer runs GEONS," Elena explained. "It models our trajectory using classical Cartesian coordinates $(x, y, z)$. As we approached the Moon, the gravitational pull of the Earth and the Moon reached an inflection point near the collinear Lagrange neck. In single precision, the 32-bit floating point processor ran out of mantissa bits. When it calculated the Normalized Innovation Squared—the statistical measure of whether our physical sensor measurements match the mathematical model—the roundoff error drove the value past 16.8."

"And the safety software thought the sensors were broken," Aris said.

"Exactly," Elena nodded bitterly. "The software assumed that because the measurements didn't match its flawed Cartesian equations, our star trackers and laser altimeters must be hallucinating. So it executed the prime safety rule written into the Axiom-Lockheed flight manual: when in doubt, do not fire the engine. It locked the propellant isolation valves, disabled the gimbal actuators, and threw *Prometheus* into `PROTECTIVE_SCREENED_COAST`."

"And on a hyperbolic trajectory," Chen Wei said, staring out the forward window at the looming, cratered expanse of the Moon, "a coast means death. We don't enter orbit. We skim past perilune at twenty-four hundred meters per second, slingshot around the farside, and drift into heliocentric space."

### The Crawlway Descent

"I'm not going to freeze to death waiting for a computer that can't divide by three," Elena said with sudden, fierce resolve.

She unbuckled her restraint harness and pushed herself down into the lower equipment bay beneath the cockpit floorboards. She pulled a heavy aluminum toolbox from the storage locker and extracted a digital multimeter, a pair of wire strippers, and a bundle of Teflon-insulated copper jumper leads.

"Elena, what are you doing?" Chen asked, leaning over the hatchway.

"I'm going into the service module crawlway," Elena said, clicking her headlamp onto her forehead. "I'm going to physically bypass the flight computer. If I can find the primary 28-volt torque-motor relay on the AJ10 engine solenoid bus, I can hot-wire the propellant valves directly to the manual abort battery."

"Are you insane?" Chen said, his eyes wide with terror. "The AJ10 engine produces twenty-seven kilonewtons of thrust! If you ignite that engine without closed-loop computer gimbaling, the thrust vector will be off-axis! The spacecraft will tumble end-over-end, rip off the solar arrays, and tear itself apart under forty gravities of rotational shear!"

"It's better than dying in our sleep!" Elena shouted back.

She wriggled through the unpressurized crawlway hatch into the freezing, narrow tunnel running down the spine of the service module. The temperature out here was minus forty degrees. Titanium propellant tanks loomed on either side like giant frozen eggs, wrapped in gold Kapton insulation. Her breath froze into ice flakes on her visor.

With trembling fingers, she peeled back the wiring conduit above the AJ10 engine gimbal gimbal block.

There, embedded in a charred aluminum junction box, sat the primary solid-state relay: `RELAY_PROP_ENG_ARM_01`.

She touched her multimeter probes to the contact pins.

The digital readout flickered: `0.00 V`. Resistance: infinite.

Elena's stomach dropped into a bottomless abyss. The copper trace on the circuit board hadn't just tripped. It had vaporized. The intense induced voltage from the solar flare had turned the silicon switching transistor into an inert lump of melted slag.

No jumper wire could fix this. The circuit was dead.

### The Emerald Beam

Despairing, Elena pulled herself back through the crawlway hatch into the cockpit. She dragged herself onto the floorboards, shivering uncontrollably, her face gray with defeat.

"It's gone," Elena whispered. "The relay is vaporized. We can't hot-wire the engine. There's nothing left to do."

Aris Thorne reached down, taking Elena's frozen hand in hers. "Then we make peace with it, Elena. We did everything we could."

Chen Wei bowed his head, closing his eyes in silent prayer.

Suddenly, Aris gasped. "Elena... Chen... look out the forward observation port!"

Elena pulled herself up to the glass.

Outside the main vision block, hanging fifty kilometers above the jagged, sunlit rim of the lunar crater drylands, a tiny, piercing spark of light was shining against the velvet blackness.

It wasn't a star. Stars didn't pulse with a coherent, monochromatic, emerald-green brilliance.

It was an optical laser beam pulsing at precisely 1550 nanometers.

A high-speed data acquisition tone chirped on *Prometheus*’s optical communications terminal. On the secondary screen, a line of green text decrypted with flawless precision:

`OPTICAL_LINK_ACQUIRED: 1550_NM_OCOMM`  
`SOURCE_IDENTIFIER: ARGONAUT_RELATIONAL_CORE`  
`UPLINK_RATE: 10.0_GBPS`  
`SECURITY_HANDSHAKE: QRC_CIPHER_ACCEPTED`  

Elena stared at the screen, tears welling in her cold-reddened eyes.

Across the optical link came a single, voice-encoded transmission:

*"Prometheus, this is Ryan Vance aboard Argonaut. Step away from the jumper wires, Elena. We brought your new brain."*
"""

ch8_full = r"""# CHAPTER EIGHT
## The Relational Uplink
### The Silicon Graft

The emerald-green beam of the 1550-nanometer optical communications laser locked onto the forward receiver aperture of *Prometheus* with nanoradian precision.

Inside the cockpit of *Argonaut*, flying six hundred kilometers behind the stricken Artemis vessel, Ryan Vance watched the data transfer rate climb to ten gigabits per second. On his console, the entire memory architecture of *Prometheus*’s primary flight computers was laid out in a real-time memory map.

"Direct Memory Access (DMA) injection channel open," Ryan reported over the high-bandwidth laser voice loop. "Elena, can you hear me?"

*"Loud and clear, Ryan!"* Elena Rostova's voice sounded through the speakers, vibrant with relief yet taut with tension. *"We have eighty-two minutes before perilune. We are descending toward the farside at twenty-two hundred meters per second. The cabin is freezing, and our flight software is locked down solid."*

"I see your registers," Ryan said, his fingers flying across his keyboard as he prepared the ArgonautOS payload injection. "Hastings's code is completely locked in the `PROTECTIVE_SCREENED_COAST` state machine. The CPU is looping in a watchdog trap because the single-precision covariance matrix has negative eigenvalues on the diagonal."

*"Can you clear the fault register from there?"* Elena asked.

"Clearing the register won't fix it," Ryan answered. "The moment the legacy filter processes another optical limb measurement, the covariance will collapse again. We have to replace the entire guidance kernel."

Marcus Thorne leaned over Ryan's shoulder, his eyes fixed on the relative trajectory plot. "Ryan, look at their closing velocity. *Prometheus* is dropping faster than the nominal ephemeris. The lunar mass concentrations beneath Mare Serenitatis are pulling them downward. If we don't restore positive-definite covariance and execute the perilune capture burn in sixty-four minutes, they will impact the farside highlands."

### The Injection

"I am executing the injection right now," Ryan said.

He engaged the primary execution script:

`ARGONAUT_OS_HOT_GRAFT: INITIATED`  
`TARGET: PROMETHEUS_AVIONICS_BUS_B`  
`INJECTING: KERNEL_SRIF_V5.4 (MONTGOMERY_SHAPE_SOLVER)`  
`MEMORY_OVERWRITE: 0x80000000 - 0x8FFFFFFF`  
`VERIFIER: CARTESIAN_INDEPENDENT_PARALLEL_CHECK`  

Across the six-hundred-kilometer gap of deep space, the compiled binary of ArgonautOS streamed over the optical laser beam. It bypassed the locked RAD750 central processor and flashed directly into the static RAM of *Prometheus*’s payload FPGA—the high-speed instrument controller normally reserved for lunar surface experiments.

On *Prometheus*’s instrument panel, the dead amber warning lights flickered, dimmed, and extinguished.

In their place, crisp, high-contrast cyan displays sprang to life:

`SYSTEM REBOOT: ARGONAUT_OS_RELATIONAL_CORE`  
`SOLVER: 18_STATE_JACOBI_RELATIONAL_EKF`  
`GEOMETRY: MONTGOMERY_SHAPE_SPHERE (S^2)`  
`COVARIANCE_STATUS: POSITIVE_DEFINITE_VERIFIED`  
`INNOVATION_NIS: 0.84 (NOMINAL)`  
`PERILUNE_INSERTION_BURN: ARMED`  
`DELTA_V_REQUIRED: 842.6 M/S`  
`TIME_TO_IGNITION: 58 MIN 14 SEC`  

In the cockpit of *Prometheus*, Chen Wei let out a ragged cheer, slapping the instrument console with his gloved hand. Aris Thorne leaned forward, tears streaming down her face as the cabin heater blowers spun up, circulating warm, filtered air through the vents.

*"It worked!"* Elena laughed over the comms loop. *"The filter is tracking the lunar limb with zero residual error! NIS is zero point eight four! The engine interlocks have released! We have green lights across the board!"*

### The Blown Solenoid

"Don't celebrate yet," Ryan warned, his voice tight as he analyzed the hardware diagnostic return. "Elena, check the solenoid continuity on the AJ10 bipropellant valves."

Elena's laughter died instantly. She tapped the propulsion diagnostic panel.

A red caution box appeared on the newly restored display:

`PROPULSION FAULT: AJ10_PILOT_SOLENOID_OPEN_CIRCUIT`  
`RESISTANCE: INFINITE (OPEN)`  
`VALVE_ACTUATOR: UNRESPONSIVE`  

*"No..."* Elena whispered, her voice cracking. *"I checked the crawlway junction box ten minutes ago. The relay is physically vaporized. The solar storm's EMP melted the silicon trace right off the board."*

Marcus Thorne swore violently, slamming his fist onto the edge of *Argonaut*’s flight desk. "The circuit is physically broken. The computer can send all the fire commands it wants—the fuel valves will never open."

*"We have fifty-four minutes until perilune,"* Elena said, her voice trembling. *"If the AJ10 doesn't fire, we can't stop. We will skip off the upper exosphere and fling ourselves into deep space with four hours of battery power left."*

Ryan stared at the schematic of the AJ10 propulsion bus glowing on his screen.

Then he looked at the gold-plated spare hardware mounted in *Argonaut*’s equipment locker: the auxiliary gallium-nitride (GaN) high-power solid-state switching module they had salvaged from the Giles County Sagnac vault.

### The Intercept Plan

"Marcus," Ryan said, turning to the pilot. "What is our maximum closing speed?"

"If I burn the Hall thrusters and fire all four hydrazine quads at full emergency thrust," Marcus replied, his eyes narrowing, "we can close six hundred kilometers in forty minutes. We can intercept *Prometheus* fifteen minutes before perilune."

"And then?" Marcus asked.

"And then I'm going out there," Ryan said, pulling his extravehicular helmet from its storage rack. "I'm going to take the GaN power switch, climb into *Prometheus*’s engine skirt in lunar shadow, and splice the solenoid lines with my own hands."

Marcus looked at him for three long seconds. A slow, savage smile spread across the veteran test pilot's face.

"Hold onto your harness, Ryan," Marcus said, jamming the throttle quad to maximum emergency override. "Let's go catch an Artemis."
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_05_The_Artemis_Blackout.md"), "w", encoding="utf-8") as f:
    f.write(ch5_full)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_06_Covariance_Starvation.md"), "w", encoding="utf-8") as f:
    f.write(ch6_full)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_07_The_Coast_Lock_Bug.md"), "w", encoding="utf-8") as f:
    f.write(ch7_full)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_08_The_Relational_Uplink.md"), "w", encoding="utf-8") as f:
    f.write(ch8_full)

print("Expanded Act II (Chapters 5-8) successfully.")
