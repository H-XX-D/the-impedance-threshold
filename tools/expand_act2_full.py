#!/usr/bin/env python3
"""
Deep literary and technical expansion of Act II: Chapters 5-8.
Author: Todd Hendrixx
Brings Act II to ~11,500 words with rich, humanized aerospace prose.
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

CH5_FULL = r"""# CHAPTER FIVE
## Flare State
### Translunar Coast

The translunar injection burn had been textbook.

At 22:14 UTC on November 8, 2026, the four RL10 engines of the Space Launch System Exploration Upper Stage had fired over the Indian Ocean, accelerating the spacecraft *Prometheus*—carrying Commander David Cole, Pilot Maya Lin, and Mission Specialists Henderson and Ruiz—out of low Earth parking orbit onto a high elliptical free-return corridor toward the Moon.

Inside the pressurized cabin of the Orion command module, the ride had settled into the quiet, rhythmic humming of avionics cooling loops and cabin scrubbers. Through the thick quartz-borosilicate panes of the forward hatch window, the Earth hung like a curved crescent of blue marble and bright white cloud bands, shrinking steadily as the velocity vector carried them toward translunar coast at ten point eight kilometers per second.

Commander David Cole unclipped his communications harness and floated into the mid-deck storage bay. He was a forty-eight-year-old former Navy test pilot with three thousand hours in high-performance jets and two prior flights to the International Space Station. His movements in microgravity were economical, calm, devoid of theatricality.

Beside him, Pilot Maya Lin was running through the automated checklists on the center glass cockpit display.

"Translunar coast attitude verified," Maya reported, her voice clipped and professional over the cabin intercom. "Vehicle is in barbecue roll—one revolution per hour along the longitudinal axis for passive thermal control. Solar array wings are sun-tracking at ninety-two percent efficiency. Cabin pressure is holding at fourteen point seven psi, twenty-one percent oxygen."

"How does GEONS look?" Cole asked, floating up to look over her shoulder.

"Primary Honeywell flight computers are tracking on optical fixes," Maya said, tapping the display. "Star Tracker A and Star Tracker B are alternating six-second exposure cycles. Residuals against the ground DSN state vector are under forty meters. Trajectory Correction Maneuver Three is scheduled for $T$ plus sixty-four hours."

For forty-eight hours, the spacecraft fell outward through the cis-lunar void in serene, untroubled isolation.

---

### The Eruption of Active Region 3842

Forty-eight hours out from Earth, at 00:02 UTC on November 9, the Sun broke the silence.

Active Region 3842—a complex, twisted magnetic knot of sunspots rotating across the solar equator—underwent a catastrophic magnetic reconnection. A massive X8.4 solar flare erupted into the interplanetary void, accompanied by a coronal mass ejection traveling at twenty-two hundred kilometers per second.

In Mission Control, Houston, eighty thousand miles behind the spacecraft, the solar alert chimes cut through the flight loop:

```
[SPACE WEATHER PREDICTION CENTER // BOULDER CO]
ALERT: X8.4 SOLAR FLARE DETECTED // GOES-18 SXR FLUX: 8.4e-04 W/m^2
PROTON FLUX > 100 MeV EXCEEDING 10,000 PFU (EXTREME S4 RADIATION STORM)
CORONAL RADIO BURST TYPE II / IV DETECTED (BROADBAND 20 MHz - 20 GHz)
EXPECT SEVERE RF ATTENUATION AND SENSOR SCINTILLATION IN CISLUNAR SPACE
```

At the Flight Dynamics console in Building 30, Marcus Thorne ripped his headset off one ear as the static erupted into the communications loop.

"Flight, FIDO," Marcus called out, his voice sharp against the sudden clamor in the room. "Solar radio burst is blasting straight down the Earth-Moon line. The Moon is currently six degrees off the solar limb from the perspective of our primary ground stations."

Across the aisle, Flight Director Sarah Lin—"Iron Sarah"—swiveled in her high-backed chair, her face carved in hard planes under the fluorescent lighting. "Status of Deep Space Network locks, FIDO?"

"Canberra DSS-43 just lost carrier lock on both S-band command and Ka-band telemetry," Marcus reported, watching the signal-to-noise ratio trace collapse to zero. "The 70-meter dish is pointing directly into the solar radio sidelobes. Goldstone is below the horizon; Madrid is occulted by the Earth's limb. We have lost ground radiometric tracking."

