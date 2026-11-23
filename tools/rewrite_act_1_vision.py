import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

ch1 = r"""# CHAPTER ONE
## The Three-Body Clock
### The 0D Condition

The power supply fan on the workbench had an irritating high-frequency rattle that Ryan Vance had been trying to ignore since midnight.

It was 03:14 AM in an unheated garage workshop behind a rental house outside Blacksburg, Virginia. Outside, an autumn frost was settling across the Blue Ridge foothills, stiffening the fallen oak leaves on the gravel driveway. Inside, the only heat came from a ceramic space heater glowing orange under the desk and the exhausted warm air blowing off an exposed aluminum heatsink.

On the desk sat a green circuit board no larger than a deck of playing cards: an NVIDIA Jetson Orin Nano, powered by a 12-volt bench supply with a digital ammeter showing a steady current draw of 0.58 amps.

Seven watts.

Ryan rubbed his eyes, his knuckles catching on three days of beard stubble. On his 27-inch monitor, two terminal windows were open side by side. On the left was an open-source C++ codebase compiled with `-O3 -march=native`. On the right was a scratchpad document titled `QRC_FOUNDATIONS.md`.

For three years, Ryan had watched the theoretical physics community run itself into an intellectual dead end. 

The establishment had spent fifty years and billions of dollars chasing string theory into a landscape of ten to the five hundredth metastable vacua, inventing extra spatial dimensions that could never be observed, and inventing hypothetical supersymmetric particles that never showed up in the Large Hadron Collider. When astronomical surveys measured the accelerating expansion of the universe, they patched their equations with an ad-hoc cosmological constant fine-tuned to one hundred and twenty decimal places. When galactic rotation curves didn't match Newton, they invented cold dark matter particles that stubbornly refused to interact with any detector on Earth.

They treated space like an enormous, pre-existing spreadsheet. An infinite Euclidean box with rows and columns. When a planet or a photon moved, the equations simply updated the coordinates $(x, y, z)$.

"Nobody asks who updates the spreadsheet," Ryan muttered to himself, reaching for a mug of black coffee that had gone cold two hours ago. "Nobody asks what the clock rate of the universe is."

### Distance as Impedance

Ryan set the mug down, his fingers hovering over the mechanical keyboard.

He wasn't an academic with tenure, and he wasn't a corporate aerospace contractor with a cost-plus grant. He was an independent programmer and metrologist who had spent fifteen years writing embedded flight control software for small research satellites. He knew that in the real world of microcontrollers and physical sensors, there is no such thing as an abstract coordinate.

Every sensor measurement is a physical relation between two events.

"Start from nothing," Ryan typed onto the scratchpad. "The fundamental condition of reality is zero-dimensional and non-local. Spacetime is not a container, not a fabric, and not an ether. Space is an emergent network of causal connections."

He stared at the blinking cursor, feeling the quiet, electrifying clarity that comes when a tangled mathematical problem suddenly untangles itself into a single clean line.

"Distance is the inferred measurement of causal impedance:

$$d \equiv \int Z_H \, d\tau$$

"Impedance doesn't cause distance. It doesn't resist anything through a medium. There is no medium. Distance is simply how long it takes for a causal update to propagate across a network of discrete relational state transitions."

He picked up a ballpoint pen and scribbled the Margolus-Levitin theorem on the back of an envelope:

$$\frac{dN}{dt} \le \frac{2 E}{\pi \hbar} = \frac{2 M c^2}{\pi \hbar}$$

"The Margolus-Levitin bound," Ryan murmured. "The fundamental quantum limit on state transitions. Mass-energy is not stuff packed into a box. Mass is an intense localized density of state updates! When you place a massive body—an Earth, a Moon, a star—into a region of space, you concentrate trillions of quantum state transitions every second. The local network capacity becomes saturated. It experiences network latency."

He leaned back in his chair, looking at the ceiling joists.

"Gravitational time dilation isn't space stretching," he whispered. "It's network ping time. A photon passing near a massive body appears to slow down because the wavefront experiences Fermat refraction across an update-latency gradient:

$$n(r) = 1 + \frac{2GM}{c^2 r}$$

"And because it is an informational latency inherent to the network itself, it is strictly achromatic. Radio, optical, X-rays—they all slow down by the exact same nanosecond count."

It was a breathtakingly simple, elegant concept.

But in physics, an elegant concept on a scratchpad is worth exactly nothing without empirical data.

### The Archive

Ryan opened a new browser tab and navigated to the public open-access data repository of the Green Bank Telescope and the North American Nanohertz Observatory for Gravitational Waves.

If Quantum Relational Causality was real, it had to show up in the cleanest, most demanding three-body laboratory in the galaxy: **PSR J0337+1715**.

Discovered in 2014, J0337 was a millisecond pulsar four thousand light-years away in the constellation Taurus. It spun on its axis three hundred and sixty-six times every second, emitting a beam of synchrotron radio waves with the regularity of an atomic clock. But unlike isolated pulsars, J0337 was locked in an intense, hierarchical three-body orbit with two degenerate helium white dwarf stars.

The inner companion, a white dwarf of 0.2 solar masses, whirled around the pulsar once every 1.63 days. The outer companion, weighing 0.4 solar masses, circled the inner pair every 327 days.

Because the outer star pulled on the inner binary with fierce gravitational tides, the system was the ultimate real-world test of the Strong Equivalence Principle (SEP)—the cornerstone of general relativity which dictates that all bodies, regardless of their gravitational self-energy, fall with the exact same acceleration in an external gravitational field.

In 2018, Anne Archibald and an international team of radio astronomers had published a landmark paper analyzing 27,110 individual pulse arrival times collected over four years, demonstrating that the pulsar and its inner white dwarf fell alike to within 2.6 parts per million.

Ryan found the direct download link for the raw data file: `j0337_archibald2018_toas.dat`.

File size: 4.8 megabytes.

"Twenty-seven thousand, one hundred and ten pulse arrival times," Ryan said, clicking the download button. "Let's see what happens when we build a three-body relational engine on a seven-watt board."
"""

