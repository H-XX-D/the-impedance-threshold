#!/usr/bin/env python3
"""
Deepen Chapters 7, 8, 9, 10, 11, 12 to ~2,000 - 2,300 words each.
Author: Todd Hendrixx
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

# Chapter 7
CH07 = r"""# CHAPTER SEVEN
## Dead Man's Trajectory
### The Houston Standoff

Inside the FCR-1 conference room behind the glass partition of Mission Control, the atmosphere had deteriorated into an open, venomous shouting match.

The room smelled of stale coffee, industrial floor wax, dry air from the HVAC circulation ducts, and human panic. On the whiteboard along the western wall, Marcus Thorne had drawn three crude sketches of the Earth-Moon three-body potential well in black dry-erase marker. A jagged red arrow plunged off the saddle curve of the $L_1$ Lagrange point, slicing straight into the farside lunar crust.

Around the laminate conference table sat eight people: Sarah Lin, her jaw set like quarried granite; Marcus Thorne, his uniform collar unbuttoned and eyes bloodshot from twenty-two hours on console; the Flight Dynamics officer; the Lead Flight Director for the Artemis program; and four senior contractor representatives from Boeing and Lockheed Martin, their NASA access badges dangling from branded lanyards.

"We are not uploading unverified third-party software to an active crewed spacecraft," Arthur Vance—no relation to Ryan, a senior vice president of flight systems for Lockheed—said, slamming his open palm on the table with enough force to rattle the ceramic mugs. "It violates every flight certification protocol established since Apollo 11. It breaks the software baseline freeze. If we upload unverified code and the auxiliary communications processor hangs or corrupts the internal memory bus, we lose command authority over the entire service module. We lose RCS, we lose the AJ10, we lose life support telemetry."

"You don't have command authority now, Arthur!" Marcus shot back, leaning across the table until he was inches from the executive's face. "Orion’s flight computer thinks its perilune is one hundred and eighty kilometers. Its automated burn manager will not fire the service propulsion engine because it believes the spacecraft is on a nominal free-return trajectory. In four hours and fifty minutes, that spacecraft will strike the crater Daedalus at two kilometers a second. You want to follow flight certification protocols all the way into the bedrock?"

"We execute a manual burn," Arthur insisted, his face flushed red above his stiff white collar. "We instruct the crew to take manual attitude control, point the nose to the burn vector using the optical reticle on the commander's window, and fire the AJ10 for sixty seconds under manual switch closure."

"Under what attitude?" Marcus demanded, his voice trembling with exhausted rage. "Look at the telemetry, man! The Honeywell IMU has been drifting without an external star-tracker reference for six hours. The gyro bias is sitting at zero point zero eight degrees per hour. Across six hours of coast, that’s half a degree of uncorrected attitude error. In the non-linear three-body manifold around the Moon, half a degree of burn pointing error doesn't raise perilune—it rotates the velocity vector into an even steeper dive. I ran the Monte Carlo dispersion twenty minutes ago: a manual blind burn has a sixty-two percent probability of accelerating their impact. You’d be ordering the crew to execute their own execution burn."

Sarah Lin held up a hand. The gesture was small, but the entire room fell dead silent.

"Marcus," Lin said quietly. "What is our current ground tracking status?"

"Dead," Marcus said flatly, slumping back into his leather chair. "Canberra DSN is blind. The coronal mass ejection from the X8.4 flare slammed into the Australian ionosphere two hours ago. Total electron content over the Pacific Basin is pegged off the scale. S-band and X-band radio signals are refracting by several degrees; we can't maintain phase lock on their carrier wave. Goldstone has dipped to six degrees elevation; within forty minutes, the dish will hit its mechanical elevation limit and stow. We have zero radio link to the vehicle until Madrid rises in seven hours."

"And by then?" Lin asked.

"By then, Orion is a smear of pulverized aluminum across thirty miles of lunar farside regolith."

---

### The Red Wire into FCR-1

The conference room phone beeped with a sharp, high-priority warble.

Lin reached over and hit the speaker button. "Lin here. Go."

"Sarah, this is Elena Rostova at Goddard," a voice echoed through the speaker, crisp, tight, and completely devoid of hesitation. "I am standing in the Optical Communications Directorate with Dr. Ryan Vance on secure patch. We have a solution."

Arthur Vance groaned audibly, rolling his eyes toward the ceiling. "Sarah, do not entertain this. Ryan Vance was forced out of academia for refusing to peer-review his relational models. He’s an outsider running rogue simulations on consumer hardware."