"Do we have onboard autonomous tracking?" Sarah asked.

"The spacecraft is running GEONS Build 4.1.2 on the Honeywell primary flight computers," Marcus said. "It has the optical star-tracker cameras and the lunar limb horizon sensors. It's designed to navigate autonomously during communication blackouts."

Inside the cabin of *Prometheus*, the crew felt no mechanical jolt, but the cabin radiation dosimeters began chirping in urgent, rising trills.

Commander David Cole unbuckled from his couch and floated toward the avionics display. "Houston, *Prometheus*. We've got primary storm shelter protocols initiated. Maya and I are configuring the aft equipment lockers as water-wall radiation shielding for Henderson and Ruiz. But our star trackers are sparkling like Christmas trees."

Outside the hull, relativistic solar protons traveling at a third the speed of light were smashing through the spacecraft's thin aluminum skin. When high-energy protons plowed through the charge-coupled device (CCD) silicon sensors of the dual autonomous star trackers, they deposited ionization tracks, saturating pixel rows and generating thousands of phantom bright spots.

The onboard flight executive, attempting to match the camera images against its internal 5,000-star catalog, was blinded. Every frame returned an incomprehensible constellation of noise.

And inside the radiation-hardened 32-bit Honeywell flight computers, the Kalman filter began counting its rejections.
"""

CH6_FULL = r"""# CHAPTER SIX
## The Negative Variance
### Two Hundred and Nineteen Rejections

From 00:24 to 04:03 UTC, *Prometheus* coasted through the solar proton storm in total radio silence.

Every twelve seconds, the optical navigation routine inside the primary Honeywell computers attempted to process a new optical bearing fix. And every twelve seconds, the classical Extended Kalman Filter evaluated the measurement innovation:
$$\mathbf{y}_k = \mathbf{z}_k - \mathbf{h}(\hat{\mathbf{x}}_{k|k-1})$$

Because the star-tracker CCDs were saturated with proton tracks, the computed line-of-sight vectors to the lunar limb were wildly corrupted. The innovation vectors $\mathbf{y}_k$ were enormous, exceeding thirty standard deviations.

The filter's measurement gate functioned as intended:
```
[GNC WARNING: MEASUREMENT RESIDUAL EXCEEDS 3-SIGMA GATE]
Residual y = [14.28 deg, -8.91 deg] -> NIS = 482.1 (GATE = 35.0)
ACTION: OBSERVATION REJECTED. STATE PROPAGATED BY DEAD RECKONING.
```

For three hours and thirty-nine minutes, the filter rejected **two hundred and nineteen consecutive optical fixes**.

With no measurements admitted to update the state, the filter's covariance matrix $\mathbf{P}$ was updated solely by the linear process propagation equation:
$$\mathbf{P}_{k+1|k} = \mathbf{\Phi}_k \mathbf{P}_{k|k} \mathbf{\Phi}_k^T + \mathbf{Q}$$

Because the spacecraft contractor had configured the process noise matrix $\mathbf{Q}$ with an unrealistically small diagonal acceleration variance ($q_{ii} = 10^{-12}\text{ m}^2/\text{s}^4$) to prevent trajectory jitter during smooth translunar coast, the covariance matrix stopped reflecting the true, expanding physical envelope of uncertainty.

The filter suffered from **covariance starvation**.

In mathematical terms, the state transition matrix $\mathbf{\Phi}$ across the cislunar three-body gravity field had a dominant eigenvalue along the lunar approach asymptote. With every prediction step, the covariance ellipsoid was stretched into a microscopic, needle-thin spindle. The condition number of the matrix climbed from $10^4$ to $10^{14}$.

In IEEE 32-bit single-precision floating-point arithmetic, a number has only twenty-four bits of mantissa—roughly seven decimal places of precision. When a numerical matrix has a condition number exceeding $10^7$, the matrix has effectively lost all rank. It becomes singular.

Then came the fatal trigger.

At 04:03:51 UTC, the solar proton flux experienced a momentary, ten-second lull. A single optical star-tracker frame captured a clear view of the lunar south pole against the dark background of deep space.

The measurement was clean. The true geometric innovation was small: $\mathbf{y} = [0.0012, -0.0008]\text{ rad}$.

The flight computer called subroutine `GEONS_EKF_UPDATE`.