ch2 = r"""# CHAPTER TWO
## The Montgomery Shape Sphere
### The 27,110 Pulses

The raw dataset downloaded in four seconds.

Ryan unpacked the text file into his project directory: `~/qrc-pulsar-benchmark/data/`. Each row in the file represented a single pulse Time of Arrival (TOA) recorded at Green Bank, Arecibo, or Westerbork, stamped with a topocentric arrival time measured against an observatory hydrogen maser to fifty picoseconds of precision.

In the standard astrophysical pipeline, pulsar timing used a massive legacy software suite called **TEMPO2**. 

TEMPO2 was a venerable, half-million-line collection of Fortran and C code developed over thirty years. It worked by transforming topocentric arrival times into the solar system barycenter frame, then predicting pulse arrival times using an analytic post-Keplerian binary model. For a triple system like J0337, TEMPO2 handled the three-body problem the only way it knew how: by nesting two independent two-body Keplerian ellipses one inside the other, dressed in a series of empirical post-Keplerian correction parameters.

On the screen, Ryan looked at the post-fit residuals published by the Archibald team.

When the nested-Kepler model was fitted against the real data, the residuals were not a flat line. They exhibited a structured, sinusoidal wave with an amplitude of nearly four microseconds.

"Because they're fitting two separate ellipses to a non-linear three-body manifold," Ryan said, opening his C++ editor. "Three bodies do not move in nested two-body orbits. They interact continuously."

### Building the Jacobi Engine

Ryan began writing the core dynamics module: `qrc_pulsar_bench/dynamics.py` and its native C++ backend `jacobi_symplectic_core.cpp`.

Instead of setting up an arbitrary Cartesian origin in deep space and tracking twelve independent coordinates $(x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3)$, Ryan formulated the equations of motion in **Jacobi relational coordinates**:

$$\mathbf{r}_1 = \mathbf{x}_2 - \mathbf{x}_1$$

$$\mathbf{r}_2 = \mathbf{x}_3 - \frac{m_1 \mathbf{x}_1 + m_2 \mathbf{x}_2}{m_1 + m_2}$$

Vector $\mathbf{r}_1$ was the relative separation between the pulsar and its inner white dwarf companion. Vector $\mathbf{r}_2$ was the vector from the inner binary's center of mass to the outer white dwarf.

The equations described purely how the bodies stood relative to one another. There was no absolute coordinate origin nailed to the stars. The translations were quotiented out.

He added the first-order Post-Newtonian (1PN) Einstein-Infeld-Hoffmann (EIH) relativistic corrections, accounting for the gravitational self-energy of the neutron star. Then he paired the dynamics with an eighth-order Dormand-Prince (DOP853) adaptive-step numerical integrator.

He hit compile.

`g++ -O3 -std=c++17 -march=native -shared -fPIC dynamics_core.cpp -o dynamics_core.so`

The Jetson Nano's heatsink warmed slightly. After twenty seconds, the terminal prompt returned clean. Zero errors. Zero warnings.

Ryan loaded the Archibald dataset into the Python harness and executed the fit:

`python3 run_pulsar_fit.py --dataset archibald2018 --engine jacobi_dop853`

### The Receipt

On the small terminal window, the processor threads pegged at ninety-five percent. The Jetson's 7-watt power indicator ticked up to 7.4 watts.

For four minutes, the algorithm processed the 27,110 pulse arrival times, integrating the coupled three-body trajectory across four years of orbital motion.

Then the terminal printed the final statistics:

`============================================================`  
`PSR J0337+1715 THREE-BODY RELATIONAL FIT COMPLETE`  
`TOTAL TOAs EVALUATED: 27,110`  
`POST-FIT RESIDUAL RMS: 1.542602 us`  
`STRONG EQUIVALENCE PRINCIPLE DELTA: < 2.6e-6 (CONFIRMED)`  
`WALL-CLOCK RUNTIME: 242.4 SECONDS`  
`TOTAL POWER CONSUMED: 0.49 WATT-HOURS`  
`============================================================`  

Ryan leaned back, a low whistle escaping his lips.

The structured 4-microsecond residual wave that had plagued the nested-Keplerian model had vanished. The post-fit residuals had collapsed into a clean, gaussian, white-noise scatter with an RMS of 1.54 microseconds—the fundamental thermal noise floor of the Green Bank cryogenic receiver.

And he had run the entire four-year, three-body relativistic simulation on an edge board that drew less power than an LED hallway nightlight.

### The Honest Null

Ryan didn't celebrate. He had been an engineer long enough to know that the easiest person to fool is yourself.

He opened a new script: `compare_coordinates.py`.

He wanted to know: did the Jacobi relational coordinates possess an intrinsic physical advantage over classical Cartesian coordinates? Did his relational formulation magically beat Newton and Einstein?

He ran a rigorous, side-by-side benchmark, integrating the exact same J0337 trajectory using 18-state barycentric Cartesian coordinates versus his 12-state Jacobi relational coordinates, holding the numerical tolerances identical at $10^{-13}$.

Ten minutes later, the comparison numbers appeared on the screen:

`COORDINATE CONSISTENCY CHECK:`  
`MAXIMUM TRAJECTORY DIFFERENCE: 0.000120 METERS (0.12 MM)`  
`STEADY-STATE RMS DELTA: 0.00000000 METERS`  
`ONLINE CPU TIME (CARTESIAN): 18.08 SECONDS`  
`ONLINE CPU TIME (JACOBI):    19.04 SECONDS`  

Ryan stared at the numbers, then burst into a dry, self-deprecating laugh.

"Of course," he said, shaking his head. "A change of coordinates never changes the physics."

The physics was identical. Down to a tenth of a millimeter across a four-year orbit spanning millions of kilometers, the Cartesian and Jacobi equations gave the exact same answer. Jacobi wasn't faster; in fact, it was five percent slower because of the coordinate translation arithmetic.

The advantage of QRC wasn't magic coordinates. It was conceptual honesty: describing the physical relations as they actually existed in nature.

And now, looking at the code on his screen, Ryan realized something far more dangerous.

This three-body relational engine wasn't just an astrophysical tool for analyzing dead pulsars in deep space.

It was a real-time, high-precision guidance and navigation filter.

And right now, four hundred miles to the south, NASA was preparing to launch three human beings toward the Moon using flight software that couldn't handle three bodies without crashing.
"""

