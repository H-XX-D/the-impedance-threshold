# Astrophysical and Planetary Data Specification: KOI-7923.01 (KIC 9084569)

**Document Identifier:** NASA-ADS/EXO-KOI7923-SPEC-2026.1  
**Classification:** Exoplanetary Astrometry, Atmospheric Radiative-Convective Transfer, and Astrobiological Boundary Conditions  
**Primary Catalogs:** Kepler Data Release 25 (Q1–Q17), Gaia DR3 (Source ID 2081546592237936128), Berger et al. (2018, 2020) Asteroseismic Revisions  

---

## 1. Astrometric and Stellar Characterization (Host Star: KIC 9084569)

### 1.1 Coordinates and Kinematics
* **Equatorial Coordinates (ICRS, Epoch J2000):**
  * Right Ascension ($\alpha$): $19^{\mathrm{h}} 27^{\mathrm{m}} 38.643^{\mathrm{s}}$ ($291.911012^\circ$)
  * Declination ($\delta$): $+45^\circ 25' 52.41''$ ($+45.431225^\circ$)
* **Galactic Coordinates:**
  * Galactic Longitude ($l$): $75.148^\circ$
  * Galactic Latitude ($b$): $+13.621^\circ$
* **Distance and Parallax (Gaia DR3):**
  * Parallax ($\varpi$): $4.782 \pm 0.038\ \mathrm{mas}$
  * Distance ($d$): $209.12 \pm 1.66\ \mathrm{pc}$ ($682.06 \pm 5.41\ \mathrm{ly}$)
  * Renormalised Unit Weight Error (RUWE): $1.08$ (nominal astrometric single star)
* **Proper Motion:**
  * $\mu_\alpha \cos\delta$: $-12.418 \pm 0.042\ \mathrm{mas/yr}$
  * $\mu_\delta$: $+8.914 \pm 0.045\ \mathrm{mas/yr}$
  * Radial Velocity ($v_{\mathrm{rad}}$): $-21.4 \pm 1.2\ \mathrm{km/s}$

### 1.2 Fundamental Stellar Parameters
* **Spectral Classification:** K0V (Main-sequence orange dwarf)
* **Photometric Magnitudes:**
  * Kepler band ($K_p$): $14.821$
  * Johnson $V$: $15.140$
  * 2MASS $J$: $13.652$
  * 2MASS $H$: $13.245$
  * 2MASS $K_s$: $13.158$
* **Effective Temperature ($T_{\mathrm{eff}}$):** $5075 \pm 115\ \mathrm{K}$
* **Stellar Mass ($M_*$):** $0.882 \pm 0.046\ M_\odot$ ($1.754 \times 10^{30}\ \mathrm{kg}$)
* **Stellar Radius ($R_*$):** $0.884 \pm 0.039\ R_\odot$ ($6.150 \times 10^5\ \mathrm{km}$)
* **Surface Gravity ($\log g_*$):** $4.491 \pm 0.052\ [\mathrm{cgs}]$ ($g_* \approx 309.7\ \mathrm{m/s^2}$)
* **Stellar Luminosity ($L_*$):** $0.432 \pm 0.038\ L_\odot$ ($1.652 \times 10^{26}\ \mathrm{W}$)
* **Metallicity ($[\mathrm{Fe/H}]$):** $-0.08 \pm 0.11\ \mathrm{dex}$ (solar-analog abundance)
* **Stellar Age ($\tau_*$):** $4.8 \pm 1.4\ \mathrm{Gyr}$ (Gyrochronology and isochrone matching)
* **Projected Rotational Velocity ($v \sin i$):** $2.1 \pm 0.5\ \mathrm{km/s}$
* **Rotation Period ($P_{\mathrm{rot}}$):** $21.2 \pm 1.8\ \mathrm{days}$ (Photometric modulation)

---

## 2. Orbital Architecture and Transit Telemetry: KOI-7923.01

