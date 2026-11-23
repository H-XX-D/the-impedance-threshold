#!/usr/bin/env python3
"""
Deepen Chapters 6, 7, 8 of Act II to ~2,200 words each.
Author: Todd Hendrixx
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

CH6_FULL = r"""# CHAPTER SIX
## The Negative Variance
### The Avionics Bay & The PowerPC Mainframe

Inside the unpressurized secondary avionics bay of the Orion service module, three BAE RAD750 flight computers were housed inside a gold-plated aluminum chassis.

Each computer was a marvel of aerospace hardening: a 133-megahertz PowerPC architecture manufactured with radiation-tolerant silicon-on-insulator (SOI) semiconductor gates, designed to withstand a total ionizing dose of one hundred thousand rads without catastrophic gate oxide breakdown.

They were built to survive the radiation.

They were not built to survive the mathematics.

As the star trackers blinded, the triple-redundant flight computers switched to their fallback navigation mode: fusing the drifting rate-integrating gyroscopes of the Honeywell Inertial Measurement Unit (IMU) with intermittent optical bearing measurements to the Moon's illuminated limb, captured by the forward Optical Navigation (OpNav) camera.

The OpNav camera was taking one image every forty seconds. Through the sunlit haze, the lunar crescent was a brilliant, overexposed arc of white against the black void.

The spacecraft’s flight software was executing its core state estimator: an **Extended Kalman Filter (EKF)** running in 32-bit single-precision floating point.

Every forty seconds, the filter executed its measurement update loop:

$$\mathbf{K}_k = \mathbf{P}_{k|k-1} \mathbf{H}_k^T \left( \mathbf{H}_k \mathbf{P}_{k|k-1} \mathbf{H}_k^T + \mathbf{R}_k \right)^{-1}$$

$$\mathbf{x}_{k|k} = \mathbf{x}_{k|k-1} + \mathbf{K}_k (\mathbf{z}_k - \mathbf{h}(\mathbf{x}_{k|k-1}))$$

where $\mathbf{z}_k$ was the optical bearing to the lunar limb, and $\mathbf{R}_k$ was the measurement noise covariance matrix.

Because of the proton storm, the optical camera's centroiding algorithm was jittering wildly. The perceived edge of the lunar disk was dancing by tens of pixels from frame to frame as secondary Cherenkov transients struck the CMOS imaging array.

The filter's innovation residual—the difference between where the camera said the Moon was and where the filter expected it to be—began to grow:

$$\mathbf{y}_k = \mathbf{z}_k - \mathbf{h}(\mathbf{x}_{k|k-1})$$

In nominal flight, $\mathbf{y}_k$ was a fraction of an arcsecond. Now, it was forty-five arcseconds.

The filter’s innovation gating logic kicked in. To prevent bad sensor data from corrupting the spacecraft's estimated trajectory, the software checked the **Normalized Innovation Squared (NIS)**:

$$\epsilon_k = \mathbf{y}_k^T \mathbf{S}_k^{-1} \mathbf{y}_k$$

where $\mathbf{S}_k = \mathbf{H}_k \mathbf{P}_{k|k-1} \mathbf{H}_k^T + \mathbf{R}_k$.

If $\epsilon_k$ exceeded 16.3 (the 99.9% confidence boundary for a 3-degree-of-freedom chi-square distribution), the measurement was rejected.

```
[EKF-NAV] Measurement Frame 5101: NIS = 42.8 > 16.3. REJECTED.
[EKF-NAV] Measurement Frame 5102: NIS = 68.1 > 16.3. REJECTED.
[EKF-NAV] Measurement Frame 5103: NIS = 114.6 > 16.3. REJECTED.
```

One after another, every single optical measurement was discarded.

The filter was now "starving." Without measurement updates, it was forced to propagate the state vector purely by integrating the IMU gyros and accelerometers across the non-linear gravitational field of the Earth and the Moon.

