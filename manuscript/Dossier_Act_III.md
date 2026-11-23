# INTER-ACT DOSSIER III
## Project ARGONAUT Phase C Critical Design Review
### Document Classification: NASA-HQ / Planetary Science Division Programmatic Baseline
#### Date of Archival: March 14, 2032 | Mission Phase: Flight Architecture & Hardware Fabrication

![Project ARGONAUT Callisto Staging & Aerogel Gun Bench](assets/plate_04_dossier_3_callisto_staging.png)

### 1.0 JOVIAN RADIATION SANCTUARY ARCHITECTURE

Project ARGONAUT avoids the lethal radiation environment of the inner Jovian magnetosphere by anchoring its mothership, automated fuel depot, and long-term science laboratory at the outermost Galilean satellite: **Callisto**.

#### 1.1 Galilean Satellite Radiation Environment Comparison
* **Io ($r = 421,700\text{ km}$):** Unshielded dose rate: **$3,600 \text{ rad/day}$**. Surface lifetime of electronics: $< 6\text{ hours}$.
* **Europa ($r = 670,900\text{ km}$):** Unshielded dose rate: **$540 \text{ rad/day}$**. Electronics lifetime: $< 40\text{ days}$.
* **Ganymede ($r = 1,070,400\text{ km}$):** Unshielded dose rate: **$8.0 \text{ rad/day}$**. Harsh magnetospheric trapping zone.
* **Callisto ($r = 1,882,700\text{ km}$):** Unshielded dose rate: **$0.012 \text{ rad/day}$**. Natural radiation sanctuary.

---

### 2.0 GRADED-DENSITY SILICA AEROGEL SPECIFICATION

To capture high-speed cryomagma ice grains from Europa's Manannán plume without thermal pyrolysis of organic compounds, the Skimmer probe utilizes an engineered four-stage graded aerogel matrix:

| Sol-Gel Layer | Density ($\rho$) | Thickness | Primary Physical Function | Maximum Temperature |
| :--- | :--- | :--- | :--- | :--- |
| **Layer 1: Entry** | $0.005 \text{ g/cm}^3$ | $4.0 \text{ mm}$ | Non-destructive particle penetration | $+184^\circ\text{C}$ (Surface Sheath) |
| **Layer 2: Drag** | $0.015 - 0.035 \text{ g/cm}^3$ | $8.0 \text{ mm}$ | Compressive vapor cushioning & deceleration | $+42^\circ\text{C}$ (Vapor Buffer) |
| **Layer 3: Arrest** | $0.060 \text{ g/cm}^3$ | $6.0 \text{ mm}$ | Subsonic soft-stop of intact frozen core | **$-12^\circ\text{C}$ (Frozen Core)** |
| **Layer 4: Backstop** | Grade-5 Ti / Sapphire | $2.0 \text{ mm}$ | Structural baseline & optical inspection | $-140^\circ\text{C}$ (Cryo Structural) |

---

### 3.0 LASER VACUUM WELDING SPECIFICATION

* **Laser Subsystem:** IPG Photonics 200W Ytterbium Single-Mode Fiber Laser ($\lambda = 1,070\text{ nm}$).
* **Optics:** 180-micron focal spot diameter, f/4 focusing objective, telecentric galvanometer scan head.
* **Weld Joint:** Circumferential knife-edge butt weld with pre-compressed copper-nickel crush gasket.
* **Process Environment:** Deep space vacuum ($P < 10^{-6}\text{ torr}$), cryogenic substrate ($T \approx -140^\circ\text{C}$).
* **Tracer Gas Charge:** 20 mbar of 99.999% pure Helium-4 tracer gas pre-loaded beneath titanium lid.
* **Qualified Leak Rate:** $< 4.2 \times 10^{-12}\text{ mbar}\cdot\text{L/sec}$ (Sniffer mass spectrometry verified).

---

### 4.0 PROGRAMMATIC CDR SIGN-OFF

* **Program Director:** Dr. Elena Rostova, NASA Headquarters.
* **Chief Architect:** Dr. Ryan Vance, Boulder Space Science Consortium.
* **Materials Lead:** Dr. Marcus Alvarez, Jet Propulsion Laboratory.
* **System Auditor:** Todd Hendrixx, Aerodynamics & Spaceflight Systems Archive.
