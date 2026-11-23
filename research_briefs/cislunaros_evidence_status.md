# CislunarOS: what has been demonstrated, and where it stands

Status as of 22 November 2026. Read-only review of project files and the Recall graph `cislunaros`. Nothing was rerun and the Nano (pageqa) was not contacted.

Path prefixes: `PR/` = `/Volumes/Thunderbolt SSD/UserData/Relocated-20261102/artemis_live/mission_os/`, `VAL/` = `PR/baseline_rebuild/validation/`, `RS/` = `/Users/hendrixx./Documents/CislunarOS_Review_20261112/`. Recall IDs are cell key prefixes.

## Bottom line

CislunarOS is bench software. Native C++14 autonomy (Jacobi relational navigation, a sparse receding-horizon QP controller, an independent burn verifier, authenticated ground goals) runs as cFE applications on one Jetson Orin Nano held to 7 W and a 960 MHz CPU cap. Every mission result below uses a simulated spacecraft, synthetic sensor measurements and modeled valves, mostly in accelerated time, scored by audit code from the same author. No physical sensor, actuator, flight computer, numerical TRL or NASA compliance has been established, and the proposal is held.

## Common test conditions

- Host: pageqa, PREEMPT_RT kernel 5.15.148-rt-tegra (NVIDIA developer-preview quality), 7 W profile, 960 MHz cap (`PR/BENCH_DEPLOYMENT_BASELINE.md`).
- Plant: simulated. The force model differs by test and is given with each result.
- Sensors: rendered camera and star images, modeled IMU and valve feedback.
- Audits: separate code paths, same authorship; independence is of implementation, not of party (Recall f54accae).

## Demonstrated results

**Six-hour lunar tracking (the Phase I gate).**
- MC01, 16 November: base profile flew 12 cycles from one ground RESUME. Terminal error 0.435 m, navigation error max 6.47 m, fuel 0.03477 kg. Truth: independent Cartesian RK4 with point-mass DE440 GM values, no ephemeris. The sparse profile missed the frozen 500 m terminal limit at 768.695 m, so the campaign is recorded as FAIL (`VAL/mission_campaign/v1/REPORT.md`; Recall 339a0f84).
- After the fix, three six-hour variations ended at 0.393, 0.309 and 0.353 m using 0.029 to 0.033 kg, also under sanitizers, same point-mass truth (`VAL/sparse_feasibility/v1/REPORT.md`).
- Dated higher-fidelity plants (DE440s, lunar J2, solar pressure, finite burns): five dates each completed 12 maneuvers with matched receipts. Terminal errors 12.52 to 16.62 m against the 500 m limit; largest path error 391.5 m (`VAL/dated_v7_host/REPORT.md`; Recall 07f25a39).
- Timing: slowest protected call 6.926 s against a 10 s single-core allocation; peak memory 21,308 KiB; board power 5.63 W mean, 6.38 W peak. An authenticated STOP inhibited a live plan within 1.110 ms (`VAL/phase_i_software_gate/REPORT.md`).

**Low lunar orbit residence** (100 to 200 km corridor, 215 kg vehicle, +6 m/s insertion error).
- Hazard campaign, ideal spherical camera, degree-16 gravity truth: the 6-hour, 30-day and 120-day lanes completed 12, 1,440 and 5,760 half-hour windows, each ending in a cFE FINISH and an `authority_complete` audit. The 120-day lane took about 9.4 wall hours, made 2,974 burns totaling 166.93 m/s, held 146.57 to 177.67 km, and had a worst optical position error of 0.239 km. Ground contact was the signed upload plus one cap change (0.10 to 0.09 m/s per decision). Injected faults: two optical faults, clock loss and reacquisition, a mount slip (`VAL/llo_hazard_mission_campaign/STATUS.md`; Recall 1fa6c100, fe709d17).
- With a realistic terrain camera and a navigation filter: 30 days passed full audit against both degree-16 and degree-32 gravity truth with zero bound misses (Recall 816d6a3b). The 120-day degree-16 run completed (166.85 m/s, 333,513 of 351,360 images accepted). The degree-32 run stopped at day 104.1 (`VAL/llo_nav_filter/mission/RESULTS_120D.md`; Recall 028df9b6).