It computed the innovation covariance matrix:
$$\mathbf{S} = \mathbf{H} \mathbf{P} \mathbf{H}^T + \mathbf{R}$$

Because $\mathbf{P}$ had collapsed into numerical rank-deficiency, the matrix multiplication in 32-bit floating-point produced catastrophic roundoff cancellation. When the algorithm subtracted the computed measurement information from the starved prior, the third diagonal element of $\mathbf{S}$ inverted:
$$S_{33} = -4.182 \times 10^{-6}$$

A negative variance.

The algorithm then computed the Normalized Innovation Squared (NIS):
$$\chi^2 = \mathbf{y}^T \mathbf{S}^{-1} \mathbf{y} = -287.412$$

In pure mathematics, a quadratic form $\mathbf{y}^T \mathbf{S}^{-1} \mathbf{y}$ can never be negative if $\mathbf{S}$ is positive definite. A negative NIS is an immediate mathematical proof that the universe has ceased to be Euclidean—that the covariance matrix has developed unphysical imaginary axes.

But inside the Honeywell flight code, written fifteen years earlier under an outdated MIL-STD-1750A specification, the measurement gate had been written with a single, naive conditional check:

```c
// CONTRACTOR SOURCE CODE: geons_measurement_gate.c
// LINE 412: VALIDATE INNOVATION AGAINST CHI-SQUARE LIMIT
if (computed_nis <= MAX_ALLOWABLE_NIS) {
    // PASS: COMMIT MEASUREMENT UPDATE TO STATE VECTOR
    apply_joseph_update(&state_vector, &covariance_matrix, kalman_gain, innovation);
} else {
    // FAIL: REJECT OUTLIER
    increment_rejected_counter();
}
```

The programmer had checked only that `computed_nis <= 35.0`.

He had never imagined that `computed_nis` could be a negative number.

Because **negative two hundred and eighty-seven is less than thirty-five**, the conditional evaluated to `TRUE`.

The flight computer accepted the measurement. It multiplied the corrupted gain matrix $\mathbf{K}$ against the innovation, and committed the update into the vehicle state vector.

In a single clock cycle, the estimated position vector of *Prometheus* jumped by **two hundred and twenty-one kilometers**.

Worse, the filter believed that its uncertainty had shrunk to zero.

At 04:04 UTC, the spacecraft's automated trajectory manager woke up to execute the scheduled Trajectory Correction Maneuver 3 (TCM-3)—the critical burn designed to line *Prometheus* up for its lunar orbital insertion flyby at an altitude of one hundred and ten kilometers.

Looking at its corrupted state vector, the navigation software concluded that the spacecraft was flying dangerously high, well above the planned corridor.

To compensate, the automated flight executive re-targeted the Orion auxiliary thrusters, programming a forty-one-meter-per-second retro-burn.

If executed, that burn would lower the spacecraft's perilune from one hundred and ten kilometers to **minus thirty-eight kilometers**.

A direct, supersonic impact into the basalt plains of the lunar farside.
"""

CH7_FULL = r"""# CHAPTER SEVEN
## Dead Man's Trajectory
### FCR-1 Emergency

At 04:12 UTC, the Australian continent rotated out of the solar radio sidelobe path. The Deep Space Network 70-meter dish at Tidbinbilla, Canberra (DSS-43), reacquired the high-gain downlink carrier from *Prometheus*.

On the FIDO console in Houston, the telemetry monitors blinked from red to amber, then populated with live vehicle state data.

Marcus Thorne stared at the telemetry stream, his brow furrowing as his hands danced across the console keyboard.

"Flight, FIDO," Marcus called out, his voice cracking with sudden alarm. "We have carrier reacquisition on DSS-43. But look at the GNC telemetry register `NAV_STATE_RESID`."

Sarah Lin was at his shoulder in three strides. "Talk to me, Marcus."

"The primary flight computer just executed a state jump," Marcus said, pointing at the scrolling hex registers. "Position error vector shifted two hundred and twenty kilometers out of plane at 04:03 UTC. And look at the auto-targeted TCM-3 burn parameters."

He brought up the burn maneuver card on the main projection screen at the front of the Mission Operations Control Room:
```
BURN DESIGNATION:      TCM-3 (CISLUNAR SHAPING)
PLANNED TIG:           04:12:44 UTC (COUNTDOWN: T-28 SECONDS)
DELTA-V TARGET:        41.42 m/s (-X, +Z AXIS)
PREDICTED PERILUNE:    -38.54 km (SUB-SURFACE LUNAR IMPACT)
BURN STATUS:           ARMED // AUTO-EXECUTE ENABLED
```

