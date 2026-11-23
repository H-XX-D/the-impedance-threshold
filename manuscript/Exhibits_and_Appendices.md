# DIEGETIC EXHIBITS & MATHEMATICAL APPENDICES
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
In ArgonautOS, developed by Dr. Ryan Vance, covariance matrices are completely discarded. The state uncertainty is parameterized strictly by the upper-triangular **Square-Root Information Matrix** $\mathbf{R}$, where $\mathbf{P}^{-1} = \mathbf{R}^T \mathbf{R}$, and the information vector $\mathbf{z} = \mathbf{R} \hat{\mathbf{x}}$.

```cpp
// =============================================================================
// ARGONAUTOS REVISION 6.1: SQUARE-ROOT INFORMATION FILTER (SRIF) CORE
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

struct SRIFState {
    int32_t R[STATE_DIM][STATE_DIM]; // Upper triangular information matrix (Q16.16)
    int32_t z[STATE_DIM];            // Information state vector (Q16.16)
    int32_t x_hat[STATE_DIM];        // Estimated state (m, m/s in Q16.16)
};

// Fixed-point Q16.16 multiply-accumulate with saturation
inline int32_t q16_mul(int32_t a, int32_t b) {
    int64_t temp = static_cast<int64_t>(a) * static_cast<int64_t>(b);
    return static_cast<int32_t>(temp >> 16);
}

// Fixed-point square root via integer Newton-Raphson
int32_t q16_sqrt(int32_t val) {
    if (val <= 0) return 0;
    int64_t x = val;
    int64_t y = (x + 65536) >> 1;
    for (int i = 0; i < 8; ++i) {
        y = (y + (x << 16) / y) >> 1;
    }
    return static_cast<int32_t>(y);
}

// In-place Householder QR orthogonalization across the measurement tableau
void householder_srif_update(SRIFState& state, 
                            const int32_t H[MEAS_DIM][STATE_DIM], 
                            const int32_t y[MEAS_DIM], 
                            const int32_t V_inv[MEAS_DIM]) {
    int32_t A[TOTAL_ROW][STATE_DIM + 1];
    std::memset(A, 0, sizeof(A));

    // Fill prior information
    for (int i = 0; i < STATE_DIM; ++i) {
        for (int j = i; j < STATE_DIM; ++j) {
            A[i][j] = state.R[i][j];
        }
        A[i][STATE_DIM] = state.z[i];
    }

    // Fill new measurement information
    for (int i = 0; i < MEAS_DIM; ++i) {
        for (int j = 0; j < STATE_DIM; ++j) {
            A[STATE_DIM + i][j] = q16_mul(V_inv[i], H[i][j]);
        }
        A[STATE_DIM + i][STATE_DIM] = q16_mul(V_inv[i], y[i]);
    }

    // Householder transformations to eliminate sub-diagonal elements
    for (int k = 0; k < STATE_DIM; ++k) {
        int64_t sum_sq = 0;
        for (int i = k; i < TOTAL_ROW; ++i) {
            sum_sq += static_cast<int64_t>(A[i][k]) * A[i][k];
        }
        int32_t norm_x = static_cast<int32_t>(std::sqrt(sum_sq));
        if (norm_x == 0) continue;

        int32_t alpha = (A[k][k] > 0) ? -norm_x : norm_x;
        int32_t u_k = A[k][k] - alpha;
        int64_t u_norm_sq = static_cast<int64_t>(u_k) * u_k;
        for (int i = k + 1; i < TOTAL_ROW; ++i) {
            u_norm_sq += static_cast<int64_t>(A[i][k]) * A[i][k];
        }

        if (u_norm_sq == 0) continue;

        for (int j = k; j <= STATE_DIM; ++j) {
            int64_t dot = static_cast<int64_t>(u_k) * A[k][j];
            for (int i = k + 1; i < TOTAL_ROW; ++i) {
                dot += static_cast<int64_t>(A[i][k]) * A[i][j];
            }
            int32_t gamma = static_cast<int32_t>((dot << 1) / u_norm_sq);

            A[k][j] -= q16_mul(gamma, u_k);
            for (int i = k + 1; i < TOTAL_ROW; ++i) {
                A[i][j] -= q16_mul(gamma, A[i][k]);
            }
        }
        A[k][k] = alpha;
    }

    // Extract updated upper-triangular information matrix R and vector z
    for (int i = 0; i < STATE_DIM; ++i) {
        for (int j = i; j < STATE_DIM; ++j) {
            state.R[i][j] = A[i][j];
        }
        state.z[i] = A[i][STATE_DIM];
    }

    // Back-substitution to solve R * x_hat = z
    for (int i = STATE_DIM - 1; i >= 0; --i) {
        int64_t rhs = static_cast<int64_t>(state.z[i]) << 16;
        for (int j = i + 1; j < STATE_DIM; ++j) {
            rhs -= static_cast<int64_t>(state.R[i][j]) * state.x_hat[j];
        }
        state.x_hat[i] = static_cast<int32_t>(rhs / state.R[i][i]);
    }
}
```

