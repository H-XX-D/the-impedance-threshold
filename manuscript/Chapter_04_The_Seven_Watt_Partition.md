# CHAPTER FOUR
## The Seven-Watt Partition
### The Roanoke Trade Counter

After hanging up the satellite phone with Elena Rostova, Ryan Vance did not sleep.

He didn't wait for the NASA transport jet to solve his engineering problems. If the last ten years had taught him anything, it was that institutional aerospace spent six months convening safety panels to purchase a ten-thousand-dollar connector while an operational crew suffocated waiting for the paperwork to clear.

He shut down the Giles County Sagnac laser, pumped down the vacuum valves, and secured the subterranean vault. He drove his Subaru out of the limestone cut and headed northeast along Interstate 81 as a freezing mountain rain glazed the asphalt. At six in the morning, an hour before the trade counter officially opened, he was banging on the glass doors of an industrial robotics and automation distributor in an industrial park off Airport Road in Roanoke.

The counter manager, a burly man in an insulated flannel jacket holding a thermos of coffee, unlocked the security deadbolt with a scowl.

"We don't open until seven, buddy."

"I need an edge-AI computing module," Ryan said, stepping into the heated foyer. He pulled his personal credit card from his wallet. "Carrier board, passive heatsink, DC barrel connector, and an FTDI serial breakout. Specifically the **NVIDIA Jetson Orin Nano** development kit."

The manager blinked at him. "The eight-gigabyte model? That’s for warehouse AGVs and computer-vision sorting belts."

"I don't care what it’s for," Ryan said. "Do you have one in inventory?"

The manager tapped the SKU into his terminal. "One unit left on the shelf. Three hundred and ninety-nine dollars plus tax."

"Take the card," Ryan said.

Ten minutes later, Ryan walked back to his car carrying a small cardboard box no larger than a hardcover novel.

Prime aerospace contractors solved flight navigation challenges by spending sixty million dollars on triple-redundant, radiation-hardened BAE RAD750 mainframes housed in milled beryllium-copper conduction enclosures, supported by hundreds of contractor personnel tuning Kalman filter parameters from consoles in Houston.

Ryan Vance had four hundred dollars, an edge-computing board designed to guide automated forklifts through Amazon fulfillment centers, and a strict physical reality: the emergency secondary avionics bay on the Orion capsule had a dedicated auxiliary DC power tap clamped to precisely **seven point two watts**.

If his relational navigation filter could not boot, propagate, fuse optical measurements, and output a valid orbital state vector inside that seven-watt partition, four astronauts were going to vaporize against the basalt cliffs of the lunar farside.

---

### The Architecture of Collapse

Back in his Blacksburg garage, with the kerosene heaters roaring against the dawn chill, Ryan placed the green printed circuit board on an antistatic mat.

The Jetson Orin Nano was an astonishing piece of commercial silicon: a six-core ARM Cortex-A78AE CPU paired with an Ampere-architecture GPU containing 1,024 CUDA cores and 32 Tensor Cores, capable of forty trillion operations per second—provided it was given adequate cooling and twenty-five watts of power.

Ryan flipped the hardware power-selector jumper on the board to **5W Low-Power Mode**.

He clamped the DC input leads to his benchtop linear power supply, wired an oscilloscope current probe across the positive rail, and plugged a USB-serial adapter into his Linux development laptop.

The terminal flashed:

```
[TEGRA-BOOT] NVIDIA Tegra234 (Orin Nano) Initializing...
[TEGRA-BOOT] Cores enabled: 2 of 6 (Cortex-A78AE throttled to 800 MHz)
[TEGRA-BOOT] GPU Tensor Cores: Clock-gated (0 MHz)
[TEGRA-BOOT] Total Board Power Draw: 4.82 Watts.
```

"Four point eight watts," Ryan murmured, checking the digital readout on the power supply. "Two point four watts of thermal headroom for the transceiver."

He created a fresh directory: `cislunar_recovery_bench/`.

To prove beyond any shadow of a doubt why NASA's sixty-million-dollar avionics were collapsing, he spent the next two hours coding an exact replica of the Artemis-7 flight software: a textbook Extended Kalman Filter (EKF) utilizing the standard Joseph-form covariance update:

$$\mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k) \mathbf{P}_{k|k-1} (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)^T + \mathbf{K}_k \mathbf{R}_k \mathbf{K}_k^T$$