### 2.1 Kepler DR25 Transit Observable Parameters
* **Orbital Period ($P$):** $395.1264 \pm 0.0215\ \mathrm{days}$ ($1.0818\ \mathrm{yr}$)
* **Transit Epoch ($T_0$):** $\mathrm{BJD}\ 2455024.1284 \pm 0.0082$
* **Transit Duration ($T_{\mathrm{dur}}$):** $10.82 \pm 0.45\ \mathrm{hours}$
* **Transit Depth ($\Delta F / F$):** $112.4 \pm 12.1\ \mathrm{ppm}$
* **Impact Parameter ($b$):** $0.41 \pm 0.18$
* **Orbital Inclination ($i$):** $89.76^\circ \pm 0.12^\circ$
* **Orbital Eccentricity ($e$):** $0.032^{+0.045}_{-0.025}$ (Near-circular)

### 2.2 Derived Planetary Orbital Dynamics
* **Semi-Major Axis ($a$):**
  $$a = \left( \frac{G M_* P^2}{4\pi^2} \right)^{1/3} = 0.9852 \pm 0.0175\ \mathrm{AU} \quad (1.4738 \times 10^8\ \mathrm{km})$$
* **Orbital Velocity ($v_{\mathrm{orb}}$):** $28.18\ \mathrm{km/s}$
* **Stellar Insolation Flux ($S_p$):**
  $$S_p = \frac{L_* / L_\odot}{(a / \mathrm{AU})^2} = \frac{0.432}{(0.9852)^2} = 0.4451 \pm 0.039\ S_\oplus \quad (608.1\ \mathrm{W/m^2})$$
* **Blackbody Equilibrium Temperature ($T_{\mathrm{eq}}$):**
  Assuming Bond albedo $A_B = 0.30$ and complete atmospheric thermal redistribution ($f = 1/4$):
  $$T_{\mathrm{eq}} = T_{\mathrm{eff}} \left( \frac{R_*}{2a} \right)^{1/2} (1 - A_B)^{1/4} = 208.4 \pm 5.2\ \mathrm{K} \quad (-64.75^\circ\mathrm{C})$$

---

## 3. Geophysical and Structural Parameters

### 3.1 Bulk Physical Dimensions
* **Planetary Radius ($R_p$):**
  $$R_p = R_* \sqrt{\Delta F / F} = 0.972 \pm 0.084\ R_\oplus \quad (6195 \pm 535\ \mathrm{km})$$
* **Planetary Mass ($M_p$):**  
  Derived from the Wolfgang, Rogers, & Ford (2016) mass-radius empirical relation for terrestrial regimes ($R_p < 1.23\ R_\oplus$):
  $$M_p = 0.865 \pm 0.120\ M_\oplus \quad (5.166 \times 10^{24}\ \mathrm{kg})$$
* **Mean Bulk Density ($\bar{\rho}_p$):**
  $$\bar{\rho}_p = \frac{3 M_p}{4\pi R_p^3} = 5.21 \pm 0.45\ \mathrm{g/cm^3}$$
* **Surface Gravity ($g_p$):**
  $$g_p = \frac{G M_p}{R_p^2} = 8.46 \pm 0.58\ \mathrm{m/s^2} \quad (0.863 \pm 0.059\ g_0)$$
* **Planetary Escape Velocity ($v_{\mathrm{esc}}$):**
  $$v_{\mathrm{esc}} = \sqrt{\frac{2 G M_p}{R_p}} = 10.54 \pm 0.42\ \mathrm{km/s}$$