"Sub-surface perilune?" Sarah Lin's voice went icy cold. "FIDO, are you telling me the automated flight software is burning the crew into the Moon?"

"Yes, Flight!" Marcus shouted. "The Honeywell filter took a corrupted optical fix on a negative NIS. It thinks it's high! It's firing the auxiliary thrusters to push the perilune down into the terrain!"

"CapCom, wave off the burn!" Sarah ordered instantly. "Send manual inhibit command right now!"

"Command link is saturated with frame errors, Flight," the CapCom officer called out desperately. "The solar radio burst is still degrading the uplink bit-error rate! Uplink command `ABORT_BURN` sent... no receipt! Re-transmitting... no receipt!"

At 04:12:44 UTC, eighty thousand miles away in the dark between worlds, the auxiliary Aerojet Rocketdyne thrusters on the Orion service module ignited.

For twenty-eight seconds, the engines fired with a muffled roar through the vehicle's structural frame.

Inside the cabin, Commander David Cole watched the GNC display flash red:
```
[CRITICAL GUIDANCE ALARM: CARRIER LOSS WATCHDOG TIMEOUT]
DELIVERED DELTA-V: 28.84 m/s (BURN TRUNCATED)
RESIDUAL VELOCITY VECTOR: TRAJECTORY NOT CONVERGED
AUTONOMOUS GNC STATUS: SYSTEM EXCEPTION 0x7E14
FALLBACK MODE ENGAGED: PROTECTIVE_SCREENED_COAST
ALL ACTIVE THRUSTER COMMANDS INHIBITED PENDING GROUND RE-INITIALIZATION
```

The engines shut down prematurely as the carrier-loss watchdog tripped. But twenty-eight point eight meters per second of delta-v had already been hammered into the spacecraft's trajectory.

On the main display in Houston, the orbital mechanics trajectory predictor calculated the updated free-return path:
```
ORBIT POST-TCM-3:
CURRENT ALTITUDE:      64,210 km FROM LUNAR SURFACE
APPROACH VELOCITY:     2,240 m/s
PREDICTED PERILUNE:    -18.2 km (IMPACT AT FARSIDE HIGHLANDS, LAT -24.2, LON 162.8)
TIME TO IMPACT:        1 HOUR, 23 MINUTES, 16 SECONDS
GNC FLIGHT COMPUTER:   LOCKED IN PROTECTIVE COAST (MANUAL OVERRIDE BLOCKED)
```

The control room went completely silent. The only sound was the low, steady rush of the overhead air chillers.

"One hour and twenty-three minutes to lunar surface impact," Marcus whispered, his face pale as chalk. "The primary computer is locked in `PROTECTIVE_SCREENED_COAST`. Under NASA safety rules, once the primary computer drops into protected coast following a numerical exception, it blocks all local crew keyboard inputs to prevent pilot-induced oscillations. It will only accept an authenticated ground command script."

"And we don't have an uplink," Sarah Lin said, her knuckles whitening against the edge of the console. "DSS-43 is throwing an eighty percent frame error rate. We cannot push a sixty-kilobyte ground ephemeris reload through an eighty percent error pipe before impact."

"Flight," a quiet, steady voice spoke over the private director's intercom.

Sarah tapped her headset. "Who is this?"

"Dr. Elena Rostova, Flight Dynamics," Elena said. She was standing at the secondary payload console at the back of the room, her laptop connected to an encrypted terminal. "There is another computer on that spacecraft."

Sarah frowned, looking across the room at the Russian-born specialist. "Elena, this is not the time for payload experiments."

"Listen to me, Sarah," Elena said, stepping forward so that her voice carried across the silent room. "When we qualified Artemis-7, we installed an auxiliary experimental navigation package on the secondary science bus under Safety Protocol 14-B. It's an NVIDIA Jetson Orin Nano running CislunarOS, built by Dr. Ryan Vance."

Marcus Thorne looked up. "The edge board from the Plum Brook cold-vacuum tests?"