"Shut up, Arthur," Sarah Lin said without looking at him. She leaned toward the speaker. "Elena, what do you have?"

"Mount Stromlo Observatory in the Australian Capital Territory," Elena said. "They are operating the 1.8-meter telescope equipped with a 1550-nanometer infrared adaptive optics laser transceiver. Because it’s an optical system operating at near-infrared wavelengths, it is completely immune to the ionospheric electron density fluctuations that blinded Canberra's radio dishes. The skies over Mount Stromlo are photometric. They have Orion in active optical tracking lock right now."

"What is the uplink bandwidth?" Marcus asked, his pulse suddenly racing.

"Two hundred megabits per second," Elena replied. "Enough to send the entire Library of Congress in three minutes. But we don't need three minutes. Ryan Vance has compiled the autonomous integer guidance core of CislunarOS into a four-hundred-and-eighty-two-kilobyte ELF binary."

"Tell me about the code, Dr. Vance," Sarah Lin said, her eyes fixed on the speakerphone.

Through the wire, Ryan Vance’s voice was calm, measured, and shockingly direct, sounding as though he were standing in the room rather than speaking from a rain-slicked garage in the Blue Ridge Mountains.

"Flight Director," Ryan said. "The binary contains two mathematical algorithms. First, a Square Root Information Filter implemented via Householder orthogonal QR factorization. It completely bypasses covariance matrices. It parameterizes state uncertainty as an upper-triangular information matrix $\mathbf{R}$, where $\mathbf{P}^{-1} = \mathbf{R}^T \mathbf{R}$. It is mathematically impossible for $\mathbf{R}$ to lose positive-definiteness, because Householder reflections preserve the Euclidean norm to machine precision. There are no subtractions of nearly equal quantities. Second, it contains the FixedQP active-set quadratic programming solver running in thirty-two-bit integer math. It solves the non-linear three-body Lambert targeting problem in two hundred and fifty-six deterministic clock cycles."

"Can it execute on the vehicle?" Lin asked. "The RAD750 is an ancient architecture."

"It doesn't run on the RAD750," Ryan explained. "It runs on the auxiliary optical communication processor—a modern ARM-based SoC integrated into the optical transceiver module on the service module exterior. That processor has direct DMA access to the secondary CAN bus governing the auxiliary reaction control thrusters. Once uploaded, CislunarOS will take autonomous command of the four ten-pound reaction control pods, determine the true state vector using the raw OpNav camera stream, and execute a forty-nine point five meter-per-second radial correction burn before the spacecraft enters the lunar occultation zone."

"It's a suicide pact," Arthur hissed. "We are handing control of an eight-billion-dollar crewed spacecraft to a script written in a garage!"

"Arthur," Sarah Lin said, standing up and towering over the table. "Right now, your certified aerospace software is driving three astronauts into the side of a mountain at Mach five. If we do nothing, they die. If we upload this binary, they have a mathematical chance."

She looked at Marcus Thorne. "FIDO. What is your recommendation?"

Marcus didn't hesitate for a heartbeat. "Authorize the laser uplink, Flight. Let Ryan Vance fly the ship."

Sarah Lin tapped the flight director console switch, opening the wide-area net across all NASA flight centers.

"This is Flight," she announced, her voice ringing with absolute authority. "I am authorizing an emergency optical uplink to Artemis-7 via Mount Stromlo. Goddard, coordinate the laser pointing vectors. FIDO, prepare the trajectory verification scripts. We have one shot at this before the vehicle passes behind the Moon. Let's get to work."

---

### The Three-Body Trap

Outside the conference room, Marcus walked back to the Flight Dynamics console and pulled up the three-body Jacobi invariant equations on his primary workstation.

In classical Newtonian astrodynamics, a spacecraft orbits a single dominant central body: an ellipse, a parabola, or a hyperbola. The energy is conserved, the angular momentum is constant, and Kepler's elegant laws dictate the trajectory with clockwork simplicity.

In the Earth-Moon system, that clockwork dissolves into non-linear chaos.

The spacecraft moves inside the **Circular Restricted Three-Body Problem (CR3BP)**, where the Earth and the Moon rotate around their common center of mass, dragging their gravitational potentials with them. The only conserved quantity is the **Jacobi Constant**:

$$C_J = 2 \Omega(x, y, z) - (v_x^2 + v_y^2 + v_z^2)$$

where $\Omega(x, y, z)$ is the effective potential including centrifugal acceleration:

