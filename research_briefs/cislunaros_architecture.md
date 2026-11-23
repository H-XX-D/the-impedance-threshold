# CislunarOS architecture as built

Research brief for the novel, 22 November 2026. Read-only review of source, specifications and evidence; nothing was built, run, committed or written to Recall.

Path abbreviations: `MOS` = `/Volumes/Thunderbolt SSD/UserData/Relocated-20261102/artemis_live/mission_os`; `MATH` = `MOS/baseline_rebuild/design/math`; `VAL` = `MOS/baseline_rebuild/validation`; `CR` = `MOS/cleanroom_rewrite`; `REV` = `/Users/hendrixx./Documents/CislunarOS_Review_20261112`.

**Summary.** CislunarOS is a C++14 hosted-autonomy research suite: an 18-state Earth/Moon/spacecraft/Sun Jacobi navigator (an extended Kalman filter), a box-constrained QP receding-horizon controller run as three voting software channels, a separate interval-arithmetic Cartesian verifier, and a protected host owner that alone can issue a burn and that ground can stop. It runs on a Jetson Orin Nano bench inside NASA cFE with simulated sensors, thrusters and clocks. It has no flight host, no assigned TRL and no flight acceptance (`MOS/baseline_rebuild/definition.json`: `flight_acceptance: false`, `numerical_trl: null`, `flight_target: null`).

Three code lines share the project. The frozen prototype (`MOS/flight_executive_cpp`, `MOS/cfs_cislunar_gnc`, "prototype 3.x", reviewed in `REV`) is history. The current Phase I core is the cleanroom rewrite in `CR`, authored fresh from reviewed specifications (`MOS/baseline_rebuild/CLEANROOM_REWRITE_POLICY.md`). A newer low lunar orbit (LLO) line mostly uses a different navigator and controller (section 6). The Jacobi and QP description fits the cleanroom core.

## 1. Jacobi relational coordinates

**State.** Four bodies, three 6-vectors (position then velocity, SI, one nonrotating frame) (`MATH/jacobi_core_entry/v1/packet/UNIT_CONTRACT.md`):
- q1 = Moon minus Earth (states 1 to 6)
- q2 = spacecraft minus the Earth-Moon barycenter (states 7 to 12)
- q3 = Sun minus that barycenter (states 13 to 18)

With fE = muE/(muE+muM), the Moon-relative spacecraft state is q2 minus fE times q1. The spacecraft and Sun both reference the Earth-Moon barycenter, so this is a two-level relational chain, not a fully nested textbook Jacobi tree; for a massless spacecraft the difference vanishes. The author's documents call it "relational/Jacobi" mathematics (`MOS/baseline_rebuild/planning/ORIGINAL_CPP_AUTONOMY_CARRY_FORWARD.md`).

**Force model.** J4-CORE-01 is point-mass mutual gravity among all four bodies, including the Sun's response and optional spacecraft back-reaction, plus one constant non-gravitational spacecraft acceleration input, with an analytic 18 by 18 Jacobian (`CR/src/jacobi_four_body_v1.cpp`). J4-PROP-01 integrates the state and all 324 transition-matrix entries together with eighth-order DOP853 (`MATH/jacobi_propagator_entry/v1/packet/UNIT_CONTRACT.md`). Additions sit outside the core:
- Lunar J2 with a pole fixed at mission start, in an experimental navigator (`CR/increments/lunar_quadrupole_v1/ASSIGNMENT.md`; `VAL/dated_navigation_and_planning/REPORT.md`).
- Two constant acceleration corrections on q1 and q3, precomputed from ephemeris at each mission start (`VAL/dated_v7_host/REPORT.md`).
- No onboard solar radiation pressure term. SRP exists in the test truth and reaches the navigator only through measured IMU acceleration (same report).
- Degree-16 GRGM1200A lunar gravity lives in the frozen prototype and the LLO line, not in the Jacobi core (`MOS/GRAVITY_MODEL_REVIEW.md`).

The planner's forecast stays point-mass even when the navigator carries J2.