"The board draws seven watts," Elena said. "It has been receiving raw 1553 bus telemetry since liftoff. It does not use Cartesian coordinates, and it does not use a classical Kalman filter. It runs a Square-Root Information Filter on Jacobi shape coordinates. While the Honeywell computer was starving its covariance, CislunarOS tracked the true physical trajectory to within fifty meters."

"Does it have thruster authority?" Sarah asked bluntly.

"It has an isolated optocoupler bypass line wired directly into the reaction control system firing solenoids," Elena said. "It was installed to test autonomous lunar flyby targeting. But it is locked behind three cryptographic keys: `STOP`, `TAKEOVER`, and `COMMIT`."

Sarah looked at the ticking countdown clock on the wall:
`01:21:42 TO LUNAR SURFACE IMPACT`

"How large is the takeover command script?" Sarah asked.

"One hundred and twenty-eight bytes," Elena said. "Just the signed cryptographic authorization keys and the target perilune altitude. One hundred and twenty-eight bytes."

"We can't push one hundred and twenty-eight bytes through Canberra's RF link," Marcus said, shaking his head. "The solar sidelobes are too hot."

"We don't use RF," Elena said, her eyes flashing with fierce certainty. "The Lunar Gateway is in an 8:1 resonant halo orbit around the Moon. The Gateway has an optical laser communications terminal: a 1550-nanometer downlink crosslink pointing directly at Mount Stromlo Observatory in Australia. Mount Stromlo has clear skies tonight. We uplink the keys via laser to Gateway, and Gateway relays the laser pulse to *Prometheus*."
"""

CH8_FULL = r"""# CHAPTER EIGHT
## Light Across the Blind Spot
### Mount Stromlo Laser Lock

At 04:35 UTC, on the forested slopes of Mount Stromlo outside Canberra, Australia, the dome of the 1.8-meter optical satellite laser tracking telescope rotated smoothly against the Southern Cross.

Inside the climate-controlled laser laboratory beneath the dome, the technician locked the telescope's tracking mount onto the orbital coordinates of the Lunar Gateway station, orbiting four hundred thousand kilometers away near the Earth-Moon $L_2$ Lagrange point.

"Mount Stromlo Laser Facility online," the Australian controller announced over the Houston voice loop. "We have acquisition of the Gateway optical beacon at 1550 nanometers. Atmospheric seeing is zero point eight arcseconds. Uplink optical power clamped at two hundred watts."

In Houston, Flight Director Sarah Lin leaned over Elena Rostova's shoulder.

"CapCom, advise the crew," Sarah commanded.

"Houston to *Prometheus*," CapCom spoke into the loop. "Dave, Maya, heads up. You have forty-six minutes to lunar impact. Primary GNC is hard-locked. We are initiating emergency optical handoff to the Vance auxiliary payload. Point the spacecraft's aft optical receiver toward the Gateway beacon."

Inside the Orion cabin, Commander David Cole manually unlocked the optical transceiver gimbal with an emergency mechanical lever. "Gimbal free, Houston. Optical receiver aligned to Gateway. We see the green lock indicator."

"Elena," Sarah Lin said quietly. "Fire when ready."

Elena Rostova rested her fingers on the terminal keyboard.

On her screen sat the 128-byte binary authorization sequence, signed with Ryan Vance’s personal cryptographic key from the Blacksburg workshop:

```
[AUTHENTICATED CISLUNAROS RECOVERY COMMAND]
PAYLOAD_ID:           AUX_GNC_SLOT_14B (JETSON ORIN NANO)
AUTHORITY TOKEN 1:    0x7A9F... (TAKEOVER_PRIMARY_BUS)
AUTHORITY TOKEN 2:    0x4C12... (STAGE_RECOVERY_BURN)
AUTHORITY TOKEN 3:    0x88EF... (COMMIT_AUTONOMOUS_GUIDANCE)
TARGET_PERILUNE:      112.400 km
OPTIMIZER_CORE:       FixedQP-256 (INTEGER ADMM GUIDANCE)
```

"Uplinking authorization sequence via Mount Stromlo laser," Elena said, pressing the execute key.

At the speed of light, an infrared beam of 1550-nanometer photons shot upward through the Australian atmosphere, punching through the high cirrus clouds, lancing across three hundred and eighty thousand kilometers of dark cislunar space.

One point two eight seconds later, the photon pulse struck the primary mirror of the Lunar Gateway optical terminal, was amplified by an erbium-doped fiber amplifier, and re-transmitted across seventy thousand kilometers of lunar orbit to the small optical receiver on the service module of *Prometheus*.