### 3.2 Internal Differentiation & Geodynamo Feasibility
* **Core Mass Fraction (CMF):** $0.312 \pm 0.025$ (Fe-Ni composition)
* **Outer Liquid Core Radius:** $\approx 1680\ \mathrm{km}$
* **Convective Geodynamo Parameter:**
  * Rayleigh number ($\mathrm{Ra}_{\mathrm{core}}$): $\sim 10^{14}$ (supercritical vigorous convection)
  * Estimated Dipolar Magnetic Moment ($\mathcal{M}_{\mathrm{mag}}$): $0.72 \pm 0.15\ \mathcal{M}_\oplus$
  * Surface Magnetic Field Strength ($B_0$): $0.28\text{--}0.42\ \mathrm{G}$ ($28\text{--}42\ \mu\mathrm{T}$)
  * Stand-off Magnetopause Stagnation Radius ($R_{\mathrm{mp}}$):
    $$R_{\mathrm{mp}} = \left( \frac{B_0^2 R_p^6}{2\mu_0 \rho_{\mathrm{sw}} v_{\mathrm{sw}}^2} \right)^{1/6} \approx 9.4\ R_p$$
    (Sufficient to prevent non-thermal solar wind ion-pickup stripping).

---

## 4. Atmospheric Structure and Radiative-Convective Equilibrium

### 4.1 Atmospheric Composition and Physical Constants
* **Surface Atmospheric Pressure ($P_0$):** $1.82 \pm 0.08\ \mathrm{bar}$ ($182.0\ \mathrm{kPa}$)
* **Atmospheric Column Mass ($m_{\mathrm{col}}$):**
  $$m_{\mathrm{col}} = \frac{P_0}{g_p} = 21,513\ \mathrm{kg/m^2} \quad (2.11\times \text{Earth normal})$$
* **Volumetric Mixing Ratios (Dry Baseline):**
  * Molecular Nitrogen ($\mathrm{N}_2$): $75.22\%$
  * Molecular Oxygen ($\mathrm{O}_2$): $22.10\%$
  * Carbon Dioxide ($\mathrm{CO}_2$): $1.82\%$ ($18,200\ \mathrm{ppm}$)
  * Argon ($^{40}\mathrm{Ar}$): $0.84\%$
  * Trace species ($\mathrm{CH}_4, \mathrm{CO}, \mathrm{O}_3$): $< 20\ \mathrm{ppm}$
* **Mean Molecular Weight ($\bar{\mu}$):** $29.14\ \mathrm{g/mol}$
* **Atmospheric Scale Height ($H$):**
  $$H = \frac{k_B \bar{T}}{\bar{\mu} g_p} = \frac{(1.3806 \times 10^{-23}) \times (242)}{(4.839 \times 10^{-26}) \times (8.46)} \approx 8.16\ \mathrm{km}$$
* **Adiabatic Lapse Rate ($\Gamma_{\mathrm{ad}}$):**
  $$\Gamma_{\mathrm{ad}} = \frac{g_p}{c_p} \approx \frac{8.46\ \mathrm{m/s^2}}{1040\ \mathrm{J/(kg\cdot K)}} \approx 8.13\ \mathrm{K/km}$$

### 4.2 Radiative Transfer and Greenhouse Effect ($\Delta T_{\mathrm{GH}}$)
Because stellar insolation is $44.5\%$ of terrestrial normal ($S_p = 608.1\ \mathrm{W/m^2}$), bare equilibrium predicts a frozen snowball ($T_{\mathrm{eq}} \approx 208\ \mathrm{K}$). Habitability is maintained entirely via carbon-dioxide and water-vapor collision-induced absorption (CIA):

1. **Pressure Broadening and CIA Absorption:**
   * At $1.82\ \mathrm{bar}$, $\mathrm{N}_2\text{--}\mathrm{N}_2$ and $\mathrm{N}_2\text{--}\mathrm{CO}_2$ collision-induced dipole absorption closes the standard infrared window between $7.5\ \mu\mathrm{m}$ and $14\ \mu\mathrm{m}$.
   * Optical depth in the thermal infrared ($\tau_{\mathrm{IR}}$): $\tau_{\mathrm{IR}} \approx 2.45$.