$$\Omega = \frac{1-\mu}{r_1} + \frac{\mu}{r_2} + \frac{1}{2}(x^2 + y^2)$$

For Artemis-7, falling along a high-energy translunar trajectory, the Jacobi constant was dangerously low: $C_J = 2.894$.

At that energy level, the "forbidden regions"—the geometric boundaries where the effective potential exceeds the spacecraft's energy—are wide open. The zero-velocity curves around the Earth-Moon $L_1$ and $L_2$ Lagrange points do not act as barriers; they act as funnels.

When a spacecraft approaches the Moon with an uncorrected state error, the gravitational gradient does not simply pull it into a lower orbit. The trajectory enters a chaotic, non-linear phase space governed by **invariant manifolds**: multi-dimensional tubes of phase space that either pull trajectories asymptotically toward periodic orbits or violently eject them into the cislunar void.

Artemis-7 had slipped off the stable manifold.

It was now caught on an unstable collision trajectory: an invariant tube that terminated directly upon the lunar surface. Because the gravitational pull of the lunar farside mass concentrations (mascons) was perturbing the orbital plane, every minute of delay required an exponentially greater $\Delta v$ to escape the impact corridor.

Marcus looked at the digital countdown timer glowing red in the upper corner of his display:

```
TIME TO LUNAR HORIZON OCCULTATION: 01:14:22
ESTIMATED TIME TO IMPACT:          03:42:18
MINIMUM DELTA-V TO CLEAR PERILUNE: 49.52 M/S
```

The spacecraft was plunging toward the shadow of the Moon at twenty-eight miles every minute. Once it slipped behind the lunar limb, all line-of-sight communication with Earth would be severed for forty-eight minutes.

If the burn was not executed before that horizon closed, Artemis-7 would vanish into the farside silence—and never emerge.

---

### The Last Voice from Houston

On the FCR-1 floor, the Capcom officer was desperately trying to establish a coherent voice exchange with Commander Reid Wiseman over the fading Goldstone UHF antenna.

The audio was shredded by white noise, cutting in and out like a broken radio in a storm:

"Artemis-7... Houston... do you copy... Goldstone elevation limit... two minutes..."

Wiseman's voice emerged through the hash, calm but tightly strained:

"...Houston... copy broken... rate gyros showing zero-point-one drift... lunar limb filling forward glass... confirming our automated perilune estimate... displays say one-eight-zero kilometers... why is the flight director loop calling an abort?..."

Sarah Lin stepped up to the Capcom console, plugged her headset directly into the flight loop, and overrode the channel.

"Reid, listen to me," Lin said, her tone cutting through the static with visceral clarity. "Your primary guidance computers are lying to you. The RAD750 has suffered a numerical covariance collapse. Your actual perilune is negative thirty-eight kilometers. You are on an impact trajectory with the farside highlands."

A long pause stretched across the UHF link, punctuated by the rhythmic hiss of solar static.

"...Negative thirty-eight?..." Wiseman replied, the professional composure momentarily fracturing. "...Houston, confirm negative thirty-eight? We don't have visual terrain altitude yet... OpNav shows green..."

"OpNav is starving, Reid," Lin said. "We cannot command your AJ10 through the primary bus. We are about to lose Goldstone. In four minutes, Mount Stromlo in Australia is going to initiate an optical laser uplink to your auxiliary communications terminal. They are uploading an autonomous guidance core called CislunarOS. It will take command of your auxiliary RCS thrusters and execute a forty-nine point five meter-per-second burn. You will see an auxiliary takeover prompt on your cockpit display. You must flip the override toggle. Do not wait for Houston confirmation. If you don't authorize that burn, you will hit the ground before we acquire you on the other side."

"...Copy, Houston..." Wiseman’s voice faded as the signal-to-noise ratio plunged toward zero. "...Standing by for... laser acquisition... auxiliary override... armed... see you on the other side..."

The UHF carrier flatlined.

`GOLDSTONE DSN: SIGNAL LOST (ANTENNA BELOW ELEVATION LIMIT).`

Sarah Lin pulled off her headset. FCR-1 was completely cut off from the crew. The fate of the mission had passed out of Houston’s hands entirely, crossing the Pacific to a darkened telescope dome on an Australian mountain ridge.
"""

# Chapter 8
CH08 = r"""# CHAPTER EIGHT
## Light Across the Blind Spot
### The Eucalyptus Ridge

On the summit of Mount Stromlo, seven hundred and seventy meters above the Australian capital city of Canberra, the cold night air smelled of eucalyptus resin, damp bark, and dry mountain dust.

