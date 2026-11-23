import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

ch9_full = r"""# CHAPTER NINE
## Project ARGONAUT
### The Lunar Intercept

The distance counter on *Argonaut*’s tactical head-up display was unwinding like the numbers on a high-speed slot machine:

`RANGE_TO_TARGET: 142.4 KM`  
`CLOSING_VELOCITY: 312.8 M/S`  
`TIME_TO_PERILUNE: 24 MIN 18 SEC`  
`ALTITUDE_ABOVE_FARSIDE: 112.6 KM`  

Through the quartz forward viewport, the Moon was no longer a celestial object. It was a suffocating, horizon-spanning wall of cratered, monochromatic death. 

They were skimming over the farside lunar highlands at two point four kilometers per second. Below them, the shadows inside the ancient impact basins—Hertzsprung, Apollo, Korolev—were pitch-black chasms, while the rim peaks caught the low-angle sunlight like broken razor blades.

Two kilometers ahead, tumbling through the void against the black starfield, was *Prometheus*.

The Artemis vehicle was rotating wildly along its minor inertial axis, its four 15-meter solar array wings whipping through the vacuum like the blades of a runaway windmill. Every three point two seconds, the silver-and-white hull flashed into the sunlight, reflecting a blinding glare before plunging back into shadow.

"Relative closing rate is nominal," Marcus Thorne called out, his hands working the dual three-axis rotational and translational hand controllers. "I have visual acquisition on their forward docking port. But look at that roll rate. Eighteen revolutions per minute. If we make contact while she's rolling like that, their docking petals will shear our forward collar clean off."

"We don't dock in flat Cartesian space, Marcus," Ryan Vance said from the right couch. He had tied *Argonaut*’s autonomous guidance loop directly into the Kintex FPGA core. "I am uploading the Montgomery shape-sphere docking solution. We match their angular momentum vector."

### The Synchronized Roll

Marcus gripped the controls, feeling the fly-by-wire system kick in through the force-feedback solenoids. "Matching their roll rate. Engaging roll thrusters."

*Argonaut*’s forward and aft hydrazine reaction control quads fired in sharp, rhythmic bursts: *ch-ch-ch-ch*.

The cockpit began to rotate. To Ryan, the Moon and the starfield suddenly became a whirling vortex, while the tumbling hull of *Prometheus* slowed, stabilized, and locked into a stationary orientation directly in front of their nosecone.

They were now spinning in perfect synchronization, two spacecraft rotating at eighteen revolutions per minute while hurtling through the lunar gravity gradient a hundred kilometers above the farside.

"Range thirty meters," Marcus called out, beads of sweat dripping from his nose inside his helmet. "Closing at zero point three meters per second. Alignment crosshairs are green. Capture latches armed."

Inside the cabin of *Prometheus*, Elena Rostova watched through the forward docking camera as the angular, matte-black nosecone of *Argonaut* closed the final ten meters.

"Capture in five seconds," Elena announced over the shared laser loop. "Aris, Chen, brace for impact!"

*CLANG-SLAM.*

The mechanical shock wave rippled through both spacecraft. Three spring-loaded titanium capture latches on *Argonaut*’s probe snapped over the passive capture ring of *Prometheus*. 

Immediately, the structural docking collar engaged its twelve motorized locking dogs. The high-torque electric motors whined in the vacuum, driving the steel pins home with eight thousand pounds of clamping force.

`DOCKING_STATUS: HARD_MATE_CONFIRMED`  
`PRESSURE_INTEGRITY: SEALED`  
`STACK_MASS: 48,210 KG`  
`COMBINED_MOMENTUM: STABILIZING`  

"Hard dock confirmed!" Marcus roared, immediately slapping the roll-damping override switch. *Argonaut*’s high-thrust hydrazine thrusters fired against the spin, fighting the combined forty-eight-ton mass of the two coupled spacecraft. 

Slowly, agonizingly, the violent rotation decayed: fourteen RPM... eight RPM... two RPM... zero.

The stars stopped spinning. The lunar surface settled into a flat, silent plane gliding serenely below their bellies.

### The Hatch Opens

Ryan unstrapped from his seat, floated out of his harness, and moved into *Argonaut*’s forward docking tunnel. He swung the manual pressure equalization valve open. Air hissed into the vestibule, balancing the pressure between the two vehicles.

He rotated the heavy aluminum hatch wheel and pulled the hatch inward.

Standing on the other side of the tunnel, illuminated by the emergency cabin lights of *Prometheus*, was Elena Rostova. Her face was pale and smudged with carbon, her flight suit damp with sweat, but her eyes were burning with fierce, unbreakable life.

"You took your time, Vance," Elena said with a shaky, breathless smile.

"Traffic on the translunar corridor was terrible," Ryan replied, reaching out to grasp her gloved hand.

Behind Elena, Aris Thorne pulled herself up into the hatchway. She froze, staring past Ryan into the cockpit of *Argonaut*.

Sitting in the left-hand command couch, unlatching his helmet, was Marcus Thorne.

"Dad?" Aris whispered, her voice trembling in the zero-gravity air.

Marcus turned his head, his hard, weathered features softening into something fragile and vulnerable. "Hey, kiddo. Heard you were having some software trouble."

Aris let out a sob that broke the cold tension of the cabin, floating across the tunnel and burying her face into her father's shoulder. Marcus wrapped his heavy flight-jacketed arms around his daughter, holding her tight against the hum of the avionics racks.

### The Burned Harness

Elena turned back to Ryan, her expression returning to razor-sharp operational focus.

"The reunion will have to wait," Elena said, pulling Ryan toward the aft service module access hatch. "Look at the telemetry clock. We have nineteen minutes until perilune."

"And the engine?" Ryan asked.

Elena pointed at the engineering status terminal:

`PROPULSION_STATUS: AJ10_SOLENOID_CIRCUIT_DEAD`  
`RESISTANCE: OPEN_LOOP`  
`VALVE_STATE: SPRING_HELD_CLOSED`  
`ALTITUDE_TO_SURFACE: 74.2 KM (DECREASING @ 840 M/S)`  

"The primary and secondary solid-state relays in the engine skirt are fused," Elena said. "The fuel and oxidizer valves are held shut by mechanical return springs. Unless we can feed twenty-eight volts at twelve amps directly into the torque-motor coils in the next twelve minutes, the engine will never ignite."

Ryan unzipped his tool harness and pulled out the gold-plated aluminum module they had salvaged from the Giles County vault: the **Gallium-Nitride (GaN) Solid-State Power Switching Stage**.

"This switch can handle two hundred amps at two hundred kilohertz," Ryan said. "It has its own isolated gate driver and an independent optocoupled trigger line."

"Where does it go?" Elena asked.

"It doesn't go in the cabin," Ryan answered, looking toward the exterior airlock. "It has to be spliced directly into the wiring harness on the engine gimbal block. In the engine skirt. Outside."

Elena stared at him. "Ryan, we are descending into the lunar shadow. Outside the spacecraft, the temperature is minus one hundred and sixty degrees Celsius. You have fifteen minutes before we hit the perilune burn window."

"Then I'd better hurry," Ryan said, grabbing his helmet.
"""

