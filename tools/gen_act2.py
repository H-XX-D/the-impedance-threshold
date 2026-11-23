#!/usr/bin/env python3
"""
Generate Act II: Chapters 5-8 and Dossier II from scratch.
Author: Todd Hendrixx
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

CH5 = r"""# CHAPTER FIVE
## Flare State

The translunar injection burn had been textbook.

At 22:14 UTC on November 8, 2026, the four RL10 engines of the Space Launch System Exploration Upper Stage had fired over the Indian Ocean, accelerating the spacecraft *Prometheus*—carrying Commander David Cole, Pilot Maya Lin, and Mission Specialists Henderson and Ruiz—out of low Earth parking orbit onto a high elliptical free-return corridor toward the Moon.

Inside the pressurized cabin of the Orion command module, the ride had settled into the quiet, rhythmic humming of avionics cooling loops and cabin scrubbers. Through the thick quartz-borosilicate panes of the forward hatch window, the Earth hung like a curved crescent of blue marble and bright white cloud bands, shrinking steadily as the velocity vector carried them toward translunar coast at ten point eight kilometers per second.

Forty-eight hours out from Earth, at 00:02 UTC on November 9, the Sun broke the silence.

Active Region 3842—a complex, twisted magnetic knot of sunspots rotating across the solar equator—underwent a catastrophic magnetic reconnection. A massive X8.4 solar flare erupted into the interplanetary void, accompanied by a coronal mass ejection traveling at twenty-two hundred kilometers per second.

In Mission Control, Houston, eighty thousand miles behind the spacecraft, the solar alert chimes cut through the flight loop:

`SOLAR_ACTIVITY_ALERT: GOES-19 X-RAY FLUX EXCEEDS 8.4e-4 W/m^2`  
`RADIO_BURST_DETECTION: TYPE_IV CONTINUUM EMISSION CONFIRMED`  
`FREQUENCY_BAND: 1.0 GHz TO 15.0 GHz [BROADBAND NOISE STORM]`  
`ESTIMATED_PROTON_ARRIVAL: T_MINUS_18_MINUTES`  

In Building 30, Flight Dynamics Officer Marcus Thorne ripped off his reading glasses and leaned toward his primary console.

"Flight, FIDO," Marcus called over the flight director's loop.

"Go ahead, FIDO," Flight Director Sarah Lin responded, her voice calm and level.

"The radio burst is centered near six degrees off the solar disk," Marcus said, his eyes tracking the RF waterfall display. "Because of the current orbital alignment—new Moon was three days ago—the line of sight from Earth to *Prometheus* passes within seven degrees of the Sun. Deep Space Network Canberra, DSS-43, is getting swamped in antenna sidelobes. Receiver noise floor just jumped twenty-eight decibels. Downlink SNR is collapsing."

"Can we hand off to Goldstone?" Sarah Lin asked.

"Goldstone hasn't acquired yet; their horizon limit is twelve minutes out," Marcus replied. "And Madrid is setting. DSN Canberra is our only active carrier link, and their receiver front-ends are saturating on solar synchrotron emission. We are entering carrier loss."

On the main tracking map at the front of the control room, the green telemetry vector for *Prometheus* blinked once, flickered amber, and froze:

`CARRIER_LOCK: DROPPED [DSS-43 S-BAND DOWNLINK UNLOCKED]`  
`TIME_TO_TCM3_IGNITION: 04_HOURS_10_MINUTES`  
`PAYLOAD_STATUS: AUTONOMOUS_SCREENED_COAST`  

Ten minutes later, the first wave of relativistic solar protons arrived.

They traveled at a third of the speed of light, penetrating the spacecraft's outer micrometeoroid shielding. On the optical focal planes of *Prometheus*’s twin star trackers, the high-energy protons ionized silicon pixels, producing hundreds of false-star flashes across every charge-coupled image frame.