ch3 = r"""# CHAPTER THREE
## The Expanding Causal Boundary
### The Houston Connection

The phone on the workbench vibrated against the plywood desk, buzzing like an angry hornet.

Ryan picked it up. The caller ID showed a Houston area code: `281-483-XXXX`. Building 30 at the Johnson Space Center.

He swiped the screen. "Vance."

"Ryan, it's Elena," Dr. Elena Rostova said without saying hello. Her voice was muffled by the ambient hum of air conditioning and the distant murmur of flight controllers. "Are you in front of your terminal?"

Dr. Elena Rostova was the Lead Guidance, Navigation, and Control Flight Officer for the Artemis program. She and Ryan had met six years earlier at an AIAA astrodynamics conference in Long Beach, where they had bonded over a shared, venomous contempt for aerospace contractor bloat. Elena had a PhD in celestial mechanics from Caltech, a commercial pilot's license, and an absolute intolerance for administrative bullshit.

"I'm at my bench," Ryan said. "What's wrong?"

"We just ran the final end-to-end mission sim for Artemis-7," Elena said, her voice dropping into a guarded, cautious register. "We simulated the perilune insertion burn with the primary star-tracker optical navigation loop closed. The run crashed at $T$ minus eighteen minutes."

Ryan sat up straight, his fatigue vanishing. "How did it crash?"

"Covariance collapse in GEONS," Elena replied. "As the vehicle entered the Earth-Moon three-body threshold, the filter began rejecting optical star-tracker fixes. The Normalized Innovation Squared ticked past sixteen point eight. The fault management software declared a primary sensor anomaly, disarmed the AJ10 main engine, and threw the simulation into `PROTECTIVE_SCREENED_COAST`."

"And on a real flight?"

"On a real flight, *Prometheus* skims past the Moon at twenty-two hundred meters per second, misses orbital insertion, and flings itself into an unrecoverable solar orbit," Elena said grimly. "We killed the simulated crew."

### The Single-Precision Wall

Ryan pulled up the NASA Goddard documentation for GEONS—the Goddard Enhanced Onboard Navigation System used on Orion and Artemis.

"Elena, what precision is your flight processor running?"

"Single-precision thirty-two-bit floating point," Elena said, her frustration bleeding through the phone line. "The avionics architecture uses BAE RAD750 single-board computers. The hardware was certified in 2002. Prime contractor Axiom-Lockheed refuses to upgrade to modern 64-bit multi-core SoCs because certifying a new radiation-hardened processor would cost fifty million dollars and slip their delivery schedule by two years."

"Thirty-two bits," Ryan repeated, shaking his head in disbelief. "In thirty-two-bit IEEE 754 floating point, you only have twenty-four bits of mantissa. That's seven decimal digits of precision."

"I know the math, Ryan!" Elena snapped. "When you propagate a three-body trajectory near the collinear Lagrange neck, the gravitational potential of the Earth and the Moon cancel out to four decimal places. When you subtract two numbers that are nearly equal in single precision, you suffer catastrophic roundoff cancellation. You lose four digits of precision. You're trying to calculate an orbital state with three significant figures!"

"And what did Flight Director Hastings say when the sim crashed?"

"Hastings blamed the sim team," Elena said bitterly. "He claimed the simulation engineers injected unrealistic star-tracker noise into the synthetic sensor feed. He said the Axiom software passed four thousand Monte Carlo runs at Huntsville and that the flight software is 'certified by pedigree.' They're waiving the fault as a non-conformance artifact."

"They're launching in three weeks, Elena," Ryan said.

"That's why I'm calling you," Elena said quietly. "You've been working on a three-body relational engine on that toy board in your garage. Does it work?"

"I just fitted twenty-seven thousand real pulsar pulses across a four-year relativistic orbit to one point five microseconds," Ryan answered. "On a seven-watt Jetson board."

A long silence hung on the line.

"Can you turn it into a flight navigation filter?" Elena asked.

"Not with standard software," Ryan said. "Because the moment you try to run real-time orbit estimation on edge silicon, you hit the amateur's compute bottleneck."
"""

