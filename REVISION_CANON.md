# Revision canon for The Impedance Threshold: Argonaut

Source of truth for the November 2026 science revision. Every chapter edit follows this file. It records what the book may claim, grounded in the author's own work:

- QRC research: `~/QRC_Quantum_Relational_Causality` (status: `docs/QRC_PROJECT_STATUS.md`, current position dated 2026-11-19; foundation: `docs/QRC_CAUSAL_IMPEDANCE_GATE_FORMULATION.md`).
- Pulsar bench: `github.com/H-XX-D/qrc-pulsar-benchmark` (README; `docs/cislunar-error-budget-and-advantage.md`; `docs/controller-tuning-and-advantage.md`; `docs/navigation-recovery.md`).

## 1. QRC as the book states it

- Foundational statement: the underlying condition of space is 0D and nonlocal; particle fields are 1D excitations; electromagnetic excitations are 2D; their composition supports the experienced 3D world; time is the fourth dimension that encompasses its history. `c` is the maximum causal update and propagation rate.
- Exact wording to use: **distance is the inferred measurement of causal impedance.** Impedance does not cause distance, produce it, or "resist" anything through a medium. Do not call spacetime a medium or a fabric that impedes.
- `Z_H` means the causal-impedance response data of a relational configuration or history `H`. QRC deliberately has not yet fixed its mathematical type. It is **not** `c^3/G`, not a resistance, not a mass flow rate. Remove every `Z_H = c^3/G` statement.
- Author's intent (2026-11-22): the book is fiction so that QRC can be shown in a universe where it turns out to be true, without a peer-review gate. A skeptical physicist reading it should think "that's odd, that works", and should find no easy error to dismiss it with. That means:
  - Every QRC statement traces to the actual mathematics in the QRC repo (definitions, gate structure, derived results) and is stated at the strength the math supports.
  - Nothing contradicts data we already have (DESI, Planck, GW170817, Europa, rocket physics, real mission numbers).
  - The engineering stays practical.
  - This prequel is near-term and defensible; the later trilogy may become pure science fiction.
