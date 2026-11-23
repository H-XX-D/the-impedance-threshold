import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

ch9_content = """# CHAPTER NINE
## Project ARGONAUT
### Perilune-110

The basalt plains of the lunar farside were rushing beneath them at twenty-two hundred meters per second.

Through the forward quartz vision block of *Argonaut*, the Moon was no longer an abstraction. It was a terrifying, jagged desert of crater rims, central peaks, and razor-sharp shadows racing past sixty miles below. If Ryan Vance looked down, he could see the terraces of Daedalus crater, its sheer stone walls dropping three miles into absolute blackness.

And directly ahead, tumbling end-over-end in the blinding glare of the low sun, was *Prometheus*.

"Range: four hundred meters," Marcus Thorne called out, his knuckles white against the auxiliary attitude hand controller. "Closure rate: three point two meters per second! Relative yaw: four point one degrees per second! Ryan, she's spinning like a top!"

"Matching roll rate," Ryan said.

He grabbed the primary rotational joystick. With his left hand, he pulsed the forward cold-gas quads.

*CHUFF. CHUFF.*

*Argonaut* rolled thirty degrees to the right, then sixty, then ninety, matching the dizzying tumble of the larger transport. The starfield and the cratered floor of the Moon spun in a nauseating, centrifugal blur outside the windows. The G-meter flickered as the angular momentum of the spin pulled at Ryan's harness.

"Three-point alignment confirmed," Ryan said, his voice dropping into the icy, hyper-focused calm of a test pilot. "Docking crosshairs locked on the drogue collar. Range: fifty meters. Closing at zero point eight."

On the audio link, Elena Rostova's voice was tense, ragged with exhaustion:

*"Argonaut, you are coming in too hot! If your capture probe hits our rim off-angle, you'll shear the docking latches! We'll bounce off each other and tumble into the Aitken basin!"*

"The latches won't shear, Elena," Ryan said, not taking his eyes off the crosshairs. "I designed the titanium capture collar. It's rated for twelve thousand pounds of shear force. Marcus, prep the hard-dock sequence."

"Latches armed!" Marcus shouted. "Ten meters! Five meters!"

The mechanical docking probe on *Argonaut*’s nosecone entered the conical aluminum drogue of *Prometheus*.

*CLANG-THUMP.*

The impact vibrated through *Argonaut*’s structural spine like the blow of a sledgehammer. The three motorized capture latches snapped shut with a high-pitched, electric whine, pulling the two spacecraft into rigid structural alignment.

```
[DOCKING STATUS]: HARD MATE CONFIRMED
STRUCTURAL CONTINUITY: 100% // CAPTURE LATCHES 1-3 SEATED
MASS OF COMBINED STACK: 38,410 KG
CURRENT ALTITUDE: 112.4 KM ABOVE LUNAR FARSIDE
TRAJECTORY: SUB-ORBITAL // TIME TO SURFACE IMPACT: 42 MINUTES
```

"We are hard-docked!" Marcus yelled.

"Firing Hall thrusters to arrest the tumble," Ryan commanded.

The twin 15-kilowatt electric engines on *Argonaut*’s tail fired in opposite magnetic quadrants. The blue plasma plumes flared against the lunar darkness. Slowly, stubbornly, the brutal rotational momentum of the thirty-eight-ton combined stack began to bleed away.

The spinning stopped. The cratered plains of the Moon locked into fixed position below them, unrolling like an endless gray scroll of death.

"Elena," Ryan spoke into the open docking tunnel intercom. "We have structural capture. The tumble is arrested. Now we fire your AJ10 engine to burn out of this collision arc."

Through the pressurized hatch, Elena's voice came back, stripped of all relief:

*"Ryan... the engine won't fire."*

Ryan froze. "What did you say?"

*"The optical bypass code reached the payload bus,"* Elena said, her voice shaking. *"The computer is ready to fire. But when the coronal flare hit our service module, the primary firing harness took a high-voltage surge. The copper relay to the engine solenoid melted inside the unpressurized service spine. The circuit is open. The computer is sending the firing pulse, but the signal is dying in a severed wire!"*

Ryan looked at the mission countdown clock.

```
TIME TO PERILUNE IMPACT: 38 MINUTES, 12 SECONDS
ALTITUDE: 94.2 KM // VELOCITY: 2,380 M/S
```

"Marcus," Ryan said, reaching down and unbuckling his five-point harness. "Get me the emergency EVA suit."
"""

