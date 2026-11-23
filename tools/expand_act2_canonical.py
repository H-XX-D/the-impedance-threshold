#!/usr/bin/env python3
"""
Act II Literary Expansion: Chapters 6, 7, 8.
Authored by Todd Hendrixx.
Target: ~2,100 - 2,400 words per chapter.
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

CH06 = r"""# CHAPTER SIX
## The Negative Variance
### The Avionics Bay & The PowerPC Mainframe

Inside the unpressurized secondary avionics bay of the Orion service module, three BAE RAD750 flight computers were housed inside a gold-plated aluminum chassis, suspended on elastomeric vibration isolators against the titanium structural ribs.

Each computer was a celebrated marvel of aerospace radiation hardening: a 133-megahertz PowerPC 750GL architecture manufactured with radiation-tolerant silicon-on-insulator semiconductor gates, designed to withstand a total ionizing dose of one hundred thousand rads without gate oxide breakdown. In the cleanrooms of Littleton and Houston, engineers spoke of the RAD750 with theological reverence. It had flown to Mars aboard Curiosity and Perseverance; it had orbited the Moon; it had survived decades in deep-space coronal streams where commercial microprocessors died in seconds.

They were built to survive the radiation.

They were not built to survive the mathematics.

As the primary star trackers blinded under the secondary Cherenkov bombardment from the solar proton storm, the triple-redundant flight computers switched automatically to their emergency fallback navigation mode: fusing the drifting rate-integrating gyroscopes of the Honeywell Inertial Measurement Unit with intermittent optical bearing measurements to the Moon's illuminated limb, captured by the forward Optical Navigation (OpNav) camera mounted on the service module's forward bulkhead.

The OpNav camera was exposing one frame every forty seconds. Through the sunlit coronal haze, the lunar crescent was a brilliant, overexposed arc of white against the black void, its features softened and jittered by secondary photon showers hitting the CMOS sensor array.

The spacecraft’s flight software was executing its core state estimator: an Extended Kalman Filter running in standard IEEE 754 32-bit single-precision floating point.

Every forty seconds, the filter executed its classical measurement update sequence:

$$\mathbf{K}_k = \mathbf{P}_{k|k-1} \mathbf{H}_k^T \left( \mathbf{H}_k \mathbf{P}_{k|k-1} \mathbf{H}_k^T + \mathbf{R}_k \right)^{-1}$$

$$\mathbf{x}_{k|k} = \mathbf{x}_{k|k-1} + \mathbf{K}_k (\mathbf{z}_k - \mathbf{h}(\mathbf{x}_{k|k-1}))$$

where $\mathbf{z}_k$ was the optical bearing to the lunar limb, and $\mathbf{R}_k$ was the measurement noise covariance matrix.

Because of the proton storm, the optical camera's limb-centroiding algorithm was jittering violently. Secondary proton tracks traversing the silicon photodiode wells registered as false illuminated features along the lunar terminator. The perceived edge of the lunar disk danced by tens of pixels from frame to frame.

The filter's innovation residual—the physical vector difference between where the camera reported the lunar horizon and where the filter's orbital propagator expected it to be—began to swell:

$$\mathbf{y}_k = \mathbf{z}_k - \mathbf{h}(\mathbf{x}_{k|k-1})$$

In nominal translunar coast, $\mathbf{y}_k$ was an imperceptible fraction of an arcsecond. Now, it swung through forty-five arcseconds.

The filter’s autonomous innovation gating logic responded as programmed. To prevent corrupt sensor measurements from degrading the spacecraft's estimated trajectory, the software evaluated the Normalized Innovation Squared:

$$\epsilon_k = \mathbf{y}_k^T \mathbf{S}_k^{-1} \mathbf{y}_k$$

where $\mathbf{S}_k = \mathbf{H}_k \mathbf{P}_{k|k-1} \mathbf{H}_k^T + \mathbf{R}_k$ was the residual covariance matrix.

If $\epsilon_k$ exceeded 16.3—the classical 99.9% confidence boundary for a three-degree-of-freedom chi-square distribution—the measurement was rejected as an unphysical outlier.