---

## DIEGETIC EXHIBIT B: FORMAL MATHEMATICAL DERIVATION OF 0D PREGEOMETRY
### The Nested-Reciprocity Source Law $S_{\rm pre}^{\rm NR}$ & Relational Impedance $Z_H$

### 1.0 THE 0D SOURCE GROUPOID & TRANSVERSE RECIPROCITY
Let space in its underlying condition be zero-dimensional and nonlocal. We define a pregeometric configuration as a pair $(D, M)$ on a source groupoid:
1. $D$ is a finite unlabelled set of primitive reversible excitation types, with cardinality $n = |D|$.
2. $P_2(D) = \binom{D}{2}$ is the set of all unordered binary spans (every pair is present).
3. $M \subseteq D \times P_2(D)$ is a partial matching, injective in both projections, with cardinality $m = |M|$.
4. Every matched pair is **transverse**:
   $$(d, p) \in M \implies d \notin p$$

The empty object $D = \varnothing$ represents the undifferentiated 0D condition: it possesses no moves, no adjacencies, and no metric distance. The relational grades $\Lambda^0, \dots, \Lambda^3$ of $\mathbb{R}[D]$ (undifferentiated condition, primitive excitation, coupled binary span, transverse interleaving) form an increasing filtration, retaining all lower-dimensional constituents.

### 2.0 THE NESTED-RECIPROCITY SOURCE LAW
The reciprocity defect $\Delta(D, M)$ measures the sum of unmatched primitive excitations plus unmatched binary spans:
$$\Delta(D, M) = (n - m) + \left( \binom{n}{2} - m \right)$$

For coupling constants $\lambda > 0$ and activity parameter $h \in \mathbb{R}$, the pregeometric action is defined by:
$$S_{\rm pre}^{\rm NR}(D, M) = \lambda \, \Delta(D, M) - h \, n$$

The groupoid partition function across all isomorphism classes is:
$$Z_\beta = \sum_{n \ge 0} \frac{1}{n!} \sum_{M} \exp\left( -\beta S_{\rm pre}^{\rm NR}([n], M) \right)$$
where each class is weighted by $1 / |\operatorname{Aut}(D, M)|$.

### 3.0 THE RANK-THREE SELECTION THEOREM
**Theorem (Rank-3 Ground State Selection):**  
*In the open activity window $0 < h < 2\lambda$, the unique ground state minimizing $S_{\rm pre}^{\rm NR}$ up to relabelling has rank $n = |D| = 3$ with the complete complement matching ($m = 3$), with an exact excitation energy gap:*
$$\Delta E = \min(3h, 2\lambda - h)$$

*Proof Summary:*  
For $n = 3$, the binary spans are $\binom{3}{2} = 3$ pairs: $\{1,2\}, \{2,3\}, \{3,1\}$. The unique transverse matching pairs each element with the opposite span: $1 \leftrightarrow \{2,3\}$, $2 \leftrightarrow \{3,1\}$, and $3 \leftrightarrow \{1,2\}$. Thus $m = 3$, yielding zero defect:
$$\Delta(3, 3) = (3 - 3) + (3 - 3) = 0 \implies S_{\rm pre}^{\rm NR} = -3h$$
For any $n \neq 3$, the defect $\Delta(n, m) \ge 1$, which adds a penalty $\ge \lambda$. In the window $0 < h < 2\lambda$, all competing configurations have strictly higher action, establishing rank 3 as the isolated, stable ground state of the universe. $\blacksquare$

