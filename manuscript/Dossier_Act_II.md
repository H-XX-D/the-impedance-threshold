# INTER-ACT DOSSIER II
## The Artemis-7 Cislunar Anomaly & Autonomous Recovery
### Document Classification: NASA-JSC / Flight Operations Directorate Tiger Team Report
#### Date of Archival: November 12, 2026 | Mission Phase: Cislunar Free-Return Trajectory

![Cislunar Trajectory Recovery & Gateway Optical Lock](assets/plate_03_dossier_2_cislunar_recovery.png)

### 1.0 MISSION TELEMETRY TIMELINE: THE X8.4 SOLAR FLARE

* **MET 48:12:00 (14:22 UTC):** Solar active region AR3842 produces an X8.4 soft X-ray flare. Proton flux at GOES-19 exceeds $10^4\text{ pfu}$ ($E > 10\text{ MeV}$).
* **MET 48:16:30 (14:26 UTC):** DSN Canberra 70m DSS-43 loses RF carrier lock. Solar radio burst index spikes to $5,400\text{ SFU}$.
* **MET 48:18:00 (14:28 UTC):** Star Trackers STR-A and STR-B saturate under Cherenkov proton transient noise. False centroid count exceeds 1,800/frame.
* **MET 50:36:12 (16:48 UTC):** OpNav camera accepts crater Copernicus horizon fix. Flight computer executes Joseph-form update.
* **MET 50:36:14 (16:48 UTC):** Register `r14` of RAD750 Computer A underflows. Radial velocity variance evaluates to $-0.000412\text{ m}^2/\text{s}^2$. Normalized Innovation Squared evaluates to $-287.412$.
* **MET 50:36:15 (16:48 UTC):** Computer A disqualifies itself. Computer B fails identically in 40 ms. Computer C enters infinite divide loop. Primary guidance locked in `PROTECTIVE_SCREENED_COAST`.
* **MET 52:00:00 (18:12 UTC):** Ballistic trajectory propagation indicates perilune altitude $-38.42\text{ km}$ (farside impact at crater Daedalus).
* **MET 54:06:00 (20:18 UTC):** Mount Stromlo fires 1550 nm laser uplink. 482 KB `cislunar_os_core.elf` loaded into Auxiliary Transceiver.
* **MET 54:06:02 (20:18 UTC):** CislunarOS boots in 5.12W partition. Householder SRIF reacquires attitude. FixedQP computes TCM-3.
* **MET 54:06:20 (20:18 UTC):** TCM-3 executed: $\Delta V = 49.524\text{ m/s}$. Perilune altitude raised to $+112.44\text{ km}$. Mission saved.

---

### 2.0 HARDWARE COMPARISON MATRIX: TRIPLE-REDUNDANT MAINFRAME VS. EDGE CORE

| Avionics Parameter | BAE RAD750 Flight Mainframe (Primary) | NVIDIA Jetson Orin Nano / CislunarOS (Auxiliary) |
| :--- | :--- | :--- |
| **Processor Architecture** | 133 MHz PowerPC 750GL (32-bit SOI) | 6-Core ARM Cortex-A78AE + Ampere Tensor Core |
| **Operating Power Draw** | $28.5 \text{ Watts}$ per channel ($85.5 \text{ W}$ total) | **$5.12 \text{ Watts}$** (5W Low-Power Mode) |
| **Numerical Format** | IEEE 754 32-bit Floating Point | **Q16.16 Fixed-Point 32-bit Integer** |
| **State Filter Algorithm** | Classical Extended Kalman Filter (Joseph Form) | **Square Root Information Filter (Householder QR)** |
| **Numerical Failure Mode** | Negative NIS ($\chi^2 = -287.4$) via mantissa roundoff | **Mathematically Immune to Negative NIS** |
| **Radiation Tolerance** | $100 \text{ krad}$ (Total Ionizing Dose) | $10 \text{ krad}$ (Mitigated via Causal Reacquisition) |
| **Procurement Unit Cost** | $\$20,000,000$ (Triple-channel certified stack) | **$\$399.00$** (Off-the-shelf commercial development kit) |

---

### 3.0 FLIGHT OPERATIONS SIGN-OFF

* **Flight Director:** Michael Hayes, NASA Flight Operations Directorate, Houston.
* **Mission Director:** Dr. Elena Rostova, Artemis Program Office.
* **GNC Lead:** Greg Vance, Prime Avionics Contractor.
* **Investigator of Record:** Todd Hendrixx, Aerodynamics & Spaceflight Systems Archive.