Inside the avionics bay, the flight software—GEONS Build 4.1.2, executing on the primary Honeywell RAD750 processor—woke up to process its scheduled optical state update.

It looked out at the sky through a shower of artificial lightning.
"""

CH6 = r"""# CHAPTER SIX
## The Negative Variance

Inside the pressurized avionics vault of *Prometheus*, the primary Honeywell flight computer was operating under an architectural death sentence.

Every ninety seconds, the flight executive invoked subroutine `GEONS_EKF_UPDATE`.

Under nominal flight conditions, the star trackers took star-pair angular separation bearings, while the forward optical horizon scanner tracked the bright limb of the Moon against the black background of space. The software compared the measured unit vectors $\mathbf{z}_k$ against its propagated prediction $h(\mathbf{x}_k)$, forming the innovation vector:
$$\mathbf{y}_k = \mathbf{z}_k - h(\mathbf{x}_k)$$

Then it evaluated the Normalized Innovation Squared (NIS):
$$\text{NIS} = \mathbf{y}_k^T S_k^{-1} \mathbf{y}_k$$
where $S_k = H P_{k|k-1} H^T + R$ was the innovation covariance matrix.

From 00:24 UTC to 04:03 UTC, as the solar proton storm intensified, the star tracker’s image processor was overwhelmed by ionizing radiation spikes. In three hours and thirty-nine minutes, the algorithm generated **two hundred and nineteen consecutive optical candidate fixes**.

Every single one of them was corrupted by proton hits.

At first, the filter behaved exactly as its designers had intended. The innovation vectors were huge—forty to two hundred kilometers in magnitude. The calculated NIS values exceeded ten thousand. The filter rejected fix after fix, discarding the corrupted measurements:

```
00:24:12 UTC - REJECT: FIX 001 - NIS = 12,418.2 > GATE 35.0
00:25:42 UTC - REJECT: FIX 002 - NIS = 9,841.0 > GATE 35.0
...
04:02:21 UTC - REJECT: FIX 218 - NIS = 14,102.8 > GATE 35.0
```

Two hundred and nineteen consecutive rejections.

---

### The Rank Collapse

In classical textbook Kalman filtering, rejecting bad measurements protects the state vector. But in reality, an estimator that rejects all measurements does not stand still.

It propagates by prediction alone:
$$P_{k+1|k} = \Phi_k P_{k|k} \Phi_k^T + Q$$

The spacecraft was hurtling through the non-linear gravitational neck between Earth and Moon. The state transition matrix $\Phi_k$ stretched the uncertainty along the approach trajectory, while the transverse uncertainties received zero empirical updates.

And the process noise matrix $Q$ had been configured with an ultra-conservative diagonal acceleration variance:
$$q_{ii} = 1.0 \times 10^{-12} \text{ m}^2/\text{s}^4$$

On a sixty-four-bit workstation, the matrix would have retained its mathematical properties. But inside the Honeywell RAD750, the covariance entries were carried in IEEE 754 single-precision floating point. With only twenty-four bits of mantissa, small cross-axis variances were repeatedly added to huge along-track variances.

The lower bits rounded off into the bit-bucket on every cycle.

At 04:03:51 UTC, the eigenvalues of the three-by-three position covariance sub-matrix reached:
$$\lambda_1 = 4.1 \times 10^6 \text{ m}^2$$
$$\lambda_2 = 3.8 \text{ m}^2$$
$$\lambda_3 = -0.6 \text{ m}^2$$

A negative eigenvalue in a covariance matrix is a mathematical impossibility. It means the estimator believes the variance of its position along the minor axis is less than zero.

The matrix had collapsed toward rank one. It had ceased to be positive-definite.

At 04:03:52 UTC, fix number two hundred and twenty arrived. A proton hit the lunar limb sensor array, creating an apparent limb offset with an innovation magnitude $\|\mathbf{y}_k\| = 221.8\text{ km}$.