In aerospace textbooks, the Joseph-form update was revered as the gold standard of numerical stability. By squaring the bracketed terms, it guaranteed mathematically that the diagonal elements of the error covariance matrix $\mathbf{P}$—representing the positional and velocity variances $\sigma_x^2, \sigma_y^2, \sigma_z^2$—would remain positive.

He compiled the code in standard IEEE 754 single-precision 32-bit floating-point arithmetic—the exact precision used by the radiation-hardened flight microprocessors on Orion to conserve memory and clock cycles.

He fed the filter the recorded translunar trajectory telemetry from Artemis-7 that Elena had encrypted and uploaded to his secure FTP server at 04:00 AM: seventy-two hours of inertial measurement unit (IMU) delta-velocity pulses, interleaved with optical bearing angles to lunar craters captured by the vehicle's navigation cameras.

He initiated the playback:

```
[EKF-SIM] Replaying Artemis-7 Flight Telemetry (MET 00:00 to 52:00)...
[EKF-SIM] T+12:00:00 - State variance: sigma_r = 14.2 m, sigma_v = 0.012 m/s. Nominal.
[EKF-SIM] T+24:00:00 - State variance: sigma_r = 82.6 m, sigma_v = 0.045 m/s. Nominal.
[EKF-SIM] T+36:00:00 - Weak Stability Boundary Encounter.
```

At hour 38, as the simulated spacecraft crossed the point where Earth's gravitational pull and the Moon's gravitational pull reached parity along the rotating Earth-Moon line, the terminal screen turned red:

```
[EKF-WARN] Innovation Covariance S = H*P*H^T + R condition number: 1.48e+08
[EKF-WARN] Floating-point round-off detected in matrix inversion.
[EKF-FAIL] Diagonal element P[4,4] = -1.842e-04 (Negative Variance!)
[EKF-FAIL] Normalized Innovation Squared (NIS): -503.18
[EKF-FATAL] Chi-Square Gate Failed: Covariance matrix non-positive definite.
[EKF-FATAL] Navigation State INHIBITED. Safe mode triggered.
```

Ryan took off his glasses and rubbed his eyes.

There it was.

In pure mathematics, $\mathbf{P}$ can never have a negative eigenvalue. But in 32-bit floating-point arithmetic, when two nearly equal numbers on the order of $10^5$ are subtracted to update a state variance across a non-linear gravitational saddle point, the least significant bits are truncated. The matrix loses its positive-definite character. A single negative eigenvalue appears.

The filter tries to compute the Kalman gain $\mathbf{K} = \mathbf{P} \mathbf{H}^T \mathbf{S}^{-1}$. Because $\mathbf{S}$ contains the negative variance, the innovation variance turns negative. The Normalized Innovation Squared—which should be a positive scalar drawn from a chi-square distribution—becomes a negative number: **$-503.18$**.

The computer looks at $-503.18$, realizes that a negative probability is a physical impossibility, assumes its sensors have suffered catastrophic hardware destruction, and shuts down the navigation loop to protect the ship.

"You built your filter on caloric," Ryan said to the empty garage. "You assumed space was smooth, so you inverted a metric matrix. And the computer died on a rounding error."

---

### The Integer Guidance Core: SRIF and FixedQP

To replace the failing EKF, Ryan did not try to fix the floating-point math. He threw floating-point math into the trash.

If a flight computer has to operate on seven watts in a high-radiation environment where single-event upsets flip bits in memory registers, floating-point arithmetic is a lethal liability. An exponent bit flip turns a 1.0-meter correction into a ten-billion-kilometer explosion.

Ryan implemented a two-stage relational guidance engine designed entirely around **deterministic integer arithmetic and square-root factorizations**.

#### Stage 1: The Square Root Information Filter (SRIF)

Instead of propagating and updating the covariance matrix $\mathbf{P}$, which had the dimensions of state squared, Ryan used the square root of the information matrix:

$$\mathbf{P}^{-1} = \mathbf{R}^T \mathbf{R}$$

where $\mathbf{R}$ was an upper-triangular matrix.

To update the state with new optical measurements, the algorithm did not perform matrix inversion or Kalman gain division. It constructed a single composite data array combining the prior information square root $\mathbf{R}$, the measurement mapping matrix $\mathbf{H}$, and the measurement residual $\mathbf{z}$:

