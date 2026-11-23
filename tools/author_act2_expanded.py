#!/usr/bin/env python3
"""
Deep literary authoring of Act II: Chapters 5-8.
Author: Todd Hendrixx
Target: ~2,200 words per chapter (~8,800 words total for Act II).
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

CH5_FULL = r"""# CHAPTER FIVE
## Flare State
### Translunar Coast & The Blue Marble

The translunar injection burn had been textbook.

At 22:14:08 UTC on November 8, 2026, the four RL10-B-2 cryogenic engines of the Space Launch System Exploration Upper Stage had ignited over the southern Indian Ocean, firing for eight minutes and twenty-two seconds through the orbital darkness. The burn had delivered 3,048.6 meters per second of forward delta-V, accelerating the three-hundred-ton stack through the translunar injection corridor and flinging the Orion spacecraft into the deep cislunar void.

Inside the pressurized command module of Orion, Commander Sarah Ross floated above the forward pilot's station, watching the Earth retreat through the three-pane fused-silica viewports.

The blue marble of the home world was visibly shrinking. Its curved rim was etched with the paper-thin cyan haze of the atmosphere, receding into the velvet blackness by three thousand meters every second. At forty-two years old, Sarah had logged over two thousand hours in carrier-capable strike fighters as a naval test pilot before selection to the astronaut corps. She had the cool, resting pulse of someone who had survived engine flameouts and night deck landings in high sea states, but staring into the cislunar dark, she felt the ancient, biological dread of leaving the protective womb of the home planet.

Her three children were asleep in their beds in Pensacola, Florida. Her husband, an aeronautical engineer at Eglin Air Force Base, had squeezed her hand through the quarantine glass in Houston three days ago and told her not to look at the numbers. But Sarah was an engineer; she always looked at the numbers.

Beside her in the center couch, Pilot David Miller verified the primary flight displays. David was thirty-six, an Air Force colonel with a doctoral degree in astrodynamics from MIT. His wife was seven months pregnant with their first daughter back in Corpus Christi.

"Stage separation confirmed nominal," Miller said, his voice level and methodical. "EUS disposal burn confirmed: the spent stage has entered a heliocentric disposal trajectory. Solar array wings deployed and sun-tracking. All four wings generating twelve point four kilowatts. Reaction control system pressurized to two hundred and eighty bar of gaseous helium. We are coasting."

In the lower equipment bay beneath the flight deck, Mission Specialists Robert Thorne and Dr. Lin Liu were stowing the launch umbilical lines and preparing the autonomous biological radiation experiment racks. Lin Liu, an astrophysicist and cellular biophysicist who had spent five years studying cellular DNA repair mechanisms in low-Earth orbit, was securing the passive thermoluminescent dosimeter badges along the cabin bulkheads.

"Cabin atmosphere is nominal," Liu called up through the access hatch. "Twenty-one percent oxygen, seventy-nine percent nitrogen at ten point two psi. Carbon dioxide scrubbers sitting at zero point two millimeters of mercury. The bio-racks are locked down."

For thirty-six hours, the flight was what NASA flight controllers loved most: completely boring.

The spacecraft was drifting outward along a coasting ellipse toward the Moon, three hundred and ten thousand kilometers from Earth, moving at slightly under one kilometer per second relative to the Earth-Moon barycenter. The cabin hummed with the constant, reassuring drone of cabin avionics fans, the rhythmic clicking of the carbon-dioxide scrubbers, and the low hiss of the air recirculators.

Then, at 14:22 UTC on November 10, the sun decided to remind four human beings that space was not a quiet void.

---

### The Coronal Eruption

Ninety-three million miles away, an immense magnetic knot in active region AR3842—a sunspot complex four times the diameter of Earth—snapped.

The reconnection event released the equivalent of one billion one-megaton hydrogen bombs in less than forty seconds. It was an **X8.4 solar flare**, one of the most violent stellar eruptions recorded in the twenty-first century.

A blinding flash of extreme ultraviolet and soft X-ray radiation washed over the inner solar system at the speed of light, ionizing Earth’s upper ionosphere and causing immediate high-frequency radio blackouts across Europe and North America.

Behind the light came the monster: a coronal mass ejection consisting of billions of tons of magnetized solar plasma, accompanied by a relativistic shockwave that accelerated protons to eighty percent of the speed of light.

Inside the Orion cockpit, the radiation dosimeters did not register a gradual rise. They screamed.

A high-pitched acoustic alarm cut through the ambient avionics hum: *BEEP-BEEP-BEEP-BEEP*.

The primary caution-and-warning matrix on Ross’s central console lit up in bright amber:

```
[CAUTION] SPE EVENT DETECTED: GOES-19 PROTON FLUX > 10,000 PFU
[CAUTION] ONBOARD DOSIMETER RATE: 14.8 RAD/HR AND CLIMBING
[WARNING] FLIGHT RULE 2-DELTA: CREW RETREAT TO SHELTER REQUIRED
```