Inside the copper-sheathed dome of the 1.8-meter optical research telescope, there were no overhead lights. The vast circular chamber was illuminated only by the pale amber glows of instrument racks, the digital readouts of cryostat temperature monitors, and the rhythmic, clicking cadence of the massive azimuth gear drive tracking across the meridian.

Outside the open dome slit, the southern sky was an ocean of diamond-hard stars: the Southern Cross tilted on its side, the dark rift of the Coal Sack Nebula standing out like an ink-stain on the luminous sweep of the Milky Way, and high in the northeast, hanging pale and brilliant over the Brindabella ranges, the gibbous Moon.

Dr. Lachlan Mackay, Senior Optical Engineer for the Australian National University, sat at the telescope control console with a heavy communication headset clamped over his thick grey hair.

"Goddard Optical Directorate, Mount Stromlo terminal is in closed-loop pointing lock," Mackay spoke into the boom mic, his Australian drawl unhurried despite the immense tension vibrating through the international voice loop. "We have the Orion optical transceiver acquired on our quad-cell quadrant tracking sensor. Target elevation is forty-one degrees. Atmospheric seeing is zero point eight arcseconds. The adaptive optics deformable mirror is active, operating at two point four kilohertz."

Beneath the primary mirror cell, in the temperature-controlled coudé room, a piezoelectric deformable mirror—a thin, flexible sheet of polished silica glass backed by ninety-seven electrostrictive ceramic actuators—was pulsing thousands of times a second. It was sensing the atmospheric turbulence in the thermal boundary layers above the Australian capital and flexing its surface to cancel the optical wavefront distortions, transforming a smeared, twinkling star image into a diffraction-limited optical point.

"Mount Stromlo, this is Elena Rostova at Goddard," Elena's voice came through the dedicated trans-Pacific fiber link with zero latency. "Telemetry confirm, Lachlan. We have the payload staged in the local memory buffer. File name: `cislunar_os_core.elf`. Size: four hundred and eighty-two kilobytes. Checksum: `0x7F4A8C91`. Are you ready to arm the high-power transmitter?"

Mackay looked at the key-switch on the laser safety interlock panel. A red tag dangled from the brass tumbler: `DANGER: CLASS 4 COVERT LASER RADIATION - EYE HAZARD AT 500 KM`.

He turned the key ninety degrees. A heavy contactor clicked behind the wall.

A bank of high-pressure liquid cooling pumps hummed to life in the basement below the dome floor.

"Laser armed," Mackay said. "Ytterbium fiber laser running at fifteen hundred and fifty nanometers. Average power output: forty watts. Beam divergence: twenty-five microradians. Goddard, you have the trigger."

"Three," Elena counted down. "Two. One. Mark. Uplink initiated."

From the secondary mirror housing of the 1.8-meter telescope, an invisible lance of infrared light cut upward into the night sky.

To the naked eye, the sky remained dark, serene, and undisturbed. But at fifteen hundred and fifty nanometers—a wavelength invisible to human retinas but perfectly matched to the quantum efficiency of InGaAs photodetectors—a blinding beacon of forty watts was climbing through the troposphere, traversing the stratosphere, and punching outward across three hundred and eighty thousand kilometers of hard vacuum toward the Moon.

---

### The Parity Check in the Void

Aboard Artemis-7, three hundred and twenty thousand kilometers from Earth, the spacecraft was drifting in absolute silence.

Inside the pressurized crew module, Commander Reid Wiseman and his two crewmates were strapped into their contour couches under dim red cabin lighting. They had felt the subtle, sickening shudder through the hull when the primary star trackers tripped out two hours earlier. Through the forward hatch window, the grey, cratered curve of the Moon was growing with terrifying speed, no longer an abstract destination but an immense, suffocating wall of dead stone filling their field of view.

Outside the pressure vessel, mounted on an articulated titanium gimbal on the service module’s exterior, the **Optical Communications Telescope Assembly (OCTA)** was staring back toward Earth.

Its four-inch aperture caught the incoming infrared photons from Mount Stromlo.

The photons focused onto a high-speed InGaAs avalanche photodiode, triggering an avalanche of secondary electrons across the semiconductor junction. The high-speed receiver circuit transformed the optical pulses into a differential digital bitstream:

```
[OCTA-RX] OPTICAL CARRIER LOCKED: 1550.12 nm
[OCTA-RX] SIGNAL-TO-NOISE RATIO: +18.4 dB
[OCTA-RX] INCOMING BITSTREAM: 100.0 Mbps
[DMA-ENGINE] INCOMING PACKET STREAM: CISLUNAR_OS_CORE.ELF
[DMA-ENGINE] WRITING TO FLASH BLOCK 0x00400000...
```

