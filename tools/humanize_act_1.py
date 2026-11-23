import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

ch1 = r"""# CHAPTER ONE
## The Three-Body Clock
### The Zero-Point Stutter

The air sixty feet beneath Giles County smelled of damp dolomite and sulfur.

It was an old quarry shaft, originally bored out in the 1930s and later stabilized with steel rock bolts and shotcrete when the university took it over for seismic isolation. The temperature stayed at a steady eight degrees Celsius year-round, which was good for the optics but miserable for the joints. 

Dr. Ryan Vance sat on an overturned milk crate beside an unpainted aluminum equipment rack, his hands tucked inside the sleeves of a heavy woolen sweater. On the folding table before him, an electric kettle with a cracked plastic handle was humming softly, boiling water for another cup of instant black tea.

Across the optical bench, Dr. Kenji Sato was tightening an SMA connector on the rubidium standard with an open-ended torque wrench. Kenji was sixty-one, formerly of Sandia's primary standards laboratory, with bad eyesight and the infinite patience of a man who had spent four decades measuring volts and seconds.

"Give it another eighth of a turn," Ryan said, watching the noise floor on the spectrum analyzer.

"I know how to seat an SMA, Ryan," Kenji said without looking up. The wrench clicked twice. "That's twenty-six ounce-inches. If the ground loop is still there, it's coming from the sub-station down the road, not my cable."

On the central workstation display, thirty gigabytes of raw baseband radio telemetry were scrolling in silent green columns. The feed was piped in over a leased dark-fiber line from the Robert C. Byrd Green Bank Telescope in West Virginia, four hundred miles to the northeast.

The signal was the pulse profile of **PSR J0337+1715**.

Every 2.73 milliseconds, the pulsar swept its emission beam across the solar system like a lighthouse on a rocky coast. In the astronomical catalogs, it was listed as a millisecond pulsar in a hierarchical triple system: a 1.44-solar-mass neutron star locked in an inner 1.6-day orbit with a cool helium white dwarf, both of them circled every 327 days by a second, more distant white dwarf. Because the three relativistic bodies pulled on one another with violent gravitational gradients, the system was the cleanest natural clockwork in the known galaxy.

For four years, the standard timing pipelines—TEMPO2, running the standard post-Keplerian orbital models—had predicted pulse arrival times down to the microsecond.

Except for the last six weeks.

Whenever the Moon crossed the local meridian, swinging through its monthly perigee, the arrival times of the pulses recorded by the 100-meter dish lagged.

By 1.54 microseconds.

### The Missing Dispersion

"Check the spectral split again," Kenji said, reaching for his tea.

Ryan clicked the mouse, bringing up the channelized time-of-arrival residuals across the receiver bands.

"Eight-hundred-twenty megahertz is lagging three point seven one microseconds," Ryan said. "Fourteen-hundred megahertz is lagging three point seven zero. Two-point-one gigahertz is lagging three point seven one."

Kenji took a sip of his tea, squinted through his bifocals at the plot, and frowned.

"That's flat," Kenji said.

"It's completely flat," Ryan said. "If this were cold plasma in the interstellar medium, or ionospheric disturbance over the Allegheny Mountains, the group delay would drop with the square of the frequency:

$$\Delta t_{\text{plasma}} \propto \frac{\text{DM}}{f^2}$$

"At two gigahertz, the delay should have collapsed by a factor of six compared to P-band. It didn't. The ratio between P-band and S-band is 1.002 plus or minus 0.015. It is completely achromatic across a factor of two and a half in electromagnetic frequency. There's zero plasma dispersion."

Kenji set his mug on the edge of the optical table. "Then the hydrogen maser at Green Bank has a thermal drift in the multiplier chain."

"I pulled the logs from the US Naval Observatory in DC, the optical strontium clock at Plum Brook, and the rubidium clock on the Deep Space Network station in Goldstone," Ryan replied quietly. "All three independent atomic time scales show the exact same residual shape. The delay curve tracks the lunar gravitational potential $\Phi_{\text{Moon}}(t)$ to six significant figures."

Kenji pulled off his wire-rimmed glasses and rubbed the bridge of his nose. The silence in the cavern was heavy, broken only by the faint, rhythmic whirr of the vacuum turbopumps on the perimeter ring.

"A gravitational wave?" Kenji asked.

"No," Ryan said. "A gravitational wave is a transverse quadrupole. It stretches one axis and compresses the perpendicular axis while keeping volume constant. It shows up in an interferometer as a differential strain between two arms. This isn't strain. It's retarding the clock rate itself."

### The Speed of Update

Ryan picked up a stub of yellow chalk from the table and walked over to the smooth, exposed dolomite face of the cavern wall.

"Think about how we write down the equations," Ryan said, drawing three small circles representing the Earth, the Moon, and the pulsar. "Every flight dynamics model at NASA, every orbit propagator in Houston, treats space as an empty Cartesian grid. An infinite, pre-existing coordinate box. When an object moves, the model updates the coordinates $(x, y, z)$. But in nature, there is no grid. Space is not a container."

"It's relations," Kenji said, nodding slowly. "We've known that since Leibniz."

"Right, but take it seriously," Ryan said, tapping the chalk against the stone. "Distance is not an empty interval. Distance is the inferred measurement of causal impedance:

$$d \equiv \int Z_H \, d\tau$$

"Now look at the Margolus-Levitin theorem from quantum information theory. What is the fundamental quantum limit on how fast any physical system can move from one orthogonal state to another?

$$\frac{dN}{dt} \le \frac{2 E}{\pi \hbar} = \frac{2 M c^2}{\pi \hbar}$$

"The maximum update rate of reality is strictly proportional to mass-energy," Ryan said. "Mass is not stuff sitting inside an empty geometric space. Mass is an intense concentration of local quantum updates. It is update-rate density."

He drew a photon track passing close to the Moon.

"When you place ten to the twenty-second kilograms of mass into a region, you concentrate ten to the seventy-second state transitions every second. The relational network becomes congested. Information takes longer to propagate through that cluster of updates. To an observer with a clock far away, light appears to slow down. That is why the vacuum exhibits an effective refractive index:

$$n(r) = 1 + \frac{2GM}{c^2 r}$$

"Light doesn't curve because space is a rubber sheet bent by bowling balls," Ryan said. "It curves because the wavefront experiences Fermat refraction across an update-latency gradient. And because the latency is an informational property of the network itself, it is strictly achromatic. Radio, optical, X-rays—they all slow down by the exact same nanosecond count."

Kenji looked at the chalk marks on the limestone, his expression guarded. "It's an elegant interpretation, Ryan. But you know what happens when you tell the navigation community that Cartesian coordinates are an illusion."

"They don't have to believe the philosophy," Ryan said, walking back to his terminal. "They just have to look at their telemetry."

### The Artemis Downlink

Ryan shifted the display to a secondary browser window. It showed a password-protected telemetry stream mirrored from NASA Glenn's research intranet: the live downlink of **Artemis-7**, the lunar exploration vehicle *Prometheus*.

On board were Commander Elena Rostova, lunar geologist Aris Thorne, and systems specialist Chen Wei. Launched four days prior from Cape Canaveral, the spacecraft was ninety-four thousand kilometers out, descending toward perilune insertion into a Near-Rectilinear Halo Orbit.

On the telemetry strip, a series of warning indicators were blinking yellow:

`NAV_RESIDUAL_TREND: +0.18 M/SEC / MIN`  
`KALMAN_INNOVATION_NIS: 14.92 (LIMIT: 16.80)`  
`STATE_ESTIMATOR: GEONS_V4.2 [SINGLE_PRECISION]`  

"Look at their filter," Ryan whispered. "Elena's flight computer is running GEONS in 32-bit single precision. It assumes the Moon's gravity is an external potential expanding in spherical harmonics. As *Prometheus* drops into the lunar update well, the real optical arrival times from their star trackers are lagging behind their Cartesian model."

"The covariance matrix is starving," Kenji noted, his voice tightening. "The diagonal elements are collapsing toward rank one."

"If the Normalized Innovation Squared crosses 16.8," Ryan said, "the software assumes the star trackers have suffered a catastrophic hardware failure. It trips `PROTECTIVE_SCREENED_COAST`."

"And if it trips during the perilune approach?"

"The engine interlocks lock shut," Ryan said. "They miss orbital capture. They skim the lunar farside at twenty-four hundred meters per second, run out of consumables, and drift into a dead solar orbit."

Ryan picked up his satellite phone from the bench. "I have to call Elena."
"""