The subroutine computed the innovation covariance $S_k = H P H^T + R$. Because $P$ was indefinite, $S_k$ inherited the negative eigenvalue. The single-precision matrix inversion solve returned:

$$\text{NIS} = \mathbf{y}_k^T S_k^{-1} \mathbf{y}_k = -287.4$$

Then the flight software checked its acceptance gate:

```c
// UNINTENDED DEFECT: ONE-SIDED NIS GATE IN GEONS BUILD 4.1.2
if (nis <= NIS_GATE_35) {
    joseph_update(&x, &P, &K, &y);
}
```

Negative two hundred and eighty-seven is less than thirty-five.

The one-sided gate evaluated to **TRUE**.

The filter concluded that the measurement was extraordinarily accurate. Subroutine `joseph_update` executed, multiplying the 221-kilometer false innovation by an invalid Kalman gain.

In a single computational clock cycle, the estimated state of *Prometheus* jumped **two hundred and twenty-one kilometers sideways**. The velocity vector was instantly corrupted by thirty-eight meters per second, and the diagonal velocity variance collapsed to negative numbers.

Ten minutes later, the automated sequencer began Trajectory Correction Maneuver 3 (TCM-3). Believing it was radically off-course, the autopilot re-targeted the main engine burn to 41.4 meters per second to compensate for a trajectory error that existed only in its corrupted memory.

At 04:12:44 UTC, the auxiliary service module engine ignited.

Twenty-eight seconds into the burn, the carrier-loss watchdog tripped. The delivered delta-v was twenty-eight point eight meters per second.

The resulting trajectory was lethal. Perilune—the closest approach to the lunar surface—dropped from a safe one hundred and ten kilometers altitude to **negative thirty-eight point five kilometers**.

Thirty-eight kilometers below the solid basalt farside surface of the Moon.

And behind the burn, having detected the numerical inconsistency in its own registers, the Honeywell executive latched into emergency backup shutdown:

`AVIONICS_FLIGHT_EXECUTIVE: HARDWARE_LOCKOUT`  
`FAULT_CODE: 0x7E14 [PROTECTIVE_SCREENED_COAST]`  
`THRUST_AUTHORITY: REVOKED`  
`STATUS: PASSIVE_BALLISTIC_IMPACT_COURSE`  
"""

CH7 = r"""# CHAPTER SEVEN
## Dead Man's Trajectory

In Mission Control, Houston, the room was dead silent except for the low murmur of cooling fans and the rhythmic clicking of keyboards.

At 04:22 UTC, forty-five minutes before lunar farside occultation, the Deep Space Network station at Goldstone, California, finally punched through the edge of the solar sidelobe interference, reacquiring a fragile eight-kilobit telemetry carrier from *Prometheus*.

Marcus Thorne stared at the incoming state packet on his console. His face went gray.

"Flight, FIDO," Marcus said, keeping his voice strictly level. "We have the state vector from the post-burn telemetry downlink."

Sarah Lin stepped down from the Flight Director’s console, standing directly behind Marcus’s left shoulder. "Give it to me, Marcus."

"TCM-3 ignited at zero-four-twelve," Marcus said, pointing a finger at the raw hexadecimal memory dump scrolling across his screen. "Delivered twenty-eight point eight meters per second before the watchdog cut the engine. The primary GEONS filter committed a corrupted state update prior to ignition. Look at the variance registers: velocity covariance diagonal is negative. The flight computer has latched into `PROTECTIVE_SCREENED_COAST`. Fault code `0x7E14`."

"What does that mean for the orbit?" Sarah asked.

"It means the primary GNC has revoked its own thrust authority," Marcus replied. "The engine is locked out. And the trajectory... Flight, the burn was executed in the wrong vector. Current perilune is calculated at negative thirty-eight point five kilometers. Time of impact is zero-five-thirty-six UTC. Over the farside highlands, between Daedalus crater and the South Pole-Aitken basin."

A heavy, suffocating silence settled over the row of consoles.

"How long do we have before occultation?" Sarah Lin asked.

