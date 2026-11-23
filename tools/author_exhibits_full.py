#!/usr/bin/env python3
"""
Author Exhibits and Appendices Full: Complete from-scratch generation.
Author: Todd Hendrixx
All diegetic exhibits renewed with authentic mathematics, flight code, and data logs.
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"
os.makedirs(MANUSCRIPT_DIR, exist_ok=True)

EXHIBITS = r"""# DIEGETIC EXHIBITS & MATHEMATICAL APPENDICES
## The Relational Spaceflight & Astrobiological Archive
### Curated by Todd Hendrixx

---

## DIEGETIC EXHIBIT A: SQUARE-ROOT INFORMATION FILTERING & INTEGER GUIDANCE CORE
### Edge Autonomy Implementation: `srif_qr_integer_core.cpp` & `fixed_qp_guidance.h`

![QRC Relational State Estimator & Autonomous Control Flow](assets/plate_08_exhibits_navigation_algorithm.png)

### 1.0 THE FAILURE OF JOSEPH-FORM COVARIANCE IN SINGLE PRECISION
When an Extended Kalman Filter (EKF) is implemented in IEEE 754 32-bit single-precision floating-point arithmetic on edge avionics, the conventional Joseph-form covariance update equation exhibits catastrophic numerical vulnerability:
$$\mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k) \mathbf{P}_{k|k-1} (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)^T + \mathbf{K}_k \mathbf{R}_v \mathbf{K}_k^T$$

In theory, this algebraic formulation ensures positive semi-definiteness. In finite-precision hardware, however, when the prior covariance $\mathbf{P}_{k|k-1}$ is starved across multiple rejected observation cycles (such as during the Artemis-7 solar proton storm), the subtraction $(\mathbf{I} - \mathbf{K}\mathbf{H})$ induces roundoff cancellation. Diagonal elements $P_{ii}$ become negative, and the residual covariance matrix $\mathbf{S} = \mathbf{H}\mathbf{P}\mathbf{H}^T + \mathbf{R}_v$ develops negative eigenvalues.

Consequently, the Normalized Innovation Squared (NIS):
$$\chi^2 = \mathbf{y}^T \mathbf{S}^{-1} \mathbf{y}$$
evaluates to negative values ($\chi^2 = -287.412$). In flight software where the measurement gate is implemented as a simple upper-bound inequality (`nis <= GATE_LIMIT`), negative NIS values pass undetected, committing corrupted state vectors to the flight executive.

### 2.0 THE HOUSEHOLDER QR SQUARE-ROOT INFORMATION FILTER (SRIF)
In CislunarOS, developed by Dr. Ryan Vance, covariance matrices are completely discarded. The state uncertainty is parameterized strictly by the upper-triangular **Square-Root Information Matrix** $\mathbf{R}$, where $\mathbf{P}^{-1} = \mathbf{R}^T \mathbf{R}$, and the information vector $\mathbf{z} = \mathbf{R} \hat{\mathbf{x}}$.

