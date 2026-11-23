# qrc-pulsar-benchmark: research brief

Read-only review, 2026-11-22: nothing was built or run; test counts are as the repo reports them.

## Source state

- GitHub main is commit `04e56fb` (2026-11-02). The local copy at `/Volumes/Thunderbolt SSD/UserData/Relocated-20261102/qrc-pulsar-benchmark` has the same HEAD, so committed files match.
- The local tree is not clean: uncommitted edits to `README.md`, `cislunar_forces.py`, `compound_benchmark.py` and `qrc_engine.py`, plus about 45 untracked files (a "layered autonomy" campaign, six Python modules, about 30 C++ flight files such as `hardware/flight_avionics_core.cpp`, and build artifacts). This brief uses main; local-only items are marked.
- The repo was built in four days: 66 commits, 2026-10-30 to 2026-11-02.

## 1. Jacobi relational coordinates

**Three-body side.** `qrc_pulsar_bench/dynamics.py` integrates the 12-component Jacobi state (r1, v1, r2, v2) of a hierarchical triple with DOP853 under Newtonian gravity, optionally with first-PN EIH terms. `compare` runs a matched 18-component Cartesian integration; the README calls agreement coordinate consistency, not physical validation, and claims no speedup. Despite its name, `hardware/jacobi_symplectic_core.cpp` steps barycentric Cartesian point masses.

**Cislunar side.** `jacobi_control.py` uses a restricted state q = r_sc_rel_Moon + (1 - mu) r1, with the Earth-Moon vector r1 prescribed by an ephemeris spline. The "matched Cartesian" model in `adaptive_control.py` is the same class with that translation factor set to zero.

**Measured advantages: none established.**

- Tracking and fuel (`docs/controller-tuning-and-advantage.md`, six frozen nine-day cases): the identical predictive policy gave 291.64 m mean steady RMS and 0.5951 m/s in both coordinate systems (online CPU: Jacobi 19.04 s, Cartesian 18.08 s). Maximum differences were 0.000120 m in scenario steady RMS and 0.000000712 m/s in total delta-v. The doc concludes: "No unique Jacobi physical or control-policy advantage is established by this comparison."
- Computation at matched accuracy (same doc, two repetitions, Apple M2 Pro): Jacobi/Cartesian CPU ratios 1.14, 1.48 and 1.06 at a 0.1 m error target; 0.99, 0.89 and 1.06 at 1 m. The doc reports no general speed advantage.
- Shape coordinates (`docs/cislunar-error-budget-and-advantage.md`, isolated Newtonian Earth-Moon-spacecraft, under 1 m error): CAPSTONE geometry Cartesian 3.813 ms, Jacobi 3.601 ms, spatial shape 31.599 ms (8.78x Jacobi); LRO geometry 17.488, 17.248 and 166.864 ms (9.67x). At 0.1 m: 6.60x and 9.67x. Shape state is 112 bytes versus 96 for Jacobi, beside 118,096 bytes of degree-120 gravity coefficients either needs.
- Conditioning, a measured cost: the first 90-day Jacobi run differed from an independent Moon-centred control by 581.35 m because of a C2 cubic origin spline and loose tolerances; a quintic spline and tighter tolerances cut that to 0.626 m (`docs/jacobi-predictive-control.md`). The sweep JSON shows Jacobi needing tighter rtol (2e-13 versus 5e-12 on one geometry) for the same physical error, because q is measured from the barycentre. The spatial shape chart is singular at collinearity.
- Why no policy advantage could appear: actual and reference states receive the same translation, so delta_q = delta_r and delta_q_dot = delta_v; Jacobians, constraints and costs are identical in exact arithmetic.

**Separating the three effects (same campaign):**

- Coordinate effect: nil, as above.
- Guidance-policy effect: tuned predictive versus tuned target-point guidance gave 291.64 versus 341.49 m (14.6% lower RMS), 0.5951 versus 0.7508 m/s (20.7% less delta-v), at 25.0% more CPU. Predictive won both metrics in 2 of 6 cases, lost both in 2, traded in 2. In the 30-day case tracking tied (235.98 versus 235.93 m full interval) with 3.45% less delta-v, about 11 g of propellant. Tuned sampled PD met no training constraint (5,650.54 m).
- Estimator effect: the original raw-fix controller scored 1,121.42 m and 0.9376 m/s; that gain mixes filtering with retuning, and the doc credits it mainly to fault tolerance. The feedforward ablation (same filter, bias estimate withheld from guidance) improved both metrics in 5 of 6 cases but raised case C from 397.99 to 669.34 m, so mean RMS was worse (312.75 m).

## 2. QP receding-horizon controller