```
[EKF-NAV] Measurement Frame 5101: NIS = 42.8 > 16.3. REJECTED.
[EKF-NAV] Measurement Frame 5102: NIS = 68.1 > 16.3. REJECTED.
[EKF-NAV] Measurement Frame 5103: NIS = 114.6 > 16.3. REJECTED.
```

One after another, with ruthless algorithmic obedience, every single optical navigation frame was discarded.

The state estimator was starving. Without measurement updates to rein in the integration drift, the flight software was forced to propagate the six-dimensional state vector purely by integrating the IMU gyroscopes and accelerometers across the non-linear, non-spherical gravitational fields of the Earth, the Moon, and the Sun.

---

### The Rank Collapse in Register 14

In cislunar celestial mechanics, propagating an orbit without measurement updates across the Earth-Moon weak stability boundary is a mathematical death sentence.

At the Lagrange boundary between the two celestial bodies, the gravity gradients pull in opposite directions. The linearized state transition matrix $\mathbf{\Phi}(t_k, t_{k-1})$ becomes severely ill-conditioned. The true uncertainty distribution does not expand as a neat, symmetric Gaussian sphere; it stretches and warps into an impossibly thin, curved banana shape along the unstable manifold.

Within the flight computer's memory registers, the covariance matrix $\mathbf{P}$ developed an extreme, pathological disparity between its eigenvalues. The positional uncertainty along the velocity vector expanded to forty kilometers, while the uncertainty perpendicular to the orbital plane remained constrained at twenty meters.

The condition number of $\mathbf{P}$—the ratio of its largest eigenvalue to its smallest—skyrocketed from a healthy $10^2$ to an unstable $10^8$.

Then came the fatal subtraction.

At 16:48 UTC, after rejecting two hundred and nineteen consecutive optical navigation frames, the OpNav camera caught a brief, clear interval of solar shadowing. A high-contrast image of the crater Copernicus flashed onto the sensor array, free of Cherenkov streaking.

The filter calculated the innovation. The measurement residual passed beneath the chi-square gate: $\epsilon_k = 11.2 < 16.3$. The flight executive accepted the update.

It began computing the Joseph-form covariance update:

$$\mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K} \mathbf{H}) \mathbf{P} (\mathbf{I} - \mathbf{K} \mathbf{H})^T + \mathbf{K} \mathbf{R} \mathbf{K}^T$$

In standard 32-bit IEEE 754 floating point, the mantissa has exactly twenty-four bits of precision—equivalent to approximately seven decimal digits. When numbers of vastly different scales are multiplied and added, the lower-order bits are silently truncated.

To compute the updated velocity variance along the radial axis, the PowerPC microprocessor executed a floating-point subtraction between two massive numbers that were identical across their first six decimal places:

$$P_{vv} = 482914.8 - 482915.2$$

In pure mathematical analysis with infinite real numbers, the result would have been a minute positive variance. In the 32-bit hardware register of the RAD750, the subtraction suffered catastrophic roundoff cancellation.

The updated diagonal element stored in Register 14 was:

$$P_{vv} = -0.4000000$$

A negative variance.

The matrix $\mathbf{P}_{k|k}$ was no longer positive-definite. It had lost its mathematical rank. One of its eigenvalues had crossed the zero axis into the negative complex half-plane.

Instantly, the residual covariance matrix $\mathbf{S} = \mathbf{H}\mathbf{P}\mathbf{H}^T + \mathbf{R}$ inherited the negative eigenvalue. When the flight software evaluated the Normalized Innovation Squared for the subsequent measurement frame, the matrix inversion inverted the sign of the entire quadratic form:

$$\chi^2 = \mathbf{y}^T \mathbf{S}^{-1} \mathbf{y} = -287.412$$

In the flight software’s C++ codebase, written under NASA software safety standards twenty years earlier, the measurement validation gate had been coded as a simple upper-bound conditional check:

```c
if (nis <= GATE_LIMIT) {
    accept_measurement();
} else {
    reject_measurement();
}
```

The developers had anticipated large positive values during sensor failures. They had never imagined that the laws of probability could be violated so profoundly that a variance could become negative.

Because $-287.412$ was mathematically less than $16.3$, the gate evaluated to `TRUE`.

The filter opened its doors. It accepted every corrupted, noisy, out-of-scale measurement frame without restriction. With every update, the negative variance propagated deeper into the state estimates. The estimated altitude ceased to reflect physical reality, freezing on the telemetry displays at a comfortable, reassuring three hundred kilometers above the lunar surface.