"Forty-two minutes," Marcus answered. "Once the vehicle passes behind the lunar western limb at zero-five-zero-five, we lose direct line-of-sight communications with Earth for forty-six minutes. If we don't execute a correction burn before occultation, they hit the ground while in the radio shadow."

"Can we command a manual open-loop burn from Houston?"

Marcus shook his head. "We don't have a reliable state vector, Flight. Because GEONS corrupted its registers, the onboard inertial platform doesn't know which way the spacecraft is pointed to within fifteen degrees. If we upload an open-loop burn based on DSN two-way Doppler alone, the antenna pointing error will misalign the thrust vector. An open-loop burn has less than an eight percent probability of clearing the terrain. It’s a dead man's burn."

---

### The Parachute

Standing two consoles over, Dr. Elena Rostova leaned into her headset. Her knuckles were white where she gripped the steel edge of the terminal bay.

"Sarah," Elena called over the private director's loop. "Listen to me."

Sarah Lin turned to look at her. "Elena, if you have an option, speak."

"We have a shadow payload on *Prometheus*," Elena said.

The room seemed to pause.

"The experimental avionics box," Marcus Thorne interjected, turning around in his swivel chair. "The Jetson board in Payload Bay 4. Under Safety Protocol 14-B."

"Safety Protocol 14-B was an observational experiment, Elena," Sarah Lin said, her tone sharp with institutional warning. "It was approved by the Flight Review Board to log passive telemetry. It has zero Level-1 flight software certification. It is not connected to the primary thruster bus."

"It *is* connected to the bus," Elena said, stepping toward the center aisle. "Under the protocol we qualified at Plum Brook, the shadow payload is wired to the auxiliary thruster driver through an optical solid-state relay. The primary Honeywell processor holds command authority by default. But the relay was built with an emergency hardware override: if Houston sends an authenticated cryptographic command packet—`STOP`, `TAKEOVER`, `STAGE`, `COMMIT`—the relay disconnects the Honeywell and gives thruster firing authority to the shadow executive."

"And what is running on that shadow board?" Sarah Lin asked.

"ArgonautOS," Elena said. "Ryan Vance’s square-root relational stack. It doesn't use GEONS. It doesn't invert the covariance matrix. It carries its uncertainties in square-root Cholesky form, and it gates its measurements with QR factorization. It cannot produce a negative variance."

Marcus leaned forward, pulling up the shadow telemetry channel on a secondary display: `AUX_PL_04_HEALTH`.

The screen blinked:

```
[AUX_PAYLOAD_04] CISLUNAR-OS BUILD 7.0.1 (cFS DRACO)
HARDWARE: JETSON ORIN NANO [7-WATT LOW-POWER MODE]
PROCESSOR LOAD: 18.4% | MEMORY USED: 21,308 KiB
ESTIMATOR STATUS: SRIF ACTIVE | COVARIANCE: POSITIVE-DEFINITE
RECONSTRUCTED STATE: SELENOCENTRIC JACOBI RELATIONAL
CALCULATED PERILUNE: -38.48 KM (MATCHES DSN GROUND TRACK)
PROPOSED RECOVERY PLAN: 49.5 M/S RETROGRADE CORRECTION
DIVERSE CARTESIAN VERIFIER STATUS: PASS_CONDITIONAL
TIME TO OCCULTATION: 38 MINUTES 12 SECONDS
```

Marcus let out a low whistle. "Look at the perilune calculation, Flight. Vance's seven-watt board figured out the impact trajectory entirely on its own, fifteen minutes before Goldstone reacquired the link."

Sarah Lin stared at the numbers. She looked at Marcus, then at Elena Rostova.

"If this board fails, Sarah," Elena said quietly, "they impact the farside in fifty minutes. If we do nothing, they impact the farside in fifty minutes. The Honeywell has locked itself in a screen coast and will not burn. Vance's board is the only clock on that ship that isn't lying to itself."