- Status in-world: in 2026 QRC is a research program. Gate 1 (recovering three-dimensional space from the 0D condition) is the furthest along; propagation, gravity, gauge and particle-spectrum gates are open. Characters may believe it and argue for it, and later chapters may show hard-won in-world progress on open gates as long as it contradicts neither the math nor known data. Institutions in the prequel certify **navigation performance**, not QRC as proven physics. Avoid "QRC has proven X" unless the repo's mathematics actually proves X.
- Faster than light: QRC opens no route around `c`, and no experiment in the book finds one. Characters say exactly that. No "vacuum decoherence", no "total matter dissolution", no "0D Space Invariance principle forbids warp bubbles".
- Dark energy (tested 2026-11-22 against Pantheon+, DES-Dovekie, DESI DR1 BAO and the chronometers; see QRC audits/2026-11-22_real_data/RESULTS.md):
  - **Boundary (agegraphic, Cai and Wei-Cai form, credited):** n = 1 is rejected. Fitted n ≈ 2.85 gives w0 ≈ -0.80 and wa ≈ +0.14, the wrong sign versus DESI, with Δχ² ≈ +4: mildly disfavored. In Ch 3 Elena catches the sign.
  - **Memory (retarded causal kernel):** ρ_DE = K∫e^{-(t-t')/τ} S dt' with S = ρ_m/(ρ_m+2ρ_r)·sqrt(ρ_m) and τ = 1.35/H0. It gives w0 ≈ -0.80 and wa ≈ -0.17 (DESI's sign) and Δχ² +0.2 to +1.7 versus ΛCDM: consistent, neither preferred nor excluded. The mechanism is open; the trace-anomaly derivation fails. Ryan calls it 'a fitting function with a story attached'.
  - **Never use:** R_h = ct, H0 = 1/t0 as parameter-free, the holographic H² law, Z_H = c³/G, or the old multi-survey 'certified' results.

## 1b. The lineage and timeline (the author's spine for the whole book)

### The real chronology the book mirrors (from the repos and Recall)

| When (2026) | What | Where |
|---|---|---|
| August to November | QRC research: the 0D foundation, causal impedance, the gates | `QRC_Quantum_Relational_Causality` (repo created Aug 10) |
| Oct 30 | J0337+1715 relational three-body engine: Jacobi state, shape-sphere evolution benchmarked against Cartesian, 1PN EIH forces, Archibald post-fit residuals (27,110 TOAs, RMS 1.54 us), SEP diagnostics | `qrc-pulsar-benchmark` |
| Oct 30 to Nov 1 | The same codebase grows GNC: Earth-Moon station-keeping, the Jacobi predictive controller, MPC and FixedQP, square-root filter and reacquisition, a Jovian sample-return/XNAV concept | `qrc-pulsar-benchmark` |
| November | Autonomous flight software: cleanroom native C++ on edge silicon, LLO residence. It imports the bench's JacobiFlightModel, RoutineMPC and FixedQP | Autonomous GNC Stack |
| Nov 3 onward | ARGONAUT: the outer-system science campaign, built on autonomous navigation | Recall `obs_654c`, `obs_0aff` |
| Nov 22 | This novel | |

### How the links work (state them this way in the book)

1. **QRC → pulsar timing: a direct link.**
   - J0337+1715 is where QRC's relational view of three bodies meets real data. Pulse arrival times are pure relations between clocks: distance inferred from the measured causal delay, the exact operational meaning QRC gives to distance.
   - The Shapiro delay is the measured extra delay near mass, so in QRC language it is extra causal impedance.
   - J0337 is also the strongest test of the strong equivalence principle: Archibald et al. (2018) found the pulsar and the inner white dwarf fall alike to within 2.6e-6. Any relational theory of gravity must pass that test, so it is the first thing QRC has to survive.
   - In the book, Ryan's bench is QRC's first contact with data. Real numbers: residual scatter about 1.5 us; the full three-body model removes the nested-Kepler residual. The novelty is doing it live, on Jetson-class silicon.
2. **Pulsar timing → cislunar: an engineering link.**
   - Real-time three-body integration in Jacobi relational form, honest error bounds, and fast native code on a Jetson were exactly what onboard navigation needed. The bench's Jacobi model, QP controller and filters became the cislunar stack.
   - QRC opened the line of thought (build the state from relations); the engineering made it work. Navigation does not depend on QRC being true.
3. **Cislunar → ARGONAUT: a prerequisite.** Autonomy proven in cislunar space and LLO (Act II) is what makes an uncommanded Jupiter sample return thinkable (Acts III and IV). Pulsars return as a deep-space sensor there.
4. **QRC's own arc** runs alongside: the cosmology on the glass wall (Ch 3), the gates (Appendix A), the open tensions. In this prequel the reader sees why Ryan believes it and where it can still lose.

### Novel timeline (compressed, accelerated alternate history)

- **2026:** Green Bank bench (Ch 1); Houston and the bench becoming GNC (Ch 2); the Sagnac ring and cosmology (Ch 3); Plum Brook qualification (Ch 4).
- **Late 2026:** Artemis-7 blackout and rescue (Act II).
- **2027:** JWST plume confirmation → ARGONAUT (Ch 9).
- **2033:** launch.
- **2036:** Jupiter arrival.
- **2036 to 2040:** plume watch at Callisto.
- **May 2040:** harvest and seal.
- **Jan 20, 2041:** departure (Day 0).
- **2042:** Senate hearing.
- **Sep 27, 2043:** capture (Day 980).
- **Oct 5, 2043:** cleanroom.
- **Nov 14, 2043:** UN.
- **2058:** epilogue.

## 2. Navigation: what Ryan's system is and why it works

### Ryan's autonomous stack = ArgonautOS (depict it like this)

- **State.** An 18-state Jacobi relational state: the Moon relative to the Earth, the spacecraft relative to the Earth-Moon barycenter, and the Sun relative to the Earth-Moon barycenter (position and velocity each). Integrated with an eighth-order integrator (DOP853) under the gravity of all the bodies. It is a description of how the bodies stand relative to one another; there is no grid nailed to the stars.
- **Navigation.** An extended Kalman filter with full covariance and a Joseph-form update. Inputs: optical position fixes, bearings to the Moon, and IMU accelerations driving the prediction. In-world, after the failure below, Ryan's flight filter carries its covariance in square-root form with causal reacquisition. That repair is real and comes from the author's benchmark repo.
- **Guidance.** A QP receding-horizon controller. It replans on 1,800-second intervals over a horizon of several intervals ("base" profile 12 intervals, "sparse" profile 4), executes only the first burn, then replans. The plan carries an interval-arithmetic certificate.
- **Safety.** Three planner channels vote: a software triplex running on one processor, so not hardware redundancy. A separate **diverse first-command verifier**, written in plain Cartesian coordinates on purpose, independently checks every first command for clearance, fuel and authority before anything fires. A prepare-before-issue journal means a burn is recorded before it is commanded and survives a reboot. The protective planner and coast-lock logic are Ryan's (they exist in the author's earlier package); keep them.
- **Authority.** Ground keeps HMAC-signed STOP, TAKEOVER, STAGE and COMMIT commands. The concept is ground-supervised autonomy: ground observes and directs, and the spacecraft does not need the DSN for routine navigation or commanding.
- **Software and hardware.** NASA core Flight System. In the author's world the mission phase sequencer runs on cFS Draco (v7.0.1); navigation and control run as cFE apps. Native C++, bench-tested on a Jetson Orin Nano held to 7 W. Python is ground tooling and reference models only. Ryan may add an FPGA coprocessor in the story; it is fiction beyond the bench.

### Why it works (the honest version, which the characters may say)

- A change of coordinates never changes a physical prediction. The author's own matched tests found Jacobi and Cartesian equivalent to within 0.00012 m; for that controller, equality was structurally guaranteed. Shape-sphere evolution ran about 9 times slower than Jacobi.
- Ryan chose Jacobi relational coordinates because they say what the system is, a set of relations, and they keep the bookkeeping honest. He makes no claim that they beat the physics. A good beat is to let him admit this, with the receipt.
- The measured gains came from elsewhere:
  - **Decision-making.** In matched tests the predictive receding-horizon guidance cut tracking RMS 14.6 percent and delta-v 20.7 percent against a tuned target-point controller, but used 25 percent more CPU and won outright in only 2 of 6 cases. The MPC used 40 percent less delta-v than PID at 7.6 percent higher RMS.
  - **Estimator discipline.** The negative-NIS covariance failure: after prolonged rejection of fixes, the covariance collapses toward rank one, an impossible negative NIS is accepted, and a corrupted update commits before it is checked. It was fixed with square-root filtering and causal reacquisition.
  - **Architecture.** Voting channels, the diverse verifier, the journal, and ground authority.
- Bench results worth quoting, as simulation (synthetic sensors, simulated plant):
  - The six-hour autonomous campaign ended the base profile 0.435 m from target on 0.035 kg of propellant with point-mass gravity, and 12.5 to 16.6 m off with fuller physics.
  - The sparse profile first failed (768.7 m against a 500 m limit) and was then fixed.
  - The slowest planning call took 6.93 s of a 10 s budget.
  - Fault drills included a cFE restart mid-outage and a physical reboot of the main board while a second Nano held the burn record.
  - Failures are kept on the record, and Ryan does the same.
- Do not claim:
  - "first autonomous cislunar navigation" in the high halo orbit (CAPSTONE flew onboard autonomous navigation in the NRHO in 2022 to 2023). The author's system targets **low lunar orbit** (LLO) residence and station-keeping, a harder regime: roughly two-hour orbits, mascons tugging on every pass, and Earth occulted for a large part of each orbit. Ryan may say LLO is what he built it for. Simulated LLO evidence: 120 days, 5,760 half-hour windows, 166.9 m/s; 30-day runs passed against both gravity models.
  - flight-qualified FPGA hardware in the 2026 to 2027 part of the story;
  - NRHO operations as already demonstrated;
  - "zero divergence" or perfect anything.

### Pulsars (Act I bench and deep space only)

- The Green Bank Pulsar Bench mirrors the author's qrc-pulsar-benchmark repo: J0337+1715 timing and three-body evolution in Jacobi form. In the story Ryan runs a full three-body timing model live on Jetson-class hardware at the telescope.
- Pulsars are **not** part of Ryan's cislunar navigation. In the author's real stack XNAV is only a simulated sensor model. In the story, X-ray pulsar timing is added as **one extra sensor** for deep space (the Jupiter legs and the ghost run), feeding the same filter. Sources are J0437-4715, B1821-24, B1937+21 and J0030+0451. Each fix takes hours of photons and is good to about 1 to 5 km, with integer-cycle ambiguity resolved by the filter's prior. Optical navigation tightens it near targets. Timing is in microseconds, not nanoseconds.

### Mathematics the characters must get right

- Signed shape-sphere map: `w_x = |u|^2 - |v|^2`, `w_y = 2 u.v`, `w_z = 2 (u x v)`, with no absolute value. The poles are the equilateral triangles of opposite orientation, the equator the collinear configurations, and the binary collisions three punctures on the equator. Kinetic energy `T = (1/2)(|u'|^2 + |v'|^2)`.
- Planar three-body counting: 6 configuration coordinates, minus 2 (translation), 1 (rotation) and 1 (scale), leaves 2. Phase space is 12-dimensional. Planar rotation is SO(2).
- McGehee coordinates handle **triple** collision; binary collisions are regularized with Levi-Civita or Kustaanheimo-Stiefel. Chaos and non-integrability hold in every chart.
- Integrator-failure demo: Burrau's Pythagorean problem (masses 3, 4, 5 at rest on a 3-4-5 triangle), not the figure-eight. The figure-eight exists by a variational proof, has no closed form, and is numerically linearly stable.
- J0337+1715: TEMPO2's built-in binary models are two-body; the real system needed a full three-body timing model (Ransom et al. 2014, offline). Residual scatter is sub-microsecond to microsecond.
- NRHO station-keeping is small and physical, under about 1 m/s per year with good navigation. Navigation error and guidance policy drive the cost; the orbit is never "free".

### Act II mechanisms (the Artemis blackout)

- The book runs on an accelerated alternate timeline for Artemis and Gateway; the front matter says so in one line. Europa plumes are confirmed in 2027 by JWST imaging, not by Europa Clipper (which arrives in 2030).
- The blackout is an intense **solar radio burst near new Moon**. The Moon sits close to the Sun in the sky, so every DSN antenna pointed at Prometheus also takes the burst into its sidelobes, and the S-band and X-band receivers are swamped for hours. Solar flares cause HF absorption, not S- or X-band blackouts. The Gateway 1550 nm optical link is immune to radio noise, which is why the laser relay works. Prometheus carries only a short-range optical crosslink to Gateway, not a ground-capable optical terminal.
- The false position jump comes from **solar-energetic-proton hits** on the optical navigation and star-tracker detectors (real: proton strikes create false stars and corrupt limb fits). It does not come from sodium glare. Keep the angle-to-distance geometry consistent.
- The GEONS failure mirrors the real bug the author found and fixed in their own filter: after prolonged rejection of fixes the covariance collapses toward rank one, the gate accepts an impossible negative NIS, and the update commits before validation. GEONS then believes the corrupted fix. Ryan recognizes it because his own filter failed exactly this way on the bench, and he kept the receipt. His Jetson runs square-root covariance with causal reacquisition, rejects the fix, and its QP receding-horizon planner, checked by the diverse verifier, produces the recovery burn. The handover arrives as a signed TAKEOVER and COMMIT over the laser relay.
- Delta-v must match the error being corrected. Light times: about 1.28 s one way and 2.56 s round trip at lunar distance; scale for the actual range.

## 3. Mission timeline and propulsion (Acts III to V)

- Launch: August 2033. Depot reaches Jupiter: November 2036.
- November 2036 to April 2040: the depot sits in the Callisto radiation haven while the team watches Europa for an active plume. Europa's plumes are intermittent and contested; waiting for a confirmed strong one is the reason for the delay.
- Plume harvest: **May 4, 2040** (Plume #3, Manannán region). Skimmer departs the depot **April 28, 2040**; the Callisto-to-Europa half-ellipse takes about 112 hours.
- Laser seal at the depot: May 12, 2040. The sealed canister then waits about eight months in the depot's shielded vault for the next Jupiter-to-Earth window. Windows open about 85 to 90 days before Jupiter's opposition (Dec 2039, Jan 2041).
- Departure from Callisto: **January 20, 2041** = Day 0. Jupiter is near aphelion (about 5.45 AU), where a minimum-energy return takes about 1,058 days. The 980-day transfer is slightly faster than minimum energy, paid for by margin in the departure burn. Day 980 = **September 27, 2043**, Gateway capture.
- Senate hearing during the cruise: spring 2042. Elena Vance (born 2026) is 16 in 2042.
- Cleanroom opening: **October 5, 2043** (weld made "three years earlier"). UN broadcast: **November 14, 2043**. Preface delivered December 2043. Epilogue: 2058.
- Propulsion: Canister 1 cannot coast home unpowered. It rides in a two-stage storable-bipropellant **Return Stack** (about 1.9 t wet, Isp about 320 s):
  - Departure stage: about 4.8 km/s from Callisto orbit to the Earth-return transfer, then jettisoned.
  - Capture stage: a 3.86 km/s perigee burn at 600 km on Earth arrival (arrival speed relative to Earth 9.72 km/s for the 980-day transfer), followed by a lunar flyby and small trims (tens of m/s) into Gateway's NRHO. The departure needs 4.63 km/s, so the 4.8 km/s stage has a 170 m/s margin.
  - Cold-gas thrusters handle attitude and the small cruise trims. The aim point is biased so that a failed capture burn means a harmless Earth flyby, never an atmospheric entry.
  - "Ghost run" means no ground commands and no transmissions; the stack executes its burns autonomously under ground-supervised authority.

## 4. Writing rules for revised text

- Keep the author's plot, characters, chapter structure, image-plate references and markdown formatting. Change the minimum needed to make a statement true.
- New or rewritten sentences use no em dashes or en dashes (commas, colons, semicolons, periods or parentheses instead). Do not rewrite untouched existing sentences only to remove dashes.
- When a fix removes a false dramatic beat, replace it with a true one of similar weight. Real failure modes, real risk and real numbers are better drama.