In the physical void, undisturbed by the software's delusional registers, Artemis-7 was falling at 1.8 kilometers per second toward the jagged highland ridges of the lunar farside.

---

### The FCR-1 Telemetry Alarms

In Building 30 of the Lyndon B. Johnson Space Center in Houston, the Flight Control Room (FCR-1) was submerged in a cold, fluorescent gloom.

Behind the Flight Dynamics console, Marcus Thorne sat motionless. He was thirty-nine, with hollows under his cheekbones and eyes reddened from twenty-two hours on console. A printed trajectory plot from the morning shift was taped to the edge of his workspace, its paper curling under the air-conditioning vents.

On his primary display, the real-time cislunar ephemeris feed was refreshing at one hertz.

To an untrained eye, the mission looked stable. The spacecraft summary widget showed a green status banner: `EKF STATE: CONVERGED`. The velocity vector was holding within nominal margins.

Marcus leaned forward, his nose two inches from the terminal glass.

He had toggled the telemetry display from the primary mission summary to the raw covariance diagnostic page—a low-level engineering screen that flight controllers rarely opened during nominal coast phases.

"Sarah," Marcus said. His voice was quiet, lacking the sharp urgency that usually accompanied a flight abort call, but it had a deadweight gravity that cut straight through the low hum of the room.

Flight Director Sarah Lin looked up from the center console. She was forty-eight, known across the directorate as 'Iron Sarah,' a veteran who had worked her way up from electrical systems on the International Space Station to the top seat in Mission Control. She wore a dark blue blazer with the sleeves pushed up to her forearms.

"Go ahead, FIDO," she said over the flight loop.

"Take a look at Channel 44-Bravo on the FIDO console," Marcus said. "RAD750 primary bus. Covariance trace."

Lin tapped her console keyboard. Channel 44-Bravo appeared on the large front projection screen at the head of the room.

Across the bottom of the plot, the positional uncertainty ellipsoids were rendered as green bars. But the third bar—the radial velocity variance along the spacecraft's nadir vector—was not pointing upward. It was inverted. It was a red spike extending downward below the zero baseline.

"What am I looking at, Marcus?" Lin asked. Her eyes narrowed. "Is that a display scaling glitch?"

"It’s not a display glitch," Marcus replied, his voice chillingly steady. "It’s a sign inversion. The state covariance matrix aboard Orion has lost positive-definiteness. Register 14 is holding a negative diagonal element."

"A negative variance?" The Flight Software Lead, sitting three consoles over, spun around in his chair. "That's impossible. The Joseph-form update is guaranteed positive-semidefinite. It’s an analytical identity."

"It’s an analytical identity on paper with real numbers," Marcus snapped, turning his chair to face the software engineer. "It is not an identity in 32-bit floating point after two hundred frames of covariance starvation. The mantissa truncated during the Copernicus update. The filter evaluated a negative NIS, passed the chi-square gate, and accepted corrupted optical limb data."

Sarah Lin was on her feet. "What is the physical state of the vehicle, FIDO?"

"The vehicle thinks it’s in a nominal translunar coast with a perilune altitude of one hundred and eighty kilometers," Marcus said. "That’s what its guidance computer is reporting. But that’s a hallucination. The physical spacecraft hasn’t executed a midcourse correction in forty-two hours. Without corrective delta-v, lunar gravitational perturbation has pulled the orbital plane two point four degrees off nominal."

Marcus slammed an enter key, running an independent numerical integration of the last verified radar state vector captured by Goldstone before the solar storm hit.

A red trajectory curve bloomed across the front wall display. It arced past the Moon, clipped the orbital horizon, and terminated abruptly in a solid red X on the farside highlands, inside the rim of Daedalus crater.

"Physical perilune is negative thirty-eight point five kilometers," Marcus said, the words falling like lead weights into the silence of FCR-1. "Impact is five hours and forty minutes away. If we don’t restore the onboard filter and burn fifty meters per second of radial correction before loss of signal, Artemis-7 will lithobrake into farside bedrock at six thousand kilometers an hour."

---

### The Call to Blacksburg

