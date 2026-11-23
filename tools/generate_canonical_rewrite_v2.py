#!/usr/bin/env python3
"""
Generate the completely fresh, humanized canonical manuscript for
THE IMPEDANCE THRESHOLD: ARGONAUT by Todd Hendrixx.
New chapter titles, completely fresh opening, authentic human dialogue,
and strict adherence to the author's technological lineage:
QRC theory -> Pulsar bench -> 7W Jetson Nano cislunar work -> Artemis rescue -> ARGONAUT -> First life -> Daedalus epilogue.
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

CHAPTERS_DATA = [
    # Act I
    (1, "The Gridless Sky", "Chapter_01_The_Gridless_Sky.md", r"""# CHAPTER ONE
## The Gridless Sky

The Robert C. Byrd radio telescope did not care about the human calendar.

At four o'clock on a freezing November morning in Pocahontas County, West Virginia, the one-hundred-meter paraboloid stood pale and colossal against the Allegheny fog, its two thousand and four motorized aluminum panels drinking in the 1.4-gigahertz hiss of the sky. Around the base of the feed tower, the air smelled of wet oak leaves, diesel exhaust from the observatory’s stripped utility truck, and the sharp, coppery tang of the liquid-helium refrigeration lines cooling the Gregorian receiver.

Dr. Ryan Vance stood on the gravel turnaround beneath the dish, his gloved hands shoved deep into the pockets of an oilskin work jacket, watching the massive azimuth carriage crawl on its steel rail with a groaning vibration that traveled directly into the soles of his boots.

He was thirty-two years old, thin-shouldered, with dark hair curling over the collar of his wool sweater and eyes that had developed the permanent, squinting vigilance of a metrologist who trusted nothing with moving parts.

Three hours earlier, in the library of the Jansky Laboratory, Ryan had packed his belongings into cardboard boxes: fifteen years of notes, four notebooks filled with tensorial algebra, a three-inch triangular fused silica calibration prism, and a salvaged rubidium frequency standard.

The department director, Dr. Warren Hastings, had offered him a quiet out.

"Take the postdoctoral extension, Ryan," Hastings had said, standing by the library fireplace with a cup of black tea. "Sign the paper. Put your name on the DESI dark energy consensus paper. You get five years of stable funding, guaranteed observing time on the Byrd, and you don't have to live on three hundred dollars a month."

"The DESI paper is fitting a spline to an unclosed ledger, Warren," Ryan had replied, without raising his voice. "You have two free parameters—$w_0$ and $w_a$—that you tweak every time a new supernova survey shifts the distance modulus. When an engineer's bridge develops an unclosed shear force, he doesn't invent an invisible truss and declare it a breakthrough in structural theory. He checks where his statics failed. Space is not a geometric rubber sheet that stretches when you drop mass onto it. Space has no background. It is nothing more than the inferred measurement of causal impedance between things that touch."

Hastings had looked at him with the weary, patient pity of an administrator who had seen a hundred brilliant theoreticians throw their careers away on foundational obsessions.

"Natural philosophy does not pay the power bill for the cryostats, Ryan. If you cannot produce publishable Cartesian ephemerides for the funding committee, you cannot occupy an office at Green Bank."

"Then I'll build my own clocks," Ryan had said.

---

### The Paper and the Lead

By dawn, Ryan was fifty miles south, across the Virginia state line, inside the draughty concrete-floored garage behind a rented cedar-shingle cottage on the edge of Blacksburg.

A rusted cast-iron woodstove in the corner radiated the dry, crackling warmth of seasoned hickory. Outside the salt-streaked windows, the morning sun broke through the pines along the spine of Brush Mountain, turning the frozen mud of the driveway into glistening glass.

On his workbench—two sheets of three-quarter-inch marine plywood bolted over heavy fir timbers—sat an aluminum optical breadboard resting on four sorbothane vibration-damping pucks. At the center of the plate, bathed in the morning light, sat his reference tools: a dual-channel digital storage oscilloscope, a temperature-compensated rubidium atomic frequency standard whose amber status light blinked in steady, quiet ten-picosecond increments, and the heavy, three-inch triangular prism of optical-grade fused silica.

He had no research grant. He had no institutional computing cluster.

He pulled a fresh pad of engineering quadrille paper toward him and clicked the lead of a mechanical pencil.

"Start with zero," he wrote.