ch4 = r"""# CHAPTER FOUR
## The Silicon Horizon
### The Amateur's Bottleneck

After hanging up with Elena, Ryan sat in the freezing garage for an hour, staring at the green LED on the Jetson Orin Nano.

An amateur researcher working on a $400 edge board faces a brutal reality that institutional aerospace never experiences. NASA and prime contractors solve their numerical problems by throwing millions of dollars of compute at them: multi-node server clusters running double-precision 64-bit and quadruple-precision 128-bit linear algebra libraries with gigabytes of RAM.

Ryan didn't have a cluster. He had an embedded ARM Cortex processor with eight gigabytes of shared memory, running on a 7-watt power budget.

He began coding an extended Kalman filter (EKF) to fuse simulated optical star-tracker fixes with IMU accelerations for an Earth-Moon cislunar trajectory.

At 06:30 AM, he ran his first 30-day simulation of a spacecraft in Low Lunar Orbit (LLO).

Thirty seconds into the run, the terminal threw an exception:

`FATAL EXCEPTION: SIGFPE - FLOATING POINT EXCEPTION`  
`MATRIX_INVERSION_ERROR: COVARIANCE_MATRIX_IS_NOT_POSITIVE_DEFINITE`  
`DIAGONAL_ELEMENT_P[3,3] = -1.72950e-05`  
`NORMALIZED_INNOVATION_SQUARED: -503.186075`  
`CORE DUMPED.`  

Ryan rubbed his face with his hands. "There it is."

He had just reproduced the exact mathematical catastrophe that was lurking inside NASA's flight software.

### The Negative-NIS Collapse

The failure was insidious.

In classical Kalman filtering, the covariance matrix $P$ represents the estimator's uncertainty. By mathematical definition, a covariance matrix must be symmetric and positive-definite: all its diagonal elements (the variances) must be strictly positive numbers.

In theory, the Joseph-form covariance update guarantees symmetry. But on a low-power processor running in limited precision, numerical subtraction of large, nearly equal floating-point numbers causes catastrophic loss of significance. 

When a spacecraft experiences a prolonged measurement gap—such as when Earth is occulted behind the Moon, or when a star tracker is blinded by solar glint—the state covariance grows large. Then, when a new measurement finally arrives, the calculation of the Kalman gain involves inverting the innovation covariance matrix $S_k = H P_k H^T + R$.

Due to roundoff errors in the matrix inversion, the covariance matrix $P$ collapsed toward rank one.

The condition number of the matrix blew up to $2.39 \times 10^{24}$.

When the filter computed the Normalized Innovation Squared (NIS)—the statistical test that determines whether a sensor measurement is valid:

$$\text{NIS} = \mathbf{y}^T S^{-1} \mathbf{y}$$

The inverted matrix $S^{-1}$ had developed a negative eigenvalue. The solve returned an impossible negative value: $\text{NIS} = -503.18$.

Because legacy NASA flight rules evaluated sensor validity using a simple inequality gate:

`IF (NIS <= 35.0) ACCEPT_MEASUREMENT;`

The code evaluated $-503.18 \le 35.0$ as **TRUE**.

The algorithm accepted a completely corrupted measurement on a negative NIS, applied the corrupted Joseph update, and produced a negative velocity variance: $-1.7295 \times 10^{-5}$.

The mathematics had literally broken arithmetic.

### The Square-Root Invention

Ryan pushed his keyboard back, grabbed a fresh legal pad, and began working by hand.

He couldn't buy a supercomputer. He had to make the mathematics impossible to break, even on a cheap 7-watt board.

"Never propagate the full covariance matrix $P$," Ryan wrote in bold block letters. "Propagate the square root."

If a covariance matrix is factored using a Cholesky or QR matrix decomposition:

$$P = L L^T$$

Where $L$ is a lower-triangular matrix, then by mathematical construction:

$$\mathbf{x}^T P \mathbf{x} = \mathbf{x}^T (L L^T) \mathbf{x} = (L^T \mathbf{x})^T (L^T \mathbf{x}) = \| L^T \mathbf{x} \|^2 \ge 0$$

The product of a matrix and its transpose is **always, unconditionally, non-negative**. It is structurally impossible for $P$ to develop a negative eigenvalue. It cannot lose positive-definiteness, no matter how much roundoff noise exists in the processor!

Ryan spent eight hours writing the new module: `navigation_recovery.py` and its native C++ implementation `hardware/orbit_mpc_core.cpp`.

He implemented the **Square-Root Information Filter (SRIF)** using Householder orthogonal transformations and QR factorization. Every measurement update was factored jointly, and the Normalized Innovation Squared was computed as a whitened squared Euclidean norm:

$$\text{NIS} = \| \tilde{\mathbf{y}} \|^2 \ge 0$$

Zero possibility of a negative NIS. Ever.

Then he added **Causal Reacquisition**: if an optical fix was rejected during an outage, the software did not blindly commit the state. It seeded a provisional tracking hypothesis, monitored it over three consecutive fixes across an hour, and only promoted it to the primary flight track if the residual 3-sigma uncertainty dropped below two hundred meters.

### The 256-Iteration Integer Core

Next came guidance.

NASA's Orion spacecraft relied on complex target-point targeting algorithms that required ground controllers to compute delta-v burns on supercomputers in Houston, then uplink the burn parameters over the Deep Space Network.

Ryan wanted total onboard autonomy. He wrote the **FixedQP Receding-Horizon Controller**:

- It solved a quadratic programming problem over a six-hour horizon (twelve 1,800-second intervals).
- It executed only the first burn, then replanned at the next interval.
- It used an accelerated projected-gradient algorithm fixed to exactly **256 iterations**.
- It used 64-bit fixed-point integer accumulators, eliminating floating-point non-determinism entirely.
- If the final projected residual failed the clearance screen, the optimizer published **zeros** rather than an unverified burn command.

He wired a **diverse first-command verifier**—written in plain Cartesian coordinates on purpose—to independently audit every single burn command for fuel, clearance, and authority before anything could fire.

At 18:45 that evening, Ryan ran the 120-day Low Lunar Orbit simulation on the Jetson Orin Nano.

For two hours, the 7-watt board chewed through 5,760 half-hour guidance cycles, simulating low lunar orbit under the brutal gravitational mascons of the Moon.

When the run completed, the terminal displayed:

`============================================================`  
`ARGONAUT_OS 120-DAY LOW LUNAR ORBIT RESIDENCE TEST`  
`TOTAL DURATION: 120 DAYS (5,760 DECISION CYCLES)`  
`STATION-KEEPING DELTA-V: 166.9 M/S (0.035 KG PROPELLANT EQUIVALENT)`  
`FINAL POSITION ERROR: 0.435 METERS`  
`NEGATIVE-NIS EVENTS: ZERO (12,683 / 12,683 NON-NEGATIVE)`  
`EXCEPTIONS / ASSERTION FAULTS: ZERO`  
`PEAK CPU POWER: 7.2 WATTS`  
`SLOWEST PLANNING CALL: 6.93 SECONDS (10.0 S BUDGET)`  
`============================================================`  

Ryan leaned back in his creaking chair, the cold room forgotten.

A 7-watt edge board on an amateur's desk had just completed a four-month autonomous lunar station-keeping campaign, landing within four decimeters of the target path, while consuming less energy than a laptop battery.

He picked up his phone and dialed Houston.

"Elena," Ryan said when she answered. "I have your filter."
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_01_The_Three_Body_Clock.md"), "w", encoding="utf-8") as f:
    f.write(ch1)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_02_The_Montgomery_Shape_Sphere.md"), "w", encoding="utf-8") as f:
    f.write(ch2)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_03_The_Expanding_Causal_Boundary.md"), "w", encoding="utf-8") as f:
    f.write(ch3)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_04_The_Silicon_Horizon.md"), "w", encoding="utf-8") as f:
    f.write(ch4)

print("Rewrote Act I to match the user's authentic creative vision successfully.")