**Fault recovery.**
- cFE killed and restarted mid-outage after receipt 720; all 1,440 windows completed (`VAL/llo_v2_outage_faults/REPORT.md`).
- Physical warm reboot of the primary Nano: a second, separately powered Nano kept the maneuver record and elapsed time, and the new executive resumed windows 4 and 5 with no ground command. A stale checkpoint or an unreachable companion left it inhibited, as designed (`VAL/llo_v2_board_reset/REPORT.md`).
- 31 directed cFE valve-fault scenarios, signed retask, and ground re-keying after restart (Recall 82a3a71e, a5a97710).
- Safe-haven study: unthrusted coast from filter estimates stayed above 121 km for 60 days in degree-32 gravity; retrograde burns are the hazard (`VAL/llo_safe_haven/REPORT.md`).

## Failures kept on record, and the fixes

- The original November 12 to 13 audit found 36 problems with earlier claims (`RS/CislunarOS_latest_check.html`). The three "independent" guidance channels copied one another. The under-250 µs latency claim failed (263 to 327.5 µs measured). Published LRO and GRAIL tracking figures (7.34 m, 18.2 m) came from an offline Python controller, not the C++ executive. The built-in lunar-insertion target was mathematically impossible. These claims were withdrawn, the code was repaired in stages, and the author chose a cleanroom rewrite.
- MC01 sparse failure: fixed by a full-schedule feasibility check before admission.
- Dated V5 failed all three dates after 1, 2 and 2 maneuvers: fixed with a lunar J2 navigator and a QP cost on the final coast.
- At the 960 MHz cap, an earlier build exceeded the 10 s step budget (10.565 s): fixed by a revised propagator (Recall bdf8ba89).
- The V1 host refused a 30-day mission (six-hour cap) and a 600-day test: fixed for 30 days by the V2 host (`VAL/mission_30d_20261118/REPORT.md`).
- In 120-day runs, the budget was refused on day 32.21, and native inhibits occurred on days 69.35 and 88.27: answered with a reserve profile and autonomous wheel unloading.
- Realistic camera: the original estimator got 0 of 1,440 fixes (Recall 7421b62c). The terrain-aware estimator reached 94% fixes, but the verifier then refused thrust (Recall b18c288e). Adding the filter closed that gap.
- Day-104 stop: the software correctly refused one burn for lack of an independent attitude reference, but the harness treated any refusal as fatal. The run was not restarted.
- Draco app review: a corrupted table file blocked resume, and out-of-order timestamps caused a critical fault to be refused. Both were fixed by amendment A1 (Recall 657f7f3e).
- Still open: a deadline overrun (13.742 s) when an equal-priority process competes for the CPU, a cold restart that loses the record of unresolved effects (`VAL/physical_verification_entry/REPORT.md`), a shared 0.2° camera-mount bias that defeats the pointing check, and the legacy planner's continuous-clearance defect.

## cFS Draco and the networked test

cFS Draco v7.0.1 was cloned, built and booted on pageqa on 20 November (`PR/baseline_rebuild/bench/cfs_draco_v7_0_1/README.md`). The first Draco app is MPS, the mission phase sequencer. It passed 1,349 of 1,349 unit assertions with 100% line and branch coverage, ran clean under sanitizers, and killed 50 of 50 mutants; after a processor reset it resumes from its Critical Data Store. It is accepted as a bench candidate only (`PR/cleanroom_rewrite/increments/phase_app_v2/REVIEW.md`; Recall b14002c6). The navigation and control apps still run on the older Aquila cFE 6.7.0 bench host. Interfaces changed between 6.7 and 7.0, so those apps are not yet ported.