```cpp
// =============================================================================
// CISLUNAROS REVISION 6.1: SQUARE-ROOT INFORMATION FILTER (SRIF) CORE
// Implementation: Householder QR Factorization for 0D Relational State Updates
// Hardware Target: 28nm FD-SOI / NVIDIA Jetson Orin Nano (7.2 W Budget)
// Author: Dr. Ryan Vance // Verified by Todd Hendrixx
// =============================================================================

#include <cmath>
#include <cstdint>
#include <cstring>

constexpr int STATE_DIM = 6;      // Relational Jacobi Shape State
constexpr int MEAS_DIM  = 2;      // Optical Horizon / Star Bearing
constexpr int TOTAL_ROW = STATE_DIM + MEAS_DIM;

struct SRIF_State {
    float R[STATE_DIM][STATE_DIM]; // Upper-triangular square-root information matrix
    float z[STATE_DIM];             // Information vector (z = R * x_hat)
};

void householder_qr_update(
    SRIF_State& filter,
    const float H[MEAS_DIM][STATE_DIM],
    const float y[MEAS_DIM],
    const float sqrt_R_inv[MEAS_DIM][MEAS_DIM]
) {
    // Augmented information array: [ R   | z ]
    //                               [ Rv*H| Rv*y]
    float A[TOTAL_ROW][STATE_DIM + 1];
    std::memset(A, 0, sizeof(A));

    // Populate upper block from prior information
    for (int i = 0; i < STATE_DIM; ++i) {
        for (int j = i; j < STATE_DIM; ++j) {
            A[i][j] = filter.R[i][j];
        }
        A[i][STATE_DIM] = filter.z[i];
    }

    // Populate lower block with whitened measurements
    for (int i = 0; i < MEAS_DIM; ++i) {
        for (int j = 0; j < STATE_DIM; ++j) {
            float sum = 0.0f;
            for (int k = 0; k < MEAS_DIM; ++k) {
                sum += sqrt_R_inv[i][k] * H[k][j];
            }
            A[STATE_DIM + i][j] = sum;
        }
        float sum_y = 0.0f;
        for (int k = 0; k < MEAS_DIM; ++k) {
            sum_y += sqrt_R_inv[i][k] * y[k];
        }
        A[STATE_DIM + i][STATE_DIM] = sum_y;
    }

    // Execute Householder orthogonal triangularization
    for (int k = 0; k < STATE_DIM; ++k) {
        float norm_x = 0.0f;
        for (int i = k; i < TOTAL_ROW; ++i) {
            norm_x += A[i][k] * A[i][k];
        }
        norm_x = std::sqrt(norm_x);
        if (norm_x < 1e-12f) continue;

        float alpha = (A[k][k] > 0.0f) ? -norm_x : norm_x;
        float u_k = A[k][k] - alpha;
        A[k][k] = alpha;

        float inv_norm_u = 1.0f / std::sqrt(u_k * u_k + (norm_x * norm_x - A[k][k] * A[k][k]));

        // Apply reflector to remaining columns
        for (int j = k + 1; j <= STATE_DIM; ++j) {
            float tau = (A[k][j] - alpha * 0.0f); // Householder projection
            float dot = (A[k][j] - (A[k][k] - alpha)) * u_k;
            for (int i = k + 1; i < TOTAL_ROW; ++i) {
                dot += A[i][j] * A[i][k];
            }
            float gamma = dot * (2.0f / (u_k * u_k + norm_x * norm_x));
            A[k][j] -= gamma * u_k;
            for (int i = k + 1; i < TOTAL_ROW; ++i) {
                A[i][j] -= gamma * A[i][k];
            }
        }
    }

    // Extract updated upper-triangular R and information vector z
    for (int i = 0; i < STATE_DIM; ++i) {
        for (int j = i; j < STATE_DIM; ++j) {
            filter.R[i][j] = A[i][j];
        }
        filter.z[i] = A[i][STATE_DIM];
    }

    // Guaranteed strictly non-negative Normalized Innovation Squared (NIS):
    // NIS = || e ||^2 = sum_{i=0}^{MEAS_DIM-1} A[STATE_DIM + i][STATE_DIM]^2
    float guaranteed_nis = 0.0f;
    for (int i = 0; i < MEAS_DIM; ++i) {
        float e_i = A[STATE_DIM + i][STATE_DIM];
        guaranteed_nis += e_i * e_i;
    }
    // guaranteed_nis is mathematically >= 0.0f under all floating-point conditions!
}
```

---

## DIEGETIC EXHIBIT B: RELATIONAL SAGNAC PHASE EQUATIONS & PREGEOMETRIC VACUUM REFRACTION
### Ground Interferometry Model: `vacuum_refraction_sagnac.py`

In Quantum Relational Causality (QRC), gravity is not the geometric curvature of an empty container. It is the physical, refractive impedance of the vacuum acting on discrete causal updates.

### 1.0 PREGEOMETRIC CAUSAL IMPEDANCE DERIVATION
Let the universal causal impedance of the undisturbed vacuum be $Z_0 = \sqrt{\mu_0 / \varepsilon_0} \approx 376.73\ \Omega$. In the proximity of localized mass-energy $M$, the state transition rate of discrete events is bounded by the Margolus-Levitin rate limit:
$$\nu_{\text{update}} \le \frac{2 E}{\pi \hbar}$$

The local effective index of refraction for causal signals propagating at distance $r$ from mass $M$ is:
$$n(r) = 1 + \frac{2GM}{c^2 r}$$

### 2.0 GROUND INTERFEROMETRY EQUATIONS (GILES COUNTY 1,200M RING)
In a fiber-optic Sagnac ring interferometer of enclosed area $A$ and perimeter length $L$, operating at optical wavelength $\lambda = 1550\text{ nm}$ in a subterranean vault, the total phase difference between counter-propagating laser modes includes both the Earth rotation rate $\mathbf{\Omega}$ and the lunar tidal causal refraction $\Delta n(t)$:
$$\Delta \Phi(t) = \frac{8 \pi \mathbf{A} \cdot \mathbf{\Omega}}{c \lambda} + \frac{2 \pi L}{\lambda} \left[ \frac{2 G M_{\text{Moon}}}{c^2 r_{\text{Moon}}(t)} \cos(\omega_{O_1} t) \right]$$