**Why Jacobi.** Because Sun and Moon are integrated inside the state, "no future Sun-position provider is required by these equations after initialization" (`MOS/baseline_rebuild/planning/INTEGRATED_FOUR_BODY_JACOBI_DRAFT.md`). That serves the goal of cutting routine DSN and ephemeris dependence. The author treats any coordinate advantage as a hypothesis: adding solar gravity helped research runs, while "matched coordinate variants agreed" (`MOS/baseline_rebuild/research/initial_system_v1/INITIAL_SYSTEM_LINEAGE.md`). Phase I proposes a representation-only comparison against a Cartesian controller (`MOS/baseline_rebuild/PHASE_I_TECHNICAL_VOLUME_DRAFT.md`).

**Preservation.** Each unit starts as a code-independent packet: equations, C header, frozen vectors, tolerances. A fresh author with no legacy exposure writes source on the Nano; a separate reviewer owns the oracles. The J4 core passed 88 high-precision fixtures, 216 complex-step Jacobian columns, 146 negative cases and 8 exact-rational controls, 43,639 assertions in independent builds (`MATH/jacobi_core_entry/v1/README.md`). The propagator oracle is independent Radau5 collocation (`MATH/jacobi_propagator_entry/v1/packet/ORACLE_PROVENANCE.json`). This proves agreement with the declared model, not with the real sky.

## 2. Navigation inputs and filter

NAV-J4-01 is an extended Kalman filter over all 18 states with a full 18 by 18 covariance; it is neither square-root nor unscented (`MATH/avionics_integration_entry/v1/math_packet/NAV_CONTRACT.md`; `CR/src/nav_j4_v1.cpp`). Prediction carries mean and covariance through the DOP853 transition matrix plus diagonal process noise. Updates use Cholesky factorization with no repair, a normalized-innovation-squared gate and a Joseph-form covariance update. Each sample can be consumed once, even when rejected.

Inputs (`CR/include/cislunar/nav_j4_v1.h`):
1. Moon-relative position fix (3D). In bench runs this is a simulated "position provider".
2. Moon-center direction, a unit vector with a 2D tangent-plane residual: an optical bearing. The spec warns that bearing-only range ambiguity remains.
3. IMU interval mean non-gravitational acceleration, which drives prediction rather than updating (`CR/include/cislunar/avionics_host_v1.h`).

Ground does not feed the filter; it uploads the reference seed and mission. No pulsar or X-ray timing measurement exists in the native source, headers or math packets.

## 3. QP receding-horizon controller

RHC-PLAN-01 (`MATH/receding_horizon_entry/v1/rhc_packet/CONTRACT.md`; `CR/src/receding_horizon_v1.cpp`):
- **Horizon and cadence.** Intervals of exactly 1,800 s. Profile base12: up to 12 intervals (6 hours), 2 solves. Profile sparse4: up to 4 intervals (2 hours), 6 solves. One decision per 30 minutes; a six-hour mission is 12 decisions.
- **Variables.** One 3-axis delta-v per interval, normalized into [-1, 1] by a capacity c: 36 variables (base) or 12 (sparse).
- **Model.** Tracking-error dynamics frozen at each interval midpoint from the J4 Jacobian (`MATH/avionics_integration_entry/v1/math_packet/TRACK_CONTRACT.md`), discretized by a bounded Taylor matrix exponential with a finite-burn term.
- **Cost.** Least squares: weighted predicted tracking error, effort, and for sparse4 a reweighted group penalty favoring few burns. The dated experiment added terminal-coast residuals.
- **Constraints.** The box; capacity from the rocket equation using thrust, exhaust velocity, mass and protected reserve; burn no longer than its interval; a minimum command, below which the outcome is COAST.
- **Solver.** A bounded active-set generator (`QP-ROBUST-01`) proposes; success requires a CQPv2 certificate that proves positive definiteness by interval LDL factorization and bounds suboptimality under a gap tolerance in outward-rounded interval arithmetic (`MATH/qp_core_entry/v2/packet/CONTRACT.md`). Uncertified answers are discarded.
- **Number format.** IEEE binary64, no fast-math or fused contraction, integer-nanosecond time with checked subtraction, fixed work caps (at most 44 matrix exponentials per plan). The research ancestor was a 24/16 or 32/24 fixed-point integer QP aimed at an FPGA; it was not carried forward (`INITIAL_SYSTEM_LINEAGE.md`).
- **Supported tuning.** [1000, 1, 1, 0.1, 0.0005, 0.01, 1e-8, 1e-6]: position scale, velocity scale, delta-v scale, 0.1 m/s maximum per command, sparse weight, epsilon, minimum command, gap tolerance (`CR/README.md`; field order in `MATH/avionics_integration_entry/v1/host_packet/GROUND_PAYLOAD.md`).

