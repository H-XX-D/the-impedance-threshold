import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

ch9 = r"""# CHAPTER NINE
## Project ARGONAUT
### The Farside Intercept

The range counter on *Argonaut*’s head-up display was winding down in steady, rhythmic decrements:

`RANGE_TO_PROMETHEUS: 84.2 KM`  
`CLOSING_VELOCITY: 182.4 M/S`  
`TIME_TO_PERILUNE: 21 MIN 40 SEC`  
`ALTITUDE_ABOVE_TERRAIN: 112.4 KM`  

Through the forward quartz vision block, the Moon filled the lower hemisphere. 

It was the farside: a desolation of overlapping crater rims, frozen impact melts, and jagged central peaks untouched by lava flows. Below them, the massive basin of Hertzsprung slid past at two point four kilometers per second, its floor fractured by ancient tectonic rifts.

Two kilometers ahead, tumbling against the starfield, was *Prometheus*.

The Artemis vehicle was rotating along its minor axis, its four 15-meter solar array wings sweeping through the vacuum like an off-balance windmill. Every three point two seconds, the white ceramic thermal tiles of the command module flashed in the sunlight before plunging back into shadow.

"Relative closing rate is nominal," Marcus Thorne said, his hands light on the rotational hand controllers. "I have visual on their forward docking port. But look at that roll rate. Eighteen revolutions per minute. If we make contact while she's rolling like that, their docking petals will shear our forward collar clean off."

"We match their angular momentum vector," Ryan Vance said from the right couch. He had tied *Argonaut*’s attitude control loop directly into the ArgonautOS Jacobi state estimator. "The Montgomery shape-sphere solver has their spin axis mapped. Engaging synchronized roll."

### The Docking Mate

*Argonaut*’s forward and aft hydrazine reaction control quads pulsed in short, sharp bursts: *pst-pst-pst-pst*.

The cockpit began to rotate. To Ryan, the cratered horizon of the Moon became a spinning gray blur, while the tumbling hull of *Prometheus* slowed, stabilized, and locked into a motionless orientation directly in front of their nosecone.

They were spinning in unison, two spacecraft locked in a synchronized roll at eighteen revolutions per minute, hurtling through the lunar gravity gradient a hundred kilometers above the farside.

"Range twenty meters," Marcus called out, his eyes fixed on the optical alignment crosshairs. "Closing at zero point two meters per second. Capture latches armed."

Inside the cabin of *Prometheus*, Elena Rostova watched through the docking camera monitor.

"Capture in five seconds," Elena said over the laser voice loop. "Aris, Chen, brace for docking shock."

*CLANG-THUMP.*

The mechanical shock rippled through the hull. Three spring-loaded titanium capture latches on *Argonaut*’s probe snapped over the passive capture ring of *Prometheus*. 

Immediately, the structural docking collar engaged its twelve motorized locking dogs. The high-torque electric actuators whined softly in the vacuum, driving the steel pins home with eight thousand pounds of clamping force.

`DOCKING_STATUS: HARD_MATE_CONFIRMED`  
`PRESSURE_INTEGRITY: SEALED`  
`COMBINED_MASS: 48,210 KG`  
`MOMENTUM_DAMPING: ACTIVE`  

*Argonaut*’s high-thrust hydrazine thrusters fired in counter-rotation, fighting the combined forty-eight-ton mass of the two coupled spacecraft. Slowly, smoothly, the rotation decayed: twelve RPM... six RPM... two RPM... zero.

The stars stopped spinning. The Moon settled back into a flat, silent plane gliding below their keel.

### The Vestibule

Ryan floated out of his harness, pulled himself into *Argonaut*’s forward docking vestibule, and opened the manual pressure equalization valve. Air hissed into the collar, balancing the cabin atmospheres.

He rotated the heavy aluminum hatch wheel and pulled the hatch open.

Standing on the other side of the tunnel, illuminated by the amber emergency lights of *Prometheus*, was Elena Rostova. Her face was smudged with carbon, her dark hair tangled and damp with sweat, but her eyes were razor-sharp.

"You took your time, Vance," Elena said with a dry, tired smile.

"We had to take the scenic route through Ohio," Ryan replied, reaching out to grasp her gloved hand.

Behind Elena, Aris Thorne pulled herself up into the hatchway. She froze, looking past Ryan into the cockpit of *Argonaut*.

Sitting in the command couch, unlatching his helmet, was Marcus Thorne.

"Dad?" Aris said softly, her voice catching in the cold air.

Marcus turned his head, his weathered, lined face softening. "Hey, kiddo. Heard you were having some navigation trouble."

Aris floated through the hatch, burying her face into her father's shoulder. Marcus wrapped his heavy arms around his daughter, holding her tight against the hum of the avionics racks.

### The Slagged Harness

Elena pulled Ryan toward the aft service module access hatch.

"The reunion will have to wait," Elena said, pointing at the engineering status terminal. "Look at the clock. We have nineteen minutes until perilune."

`PROPULSION_STATUS: AJ10_SOLENOID_RELAY_DEAD`  
`CIRCUIT_RESISTANCE: OPEN_LOOP`  
`VALVE_POSITION: SPRING_HELD_CLOSED`  
`ALTITUDE_TO_SURFACE: 74.2 KM (DESCENDING @ 840 M/S)`  

"The primary and secondary solid-state relays in the engine skirt are fused," Elena said. "The fuel and oxidizer valves are held shut by mechanical return springs. Unless we can feed twenty-eight volts at twelve amps directly into the torque-motor coils in the next twelve minutes, the engine will never ignite."

Ryan unzipped his tool harness and pulled out the gold-plated aluminum module: the **Gallium-Nitride (GaN) Power Switching Module**.

"This switch can handle two hundred amps at two hundred kilohertz," Ryan said. "It has its own isolated gate driver and an independent optocoupled trigger line."

"Where does it go?" Elena asked.

"It doesn't go in the cabin," Ryan answered, pulling his helmet from the stowage net. "It has to be spliced directly into the wiring harness on the engine gimbal block. In the engine skirt. Outside."

Elena stared at him. "Ryan, we are descending into the lunar shadow. Outside, the temperature is minus one hundred and sixty degrees Celsius. You have fifteen minutes before we hit the perilune burn window."

"Then I'd better get to work," Ryan said.
"""