Four hundred miles to the northeast, in the cold autumn rain of Blacksburg, Virginia, Ryan Vance was sitting on the concrete floor of his garage.

The garage smelled of solder flux, damp masonry, and stale black tea. A kerosene space heater chattered in the corner, throwing orange reflections across the metal legs of a surplus workbench.

On the workbench, an amateur deep-space radio rig—a six-foot aluminum parabolic dish mounted on a heavy-duty azimuth-elevation rotator outside in the gravel driveway—was feeding an unencrypted S-band telemetry stream into a dual-monitor Linux workstation.

Ryan had written his own demodulator scripts to parse the public NASA Space Network telemetry broadcast. On his left monitor, the raw hexadecimal flight telemetry of Artemis-7 was cascading in real time.

Beside the monitor sat the four-hundred-dollar NVIDIA Jetson Orin Nano dev board, its seven-watt thermal fan humming faintly inside a 3D-printed plastic housing.

Ryan had spent two years staring at that exact hexadecimal sequence.

When the negative variance struck the Orion flight software, Ryan didn't need FCR-1 to tell him what had happened. He saw the symptom in the raw telemetry bytes of Channel 44-Bravo: the high bit of the floating-point word in Register 14 had flipped to `1`, indicating a negative sign in the IEEE 754 float32 representation.

He grabbed his phone and dialed a direct line he had memorized four years earlier.

At NASA Goddard Space Flight Center in Greenbelt, Maryland, Dr. Elena Rostova was sitting in the high-gain optical communications laboratory, surrounded by diagnostic oscilloscopes and real-time laser downlink monitors. Her cell phone vibrated violently against the stainless steel surface of an optical bench.

She picked it up on the second ring. "Rostova."

"Elena," Ryan said, without greeting. "Are you looking at Orion's S-band downlink?"

Elena gripped the receiver, her voice dropping to a whisper. "Ryan. Houston has an emergency loop active. FCR-1 is claiming the vehicle has suffered a state divergence, but the contractor reps are swearing the telemetry display is just a bit-flip in the display driver."

"Tell Sarah Lin it is not a display glitch," Ryan said, his voice hard, rapid, and mathematically surgical. "It's the Joseph-form cancellation under low-precision floating point. It's the exact failure mode I documented in the Plum Brook technical memorandum. The filter hit an ill-conditioned covariance condition, took a single good observation, subtracted nearly equal numbers in float32, and generated a negative eigenvalue. The NIS is sitting at negative two hundred and eighty-seven. The filter is wide open."

Elena's breath hitched. She knew the Plum Brook data; she had fought the review board to read it. "Can they reset the filter from the ground?"

"They can't," Ryan said. "Canberra DSN is in an ionospheric blackout from the flare. Goldstone is dipping below eight degrees elevation. Their uplink bandwidth is five bits per second over UHF. By the time they format a ground command to overwrite the RAD750 memory registers, Orion will be behind the lunar limb."

"Then the crew is dead," Elena said.

"Not if you use the laser," Ryan replied.

Silence stretched across the phone line, punctuated only by the hum of the cooling fans in the Goddard optical lab.

"The laser?" Elena repeated. "The 1550-nanometer optical communications demo? That's an experimental payload, Ryan. It's not qualified for flight control commanding. It doesn't even talk to the main 1553 avionics bus."

"It talks to the auxiliary communication processor," Ryan countered. "Which has a direct memory-mapped bridge to the guidance interface. And the Mount Stromlo optical terminal in Australia has line-of-sight to the Moon right now. It's midnight in Canberra. The skies over the Australian Capital Territory are crystal clear."

"What do we upload?" Elena asked, her heart hammering against her ribs. "A patch to the RAD750 EKF? The source code isn't even compiled for PowerPC."

"You don't patch the EKF," Ryan said. He looked down at the Jetson Orin Nano sitting on his workbench. On its solid-state drive sat a four-hundred-and-eighty-two-kilobyte compiled binary: `argonaut_os_core.elf`. "You upload ArgonautOS. You take the guidance executive away from the floating-point filter entirely. The Square Root Information Filter runs in 32-bit integer arithmetic. It cannot lose rank. It cannot evaluate a negative variance. It will solve their trajectory in twelve milliseconds."
"""

CH07 = r"""# CHAPTER SEVEN
## Dead Man's Trajectory
### The Houston Standoff