For four hundred years, since Isaac Newton laid down the axioms of the *Principia*, natural science had committed the same category error: treating space as a preexisting Euclidean box. Newton called it *Absolute Space*—an immutable, rigid container that existed before matter, held matter, and would remain unchanged if all matter were wiped out of existence. Einstein had made the container dynamic, warping its metric tensor $g_{\mu\nu}$ with mass and energy, but the container remained: a smooth, four-dimensional differential manifold upon which events were plotted like coordinates on a surveyor's map.

"The container is a mathematical ghost," Ryan murmured, the pencil scratching across the paper.

If two particles in the cosmos never exchange a photon, never exert a gravitational force, and share no causal past, there is no physical operational meaning to the claim that they are separated by five kilometers. You cannot stretch a tape measure between them without interacting with them. You cannot bounce a radar pulse off them without transferring momentum. Distance is not an empty interval across which things travel; **distance is the inferred measurement of causal impedance between the things that interact.**

He laid down the dimensional structure of Quantum Relational Causality:
- **0D: The Non-Local Substrate.** Pure relational network. No coordinates, no metric, no embedding room.
- **1D: Directed Causal Paths.** The topological histories of discrete excitations.
- **2D: Gauge Holonomies.** Closed loops of relational phase: electromagnetism and gauge curvature.
- **3D: The Reconstructed Spatial Manifold.** The macroscopic three-dimensional relations experienced by physical observers.
- **4D: Causal History.** The parameterization of sequential state updates.

"And what sets the scale?" he asked the cold morning air.

He tapped the pencil against the wood, looking at the amber pulse of the rubidium clock.

The Margolus-Levitin theorem. 

A fundamental, exact consequence of quantum mechanics: any physical system with total mass-energy $M$ has an absolute ceiling on how fast it can transition between distinct quantum states:

$$\frac{dN}{dt} \le \frac{2 E}{\pi \hbar} = \frac{2 M c^2}{\pi \hbar}$$

Mass is not an inert lump of substance resting in a room. Mass is an intense concentration of causal state transitions—an update-rate density that consumes local relational bandwidth.

And because high update density congests the network, electromagnetic wavefronts propagating through that congestion experience an effective optical refractive index:

$$n(r) = 1 + \frac{2GM}{c^2 r}$$

Light rays bend not because a hypothetical graviton pulls them sideways through an empty void, but because the wave propagates slower through the dense causal network near a mass. Planetary bodies follow curved paths for the exact reason a beam of sunlight bends when it enters a pool of water: Fermat’s principle of least time across an optical refractive gradient.

Ryan leaned back, the pencil resting between his knuckles.

The theory was clean. It had no free parameters, no unobservable dark fluid, and no background coordinates. But natural philosophy without numbers is poetry.

He turned to his Linux workstation and opened a terminal.

"Let's see what happens," he said, "when we put the relations against the sky."
"""),

    (2, "The Weight of Relations", "Chapter_02_The_Weight_of_Relations.md", r"""# CHAPTER TWO
## The Weight of Relations

To confront a theory of pure relations against real astrophysics, one needs the most unforgiving celestial clock in the sky.

Ryan Vance found it in the public radio archives of the Netherlands Institute for Radio Astronomy: **PSR J0337+1715**.

Located four thousand two hundred light-years away in the constellation Taurus, J0337+1715 was a millisecond pulsar—a city-sized ball of degenerate neutrons weighing 1.44 times the mass of the Sun, spinning on its axis three hundred and sixty-six times every second. With every rotation, its magnetic lighthouse beam swept past Earth, producing radio pulses of crystalline precision.

What made J0337 unique across the known universe was its companion system. It was locked in a tight, 1.63-day orbit with a degenerate helium white dwarf of 0.2 solar masses, and that entire inner binary was orbited by a second, outer white dwarf of 0.4 solar masses with a 327-day period.

A true relativistic three-body system.

In 2018, an international team led by Anne Archibald had published four years of pulse data in *Nature*, testing whether the extreme gravitational binding energy of the neutron star caused it to accelerate differently in the outer star’s gravitational field than the white dwarf. They had confirmed Einstein’s Strong Equivalence Principle to within $2.6 \times 10^{-6}$.

Ryan downloaded the full archive: twenty-seven thousand one hundred and ten raw Times of Arrival (TOAs) recorded across four years by Green Bank, Arecibo, and Westerbork:

```bash
curl -O https://data.astron.nl/pulsar/J0337+1715/archibald_2018_toas.tim
```