ch10_full = r"""# CHAPTER TEN
## The Canister Dilemma
### The Lunar Shadow EVA

The darkness that enveloped *Argonaut* and *Prometheus* as they crossed the lunar terminator was not the darkness of an Earth night. It was an absolute, suffocating absence of photons.

As the spacecraft swept behind the western limb of the Moon, the blazing crescent of the Sun was eclipsed by the jagged rim of the crater Daedalus. The sunlight died instantly, replaced by a deep, freezing vacuum where ambient radiation dropped to two point seven Kelvin.

Ryan Vance pushed himself out through *Argonaut*’s auxiliary equipment airlock into the void.

He was tethered by a twelve-foot braided steel cable to the docking truss. In his right hand, he carried a waterproof Cordura tool roll containing wire strippers, high-leverage crimpers, Kapton insulating tape, and the gold-plated GaN power switching module. In his left hand, he held a high-intensity LED inspection wand.

*"Ryan, comms check,"* Elena's voice spoke in his helmet earphones.

"Comms nominal, Elena," Ryan replied, his teeth chattering despite the liquid cooling garment circulating warm water against his skin. "I am on the exterior truss, moving aft along the service module hull."

The sheer scale of the lunar terrain below was terrifying. Even in the dark, the lunar surface was faintly illuminated by the pale, ghostly blue glow of Earthshine reflecting off the high crater peaks. He was falling toward the surface at two point six kilometers per second.

`OXYGEN_RESERVE: 14 MIN 30 SEC`  
`ALTITUDE: 48.2 KM`  
`TIME_TO_PERILUNE_BURN: 11 MIN 12 SEC`  

"Moving into the engine skirt," Ryan reported.

### The Belly of the Beast

He pulled himself hand-over-hand along the titanium structural rails of the service module, swinging his legs around the flared lip of the spacecraft's aft heat shield.

Before him loomed the bell of the **AJ10-190** rocket engine—a three-meter nozzle of niobium alloy coated with discolored titanium silicate. Above the nozzle was the gimbal assembly: a dense jungle of high-pressure braided stainless-steel propellant lines, hydraulic actuators, and electrical wire bundles wrapped in gold thermal foil.

The cold was penetrating his pressurized gloves. His fingertips were losing sensation, the rubberized silicone stiffening in the minus one hundred and sixty-degree vacuum.

"I have visual on the engine junction box," Ryan gasped, his breath misting on the inside of his gold-filmed visor. "Opening the access plate."

He used a magnetic screwdriver to back out four quarter-turn Dzus fasteners. The carbon-composite cover popped off, floating away on its safety lanyard.

Inside, the sight was grim.

The high-voltage EMP induced by the solar mega-flare had turned the primary solenoid distribution board into a blackened mass of charred fiberglass and melted solder. Two heavy copper bus bars were welded together in a short-circuit bridge.

"Elena, the board is completely slagged," Ryan called out. "I have to sever the primary harness and bypass the entire distribution block."

*"Cut the red and yellow twisted pairs!"* Elena instructed from the cockpit. *"Those are lines `SOL_A_PWR` and `SOL_B_PWR`. They feed directly into the torque-motor coils on the bipropellant ball valves!"*

"Copy. Cutting lines."

Ryan extracted the heavy wire strippers from his pouch. Pressing his boots against the engine gimbal ring for leverage, he clamped the steel jaws around the heavy 12-gauge Teflon-jacketed wire. 

He squeezed with both hands. The cold-stiffened copper resisted, then sheared with a sharp metallic snap that vibrated through his gloves.

`OXYGEN_RESERVE: 09 MIN 45 SEC`  
`TIME_TO_IGNITION: 07 MIN 18 SEC`  

### The Splice in the Cold

"Wires severed," Ryan reported, his heart hammering against his ribs at one hundred and forty beats per minute. "Stripping the insulation."

He worked with frantic, desperate precision. Stripping two inches of silver-plated copper wire. Inserting the bare conductors into the gold-plated screw terminals of the GaN switching module. Tightening the set screws with a calibrated torque driver.

*Click. Click. Click.*

"GaN module spliced into the primary valve circuit," Ryan said, wiping sweat from his forehead with the foam nose-scratcher inside his helmet. "Now connecting the optocoupled trigger line to *Argonaut*’s auxiliary umbilical."

He ran a thin, high-voltage shielded coax cable from the GaN module's gate driver around the engine skirt, plugging it into the exterior SpaceWire auxiliary port on *Argonaut*’s forward boom.

"Elena, trigger line is connected," Ryan gasped. "Cycle the test command from CislunarOS!"

Inside the cockpit of *Prometheus*, Elena's fingers flew across the touch interface.

`CMD: SEND_TEST_PULSE_VALVE_SOLENOID`  
`PULSE_WIDTH: 50 MS`  
`CURRENT_TARGET: 12.0 A`  

Outside in the dark, beneath the bell of the AJ10 engine, two heavy metallic thuds echoed through Ryan's boots:

*CLACK-CLACK.*

The mechanical valve poppets had slammed open and shut in vacuum.

`DIAGNOSTIC_RETURN: BIPROPELLANT_SOLENOID_CONTINUITY_100%`  
`VALVE_RESPONSE_TIME: 1.2 MS`  
`ENGINE_STATUS: ARMED_AND_READY`  

*"Continuity confirmed!"* Elena cried over the radio. *"The valves are responding! Ryan, get the hell out of there! You have four minutes until ignition!"*

### The Scramble for the Hatch

Ryan didn't need to be told twice. He threw his tools into the Cordura roll, clipped it to his D-ring, and scrambled out from beneath the engine skirt.

His oxygen telemetry was flashing yellow:

`OXYGEN_RESERVE: 04 MIN 12 SEC`  
`SUIT_PRESSURE: 28.4 KPA (NOMINAL)`  

He pulled himself along the guide rails, his muscles burning with lactic acid, his pressurized gloves slipping on the cold titanium handholds. Below him, the jagged craters of the lunar farside were rushing past with terrifying, dizzying speed.

He reached *Argonaut*’s auxiliary airlock, vaulted through the outer portal, and hauled the heavy hatch shut. He spun the manual locking dogs until they engaged, then hit the rapid repressurization valve.

Nitrogen and oxygen roared into the chamber with a deafening hiss.

The inner hatch swung open. Marcus reached in with both hands, grabbing Ryan by his suit collar and dragging him onto the cockpit floorboards.

"Hatch sealed! Cabin pressure nominal!" Marcus yelled, slamming the inner door. "Ignition in forty seconds!"

Ryan ripped off his helmet, gasping in great lungfuls of warm cabin air, his hair soaked with sweat, his fingers trembling with exhaustion.

Marcus shoved Ryan into the right command couch, slapping the restraint harness across his chest.

On the central flight console, the countdown reached ten seconds:

`00:10`  
`00:09`  
`00:08... GIMBAL_SLEW_TO_BURN_VECTOR`  
`00:05... UMBILICAL_ARMED`  
`00:03... GaN_GATE_DRIVE_ACTIVE`  
`00:02... IGNITION_SEQUENCE_START`  
`00:01...`  
`00:00... IGNITION!`  
"""