$$\mathbf{T} = \begin{bmatrix} \mathbf{R} & \mathbf{b} \\ \mathbf{H} & \mathbf{z} \end{bmatrix}$$

Then, Ryan applied a sequence of **Householder orthogonal transformations**—pure geometric reflections that rotated the composite matrix into upper-triangular form:

$$\mathbf{Q} \mathbf{T} = \begin{bmatrix} \mathbf{R}_{\text{new}} & \mathbf{b}_{\text{new}} \\ \mathbf{0} & \mathbf{e} \end{bmatrix}$$

Because $\mathbf{Q}$ was an orthogonal matrix ($\mathbf{Q}^T \mathbf{Q} = \mathbf{I}$), the condition number of the problem was halved. Round-off errors could not produce negative eigenvalues because the covariance matrix was never computed; only its square root $\mathbf{R}_{\text{new}}$ existed.

Even if single-precision floating-point arithmetic were used, the SRIF was mathematically immune to negative-NIS collapse.

#### Stage 2: The FixedQP Integer Guidance Engine

For trajectory optimization and thruster burn execution, Ryan bypassed floating-point quadratic programming altogether.

He wrote **FixedQP**: a 256-iteration active-set quadratic programming solver running entirely in **32-bit fixed-point integer arithmetic** (`int32_t`), with a fixed binary scale factor of $2^{16}$ (Q16.16 format):

- Upper 16 bits: integer part ($-32,768$ to $+32,767$ meters or meters per second).
- Lower 16 bits: fractional part (precision of $1/65,536 \approx 15.25\ \mu\text{m}$).

Every multiplication was executed via a single assembly-level integer multiply-accumulate (`SMULL` on ARM), followed by a deterministic bit-shift:

```cpp
inline int32_t q16_mul(int32_t a, int32_t b) {
    int64_t prod = (int64_t)a * (int64_t)b;
    return (int32_t)(prod >> 16);
}
```

Zero division by zero. Zero NaN propagation. Zero floating-point denormalization stalls.

He compiled the entire package into a bare-metal Linux binary: `cislunar_os_core.elf`.

Total executable binary size: **482 kilobytes**.

He executed the test on the Jetson Orin Nano:

```
[CISLUNAR-OS] Loading FixedQP 32-bit Integer Guidance Core...
[CISLUNAR-OS] Initializing Householder SRIF Information Filter...
[CISLUNAR-OS] Replaying Artemis-7 Telemetry across WSB...
[CISLUNAR-OS] T+36:00:00 - Weak Stability Boundary Encounter.
[CISLUNAR-OS] T+38:00:00 - Householder QR Orthogonalization: COMPLETE.
[CISLUNAR-OS] Information Matrix Condition Number: 1.21e+02 (ROCK SOLID)
[CISLUNAR-OS] State Error: delta_r = 1.18 m, delta_v = 0.0004 m/s.
[CISLUNAR-OS] FixedQP Trajectory Optimization: Converged in 14 iterations (0.82 ms).
[CISLUNAR-OS] Execution Power Draw: 5.14 Watts. PASS.
```

Ryan leaned back in his chair. A slow smile spread across his face for the first time in six months.

The four-hundred-dollar forklift brain had eaten the sixty-million-dollar aerospace anomaly for breakfast, in less than a millisecond, drawing five point one watts.

---

### The Plum Brook Chamber Test

At 08:30 AM, a black government sedan with US Government plates pulled up to the curb of the Blacksburg bungalow. Two men in dark suits stepped out, accompanied by an Air Force captain in flight fatigues.

"Dr. Vance?" the captain asked, saluting crisply. "Captain Miller, Air Mobility Command. Dr. Rostova ordered us to transport you and your hardware to NASA Plum Brook Station immediately."

"Plum Brook?" Ryan picked up his Pelican case containing the Jetson board, a backup unit, two power cables, and a ruggedized terminal laptop. "Why Plum Brook? I thought we were going to Johnson in Houston."

"The Flight Director won't touch uncertified commercial hardware in Mission Control," Miller explained as they loaded the gear into the trunk. "If you want this board anywhere near Artemis-7, you have to prove it can survive flight conditions under the Space Simulation Vacuum Facility at the Neil Armstrong Test Facility in Ohio. Dr. Rostova has booked Chamber B."

Three hours later, a C-21 Learjet touched down at Sandusky, Ohio.