The transfer took exactly thirty-eight milliseconds.

In the auxiliary communication processor's non-volatile memory, the cyclic redundancy check evaluated the downloaded payload:

```
[CRC32] COMPUTED: 0x7F4A8C91
[CRC32] EXPECTED: 0x7F4A8C91
[CRC32] INTEGRITY VERIFIED: 100% MATCH
[EXEC] OVERRIDING GUIDANCE ARBITER...
[EXEC] CISLUNAROS INITIALIZING IN ISOLATED MEMORY PARTITION...
```

The software was alive.

Ryan Vance’s integer engine woke up in twelve milliseconds. It did not initialize a floating-point unit; it did not allocate gigabytes of dynamic heap memory. It claimed a static sixty-four kilobytes of integer scratchpad RAM.

Instantly, the **Square Root Information Filter (SRIF)** hooked into the raw video buffer of the Optical Navigation camera.

It pulled the last fifteen raw, noisy image frames that the RAD750's Extended Kalman Filter had rejected as unphysical outliers.

The SRIF did not evaluate an Extended Kalman Filter gain matrix. It did not invert a residual covariance matrix $\mathbf{S}$.

Instead, it constructed the augmented data matrix:

$$\mathbf{T} = \begin{bmatrix} \mathbf{R} & \mathbf{z} \\ \mathbf{A} & \mathbf{y} \end{bmatrix}$$

where $\mathbf{R}$ was the upper-triangular square-root information matrix of the prior state, and $\mathbf{A}$ was the measurement sensitivity matrix.

Then, with ruthless algorithmic speed, it executed a sequence of **Householder orthogonal transformations**:

$$\mathbf{H}_k = \mathbf{I} - 2 \frac{\mathbf{v}_k \mathbf{v}_k^T}{\mathbf{v}_k^T \mathbf{v}_k}$$

The Householder matrices reflected the noisy observation vectors onto the orthogonal subspace, sweeping the below-diagonal elements of the augmented matrix to absolute zero.

Because orthogonal transformations preserve the Euclidean vector norm:

$$\|\mathbf{H}_k \mathbf{x}\| = \|\mathbf{x}\|$$

the algorithm was fundamentally immune to numerical roundoff instability. There were no subtractions of nearly equal numbers. There were no matrix inversions. The condition number of the information matrix was exactly the square root of the condition number of the old covariance matrix:

$$\kappa(\mathbf{R}) = \sqrt{\kappa(\mathbf{P}^{-1})} = \sqrt{10^8} = 10^4$$

A perfectly stable, well-conditioned matrix.

In three iterations of the Householder loop, the true physical state of Artemis-7 crystallized in the processor registers:

```
[SRIF-SOLVE] STATE VECTOR CONVERGED IN 3 ITERATIONS (8.4 MS)
[SRIF-SOLVE] ESTIMATED ALTITUDE: 184.2 KM (RAD750 REPORTED: 312.0 KM)
[SRIF-SOLVE] RADIAL VELOCITY:    -1842.14 M/S
[SRIF-SOLVE] ESTIMATED PERILUNE: -38.48 KM (IMPACT PREDICTED)
[SRIF-SOLVE] IMPACT SITE:        LUNAR FARSIDE (DAEDALUS CRATER RIM)
[SRIF-SOLVE] TIME TO IMPACT:     03:38:12
```

The machine saw the abyss.

---

### Forty-Nine Point Five Two

Inside the auxiliary processor, the **FixedQP** integer quadratic programming solver engaged.

The problem was clear: compute the minimum-fuel burn vector $\Delta \mathbf{v}$ using the four auxiliary reaction control quads to raise the perilune altitude from negative thirty-eight kilometers to a safe, stable flyby corridor of one hundred and ten kilometers, subject to the thruster duty-cycle limits and remaining propellant mass.

The solver iterated through its active-set algorithm using thirty-two-bit integer math:

```
[FIXED-QP] ITERATION 01: RESIDUAL = 412.0 M/S
[FIXED-QP] ITERATION 04: RESIDUAL = 84.1 M/S
[FIXED-QP] ITERATION 09: RESIDUAL = 2.4 M/S
[FIXED-QP] CONVERGED AT ITERATION 12 (0.84 MS)
[BURN-TARGET] OPTIMAL DELTA-V: 49.52 M/S
[BURN-TARGET] ATTITUDE TARGET: PITCH +14.2 DEG, YAW -08.6 DEG
[BURN-TARGET] BURN DURATION:   27.8 SECONDS
[BURN-TARGET] T-MINUS TO IGNITION: 00:04:18
```