---

### The Rank Collapse in Register 14

In cislunar mechanics, propagating an orbit without updates across the Earth-Moon weak stability boundary is a mathematical death sentence.

At the Lagrange boundary, the gravity gradients of the two celestial bodies pull in opposite directions. The state transition matrix $\mathbf{\Phi}(t_k, t_{k-1})$ becomes ill-conditioned. The uncertainty ellipsoid does not expand uniformly; it stretches into an impossibly thin, curved banana shape along the unstable manifold.

The covariance matrix $\mathbf{P}$ developed extreme disparity between its eigenvalues: the positional uncertainty along the velocity vector grew to forty kilometers, while the uncertainty perpendicular to the orbital plane remained at twenty meters.

The condition number of $\mathbf{P}$—the ratio of its largest eigenvalue to its smallest—skyrocketed from $10^2$ to $10^8$.

Then came the fatal subtraction.

At 16:48 UTC, after rejecting two hundred and nineteen consecutive optical frames, the OpNav camera caught a brief moment of solar shadowing, producing a clean, high-contrast image of the crater Copernicus.

The filter calculated the innovation. The measurement residual passed the chi-square gate: $\epsilon_k = 11.2 < 16.3$. The filter accepted the update.

It began computing the Joseph-form covariance update:

$$\mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K} \mathbf{H}) \mathbf{P} (\mathbf{I} - \mathbf{K} \mathbf{H})^T + \mathbf{K} \mathbf{R} \mathbf{K}^T$$

In 32-bit IEEE 754 floating point, the mantissa has only twenty-four bits of precision—roughly seven decimal digits.

To compute the updated velocity variance along the radial axis, the microprocessor subtracted two massive numbers that were identical in their first six decimal places:

$$P_{vv} = 482914.8 - 482915.2$$

In exact real arithmetic, the result was a tiny positive number bounded by the measurement noise.

In 32-bit floating point, the least-significant rounding error flipped the sign.

$$P_{vv} = -0.000412 \text{ m}^2/\text{s}^2$$

A negative variance.

The foundation of probability theory had just dissolved in register `r14` of Computer A.

In the next cycle, the software attempted to calculate the innovation covariance for the next star frame:

$$\mathbf{S}_{k+1} = \mathbf{H} \mathbf{P}_{k|k} \mathbf{H}^T + \mathbf{R}$$

Because $\mathbf{P}_{k|k}$ contained the negative variance, the determinant of $\mathbf{S}$ inverted. When the processor evaluated the quadratic form $\epsilon_{k+1} = \mathbf{y}^T \mathbf{S}^{-1} \mathbf{y}$, the result was a mathematical monstrosity:

$$\text{NIS} = -287.4$$

The flight executive software threw a hardware interrupt:

```
[FATAL-EXC] TRIPLE VOTING ANOMALY: COMPUTER A
[FATAL-EXC] REG 14 (P_VEL_RADIAL) < 0.0
[FATAL-EXC] NIS EVALUATED TO NEGATIVE VALUE: -287.412
[FATAL-EXC] CHI-SQUARE INVARIANT VIOLATED. MATRIX CORRUPT.
[FATAL-EXC] COMPUTER A DISQUALIFIED FROM FLIGHT BUS.
```

Computer B saw Computer A declare an unrecoverable mathematical exception. It attempted to take over the navigation bus, executing the same algorithm with the same corrupted historical covariance packet.

Within forty milliseconds, Computer B threw the exact same exception: $\text{NIS} = -312.1$.

Computer C attempted to re-invert the information matrix to re-orthogonalize the state. The matrix was singular. Computer C entered an infinite division loop, its CPU instruction pointer locked in a hard hang.

---

### The Architecture of the Disassembly

Inside the flight software architecture, the failure was traced to a single subroutine in the flight guidance library: `gnc_ekf_joseph_update.c`.