**Formulation** (`docs/artemis-predictive-mpc.md`, `predictive_mpc.py`): e[k+1] = Phi[k] e[k] + B[k] dv[k], linearized about a path propagated from the initial state only; quadratic tracking cost plus a delta-v penalty (a fuel proxy); per-axis bounds inside a 0.15 m/s cap; 30-minute updates; only the first burn executes, after a nonlinear clearance screen. No PID fallback.

**Integer core** (`hardware/orbit_mpc_core.cpp`): 36 variables (12 three-axis corrections), exactly 256 accelerated projected-gradient iterations, 64-bit accumulators, round-half-away-from-zero, output published only if the final projected residual passes, otherwise zeros. Two calls per decision (six for sparse policies). Format 24/16 first, then 32/24 because 24/16 shifted RMS 5.515% on one training case for the strategy-search primary. No FPGA part selected; no synthesis, timing, resource or power result exists.

**December fresh test versus tuned PID** (four three-day cases): MPC used 40.38% less delta-v (0.68098 to 0.40603 m/s), had 7.63% higher RMS (22.013 to 23.693 m) and 49.27% more host CPU. PID had lower RMS in every case; MPC reversed direction more (70.0 versus 40.25 changes over 90 degrees).

**Strategy search** (15 settings, 116 runs): training chose `sparse_event60`; on eight fresh January cases `sparse_05` did better, with RMS 9.73%, delta-v 18.65% and burns 35.02% below baseline, passing 100 m / 500 m limits in 8 of 8. `sparse_event60` used fewest burns (35.25) but failed 1 of 8 (worst RMS 173.9 m, peak 626.9 m). No policy met 50 m / 300 m in all eight. Smoothing and forced-spacing settings failed at kilometre scale.

**Hardening and endurance** (`docs/mpc-hardening.md`): input, ABI and replay checks, bounded caches, 1,200 native fault/range cases. A fresh seven-day P1 case lost the trajectory (463,647 m RMS, 26.66 m/s demand); its reference passed 37.8 km from the Moon, under the 50 km floor. `RoutineMPC` then added a 5 km / 0.5 m/s envelope that latches `recovery_required` and a 1 m/s per 24 h budget; the replay cut demand to 0.215 m/s but did not recover. Thirty-day runs: P1 42.4 m RMS, 2.186 m/s, 866 burns, two clearance rejections and a nominal path reaching 45.9 km (inadmissible); P2 36.2 m, 2.270 m/s, 905 burns, clean.

**Blind anomalies** (58 runs): 14 of 18 anomaly instances recovered or contained; matched coasting settled in 0 of 18. Failures: the 0.5 m/s kick in both geometries (P2 stopped on a negative-variance exception at 154 h) and permanent thrust failure in both. Recovered cases still peaked at up to 9,723 m.

**Compound faults** (124 runs, 0 exceptions, 0 modeled collisions): navigation/trajectory restored in 20/20 single, 10/8 of 10 concurrent and 9/8 of 10 consecutive cases. MPC beat coasting on post-event RMS in 36 of 40 comparisons (median 96.0% lower). Failures: stuck thruster with blackout (819.4 and 316.3 km off, about 2.1 kg actual propellant, since no valve shutoff exists); a P1 sequence where MPC was worse than coasting (3.261 versus 1.162 km RMS); a P1 navigation lockout ending 3,756 m wrong.

Local only: a 118-run layered-autonomy campaign adds isolation hardware assumptions. With working isolation the stuck-thruster error falls from 819.360 to 0.023 km; with failed isolation it is unchanged.

## 3. Navigation recovery

`docs/navigation-recovery.md`: in the P2 0.5 m/s replay, prolonged rejection left the covariance nearly rank one (position variance 6.88105e19 m^2, condition number 2.39212e24). The solve returned NIS = -503.186075, which passed the old `NIS <= 35` gate, and the Joseph update produced a velocity variance of -1.72950e-5. The fix is a square-root filter: P = L L^T, QR propagation, joint measurement factorization, NIS as a whitened squared norm, no commit before validation.

Causal reacquisition (`navigation_recovery.py`): a rejected fix showing a 0.03 to 2 m/s velocity jump with velocity NIS of at least 25 seeds one provisional track; promotion needs three fixes over an hour at NIS 16.8 or less, with 3-sigma under 200 m and 0.02 m/s. A cold path handles real gaps over three hours (added after a miss that took 100.5 h). 47 of 61 cases ran (14 references failed preflight); all 12,683 NIS values were nonnegative. On the P2 0.5 m/s case, square-root alone ended 60,420 m wrong; with reacquisition, 19.8 m. Navigation recovery is not trajectory recovery: 0.75 and 1.25 m/s kicks ended 121 and 203 km off. 3-sigma coverage was 89.4% to 100%. A coherent sensor fault is indistinguishable from real motion in this single stream.

