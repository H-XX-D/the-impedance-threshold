# CHAPTER SEVEN
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