"Solar flare," Ross said, her voice dropping into the flat, clipped cadence of a combat test pilot. "Miller, Thorne, Liu—abort scheduled tasks. Helmets on, grab your emergency water jackets. We are moving into the storm shelter."

The crew didn't ask questions. They knew the numbers.

At fourteen rads per hour of unshielded flux, a human being receives a lethal dose of radiation in less than thirty hours. Acute radiation sickness—nausea, intestinal hemorrhage, bone marrow destruction—would begin within six hours.

The four astronauts scrambled down from their flight couches into the central floor well between the equipment lockers. They pulled dense Nomex-and-polyethylene radiation blankets from the stowage bays, stacking the spacecraft’s twenty-liter contingency water containers around them to create a makeshift hydrogen-rich radiation bunker.

They sealed the thermal curtain above their heads, wedging themselves shoulder-to-shoulder in the dark, breathing through their oxygen masks, listening to the metallic creak of the hull as the high-energy proton storm pounded the outer spacecraft skin.

In the dark of the shelter, strange optical phosphenes flickered across their vision: tiny, brilliant flashes of blue-white light caused by relativistic protons slicing through the vitreous humor of their eyeballs and striking their retinas directly.

"Taste that?" Thorne whispered through his comm mic.

"Metallic," Lin Liu said, her teeth clenched. "Like sucking on a copper penny. That’s the ozone and free radicals forming in your saliva from secondary ionization."

---

### The Blinding of the Eyes

Outside the pressurized hull, Orion’s primary sensory systems were fighting for their lives.

To navigate autonomously across cislunar space, the spacecraft relied on two primary optical systems: two high-resolution Star Trackers mounted on the service module, and an Optical Navigation (OpNav) camera mounted on the command module forward bulkhead.

The star trackers were designed to match patterns of distant stars against an onboard catalog of fifteen thousand astronomical coordinates, determining the spacecraft’s three-axis attitude to within two arcseconds.

As the relativistic solar proton storm struck the star tracker CCD sensor chips, the high-energy particles slammed through the protective borosilicate glass windows. Each proton created a miniature shower of secondary ionization electrons in the silicon, producing bright, spurious pixel clusters known as Cherenkov transients.

On the avionics bus, the star tracker software attempted to process the image:

```
[STR-A] Frame 4182: Detected 1,842 bright centroids.
[STR-A] Star Pattern Match: FAILED (Catalog limit: 60 stars).
[STR-A] Noise Rejection Gate: OVERRUN. False Centroids: 98.4%.
[STR-A] Attitude Lock: LOST. Entering Coast-Attitude Mode.
[STR-B] Frame 4182: Sensor Saturated. Latch-up Protection Triggered.
```

Within ninety seconds of the proton front's arrival, both primary star trackers were completely blind.

At the same time, the solar radio burst—a ferocious, broadband blast of synchrotron radio noise generated by relativistic electrons spiraling through the sun's magnetic field—swept across the Earth-Moon axis.

On the Earth's surface, the 70-meter parabolic dish of Deep Space Station 43 at the Canberra Deep Space Communication Complex in Australia was pointed at Artemis-7.

At 14:26 UTC, the signal-to-noise ratio on the spacecraft’s high-gain S-band down-link dropped off a cliff. The carrier lock dropped from plus thirty-two decibels down to minus four decibels, vanishing beneath the deafening solar hiss.

The station operator at Canberra hit his voice switch:

"Houston, Canberra DSN. We have lost RF carrier lock on Artemis-7. Solar radio flux index is sitting at five thousand solar flux units. The S-band transponder is drowned in solar noise. We are blind on ground tracking."

In the dark of the storm shelter, three hundred and ten thousand kilometers from home, Sarah Ross watched a single red LED blinking on her wrist telemetry display:

`COMM: CARRIER LOST`  
`ATTITUDE: DEGRADED (IMU OPEN LOOP)`  
`RANGE TO PERILUNE: 68,400 KM`  
`TIME TO IMPACT: 28 HOURS 14 MINUTES`  

---

### The Drifting Inertial Platform

Inside the avionics bay, the Honeywell Miniature Inertial Measurement Unit (MIMU) was spinning its three ring-laser gyroscopes.

With the star trackers offline and the ground tracking antennas drowned in solar radio noise, the spacecraft had no external frame of reference. It had become a closed, isolated box drifting through space, forced to infer its orientation and position by integrating the tiny accelerations and angular rates detected by its internal sensors.

In atmospheric flight, a ring-laser gyro is a precision instrument. In deep space, over hours of uncorrected coasting, it is an engine of creeping error.