## 4. Archive replays and force repairs

- Future-data injection (`docs/cislunar-force-validation.md`): the earlier replay differentiated archived velocities and added the residual to every forward force evaluation. Changing one future CAPSTONE velocity sample by +1 m/s moved the first-hour forecast 1,500.29 m. That path was removed; forecasts now pass future-value-invariance tests. Lunar GM and the J2 formula (wrong radial power and polar sign) were also corrected.
- LRO, January 2023, three days: 240.758 km with old constants, 22.749 km with DE440 GMs, Sun and J2, about 0.460 km with GRGM900C degree 120, 427.045 m with Earth J2, planets and 1PN. Tide variants give 367.702 or 430.534 m; the convention is unresolved. A 0.05016 m/s^2 feature in the NASA reference near 01:10 TDB is unexplained.
- CAPSTONE February 2023: 35.6 to 1.91 km. CAPSTONE November 2022 (about 342 km) and Orion (about 9,734 km) fail because documented maneuvers are unmodeled; the failures stay in the scores.
- ARTEMIS P1/P2 (2011): best arc 75 m at one day; arcs crossing maneuver flags reach 7,838 and 9,164 km. Two unflagged arcs contain 428 and 618 m position jumps within 15.26 microseconds, a reference-product discontinuity.
- Starting states are reconstructed and may use later tracking, so these are retrospective replays. Control experiments use only the first archived state; everything after is synthetic.

## 5. J0337+1715

- The default trajectory is illustrative, not a reconstruction of the observed orbit (README).
- Archibald post-fit residuals: 27,110 rows, RMS 1.542602 us. The SEP diagnostic gives conditional sigma about 7.30e-13 and marginal 1.91e-7; the README says neither is a new SEP measurement and post-fit scatter does not validate the package.
- An observed-arrival fitter (`timing_fit.py`, PINT preparation) exists with early-only calibration; no fit results are published.
- Shape evolution (`shape_dynamics.py`) integrates shape, scale and orientation directly. It is 8.78x to 9.67x slower than Jacobi, has no PN forces, and Jacobi remains the default.
- `qrc_engine.py`, the "Quantum / Dynamical Relational Reservoir Computing" module, feeds a synthetic sinusoid that never drives the dynamics, so it is not a reservoir test. Nothing quantum is computed.

## 6. Relationship to CislunarOS

`artemis_live/mission_os` is separate but depends on this repo: it imports `JacobiFlightModel`, `FiniteBurn`, `RoutineMPC`, `FixedQP`, lunar gravity, perturbations and thruster allocation, and its cFS build (`cfs_cislunar_gnc/CMakeLists.txt`) compiles `qrc-pulsar-benchmark/hardware/flight_avionics_core.cpp`, which exists only locally, not on main.

Pulsars in the control path:

- This repo: no. Control campaigns use synthetic direct-state fixes, and no control module imports timing code. `OrbitClockEKF` uses XNAV-shaped plane-wave pseudoranges but is labeled not a pulsar-TOA model and sits outside the control campaigns.
- mission_os: a simulated `XnavSensor` (2,000 m noise, one fixed pulsar direction, injected 25 km phase jumps) feeds fusion gates in Python simulation scripts. In the native flight sources `xnav_range_m` is parsed but I found no consumer, and `node3_flight_executive.py` treats XNAV status as diagnostic. This is a grep-level trace, not an executed one.

## 7. Novel guidance

Truthful to depict:

- Frozen protocols: holdout splits, hashed sources, failures kept on record.
- A matched coordinate test that came back null, published anyway.
- A covariance going negative under long rejection, caught and repaired with square-root filtering.
- The gap between "we know where we are" and "we are back on course".
- A latch only a human can rearm, a 1 m/s daily budget, and a stuck thruster software cannot stop.
- A 256-iteration integer optimizer that returns zeros rather than an unverified answer.
- A sensor stream that lies coherently; only an independent observable exposes it.

Overclaiming:

- Jacobi or shape coordinates giving better accuracy, fuel, speed or memory.
- Pulsar navigation steering a cislunar craft in this work.
- Validation against real flights; only initial states are real.
- FPGA or flight-qualified hardware; collision probabilities or survival guarantees.
- A new SEP or gravity result, quantum computation, or working reservoir computing.
- Treating the speculative modules (ARGONAUT, Jovian tour, valuation engines, `catastrophe_avoidance.py`) as results; the repo's own CR3BP counterexample impacts despite passing the Jacobi-integral test.