Inside the FCR-1 conference room behind the glass partition of Mission Control, the atmosphere had deteriorated into an open shouting match.

The room smelled of stale coffee, industrial floor wax, and human panic. On the whiteboard along the western wall, Marcus Thorne had drawn three crude sketches of the Earth-Moon three-body potential well, with a jagged red arrow plunging into the farside lunar crust.

Around the table sat eight people: Sarah Lin, her jaw set like granite; Marcus Thorne; the Flight Dynamics officer; the Lead Flight Director for the Artemis program; and four senior contractor representatives from Boeing and Lockheed Martin, their NASA badges dangling from branded lanyards.

"We are not uploading unverified third-party software to an active crewed spacecraft," Arthur Vance—no relation to Ryan, a senior vice president of flight systems for Lockheed—said, slamming his open palm on the laminate table. "It violates every flight certification protocol established since Apollo 11. If we upload unverified code and the auxiliary processor hangs, we lose command authority over the entire service module. We lose RCS, we lose the AJ10, we lose everything."

"You don't have command authority now, Arthur!" Marcus shot back, leaning across the table until he was inches from the executive's face. "Orion’s flight computer thinks its perilune is one hundred and eighty kilometers. Its automated burn manager will not fire the service propulsion engine because it believes the spacecraft is on a nominal free-return trajectory. In four hours and fifty minutes, that spacecraft will strike the crater Daedalus at two kilometers a second. You want to follow flight certification protocols all the way into the bedrock?"

"We execute a manual burn," Arthur insisted, his face flushed. "We instruct the crew to take manual attitude control, point the nose to the burn vector using the optical reticle on the commander's window, and fire the AJ10 for sixty seconds under manual switch closure."

"Under what attitude?" Marcus demanded. "Look at the telemetry! The Honeywell IMU has been drifting without an external star-tracker reference for six hours. The gyro bias is sitting at zero point zero eight degrees per hour. Across six hours of coast, that’s half a degree of uncorrected attitude error. In the non-linear three-body manifold around the Moon, half a degree of burn pointing error doesn't raise perilune—it rotates the velocity vector into an even steeper dive. I ran the Monte Carlo dispersion twenty minutes ago: a manual blind burn has a sixty-two percent probability of accelerating their impact."

Sarah Lin held up a hand. The room fell silent instantly.

"Marcus," Lin said quietly. "What is our current ground tracking status?"

"Dead," Marcus said flatly. "Canberra DSN is blind. The coronal mass ejection from the X8.4 flare slammed into the Australian ionosphere two hours ago. Total electron content over the Pacific Basin is pegged off the scale. S-band and X-band radio signals are refracting by several degrees; we can't maintain phase lock on their carrier wave. Goldstone has dipped to six degrees elevation; within forty minutes, the antenna will hit its mechanical elevation limit and stow. We have zero radio link to the vehicle until Madrid rises in seven hours."

"And by then?" Lin asked.

"By then, Orion is a smear of pulverized aluminum across thirty miles of lunar farside regolith."

---

### The Red Wire into FCR-1

The conference room phone beeped with a sharp, high-priority warble.

Lin reached over and hit the speaker button. "Lin here. Go."

"Sarah, this is Elena Rostova at Goddard," a voice echoed through the speaker, crisp, tight, and completely devoid of hesitation. "I am standing in the Optical Communications Directorate with Dr. Ryan Vance on secure patch. We have a solution."

Arthur groaned audibly. "Sarah, do not entertain this. Ryan Vance was forced out of academia for refusing to peer-review his relational models. He’s an outsider running rogue simulations on consumer hardware."

"Shut up, Arthur," Sarah Lin said without looking at him. She leaned toward the speaker. "Elena, what do you have?"

"Mount Stromlo Observatory in the Australian Capital Territory," Elena said. "They are operating the 1.8-meter telescope equipped with a 1550-nanometer infrared adaptive optics laser transceiver. Because it’s an optical system operating at near-infrared wavelengths, it is completely immune to the ionospheric electron density fluctuations that blinded Canberra's radio dishes. The skies over Mount Stromlo are photometric. They have Orion in active optical tracking lock right now."

"What is the uplink bandwidth?" Marcus asked.