```python
# =============================================================================
# GROUND SAGNAC VERIFICATION: LUNAR O1 TIDAL REFRACTION MODEL
# Location: Giles County Vault (800 ft depth) // Perimeter: 1,200 meters
# Author: Todd Hendrixx // Derived from Ryan Vance Research Notes
# =============================================================================

import numpy as np

def calculate_sagnac_causal_phase(time_hours):
    G = 6.67430e-11          # Gravitational constant (m^3 / kg s^2)
    c = 299792458.0          # Speed of light (m/s)
    M_moon = 7.342e22        # Lunar mass (kg)
    r_moon_mean = 3.844e8    # Mean Earth-Moon distance (m)
    wavelength = 1550e-9     # Laser wavelength (m)
    L = 1200.0               # Fiber loop length (m)
    A = 1.146e5              # Enclosed area (m^2)
    omega_earth = 7.292115e-5 # Earth rotation rate (rad/s)
    latitude = np.radians(35.2)

    # Lunar diurnal O1 tidal frequency (radians per second)
    omega_O1 = 2.0 * np.pi / (25.819 * 3600.0)
    t_seconds = time_hours * 3600.0

    # Geometric Earth Sagnac rotation phase (static baseline)
    phi_rot = (8.0 * np.pi * A * omega_earth * np.sin(latitude)) / (c * wavelength)

    # QRC Vacuum Refractive Impedance Shift
    delta_n = (2.0 * G * M_moon) / (c**2 * r_moon_mean) * np.cos(omega_O1 * t_seconds)

    # Dynamic Causal Phase Modulation
    phi_causal = (2.0 * np.pi * L / wavelength) * delta_n

    return phi_rot, phi_causal, delta_n

# Verification at t = 0 (Lunar Meridian Transit):
phi_base, phi_tide, dn = calculate_sagnac_causal_phase(0.0)
print(f"Static Rotation Sagnac Phase: {phi_base:.4f} rad")
print(f"Dynamic Causal Tidal Phase:  {phi_tide * 1e6:.4f} micro-rad")
print(f"Refractive Index Shift Delta n: {dn:.4e}")
# Output confirms 12.4 picosecond phase lead observed at Giles County
```

---

## DIEGETIC EXHIBIT C: HYPERVELOCITY AEROGEL HUGONIOT & LASER SEAL
### Canister 1 Qualification Archive: `aerogel_shock_hugoniot.py`

![Canister 1 Metallurgical Qualification & Laser Seal](assets/plate_09_exhibits_canister_qualification.png)

### 1.0 GRADED SILICA AEROGEL HYDRODYNAMIC DECELERATION
The capture of cryogenic brine ice grains at $2,214.2\text{ m/s}$ without thermal degradation requires a continuous spatial grading of aerogel bulk density $\rho(x)$:
$$\rho(x) = \rho_0 + (\rho_{\text{max}} - \rho_0) \left( \frac{x}{L_{\text{cassette}}} \right)^2$$
Where $\rho_0 = 0.005\text{ g/cm}^3$, $\rho_{\text{max}} = 0.080\text{ g/cm}^3$, and $L_{\text{cassette}} = 30.0\text{ mm}$.

Under the Rankine-Hugoniot hydrodynamic shock relations, the shock pressure $P_s$ and shock temperature $T_s$ experienced by the incoming ice grain of initial temperature $T_0 = 80\text{ K}$ are:
$$P_s = \rho_{\text{aerogel}} u_s u_p = \rho(x) (c_0 + s u_p) u_p$$
$$T_s = T_0 \exp\left[ \frac{\gamma_0}{V_0} (V_0 - V) \right] + \frac{\Delta E_{\text{shock}}}{C_v}$$

Because the entrance density is less than $0.006\text{ g/cm}^3$, initial shock pressures remain strictly below $0.08\text{ GPa}$, keeping peak core temperatures below $120^\circ\text{C}$ and preserving molecular PNA backbones intact.

---

## DIEGETIC EXHIBIT D: PULSAR BENCH LOGS & SHAPE SPHERE REDUCTION
### National Radio Astronomy Observatory // Archibald 2018 Dataset Fit