In standard astrophysics, fitting those twenty-seven thousand timestamps required supercomputer clusters running TEMPO2, integrating high-order post-Newtonian equations inside an artificial solar-system barycentric Cartesian grid ($x, y, z$). It had taken thousands of CPU hours.

Ryan opened his code editor and began writing `qrc_three_body_engine.cpp`.

---

### The Shape Sphere

He did not set up an origin at $(0, 0, 0)$. In a three-body system, an origin is a fiction; the universe has no nail driven into the center of mass.

Instead, Ryan formulated the dynamics entirely through **Jacobi relational vectors**:
$$\mathbf{r}_1 = \mathbf{x}_2 - \mathbf{x}_1$$
$$\mathbf{r}_2 = \mathbf{x}_3 - \frac{m_1 \mathbf{x}_1 + m_2 \mathbf{x}_2}{m_1 + m_2}$$

Vector $\mathbf{r}_1$ described the relation between the pulsar and its inner white dwarf. Vector $\mathbf{r}_2$ described the relation between the outer white dwarf and the inner pair’s center of mass. 

He scaled both by their reduced masses, forming mass-weighted vectors $\mathbf{u}$ and $\mathbf{v}$, and mapped their inner products directly onto **Montgomery’s Shape Sphere**:

$$w_x = \|\mathbf{u}\|^2 - \|\mathbf{v}\|^2$$
$$w_y = 2 (\mathbf{u} \cdot \mathbf{v})$$
$$w_z = 2 (\mathbf{u} \times \mathbf{v})$$

On this two-dimensional sphere, the three-body problem ceased to be an intractable nine-variable mess in empty space. The size of the triangle was scale; its rotation in space was orientation; its position on the sphere was pure shape. Collinear configurations sat on the equator; equilateral Lagrange triangles sat at the poles. The gravitational dance was transformed into the motion of a single point moving along a geodesic on a curved surface.

He compiled the code on his workstation using an eighth-order Dormand-Prince integrator (DOP853) with first post-Newtonian (1PN) Einstein-Infeld-Hoffmann relativistic corrections:

```bash
g++ -O3 -march=native qrc_three_body_engine.cpp -o qrc_engine
./qrc_engine --dataset archibald_2018_toas.tim --threads 8
```

He pressed Enter.

The eight cores of his desktop CPU engaged with a muted hiss from the cooling fan.

On the screen, the solver marched through four years of cosmic data:

```
[QRC-ENGINE v1.0] INGESTING ARCHIBALD 2018 ARCHIVE: 27,110 TOAs
EPHEMERIS WINDOW: MJD 55928.14 TO MJD 57328.91 (1,400.77 DAYS)
INITIAL RESIDUAL RMS: 412.48 MICROSECONDS
PASS 1: RMS = 28.14 MICROSECONDS
PASS 2: RMS = 2.18 MICROSECONDS
PASS 3: RMS = 1.54 MICROSECONDS
CONVERGENCE ACHIEVED: DELTA_RMS < 1.0e-8 SECONDS
TOTAL COMPUTE TIME: 248.3 SECONDS (4 MINUTES, 8 SECONDS)
```

Ryan leaned back.

Four minutes. On an ordinary desktop computer, the relational Jacobi model had solved the non-linear three-body equations across four years of data, accounting for orbital precession, gravitational redshift, and the Shapiro delay.

He plotted the post-fit residuals.

Twenty-seven thousand one hundred and ten points formed a perfectly flat, Gaussian white-noise ribbon across four years, centered precisely on zero, with an RMS scatter of **1.54 microseconds**—matching the thermal noise limit of the cryogenic receivers.

---

### The Honest Receipt

Ryan did not celebrate. He was a metrologist.

He wrote a second verification script: `matched_cartesian_check.py`. He took the identical physical force models—the same point-mass gravities, the same 1PN relativistic terms—and integrated the system in standard barycentric Cartesian coordinates.

He ran the differential comparison:
$$\Delta \mathbf{r}(t) = \|\mathbf{r}_{\text{Jacobi}}(t) - \mathbf{r}_{\text{Cartesian}}(t)\|$$

The terminal printed the maximum trajectory divergence across the entire four-year integration:

`MAX_COORDINATE_DIVERGENCE: 0.000120 METERS (0.12 MM)`

Ryan smiled, a quiet, tight expression.

A change of coordinates never alters a physical prediction. Jacobi coordinates did not magically beat the laws of gravitation; they agreed with Cartesian coordinates to a tenth of a millimeter.