"Two hundred megabits per second," Elena replied. "Enough to send the entire Library of Congress in three minutes. But we don't need three minutes. Ryan Vance has compiled the autonomous integer guidance core of ArgonautOS into a four-hundred-and-eighty-two-kilobyte ELF binary."

"Tell me about the code, Dr. Vance," Sarah Lin said, her eyes fixed on the speakerphone.

Through the wire, Ryan Vance’s voice was calm, measured, and shockingly direct.

"Flight Director," Ryan said. "The binary contains two mathematical algorithms. First, a Square Root Information Filter implemented via Householder orthogonal QR factorization. It completely bypasses covariance matrices. It parameterizes state uncertainty as an upper-triangular information matrix $\mathbf{R}$, where $\mathbf{P}^{-1} = \mathbf{R}^T \mathbf{R}$. It is mathematically impossible for $\mathbf{R}$ to lose positive-definiteness, because Householder reflections preserve the Euclidean norm to machine precision. There are no subtractions of nearly equal quantities. Second, it contains the FixedQP active-set quadratic programming solver running in thirty-two-bit integer math. It solves the non-linear three-body Lambert targeting problem in two hundred and fifty-six deterministic clock cycles."

"Can it execute on the vehicle?" Lin asked. "The RAD750 is an ancient architecture."

"It doesn't run on the RAD750," Ryan explained. "It runs on the auxiliary optical communication processor—a modern ARM-based SoC integrated into the optical transceiver module on the service module exterior. That processor has direct DMA access to the secondary CAN bus governing the auxiliary reaction control thrusters. Once uploaded, ArgonautOS will take autonomous command of the four ten-pound reaction control pods, determine the true state vector using the raw OpNav camera stream, and execute a forty-nine point five meter-per-second radial correction burn before the spacecraft enters the lunar occultation zone."

"It's a suicide pact," Arthur hissed. "We are handing control of an eight-billion-dollar crewed spacecraft to a script written in a garage!"

"Arthur," Sarah Lin said, standing up and towering over the table. "Right now, your certified aerospace software is driving three astronauts into the side of a mountain at Mach five. If we do nothing, they die. If we upload this binary, they have a mathematical chance."

She looked at Marcus Thorne. "FIDO. What is your recommendation?"

Marcus didn't hesitate. "Authorize the laser uplink, Flight. Let Ryan Vance fly the ship."

Sarah Lin tapped the flight director console switch, opening the wide-area net across all NASA flight centers.

"This is Flight," she announced, her voice ringing with absolute authority. "I am authorizing an emergency optical uplink to Artemis-7 via Mount Stromlo. Goddard, coordinate the laser pointing vectors. FIDO, prepare the trajectory verification scripts. We have one shot at this before the vehicle passes behind the Moon. Let's get to work."

---

### The Three-Body Trap

Outside the conference room, Marcus walked back to the Flight Dynamics console and pulled up the three-body Jacobi invariant equations on his workstation.

In classical Newtonian astrodynamics, a spacecraft orbits a single dominant central body: an ellipse, a parabola, or a hyperbola. The energy is conserved, the angular momentum is constant, and Kepler's elegant laws dictate the trajectory with clockwork simplicity.

In the Earth-Moon system, that clockwork dissolves.

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
"""

CH08 = r"""# CHAPTER EIGHT
## Light Across the Blind Spot
### The Eucalyptus Ridge

On the summit of Mount Stromlo, seven hundred and seventy meters above the Australian capital city of Canberra, the cold night air smelled of eucalyptus resin and dry mountain dust.

Inside the copper-sheathed dome of the 1.8-meter optical research telescope, there were no lights except for the pale amber glows of instrument racks and the rhythmic, clicking cadence of the azimuth gear drive tracking across the meridian.

Outside the dome slit, the southern sky was an ocean of diamond-hard stars: the Southern Cross tilted on its side, the dark rift of the Coal Sack Nebula standing out like a tear in the fabric of the Milky Way, and high in the northeast, hanging pale and brilliant over the Brindabella ranges, the gibbous Moon.

Dr. Lachlan Mackay, Senior Optical Engineer for the Australian National University, sat at the telescope control console with a heavy headset clamped over his grey hair.