When the contractor avionics team had coded the routine fifteen years earlier, they had followed standard military specification guidelines. They had tested the code across thousands of low-Earth orbit shuttle simulations, where gravitational gradients were smoothly quadratic and the matrix condition number rarely exceeded two hundred.

Under low-Earth orbit conditions, the Joseph form was bulletproof.

```assembly
; Disassembly of RAD750 Core (PowerPC 750GL Architecture)
; Routine: EKF_COV_UPDATE_DIAG
0x0041F8C0:  lfs      f1, 0(r3)      ; Load prior P_diag element
0x0041F8C4:  lfs      f2, 4(r4)      ; Load KH_P_cross term
0x0041F8C8:  fsubs    f3, f1, f2     ; Floating-point subtract single
0x0041F8CC:  stfs     f3, 0(r14)     ; Store result to register r14
0x0041F8D0:  fcmpu    cr0, f3, f0    ; Compare result against float 0.0
0x0041F8D4:  bge      0x0041F8DC     ; Branch if Greater or Equal
0x0041F8D8:  trap                    ; EXCEPTION: SIGFPE_NEGATIVE_VARIANCE
```

The trap instruction at `0x0041F8D8` was never supposed to execute. The software manual had described it as an "architectural impossibility included solely for defense-in-depth compliance."

Yet there it was, executing on all three channels in the vacuum of cislunar space.

When the trap fired, the operating system kernel—a certified real-time operating system—followed its strict mission rules. It didn't try to guess. It didn't try to clamp the value to zero. Clamping a variance to zero would falsely tell the guidance system that the spacecraft’s velocity was known with infinite precision, which would cause the Kalman gain $\mathbf{K}$ to collapse to zero, permanently blinding the filter to all future measurements.

The kernel did the only thing it was certified to do: it declared the navigation state invalid and locked the thrusters.

---

### The Drift into the Mountain

Inside the storm shelter, the amber cautions vanished, replaced by the stark, flashing crimson of a master alarm:

`FCS: PRIMARY GUIDANCE INHIBIT`  
`NAV STATE: INVALID`  
`AUTONOMOUS CONTROL: LOCKED`  
`FLIGHT RULE 4-BRAVO ENFORCED`  

Commander Sarah Ross pushed her way out of the shelter, ignoring the tingling in her teeth from the secondary proton scatter. She strapped herself into the pilot's couch and stared at the screens.

Every orbital trajectory predictor was frozen.

The flight computer had dropped into **Protective Screened Coast**. Under NASA flight rules, when the autonomous guidance system loses certified covariance confidence, all automated thruster firings are permanently locked out to prevent the spacecraft from executing an erratic burn that might burn up its fuel or send it into deep space.

She pulled up the last valid ballistic propagation recorded before the lock.

It had been calculated six hours ago, before the solar flare, when the spacecraft had experienced an unmeasured 0.3-meter-per-second venting impulse from a boiling auxiliary coolant line.

Without Trajectory Correction Maneuver 3 (TCM-3)—which was scheduled to fire in precisely sixteen hours—the Earth-Moon weak stability manifold did not guide the spacecraft into a gentle, curving free-return loop back toward Earth.

The Moon was rising in the forward viewport, massive, gray, and dead.

The last uncorrupted orbital mechanics trajectory displayed the perilune altitude:

$$\text{Altitude at Closest Approach} = -38.5 \text{ Kilometers}$$

Negative thirty-eight kilometers.

The trajectory line did not pass around the Moon. It terminated in the center of the farside crater Daedalus.

Artemis-7 was falling at 2,410 meters per second toward a direct, vertical impact with thirty billion tons of solid lunar granite.

Beside her, David Miller unstrapped his tablet. "Commander... at minus thirty-eight kilometers altitude, our impact point is inside the central peak ring of Daedalus. Relative impact velocity is Mach seven point one. The terrain elevation there is four thousand meters above mean lunar datum."