ch10 = r"""# CHAPTER TEN
## The Canister Dilemma
### Lunar Shadow

The darkness that swallowed *Argonaut* and *Prometheus* as they crossed the lunar terminator was absolute.

As the coupled stack swept behind the western limb of the Moon, the blazing crescent of the Sun was eclipsed by the jagged rim of the crater Daedalus. The sunlight died instantly, replaced by a deep, freezing vacuum where the ambient temperature dropped to two point seven Kelvin.

Ryan Vance pushed himself out through *Argonaut*’s auxiliary equipment airlock into the void.

He was tethered by a twelve-foot braided steel cable to the docking collar. In his right hand, he carried a Cordura tool roll containing wire strippers, high-leverage crimpers, Kapton insulating tape, and the gold-plated GaN switching module. In his left hand, he held a high-intensity LED inspection wand.

"Comms check, Elena," Ryan said into his helmet microphone.

*"Comms nominal, Ryan,"* Elena's voice replied in his earphones. *"You are on the exterior truss, moving aft along the service module hull. Perilune burn window opens in eleven minutes."*

The lunar surface below was illuminated only by the faint, ghostly blue glow of Earthshine reflecting off the high crater peaks. They were falling toward the surface at two point six kilometers per second.

`OXYGEN_RESERVE: 14 MIN 30 SEC`  
`ALTITUDE: 48.2 KM`  
`TIME_TO_IGNITION: 10 MIN 12 SEC`  

"Moving into the engine skirt," Ryan reported.

### The Engine Skirt

He pulled himself hand-over-hand along the titanium structural rails of the service module, swinging his legs around the flared lip of the spacecraft's aft heat shield.

Before him loomed the bell of the **AJ10-190** rocket engine—a three-meter nozzle of niobium alloy coated with discolored titanium silicate. Above the nozzle was the gimbal assembly: a dense cluster of high-pressure braided stainless-steel propellant lines, hydraulic actuators, and electrical wire bundles wrapped in gold thermal foil.

The cold was penetrating his pressurized gloves. His fingertips were losing sensation, the silicone stiffening in the minus one hundred and sixty-degree vacuum.

"I have visual on the engine junction box," Ryan gasped, his breath misting on the inside of his visor. "Opening the access plate."

He used a magnetic screwdriver to back out four quarter-turn Dzus fasteners. The carbon-composite cover popped off, floating on its safety lanyard.

Inside, the sight was grim.

The high-voltage surge from the solar storm had turned the primary solenoid distribution board into a blackened mass of charred fiberglass and melted solder. Two heavy copper bus bars were welded together in a short-circuit bridge.

"Elena, the board is completely slagged," Ryan called out. "I have to sever the primary harness and bypass the entire distribution block."

*"Cut the red and yellow twisted pairs,"* Elena instructed from the cockpit. *"Those are lines `SOL_A_PWR` and `SOL_B_PWR`. They feed directly into the torque-motor coils on the bipropellant ball valves."*

"Copy. Cutting lines."

Ryan extracted the heavy wire strippers from his pouch. Pressing his boots against the engine gimbal ring for leverage, he clamped the steel jaws around the heavy 12-gauge Teflon-jacketed wire. 

He squeezed with both hands. The cold-stiffened copper sheared with a sharp metallic snap that vibrated through his gloves.

`OXYGEN_RESERVE: 09 MIN 15 SEC`  
`TIME_TO_IGNITION: 06 MIN 48 SEC`  

### The Splice

"Wires severed," Ryan reported, his heart hammering against his ribs. "Stripping the insulation."

He worked with careful, measured precision. Stripping two inches of silver-plated copper wire. Inserting the bare conductors into the gold-plated screw terminals of the GaN switching module. Tightening the set screws with a calibrated torque driver.

*Click. Click. Click.*

"GaN module spliced into the primary valve circuit," Ryan said, wiping sweat from his forehead with the foam nose-scratcher inside his helmet. "Now connecting the optocoupled trigger line to *Argonaut*’s auxiliary umbilical."

He ran a thin, high-voltage shielded coax cable from the GaN module's gate driver around the engine skirt, plugging it into the exterior SpaceWire auxiliary port on *Argonaut*’s forward boom.

"Elena, trigger line is connected," Ryan gasped. "Send the test pulse from ArgonautOS."

Inside the cockpit of *Prometheus*, Elena touched the diagnostic command:

`CMD: SEND_TEST_PULSE_VALVE_SOLENOID`  
`PULSE_WIDTH: 50 MS`  
`CURRENT_TARGET: 12.0 A`  

Outside in the dark, beneath the bell of the AJ10 engine, two heavy metallic thuds echoed through Ryan's boots:

*CLACK-CLACK.*

The mechanical valve poppets had slammed open and shut in vacuum.

`DIAGNOSTIC_RETURN: BIPROPELLANT_SOLENOID_CONTINUITY_100%`  
`VALVE_RESPONSE_TIME: 1.2 MS`  
`ENGINE_STATUS: ARMED_AND_READY`  

*"Continuity confirmed!"* Elena called out over the radio. *"The valves are responding! Ryan, get back inside! You have four minutes until ignition!"*

### The Ingress

Ryan clipped his tool roll to his harness D-ring and scrambled out from beneath the engine skirt.

His oxygen telemetry was blinking yellow:

`OXYGEN_RESERVE: 03 MIN 45 SEC`  
`SUIT_PRESSURE: 28.4 KPA (NOMINAL)`  

He pulled himself along the guide rails, his muscles aching with fatigue, his pressurized gloves gripping the cold titanium handholds. Below him, the jagged crater rims of the lunar farside were rushing past at eye-watering speed.

He reached *Argonaut*’s auxiliary airlock, vaulted through the outer portal, and hauled the heavy hatch shut. He spun the manual locking dogs until they engaged, then hit the rapid repressurization valve.

Nitrogen and oxygen flooded into the chamber with a loud roar.

The inner hatch swung open. Marcus reached in, grabbed Ryan by his suit collar, and hauled him onto the cockpit floorboards.

"Hatch sealed! Cabin pressure nominal!" Marcus called out, slamming the inner door. "Ignition in thirty seconds!"

Ryan pulled off his helmet, breathing in the warm cabin air, his hair soaked with sweat, his fingers trembling with exhaustion.

Marcus helped Ryan into the right command couch, buckling the restraint harness across his chest.

On the central flight console, the countdown reached ten seconds:

`00:10... GIMBAL_SLEW_TO_BURN_VECTOR`  
`00:05... UMBILICAL_ARMED`  
`00:03... GaN_GATE_DRIVE_ACTIVE`  
`00:02... IGNITION_SEQUENCE_START`  
`00:01...`  
`00:00... IGNITION!`  
"""