Only the first burn executes, as constant thrust for a rocket-equation duration. The shifted warm start survives only after the host reconciles the effect receipt. Before issue, TFR-01 forecasts the whole schedule to mission end, then the verifier runs, then the host gate.

## 4. Safety and authority

- **Triplex.** Three RHC calls on one snapshot with three separate workspaces, run in sequence in one process (`CR/src/avionics_owner_v1.cpp`). Pairs (0,1), (0,2), (1,2) are tested for delta-v, direction, duration and force agreement; the first compatible pair wins; no averaging; one channel alone cannot issue. The contract calls this "software disagreement testing, not independent physical fault isolation" (`MATH/avionics_integration_entry/v1/math_packet/TRIPLEX_CONTRACT.md`).
- **DVC.** `Dvc` is the code prefix of DIVERSE-CHECK-01, the "diverse first-command verifier"; the documents never expand it as "delta-v checker" (`CR/include/cislunar/diverse_first_command_v1.h`). It recomputes in Cartesian coordinates with interval arithmetic, proves no body leaves a travel radius, bounds fuel against reserve and proves continuous clearance from Earth, Moon and Sun for one command and its follow-up (`MATH/diverse_verifier_entry/v1/packet/MATHEMATICAL_CONTRACT.md`). Outcomes: PASS_CONDITIONAL, REJECT, INCONCLUSIVE. It shares point-mass physics and the CPU with the planner.
- **Protective planner and coast-lock: not in CislunarOS.** `protective_planner.py` exists only in the older Python research package `qrc_pulsar_bench`, listed as lineage (`INITIAL_SYSTEM_LINEAGE.md`). "Coast-lock" has zero matches in the project. Actual equivalents: the planner's COAST outcome; host modes INHIBITED, AUTO, MANUAL_HOLD, MISSION_HOLD; the sequencer's "refuge COAST"; the LLO host's 60 s contingency coast.
- **PREPARE before ISSUE.** The host durably writes a complete PREPARED/ISSUING record, releases its lock during disk I/O, then rechecks fence, mode, time and reservation before calling issue exactly once. A STOP during the write wins (`MATH/avionics_integration_entry/v1/host_packet/JOURNAL_CONTRACT.md`).
- **Ground authority.** Fixed 512-byte packets with HMAC-SHA256: STOP, TAKEOVER, RESUME_AUTO, STAGE_MISSION (400-byte mission), COMMIT_MISSION, MANUAL; plus local `av_host_revoke_v1`. Sequence counters, a 32-entry retry cache and expiry windows apply. STOP needs a valid MAC and session but no matching revision. Reboot starts inhibited; contact return never rearms (`MATH/avionics_integration_entry/v1/host_packet/GROUND_CONTRACT.md`). Measured: STOP inhibited a live plan within 1.110 ms of local publication (`VAL/phase_i_software_gate/REPORT.md`).
- **Journal.** Two file slots, fsync, atomic rename, SHA-256. A recovered in-flight record becomes UNKNOWN (possibly issued) and is never repeated. Open gap: loss of all newer records is undetectable without an external generation reference (`CR/integration/CONTRACT.md`).

## 5. cFS and hardware

The Phase I workload runs as a cFE application under the Aquila bundle, cFE 6.7.0 with OSAL 5.0 (`MOS/baseline_rebuild/planning/CFS_AND_COMPLIANCE_FRAMEWORK.md`). cFS Draco v7.0.1 was built on the Nano on 20 November 2026 as the reference for new apps (`MOS/baseline_rebuild/bench/cfs_draco_v7_0_1/README.md`). The first Draco app is MPS, the Mission Phase Sequencer, hosting the `phase_sequencer_v2` mission plan core (up to 16 phase instances, revision, rollback, committed disposal). With amendment A1 it is "accepted as a bench candidate": 1,349 assertions pass, 50 of 50 mutants killed (`CR/increments/phase_app_v2/REVIEW.md`). I found no evidence the navigator or RHC has moved to Draco.