"Goddard Optical Directorate, Mount Stromlo terminal is in closed-loop pointing lock," Mackay spoke into the boom mic, his Australian drawl unhurried despite the tension vibrating through the international voice loop. "We have the Orion optical transceiver acquired on our quad-cell tracking sensor. Target elevation is forty-one degrees. Atmospheric seeing is zero point eight arcseconds. The adaptive optics deformable mirror is active, operating at two point four kilohertz."

Beneath the primary mirror cell, a piezoelectric deformable mirror—a thin, flexible sheet of polished glass backed by ninety-seven ceramic actuators—was pulsing thousands of times a second. It was sensing the atmospheric turbulence in the thermal layers above the Australian capital and flexing its surface to cancel the wavefront distortions, transforming a smeared, twinkling star image into a diffraction-limited optical point.

"Mount Stromlo, this is Elena Rostova at Goddard," Elena's voice came through the fiber link with zero latency. "Telemetry confirm, Lachlan. We have the payload staged. File name: `argonaut_os_core.elf`. Size: four hundred and eighty-two kilobytes. Checksum: `0x7F4A8C91`. Are you ready to arm the high-power transmitter?"

Mackay looked at the key-switch on the interlock panel. A red tag dangled from the brass tumbler: `DANGER: CLASS 4 COVERT LASER RADIATION - EYE HAZARD AT 500 KM`.

He turned the key ninety degrees.

A bank of cooling pumps hummed to life in the coudé room below the dome floor.

"Laser armed," Mackay said. "Ytterbium fiber laser running at fifteen hundred and fifty nanometers. Average power output: forty watts. Beam divergence: twenty-five microradians. Goddard, you have the trigger."

"Three," Elena counted down. "Two. One. Mark. Uplink initiated."

From the secondary mirror housing of the 1.8-meter telescope, an invisible lance of infrared light cut upward into the night sky.

To the naked eye, the sky remained dark. But at fifteen hundred and fifty nanometers—a wavelength invisible to human retinas but perfectly matched to the quantum efficiency of InGaAs photodetectors—a blinding beacon of forty watts was climbing through the troposphere, traversing the stratosphere, and punching outward across three hundred and eighty thousand kilometers of hard vacuum toward the Moon.

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
[DMA-ENGINE] INCOMING PACKET STREAM: ARGONAUT_OS_CORE.ELF
[DMA-ENGINE] WRITING TO FLASH BLOCK 0x00400000...
```

The transfer took exactly thirty-eight milliseconds.

In the auxiliary communication processor's non-volatile memory, the cyclic redundancy check evaluated the downloaded payload:

```
[CRC32] COMPUTED: 0x7F4A8C91
[CRC32] EXPECTED: 0x7F4A8C91
[CRC32] INTEGRITY VERIFIED: 100% MATCH
[EXEC] OVERRIDING GUIDANCE ARBITER...
[EXEC] ARGONAUTOS INITIALIZING IN ISOLATED MEMORY PARTITION...
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

Reid Wiseman looked at the digital prompt. Through his headset, over the crackling UHF link from Goldstone's dying dish, Sarah Lin’s voice broke through the static one last time before horizon loss:

*"Artemis-7, Houston. Accept the takeover. Authorize the burn. I say again: accept the takeover."*

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

`GNC-CORE: ARGONAUTOS REV 6.1 // AUTHOR: DR. RYAN VANCE // INTEG-SRIF`

Marcus reached over to his private phone, dialed the Blacksburg garage, and whispered into the receiver:

"Ryan. You did it. You just saved three lives with seven watts."
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_06_The_Negative_Variance.md"), "w", encoding="utf-8") as f:
    f.write(CH06.strip() + "\n")
print(f"Updated Chapter_06_The_Negative_Variance.md: {len(CH06.split())} words")

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_07_Dead_Mans_Trajectory.md"), "w", encoding="utf-8") as f:
    f.write(CH07.strip() + "\n")
print(f"Updated Chapter_07_Dead_Mans_Trajectory.md: {len(CH07.split())} words")

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_08_Light_Across_the_Blind_Spot.md"), "w", encoding="utf-8") as f:
    f.write(CH08.strip() + "\n")
print(f"Updated Chapter_08_Light_Across_the_Blind_Spot.md: {len(CH08.split())} words")
