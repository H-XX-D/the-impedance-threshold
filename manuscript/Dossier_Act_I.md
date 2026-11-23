# INTER-ACT DOSSIER I
## The Green Bank Pulsar Baseline & Relational Reduction
### Document Classification: NASA-GSFC / NRAO Joint Technical Memorandum 2026-QRC-01
#### Date of Archival: October 28, 2026 | Location: Green Bank, West Virginia & Houston, Texas

![PSR J0337+1715 Timing & Montgomery Shape Sphere](assets/plate_02_dossier_1_pulsar_bench.png)

### 1.0 ASTROPHYSICAL CONTEXT & CELESTIAL CLOCK ARCHITECTURE

PSR J0337+1715 is a millisecond pulsar with a rotational period $P = 2.732588147618\text{ ms}$, exhibiting an intrinsic spin-down rate $\dot{P} \sim 10^{-20}\text{ s/s}$. The pulsar is embedded in a hierarchical three-body stellar system consisting of two degenerate helium white dwarf companions:

* **Inner Companion ($m_1$):** Degenerate helium white dwarf, $m_1 = 0.1975 M_\odot$, relative orbital semi-major axis $a_1 = 0.0319\text{ AU}$, orbital period $P_{\text{inner}} = 1.6294\text{ days}$. Eccentricity $e_{\text{inner}} = 0.00069$.
* **Outer Companion ($m_2$):** Degenerate helium white dwarf, $m_2 = 0.4104 M_\odot$, semi-major axis of its orbit about the inner binary $a_2 = 1.18\text{ AU}$, orbital period $P_{\text{outer}} = 327.25\text{ days}$. Eccentricity $e_{\text{outer}} = 0.0353$.
* **Pulsar Primary ($m_p$):** Highly relativistic neutron star, $m_p = 1.4378 M_\odot$, surface magnetic field $B \approx 2 \times 10^8\text{ Gauss}$.

Because the gravitational field of the outer companion strongly perturbs the inner binary orbit, PSR J0337+1715 represents the premier natural laboratory in the galaxy for testing the Strong Equivalence Principle (SEP) and non-linear multi-body gravitational interactions. Archibald et al. (2018) confirmed that the neutron star and the inner white dwarf fall toward the outer white dwarf alike to within $2.6 \times 10^{-6}$.

---

### 2.0 THE RELATIONAL SHAPE SPHERE FORMULATION

In standard astrophysics, multi-body ephemerides are formulated by integrating the post-Newtonian Einstein-Infeld-Hoffmann (EIH) equations of motion inside an artificial Barycentric Celestial Reference System (BCRS):
$$\frac{d^2 \mathbf{r}_i}{dt^2} = - \sum_{j \neq i} \frac{G m_j (\mathbf{r}_i - \mathbf{r}_j)}{r_{ij}^3} + \mathcal{O}(c^{-2})$$

In the QRC framework developed by Dr. Ryan Vance, the BCRS origin is discarded as an unmeasurable background artifact. The dynamics are mapped onto the **Montgomery Shape Sphere** using Jacobi coordinates.

#### 2.1 Mass-Weighted Jacobi Reduction
Let $\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3$ be the positions of the pulsar, inner companion, and outer companion. Define the Jacobi vectors:
$$\mathbf{u} = \sqrt{\frac{m_1 m_2}{m_1 + m_2}} (\mathbf{x}_2 - \mathbf{x}_1)$$
$$\mathbf{v} = \sqrt{\frac{m_3 (m_1 + m_2)}{m_1 + m_2 + m_3}} \left( \mathbf{x}_3 - \frac{m_1 \mathbf{x}_1 + m_2 \mathbf{x}_2}{m_1 + m_2} \right)$$

The shape coordinates $\mathbf{w} = (w_x, w_y, w_z)$ are defined by Hopf projection:
$$w_x = |\mathbf{u}|^2 - |\mathbf{v}|^2$$
$$w_y = 2 (\mathbf{u} \cdot \mathbf{v})$$
$$w_z = 2 (\mathbf{u} \times \mathbf{v}) \cdot \hat{\mathbf{n}}$$

On this sphere, the radius $R_s = |\mathbf{u}|^2 + |\mathbf{v}|^2$ measures the instantaneous moment of inertia of the system, while the angles $(\theta, \phi)$ determine its instantaneous triangle geometry. Binary collisions correspond to three fixed punctures on the equator, rendering the phase space globally compact and singularity-free under Kustaanheimo-Stiefel (KS) regularization.

---

### 3.0 OBSERVATIONAL RESIDUAL COMPARISON TABLE

| Epoch (MJD) | Observed TOA Residual (TEMPO2 / EIH) | QRC Relational Geodesic Residual | Variance Reduction |
| :--- | :--- | :--- | :--- |
| **55900.24** | $+12.4 \text{ ns}$ | $+0.8 \text{ ns}$ | $93.5\%$ |
| **56200.81** | $-18.6 \text{ ns}$ | $-1.1 \text{ ns}$ | $94.1\%$ |
| **56500.12** | $+22.1 \text{ ns}$ | $+1.4 \text{ ns}$ | $93.7\%$ |
| **56800.45** | $-14.9 \text{ ns}$ | $-0.9 \text{ ns}$ | $94.0\%$ |
| **57100.90** | $+16.8 \text{ ns}$ | $+1.2 \text{ ns}$ | $92.9\%$ |
| **57380.15** | $-21.4 \text{ ns}$ | $-1.0 \text{ ns}$ | $95.3\%$ |

**Summary Finding:** The relational QRC framework reduces post-fit timing variance from $18.4\text{ ns}$ down to $1.14\text{ ns}$ across 1,480 days of observation without invoking empirical quadrupole Love numbers or ad-hoc dark sector parameters.

---

### 4.0 SIGN-OFF & ARCHIVAL AUDIT

* **Primary Investigator:** Dr. Ryan Vance, Department of Physics, Virginia Polytechnic Institute (Dismissed / Independent).
* **Observer of Record:** Dr. Richard Harrison, Green Bank Observatory Liaison.
* **Flight Dynamics Witness:** Dr. Elena Rostova, Mission Operations Directorate, NASA Johnson Space Center.
* **Archival Certification:** Certified for inclusion in the National Radio Astronomy Observatory Historical Record by Todd Hendrixx.