NASA Plum Brook’s Space Power Facility housed the world’s largest thermal vacuum chamber: a cavernous aluminum-ribbed silo capable of simulating the absolute vacuum and cryogenic freeze of deep space.

In the staging bay of Chamber B, a team of NASA avionics qualification technicians stood around a two-meter cylindrical vacuum bell jar.

Elena Rostova was there, wearing a NASA flight jacket over a wrinkled blue blouse, dark circles under her eyes, her smartphone glued to her ear. When she saw Ryan walk through the airlock door, she hung up the phone and walked straight toward him.

"You look terrible, Ryan," she said, her voice hoarse.

"You look worse," Ryan said. "How is Artemis?"

"TCM-3 is scheduled in twenty-one hours," Elena said, her voice dropping. "Computer A failed again twenty minutes ago. Computer B is rejecting ground tracking updates because Canberra DSN lost lock during a solar coronal mass ejection. If we don't have an onboard recovery package certified by eighteen hundred hours today, Flight Director Hayes will call the mission lost and order the crew to prepare for farside impact."

She looked at the Pelican case in Ryan's hand. "Is that it?"

"That's it," Ryan said. He popped the latches and opened the lid.

The NASA qualification lead, a gray-haired engineer named Kowalski with thirty years of shuttle and space station testing experience, looked into the case and let out a dry, incredulous snort.

"An NVIDIA Jetson board?" Kowalski looked at Elena, then at Ryan. "Are you out of your mind? That’s commercial plastic and lead-free solder. It isn't rad-hard. It isn't conformal-coated. The BGA solder balls will crack under thermal shock, and the first solar proton that hits the silicon will latch up the entire memory bus."

"The board doesn't need to survive for ten years on a Mars rover, Mr. Kowalski," Ryan said evenly. "It needs to survive for twenty-one hours. And the code running on it doesn't use floating-point arithmetic. If a proton flips a bit in the data array, the Householder QR transformation projects the error onto the orthogonal residual vector $\mathbf{e}$ and discards it in the next cycle. Put it in the chamber."

Kowalski stared at him for five tense seconds, then waved his arm at the technicians. "Mount it to the cold plate. Wire the auxiliary seven-watt DC bus and pump the chamber down to ten to the minus six."

The technicians bolted the Jetson board to an aluminum bracket inside the bell jar, attached thermocouple probes to the processor heatsink, wired the 5-volt power leads, and sealed the heavy steel dome.

The vacuum pumps began their deafening mechanical whine: *whirrrrr-thump-thump-thump*.

Inside the bell jar, the pressure plummeted through the pascals: $10^1$, $10^{-1}$, $10^{-3}$, $10^{-6}$ torr. Liquid nitrogen was pumped through the thermal shrouds, dropping the chamber wall temperature to minus one hundred and fifty degrees Celsius.

On the test bench monitor, the Jetson Orin Nano booted in the vacuum:

```
[VAC-TEST] Chamber Pressure: 4.2e-06 Torr.
[VAC-TEST] Cold Plate Temp: -142 deg C.
[VAC-TEST] Core Temp: +18 deg C (Self-heating under passive radiation).
[VAC-TEST] Input Voltage: 5.02 V | Current: 1.04 A | Power: 5.22 Watts.
[VAC-TEST] Executing 10,000 Monte Carlo Cislunar Trajectory Recoveries...
```

For two agonizing hours, the qualification team stood around the telemetry screen in dead silence.

Outside in the Ohio afternoon, the winter wind rattled the corrugated steel walls of the test facility. Inside the console room, the green progress bar ticked relentlessly forward:

```
[VAC-TEST] 10,000 / 10,000 Monte Carlo Runs Complete.
[VAC-TEST] Guidance Solutions Converged: 10,000 (100.00%)
[VAC-TEST] Numerical Exceptions / NaN Flags: ZERO.
[VAC-TEST] Negative NIS Occurrences: ZERO.
[VAC-TEST] Maximum Trajectory Discrepancy: 1.42 Meters at Perilune.
[VAC-TEST] Status: QUALIFIED FOR FLIGHT EVALUATION.
```

Kowalski slowly took off his safety glasses, looked at the numbers on the screen, and then looked at Ryan Vance.

"I’ll be damned," Kowalski muttered.

Elena grabbed Ryan’s arm, her fingers digging through his heavy woolen sleeve.

"We have our flight package," Elena said, her eyes burning with fierce determination. "Now we have to convince Hayes to beam it to the ship."
