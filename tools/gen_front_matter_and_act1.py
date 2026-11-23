#!/usr/bin/env python3
"""
Generate Front Matter, Chapters 1-4, and Dossier I from scratch.
Author: Todd Hendrixx
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

FRONT_MATTER = r"""# THE IMPEDANCE THRESHOLD: ARGONAUT
## A Novel of Relational Spaceflight & First Life
### Canonical Prequel to the Exospecies Survey Series
#### By Todd Hendrixx

---

![Sol Navigation Directorate: Master Mission Architecture](assets/plate_01_front_matter_architecture.png)

---

## DRAMATIS PERSONAE

### The Pulsar Bench & Cislunar Pioneers (2026–2030)
* **Dr. Ryan Vance:** Protagonist. Astrodynamicist, relational metrologist, and Lead Guidance, Navigation, and Control (GNC) Architect for Project ARGONAUT. Originator of the Quantum Relational Causality (QRC) theoretical framework. Former post-doctoral researcher at Green Bank Observatory. Independent developer of ArgonautOS on edge silicon. Driven by an uncompromising reverence for physical clocks and measurable relations.
* **Dr. Elena Rostova:** Senior Flight Dynamics Specialist at NASA Johnson Space Center and Goddard Space Flight Center. Co-architect of the Cislunar Optical Communication (O-COMM) network. Former test director for the Lunar Gateway Power and Propulsion Element. Fierce, brilliant, with an intuitive mastery of chaotic three-body phase space.
* **Marcus Thorne:** Lead Flight Dynamics Officer (FIDO), Mission Control Center, Houston (Building 30). Veteran of the Artemis program. Unflinching under telemetry emergencies; identifies the fatal covariance starvation failure aboard *Prometheus*.
* **Sarah Lin:** NASA Flight Director, Mission Control Center, Houston ("Iron Sarah"). Procedurally rigorous, decisive, and the executive authority who authorizes the emergency laser takeover of Artemis-7.

### Project ARGONAUT Directorate & Science Team (2030–2043)
* **Dr. Aris Thorne:** Lead Astrobiologist, NASA Jet Propulsion Laboratory and Lunar Receiving Laboratory. Elder brother to Marcus Thorne. World authority on deep-sea hydrothermal extremophiles and chemosynthetic metabolic pathways. Designer of the graded silica aerogel cassette.
* **Dr. Kenji Sato:** Lead Materials Engineer, Sandia National Laboratories and Goddard Space Flight Center. Fabricator of the 10-kilogram titanium-alloy return canister (Canister 1) and master of the spaceborne ytterbium fiber laser welding system.
* **Senator Thomas Sterling:** Chairman of the Senate Commerce, Science, and Transportation Subcommittee on Space. Fiscal hawk who challenges the silent 980-day uncommanded ghost run of Canister 1.

### The Architect of the Foundation (2043–2058)
* **Dr. Elena Vance:** Daughter of Ryan Vance, named in honor of Dr. Elena Rostova. Born in 2026 during the initial Pulsar Bench trials. Educated at Cambridge and Caltech; becomes Chief Metrologist of the Sol Navigation Directorate, guiding the four-century technological campaign that culminates in the launch of the **IAS *Daedalus***.

---

## PREFACE: ON THE FALLACY OF THE BACKGROUND CONTAINER
### By Dr. Ryan Vance, Mission Director, Project ARGONAUT
*Delivered at the Lunar Gateway Institute for Relational Physics, December 2043*

For four centuries, physics has labored under a single mathematical convenience: the assumption of the background container.

Isaac Newton called it *Absolute Space*—a rigid, immutable three-dimensional room existing prior to, independent of, and indifferent to whatever matter was placed within it. Albert Einstein warped the room into a dynamical Riemannian manifold ($g_{\mu\nu}$), but the container remained: a smooth four-dimensional sheet onto which events were plotted like pins on a chart.

In deep space navigation, that habit nearly cost humanity its future.