Sarah Lin took a slow breath. She reached for the red master console switch and flipped the plastic safety guard.

"FIDO, prepare the cryptographic command string," Sarah Lin ordered. "Authorize emergency bus takeover under Flight Director Authority Directive Nine. We are giving the ship to the seven-watt board."
"""

CH8 = r"""# CHAPTER EIGHT
## Light Across the Blind Spot

The radio link died at 04:46 UTC.

As the spacecraft rotated into attitude, the high-gain dish on *Prometheus* lost its fringe lock on Goldstone. Solar radio noise from the flare surged again across the S-band spectrum, a roaring wall of synchrotron static that smothered the DSN receivers.

In Mission Control, the uplink carrier status turned crimson:

`UPLINK STATUS: FAILED [RF CARRIER TIMEOUT - 0x00FF]`  
`COMMAND REJECTED: UNABLE TO SYNCHRONIZE HMAC SESSION`  
`TIME TO LUNAR OCCULTATION: 18 MINUTES`  

"We lost RF uplink," Marcus Thorne called out, his voice tightening. "The solar burst is at peak flux. We can't push the `TAKEOVER` key over S-band."

Elena Rostova grabbed the flight loop handset. "Switch to optical. Mount Stromlo."

Across the world, on a wooded ridge outside Canberra, Australia, the night sky was cold, crystal clear, and completely dark. The laser communications ground terminal at the Mount Stromlo Observatory—a one-meter coudé telescope fitted with high-speed adaptive optics—was pointed toward the silver crescent of the Moon hanging forty degrees above the Pacific horizon.

Unlike radio waves, which were scrambled and swamped by the broad synchrotron noise of the solar flare, the optical communications channel operated at an infrared wavelength of **1,550 nanometers**—a sharp, monochromatic optical carrier immune to radio-frequency plasma turbulence.

"Mount Stromlo has acquisition of Lunar Gateway's optical transponder," Elena announced, reading the laser relay status stream. "Gateway is tracking *Prometheus*’s optical terminal on its auxiliary crosslink. We have an unbroken infrared photon path: Houston to Stromlo via terrestrial fiber; Stromlo to Gateway via optical uplink; Gateway to *Prometheus* via crosslink."

"Laser line of sight is clear," Marcus confirmed. "Data rate is one point two megabits. Clean bit-error rate: $10^{-9}$."

"Upload the keys," Sarah Lin commanded.

Marcus Thorne entered his authorization sequence. On his terminal, three 512-byte cryptographic packets were signed with NASA's master flight operations private key:

```
[AUTHENTICATED FLIGHT DIRECTIVE]
TARGET: AUX_PAYLOAD_04 (JETSON ORIN NANO)
COMMAND_1: 0xAA01 [AV_HOST_TAKEOVER_PRIMARY_GNC]
COMMAND_2: 0xBB04 [STAGE_RECOVERY_BURN_49.5_MS]
COMMAND_3: 0xCC09 [COMMIT_MISSION_PHASE_EXECUTION]
HMAC-SHA256: 4f8a9e71b2d019a3c8e47f20b...
TRANSMITTING VIA OPTICAL LASER RELAY...
```

The command pulse left the coudé telescope at Mount Stromlo as a burst of invisible infrared photons, crossing four hundred thousand kilometers of vacuum in one point two eight seconds. It struck the receiver optics on Lunar Gateway, bounced through the high-speed crosslink, and hit the receiver photodiode on the auxiliary bay of *Prometheus*.

---

### The Relational Recovery

Inside Payload Bay 4, the Jetson Orin Nano processed the authenticated packet.

The solid-state optical relay clicked. The primary Honeywell flight executive was gracefully disarmed, its corrupted registers isolated from the thruster drivers.

