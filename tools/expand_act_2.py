import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

ch5_expanded = r"""# CHAPTER FIVE
## The Artemis Blackout
### The Blind Translunar Run

The solid rocket booster did not separate gently. It blew off with an ear-splitting concussive slam that drove Ryan Vance's helmet into the Kevlar headrest of *Argonaut*’s command couch.

Outside the narrow, quartz-laminated vision blocks, the pitch-black void of deep space was suddenly illuminated by the blinding, incandescent violet-blue plasma plume of the twin 15-kilowatt Hall-effect electric thrusters. Inside the vacuum acceleration chambers of the magnetic nozzles, high-purity xenon gas was stripped of its electrons by a 300-volt radial electric field, accelerating heavy ions to thirty-two kilometers per second. The gentle, unyielding push of zero point two gravities pinned Ryan and Marcus Thorne into their harnesses.

"Translunar injection burn complete," Marcus called out, his gloved fingers flying across the auxiliary propulsion panel. "Booster staging confirmed. The spent solid casing is tumbling away behind us into a heliocentric graveyard orbit. We are in the cislunar corridor."

On the central tactical navigation display, the Earth was already a swirling blue-and-white marble receding at eleven point two kilometers per second. Four hundred thousand kilometers ahead, the Moon was a pale, razor-sharp crescent hanging against the starfield like a curved bone.

And between them, an invisible wall of solar fury was tearing the cislunar communication grid to shreds.

"Look at the solar flux monitor on channel four," Marcus said, pointing at the spiking telemetry graph. "That wasn't a standard coronal mass ejection. It was an X8.4 solar radio burst. A mega-flare. The radio emission from the Sun is pumping gigawatts of broadband thermal noise directly into the lower gigahertz bands. It's pouring into the sidelobes of the 70-meter Deep Space Network parabolic dishes in Canberra, Goldstone, and Madrid."

"The DSN is blinded," Ryan said.

"Worse than blinded," Marcus replied grimly. "Space Command has been pinging our transponder on the emergency military frequency every forty seconds. They are trying to uplink an automated remote kill-command to our flight termination unit. They think we stole an orbital weapon."

"Let them ping," Ryan said with icy calm. He reached across the center console, flipped a red mechanical safety guard, and severed the RF receiver antenna bus with a physical toggle switch. "We don't need their ground stations. We are off the grid."

"Ryan, nobody flies cislunar space without the Deep Space Network!" Marcus shouted. "How do we navigate? If we drift by a hundredth of a degree, we will miss the Moon's capture corridor and fling ourselves into an unrecoverable solar orbit!"

"We navigate by reality, Marcus," Ryan said. 

He keyed the initialization sequence on the gold-plated QRC guidance core mounted beneath the instrument glareshield.

On the upper avionics bus, the cryogenic silicon drift detectors—shielded behind five millimeters of solid tantalum to reject energetic solar protons—opened their shutter apertures to deep space. They did not search for GPS satellites or ground radars. They pointed their collimators at four immutable celestial beacons:

**PSR J0437-4715.**  
**PSR B1821-24.**  
**PSR B1937+21.**  
**PSR J0030+0451.**

Every millisecond, the X-ray pulses from the rotating neutron stars struck the silicon detectors. Inside the Kintex UltraScale+ FPGA, the raw arrival times were converted into phase offsets. 

"Look at the math, Marcus," Ryan said. "A classic GPS receiver measures pseudoranges from satellites orbiting Earth. But those satellites are orbiting inside an imaginary Cartesian coordinate system that rotates with the Earth's crust. It's a house of cards. When the solar storm hits, the ionosphere introduces differential delays, and the whole system lies to itself."

He brought up the QRC relational state equation:

$$\begin{pmatrix} \Phi_1 - \Phi_{0,1} \\ \vdots \\ \Phi_4 - \Phi_{0,4} \end{pmatrix} = \frac{1}{c}\begin{pmatrix} \nu_1 \hat{n}_1^T \\ \vdots \\ \nu_4 \hat{n}_4^T \end{pmatrix} \vec{r}_{\text{rel}} + \vec{N}_{\text{cycle}} + \vec{\epsilon}_{\text{noise}}$$

"The millisecond pulsars are not in Earth orbit," Ryan explained, his voice low and steady. "They are anchored in the deep gravitational potential of the galaxy. By measuring the phase differences across four non-coplanar pulsars, we determine our relational position relative to the Earth-Moon barycenter with an uncertainty under three hundred meters. In real time. On a chip that burns seven watts."

Marcus stared at the green navigation vector updating smoothly across the screen. There were no dropouts. There was no hunting. While every satellite in Earth orbit was screaming in confusion, *Argonaut* was cutting through the cislunar void like a scalpel.

"Thirty-eight hours to lunar orbit insertion," Marcus whispered.

"Then we have thirty-eight hours to make sure Elena is still alive to meet us," Ryan said.
"""