Not because a coordinate grid is wrong—any honest chart, Cartesian or otherwise, predicts the same physical sky. It nearly cost us because we forgot that the grid is human bookkeeping, and began trusting our coordinates more than our instruments.

When a flight computer models an interplanetary spacecraft as an isolated state vector in an unmeasurable solar coordinate system, every unmodeled force—every photon of solar radiation pressure, every micro-puff of outgassing, every thermal imbalance—becomes an error that grows quadratically with time. Left unmeasured across nine hundred and eighty days between Jupiter and Earth, those errors grow to tens of thousands of kilometers. A spacecraft that misses its destination does not miss because of its coordinates; it misses because its navigation software believed it knew more than it had measured.

The universe contains no empty rooms.

There is no background stage. There is no pre-existing coordinate grid stretching between the stars. The universe consists of causal relations between physical interactions. Distance is not an empty interval across which things travel; **distance is the inferred measurement of causal impedance between things that touch.**

Gravity is not an exchange of hypothetical graviton particles across a void. It is the macroscopic optical refractive impedance of the causal network:
$$n(r) = 1 + \frac{2GM}{c^2 r}$$

Light rays bend and planetary orbits curve along minimum-action Fermat geodesics through that refractive gradient. A mass remains continuously bound to everything in its causal past; only dynamic accelerations shed transverse tensor waves propagating across the horizon at $c$.

When Canister 1 crossed six hundred and twenty-eight million kilometers of interplanetary void without a single radio command from Earth, it did not wait to be told where it was. It measured its own relations: the arrival times of X-ray pulses from four millisecond pulsars, the angular bearings to the Sun and the stars, and the steady count of its own atomic clock. It treated every estimate as a hypothesis to be tested against the next measurement, and it never let itself be more certain than its data allowed.

And when we opened that canister in the cleanroom of Lunar Gateway, we discovered that the relational nature of reality does not end with physics. It reaches into biology.

Life is not a fragile, improbable miracle that occurred once on Earth by supernatural luck. Two independent origins in a single solar system prove that life is what non-equilibrium chemistry does when water meets warm catalytic stone. 

Life is simple.

It is the ladder above it—the steep, unforgiving physical rungs of gravity wells, ice shells, stellar flares, and causal horizons—that tests whether a living world can ever touch the stars.

---

## TABLE OF CONTENTS

### ACT I: THE PULSAR BENCH
* **Chapter 01:** The Gridless Sky
* **Chapter 02:** The Weight of Relations
* **Chapter 03:** Tides in the Granite
* **Chapter 04:** The Seven-Watt Partition
* **Inter-Act Dossier I:** The Green Bank Pulsar Baseline & Relational Reduction

### ACT II: THE CISLUNAR CRUCIBLE
* **Chapter 05:** Flare State
* **Chapter 06:** The Negative Variance
* **Chapter 07:** Dead Man's Trajectory
* **Chapter 08:** Light Across the Blind Spot
* **Inter-Act Dossier II:** The Artemis-7 Cislunar Anomaly & Autonomous Recovery

### ACT III: THE CALLISTO STAGING
* **Chapter 09:** The Ocean Beyond the Ice
* **Chapter 10:** Catching Smoke
* **Chapter 11:** Fire on the Water
* **Chapter 12:** The Cold Sanctuary
* **Inter-Act Dossier III:** Project ARGONAUT Phase C Critical Design Review

### ACT IV: THE EUROPA SKIMMER
* **Chapter 13:** The Dive into the Belt
* **Chapter 14:** Forty-Two Seconds
* **Chapter 15:** The Glass Seam in the Dark
* **Chapter 16:** The Silent Arc
* **Chapter 17:** Gravity's Needle
* **Inter-Act Dossier IV:** Europa Plume Encounter & 980-Day Autonomous Flight Report