The files I read never name the networked Jetson feasibility test. The nearest recorded work is the two-Nano reboot test and roadmap item 6, a backup computer that "needs a second board" (`PR/baseline_rebuild/planning/SCAFFOLD_ROADMAP.md`). A test of that kind can show cross-board authority and recovery behavior on a LAN. It cannot show flight-link behavior; the measured lunar round trip from NASA LRO data is 2.444 to 2.481 s.

## Explicitly open

- **Flight target:** none. The Jetsons are bench hardware.
- **Physical sensors:** none. Every camera, star, IMU and valve signal is synthetic.
- **Actuator calibration:** none. When thrust physically stops after a STOP is unknown.
- **Assurance:** 130 NPR 7150.2D requirement IDs inventoried, all unassessed. Agent review is not independent V&V. Export control is unassessed.
- **TRL:** TRL 4 is the Phase I target; the numerical TRL is null; TRL 6 is explicitly not established (Recall efc408b1).
- **Missing capabilities:** native transfer and insertion, DRO safe haven, thruster reconfiguration, backup computer, commissioning, disposal.

## SBIR and NASA positioning

Submission is held, registration deferred, PI undesignated and the applicant firm undecided (`PR/baseline_rebuild/PHASE_I_SUBMISSION_GATE.json`). The project is waiting for a NASA Phase I appendix with a navigation fit. The historical match is COMNAV.1.S26B, Flight Dynamics and Navigation Technologies, which closed 21 May 2026. NASA targets program-year 2027 Appendix A for winter 2026 to 2027; no matching topic was confirmed as of 18 November (Recall a1ab2148; `VAL/opportunity_review_20261117/REPORT.md`). Phase II pays up to $1,275,000 over 24 months and requires a Phase I award.

The product is "hosted autonomous avionics": an autonomy core evaluated as a hosted application on someone else's flight computer. Ground observes and directs through authenticated goals, the vehicle plans and acts within an authorized envelope, and the host can revoke its authority. The goal is to remove routine DSN navigation and commanding with a lightweight link (`PR/baseline_rebuild/HOSTED_AUTONOMY_CONOPS.md`). Novelty is narrowed on purpose. autoNGC on CAPSTONE computed maneuvers onboard in 2026. The defensible claim is that no flown example was found of ground-free, multi-month low-lunar-orbit stationkeeping driven by onboard optical navigation under a signed, retaskable profile with an independent thrust verifier, and CislunarOS shows that only in simulation (Recall 2ee4b795).

## For the novel

**True early history (2026):** one engineer and a palm-sized 7 W board. Simulated 120-day missions run in about nine hours. One board was rebooted on purpose while a second board held the burn ledger. A realistic camera broke navigation (0 of 1,440 fixes) and the estimator was rebuilt. A day-104 run was lost because the test harness could not count a correct refusal. Failures stay on the record, and the proposal waits on a NASA topic.

**Realistic next milestones, in recorded dependency order (plans, not evidence):**
1. Finish the realistic-sensor evidence (rerun 120 days in degree-32 gravity with the harness fix).
2. Port GNC to Draco under the phase sequencer.
3. Add a low-lunar-orbit safe haven, sensor fault detection, thruster reconfiguration and a backup board.
4. Submit Phase I if a 2027 appendix fits: feasibility, preliminary software, integration plan, TRL 4.
5. With a Phase II award: host adapter, real camera and valves on a FlatSat.
6. On a host mission: shadow mode with advisory output, then bounded actuation if the host allows it (the ConOps progression).
7. Transfer, insertion, then halo and DRO profiles (the ARGONAUT case).

The ARGONAUT timeline in the files, anchored on July 2027 funding, is aspirational (Recall d0228da0). Any history after November 2026 is invention; no host, award or partner exists in the records.

**Overclaiming, even in backstory:**
- "First autonomous cislunar navigation" (CAPSTONE came first).
- "Flight-proven," "TRL 6," "NASA-certified," "NPR 7150.2 compliant."
- The 0.24 km or centimeter-level figures presented as real-world accuracy.
- Demonstrated DSN independence, triple-redundant voting, or guaranteed real-time behavior.
- The Jetson as a flight computer, DRO refuge performance, or "any mission" (today it flies one regime and one phase).