Hardware: Jetson Orin Nano "pageqa", aarch64, PREEMPT_RT kernel 5.15.148, GCC 11.4. The Phase I run used one core capped at 960 MHz in the 7 W mode: longest protected call 6.926 s against a 10 s limit, peak memory 21,308 KiB, board power 5.63 W average (`VAL/phase_i_software_gate/REPORT.md`). The tested path needs no GPU (`VAL/arm_host_budget/HOST.json`). Three Nanos are bench hardware; the flight sizing reference is a radiation-tolerant Cortex-A72 module at 1.2 GHz (same file).

## 6. Mission concept

"Hosted autonomy" means an application on a host spacecraft's computer: ground uploads authenticated goals; the software estimates, plans and executes inside a host-granted envelope; host or ground can inhibit or take over (`MOS/baseline_rebuild/HOSTED_AUTONOMY_CONOPS.md`). Priorities: real requirements, then autonomy, then routine DSN independence.

All results are simulated:
- Six-hour lunar-relative tracking of a point-mass reference: five dated cases completed 12 decisions each, terminal error 12.5 to 16.6 m (`VAL/dated_v7_host/REPORT.md`).
- LLO, 100 to 200 km band: a 30-day cFE run with 1,440 authorized windows after one upload (`VAL/llo_host_windows/REPORT.md`). Over 120 days the original RHC/QP held the band only with 600 m/s of authority (25.6 kg); the selected mode (7.7 kg) is mean-orbital-element feedback (`VAL/llo_120d_stabilization/REPORT.md`). The LLO navigator is a Python EKF on Moon-centred position and velocity with degree-16 gravity and camera fixes (`VAL/llo_nav_filter/sensors/nav_filter.py`). With a realistic camera it completed 5,760 of 5,760 windows on degree-16 truth; the degree-32 run stopped on day 104.1 when the harness treated a correct refusal as fatal (`VAL/llo_nav_filter/mission/RESULTS_120D.md`).
- A 600-day Earth-to-Moon test failed native staging at the six-hour limit (`MOS/CODEX_HANDOFF.md`).

NRHO and DRO appear only in research data, the prototype and a roadmap note. Orbit families remain open; standing goals without end dates are planned, not built (`MOS/baseline_rebuild/planning/OPEN_ENDED_MISSIONS.md`).

## 7. Guidance for the novel

**Truthful to depict.** The ship carries the Sun and Moon inside its own state instead of asking Earth where they are. Every 30 minutes it re-solves a small QP, flies only the first burn and discards the rest. Three planners must agree in pairs; then a deliberately different Cartesian calculation must prove the burn safe, or nothing fires. The host owner, not the planner, issues. STOP outruns any calculation. After a reboot it wakes inhibited and treats an interrupted burn as possibly fired. It refuses rather than guesses, and refusals are frequent.

**Author vocabulary.** Jacobi four-body, q1/q2/q3, relational coordinates, J4, STM, base12/sparse4, certificate, COAST, CANDIDATE, triplex, NO_MAJORITY, DVC, PASS_CONDITIONAL, fence, authority generation, STAGE/COMMIT/RESUME, TAKEOVER, PREPARED/ISSUING/UNKNOWN, receipt, inhibit, hosted autonomy, DSN independence.

**Overclaims to avoid.**
- Flight heritage, flight hardware, a TRL or NASA compliance.
- Triplex as hardware or radiation redundancy.
- Pulsar navigation, or a protective planner or coast-lock inside CislunarOS.
- Navigation from real sensors; every fix so far is simulated.
- Proven fuel savings, or proof that Jacobi coordinates beat Cartesian.
- NRHO operations, transfers, months of Jacobi-QP stationkeeping, or indefinite operation.
- An onboard Jacobi model with full harmonics or SRP.
- STOP as a physical thruster cutoff; only software inhibition was measured.