### ACT V: THE LIVING GRAIN
* **Chapter 18:** The Quarantine Gate
* **Chapter 19:** Life Is Simple
* **Chapter 20:** The Rungs Above the Water
* **Chapter 21:** Epilogue — The North Sea Horizon
* **Inter-Act Dossier V:** Gateway Bio-Quarantine Audit & IAS Daedalus Foundation

---

### DIEGETIC EXHIBITS & MATHEMATICAL APPENDICES
* **Exhibit A:** The ARGONAUT Flight Schedule & System Specification (`argonaut_timeline.py`)
* **Exhibit B:** The Square-Root Innovation Gate & Negative-NIS Repair (`loss_of_track.py`)
* **Exhibit C:** The Protective Autonomous Recovery Planner & Diverse Verifier (`protective_planner.py`)
* **Exhibit D:** Green Bank Pulsar Residual Timing Logs for PSR J0337+1715
* **Exhibit E:** Cryogenic Aerogel Cassette Laser-Weld & Mass Spectrometry Log
"""

CH1 = r"""# CHAPTER ONE
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
"""

CH2 = r"""# CHAPTER TWO
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

The eight cores of his desktop CPU engaged with a muted whir from the cooling fan.

On the screen, the progress counter began ticking through the twenty-seven thousand one hundred and ten pulse arrival times:

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
"""

CH3 = r"""# CHAPTER THREE
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
"""

CH4 = r"""# CHAPTER FOUR
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
"""

DOSSIER1 = r"""# INTER-ACT DOSSIER I
## The Green Bank Pulsar Baseline & Relational Reduction
### Document Classification: NASA-GSFC / NRAO Joint Technical Memorandum 2026-QRC-01
#### Date of Archival: October 28, 2026 | Location: Green Bank, West Virginia & Houston, Texas

![PSR J0337+1715 Timing & Montgomery Shape Sphere](assets/plate_02_dossier_1_pulsar_bench.png)

### 1.0 ASTROPHYSICAL CONTEXT & CELESTIAL CLOCK ARCHITECTURE

PSR J0337+1715 is a millisecond pulsar with a rotational period $P = 2.732588147618\text{ ms}$, exhibiting an intrinsic spin-down rate $\dot{P} \sim 10^{-20}\text{ s/s}$. The pulsar is embedded in a hierarchical three-body stellar system consisting of two degenerate helium white dwarf companions:

* **Inner Companion ($m_1$):** Degenerate helium white dwarf, $m_1 = 0.1975 M_\odot$, relative orbital semi-major axis $a_1 = 0.0319\text{ AU}$, orbital period $P_{\text{inner}} = 1.6294\text{ days}$. Eccentricity $e_{\text{inner}} = 0.00069$.
* **Outer Companion ($m_2$):** Degenerate helium white dwarf, $m_2 = 0.4104 M_\odot$, semi-major axis of its orbit about the inner binary $a_2 = 1.18\text{ AU}$, orbital period $P_{\text{outer}} = 327.25\text{ days}$. Eccentricity $e_{\text{outer}} = 0.0353$.
* **Pulsar Primary ($m_p$):** Highly relativistic neutron star, $m_p = 1.4378 M_\odot$, surface magnetic field $B \approx 2 \times 10^8\text{ Gauss}$.

Because the gravitational field of the outer companion strongly perturbs the inner binary orbit, PSR J0337+1715 represents the premier natural laboratory in the galaxy for testing the Strong Equivalence Principle (SEP) and non-linear multi-body gravitational interactions. Archibald et al. (2018) found that the neutron star and the inner white dwarf fall toward the outer white dwarf alike to within $2.6 \times 10^{-6}$.

---

### 2.0 THE ACHROMATIC TIMING ANOMALY

During an eleven-hour continuous integration campaign on October 14, 2026, raw Time-of-Arrival (TOA) timestamps were logged using both the observatory's standard VEGAS pulsar backend (processed via TEMPO2 in the solar-system-barycentric frame, with its built-in nested binary model) and the experimental QRC relational pipeline running a full three-body timing model. Per-TOA scatter was about $1.5\,\mu\text{s}$ in both pipelines.