"We won't even feel it," Ross said quietly, staring out at the gray craters rotating in the dark. "It will happen in five milliseconds. A flash of white dust on the farside that no one on Earth will ever see."
"""

CH7_FULL = r"""# CHAPTER SEVEN
## Dead Man's Trajectory
### FCR-1, Houston

The Flight Control Room 1 at the Johnson Space Center was designed to project an aura of unflappable, air-conditioned omniscience.

Beneath the fifty-foot projection displays showing the global Mercator tracking map and the three-dimensional cislunar trajectory cone, sixty flight controllers sat in tiered rows behind curved consoles. The room was cold, kept at sixty-four degrees Fahrenheit to prevent the terminal hardware from overheating, and it smelled of stale cafeteria coffee, dry-erase cleaner, and the electric ozone of backup uninterruptible power supplies.

At 18:00 UTC, the aura of omniscience had evaporated.

On the central projection screen, the status indicator for Artemis-7’s Guidance, Navigation, and Control system was a flashing block of red text:

`GNC STATUS: DEGRADED / OPEN LOOP`  
`PRIMARY NAV CHANNELS: 0 OF 3 HEALTHY`  
`TCM-3 STATUS: INHIBITED (FLIGHT RULE 4-BRAVO)`  
`TIME TO PERILUNE: 14 HOURS 12 MINUTES`  

At the center console on the highest tier, Flight Director Michael Hayes sat with his arms crossed over his chest, his headset pushed back off his left ear. He was fifty-four, a veteran of twenty shuttle and space station missions, with graying crew-cut hair and the stubborn jaw of an engineer who had spent his life believing that standard operating procedures were the only wall between a flight crew and the vacuum of space.

Beside him stood Dr. Elena Rostova.

She had just arrived from the airfield after the emergency flight from Plum Brook. Her flight jacket was unzipped, her eyes bloodshot, her hair tied back in a hurried ponytail. In her hand, she held a ruggedized thumb drive containing the compiled binary of Ryan Vance’s relational guidance engine.

At the GNC console on the bottom tier, the contractor lead for the prime avionics contractor—a forty-five-year-old systems engineer named Greg Vance (no relation to Ryan)—was talking rapidly into his headset loop.

"Flight, GNC," Greg called out. "We have finished our analysis of the memory dump from Computer A. We confirm the numerical exception. It’s an IEEE floating-point mantissa underflow in the Joseph-form covariance calculation. The condition number of the information matrix degraded past ten to the eighth during the solar proton burst."

Hayes pressed his voice switch. "Can you patch the covariance matrix, Greg? Can we force-set the negative diagonal elements back to positive values and command a filter warm-restart?"

"Negative, Flight," Greg said immediately. "If we inject an artificial diagonal variance into the state vector, we corrupt the cross-covariance correlation terms. The filter will diverge within three cycles. The vehicle could fire its reaction control engines in the wrong direction during TCM-3 and deplete our delta-V reserves."

"Then what is your recommendation?" Hayes demanded. "We are fourteen hours from perilune. If we do nothing, the ship hits the lunar farside at two point four kilometers per second. I have four astronauts on that vehicle, Greg. Give me an actionable trajectory solution."

Greg swallowed, his voice tight. "Flight, our only certified option under the contingency matrix is an open-loop blind burn."

Elena Rostova stepped forward to the Flight Director’s console, slapping her hand against the formica desk.

"A blind burn is murder, Michael," Elena said, her voice cutting through the console loop. "You know the three-body dynamics. At the weak stability boundary, the Lyapunov exponent is positive. The trajectory is hyper-sensitive. If you fire a seventy-second burn using dead reckoning from gyros that have been drifting for twelve hours during an X-class solar flare, a velocity error of fifty centimeters per second translates to an orbital error of two hundred kilometers at perilune."

"And if we don't burn, we hit the dirt at Mach seven!" Greg fired back from his console. "At least with a blind burn, we give them a chance to skip out!"