ch11_full = r"""# CHAPTER ELEVEN
## The August 2033 Launch
### The Antoniadi Inversion

The AJ10 engine did not ignite with a gentle rumble. It lit with an incandescent, violent hammer blow that slammed Ryan Vance, Marcus Thorne, Elena Rostova, Aris, and Chen Wei into their cushions with three gravities of unyielding physical force.

In the vacuum of space, twenty-seven kilonewtons of thrust erupted from the niobium engine bell. Hypergolic propellant—aerozine-50 and nitrogen tetroxide—ignited on contact inside the combustion chamber, blasting glowing orange exhaust gases through the nozzle at three thousand one hundred meters per second.

Through the forward vision blocks, the lunar terrain below was rushing past at eye-watering speed.

They were eighteen kilometers above the central peak of **Antoniadi crater**—a massive, two-hundred-kilometer-wide impact basin in the southern farside highlands. The central uplift of the crater rose six kilometers into the black sky like a jagged titanium fang, its frozen terraces illuminated by the brilliant orange fire of the rocket exhaust.

`DELTA_V_APPLIED: 412 M/S`  
`TARGET_DELTA_V: 842.6 M/S`  
`BURN_TIME_REMAINING: 48 SEC`  
`ACCELERATION: 3.12 G`  
`GUIDANCE_MODE: QRC_MONTGOMERY_SHAPE_CLOSED_LOOP`  

"Look at the shape-sphere trajectory!" Elena shouted over the roaring vibration of the engine. Her voice was strained, compressed by the heavy G-load on her chest.

On the navigation terminal, the green crosshairs were locked onto the optimal geodesic curve. The square-root information filter was processing thirty optical range measurements every second, continuously recalculating the three-body gravitational interactions between Earth, Moon, and the coupled spacecraft stack.

"Gimbal actuators tracking nominal!" Marcus reported from *Argonaut*’s helm. "The GaN power switch is holding fifty amps without thermal drift. Engine chamber pressure is rock steady at one hundred atmospheres!"

"Perilune altitude holding at eighteen point four kilometers!" Ryan called out, his eyes glued to the radar altimeter. "We are skimming the crater rim! Ten seconds to cutoff!"

`00:03`  
`00:02`  
`00:01`  
`00:00... ENGINE_CUTOFF!`  

The roaring thrust vanished instantly.

The sudden transition from three gravities to weightlessness hurled their bodies forward against their restraint straps. Dust particles and loose washers floated gracefully through the cabin air.

Outside, the silence of the deep cosmos returned.

On the primary navigation display, the red hyperbolic escape trajectory snapped into a closed, stable, glowing cyan ellipse:

`ORBITAL_INSERTION: COMPLETE`  
`ORBIT_TYPE: NEAR_RECTILINEAR_HALO_ORBIT (NRHO)`  
`PERILUNE_ALTITUDE: 1,840 KM`  
`APOLUNE_ALTITUDE: 71,200 KM`  
`ORBITAL_PERIOD: 6.56 DAYS`  
`GATEWAY_RENDEZVOUS_WINDOW: OPEN (+42 HOURS)`  

In the cockpit of *Prometheus*, Chen Wei let out a triumphant roar, throwing his checklist into the air. Aris Thorne leaned across the console, laughing through tears as she grabbed Elena's arm.

Marcus Thorne closed his eyes, his hands resting on the control sticks, letting out a long, trembling breath that sounded like a prayer.

"We did it," Marcus whispered. "We're in halo orbit."

### Re-emergence into the Light

Twenty minutes later, the coupled spacecraft stack swept around the eastern limb of the Moon, crossing back over the terminator.

Blinding, golden sunlight flooded through the vision blocks, illuminating the cockpit in radiant warmth. And hanging directly above the lunar horizon, brilliant and fragile against the velvet void, was the Earth.

A swirling jewel of sapphire oceans, white cloud spirals, and ochre continents.

Suddenly, the communications terminal erupted with high-frequency RF chatter. The Deep Space Network had re-acquired their carrier signal.

Over the primary audio loop, the frantic, panicked voice of Flight Director Warren Hastings crackled through the speakers:

*"Prometheus, this is Houston Flight Dynamics! Prometheus, respond! We have your carrier signal on Canberra DSS-43! Telemetry is showing an anomalous orbit! Confirm status! Confirm crew survival!"*

Elena Rostova unclipped her microphone. She looked at Ryan, then at Marcus, a cold, serene smile touching her lips.

"Houston, this is *Prometheus* Actual," Elena said, her voice echoing clearly across four hundred thousand kilometers of space. "Commander Rostova speaking."

A stunned, dead silence fell over the radio loop from Johnson Space Center.

*"Elena...?"* Hastings's voice was barely a whisper. *"How are you transmitting? Your GEONS filter reported catastrophic sensor divergence. Our models showed you impacting the farside forty minutes ago."*

"Your models were wrong, Warren," Elena said with icy, unsparing authority. "Your Cartesian filter suffered covariance collapse, just as Dr. Vance warned you three months ago. Your software locked our engine and left us to die."

*"Then... who fired the engine?"* Hastings stammered.

"We did," Elena answered. "Dr. Ryan Vance and Marcus Thorne intercepted us aboard the research vessel *Argonaut*. They hot-grafted the CislunarOS relational guidance architecture into our avionics, bypassed your burned relays, and executed a precision three-body insertion burn using Montgomery shape-sphere coordinates."

Elena leaned into the microphone, her voice carrying the full weight of history:

"We are in a stable Near-Rectilinear Halo Orbit. All five crew members are alive and unharmed. We are docking with Lunar Gateway in forty hours. And Warren? You can tell Axiom-Lockheed that their forty-billion-dollar flight software is officially obsolete."

### The Gateway Arrival

Forty hours later, *Argonaut* and *Prometheus* glided into the vicinity of **Lunar Gateway**—the international orbital outpost hanging in the gravitational balance of Earth and Moon.

The station looked like a gleaming technological dragonfly: a central cylindrical habitat module flanked by massive, gold-mesh solar electric propulsion arrays, an external Canadian robotic arm, and multiple international docking ports.

The automated docking sequence, governed entirely by CislunarOS, executed with flawless mathematical elegance. The docking mechanisms engaged without a millimeter of lateral drift.

When the interior airlock hatch opened, Station Commander Arthur Pendelton stood waiting in the Gateway vestibule, his arms crossed, his face a complex mixture of shock, awe, and bureaucratic anxiety.

"Vance," Pendelton said, extending a hand. "The Administrator has been on the quantum secure link from Washington for twelve hours straight. Half the Pentagon wants to court-martial you for stealing *Argonaut* out of Plum Brook, and the other half wants to give you the Congressional Space Medal of Honor."

"Tell them they can save their medals," Ryan said, floating into the spacious, brightly lit module. "Because the Artemis rescue was just the proof of concept."

Ryan walked over to the observation cupola at the forward end of the station. Outside the multi-layered quartz dome, the Moon hung below them like a colossal sculpture, while the stars shone with unwavering clarity.

Elena joined him at the window, resting her hands on the handrail.

"What's next, Ryan?" Elena asked softly.

Ryan pointed past the Moon, out toward the outer solar system, where a brilliant, amber beacon was shining steadily against the background stars.

Jupiter.

"Project ARGONAUT," Ryan said. "The JWST just confirmed water vapor plumes erupting through the ice crust of Europa. The universe is waiting."
"""