The value of relations was not that they cheated physics. The value was that **they kept the bookkeeping honest**. The relational model didn't carry an imaginary solar-system barycenter that no spacecraft could ever touch. It carried the clocks that actually existed.
"""),

    (3, "Tides in the Granite", "Chapter_03_Tides_in_the_Granite.md", r"""# CHAPTER THREE
## Tides in the Granite

The subterranean vault in Giles County, Tennessee, was eight hundred feet below the rolling limestone hills, excavated into a formation of Ordovician carbonate so dense that microseismic surface vibrations died within forty feet of the surface.

The air in the tunnel stayed at a constant eleven degrees Celsius year-round, smelling of damp limestone dust and chilled hydraulic oil. Down the center of the unlit access gallery stretched a continuous, evacuated aluminum conduit enclosing a twelve-hundred-meter optical fiber loop: a ground-anchored Sagnac ring interferometer.

Ryan Vance sat on an overturned plastic equipment crate beside the laser injection rack, adjusting the polarization paddle of a single-mode diode laser.

He was measuring the lunar diurnal $O_1$ tide.

As the Moon circled the Earth every twenty-four hours and fifty minutes, its gravitational gradient did not merely tug on the Atlantic Ocean. It stretched the solid crust of North America by thirty centimeters, deforming the limestone strata beneath Tennessee.

In general relativity, this tidal deformation was described by tensor equations of spacetime curvature. In Quantum Relational Causality, the Moon's proximity altered the local causal update rate of the crust, introducing a subtle, measurable refractive impedance shift:
$$\Delta n = \frac{2 G M_{\text{Moon}}}{c^2 r_{\text{Moon}}}$$

On the oscilloscope screen, the Sagnac interference fringes shifted with the exact phase of the celestial clock overhead: a sinusoidal phase drift of twelve point four picoseconds, tracking the Moon’s declination with zero anomalous lag.

The cell phone resting on the equipment case vibrated against the plastic, buzzing loudly in the acoustic stillness of the vault.

Ryan picked it up. The caller ID showed an area code from southeast Texas: `281-483-XXXX`.

Building 30 at Johnson Space Center. Houston.

He swiped the screen. "Vance."

"Ryan, don't hang up," Dr. Elena Rostova said.

Her voice was strained, frayed by thirty straight hours at a flight dynamics console, competing against the background hum of high-volume air handlers and the muffled murmur of a mission simulation loop.

"I'm eight hundred feet underground, Elena," Ryan said. "Why are you calling my personal number?"

"We just aborted the final integrated ascent and translunar injection simulation for Artemis-7," she said, speaking rapidly. "At $T$ minus eighteen minutes."

Ryan stood up, brushing limestone dust from his trousers. "What failed?"

"The navigation filter," she replied. "We were running the high-fidelity insertion scenario into Low Lunar Orbit—a 100-kilometer circular polar parking orbit. During the trans-Earth injection burn, when the vehicle passed through the Earth-Moon $L_1$ gravitational neck, the state covariance matrix inside GEONS blew up."

---

### The Legacy Trap

GEONS—the Goddard Enhanced Onboard Navigation System—was the crown jewel of NASA’s autonomous flight software. It had flown on dozens of missions across three decades, from low Earth orbiters to deep-space probes.

"What did the eigenvalues do?" Ryan asked.

"The position variance collapsed," Elena said bitterly. "Axiom-Lockheed runs GEONS on a radiation-hardened BAE RAD750 processor. The board runs at one hundred and thirty-three megahertz, with single-precision floating-point registers. To make the orbital propagation fit within the processor's execution budget, the contractor took a formal waiver: they truncated the covariance matrix from sixty-four-bit double precision to thirty-two-bit single precision."

Ryan let out a short, harsh breath. "Single precision in a multi-body gravity neck? That leaves twenty-four bits of mantissa. You lose the least significant bits on every ninety-second integration step."

"Exactly," Elena said. "When the spacecraft coasts in solar quiet, no optical fixes arrive because the star trackers are blinded by lunar albedo. The covariance propagates by dead reckoning alone. The lunar gravity gradient stretches the covariance ellipse along the velocity vector, while the transverse variances round down to zero. Then, the moment a candidate optical fix arrives from the horizon sensor, the innovation covariance is indefinite. The filter accepts a negative variance, divides by zero, and the flight computer triggers a hardware watchdog reset."

"And what did Mission Control do?"

"Flight Director Lin called a simulated vehicle loss," Elena said, her voice dropping. "If this happens in real flight, the crew enters the lunar occultation with a corrupted state vector. TCM-3 burns open-loop into the farside terrain at two kilometers per second."