ch11 = r"""# CHAPTER ELEVEN
## The August 2033 Launch
### The Antoniadi Inversion

The AJ10 engine lit with a sharp, concussive hammer blow that slammed Ryan Vance, Marcus Thorne, Elena Rostova, Aris, and Chen Wei deep into their couch cushions with three gravities of unyielding physical force.

In the vacuum of space, twenty-seven kilonewtons of thrust erupted from the niobium engine bell. Hypergolic propellant—aerozine-50 and nitrogen tetroxide—ignited on contact inside the combustion chamber, blasting orange exhaust gases through the nozzle at three thousand one hundred meters per second.

Through the forward vision blocks, the lunar terrain below was rushing past at terrifying speed.

They were eighteen kilometers above the central peak of **Antoniadi crater**—a massive, two-hundred-kilometer impact basin in the southern farside highlands. The central uplift of the crater rose six kilometers into the black sky like a titanium fang, its terraces illuminated by the orange flare of the rocket exhaust.

`DELTA_V_DELIVERED: 412 M/S`  
`TARGET_DELTA_V: 842.6 M/S`  
`BURN_TIME_REMAINING: 46 SEC`  
`ACCELERATION: 3.12 G`  
`GUIDANCE_MODE: QRC_MONTGOMERY_SHAPE_CLOSED_LOOP`  

"Look at the shape-sphere trajectory," Elena called out over the heavy roar of the engine. Her voice was strained, compressed by the G-load on her chest.

On the navigation terminal, the green crosshairs were locked onto the optimal geodesic curve. The square-root information filter was processing thirty optical range measurements every second, continuously recalculating the three-body gravitational interactions between Earth, Moon, and the coupled spacecraft stack.

"Gimbal actuators tracking nominal," Marcus reported from *Argonaut*’s helm. "The GaN power switch is holding fifty amps without thermal drift. Engine chamber pressure is rock steady at one hundred atmospheres."

"Perilune altitude holding at eighteen point four kilometers," Ryan called out, his eyes fixed on the radar altimeter. "Skimming the crater rim. Ten seconds to cutoff."

`00:03`  
`00:02`  
`00:01`  
`00:00... ENGINE_CUTOFF!`  

The thrust died instantly.

The sudden transition from three gravities to weightlessness hurled their bodies forward against their restraint straps. Dust particles and loose washers floated gracefully through the cabin air.

Outside, the silence of the deep cosmos returned.

On the primary navigation display, the red hyperbolic escape trajectory snapped into a closed, stable cyan ellipse:

`ORBITAL_INSERTION: COMPLETE`  
`ORBIT_TYPE: NEAR_RECTILINEAR_HALO_ORBIT (NRHO)`  
`PERILUNE_ALTITUDE: 1,840 KM`  
`APOLUNE_ALTITUDE: 71,200 KM`  
`ORBITAL_PERIOD: 6.56 DAYS`  
`GATEWAY_RENDEZVOUS_WINDOW: OPEN (+40 HOURS)`  

In the cockpit of *Prometheus*, Chen Wei let out a ragged breath, leaning back against his headrest. Aris Thorne gripped Elena's arm, laughing softly through tears.

Marcus Thorne closed his eyes, his hands resting on the control sticks, letting out a long, quiet breath.

"We're in halo orbit," Marcus said.

### The Voice from Earth

Twenty minutes later, the coupled spacecraft stack swept around the eastern limb of the Moon, crossing back over the terminator.

Golden sunlight flooded through the vision blocks, illuminating the cockpit in warmth. And hanging directly above the lunar horizon, brilliant and fragile against the black void, was the Earth: a swirling marble of sapphire oceans, white clouds, and ochre continents.

Suddenly, the communications terminal erupted with high-frequency RF chatter. The Deep Space Network had re-acquired their carrier signal.

Over the primary audio loop, the voice of Flight Director Warren Hastings crackled through the speakers:

*"Prometheus, this is Houston Flight Dynamics. Prometheus, respond. We have your carrier signal on Canberra DSS-43. Telemetry is showing an anomalous orbit. Confirm status. Confirm crew survival."*

Elena Rostova unclipped her microphone. She looked at Ryan, then at Marcus, her expression calm, measured, and completely devoid of malice.

"Houston, this is *Prometheus* Actual," Elena said, her voice clear across four hundred thousand kilometers of space. "Commander Rostova speaking."

A stunned, dead silence fell over the radio loop from Johnson Space Center.

*"Elena...?"* Hastings's voice was barely a whisper. *"How are you transmitting? Your GEONS filter reported catastrophic sensor divergence. Our models showed you impacting the farside forty minutes ago."*

"Your models were wrong, Warren," Elena said with quiet, unsparing authority. "Your Cartesian filter suffered covariance collapse, just as Dr. Vance warned you three months ago. Your software locked our engine and left us to die."

*"Then... who fired the engine?"* Hastings stammered.

"We did," Elena answered. "Dr. Ryan Vance and Marcus Thorne intercepted us aboard the research vessel *Argonaut*. They hot-grafted the ArgonautOS relational guidance architecture into our avionics, bypassed your burned relays, and executed a precision three-body insertion burn using Montgomery shape-sphere coordinates."

Elena leaned into the microphone, her voice carrying the full weight of history:

"We are in a stable Near-Rectilinear Halo Orbit. All five crew members are alive and unharmed. We are docking with Lunar Gateway in forty hours. And Warren? You can tell Axiom-Lockheed that their forty-billion-dollar flight software is officially obsolete."

### The Gateway Rendezvous

Forty hours later, *Argonaut* and *Prometheus* glided into the vicinity of **Lunar Gateway**—the international orbital outpost hanging in the gravitational balance of Earth and Moon.

The station looked like a gleaming technological dragonfly: a central cylindrical habitat module flanked by massive, gold-mesh solar electric propulsion arrays, an external Canadian robotic arm, and multiple international docking ports.

The automated docking sequence, governed entirely by ArgonautOS, executed with flawless mathematical elegance. The docking mechanisms engaged without a millimeter of lateral drift.

When the interior airlock hatch opened, Station Commander Arthur Pendelton stood waiting in the Gateway vestibule, extending a hand to Ryan.

"Vance," Pendelton said. "The Administrator has been on the quantum secure link from Washington for twelve hours straight. Half the Pentagon wants to court-martial you for unauthorized launch of *Argonaut*, and the other half wants to give you the Congressional Space Medal of Honor."

"Tell them they can save their medals," Ryan said, floating into the brightly lit module. "Because the Artemis rescue was just the flight test."

Ryan walked over to the observation cupola at the forward end of the station. Outside the quartz dome, the Moon hung below them like a colossal sculpture, while the stars shone with unwavering clarity.

Elena joined him at the window, resting her hands on the handrail.

"What's next, Ryan?" Elena asked softly.

Ryan pointed past the Moon, out toward the outer solar system, where a brilliant, amber beacon was shining steadily against the background stars.

Jupiter.

"Project ARGONAUT," Ryan said. "The JWST just confirmed water vapor plumes erupting through the ice crust of Europa. The universe is waiting."
"""