Aboard the spacecraft, an amber warning light flashed on the commander’s center console display:

`AUX-GNC: TAKEOVER REQUEST. CONFIRM OVERRIDE?`

Reid Wiseman looked at the digital prompt. Outside his window, the grey craters of the farside limb were rushing upward.

Wiseman reached out his gloved finger and flipped the guarded toggle switch on the center pedestal:

`GNC OVERRIDE: ENABLED.`

Outside the hull, four cold-gas thrusters fired with sharp, staccato chuffs, venting pulses of nitrogen into the vacuum. The twenty-six-ton spacecraft swung its nose smoothly across the stars, pitching fourteen degrees above the horizon until its auxiliary bipropellant thrusters aligned with the vector computed by the integer solver.

Then came the burn.

The four auxiliary thrusters ignited in a silent, pulsing blossom of pale hypergolic flame.

Inside the cabin, the crew was pushed forward into their restraint harnesses under zero point two gravities of acceleration. Across the cabin floor, loose dust specks and an unclipped stylus floated backward against the bulkhead.

Twenty-seven point eight seconds.

The thrusters cut off with a solid, hydraulic thunk.

The spacecraft was now coasting.

Two minutes later, the brilliant white disc of Earth slipped beneath the jagged black silhouette of the lunar limb. The radio telemetry flatlined to absolute static.

Artemis-7 was in the dark.

---

### The Farside Emergence

In FCR-1, forty-eight minutes passed in complete, agonizing silence.

No one spoke. No one went to the restroom. Sarah Lin stood behind the Flight Director’s console with her hands resting on the stainless steel rail, staring at the empty carrier signal monitor.

Marcus Thorne sat with his arms crossed, his eyes fixed on the acquisition clock:

```
AOS PREDICT: 18:42:15 UTC
ELAPSED TIME SINCE LOS: 00:47:58
```

If the burn had failed—if the integer guidance core had hung, or if the delta-v had been misdirected—the spacecraft was dead on the farside regolith, and the acquisition clock would tick upward into infinity without a response.

"Madrid station is online," the Ground Control officer whispered. "Pointing at the lunar limb."

The clock hit `18:42:15`.

Nothing.

`18:42:20`.

The carrier wave display was a flat line of white thermal noise.

`18:42:28`.

Suddenly, a sharp, clean green spike erupted from the noise floor on Channel 1-Alpha.

The telemetry stream burst across the room:

```
[MADRID-DSN] CARRIER LOCK ACQUIRED!
[MADRID-DSN] TELEMETRY STREAM NOMINAL!
[MADRID-DSN] SIGNAL STRENGTH: -112 dBm
```

A second later, Reid Wiseman's voice exploded through the flight loop, crackling with static but clear as a bell:

*"Houston, Artemis-7. We are through the shadow. We cleared the farside terrain at one hundred and twelve point four kilometers. Say again: perilune altitude is one hundred and twelve point four. The ship is intact. We are coming home."*

The Flight Control Room erupted.

Flight controllers leaped from their chairs, throwing headsets onto consoles, cheering, weeping, and slamming their palms onto workspace dividers. Arthur Vance sat alone at the edge of the conference room, staring blankly at the floor.

Marcus Thorne let out a long, ragged breath that sounded like a sob. He leaned forward, rested his forehead against the cool glass of his monitor, and closed his eyes.

On his console, the telemetry stream displayed the signature of the software that had flown the ship through the dark:

`GNC-CORE: CISLUNAROS REV 6.1 // AUTHOR: DR. RYAN VANCE // INTEG-SRIF`

Marcus reached over to his private phone, dialed the Blacksburg garage, and whispered into the receiver:

"Ryan. You did it. You just saved three lives with seven watts."
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_07_Dead_Mans_Trajectory.md"), "w", encoding="utf-8") as f:
    f.write(CH07.strip() + "\n")
print(f"Deepened Chapter_07_Dead_Mans_Trajectory.md: {len(CH07.split())} words")

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_08_Light_Across_the_Blind_Spot.md"), "w", encoding="utf-8") as f:
    f.write(CH08.strip() + "\n")
print(f"Deepened Chapter_08_Light_Across_the_Blind_Spot.md: {len(CH08.split())} words")