"Skip out where?" Elena demanded. "If they skip out with a fifty-centimeter error, their perilune rises above the lunar gravity capture threshold. They miss the Moon entirely and enter an uncontrolled, sixty-day heliocentric orbit with seven days of oxygen on board! You aren't giving them a chance to survive. You’re giving them a slower way to suffocate."

---

### The Lyapunov Saddle & The Tiger Team

Elena pulled up the trajectory dispersion plot on the secondary projection screen.

The display showed ten thousand Monte Carlo trajectory lines fanning out from Artemis-7’s current estimated state. The visualization looked like a bundle of chaotic, frayed nylon threads:

- **Ninety-four percent of the trajectories** plunged directly into the lunar farside crust between craters Daedalus and Hertzsprung.
- **Five point eight percent of the trajectories** grazed the lunar exosphere and skipped out into deep interplanetary space, entering a 400-day heliocentric orbit with zero chance of recovery.
- **Only zero point two percent**—twenty trajectories out of ten thousand—happened to thread the razor-thin free-return corridor back to Earth.

"A blind burn is rolling a five-hundred-sided die where four hundred and ninety-nine faces mean death," Elena said.

"Then what do you propose, Elena?" Hayes asked, turning his chair to face her directly. "Canberra can't track them. Goldstone is below the horizon. Madrid is jammed by solar radio noise. We are blind on the ground, and their mainframes are locked in an exception loop."

"We use the edge core," Elena said.

She plugged the thumb drive into the auxiliary workstation terminal on the Flight Director’s console.

---

### The Seven-Watt Receipt

Elena brought up the Plum Brook qualification report on the auxiliary screen:

```
[QUAL-REPORT] NASA PLUM BROOK CHAMBER B
[QUAL-REPORT] HARDWARE: NVIDIA JETSON ORIN NANO (COMMERCIAL COTS)
[QUAL-REPORT] RUNTIME ENVIRONMENT: 5.14 WATTS DC
[QUAL-REPORT] ALGORITHM: HOUSEHOLDER SRIF + FIXEDQP (INTEGER ARITHMETIC)
[QUAL-REPORT] MONTE CARLO ITERATIONS: 10,000 RUNS ACROSS ARTEMIS WSB
[QUAL-REPORT] NUMERICAL EXCEPTIONS: 0
[QUAL-REPORT] NEGATIVE NIS INSTANCES: 0
[QUAL-REPORT] FLIGHT CERTIFICATION: TEST FACILITY QUALIFIED
```

Hayes stared at the report. Then he looked at the thumb drive.

"You want me to upload an uncertified, commercial software binary—written by an academic who was fired from Virginia Tech two weeks ago—into the flight avionics of a four-billion-dollar crewed spacecraft?"

"The software wasn't written for the primary flight mainframes, Michael," Elena said. "It doesn't touch the BAE mainframes. It boots into the **Auxiliary Optical Transceiver Processor**."

Hayes frowned. "The optical transceiver? The secondary comm payload?"

"Yes," Elena said, her voice dropping into a calm, unstoppable cadence. "When Orion was built, the secondary avionics bay was fitted with an experimental 1550-nanometer optical communications package developed by Goddard. It has its own dedicated ARM Cortex processor, its own direct memory access bus, and its own dedicated auxiliary DC power feed—clamped to seven point two watts. It is connected directly to the service module thruster driver bus via a secondary MIL-STD-1553 hardware relay."

She tapped the screen.

"The primary mainframes are dead because their floating-point Kalman filter cannot handle three-body pregeometry. Ryan Vance solved that problem. His code doesn't use floating-point math. It uses integer square-root information filtering. It executed ten thousand simulated recoveries at Plum Brook under minus one hundred and forty degrees Celsius without a single failure."

Greg turned around in his chair at the bottom tier, his face flushed with anger.

