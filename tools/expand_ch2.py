import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

ch2_expanded = r"""# CHAPTER TWO
## The Montgomery Shape Sphere
### Covariance Collapse in Houston

The air inside the Mission Control Center at NASA’s Johnson Space Center in Houston was thick with the bitter stench of burnt espresso, dry-erase solvent, and institutional dread.

Across the front projection wall of Building 30, the primary orbital plot of Artemis-7—the deep-space crew transport *Prometheus*, carrying Commander Elena Rostova, astrobiologist Dr. Aris Thorne, and geologist Chen Wei—was frozen in screaming amber. A dashed crimson vector extended from the spacecraft's current position sixty thousand kilometers above the Moon, diving with terrifying geometric certainty into the frozen basalt wastes of the South Pole-Aitken basin.

"Flight, guidance telemetry is completely corrupted," called the Guidance Officer (GUIDO), his hands trembling against his dual-monitor console. "The star tracker on the forward avionics ring took an intense proton shower during the X8.4 solar radio storm. When the optical fix dropped into the GEONS Extended Kalman Filter, the innovation covariance matrix lost positive-definiteness. We have a total rank collapse!"

Flight Director Warren Hastings stood behind the trench, both hands planted on the polished mahogany console rail. His tie was loose, his collar soaked in sweat.

"Speak English, GUIDO," Hastings snapped, his voice echoing across the silent room. "How does a covariance matrix lose positive-definiteness? A covariance matrix is symmetric positive-definite by definition! It is a measure of variance! Variance cannot be negative!"

"In continuous theory, yes, Flight," GUIDO answered, rapidly typing diagnostic commands to dump the RAD750 memory registers. "In 64-bit double precision, yes. But the flight software executive is running on legacy RAD750 flight computers certified under an aerospace contractor waiver twenty years ago! To save processor cycles during translunar coast, the contractor configured subroutine `GEONS_EKF_UPDATE` in IEEE single-precision floating-point arithmetic!"

GUIDO threw the memory dump onto the central big screen. Rows of raw hexadecimal registers flashed before the controllers.

"Prior to the solar flare," GUIDO explained, his voice climbing in pitch, "the spacecraft coasted through forty-eight hours of deep quiet. The process noise matrix $Q$ was set with an ultra-small acceleration variance—ten to the minus twelve meters squared per second to the fourth. The filter became infinitely overconfident. The prior covariance $P$ stretched along the velocity vector, but in the transverse directions, single-precision roundoff began eating the bits!"

He pulled up the three eigenvalues of the position covariance sub-matrix:

$$\lambda_1 = 4.1 \times 10^{6} \text{ m}^2, \quad \lambda_2 = 3.8 \text{ m}^2, \quad \lambda_3 = -0.6 \text{ m}^2$$

The room went deathly still.

"A negative eigenvalue," Hastings whispered, his face draining of color.

"A variance of minus zero point six meters squared," GUIDO said. "The matrix lost positive-definiteness. And then, at 04:03 UTC, the star tracker rebooted after the proton strike and injected an optical limb fix with an innovation magnitude of two hundred and twenty-one kilometers! When the filter computed the innovation covariance:

$$S_k = H P_{k|k-1} H^T + R$$

"Because $P$ was indefinite, $S_k$ was indefinite! The solve for the Normalized Innovation Squared produced a negative scalar:

$$\chi^2 = y_k^T S_k^{-1} y_k = -287.4$$

"And here is the catastrophic defect in Build 4.1.2," GUIDO continued, highlighting the source code on the screen:

```c
// CRITICAL DEFECT: ONE-SIDED NIS GATE IN GEONS BUILD 4.1.2
if (nis <= NIS_GATE_35) {
    // Commits corrupted state update without checking if nis >= 0
    joseph_update(&x, &P, &K, &y);
}
```

"The gate tested only the upper bound!" GUIDO cried. "It asked if minus two hundred and eighty-seven was less than thirty-five! The condition evaluated as true! The filter accepted the corrupted fix, shifted the ship's estimated position by two hundred and twenty kilometers in a single clock cycle, and committed the update! A millisecond later, the divergence monitor realized the position was physically impossible, panicked, and slammed the entire GNC bus into `PROTECTIVE_SCREENED_COAST`!"

"And the mechanical fail-safe?" Hastings demanded.

"The fail-safe is hardware-latched, Flight," the Systems Officer reported grimly. "The main AJ10 bipropellant engine is isolated. The sixteen reaction control thrusters are mechanically valved shut. The autopilot refuses to fire because its software believes that any thruster activity will worsen the state divergence. It's a digital coast-lock. The computer is holding the ship in a passive drift all the way down to the surface."

On the master lunar loop, the voice of Commander Elena Rostova crackled over the speakers, four hundred thousand kilometers away, fighting against a wall of solar radio static:

*"Houston, this is Rostova. We have tried the manual GNC override three times. The flight software rejects the rotational hand-controller input because the safety interlock requires a converged navigation covariance before opening the fuel valves! The ship has locked us out of our own thrusters! We are falling toward perilune at twenty-four hundred meters per second!"*

Hastings leaned over his microphone, gripping the console. "Elena, this is Flight. We copy your situation. We are preparing an emergency ground-commanded hydrazine blowdown. We will bypass the flight software via the backup engineering umbilical and fire the auxiliary RCS thrusters continuously for ninety seconds to push your perilune outward."

*"Negative, Houston! Absolutely negative!"* Elena fired back instantly, her tone razor-sharp with tactical fury. *"If you blow the RCS via the backup umbilical without closed-loop attitude stabilization, the spacecraft will tumble uncontrollably in the Moon's gravity gradient! You will burn through forty percent of our reserve propellant, induce an unrecoverable yaw spin, and miss the lunar capture corridor entirely! We won't crash into the Moon—we'll fly into a dead, hyperbolic orbit into the interplanetary void with three days of oxygen!"*

"It is the only procedure authorized in the Flight Operations Manual, Elena!" Hastings shouted.

*"Then your manual is an execution warrant, Warren!"* Elena yelled back. *"Put Ryan Vance on this loop right now!"*

Hastings stiffened, his face flushing dark crimson. "Dr. Vance is a civilian contractor whose unverified relational guidance software was explicitly disqualified by NASA Headquarters!"

*"I don't give a damn about headquarters!"* Elena's voice cut through the static like a diamond blade. *"Vance warned you three years ago at the Critical Design Review that the classical Cartesian Kalman filter would suffer covariance starvation in multi-body space! He told you that space is not an empty coordinate box where you can invert matrices with floating-point roundoff! He built the square-root information filter that prevents negative NIS by construction! Put him on the loop, or I will take an emergency fire axe to the primary avionics breaker!"*

Before Hastings could answer, the red carrier light on the flight director's terminal flared. A high-priority audio crosslink from the Giles County metrology station in Tennessee sliced through the channel.

"Warren," Ryan Vance's voice echoed through the Mission Control floor, calm, measured, and completely devoid of panic. "I am looking at your raw telemetry dump right now. Your Cartesian filter failed because you are trying to describe a chaotic three-body Hamiltonian with two-body osculating ellipses. You are measuring the spacecraft against an imaginary origin at the center of the Earth that has no physical meaning in cislunar space."

"Vance," Hastings growled, his knuckles white on the desk. "You have no operational standing in Building 30."

"I have the mathematics that will keep your three astronauts from dying in the Aitken basin," Ryan replied coldly. "Listen to me, Warren. *Prometheus* is caught in the Jacobi manifold between the Earth and the Moon. In classical Cartesian coordinates, the three-body equations of motion are non-linear, coupled, and numerically stiff. But if you project the system onto Montgomery's shape sphere $S^2$, the three-body problem decouples into scale and shape:

$$u = \sqrt{\frac{m_1 m_2}{m_1 + m_2}}(r_2 - r_1), \quad v = \sqrt{\frac{m_3(m_1 + m_2)}{m_1 + m_2 + m_3}}\left(r_3 - \frac{m_1 r_1 + m_2 r_2}{m_1 + m_2}\right)$$

"The shape-sphere diagnostic," Ryan continued, his voice carrying an unyielding mathematical authority that silenced every controller in the room, "defines the shape of the triangle formed by the Earth, the Moon, and *Prometheus*:

$$\begin{gathered} w_x = |u|^2 - |v|^2, \quad w_y = 2(u \cdot v), \\ w_z = 2(u \times v) = 2(u_1 v_2 - u_2 v_1) \end{gathered}$$

"On the shape sphere," Ryan said, "the collision manifold isn't an infinite plane of danger; it's a closed meridian! You don't need a massive, uncontrolled hydrazine blowdown to escape it. You need a ninety-meter-per-second burn executed at exactly twelve degrees off the Earth-Moon invariant normal! But your ship computer won't let Elena fire that burn because its software is frozen in coast-lock!"

Hastings stared at the projection wall. The collision clock was mercilessly counting down:

```
TIME TO PERILUNE IMPACT: 61 HOURS, 14 MINUTES
TRAJECTORY STATUS: UNRECOVERABLE UNDER CURRENT AUTOPILOT
```

"Then what do you propose we do, Vance?" Hastings asked, the bluster draining from his voice. "We can't reflash the RAD750 from Earth. The solar flare is drowning the S-band receivers in noise. The uplink packet loss is eighty percent!"

"You can't reflash it from Earth," Ryan said. "Which is why I am bringing the flight core to her myself."
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_02_The_Montgomery_Shape_Sphere.md"), "w", encoding="utf-8") as f:
    f.write(ch2_expanded)
print("Expanded Chapter 2 successfully.")