### 4.0 THE CUBIC-DIFFUSIVE SPATIAL PHASE
Under least endpoint completion and a centered unit-rate walk on the selected rank-3 carrier, the operational properties of physical three-dimensional space emerge without coordinates:
1. **Exact Word-Ball Volume:**
   $$V_3(R) = \frac{4R^3 + 6R^2 + 8R + 3}{3}$$
2. **Heat Kernel Return Probability:**
   $$P(t) = e^{-t} I_0(t/3)^3$$
3. **Spectral Dimension:**
   $$d_s = -2 \lim_{t \to \infty} \frac{d \ln P(t)}{d \ln t} \equiv 3$$
4. **Infrared Co-Metric Tensor:**
   $$q^\sharp = \frac{1}{3} \sum_{d \in D} d \otimes d$$

Three-dimensional space is therefore an emergent operational property of the rank-3 ground state of transverse reciprocity.

### 5.0 INTERNAL GAUGE CARRIER & CHIRAL FAMILIES
On a Hermitian $2+3$ internal carrier with a single determinant record, the stabilizer group is:
$$S(U(2) \times U(3)) = \frac{SU(2) \times SU(3) \times U(1)}{\mathbb{Z}_6}$$
recovering the exact Standard Model gauge structure. The exterior algebra decomposition yields one anomaly-free 15-state chiral fermion family, while the pair-dual anomaly polynomial:
$$\mathcal{P}(m, n) = (m + n - 5) \operatorname{ch}_3(E)$$
selects internal ranks $m=2, n=3$ within its own hypotheses.

### 6.0 CAUSAL IMPEDANCE & GENERAL RELATIVITY
Following the Margolus-Levitin theorem (1998), an ensemble of quantum states cannot evolve to an orthogonal distinguishable state in a time interval shorter than:
$$\Delta t \ge \frac{\pi \hbar}{2 \langle E \rangle}$$

At the Planck energy $E_P = \sqrt{\hbar c^5 / G}$, the maximum causal orthogonalization rate across an informational channel is:
$$\nu_{\max} = \frac{1}{\Delta t_{\min}} = \frac{2}{\pi} \sqrt{\frac{c^5}{\hbar G}}$$

The relational transmission impedance of the channel is:
$$Z_H = \frac{c^3}{G} \approx 4.037 \times 10^{35} \text{ N}$$

**The Governing Measurement Principle:**
$$d_P(a, b) := \mathcal{M}_P[Z_H; a, b]$$
*Distance is the inferred measurement of causal impedance. Causal impedance does not cause a separate substance called distance.*

General Relativity proved that spacetime has no independent existence apart from physical relations, proper times, and clocks. Gravitational time dilation and Shapiro delay do not represent an elastic fabric bending in a void, but the physical causal impedance matching of relational clock networks.

---

## DIEGETIC EXHIBIT C: SAGNAC RING LASER PHASE METROLOGY
### Giles County Underground Cut: Relational Tidal Analysis

![Sagnac Ring Laser Interferometer & Underground Cut](assets/plate_06_exhibits_ring_laser.png)

### 1.0 RING LASER CAVITY TOPOLOGY
The Giles County Sagnac facility consists of an equilateral triangular ring laser cavity with a perimeter $P = 16.000\text{ m}$ enclosing an area $A = 110.851\text{ m}^2$, mounted on six vibration-isolated Barre granite surface tables $1,200\text{ meters}$ below the surface in an inactive section of the Giles County limestone mine.

The Sagnac beat frequency $\Delta f$ produced by the interference of counter-propagating 1,550 nm optical beams is:
$$\Delta f = \frac{4 A}{\lambda P} (\vec{\Omega} \cdot \hat{\mathbf{n}})$$
where $\lambda = 1,550.42\text{ nm}$, $\vec{\Omega}$ is the rotation vector of the Earth, and $\hat{\mathbf{n}}$ is the normal vector to the cavity plane oriented at latitude $37.362^\circ\text{ N}$.

### 2.0 EMPIRICAL TIDAL LATENCY LOG

The table below records the observed phase lag of the Sagnac rotational beat note during transits of the principal lunar diurnal tide ($O_1$, period $25.819\text{ hours}$):