`CISLUNAR-OS EXECUTIVE: COMMAND AUTHORITY ACCEPTED`  
`HOST MODE: AUTO [AUTONOMOUS TRAJECTORY RECOVERY ACTIVE]`  
`ESTIMATOR: SQUARE-ROOT INFORMATION FILTER`  
`MEASUREMENT UPDATE: OPTICAL LIMB FIX VERIFIED (NIS = 4.12)`  
`CALCULATED BURN TARGET: RETROGRADE 49.52 M/S`  
`DIVERSE CARTESIAN VERIFIER: PASS_CONDITIONAL`  
`PREPARE_BEFORE_ISSUE: JOURNAL WRITTEN TO DURABLE STORAGE`  
`IGNITION COUNTDOWN: T-MINUS 00:30 SECONDS`  

In the crew cabin of *Prometheus*, Commander David Cole watched the main instrument panel reboot. The red warning banners across the primary displays vanished, replaced by the clean, unfamiliar monospace typography of ArgonautOS:

```
[RELATIONAL GNC ACTIVE]
MISSION: LLO INSERTION TRAJECTORY RESTORATION
PLANNED DELTA-V: 49.52 M/S | DURATION: 48.6 SECONDS
TARGET PERILUNE: 112.4 KM (SAFE ORBITAL INSERTION)
AUTOPILOT: LOCKED
```

"Houston, *Prometheus*," Cole’s voice crackled through the optical audio channel, calm and steady. "The board has the ship. Autopilot is slewing to burn attitude. RCS firings are clean."

At 04:48:30 UTC, twenty minutes before entering the lunar shadow, the auxiliary reaction control thrusters fired in unison.

A steady, continuous acceleration pressed the four astronauts back into their couches. Outside the windows, the silver craters of the lunar limb slid steadily past as the 49.5 m/s retrograde burn canceled the lethal descent velocity.

Forty-eight seconds later, the thrusters shut down cleanly.

On the navigation display, the revised orbital elements locked in:

```
PERILUNE ALTITUDE: 112.42 KM
APOLUNE ALTITUDE:  108.19 KM
ORBITAL PERIOD:    118.4 MINUTES
TRAJECTORY STATUS: STABLE CIRCULAR LOW LUNAR ORBIT
ESTIMATOR UNCERTAINTY (3-SIGMA): 18.2 METERS
COVARIANCE EIGENVALUES: ALL POSITIVE REAL
```

At 05:05 UTC, *Prometheus* slipped smoothly over the western limb of the Moon, passing into the silent, star-strewn darkness of the farside.

Not on an impact trajectory into the crushed basalt of the Daedalus basin. But in a stable, hundred-kilometer parking orbit, riding the natural curvature of relations, sustained by seven watts of arithmetic that had refused to lie.
"""

DOSSIER2 = r"""# INTER-ACT DOSSIER II
## The Artemis-7 Cislunar Anomaly & Autonomous Recovery
### Document Classification: NASA Mishap Investigation Board (MIB) Interim Technical Report
#### Mission Designation: Artemis-7 (Spacecraft *Prometheus*) | Date of Incident: November 9, 2026

![Artemis-7 (Prometheus) Cislunar Anomaly & Autonomous Recovery](assets/plate_03_dossier_2_artemis_recovery.png)

### 1.0 SEQUENCE OF EVENTS & TELEMETRY TIMELINE

*Sequence of Events Summary: 00:02 UTC X8.4 flare and long-duration solar radio burst, Moon about 6 degrees from the Sun; 00:03 UTC DSS-43 downlink lost in sidelobe solar noise; 00:21 UTC solar proton onset; 00:24 to 04:03 UTC 219 consecutive proton-corrupted optical fixes rejected by GEONS; 04:03:51 UTC GEONS accepts a corrupted fix on a negative NIS (state jump 221.8 km); 04:04 UTC TCM-3 re-targeted to 41.4 m/s; 04:12:40 UTC ground drops uplink carrier; 04:12:44 UTC TCM-3 ignition; 04:13:12 UTC carrier-loss watchdog trip (28.8 m/s delivered, perilune -38.5 km), backup coast-lock (0x7E14); 04:47:19 UTC Gateway crosslink lock via Mount Stromlo; 04:47:45 UTC signed TAKEOVER, STAGE and COMMIT; 04:48:30 UTC recovery burn (49.5 m/s); 05:05:20 UTC occultation; 05:34:32 UTC outbound powered flyby (188.4 m/s); 05:36:00 UTC perilune 112.4 km; 05:41:10 UTC reacquisition via Gateway. Complete timeline mapped in Plate ART-REC-0711 above.*