ch10_content = """# CHAPTER TEN
## The Canister Dilemma
### The Hardware Graft

The vacuum of space inside the lunar shadow was minus one hundred and sixty degrees Celsius.

When Ryan Vance cracked the outer airlock hatch on *Argonaut*, the escaping air blasted into the dark like a geyser of diamond crystals. He climbed out onto the structural truss, his gloved boots magnetically clamping to the cold-rolled titanium rail.

Below him, less than fifty miles away, the lunar farside was a monstrous, freezing wall of fractured rock rushing past at supersonic speed. There was no sky. There was only the jagged, cratered floor of the Moon filling his entire lower hemisphere, and the cold, unblinking glare of the stars above.

"Ryan, you have twenty-six minutes of oxygen in that suit," Marcus Thorne called over the helmet comms from *Argonaut*’s cockpit. "And you have twenty-two minutes before the terrain altitude rises to meet us at the rim of the Aitken basin!"

"I see the service bay," Ryan panted, his breath fogging the gold-coated visor of his helmet.

He pulled himself hand-over-hand along the docking collar, crossing the structural seam into the unpressurized service module of *Prometheus*.

The service bay was an engineering nightmare. Multi-layer Mylar insulation blankets hung in shredded, carbonized ribbons, burned by the coronal proton storm. Floating in the zero-gravity void around him were frozen globules of hydraulic fluid and copper wire fragments.

Mounted in the center of the bay, flanked by two massive titanium propellant tanks, was the gimbaled combustion chamber of the AJ10 rocket engine.

Ryan pulled a high-intensity inspection light from his utility belt and clicked it on. The white LED beam illuminated the engine's primary wiring harness.

Elena had been right. The main solenoid firing relay—a rectangular aluminum box labeled `GNC-ENG-ACT-01`—was charred black. A high-voltage plasma arc had blown the side out of the casing, melting the terminal pins into a slag of scorched silicon and copper.

"Relay box is dead," Ryan reported, his pulse pounding in his ears. "Total dielectric breakdown. The internal switches are fused open."

*"Ryan, can you splice it?"* Elena's voice asked over the radio from inside the command module. *"I have the auxiliary firing bus powered from the cabin batteries!"*

"The terminal block is completely vaporized, Elena," Ryan said, examining the damage with his gloved fingers. "There is nothing to splice into. If I try to twist bare wires together in this vacuum, cold-welding will short the positive lead to the frame, and we'll blow the master cabin bus."

"Then we're dead," Marcus said over the radio.

"No," Ryan said. 

He unclipped the hardened titanium utility pouch from his chest. Inside was the spare QRC square-root avionics module—the secondary backup unit he had carried from Giles County.

"What are you doing, Ryan?" Marcus asked.

"The QRC module has an internal solid-state gallium-nitride power stage," Ryan said, his fingers working with frantic, mechanical precision. "It's designed to drive the 15-kilowatt magnetic coils on the Hall thruster. It can deliver two hundred amps of pulsed DC current without breaking a sweat."

He stripped the main twenty-eight-volt battery feeder cable using the ceramic wire cutters built into his suit gauntlet. Sparks showered into the vacuum as the copper exposed.

Working against the stiffness of his pressurized gloves, Ryan bolted the heavy battery cables directly into the input terminals of the QRC module. Then he ran the output leads straight into the injector torque-motor solenoids on the AJ10 engine bell.

He was literally grafting the experimental relational processor directly into the engine's throat.

```
SUIT TELEMETRY // HEART RATE: 164 BPM
OXYGEN MARGIN: 11 MINUTES
ALTITUDE ABOVE LUNAR SURFACE: 62.4 KM
TERRAIN CLEARANCE ALARM: PULL UP // PULL UP
```

"Hardware graft complete!" Ryan shouted, securing the module to the titanium truss with heavy stainless-steel safety wire. "Elena, I have bridged the firing circuit through the QRC power stage! The engine is hardwired to my guidance core!"

*"Ryan, get back into the airlock!"* Elena screamed. *"The terrain collision warning is sounding in the cockpit! We have to ignite in two minutes!"*

Ryan turned and scrambled across the docking ring. His magnetic boots clattered against the titanium truss as he vaulted through the hatch of *Argonaut*.

He pulled the hatch shut, dogging the latches with all his strength.

"Pressurizing airlock!" Marcus yelled, slamming the oxygen valve. "Ryan, strap in! We don't have time to get you into the cockpit!"

Ryan dropped into the airlock jump seat, snapping the single emergency chest harness over his pressurized suit.

Outside, the jagged peaks of the lunar farside rose into the darkness like the teeth of a cosmic saw.

Through his headset, Elena Rostova's voice counted down the final seconds of their lives:

*"Three... two... one... IGNITION!"*
"""