| Run ID | Transit Epoch (UTC) | Optical Beat Frequency | Observed Phase Lag $\phi_{\text{obs}}$ | Relational Light-Time Latency |
| :--- | :--- | :--- | :--- | :--- |
| **GC-26-081** | 2026-10-14 01:12:08 | $348.62142 \text{ Hz}$ | $1.284 \text{ s}$ | $1.282 \text{ s}$ |
| **GC-26-082** | 2026-10-15 02:01:19 | $348.62148 \text{ Hz}$ | $1.291 \text{ s}$ | $1.285 \text{ s}$ |
| **GC-26-083** | 2026-10-16 02:50:31 | $348.62145 \text{ Hz}$ | $1.288 \text{ s}$ | $1.284 \text{ s}$ |
| **GC-26-084** | 2026-10-17 03:39:44 | $348.62140 \text{ Hz}$ | $1.286 \text{ s}$ | $1.283 \text{ s}$ |

The measured time delay of $1.286 \pm 0.005\text{ s}$ precisely matches the one-way cislunar light travel time ($r / c = 1.282\text{ s}$), demonstrating that lunar gravitational tidal forces operate as unattenuated causal relational latencies rather than instantaneous Newtonian stresses or static metric curvature.

---

## DIEGETIC EXHIBIT D: SILICA AEROGEL HYPERVELOCITY HUGONIOT EQUATIONS
### Soft-Arrest Thermomechanical Proofs

### 1.0 SHOCK COMPRESSION AT MACH 7
When an ice grain of diameter $d_p = 50\ \mu\text{m}$ strikes a collection medium at $v_{\text{rel}} = 2,214\text{ m/s}$, the shock Hugoniot jump conditions dictate the pressure $P_H$ and specific internal energy increase $\Delta e$:
$$P_H - P_0 = \rho_0 U_s u_p$$
$$e_H - e_0 = \frac{1}{2} (P_H + P_0) \left( \frac{1}{\rho_0} - \frac{1}{\rho_H} \right)$$

In solid quartz or titanium ($\rho_0 = 2.65 - 4.5\text{ g/cm}^3$), $U_s \approx 5,000\text{ m/s}$, resulting in $P_H > 35\text{ GPa}$ and post-shock peak temperatures $T > 3,000\text{ K}$, causing complete thermal pyrolysis of organic molecules.

### 2.0 SOL-GEL DISSIPATION IN GRADED AEROGEL
In the graded aerogel tile, the initial density $\rho_0 = 0.005\text{ g/cm}^3$ reduces the bulk sound speed to $c_0 \approx 70\text{ m/s}$. The equation of state is governed by irreversible compaction of the silica network:
$$P(\rho) = P_{\text{crush}} \left( \frac{\rho - \rho_0}{\rho_{\text{solid}} - \rho} \right)^{1/n}$$

The hydrodynamic drag force acting on the particle is:
$$F_d = \frac{1}{2} C_d \rho(x) A_p v^2$$
Because $\rho(x)$ increases continuously from $0.005$ to $0.060\text{ g/cm}^3$ over a track length $L = 18\text{ mm}$, the peak deceleration is bounded to:
$$a_{\max} \le 1.4 \times 10^7 \text{ m/s}^2$$

The thermal dissipation is absorbed by the sublimation of a thin boundary layer of water vapor ($\Delta m / m < 0.02$), which creates an insulating Knudsen gas buffer around the particle core. Numerical integration demonstrates that the internal core temperature of the ice grain satisfies:
$$T_{\text{core}}(t) \le -10^\circ\text{C} \quad \forall t \in [0, 42\text{ s}]$$
preserving the intact stereochemistry of caldarchaeol lipids and peptide nucleic acids.

---

## DIEGETIC EXHIBIT E: THREE-BODY INVARIANT MANIFOLDS & GATEWAY NRHO
### Heteroclinic Manifold Connections

![Three-Body Invariant Manifold Tubes & Lunar Capture](assets/plate_09_exhibits_manifold_transfer.png)