ch12 = r"""# CHAPTER TWELVE
## The Haven of Callisto
### The Jovian Challenge

In the high-vacuum observation cupola of Lunar Gateway, three hundred and eighty thousand kilometers above the Earth, Dr. Ryan Vance unrolled a large architectural schematic across the magnetic plotting table.

Beside him stood Commander Elena Rostova, Marcus Thorne, and Dr. Kenji Sato, who had arrived on Gateway three days earlier aboard an automated logistics shuttle from Kennedy Space Center after the federal charges against him in Tennessee were quietly dismissed under executive pressure.

On the table glowed the mission architecture for the most ambitious interplanetary voyage ever conceived: **Project ARGONAUT**.

"Congress passed the authorization bill yesterday morning," Elena said, tracing the orbital trajectory lines on the display. "SLS Block 2 and the commercial super-heavy boosters are funded. We have the mandate to build a forty-two-ton carrier depot and a deep-space sample return mothership. Target: Europa."

"Europa is a death trap," Marcus Thorne said bluntly, leaning over the table with his arms folded across his chest. He tapped a calloused finger against the radiation contour map of the Jovian magnetosphere. "Look at the flux numbers, Elena. Jupiter's magnetic field is twenty thousand times stronger than Earth's. It traps high-energy relativistic electrons and protons from the solar wind, accelerating them into a brutal radiation belt."

Marcus pointed at Europa's orbital track.

"At Europa's orbital radius, the ionizing radiation dose is five hundred and forty rads per day," Marcus said. "A human astronaut without four feet of lead shielding will absorb a lethal dose in forty-eight hours. Even our most hardened space-qualified CMOS electronics suffer latch-up and single-event gate rupture within three weeks. You cannot stage a multi-year sample return mission from Europa orbit."

### The Radiation Haven

"We're not staging from Europa," Ryan said with a calm, confident smile. He slid his finger outward along the Jovian satellite system, past the dangerous orbits of Io and Europa, past Ganymede, stopping at the outermost Galilean moon.

"Callisto," Ryan said.

Kenji Sato adjusted his glasses, nodding in immediate agreement. "Callisto orbits at one point eight eight million kilometers from Jupiter. It sits completely outside the lethal inner radiation belts. The ambient radiation dose on Callisto is zero point zero one rads per day—hardly higher than the natural background radiation at sea level on Earth."

"Callisto is our sanctuary," Ryan continued, his eyes shining with strategic clarity. "We park the forty-two-ton ARGONAUT mothership in an equatorial orbit around Callisto. It acts as our command center, our cryogenic storage depot, and our long-range communications relay."

"And how do we get the Europa samples?" Elena asked.

"With an uncrewed, ultra-high-speed robotic skimmer," Ryan explained, tapping the secondary schematic. "A lightweight, carbon-composite dive craft equipped with twenty-eight-nanometer Fully-Depleted Silicon-on-Insulator (FD-SOI) radiation-hardened ASICs. The skimmer remains docked at Callisto in the radiation haven until our automated orbital telescopes detect an active plume eruption."

Ryan brought up a dynamic orbital animation on the primary monitor.

"When a plume erupts, the skimmer detaches from Callisto on a high-energy, one-hundred-and-twelve-hour resonant ballistic dive," Ryan said. "It plunges through the inner Jovian radiation belt, executes a single, fifty-kilometer periapse skim directly through the Europa plume at twenty-two hundred meters per second, captures the pristine ice grains in graded silica aerogel cassettes, and uses a resonant Jovian gravity assist to fling itself straight back up to Callisto."

"Total time spent inside the lethal radiation zone?" Marcus asked, his pilot's mind evaluating the risk envelope.

"Less than sixteen hours," Ryan answered. "The total integrated ionizing dose absorbed by the skimmer during the entire encounter is under four kilorads—well within the operational tolerance of our radiation-hardened electronics."

### The Shapiro Delay of the Giant

Kenji Sato leaned closer to the monitor, examining the navigation telemetry channels. "Ryan, how does the skimmer navigate the Jovian system during the dive? At that distance, radio signals take forty-three minutes to reach Earth. Ground-based control is impossible. And Jupiter's intense decametric radio emissions will swamp classical star trackers."

"We navigate using Jupiter's own update-latency well," Ryan said, turning to the whiteboard on the cupola bulkhead.

He drew Jupiter's colossal mass-energy potential, sketching the pregeometric network latency gradient:

$$\Delta t_{\text{Shapiro}} = \frac{2 G M_{\text{Jup}}}{c^3} \ln \left( \frac{4 r_1 r_2}{d^2} \right) \approx 16.4 \text{ ms}$$

"Jupiter is a thousand times more massive than Earth," Ryan said. "By the Margolus-Levitin theorem, its localized density of relational state transitions is staggering. When Europa emits decametric radio bursts as it cuts through Jupiter's magnetic flux tube, the electromagnetic wavefront passes through Jupiter's massive update-latency gradient."

"The Shapiro time delay," Kenji murmured.

"Precisely," Ryan said. "The delay is sixteen point four milliseconds. And because it is relational network latency, it is completely achromatic. By measuring the arrival times of Europa's radio emissions relative to Callisto's reference frame using our rubidium atomic clock, ArgonautOS can determine the skimmer's position within three meters—in real time, completely autonomously, with zero communication from Earth."

Elena Rostova looked at the schematic of the skimmer, then out the window at the distant, shining disk of Jupiter.

"When do we launch?" Elena asked.

"August 2033," Ryan replied. "The planetary alignment gives us an optimal Jupiter gravity assist corridor. Ten years to build the carrier, qualify the aerogel capture cassettes, and certify the automated fiber-laser sealing system."

Marcus Thorne reached across the table, laying his heavy palm over the blueprints.

"Ten years," Marcus said, a slow, determined grin spreading across his face. "Let's build the ship that rewrites the cosmos."
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_09_Project_ARGONAUT.md"), "w", encoding="utf-8") as f:
    f.write(ch9)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_10_The_Canister_Dilemma.md"), "w", encoding="utf-8") as f:
    f.write(ch10)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_11_The_August_2033_Launch.md"), "w", encoding="utf-8") as f:
    f.write(ch11)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_12_The_Haven_of_Callisto.md"), "w", encoding="utf-8") as f:
    f.write(ch12)

print("Humanized Act III (Chapters 9-12) successfully.")