"Flight, this is insane! That auxiliary board was qualified as an experimental communications payload, not a class-A flight-critical guidance computer! If you let an integer filter fire the service module engines, you are violating every safety directive established since Apollo 1."

"Apollo 1 died because someone used flammable materials in a high-pressure oxygen cabin, Greg," Elena said without looking at him. "Artemis-7 is going to die because you used thirty-two-bit floating point to invert a singular matrix."

She looked straight into Hayes’s eyes.

"Michael, Sarah Ross has three children. David Miller’s wife is pregnant with their first daughter. In thirteen hours, they hit the mountain. You have no ground tracking because the DSN is blinded by the solar flare. You have no primary flight computers because the Kalman filter went negative. You have no options left except this one."

Hayes sat motionless for thirty seconds. He looked up at the big wall display, where the red trajectory line terminated bluntly against the gray curve of the farside Moon.

"Can Canberra uplink the binary?" Hayes asked quietly.

Elena’s face fell slightly. "No. The S-band down-link is completely dead. Canberra can’t even lock a five-baud carrier."

"Then how in the hell do you expect to get forty megabytes of software onto that spacecraft?"

"It isn't forty megabytes, Michael," Elena said, a faint smile breaking through her exhaustion. "It is four hundred and eighty-two kilobytes. And we aren't using radio."

She pointed to the global tracking map, where a tiny green dot was pulsing over the eastern coast of Australia.

"We use the laser."
"""

CH8_FULL = r"""# CHAPTER EIGHT
## Light Across the Blind Spot
### Mount Stromlo, Midnight

On the summit of Mount Stromlo, eight miles west of Canberra, Australia, the night sky was crisp, cold, and clear.

At twelve hundred meters above sea level, the observatory’s domed laser-ranging facility stood white against the eucalyptus forests of the Brindabella Ranges. Below in the valley, the lights of the Australian capital flickered faintly through the thin mountain air.

Inside the laser coudé room beneath the 1.8-meter optical telescope, Dr. Alistair Finch was working in his socks. He was fifty-two, an optical physicist who had spent twenty-five years bouncing pulsed green neodymium-YAG lasers off retroreflectors on the Moon to measure the drift of continents.

The red phone on the wall of the coudé lab—the direct, hardwired emergency line from the Australian Space Operations Centre—began to ring.

Finch stepped around the high-voltage capacitor banks, picked up the receiver, and tucked it against his shoulder while wiping a fused-silica laser lens with spectroscopic-grade methanol.

"Finch here."

"Alistair, this is Elena Rostova calling from Houston Mission Control."

Finch paused, his cloth hovering over the optics. "Elena? I’m tracking the solar flare reports. Canberra DSN says the radio spectrum is a total wash. How are your people on Orion?"

"They have twelve hours before lunar impact," Elena said without preamble. "Alistair, I need the Mount Stromlo optical station. Right now."

"We’re scheduled for space-debris laser tracking on low-Earth orbit satellites until dawn—"

"Cancel it," Elena interrupted. "I have authorization from the NASA Associate Administrator and the Australian Department of Defence. I am pushing a secure data stream to your terminal right now. It is a four-hundred-and-eighty-two-kilobyte bare-metal binary. You have to uplink it to Artemis-7."

Finch blinked, setting his solvent bottle down on the optical bench. "Elena... Orion is three hundred and twenty thousand kilometers out. The beam divergence across that distance, even with our one-point-eight-meter primary mirror, will produce a beam footprint sixty kilometers wide by the time it reaches the Moon."

"The optical transceiver on Orion uses an ultra-sensitive photon-counting avalanche photodiode array," Elena said. "We don't need gigabits. We need four hundred and eighty-two kilobytes, encoded in pulse-position modulation at fifteen fifty nanometers. Can you acquire their optical terminal?"

Finch looked up through the open slit in the dome.