### 1.0 CIRCULAR RESTRICTED THREE-BODY PROBLEM (CR3BP)
In the rotating frame of the Earth-Moon system, the equations of motion for the Earth-Return Vehicle are:
$$\ddot{x} - 2\dot{y} = \frac{\partial \Omega}{\partial x}$$
$$\ddot{y} + 2\dot{x} = \frac{\partial \Omega}{\partial y}$$
$$\ddot{z} = \frac{\partial \Omega}{\partial z}$$
where the effective pseudo-potential $\Omega(x,y,z)$ is:
$$\Omega = \frac{1}{2}(x^2 + y^2) + \frac{1-\mu}{r_1} + \frac{\mu}{r_2}$$
with mass ratio $\mu = M_{\text{Moon}} / (M_{\text{Earth}} + M_{\text{Moon}}) \approx 0.01215$.

### 2.0 MANIFOLD CAPTURE TRAJECTORY
The ERV’s 3,860.4 m/s perigee braking burn at $h = 600\text{ km}$ above Earth targets the **Stable Invariant Manifold Tube** $W^s(\gamma)$ associated with the Earth-Moon $L_2$ collinear Lagrange halo family. The trajectory coasts along the invariant tube without propulsive maneuvers, intersecting the Lunar Gateway Near-Rectilinear Halo Orbit (NRHO) at the perilune passage:
* Aposelene Altitude: $70,000 \text{ km}$ (over Lunar South Pole)
* Perilune Altitude: $3,000 \text{ km}$ (over Lunar North Pole)
* Orbital Period: $6.56 \text{ days}$ (4:1 lunar synodic resonance)

---

## DIEGETIC EXHIBIT F: TANDEM MASS SPECTROMETRY & BIOCHEMICAL PROTOCOLS
### Characterization of Extraterrestrial Macromolecules

### 1.0 CRYO-TEM VITRIFICATION PROTOCOL
1. Aerogel tracks sectioned at $T = 90\text{ K}$ using an ultrasonic diamond microtome inside a liquid-nitrogen-shielded glovebox.
2. Harvested ice grains transferred to Quantifoil R 1.2/1.3 holey carbon copper grids.
3. Rapid plunge-freezing into liquid ethane at $-183^\circ\text{C}$ to prevent ice crystallization.
4. Imaging conducted on a Thermo Scientific Krios G4 Cryo-TEM operating at 200 kV with a K3 direct electron detector in counting mode at $180,000\times$ magnification.

### 2.0 TANDEM MASS SPECTROMETRY FRAGMENTATION CHANNELS
Electrospray ionization (ESI) in positive ion mode reveals the following diagnostic fragment ions confirming the presence of caldarchaeol tetraether lipid monolayers and Peptide Nucleic Acid (PNA):

| Precursor ($m/z$) | Collision Energy | Major Product Ions ($m/z$) | Molecular Identification |
| :--- | :--- | :--- | :--- |
| **1,302.2** $[M+H]^+$ | $45 \text{ eV}$ | $651.1, 742.6, 1,210.1$ | **Caldarchaeol Tetraether** ($\text{C}_{86}\text{H}_{172}\text{O}_6$) |
| **742.6** | $30 \text{ eV}$ | $371.3, 560.5$ | Biphytanyl C40 hydrocarbon core |
| **412.2** $[M+H]^+$ | $25 \text{ eV}$ | $264.1, 149.0$ | **PNA Monomer: AEG-Diaminopurine** |
| **383.1** $[M+H]^+$ | $20 \text{ eV}$ | $235.1, 149.0$ | **PNA Monomer: AEG-Uracil** |
| **427.2** $[M+H]^+$ | $28 \text{ eV}$ | $279.1, 149.0$ | **PNA Monomer: AEG-Iso-Guanine** |
| **384.1** $[M+H]^+$ | $22 \text{ eV}$ | $236.1, 149.0$ | **PNA Monomer: AEG-Iso-Cytosine** |

The universal $m/z = 149.0$ product ion corresponds to the cleaved aminoethylglycine (AEG) backbone fragment ($[\text{NH}_2-\text{CH}_2-\text{CH}_2-\text{NH}-\text{CO}-\text{CH}_2]^+$), proving the complete absence of phosphate diester bonds and confirming the neutral peptide backbone of the Europa genetic code.

---

### ARCHIVAL VERIFICATION
This technical repository is cataloged and certified under the international authority of the Interstellar Argonaut Society (IAS) by **Todd Hendrixx**, Chief Systems Certifier and Historian of Record.