ch6_expanded = r"""# CHAPTER SIX
## Covariance Starvation
### The Tsiolkovsky Knife-Edge

At hour twenty-four of the translunar cruise, the universe reminded them that spaceflight is not a theoretical exercise.

*CLANG-CRACK.*

The impact was sharp, high-pitched, and violent—like a high-velocity rifle shot fired directly into the titanium frame beneath Ryan's boots.

The master alarm console flashed blinding amber. A shrieking audio tone stabbed through their communication headsets.

```
CAUTION & WARNING // PRIMARY RCS ATTITUDE LOOP FAILURE
PRESSURE TRANSIENT: MANIFOLD 2 PRESSURE DROPPING RAPIDLY
CURRENT: 24.1 BAR -> 12.8 BAR -> 4.2 BAR
MASS EXCURSION: NITROGEN ATTITUDE GAS VENTING TO VACUUM
ATTITUDE DIVERGENCE: YAW DRIFT 4.2 DEG/SEC // UNCHECKED
```

"Micrometeorite hit!" Marcus shouted, his body straining against his harness as the spacecraft began to twist. "Taurid debris stream! It punched straight through the thermal blanket on the forward port quadrant and severed the auxiliary cold-gas line!"

Outside the vision blocks, a white, incandescent blizzard of frozen nitrogen crystals boiled into the vacuum, spraying across the starfield. The venting gas was acting like an uncommanded rocket thruster, spinning *Argonaut* along its longitudinal axis at eighteen revolutions per minute.

"The reaction wheels are saturating!" Marcus yelled over the roar of the gyros. "They are at ninety-six percent RPM! If they hit the governor limit, the flywheels will trip the circuit breakers, and we will enter a flat spin! We won't be able to point the Hall thruster!"

Ryan didn't panic. His training as an astrodynamicist kicked in with ruthless, mathematical precision.

"Marcus, kill the automated RCS isolation valves!" Ryan commanded. "Do not let the computer try to fight the vent with opposite thrusters! It will burn through our remaining nitrogen in ninety seconds!"

"If I close the main manifold, we have zero attitude control!" Marcus protested.

"Close it!" Ryan roared.

Marcus slammed his fist down on the emergency red paddle. The heavy solenoid valves snapped shut with a hollow thud.

The venting nitrogen stopped. But the ship was still spinning, the Milky Way whirling across the windows in a dizzying, sickening blur.

"We have twelve kilograms of cold gas left in the reserve tank," Marcus gasped, wiping sweat from inside his visor. "Twelve kilograms. We need forty kilograms to execute the terminal proximity docking with *Prometheus*. We are out of gas, Ryan. We've hit the Tsiolkovsky knife-edge. We can either stop our spin and drift into space, or save the gas and crash into the Moon."

"There is a third option," Ryan said, his fingers flying across the field terminal, pulling up the predictive guidance module.

"What third option?"

"We don't use cold gas to steer," Ryan said. "We use the Hall thruster's gimbaled magnetic nozzle."

"The Hall thruster produces less than one newton of thrust!" Marcus said. "It's an ion engine! You can't use it for fast attitude maneuvers!"

"In a Cartesian frame, you can't," Ryan answered, displaying the receding-horizon quadratic program. "Classical target-point guidance calculates maneuvers based on instantaneous velocity errors. It demands huge, explosive bursts of RCS thrust. But the receding-horizon QP solver looks twelve intervals ahead across a six-hour horizon:

$$\min_u \sum_{k=0}^{N-1} \left( x_k^T Q x_k + u_k^T R u_k \right) + x_N^T P_N x_N$$

"It uses the Earth-Moon gravity gradient itself to torque the spacecraft," Ryan explained, showing the dynamic simulation. "We fire the Hall thruster in continuous, sub-newton micro-pulses, timed exactly to the rotation of the hull. We let the tidal pull of the Moon damp the roll. It doesn't fight the spin; it redirects the angular momentum into our orbital inclination!"

"You're using the Moon's gravity well as an attitude brake," Marcus whispered, his eyes wide.

"In matched simulation runs, this algorithm uses twenty point seven percent less delta-V than tuned NASA guidance," Ryan said, locking the commands into the FPGA. "Engaging receding-horizon QP solver."

The twin Hall thrusters hummed. The blue ion beams flickered in rapid, microsecond bursts, gimbaling by three degrees on their magnetic actuators.

For ten terrifying minutes, the ship shook with harmonic resonance. But slowly, millimeter by millimeter, the wild tumbling decayed. The rotation rate dropped from eighteen RPM to twelve, then five, then one.

With a final, smooth whisper of magnetic torque, *Argonaut* locked its nosecone onto the distant, glowing crescent of the Moon.

"Attitude stabilized," Marcus breathed, slumping in his harness. "Yaw drift: zero point zero zero two degrees per second. Propellant margin remaining: fourteen percent."

"Look at the range clock, Marcus," Ryan said quietly.

On the forward display, the radar rangefinder woke up.

A tiny, flickering target appeared eighty-four thousand kilometers ahead, hurtling toward the lunar horizon.

It was *Prometheus*.
"""