ch12_full = r"""# CHAPTER TWELVE
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

"Precisely," Ryan said. "The delay is sixteen point four milliseconds. And because it is relational network latency, it is completely achromatic. By measuring the arrival times of Europa's radio emissions relative to Callisto's reference frame using our rubidium atomic clock, CislunarOS can determine the skimmer's position within three meters—in real time, completely autonomously, with zero communication from Earth."

Elena Rostova looked at the schematic of the skimmer, then out the window at the distant, shining disk of Jupiter.

"When do we launch?" Elena asked.

"August 2033," Ryan replied. "The planetary alignment gives us an optimal Jupiter gravity assist corridor. Ten years to build the carrier, qualify the aerogel capture cassettes, and certify the automated fiber-laser sealing system."

Marcus Thorne reached across the table, laying his heavy palm over the blueprints.

"Ten years," Marcus said, a slow, determined grin spreading across his face. "Let's build the ship that rewrites the cosmos."
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_09_Project_ARGONAUT.md"), "w", encoding="utf-8") as f:
    f.write(ch9_full)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_10_The_Canister_Dilemma.md"), "w", encoding="utf-8") as f:
    f.write(ch10_full)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_11_The_August_2033_Launch.md"), "w", encoding="utf-8") as f:
    f.write(ch11_full)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_12_The_Haven_of_Callisto.md"), "w", encoding="utf-8") as f:
    f.write(ch12_full)

print("Expanded Act III (Chapters 9-12) successfully.")