```
================================================================================
QRC RESEARCH BENCH LOG: PULSAR TIMING ARCHIVAL FIT
Platform: Dual AMD EPYC 9654 (192 Cores, AVX-512) // RAM: 128 GB ECC DDR5
Target: PSR J0337+1715 (Hierarchical Relativistic Triple System)
Data: Archibald et al. (2018) Nature Release (27,110 TOAs across 4.0 Years)
Author: Todd Hendrixx // Computation: Dr. Ryan Vance
================================================================================
INPUT DATA SUMMARY:
  Total Pulses Integrated:        14,640,000 pulses
  Observing Frequencies:          350 MHz (GMRT), 820 MHz (GBT), 1.4 GHz (WSRT)
  Dispersion Measure (DM):        21.3148 pc / cm^3
  Classical TEMPO2 Fit Time:      78.4 Hours (64-Node Xeon Supercomputing Cluster)
  QRC Relational Fit Time:        252.4 Seconds (4.2 Minutes, Single Workstation)

RESIDUAL TIME-OF-ARRIVAL (TOA) PERFORMANCE:
  Post-Fit Weighted RMS:          1.542 microseconds (Receiver White Noise Limit)
  Phase Drift Over 4 Years:       < 0.008 microseconds (Strict Zero Secular Drift)
  Strong Equivalence Violation:   Delta = (1.24 +/- 1.38) x 10^-6 (SEP Verified)
  Shape Sphere Hopf Invariants:   w_x = +0.4128, w_y = -0.1982, w_z = +0.8841
  Regularization Method:          Kustaanheimo-Stiefel (KS) Collision Free
================================================================================
```

---

## DIEGETIC EXHIBIT E: JOVIAN INVARIANT MANIFOLD TRAJECTORY
### 980-Day Autonomous Ghost Run: `three_body_invariant_manifolds.py`

In the planar circular restricted three-body problem (PCR3BP), the Jacobi energy integral $C_J$ is strictly conserved:
$$C_J = 2 \Omega(x, y) - (\dot{x}^2 + \dot{y}^2) = \text{constant}$$

Canister 1 departed Callisto on January 20, 2041, with $C_J = 3.00084$, placing its trajectory on the **Unstable Invariant Manifold Tube** $W^U(L_1)$ of the Sun-Jupiter three-body system. Traveling along this manifold tube, the spacecraft required zero active propulsion burns during its 980-day transit, riding natural gravitational streamlines back to the Earth-Moon $L_2$ gateway portal.

---

## DIEGETIC EXHIBIT F: EUROPAN BIOCHEMISTRY & THE ENTROPY LADDER
### Lunar Receiving Laboratory // Final Analytical Report

```
================================================================================
EXOBIOLOGICAL AUDIT: EXO-ARCHAEON EUROPAE (TRACK 4812)
Instruments: 80 kV Cryo-TEM, Orbitrap MS/MS, Polarized Circular Dichroism
Classification: COSPAR Category V Pristine Alien Genesis
================================================================================
BIOCHEMICAL ARCHITECTURE:
  Cellular Envelope:        Single-layer tetraether caldarchaeol monolayer (5.2 nm)
  Core Hydrocarbon:         C40 bis-biphytanyl isoprenoid with 4 cyclopentane rings
  Membrane Permeability:    Impermeable to Na+ / Cl- under 1,700 bar hydrostatic
  Genetic Information:      Peptide Nucleic Acid (PNA) Double Helix
  Backbone Polyamide:       Poly-N-(2-aminoethyl)glycine (Uncharged, Achiral)
  Base Pair Alphabet:       2,6-Diaminopurine (D) === Uracil (U) (3 H-bonds)
                            Isoguanine (iG) === Isocytosine (iC) (3 H-bonds)
  Thermal Denaturation:     Melting Temperature T_m = 94.2 deg C
  Metabolic Mechanism:      Chemiosmotic sulfate reduction coupled to H2 oxidation
  Intracellular Mineral:    Greigite (Fe3S4) nanocrystal chains for magnetotaxis
================================================================================
CONCLUSION:
Independent planetary genesis confirmed. Life is a thermodynamic inevitability in
alkaline hydrothermal vent environments. The transition from Rung 1 (Subsurface
Chemiosmosis) to Rung 4 (Relational Spaceflight) is bounded strictly by the presence
of surface fire, metallurgy, and relational metrology.
================================================================================
```
"""

def main():
    path = os.path.join(MANUSCRIPT_DIR, "Exhibits_and_Appendices.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXHIBITS.strip() + "\n")
    print(f"Generated: Exhibits_and_Appendices.md ({len(EXHIBITS.split())} words)")

if __name__ == "__main__":
    main()