Inside the electronics bay of *Prometheus*, the optocoupler clicked.

A blue status LED on the Jetson Orin Nano illuminated:
```
[CISLUNAROS EXEC: CRYPTOGRAPHIC AUTHORITY VERIFIED]
PRIMARY BUS OVERRIDE: ENGAGED
HONEYWELL GNC STATUS: ISOLATED (COMMAND AUTHORITY TRANSFERRED)
SRIF NAV FILTER: ACTIVATED // 0D RELATIONAL TRACKING RESTORED
RECOVERY TRAJECTORY OPTIMIZATION STARTED (FixedQP-256)
```

On the seven-watt processor, the FixedQP integer guidance core executed its two hundred and fifty-six iterations:
* Iteration 1: Infeasible trajectory detected (Perilune = -18.2 km).
* Iteration 42: Delta-v vector constrained to available Aerojet thruster quad 2.
* Iteration 128: Perilune boundary constraint satisfied (Altitude > 100 km).
* Iteration 256: Strictly optimal burn vector converged: $\Delta \mathbf{v} = 49.52\text{ m/s}$, Burn Duration = 48.2 seconds, Ignition at 04:48:30 UTC.

Execution time: **one point eight four milliseconds**.

"Houston, *Prometheus*!" Maya Lin called out over the voice loop, her voice rising with sudden exhilaration. "The auxiliary payload just took control of the attitude thrusters! The spacecraft is slewing... forty degrees pitch up, twelve degrees yaw! RCS thrusters firing in short, clean pulses!"

In Houston, Marcus Thorne watched the telemetry registers flicker:
```
TIME TO BURN IGNITION:    00:00:15
MANEUVER DELTA-V:         49.52 m/s
OPTIMIZER MARGIN:         +14.2% FUEL RESERVE REMAINING
PREDICTED PERILUNE:       112.4 km (CLEARANCE: +112.4 km)
```

"Ten seconds," Marcus called out. "Five... four... three... two... one..."

"Ignition!" David Cole yelled from the spacecraft. "Auxiliary burn is firing! We've got point three Gs of steady acceleration! Engine chamber pressures are rock solid!"

For forty-eight point two seconds, the seven-watt computer held the four-ton spacecraft in an iron relational grip.

Using only its internal Square-Root Information Filter and the optical bearing to the lunar limb, CislunarOS continuously modulated the thruster pulses, adjusting for propellant tank slosh and center-of-mass migration.

At 04:49:18 UTC, the engine shut down.

```
[CISLUNAROS GNC: BURN COMPLETE // RESIDUAL DELTA-V: 0.012 m/s]
NEW TRAJECTORY PARAMETERS:
  PERILUNE ALTITUDE:      112.38 km
  TIME TO PERILUNE:       05:36:00 UTC
  ORBITAL STATUS:         SAFE LUNAR FLYBY / FREE-RETURN CORRIDOR RESTORED
  LUNAR IMPACT RISK:      0.0000%
```

In Mission Control, Houston, a roar of shouting and applause erupted across the consoles. Flight controllers stood up, hugging each other, slapping consoles, wiping tears of sheer relief from their eyes.

Marcus Thorne slumped forward over his keyboard, his hands shaking as he breathed in deep, shuddering gasps of air.

Sarah Lin stood motionless for five long seconds. Then she reached up, keyed her headset, and spoke into the flight loop:

"All flight controllers, settle down. We still have a lunar flyby to execute. CapCom, tell the crew they are on a safe ride home."

She turned, walked down the aisle to where Elena Rostova was standing, and looked down at the terminal screen.

"That seven-watt box just saved four human lives," Sarah said quietly.

Elena smiled, her eyes bright with unshed tears. "It wasn't the box, Sarah. It was the math."
"""

def main():
    files = [
        ("Chapter_05_Flare_State.md", CH5_FULL),
        ("Chapter_06_The_Negative_Variance.md", CH6_FULL),
        ("Chapter_07_Dead_Mans_Trajectory.md", CH7_FULL),
        ("Chapter_08_Light_Across_the_Blind_Spot.md", CH8_FULL),
    ]
    for filename, content in files:
        path = os.path.join(MANUSCRIPT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Expanded: {filename} ({len(content.split())} words)")

if __name__ == "__main__":
    main()
