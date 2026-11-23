# CHAPTER SIX
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