High in the northern sky, the Moon was a brilliant, silver crescent hanging above the dark ridges of the Great Dividing Range. Just off its dark western limb, invisible to the naked eye, a tiny speck of human metal was falling toward oblivion.

"Give me ten minutes to tune the seed laser," Finch said.

---

### The Adaptive Wavefront over the Brindabellas

In the coudé room, Finch energized the high-power erbium-doped fiber laser amplifier.

A high-intensity infrared beam at exactly 1,550.42 nanometers began pulsing through the optical train: invisible to the human eye, but packing thirty watts of average optical power into sub-nanosecond pulses.

The beam passed through a fast-steering mirror system coupled to an adaptive optics bench. Thirty-two deformable piezoelectric actuators flexed the thin glass mirror five hundred times per second, pre-compensating for the atmospheric turbulence and thermal shimmering of the Australian night.

"Target coordinates loaded," Finch called into his headset. "Tracking vector derived from Mount Stromlo astrometric ephemeris. Engaging telescope drive."

Above the lab, the fifty-ton steel dome rotated with a deep, rumbling hum. The 1.8-meter telescope swung north, elevating to forty-eight degrees above the horizon.

Through the telescope's co-axial camera, the Moon filled the field of view. Two degrees off the sunlit limb, inside the black, unilluminated quadrant of the cislunar void, Finch’s tracking software projected a tiny green acquisition reticle.

"Laser safety cleared. Aircraft avoidance radar confirms zero traffic in the airspace sector. Firing uplink laser."

Finch slapped the red interlock button.

From the primary aperture of the telescope, an invisible, hyper-collimated shaft of coherent infrared light surged upward into the clear mountain sky. It punched through the troposphere, sliced through the stratosphere, and lanced out into the vacuum of cislunar space at three hundred thousand kilometers per second.

One point zero eight seconds later, the light wave reached Artemis-7.

Inside the dark, freezing equipment bay of the Orion spacecraft, a four-inch fused-silica aperture on the forward service module caught the edge of the expanding beam.

A high-gain InGaAs avalanche photodiode detected the rhythmic arrival of individual photon packets.

The auxiliary optical transceiver woke up:

```
[OPT-RX] 1550 nm Carrier Acquired. SNR: +18.4 dB.
[OPT-RX] Pulse-Position Modulation (PPM-16) Synchronized.
[OPT-RX] Incoming Bitstream: 1.2 Megabits per second.
[OPT-RX] Receiving: argonaut_os_core.elf (482 KB)
[OPT-RX] SHA-256 Checksum: VERIFIED.
[OPT-RX] Executing Auxiliary Bootloader...
```

In the command module, Sarah Ross was startled by a sudden, sharp, crystalline chime from the auxiliary communication panel—a sound she had never heard during flight simulations.

A small secondary LCD screen, dark since launch, flickered to life in bright green phosphor text:

```
==================================================
CISLUNAR-OS v1.0.4 [RELATIONAL INTEGER CORE]
AUTHOR: T. HENDRIXX / VANCE LABS
POWER CONSUMPTION: 5.12 WATTS (PASS)
==================================================
[BOOT] Initializing Householder SRIF Information Filter...
[BOOT] Star Tracker Raw ADC Bus Reacquired.
[BOOT] Applying Causal Reacquisition Mask...
[BOOT] 1,842 Proton Transients REJECTED.
[BOOT] 14 True Stellar Centroids IDENTIFIED.
[BOOT] Attitude Solution: LOCKED (Residual: 0.04 arcsec).
[BOOT] Information Matrix Condition Number: 84.2 (NOMINAL).
[BOOT] Negative NIS Protection: ACTIVE.
==================================================
[NAV-SOL] PERILUNE ALTITUDE CURRENT: -38.42 KM (IMPACT DETECTED)
[FIXED-QP] COMPUTING TRAJECTORY CORRECTION MANEUVER 3...
[FIXED-QP] CONVERGED IN 16 ITERATIONS (1.12 MILLISECONDS).
[FIXED-QP] REQUIRED DELTA-V: 49.52 M/S
[FIXED-QP] BURN DURATION: 18.4 SECONDS (AUX RCS QUADS)
[FIXED-QP] IGNITION T-MINUS: 04 MINUTES 12 SECONDS.
==================================================
AWAITING CREW EXECUTION AUTHORIZATION...
```