ch2 = r"""# CHAPTER TWO
## The Montgomery Shape Sphere
### Building 30

The Flight Dynamics Room inside Building 30 at the Johnson Space Center had no windows, no natural light, and the temperature of a meat locker.

The air conditioning roared through the underfloor plenums, maintaining a dry forty-six degrees Fahrenheit to prevent the central mainframe racks from overheating. Dr. Elena Rostova sat at the Guidance, Navigation, and Control console on the third row of the pit. Her flight jacket was zipped to her chin, her knuckles raw from the cold air blowing off the keyboard.

On her primary monitor, the numbers were drifting out of tolerance:

`INNOVATION_NIS: 16.22 (ALARM @ 16.80)`  
`POSITION_UNCERTAINTY_COV: 412.4 M (CROSS_TRACK)`  
`OPTICAL_LIMB_RESIDUAL: -3.84 SIGMA`  
`PROPAGATOR: DOP853_CARTESIAN_32BIT`  

Standing three steps up on the flight director's riser behind her was Warren Hastings. Hastings was fifty-four, a former Navy test pilot turned senior administrator, whose neat gray hair and tailored blazer gave him the appearance of a corporate vice president rather than an engineer.

"Rostova, suppress that caution flag," Hastings said over the back of her chair. "The public affairs loop is patching in the Administrator for the translunar media update in ten minutes. I don't want a yellow banner sitting in the lower corner of the primary display."

Elena didn't touch the key. She turned slowly in her swivel chair, looking up at him.

"I can't suppress it, Warren," Elena said, her voice flat and controlled. "The optical limb cameras are reporting the lunar horizon four hundred meters higher than the ephemeris. The laser altimeter is confirming the same error. The spacecraft is physically thirty-eight kilometers closer to the perilune boundary than the software thinks it is."

"It's sensor glint," Hastings replied smoothly. "The forward star-tracker baffles are picking up solar reflection off the service module radiator panels. We saw the same artifact in the sim runs at Huntsville."

"It's not glint," Elena said, pointing a steady finger at the covariance matrix. "Look at the off-diagonal terms. They're oscillating at the orbital frequency. The filter has become covariance-starved. It has become completely overconfident in its internal numerical model. It is weighting its own equations ninety-nine to one over real optical measurements."

### The Arithmetic of Failure

Elena leaned forward, her voice dropping into the quiet, lethal precision of an engineer who had found the smoking gun.

"The flight code runs in single precision," she said. "Thirty-two bits. Near the collinear Lagrange points between the Earth and the Moon, the gravitational pull of the two bodies cancels out to four decimal places. When you subtract two nearly equal numbers in 32-bit floating point, you lose sixteen bits of mantissa precision on every single integration step. It's roundoff cancellation, Warren. The integrator is literally throwing away half its significant digits."

"That software was certified across four thousand Monte Carlo runs by Axiom-Lockheed," Hastings said, his voice hardening. "It has ten thousand hours of test-bench pedigree. It is flight-proven."

"It was certified on simulated data that assumed flat space and linear error propagation!" Elena retorted. "Look at the rate of NIS growth. It's climbing at zero point two every sixty seconds. In four minutes, it hits 16.8. When it hits 16.8, the fault management architecture executes an automatic abort. It trips `PROTECTIVE_SCREENED_COAST`."

"And if it trips," Hastings said coldly, "we execute the contingency timeline. We dump the forward hydrazine tanks to adjust the center of gravity, drop into manual RCS rate control, and fire the auxiliary thrusters on time-to-go."

"A blind burn?" Elena stood up, her headset wire pulling taut against the console. "If you fire seventy kilonewtons of thrust while your position covariance is corrupt by four hundred meters, you won't enter halo orbit. You will drive *Prometheus* straight into the farside rim of Antoniadi crater at two kilometers per second."

Her console's private voice circuit chimed twice. A discreet text string appeared in the diagnostic window:

`INCOMING ENCRYPTED VOIP: VANCE_R [NODE_TN_01]`

Elena glanced at Hastings. He had stepped away to talk to the public affairs officer at the Capcom desk. She touched the earbud in her left ear, clicking the channel open.

"Go ahead, Ryan," she murmured.

"Elena, do not let Hastings dump the hydrazine," Ryan Vance's voice came through, clear and quiet over the encrypted carrier. "The problem isn't just roundoff error in your integrator. It's your coordinates."

### Shape Space

"I'm seeing a four-hundred-meter position bias," Elena whispered, watching Hastings out of the corner of her eye. "The altimeter and star trackers are disagreeing with the Cartesian state."

"Because Cartesian coordinates have singularities in three-body phase space," Ryan said. "When three bodies interact gravitationally, space is not $\mathbb{R}^3 \times \mathbb{R}^3 \times \mathbb{R}^3$. You have to quotient out translations and rotations. What remains is the **Montgomery Shape Sphere**."

Elena frowned, visualizing the topology. "Richard Montgomery's shape space."

"Exactly," Ryan said. "If you normalize the moment of inertia, the configuration of the Earth, the Moon, and *Prometheus* is a single point on a two-dimensional sphere:

$$S^2 = \left\{ (u, v, w) \in \mathbb{R}^3 : u^2 + v^2 + w^2 = 1 \right\}$$

"On that sphere, the equator represents collinear configurations where the three bodies lie on a straight line. The poles represent the equilateral Lagrange configurations, $L_4$ and $L_5$. And there are three collision points on the equator."

"And our trajectory?"

"Your trajectory in real physical space is an unknotted geodesic winding smoothly across that sphere," Ryan said. "When you use Cartesian coordinates, you are projecting that curved Riemannian manifold onto flat tangent planes with coordinate poles. Every time *Prometheus* approaches the collinear line between Earth and Moon, the Cartesian coordinates experience an artificial coordinate shear. That's why your Kalman filter is blowing up."

"And the update latency?" Elena asked.

"The Moon's mass-energy concentrates local quantum updates," Ryan explained. "The optical wavefront from the lunar limb is delayed by one point five four microseconds because of network latency:

$$\Delta \tau = \int \frac{GM(r)}{c^2 r} dt$$

"Your single-precision GEONS filter expects the optical wavefront to arrive at time $t$. When it arrives at $t + 1.54\,\mu\text{s}$, the filter interprets that time lag as a four-hundred-meter spatial displacement. It tries to correct an error that doesn't exist, and the covariance collapses."

### The Threshold Breaks

Elena looked down at her screen.

The numbers were ticking upward with agonizing certainty:

`INNOVATION_NIS: 16.68`  
`INNOVATION_NIS: 16.75`  
`INNOVATION_NIS: 16.81`  

A sharp, electronic warble cut through the Flight Dynamics Room.

On the main situational display, the cyan trajectory line of *Prometheus* broke into a dashed amber track. Across Elena's console, three warning banners flashed red:

`CRITICAL_FAULT: GNC_COVARIANCE_COLLAPSE`  
`FAULT_ACTION: PROTECTIVE_SCREENED_COAST`  
`MAIN_ENGINE_STATUS: HARD_LOCKED / INHIBITED`  
`TIME_TO_PERILUNE: 41 MIN 12 SEC`  

Flight Director Hastings marched back down the riser, his jaw set in rigid, defensive fury.

"That's it," Hastings announced over the flight loop. "We have a software runaway on the primary GNC bus. Capcom, advise *Prometheus* to prepare for manual hydrazine dump and contingency attitude hold. We take her down on the backup checklist."

Elena stood her ground, her voice cutting through the panic in the room like ice:

"Warren, if you send that command, you are killing three people."

"I am following the flight rules, Dr. Rostova," Hastings said without looking at her. "Step away from the console."
"""