ch7_expanded = r"""# CHAPTER SEVEN
## The Coast-Lock Bug
### The Frozen Ship

Inside the flight deck of Artemis-7, forty thousand kilometers above the cratered basalt of the Moon, the only sound was the shallow, labored breathing of three freezing human beings.

The cabin temperature was three degrees Celsius. Frost covered the aluminum bulkheads, forming delicate, branching fern-patterns across the dead digital instrument panels. To conserve their dying lithium-hydroxide canisters, Commander Elena Rostova had ordered the crew into half-rations of oxygen.

Beside her, Dr. Aris Thorne—Marcus's brother, the mission's lead astrobiologist—blew on his numb fingers, his breath freezing instantly in the cabin air. In the jump seat behind them, geologist Chen Wei was shivering violently under an aluminized Mylar survival blanket.

"Perilune altitude: two hundred and fourteen kilometers," Elena announced, her voice flat, clinical, and completely stripped of hope. "Velocity: two thousand three hundred and forty meters per second. Time to terrain impact on the farside: six hours, twelve minutes."

On the primary commander's display, the central flight computer was mocking them with a single, unyielding line of amber text:

```
================================================================
CRITICAL FAULT: STATE COVARIANCE NON-CONVERGENCE
GEONS EKF DIAGNOSTIC: INNOVATION VECTOR REJECTED (NIS = -0.412)
SOFTWARE INTERLOCK ENGAGED: BIPROPELLANT VALVES ISOLATED
CURRENT MODE: PROTECTIVE_SCREENED_COAST
MANUAL OVERRIDE: DENIED // FLIGHT SAFETY VIOLATION
================================================================
```

"It's a digital straitjacket," Aris whispered, his teeth chattering. "We have twelve hundred kilograms of storable aerozine-50 and nitrogen tetroxide in the service module tanks. We have a five-thousand-pound-thrust AJ10 engine that works perfectly. And this goddamn computer won't let us push the button because it doesn't like its own covariance matrix."

"It's the architecture, Aris," Elena said, her eyes locked on the amber text. "The aerospace contractors built the system on fifty-year-old assumptions. They assumed space is a sterile Cartesian grid. They wrote the code so that if the mathematical model ever diverges from sensor input, the safest thing to do is coast. In Low Earth Orbit, that makes sense—if your filter fails in LEO, you stay in orbit until ground control fixes it. But in a lunar capture corridor, coasting isn't safe. Coasting is suicide."

She grabbed a heavy steel wrench from the emergency tool kit, unbolted the access panel beneath the central avionics pedestal, and pulled out the primary thruster firing relays.

A tangled nest of braided Kapton wiring bundles spilled out into the dim cabin light.

"What are you doing, Elena?" Chen asked weakly from the jump seat.

"I am going to hardwire the master engine firing circuit directly to the cabin battery bus," Elena said, stripping the insulation off a twenty-gauge red wire with her teeth. "If the software won't open the fuel valves, I'll jump the solenoid coils with twenty-eight volts of direct current."

"You can't do that!" Aris warned, leaning over her shoulder. "The bipropellant valves aren't simple mechanical switches! They are dual-stage pulsed torque motors! If you apply continuous DC voltage, you'll burn out the actuator coils in two hundred milliseconds! The fuel valve will stick open, the oxidizer valve will slam shut, and when the hypergolic propellants mix unevenly in the injector head, the combustion chamber will detonate like an artillery shell!"

Elena stopped. Her hand hovered over the copper wire, her fingers trembling with cold and exhaustion.

She knew Aris was right. The AJ10 engine was a finely tuned machine; it required precise microsecond pulse sequences to open the injector gates without hydraulic water-hammer. Hot-wiring it with raw battery voltage was a coin toss between an instant explosion and a runaway burn that would rip the service module off the command capsule.

She let the wire drop.

"Then that's it," Chen whispered from the shadows. "Six hours. Then we become part of the Aitken basin."

Elena looked through the forward quartz window.

The Moon was filling the entire universe. It was no longer a gentle, luminous orb seen from a terrestrial backyard. It was a monstrous, jagged wall of gray devastation, scarred by billions of years of impact craters, towering mountains, and bottomless shadows. The farside had no smooth, dark maria. It was an unyielding shield of broken anorthosite rock rushing toward them at supersonic speed.

And then, in the pitch-black void above the lunar horizon, Elena saw something impossible.

A tiny, needle-sharp point of brilliant green-white light was pulsing in the dark.

It was not a star. It did not twinkle. It flashed in a precise, rhythmic cadence:

*Dot. Dash. Dot. Dot. Dot.*

Elena's heart seized in her chest. She lunged forward, pressing her forehead against the freezing quartz.

"Aris!" she cried, her voice cracking with raw adrenaline. "Look at the horizon! Bearing two-four-seven relative! Do you see that light?!"

Aris stared through the window. "What is it? A star tracker reflection?"

"No," Elena breathed, tears cutting clean paths through the frost on her cheeks. "That's an optical carrier. Fifty hertz pulse modulation. It's a fifteen-fifty nanometer infrared communications laser!"

She slammed her hand down on the auxiliary optical receiver switch.

Through the dead cabin intercom, a burst of crystal-clear audio broke through the silence, cutting through the frost, the cold, and the despair:

*"Prometheus, this is Argonaut. Elena, step away from the wiring harness. We have you in our sights."*
"""