#### 2.1 Multi-Frequency Observation Matrix
To determine whether the systematic residual observed in TEMPO2 was an artifact of interstellar dispersion measure ($\Delta\text{DM}$) or plasma fluctuations in the solar wind, interleaved observations were conducted in three radio frequency bands, switching receivers between scans:

*Multi-Frequency Timing Data (fitted amplitude of the structured TEMPO2 residual: P-Band 820 MHz: 3.72 ± 0.09 µs; L-Band 1400 MHz: 3.71 ± 0.05 µs; S-Band 2100 MHz: 3.70 ± 0.11 µs) confirms no chromatic dispersion ($\Delta t \propto f^0$), establishing that the residual is not plasma-induced. See Plate QRC-GBO-0226 above.*

#### 2.2 Analytical Proof of Non-Dispersion Origin
In astrophysical plasma physics, the group delay $\Delta t_{\text{plasma}}$ induced by an ionized electron column density $\text{DM}$ scales inversely with the square of the electromagnetic observation frequency:

$$\begin{aligned} \Delta t_{\text{plasma}} &= \frac{e^2}{2\pi m_e c} \cdot \frac{\text{DM}}{f^2} \\ &\approx 4.1488 \times 10^3 \cdot \text{DM} \cdot f^{-2} \text{ s} \end{aligned}$$

If the 3.71-microsecond residual were attributable to interstellar or ionospheric dispersion fluctuations, the residual ratio between 820 MHz and 2,100 MHz would follow:

$$\frac{\Delta t(820\text{ MHz})}{\Delta t(2100\text{ MHz})} = \left( \frac{2100}{820} \right)^2 \approx 6.558$$

The observed ratio was:

$$\frac{\Delta t(820\text{ MHz})}{\Delta t(2100\text{ MHz})} = \frac{3.72\,\mu\text{s}}{3.70\,\mu\text{s}} = 1.01 \pm 0.04$$

**Engineering Determination:** The timing residual is achromatic across a factor of 2.5 in electromagnetic frequency. The residual cannot be caused by plasma dispersion, electron column variations, solar wind scattering, or receiver front-end chromatic dispersion. It is the signature of the model, not of the sky: TEMPO2's built-in binary models treat the system as two-body (nested Keplerian or post-Keplerian) orbits, while in J0337+1715 the outer white dwarf continuously perturbs the inner orbit. When the QRC pipeline's full three-body timing model is applied in place of the nested model, the 3.71-microsecond structure vanishes into the $1.5\,\mu\text{s}$ white-noise floor.

**Relational note (R. Vance):** A pulse arrival time is a relation between two clocks, the pulsar's and ours. Distance here is never measured directly; it is inferred from causal delay, which is the operational meaning QRC gives to distance (the inferred measurement of causal impedance). The Shapiro delay near the white dwarfs is, in that language, the measured optical refractive impedance $n(r) = 1 + 2GM/c^2 r$ of the relational network near mass. Light bends because the refractive gradient bends the wavefront by Fermat's principle; gravity does not involve an exchange of graviton particles. In the 5.23-year stream archive comprising 27,110 TOAs, once the 246 instrumental pointing, plasma, and RFI anomalies are scrubbed, the Archibald 1PN three-body model leaves a dipole residual below $0.25\,\mu\text{s}$ at $0.12\sigma$—zero unmodeled leakage. The strong-equivalence bound is the first exam any relational theory of gravity has to pass; here, the relational impedance model matches General Relativity to parts in a million without invoking background coordinates or quantum gravitons.

---

### 3.0 TRANSCRIPT: EXCERPT FROM THE NASA JSC FLIGHT DYNAMICS REVIEW
#### Date: June 18, 2026 | Location: Building 30, Room 312, Houston, Texas