She paused. In the silence of the Tennessee cavern, Ryan could hear her drawing a ragged breath.

"Ryan, three months ago at the Green Bank seminar, you said you were developing a relational three-body engine that bypassed background coordinates. Can you turn that into a real-time flight navigation package?"

Ryan looked at the Sagnac optical loop stretching into the dark tunnel, where photons were measuring the Moon's gravity without asking any human for an origin point.

"I have the orbital mechanics and the pulsar timing," Ryan said. "I fitted four years of triple-star data in four minutes. But turning it into flight software means putting it on edge silicon—independent hardware that can fly on a spacecraft without calling home to Houston or waiting for a supercomputer."

"Can you do it?" she pressed.

"Not with standard Kalman math," Ryan answered. "Because the moment an independent researcher tries to build autonomous multi-body navigation on edge silicon, you hit the amateur's compute wall. You hit single-precision truncation, rank starvation, and covariance collapse."

"Then find an edge board and fix it," Elena said. "Because I am not going to sit at a GNC console in Houston and watch four astronauts die because prime contractors waived basic arithmetic."
"""),

    (4, "The Seven-Watt Partition", "Chapter_04_The_Seven_Watt_Partition.md", r"""# CHAPTER FOUR
## The Seven-Watt Partition

After hanging up with Elena, Ryan Vance did not sleep.

At dawn, as the freezing rain coated the windshield of his Subaru, he drove thirty miles northeast along Route 460 into Roanoke. He parked behind an industrial automation surplus depot, walked up to the trade counter, and spent his last four hundred dollars on a single commercial edge development board: an **NVIDIA Jetson Orin Nano**.

He did not have a corporate cost-plus contract or a multi-million-dollar government grant. Prime aerospace contractors solved numerical stability by throwing fortunes at the sky: radiation-hardened mainframes, liquid-cooled server racks running 128-bit linear algebra libraries, backed by teams of software engineers tuning flight parameters in real time.

Ryan had four hundred dollars and a bench-top direct-current power supply capped at precisely seven point two watts.

Back in his Blacksburg garage, he bolted the credit-card-sized board to the aluminum mounting plate on his workbench. He wired its serial bus to his Linux terminal, connected its 5-volt power rails, and flipped the toggle switch.

A tiny green surface-mount LED began pulsing on the board—one beat per second—drawing seven watts.

"If the math can't survive on seven watts," Ryan said to the freezing room, "the math isn't true."

---

### The Negative-NIS Breakdown

He opened a fresh directory: `cislunar_recovery_bench/`.

He began by implementing the exact algorithm flown by NASA: a classical Extended Kalman Filter (EKF) using standard Joseph-form covariance updates, fusing simulated optical star-tracker bearings and lunar limb measurements with inertial measurement unit (IMU) accelerations in Low Lunar Orbit.

At 09:30 AM, he launched his first 30-day continuous simulation on the Jetson Nano.

Twenty-five minutes into the run, the terminal threw an unrecoverable exception:

```
FATAL EXCEPTION: SIGFPE - FLOATING POINT EXCEPTION
MATRIX_INVERSION_ERROR: COVARIANCE_MATRIX_IS_NOT_POSITIVE_DEFINITE
DIAGONAL_ELEMENT_P[3,3] = -1.72950e-05
NORMALIZED_INNOVATION_SQUARED: -503.186075
CONDITION_NUMBER: 2.3918e+24
CORE DUMPED.
```

Ryan leaned back, staring at the screen. He slowly pushed his glasses up his nose.

"There it is," he murmured. "The smoking gun."

He had just reproduced, on his kitchen-table edge board, the exact mathematical catastrophe lurking inside NASA’s multi-billion-dollar flight software.

The failure was subtle, insidious, and devastating.

In linear estimation theory, the covariance matrix $P$ represents the estimator's uncertainty regarding the physical state of the spacecraft (position and velocity in three dimensions). By mathematical definition, a covariance matrix must be symmetric and positive-definite: all its diagonal elements—the variances—must be strictly positive real numbers ($\sigma^2 > 0$).

In theoretical textbooks, the classical Joseph-form covariance update:
$$P_{k|k} = (I - K_k H) P_{k|k-1} (I - K_k H)^T + K_k R K_k^T$$
is algebraically guaranteed to preserve symmetry and positive-definiteness.

"Algebraic guarantees," Ryan said bitterly, sketching the matrices on a legal pad, "mean nothing to a thirty-two-bit floating-point processor."