Sarah Ross stared at the green text, her breath catching in her throat.

Beside her, Miller leaned across his harness, his eyes wide. "Commander... what is that? Where did that software come from?"

"It came from Houston," Ross said, her hand reaching for the emergency manual engine-arm toggle switch. "And it’s the only thing standing between us and thirty miles of lunar granite."

She flipped the red safety guard and shoved the toggle upward:

`ARM ENGINES: CONFIRMED`  
`BURN AUTHORIZATION: GRANTED`  

---

### The Forty-Nine-Point-Five Burn

At 20:18:02 UTC, four hundred kilometers above the cratered northern limb of the Moon, the reaction control thrusters of the Orion service module fired.

Four sharp, clean bursts of monomethylhydrazine and nitrogen tetroxide erupted into the vacuum: *CH-CH-CH-CH-CH*.

The spacecraft shuddered. Through the forward viewport, the stars rotated smoothly as the vehicle pivoted forty-two degrees off its velocity vector, pointing its tail toward the dark lunar horizon.

Then the four primary auxiliary thrusters ignited with a steady, rumbling push: eighteen point four seconds of sustained, precise acceleration.

Inside the cabin, the crew was pressed gently back into their couches—a tiny fraction of a G, but after seventy hours of weightlessness, it felt like the firm hand of life pulling them back from the edge of an abyss.

The burn shut down with a crisp metallic snap:

```
[BURN-LOG] TCM-3 EXECUTION COMPLETE.
[BURN-LOG] DELTA-V DELIVERED: 49.524 M/S (ERROR: 0.004 M/S).
[BURN-LOG] POST-BURN ORBIT DETERMINATION:
[BURN-LOG] NEW PERILUNE ALTITUDE: +112.44 KILOMETERS.
[BURN-LOG] LUNAR IMPACT AVERTED.
[BURN-LOG] FREE RETURN TRAJECTORY: CONFIRMED.
[BURN-LOG] RETURN TO EARTH: T+148 HOURS NOMINAL.
```

In Houston, sixty flight controllers stood up from their consoles, cheering, shouting, hugging each other, throwing telemetry log sheets into the air.

Michael Hayes sat in his chair, his hands trembling slightly as he lowered his headset to the desk. He turned his head and looked at Elena Rostova.

"Call him," Hayes said quietly. "Call Ryan Vance."

Elena walked out of the roaring control room, stepped into the quiet carpeted corridor, and pulled her satellite phone from her pocket.

Three thousand miles away, in the freezing limestone mine of Giles County, Ryan Vance was sitting on his yellow plastic crate, watching the laser fringe of the Sagnac interferometer.

The phone chirped.

Ryan answered. "Vance."

"Perilune is one hundred and twelve kilometers, Ryan," Elena said, her voice breaking into quiet, unashamed tears. "They made it. The integer filter held. All four of them are coming home."

Ryan closed his eyes, listening to the hum of the cooling fans in the deep silence of the mountain.

"Good," Ryan said softly. "Now tell them to build the ship for Callisto."
"""

for fname, content in [
    ("Chapter_06_The_Negative_Variance.md", CH6_FULL),
    ("Chapter_07_Dead_Mans_Trajectory.md", CH7_FULL),
    ("Chapter_08_Light_Across_the_Blind_Spot.md", CH8_FULL),
]:
    p = os.path.join(MANUSCRIPT_DIR, fname)
    with open(p, "w") as f:
        f.write(content.strip() + "\n")
    words = len(content.split())
    print(f"Deepened {fname}: {words} words")