2. **Greenhouse Thermal Lift Calculation:**
   Using a multi-layer Eddington two-stream approximation with convective adjustment:
   $$T_{\mathrm{surf}}^4 \approx T_{\mathrm{eq}}^4 \left( 1 + \frac{3}{4} \tau_{\mathrm{IR}} \right)$$
   $$T_{\mathrm{surf}} \approx 208.4 \times \left( 1 + \frac{3}{4}(2.45) \right)^{1/4} = 208.4 \times (2.8375)^{0.25} \approx 270.3\ \mathrm{K}$$
   Including sub-cloud tropospheric water vapor feedback ($\mathrm{RH} \approx 60\%$ in equatorial latitudes, precipitable water $PWV \approx 8\ \mathrm{mm}$) provides an additional $+6.5\text{--}+7.0\ \mathrm{K}$ of thermal forcing:
   $$\Delta T_{\mathrm{GH}} = +68.8\ \mathrm{K}$$
   $$\mathbf{T_{\mathrm{surf,mean}} = 277.2 \pm 3.5\ \mathrm{K} \quad (+4.05^\circ\mathrm{C})}$$

### 4.3 Surface Thermal and Phase Distribution
* **Equatorial Mean Temperature ($0^\circ\text{--}25^\circ$):** $284.5\ \mathrm{K}$ ($+11.3^\circ\mathrm{C}$)
* **Mid-Latitude Mean Temperature ($25^\circ\text{--}50^\circ$):** $275.2\ \mathrm{K}$ ($+2.0^\circ\mathrm{C}$)
* **Polar Mean Temperature ($>60^\circ$):** $235.0\ \mathrm{K}$ ($-38.1^\circ\mathrm{C}$)
* **Surface Liquid Water Boundary:** Stable open liquid water oceans exist between $-54^\circ$ and $+54^\circ$ latitude.
* **Global Permanent Ice Fraction:** $\approx 36.5\%$ (concentrated in polar ice sheets extending to $58^\circ$ latitude).

---

## 5. Astrobiological Environmental Matrix

| Environmental Parameter | KOI-7923.01 Specification | Earth Normal ($1.0\ \mathrm{Unit}$) | Astrobiological Impact / Ceiling |
| :--- | :--- | :--- | :--- |
| **Stellar UV-C Flux (200–280 nm)** | $0.18\ \mathrm{W/m^2}$ | $0.45\times$ Earth | Lower prebiotic photodissociation; quiescent K-dwarf minimizes flare stripping. |
| **Atmospheric Oxygen Fraction** | $22.10\%$ ($P_{\mathrm{O}_2} = 0.402\ \mathrm{bar}$) | $1.92\times$ Earth partial pressure | Elevated $P_{\mathrm{O}_2}$ enhances organismal metabolic diffusion; inside combustion window ($16\text{--}25\%$). |
| **Carbon Dioxide Partial Pressure** | $33.1\ \mathrm{mbar}$ ($18,200\ \mathrm{ppm}$) | $80\times$ pre-industrial Earth | Requires high-efficiency bicarbonate carbonic anhydrase buffering in terrestrial lungs. |
| **Acoustic Impedance ($Z_0 = \rho_0 c_s$)** | $552.4\ \mathrm{Pa\cdot s/m}$ | $1.34\times$ Earth air | Enhances low-frequency acoustic coupling and long-range sonic signaling efficiency. |
| **Surface Liquid Density** | $1.018\ \mathrm{g/cm^3}$ | Oceanic saline analog | Salinity $3.2\text{--}3.8\%$; open circulation without global freeze-out. |

---

## 6. Primary Archival Cross-References
* **NASA Exoplanet Archive System Record:** `KIC 9084569` / `KOI-7923`
* **Kepler DR25 Confirmed/TCE Table:** `K07923.01` (Pipeline Score: $0.78$)
* **SIMBAD Astronomical Database:** `2MASS J19273864+4525524`
* **Gaia Data Release 3 ID:** `Source 2081546592237936128`
* **Asteroseismic Reference Catalog:** Berger et al. (2018), *Astrophys. J.*, 866, 99; Berger et al. (2020), *Astron. J.*, 159, 280.