**DR. ELENA ROSTOVA (Deputy Chief, Cislunar Flight Dynamics):**
"Dr. Vance, the committee has reviewed your submission: the Jacobi relational navigation package and the Montgomery Shape Sphere diagnostics. The mathematics are undeniably elegant. But I must ask you the same question the Flight Director asked me this morning: why should the National Aeronautics and Space Administration trust anything but fifty years of flight-proven Cartesian Kalman filtering?"

**DR. RYAN VANCE (GNC Architect, Project ARGONAUT):**
"You shouldn't trust it because of the coordinates, Dr. Rostova. My Jacobi state and a Cartesian state with the same forces agree to a tenth of a millimeter in my own matched tests, and they should; a change of coordinates never changes a physical prediction. I use relations because they say what the system is: the Moon from the Earth, the spacecraft and the Sun from the Earth-Moon barycenter. It's honest bookkeeping. The ship carries the Sun and the Moon inside its own state instead of asking the ground where they are.

"What I'm asking you to trust is what the bench forced on me. A predictive planner that replans every thirty minutes and, in matched tests, used about twenty percent less delta-v than tuned target-point guidance, though it only won outright in two cases of six. An estimator that doesn't lie to itself when it has to reject fixes for hours. Three planner channels that must agree, and a separate verifier written in plain Cartesian coordinates that checks every command for clearance, fuel and authority before anything fires. I built it for low lunar orbit: two-hour orbits, mascons tugging on every pass, Earth blocked for a large part of each orbit, nobody on the ground able to steer even when the radios work.

"Now consider the bad day. A solar radio burst swamps the ground receivers. Protons hit the optical sensors and make false stars. Your filter rejects fix after fix, correctly, for hours. Mine did that on the bench, and then its covariance broke, it accepted a negative NIS, and it committed a corrupted update. I have the receipt. I fixed it with a square-root filter and causal reacquisition, and I can show you the replay. If you want a spacecraft to survive when Earth is silent, you need software that knows when it doesn't know."

**MARCUS THORNE (Lead FIDO, Artemis-7):**
"Elena, look at his bench data. Six-hour autonomous campaigns on a seven-watt board. A cFE restart in the middle of an outage. A main board physically rebooted mid-burn while a second board held the burn record. And he brought his failures. Nobody brings their failures."

**DR. ELENA ROSTOVA:**
"Marcus, you know the Level-1 flight software rules as well as I do. We cannot replace the Honeywell primary GNC computer with an uncertified research board. Sarah Lin would be stripped of her flight director certification before the week is out."

**MARCUS THORNE:**
"Then we don't replace the Honeywell. We fly the Jetson as a shadow processor on the auxiliary payload bus. We give it raw 1553 bus telemetry. We let it run its own navigation and planning in parallel, with no command authority. If Artemis-7 goes smoothly, the Jetson logs its data and proves the concept. But if the primary filter loses lock, if we hit a blackout and GEONS panics, ground keeps signed authority: STOP, TAKEOVER, COMMIT. We give ourselves a parachute."

**DR. ELENA ROSTOVA (pausing, looking at the display):**
"If we do this, Marcus, it must be documented as an experimental payload under Safety Protocol 14-B. If the flight directors find out we are using a secondary payload to shadow the primary GNC without formal Level-1 flight qualification waivers, they will ground us all. Dr. Vance, prepare your flight binary. It still has to qualify at Plum Brook. You have your shadow slot."
"""

def main():
    files = [
        ("Front_Matter.md", FRONT_MATTER),
        ("Chapter_01_The_Gridless_Sky.md", CH1),
        ("Chapter_02_The_Weight_of_Relations.md", CH2),
        ("Chapter_03_Tides_in_the_Granite.md", CH3),
        ("Chapter_04_The_Seven_Watt_Partition.md", CH4),
        ("Dossier_Act_I.md", DOSSIER1),
    ]
    for filename, content in files:
        path = os.path.join(MANUSCRIPT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Generated: {filename}")

if __name__ == "__main__":
    main()