ch8_expanded = r"""# CHAPTER EIGHT
## The Relational Uplink
### The 1550-Nanometer Handshake

Three thousand kilometers out from the lunar limb, *Argonaut* was closing on the tumbling *Prometheus* at six hundred meters per second.

Inside *Argonaut*’s cockpit, Ryan Vance was flying with both hands on the manual laser tracking verniers. On his central optics display, the magnified image of the Artemis transport filled the screen. She was tumbling along her yaw axis at four degrees per second, her solar panels glinting in the harsh, unshielded sunlight of the lunar horizon.

"Optical laser lock acquired!" Marcus called out, monitoring the tracking gimbals. "Beam divergence: twelve microradians. Return signal strength: ninety-four percent! We have hard carrier on their optical retro-reflector!"

"Elena," Ryan spoke into the laser audio loop, his voice transmitting down the coherent beam of infrared photons at the speed of light. "Can you hear me?"

*"Ryan!"* Elena's voice erupted through the cabin speakers, breathless and fierce. *"We have your carrier! The optical transceiver on our forward docking cone is locked! But our main computer is completely unresponsive! It's rejecting all S-band ground commands, and the flight safety interlock has frozen the thruster bus!"*

"I know," Ryan said. "Your GEONS filter accepted a negative NIS because your covariance matrix wasn't factored as a square-root. Your software thinks the variance of the universe is less than zero. I am going to reflash your GNC executive over the laser link."

*"You can't reflash the main core while the ship is in coast-lock!"* Elena warned. *"The RAD750 memory protection register is hardware-locked! It won't accept an executable binary from an external port!"*

"I'm not reflashing the RAD750," Ryan said, smiling faintly beneath his visor. "I'm going to bypass it entirely. Your spacecraft has an auxiliary FPGA payload processor in the service module—the technology demonstration board NASA installed to test autonomous optical navigation. It has direct DMA access to the engine driver relays."

*"The experimental cFE payload bus?"* Elena asked, realization flashing in her voice. *"That bus has never been certified for primary flight control!"*

"It's about to be certified," Ryan said. 

He initiated the high-speed optical data burst.

Through the fifteen-hundred-and-fifty-nanometer infrared beam, thirty megabytes of compiled machine code streamed across three thousand kilometers of vacuum in less than four seconds. It was the complete, flight-hardened **CislunarOS** stack: the 18-state Jacobi relational estimator, the square-root information filter, the diverse Cartesian verifier, and the receding-horizon QP guidance planner.

On the flight deck of *Prometheus*, the dead digital displays suddenly flickered.

A cascading waterfall of green diagnostics raced across the central commander's screen:

```
[OPTICAL-UPLINK]: PACKET STREAM RECEIVED VIA 1550 NM LASER
[INJECTION]: DIRECT MEMORY ACCESS ENGAGED // PAYLOAD BUS
[QRC-INIT]: SQUARE-ROOT MEASUREMENT GATE FACTORED (A^T = Q * r)
[COVARIANCE-RESTORE]: S_k POSITIVE DEFINITE GUARANTEED
[RAD750-OVERRIDE]: PRIMARY GNC BUS VETOED BY COMMAND RECEIPT
[MASTER-STATUS]: ALL 16 RCS CHANNELS & MAIN AJ10 ENGINE ARMED
```

"It worked!" Aris yelled on *Prometheus*, slamming his fist into the bulkhead. "The payload board just overrode the primary computer! The thruster relays are clicking shut!"

"Elena," Ryan said, his voice tightening as he checked the radar rangefinder. "You are five hundred kilometers above the farside, falling at twenty-four hundred meters per second. Your engine is armed, but your ship is still tumbling. If you fire the AJ10 right now, your thrust vector will point in the wrong direction and smash you directly into the Aitken basin."

*"Then how do we stop the tumble?"* Elena demanded. *"Our cold-gas lines are frozen!"*

"You don't stop it with cold gas," Ryan answered. "We are executing a synchronized three-body docking. *Argonaut* is matching your tumble rate. We are going to hard-dock our nosecone into your forward docking collar, lock our structural latches, and fire *Argonaut*’s Hall thrusters to stabilize the combined stack!"

Marcus stared at Ryan in horror. "Ryan, you are talking about docking two spacecraft while both vehicles are spinning in a gravity gradient eighty kilometers above the Moon!"

"Do you have a better idea, Marcus?" Ryan asked, his eyes locked on the crosshairs.

"No," Marcus said, swallowing hard. "May God have mercy on our trajectory."

"God has nothing to do with it," Ryan said, firing *Argonaut*’s thrusters into the dark. "This is pure relational mechanics."
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_05_The_Artemis_Blackout.md"), "w", encoding="utf-8") as f:
    f.write(ch5_expanded)
with open(os.path.join(MANUSCRIPT_DIR, "Chapter_06_Covariance_Starvation.md"), "w", encoding="utf-8") as f:
    f.write(ch6_expanded)
with open(os.path.join(MANUSCRIPT_DIR, "Chapter_07_The_Coast_Lock_Bug.md"), "w", encoding="utf-8") as f:
    f.write(ch7_expanded)
with open(os.path.join(MANUSCRIPT_DIR, "Chapter_08_The_Relational_Uplink.md"), "w", encoding="utf-8") as f:
    f.write(ch8_expanded)

print("Expanded Chapters 5, 6, 7, 8 successfully.")