ch3 = r"""# CHAPTER THREE
## The Expanding Causal Boundary
### The Arrival

The rain had turned the dirt access road into a trough of red clay.

Dr. Kenji Sato stood by the open doorway of the surface shed, wiping grease from his fingers with a shop rag. Through the sodden leaves of the white oak trees, headlights appeared: two sets of high-intensity halogen beams bouncing along the ruts, followed by the low, heavy rumble of diesel engines.

Two black Chevy Suburbans and a Dodge Ram utility truck pulled through the chain-link gate, parking in an angled formation across the gravel turnaround.

"Ryan," Kenji called into the dark interior of the shed. "We have visitors. Two sedans and a service truck with federal plates."

Ryan Vance walked out of the underground portal, wiping mud from his boots. In his right hand, he carried a heavy canvas satchel containing the project logbooks and two encrypted solid-state drives.

The doors of the Suburbans opened. Four men stepped out into the freezing drizzle. They wore dark gray rain slickers over civilian tactical gear, with federal law enforcement badges hanging on lanyards around their necks. Leading them was a tall, lean man in his late forties with a damp leather jacket and a folder tucked inside his coat.

"Dr. Vance?" the man asked, stepping onto the gravel. His voice was neutral, bureaucratic, and entirely without malice. "I'm Special Agent Miller, Department of Commerce Office of Export Enforcement. This is Agent Harris from the Defense Technology Security Administration."

"You drove a long way for a radio astronomy project, Agent Miller," Ryan said, keeping his hands visible on his bag.

"This ceased to be a radio astronomy project twelve hours ago, Dr. Vance," Miller replied, opening his folder. "We have an administrative impoundment order issued under Title 50, United States Code, and the International Traffic in Arms Regulations, Category XV."

"Category XV covers spacecraft systems and military inertial guidance," Kenji noted dryly from the doorway. "This is an underground Sagnac interferometer testing low-frequency lunar tides."

"It's a high-bandwidth digital receiver tapping the Green Bank maser, running proprietary autonomous guidance software cross-linked to NASA Johnson telemetry," Miller corrected smoothly. "Axiom-Lockheed filed a formal complaint with the Department of State this morning alleging unauthorized extraction of proprietary guidance state vectors and unlicensed dissemination ofITAR-controlled navigation algorithms."

### The Impoundment

Miller gestured to the two technicians waiting by the utility truck. "Our instructions are to secure all digital storage media, disconnect the fiber uplinks, and impound the prototype processing hardware for technical review."

"There is no proprietary Axiom software here," Ryan said, his voice quiet and even. "The code running on our hardware is ArgonautOS. It was written from scratch in open-source C++ under an academic research grant funded by the National Science Foundation."

"That will be determined during the administrative audit, Doctor," Miller said, stepping toward the shed portal. "In the meantime, please step aside and allow my technicians to enter the facility."

Kenji Sato didn't move from the doorway. He leaned casually against the wooden frame, looking Miller directly in the eye.

"Agent Miller, beneath this shed is a twelve-hundred-meter optical fiber ring running under ten to the minus nine torr vacuum, cooled by liquid helium compressors," Kenji said. "If your technicians go down there and start yanking breaker switches without following the cryogenic shutdown checklist, the turbomolecular pumps will seize, the superconducting quantum detectors will suffer thermal runaway, and you will release six hundred liters of gaseous helium into a confined subterranean cavern. You'll suffocate yourselves before you find a single USB drive."

Miller paused, glancing at his lead technician. The technician hesitated, looking at the complex schematic Kenji pulled from his pocket.

"We have certified aerospace technicians, Dr. Sato," Miller said, though his tone had lost some of its bureaucratic certainty.

"Good," Kenji said, handing him the checklist. "Then they know that an orderly cryo-safing sequence takes forty-five minutes. In the meantime, the server racks are in Sector B."

Kenji turned back into the shed, his voice dropping as he leaned toward Ryan: "Grab the FPGA flight core and the truck keys. I already killed the primary power to the fiber transceiver. The cache is wiped."

### The Back Adit

Ryan slipped through the rear equipment bay of the surface shed.

The gold-plated aluminum chassis of the **ArgonautOS Navigation Core** sat on the workbench, its dual Kintex UltraScale+ FPGAs already secured inside a foam-padded Pelican storm case. Ryan latched the four nylon dogs shut, slung the strap over his shoulder, and stepped through the rear door into the wet cedar woods.

The air was sharp with the scent of wet pine needles and ozone. Fifty yards down the ridge, half-hidden beneath a tangle of wild blackberry brambles, was the rusted iron portal of the old coal prospecting adit.

He didn't run. Running attracted attention. He walked deliberately along the slippery limestone outcrop, the twelve-kilogram Pelican case balanced against his hip, his boots sinking into the wet leaf mold.

Behind him, through the trees, he heard the muffled shouts of the federal technicians as they began their inspection of the shed, accompanied by the dull, metallic clang of an equipment box being loaded onto the truck bed.

Ryan ducked through the brambles, slipping into the dark mouth of the adit.

The tunnel was narrow, cold, and dry, its sandstone roof supported by rotting white-oak shoring timbers from ninety years ago. He switched on his headlamp, keeping the beam aimed strictly at the ground. Water seeped through the sandstone seams, pooling in the old iron-cart wheel ruts.

He walked for eight hundred yards beneath the limestone ridge, his breathing steady, counting the timber sets in the dark.

*One hundred and twelve... one hundred and thirteen...*

At the far end of the adit, the tunnel opened onto the overgrown embankment of an abandoned county drainage ditch bordering State Route 166.

Waiting on the gravel shoulder, its diesel engine idling with a steady, rhythmic clatter, was a matte-gray Ford F-350 with a battered aluminum tool rack.

The driver's window rolled down. Marcus Thorne leaned his elbow on the sill, a paper cup of black coffee in his hand.

"They shut you down?" Marcus asked.

"They brought Category XV impoundment paperwork," Ryan said, sliding the Pelican case onto the front bench seat and climbing in. "Kenji is walking them through a forty-five-minute cryogenic checklist to keep them busy."

Marcus put the truck into gear and pulled smoothly onto the wet asphalt, heading north.

"Hastings sent the abort command to *Prometheus* twenty minutes ago," Marcus said, his eyes fixed on the empty two-lane highway. "Elena refused to execute the hydrazine dump. She locked the manual valves from the cockpit."

Ryan looked over at him. "How do you know that?"

Marcus reached into his jacket pocket and pulled out a small, encrypted handheld radio tuned to the military cislunar relay.

"Because my daughter is on that ship, Ryan," Marcus said, his voice flat and hard. "And she knows what happens when you fire an engine on a bad trajectory."
"""