ch11_content = """# CHAPTER ELEVEN
## The August 2033 Launch
### The Inversion Burn

The roar of the AJ10 engine was not an acoustic sound. In the vacuum of space, it was a terrifying, violent vibration that tore through the docked hulls of *Argonaut* and *Prometheus* like an earthquake.

Three gravities of sudden, brutal acceleration slammed Ryan Vance into the airlock jump seat. The pressurized suit compressed against his chest, driving the air from his lungs. Outside the narrow vision block, the dark, cratered crust of the Moon was suddenly washed in the blinding, incandescent violet-white glare of hypergolic rocket exhaust.

Inside the flight deck, Elena Rostova was fighting the controls.

"Thrust: twenty-six kilonewtons continuous!" she called out over the howling vibration. "Combustion chamber pressure: nominal! But the center of mass is offset! *Argonaut* is hanging off our nosecone! The thrust vector is inducing a four-degree pitch moment!"

"The QRC guidance core is compensating!" Marcus yelled back from *Argonaut*’s cockpit.

On the central processor, the receding-horizon QP guidance algorithm was calculating fifty trajectory corrections every second. It did not use classical PID loops that lagged behind the disturbance. It solved the complete three-body equations of motion across the Jacobi manifold:

$$\\ddot{u} = -\\frac{G(m_1 + m_2)}{|u|^3} u + \\nabla_u \\Omega_{\\text{rel}}$$

By pulsing *Argonaut*’s forward cold-gas thrusters in precise, microsecond sync with the AJ10’s gimbal actuators, the QRC system balanced the thirty-eight-ton stack on a knife-edge of pure rocket thrust.

Below them, the towering central peak of Antoniadi crater rushed beneath the engine nozzle—less than eighteen kilometers beneath their glowing carbon-carbon bell. The radiation monitors on the hull spiked as the scorching heat of the lunar surface reflected off the exhaust plume.

"Altitude: twenty-four kilometers... twenty-eight... thirty-six!" Elena shouted. "We are climbing out of the gravity well! Vertical velocity has inverted! We are positive!"

For two hundred and forty agonizing seconds, the engine burned, consuming eleven hundred kilograms of aerozine-50.

And then, with a sharp, hydraulic shudder, the propellant depletion sensors tripped.

The engine shut down.

Silence—absolute, ringing, cosmic silence—slammed over the spacecraft.

Ryan let out a long, ragged gasp, his chest burning as the three-G load vanished. Floating in zero gravity inside the airlock, he wiped sweat from his eyes and looked through the viewport.

The Moon was no longer rushing toward them. It was dropping away beneath their keel, a majestic, curving sphere of silver and gray, falling toward the black abyss of the horizon.

On the navigation terminal, the trajectory projection updated in brilliant, glowing green:

```
================================================================
ORBITAL INSERTION: CONFIRMED
PERILUNE ALTITUDE: 112.4 KM // APOLUNE: 71,400 KM
INCLINATION: 84.2 DEGREES (POLAR)
ORBIT: STABLE NEAR-RECTILINEAR HALO ORBIT (NRHO)
RESONANCE: 9:2 LUNAR SYNODIC // GATEWAY CORRIDOR ACQUIRED
COLLISION RISK: ZERO POINT ZERO ZERO ZERO PERCENT
================================================================
```

The cabin speakers on *Prometheus* erupted into deafening cheers and weeping as Aris Thorne and Chen Wei embraced on the flight deck.

Elena Rostova’s face appeared on the internal video monitor. Her dark hair was floating in zero gravity, her Nomex flight suit soaked in sweat, but her eyes were shining with an intensity Ryan had never seen before.

"Ryan," she whispered, her voice trembling slightly. "You did it. You bent the three-body problem."

"We did it, Elena," Ryan said, unclipping his helmet and taking his first breath of cabin air in hours. "The relational geometry holds. The universe isn't a spreadsheet. It's an impedance network."

"Look at the ground feed from Houston," Marcus called out, a broad grin spreading across his face.

On the auxiliary monitor, the video link from Johnson Space Center had finally reconnected as *Prometheus* cleared the Moon's limb. The entire Mission Control floor was on its feet. Even Warren Hastings, his tie undone and his jacket off, was standing before the flight director's console, applauding with tears running down his face.

"Flight Director Hastings is requesting an open audio channel, Ryan," Marcus said.

Ryan reached across the console and hit the transmit toggle. "Houston, this is Vance aboard the *Argonaut-Prometheus* stack. We are in a stable Near-Rectilinear Halo Orbit. All three crew members are safe and accounted for."

Hastings's voice came over the loop, thick with emotion and unvarnished respect:

*"Dr. Vance... on behalf of the National Aeronautics and Space Administration, and the families of Artemis-7... I apologize. The flight rules were wrong. The coordinates were wrong. Your relational guidance system just saved three lives and the entire future of human spaceflight."*

"Thank you, Warren," Ryan said calmly. "Now tell the contractors to pack up their Cartesian code. We have a solar system to map."
"""