---

### 2.0 ENGINEERING POST-MORTEM: COVARIANCE STARVATION DYNAMICS

The primary cause of the anomalous burn execution was mathematically isolated to subroutine `GEONS_EKF_UPDATE` within the Honeywell Space-Grade Flight Executive (Build 4.1.2).

#### 2.1 The Linearized Error Budget Breakdown
Prior to the proton storm, *Prometheus* had coasted in solar quiet for forty-eight hours. The process noise matrix $Q$ had been configured by the flight software contractor with a small diagonal acceleration variance, and the full covariance was carried in IEEE single precision under a processor-timing waiver:

$$q_{ii} = 1.0 \times 10^{-12} \text{ m}^2/\text{s}^4$$

From 00:24 to 04:03 UTC, every optical fix failed the gate and was correctly rejected. With no measurement updates, the covariance propagated by prediction alone:

$$P_{k+1|k} = \Phi_k P_{k|k} \Phi_k^T + Q$$

The lunar gravity gradient stretched $P$ along the approach direction; the small $Q$ did nothing to keep the transverse directions numerically resolvable in single precision. At 04:03:51 UTC the eigenvalues of the position covariance sub-matrix were:

$$\lambda_1 = 4.1 \times 10^{6} \text{ m}^2, \quad \lambda_2 = 3.8 \text{ m}^2, \quad \lambda_3 = -0.6 \text{ m}^2$$

A covariance cannot have a negative eigenvalue. The matrix had collapsed toward rank one and lost positive definiteness.

#### 2.2 The Residual Gating Breakdown
When the proton-corrupted star tracker and limb fix injected a candidate observation with an innovation magnitude $\|y_k\| = 221.8\text{ km}$, the classical innovation covariance was:

$$S_k = H P_{k|k-1} H^T + R$$

With $R = \text{diag}(150.0^2, 150.0^2, 150.0^2)\text{ m}^2$ and a sound covariance, the normalized innovation squared would have exceeded $10^4$ and the fix would have been rejected. Built from an indefinite $P$, $S_k$ was itself indefinite, and the solve returned:

$$\chi^2 = y_k^T S_k^{-1} y_k = -287.4$$

The gate in Build 4.1.2 tested only the upper bound:

```c
// UNINTENDED DEFECT: ONE-SIDED NIS GATE IN GEONS BUILD 4.1.2
if (nis <= NIS_GATE_35) {
    // Accept: Joseph-form update commits before any validation of P or nis
    joseph_update(&x, &P, &K, &y);
}
// No check that nis >= 0, no check that P remains positive definite
```

Because $-287.4 \le 35.0$, the gate passed, corrupting the vehicle state vector and placing *Prometheus* on an impact course. The subsequent autonomous recovery by the auxiliary Jetson Orin Nano running ArgonautOS demonstrated the operational necessity of square-root information filtering and diverse verification in deep space flight.
"""

def main():
    files = [
        ("Chapter_05_Flare_State.md", CH5),
        ("Chapter_06_The_Negative_Variance.md", CH6),
        ("Chapter_07_Dead_Mans_Trajectory.md", CH7),
        ("Chapter_08_Light_Across_the_Blind_Spot.md", CH8),
        ("Dossier_Act_II.md", DOSSIER2),
    ]
    for filename, content in files:
        path = os.path.join(MANUSCRIPT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Generated: {filename}")

if __name__ == "__main__":
    main()