ch4 = r"""# CHAPTER FOUR
## The Silicon Horizon
### Plum Brook Station

NASA Glenn Research Center's Plum Brook Station sat fifty miles west of Cleveland, surrounded by six thousand acres of flat, wind-swept Ohio farmland enclosed by double-strand chain-link fence.

Established during the Second World War as an ordnance manufacturing works and later repurposed during the Apollo era, Plum Brook was home to the Space Power Facility (SPF)—the largest thermal vacuum chamber in the world. The chamber was an architectural mountain of aluminum and concrete: an inner vacuum vessel one hundred feet in diameter and one hundred and twenty-two feet high, enclosed within an outer concrete containment dome with walls eight feet thick.

At 04:15 EST, Marcus Thorne pulled the Ford F-350 up to the western security gate.

The guard in the booth was an older man in a navy-blue contract security uniform with a Thermos of coffee on his desk. He glanced at Marcus's NASA Glenn contractor badge, looked at the temporary vehicle pass taped to the windshield, and nodded.

"High bay is prepped for the vibration shake-table run, Mr. Thorne," the guard said, pressing the button to lift the hydraulic barrier. "Cleanroom team is scheduled for 07:00."

"Understood," Marcus said. "We're running a preliminary continuity check on the avionics bus before the techs arrive."

Marcus drove down the perimeter road, past the empty cryogenic storage spheres, and pulled directly into the auxiliary loading dock behind the main vacuum chamber dome.

The high bay inside was vast, silent, and cold. The overhead sodium-vapor lamps buzzed softly sixty feet above the polished concrete floor, casting long, amber shadows across rows of test equipment, hydraulic ground-support dollies, and aluminum staging scaffolding.

Resting on four pneumatic vibration-isolation pedestals in the center of the bay was **Argonaut**.

### The Airframe

She was an uncrewed, high-delta-v technology demonstrator built under an advanced logistics development contract: a six-meter hexagonal prism constructed of carbon-fiber composite and titanium-aluminide trusswork. 

At her base sat twin fifteen-kilowatt Hall-effect electric propulsion thrusters, flanked by four high-pressure hydrazine reaction control pods. Mounted beneath her forward avionics deck was a universal docking mechanism equipped with both an androgynous capture collar and an active mechanical probe.

And strapped beneath her primary propulsion truss, resting on an articulated rail dolly, was a twenty-two-foot **Castor 30XL** solid rocket upper stage—the high-thrust booster intended for her translunar injection qualification flight.

"She's fully fueled," Marcus said, walking up the aluminum access ramp. "Twenty-two thousand kilograms of HTPB solid propellant in the booster, four hundred kilograms of xenon in the electric propulsion tanks, and a full hydrazine load in the RCS quads."

Ryan climbed the staging ladder to *Argonaut*’s forward equipment bay. He opened the composite access panel labeled `AVIONICS_PRIMARY`.

Inside sat the standard NASA flight computer: a BAE RAD750 single-board computer enclosed in an aluminum chassis. Its clock speed was a modest 133 megahertz, running a heritage version of VxWorks.

"Unbolt it," Marcus said, handing Ryan a socket driver.

Ryan loosened the four mounting bolts, pulled the Mil-Spec locking pins, and slid the RAD750 chassis out of its guide rails. He placed it carefully on the workbench beside the staging ladder.

From the Pelican storm case, he lifted the gold-plated chassis of the **ArgonautOS Navigation Core**.

The unit slid smoothly into the empty bay on precision-machined Teflon runners. Ryan connected the primary MIL-STD-1553 data bus harnesses, the dual SpaceWire LVDS data lines, and the 28-volt DC power cables from the spacecraft's lithium-iron-phosphate battery bank.

He flipped the auxiliary avionics breaker on the diagnostic panel.

A faint, high-frequency whine spun up inside the chassis as the chip-scale rubidium atomic clock stabilized its vapor cell. On the small maintenance OLED monitor mounted to the chassis, clean green lines scrolled across the display:

`ARGONAUT_OS_BOOT: OK`  
`KERNEL: cFS_DRACO_V7.0.1 (NATIVE_C++)`  
`SOLVER: 18_STATE_JACOBI_RELATIONAL_EKF`  
`FILTER_MODE: SQUARE_ROOT_JOSEPH_UPDATE`  
`REACQUISITION: CAUSAL_RELATIONAL_ACTIVE`  
`COVARIANCE_DIAG: POSITIVE_DEFINITE_VERIFIED`  
`CPU_LOAD: 7.2_WATTS @ 100_HZ`  

"She's booted," Ryan said, exhaling slowly. "ArgonautOS is running on the primary bus."

### The Test Campaign

Marcus leaned over the avionics bay, inspecting the telemetry registers on his diagnostic tablet.

"The trajectory solution to the lunar $L_1$ manifold is already pre-loaded in the prepare-before-issue journal," Marcus said. "If we fire the Castor booster, the burn arc is ninety-four seconds to escape velocity. Intercept time at perilune: sixty-four hours."

"We need authorization from Range Control at Wallops before that booster can be armed, Marcus," Ryan said, stepping down from the ladder. "You can't launch an orbital-class solid rocket without a flight termination receiver lock from Space Command."

Marcus looked at Ryan, his expression calm, measured, and completely devoid of melodrama.

"I called General Vance at Air Force Materiel Command three hours ago, Ryan," Marcus said quietly. "He signed off on an emergency technological evaluation flight under Defense Production Act Title III authority. Space Command isn't shooting us down. They're tracking us."

Marcus walked to the main high-bay control console, flipped open the safety covers, and touched the auxiliary hydraulic controls.

High above their heads, the massive, motorized roof panels of the Space Power Facility high bay began to roll back on their steel tracks with a low, thunderous rumble. Outside, the cold, gray morning sky of Ohio appeared through the opening, rain washing across the steel framework.

On the flight console, the ignition arming interlocks shifted from amber to green:

`RANGE_SAFETY: DPA_TITLE_III_EXEMPTION_CONFIRMED`  
`FLIGHT_TERMINATION: ARMED_AND_MONITORED`  
`GUIDANCE_MODE: ARGONAUT_OS_AUTONOMOUS_PRIMARY`  
`BOOSTER_STATUS: CASTOR_30XL_READY`  

Ryan climbed into *Argonaut*’s pressurized two-man command module, securing his five-point restraint harness beside Marcus. Outside the forward vision block, the vast dome opened to the morning clouds.

"Ten seconds to automated ignition sequence," Marcus said, his hands resting on the manual override controls. "Check your helmet seal, Ryan. We're going to the Moon."
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_01_The_Three_Body_Clock.md"), "w", encoding="utf-8") as f:
    f.write(ch1)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_02_The_Montgomery_Shape_Sphere.md"), "w", encoding="utf-8") as f:
    f.write(ch2)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_03_The_Expanding_Causal_Boundary.md"), "w", encoding="utf-8") as f:
    f.write(ch3)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_04_The_Silicon_Horizon.md"), "w", encoding="utf-8") as f:
    f.write(ch4)

print("Humanized Act I (Chapters 1-4) successfully.")