The gyro drift rate was rated at 0.005 degrees per hour. Over thirty minutes, that error was negligible. Over twenty-four hours, an angular drift of one-tenth of a degree in pointing vector translates into an error of hundreds of kilometers when projecting an orbital trajectory across the cislunar void.

Even worse was the unmodeled acceleration.

As the solar proton storm struck the massive thirty-meter span of Orion’s four solar array wings, the flux of charged particles imparted a continuous, asymmetric mechanical pressure:

$$F_{\text{solar}} \approx 4.8 \times 10^{-5} \text{ Newtons}$$

It was a force no greater than the weight of a postage stamp. But sustained over ten hours against an eighty-ton vehicle, that minute photon and proton pressure produced an unmeasured velocity perturbation of 0.22 meters per second.

In low-Earth orbit, a quarter of a meter per second is an inconsequential drift.

In the chaotic, three-body gravitational landscape of cislunar space—where the gravitational fields of the Earth and the Moon pull against each other along the razor-thin saddle of the Lagrange manifolds—an error of twenty centimeters per second is the difference between a triumphant orbital insertion and a lethal, high-velocity impact on the lunar surface.

---

### The Manual Sextant & The Ghost of Apollo

At 18:00 UTC, Sarah Ross could no longer stay in the floor well.

She pushed back the heavy Nomex blankets, ignoring the sharp prickle of secondary ionization in her skin, and floated up to the command couch.

"Commander, the dosimeter rate is still seven rads an hour," Lin Liu warned from the shelter hatch.

"If we don't know our state vector, the dosimeter doesn't matter," Ross answered. "We hit the lunar crust in twenty-four hours."

She reached above her helmet to the secondary optical alignment hatch—a recessed, five-inch circular quartz viewport equipped with a manual optical reticle and an Apollo-heritage optical alignment sextant. In the 1960s, Jim Lovell and Buzz Aldrin had used optical space sextants to measure the angular separation between stars and lunar landmarks, calculating state vectors with paper charts and pencil.

Sarah pressed her right eye against the rubber eyecup.

The scene through the sextant was a nightmare of chaotic scintillation. The solar proton flux was lighting up the quartz glass with microscopic phosphorescent sparks. Outside, the Moon was a massive, blinding crescent of scarred gray basalt, but the limb of the lunar disk was shimmering with thermal and optical distortion.

"Miller," Ross called out, her fingers adjusting the fine-vernier micrometer drum. "Call out the Apollo benchmark stars. Can you see Acrux or Canopus?"

Miller squinted through the side viewport with handheld binoculars. "Negative. The solar coronal glow is scattering across the entire forward hemisphere. Everything within thirty degrees of the Sun is washed in white flare glare."

Ross tried to align the crosshair with the rim of the crater Copernicus.

Every time Orion’s reaction control thrusters pulsed—tiny, automated firings of cold gaseous nitrogen to keep the vehicle within its deadband attitude limit—the crosshairs in the reticle jumped by forty arcseconds.

In low-Earth orbit, a human navigator can average out ten readings and find an orbital plane within three nautical miles. But here, at the weak stability boundary, an error of forty arcseconds at a distance of sixty thousand kilometers represents an uncertainty of twelve kilometers in position.

And the lunar capture corridor had a total tolerance of less than four kilometers.

Sarah stepped back from the eyepiece, breathing hard. Her right eye burned from the glare.

"Manual sighting cannot solve this," she said, her voice dropping into a flat, grim whisper. "The non-linear gradient is too steep. We are falling down a gravitational funnel, and our eyes are full of static."
"""

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

### The Seven-Watt Receipt

Hayes raised a hand, cutting off the argument. The entire room went dead silent. The only sound was the faint hum of the air handlers and the distant click of a keyboard.

"Elena," Hayes said slowly, turning his chair toward her. "You flew to Ohio this morning without authorization. You commandeered Chamber B at Plum Brook. What did you bring back?"

Elena plugged the thumb drive into the auxiliary workstation terminal on the Flight Director’s console.

"I brought back CislunarOS," she said.

She brought up the Plum Brook qualification report on the auxiliary screen:

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

### The Needle of Light

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
[OPT-RX] Receiving: cislunar_os_core.elf (482 KB)
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

print("Updating Act II chapters...")
for fname, content in [
    ("Chapter_05_Flare_State.md", CH5_FULL),
    ("Chapter_06_The_Negative_Variance.md", CH6_FULL),
    ("Chapter_07_Dead_Mans_Trajectory.md", CH7_FULL),
    ("Chapter_08_Light_Across_the_Blind_Spot.md", CH8_FULL),
]:
    p = os.path.join(MANUSCRIPT_DIR, fname)
    with open(p, "w") as f:
        f.write(content.strip() + "\n")
    words = len(content.split())
    print(f"Updated {fname}: {words} words")