ch12_content = """# CHAPTER TWELVE
## The Haven of Callisto
### The Jovian Echo

Three days after the rescue of Artemis-7, the docked *Argonaut-Prometheus* stack was moored safely to the radial docking port of Lunar Gateway Station, four hundred thousand kilometers above the Earth.

Inside Gateway’s cupola, Ryan Vance, Elena Rostova, and Dr. Aris Thorne floated in the soft blue glow of the Earth-Moon system. Below them, the lunar South Pole was a brilliant swirl of illuminated rim-peaks and permanently shadowed craters.

On the work table before them, the QRC flight core was still plugged into Gateway’s primary science data network, continuously logging timing residuals from the deep-space pulsar array.

"Look at this data stream, Ryan," Aris Thorne said, pointing at a strange, rhythmic spike on the long-wavelength radio channel. "While you were executing the inversion burn off the farside, the X-ray drift detectors were tracking PSR J0337+1715 through the Jovian gravitational well."

Ryan leaned over the screen, his metrologist's instinct instantly sharpening. "What frequency?"

"One point four gigahertz," Aris replied. "Look at the Shapiro delay. When the pulsar signal grazed the cloud tops of Jupiter, the relational update latency spiked by sixteen point four milliseconds, exactly as your $n(r) = 1 + 2GM/c^2r$ equation predicted. But look at what is riding on top of the Shapiro curve."

He zoomed in on the residual wave.

It was not random noise. It was a coherent, periodic micro-modulation—a pulse train repeating every twenty-four hours, exactly synchronized with the orbital period of Europa.

"That's not pulsar noise," Elena said, her eyes widening. "Pulsars don't pulse on a twenty-four-hour period. That's a local planetary modulation."

"It's Europa's cryo-plumes," Aris whispered, his voice trembling with awe. "The tidal flexing from Jupiter is squeezing Europa's twenty-kilometer ice shell like a bellows. Every time Europa reaches periapse, the tensile fractures in Manannán chasma rip open. Millions of tons of hyper-velocity ocean brine are venting into the vacuum of space, ionizing in Jupiter’s magnetosphere, and creating a coherent radio modulation!"

"The ocean is venting right now," Elena breathed.

"And look at the spectral signature," Aris continued, pulling up the mass spectrometer cross-correlation from the James Webb archives. "It's not just salt water. There are heavy organic macromolecules in that spray. Complex polymers. Amino acids. Sulfur-reducing electrolytes."

He turned to Ryan and Elena, his expression burning with urgent scientific conviction.

"For seventy years, astrobiologists have argued about whether life exists in the outer solar system," Aris said. "We spent billions planning landers to drill through twenty miles of solid cryogenic ice. But we don't need to drill! The ocean is throwing itself into the sky! If we fly a probe through that plume, we can harvest the pristine living chemistry of an alien ocean and bring it back to Earth!"

"You can't send a normal spacecraft to Europa, Aris," Elena noted, her tactical discipline taking over. "Jupiter’s radiation belts around Europa deliver five hundred and forty rads of ionizing radiation every single day. Even radiation-hardened silicon dies in two weeks."

"Then you stage from Callisto," Ryan Vance said, his eyes lighting up with the architectural breakthrough.

He pulled up the orbital mechanics of the Jovian system on the holographic projector.

"Callisto sits at one point eight eight million kilometers from Jupiter," Ryan explained, drawing the resonant orbits. "It is outside the deadly radiation belts. The dose rate at Callisto is less than a tenth of a millisievert a day—lower than the International Space Station! Callisto is the radiation haven of the Jovian system!"

"A mothership at Callisto," Elena said, following his thought with razor-sharp speed. "The carrier depot anchors in Callisto halo orbit. It deploys an ultra-lightweight, autonomous kinetic skimmer. The skimmer dives deep into the Jovian gravity well, makes a single, hyper-velocity pass through the plume at fifty kilometers altitude, captures the ice grains in silica aerogel, and immediately climbs back out to Callisto!"

"And who flies the skimmer?" Aris asked.

Ryan smiled, tapping the gold-plated QRC guidance core on the table.

"The same machine that just flew us around the Moon," Ryan said. "Project ARGONAUT is going to Jupiter."
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_09_Project_ARGONAUT.md"), "w", encoding="utf-8") as f:
    f.write(ch9_content)
with open(os.path.join(MANUSCRIPT_DIR, "Chapter_10_The_Canister_Dilemma.md"), "w", encoding="utf-8") as f:
    f.write(ch10_content)
with open(os.path.join(MANUSCRIPT_DIR, "Chapter_11_The_August_2033_Launch.md"), "w", encoding="utf-8") as f:
    f.write(ch11_content)
with open(os.path.join(MANUSCRIPT_DIR, "Chapter_12_The_Haven_of_Callisto.md"), "w", encoding="utf-8") as f:
    f.write(ch12_content)

print("Wrote Chapters 9, 10, 11, 12 successfully.")