During measurement gaps—when the spacecraft passed behind the lunar farside or was blinded by solar glare—no optical fixes arrived. With every ninety-second propagation step, the lunar gravity gradient stretched the covariance along the orbital track. In limited precision, the ratio between the largest eigenvalue and the smallest eigenvalue exploded past $10^{24}$. The matrix collapsed toward rank one.

When an optical fix finally arrived, the innovation covariance $S_k = H P_{k|k-1} H^T + R$ became indefinite. The matrix solve returned an impossible negative Normalized Innovation Squared:
$$\text{NIS} = \mathbf{y}_k^T S_k^{-1} \mathbf{y}_k = -503.18$$

And the flight software contained a fatal, one-sided gate:
```c
if (nis <= NIS_GATE_35) { // Evaluates TRUE for -503.18!
    joseph_update(&x, &P, &K, &y); // Commits corrupted state!
}
```

The filter looked at a negative number, concluded it was smaller than thirty-five, and committed a corrupted state vector with negative velocity variances directly into the flight computer.

---

### The Square-Root Solution

Ryan rubbed his tired eyes. The fix could not involve more compute; the Jetson was drawing seven watts, and flight processors had even less.

"Stop inverting the matrix," he said aloud. "Never form $P$ directly."

He scrapped the classical EKF. Instead, he formulated the **Square-Root Information Filter (SRIF)**.

Instead of carrying the covariance $P$, the algorithm carried its lower-triangular Cholesky factor $L$, where:
$$P = L L^T$$

To incorporate a measurement, Ryan refused to form the innovation covariance $S_k$. Instead, he stacked the measurement sensitivity matrix $H$ and the noise factors into a single composite matrix and applied a **Householder QR decomposition**:

$$\begin{bmatrix} L_R & 0 \\ H L_P & L_P \end{bmatrix} \xrightarrow{\text{QR}} \begin{bmatrix} L_S & K_L \\ 0 & L_{P,+} \end{bmatrix}$$

The updated factor $L_{P,+}$ was lower-triangular by mathematical construction. Its square, $L L^T$, was guaranteed to be strictly positive-definite under all conditions, even in single precision.

And the Normalized Innovation Squared? 

Instead of inverting $S_k$, Ryan solved the whitened innovation vector $\mathbf{w}$ via simple triangular back-substitution:
$$L_S \mathbf{w} = \mathbf{y}$$
$$\text{NIS} = \|\mathbf{w}\|^2 = \sum_{i=1}^m w_i^2$$

A sum of squares of real numbers.

"A sum of squares," Ryan whispered, "can never be negative. Not on a supercomputer, and not on seven watts."

To complete the stack, he integrated **FixedQP**: a receding-horizon optimal controller with a 256-iteration projected-gradient integer core. It solved a 36-variable trajectory optimization every thirty minutes, replanning within six seconds of CPU time and cutting propellant consumption by 20.7% compared to standard target-point guidance.

And behind the planner, he placed a **diverse Cartesian verifier**: an independent software channel written in plain Cartesian coordinates that screened every commanded burn for clearance, fuel reserve, and corridor bounds before anything fired.

At 03:00 AM on the third day, Ryan launched a 120-day continuous Low Lunar Orbit simulation on the Jetson Nano: five thousand seven hundred and sixty thirty-minute planning windows.

Twelve hours later, the terminal completed the run:

```
[CISLUNAR-OS BENCHMARK] 120-DAY LLO SIMULATION COMPLETE
TOTAL PLANNING WINDOWS: 5,760 / 5,760 PASSED
NEGATIVE NIS EXCEPTIONS: ZERO (0)
MAXIMUM CONDITION NUMBER: 4.12e+04
TOTAL DELTA-V CONSUMED: 166.9 M/S (20.7% BELOW BASELINE)
DIVERSE VERIFIER FAULTS: ZERO (0)
BOARD POWER CONSUMPTION: 5.63 WATTS AVERAGE
```

Ryan picked up his phone and called Houston.

"Elena," he said, as she answered on the first ring. "I have your flight stack. It runs on seven watts, it never produces a negative variance, and it doesn't ask Houston where the Moon is."
"""),
]

def main():
    print(f"Writing {len(CHAPTERS_DATA)} canonical chapters...")
    for num, title, filename, content in CHAPTERS_DATA:
        filepath = os.path.join(MANUSCRIPT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"  Created: {filename} ({title})")

if __name__ == "__main__":
    main()
