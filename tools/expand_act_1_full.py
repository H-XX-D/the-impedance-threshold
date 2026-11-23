import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

ch1_full = r"""# CHAPTER ONE
## The Three-Body Clock
### The Zero-Point Stutter

The red warning beacon on the primary Sagnac console did not blink. It burned with a steady, surgical brilliance, casting long, crimson shadows across the damp limestone walls sixty feet beneath the rolling cedar glades of Giles County, Tennessee.

Dr. Ryan Vance sat hunched over his steel workstation. He wore a faded woolen sweater with frayed cuffs and fingerless climbing gloves, his breath condensing into pale, rhythmic plumes before his face. The ambient air in the subterranean vault was kept at precisely four degrees Celsius—not for human comfort, but to prevent the cryogenic helium compressors from suffering thermal runaway as they cooled the superconducting quantum interference detectors (SQUIDs) to four Kelvin.

For forty-eight continuous hours, Ryan had lived on lukewarm chicory coffee, dry oat biscuits, and the monotonous, low-frequency hum of vacuum turbopumps holding the twelve-hundred-meter optical ring at ten to the minus nine torr.

On his primary 4K display, thirty gigabytes of raw, coherent baseband radio telemetry captured from the Green Bank 100-meter telescope in Pocahontas County, West Virginia, were streaming across the screen. The waveform was an electrocardiogram of the deep cosmos: the pulse profile of **PSR J0337+1715**.

Every 2.732588 milliseconds, like an immaculate celestial clock, the millisecond pulsar rotated on its axis, sweeping a lighthouse beam of synchrotron radiation across the solar system. Four thousand light-years away in the constellation Taurus, it was embedded in a brutal, hierarchical three-body dance with two degenerate helium white dwarfs. The inner white dwarf, possessing only 0.2 solar masses, whirled around the 1.44-solar-mass neutron star once every 1.63 days. The outer companion, a heavier white dwarf of 0.4 solar masses, circled the inner pair every 327 days. Because the outer white dwarf pulled on the inner binary with fierce gravitational tides, J0337 was the premier natural laboratory in the galaxy for testing the foundations of gravitational physics.

According to Newtonian gravitation, Einstein's general relativity, and every textbook in the NASA Goddard library, the radio pulses should have arrived at the Green Bank dish with mathematical regularity, modulated only by the smooth, predictable Doppler shifts of the three-body orbit.

Instead, the pulses were stuttering.

As the Moon climbed toward the local meridian above the Appalachian ridge, swinging through its monthly perigee, the arrival times of the radio pulses recorded at Green Bank were lagging behind the ephemeris. 

Not by seconds. By 1.54 microseconds.

"It's not receiver jitter, Kenji," Ryan said softly, his voice echoing off the dripping dolomite ceiling. "And it's not the cold-plasma dispersion of the interstellar medium. Look at the spectral channel ratio."

Across the optical bench, Dr. Kenji Sato, a veteran metrologist from Sandia National Laboratories whose knuckles were scarred by liquid nitrogen frostbite, wiped grease from a calibrated torque wrench. He leaned over Ryan's shoulder, peering through wire-rimmed glasses at the real-time Fourier transform.

"If it were plasma dispersion," Kenji said, murmuring the standard astrophysical equations from memory, "the group delay would scale inversely with the square of the observation frequency:

$$\Delta t_{\text{plasma}} = \frac{e^2}{2\pi m_e c} \cdot \frac{\text{DM}}{f^2} \approx 4.1488 \times 10^3 \cdot \text{DM} \cdot f^{-2} \text{ s}$$

"A pulse at eight hundred and twenty megahertz would lag six and a half times longer than a pulse at two point one gigahertz," Kenji continued, pointing a calloused finger at the spectral split. "What is the measured ratio between P-band and S-band?"

"It's 1.000," Ryan said, highlighting the residual column in emerald phosphor. "Three point seven two microseconds at 820 megahertz. Three point seven zero microseconds at 2,100 megahertz. The ratio is 1.01 plus or minus 0.04. It is completely achromatic across a factor of two point five in electromagnetic frequency. There is zero plasma dispersion. There is zero ionospheric leakage."

Kenji set the wrench down. The metal clattered against a steel mounting jig, the sound sharp and lonely in the cavern. "Then it's the observatory clock, Ryan. The hydrogen maser at Green Bank drifted. A microsecond is four hundred meters of light-travel time. A thermal hiccup in the frequency multiplier."

"The maser didn't drift," Ryan said, spinning his terminal to display three synchronized timeline plots. "I cross-correlated the Green Bank timestamps against the cryogenic strontium optical lattice clock at the Plum Brook facility in Ohio and the deep-space atomic clock on Lunar Gateway. All three independent atomic references show the exact same residual curve. It tracks the lunar tidal potential $\Phi_{\text{Moon}}(t)$ to seven decimal places."

Kenji took a slow, sharp breath. He looked down at the massive, vacuum-sealed casing of the 1,200-meter fiber-optic Sagnac gyroscope that ringed the perimeter of the cavern floor. "A gravitational wave?"

"No," Ryan whispered. "A gravitational wave is a transverse tensor perturbation. It has two polarizations, plus and cross. It stretches one arm of an interferometer and compresses the orthogonal arm, while leaving the average volume element invariant. This isn't stretching space. It is retarding time itself."

### The Network Clock Rate

He stood up, walking toward the large whiteboard bolted to the limestone wall. He picked up a black dry-erase marker, his hand steady, driven by an urgent clarity that had kept him awake for three days.

"Think about how twentieth-century physics taught us to imagine the universe," Ryan said, drawing a massive grid of neat, perpendicular squares. "Newton called it Absolute Space. Einstein called it the metric tensor. But in practice, every engineer, every flight dynamics officer at NASA, and every GPS programmer in Colorado Springs treats space like an enormous, pre-existing spreadsheet. An empty Euclidean container with rows and columns. When an asteroid or a satellite moves from cell $(x_1, y_1)$ to cell $(x_2, y_2)$, they assume the container simply records the coordinates. But who updates the spreadsheet? What is the physical clock rate of reality?"

Kenji watched him, frowning. "The speed of light."

"Exactly," Ryan said, writing the Margolus-Levitin theorem on the board in bold, jagged strokes:

$$\frac{dN}{dt} \le \frac{2 E}{\pi \hbar} = \frac{2 M c^2}{\pi \hbar}$$

"The Margolus-Levitin theorem sets the ultimate quantum bound on how fast any physical system can process information," Ryan said. "The maximum rate of orthogonal quantum state transitions per unit time is strictly proportional to energy. Mass is not stuff stuffed into a geometrical box. Mass is an intense concentration of local state updates! It is clock rate density!"

He turned back to Kenji, his eyes burning with intensity.

"Space is not a medium, Kenji. There is no ether, no gelatinous fabric, no physical grid. Space is an emergent network of causal connections. When you place a massive body like the Moon into a region of the solar system, you are dumping ten to the twenty-second kilograms of mass-energy into that local causal cluster. By the Margolus-Levitin bound, that mass demands ten to the seventy-second state transitions every second! The local relational network becomes congested! Like an overloaded network switch routing millions of packets, it experiences computational latency!"

He drew a photon trajectory sweeping past the Moon, refracting along a curve.

"When a radio pulse from PSR J0337 passes through that congested zone, its causal path must traverse more relational updates. To an outside observer watching with an atomic clock, the photon appears to slow down. That is why the vacuum exhibits an effective refractive index:

$$n(r) = 1 + \frac{2GM}{c^2 r}$$

"Light bends not because space is a warped rubber sheet pulled down by bowling balls, but because the wavefront experiences Fermat refraction across an update-latency gradient! And because it is an informational latency inherent to the network itself, it is strictly achromatic! It slows radio waves, visible light, and X-rays by the exact same nanosecond count!"

"My God," Kenji murmured, staring at the equations. "If that's true, then gravitational time dilation is simply network ping time."

"It is causal impedance," Ryan said, tapping the console where the Sagnac interferometer data was humming. "And right now, NASA is flying the most expensive manned spacecraft in human history using software that doesn't know it exists."

### The Clandestine Tap

Ryan pointed at a secondary monitor tucked behind the pulsar receiver. It was a secure backchannel telemetry tap routed through the NASA Glenn research intranet, mirroring the live downlink of **Artemis-7**, the lunar exploration vessel christened *Prometheus*. 

On board were Commander Elena Rostova, lunar geologist Aris Thorne, and systems specialist Chen Wei. They had launched three days prior from Kennedy Space Center on an SLS Block 1B rocket, carrying a crew of three toward the first long-duration landing at the lunar south pole.

At this exact moment, *Prometheus* was sixty-five thousand kilometers from the Moon, accelerating toward the delicate perilune injection burn that would insert the spacecraft into a Near-Rectilinear Halo Orbit.

On the screen, a line of telemetry flashed yellow:

`WARN: NAV_EST_RESIDUAL_GROWTH > 4.2 SIGMA`  
`KALMAN_INNOVATION_NIS: 14.82 (REJECT_THRESHOLD: 16.80)`  
`STATE_PROPAGATION: GEONS_V4.2_SINGLE_PRECISION`  

"Look at their Kalman filter," Ryan whispered, the blood draining from his face. "Houston is running GEONS in single precision. They assume the Moon's gravity field is an external analytic potential expanding in spherical harmonics. As *Prometheus* drops into the Moon's update-latency well, the real causal arrival times of their optical star-tracker sightings are lagging behind their Cartesian model."

"The filter is starving," Kenji said, recognizing the symptoms immediately. "The covariance matrix is losing positive-definiteness."

"If their Normalized Innovation Squared exceeds 16.8, the GEONS algorithm will reject every subsequent optical measurement," Ryan said, his hands clenching into fists. "The flight software will assume the star trackers have suffered a catastrophic sensor failure. It will lock the thrusters and throw the spacecraft into `PROTECTIVE_SCREENED_COAST`."

"And on a hyperbolic lunar approach," Kenji added grimly, "a coast-lock means they miss the orbital capture window. They will slingshot around the farside, run out of consumables, and drift into a five-hundred-day solar orbit."

Ryan grabbed his satellite phone from the bench. "I have to call Elena."

### The Unspoken Alliance

Kenji watched Ryan punch the encrypted speed-dial code for Johnson Space Center. For twelve years, Kenji had worked in the black budget facilities of the Nevada test range and the underground corridors of Sandia. He knew how empires reacted when their fundamental technical assumptions were challenged from the outside.

"Ryan, put the phone down for ten seconds and think," Kenji said quietly. "If you bypass the Flight Dynamics Officer loop and call Elena Rostova on an unvetted circuit, Hastings will log the IP address. The moment Axiom-Lockheed realizes we are intercepting their raw GEONS state vectors, they won't open a scientific dialogue. They have forty billion dollars in cost-plus cislunar navigation architecture contracts riding on single-precision Cartesian flight computers."

"Elena is my friend, Kenji," Ryan said, the phone buzzing against his ear. "And more than that, she's the only pilot in the corps who actually understands non-Euclidean state propagation. If Hastings forces her to execute a manual hydrazine dump, she dies along with Aris and Chen."

"And what happens to us when the Aerospace Security Command sees a classified telemetry tap originating from an abandoned dolomite quarry in Tennessee?" Kenji asked, nodding toward the blast door. "We are operating outside every civilian NASA charter. We have an unlicensed cryogenic Sagnac ring, a direct tap into the Green Bank fiber line, and a breadboard guidance computer that violates ITAR Category XV."

"Then let them come," Ryan said as the ring tone clicked into an encrypted handshake. "The data doesn't care about their charters. Reality is running on an update clock they refuse to measure."

Across the digital carrier wave, a crisp, exhausted female voice answered:

*"Rostova. Go ahead, Ryan. Make it fast—the room is turning into a slaughterhouse."*
"""

ch2_full = r"""# CHAPTER TWO
## The Montgomery Shape Sphere
### The Houston Disconnect

The Flight Dynamics Room inside Building 30 at the Johnson Space Center was freezing. 

Air conditioning pumped forty-five-degree air through perforated floor tiles to chill rows of mainframe server racks, carrying the sharp scent of ozone, dry-erase cleaner, and stale cafeteria espresso. On the giant situational display at the front of the room, the trajectory of *Artemis-7 (Prometheus)* was represented as a brilliant cyan ellipse arcing outward from Earth toward the gray marble of the Moon.

Dr. Elena Rostova sat at the Guidance, Navigation, and Control console. Her flight suit sleeves were pushed up to her elbows, revealing pale forearms corded with tension. Her short dark hair was tucked behind her headset.

On her primary telemetry terminal, the numbers were bleeding out.

`GNC_EST_COV_DIAG: [ 1.42e-2, 2.11e-2, 8.94e-1 ]`  
`INNOVATION_NIS: 16.14 (LIMIT: 16.80)`  
`TRIP_STATUS: NOMINAL (ARMED)`  
`ALTIMETER_RESIDUAL: -412.6 m`  

Behind her, pacing the carpeted riser with his hands clasped behind his back, was Flight Director Warren Hastings. Hastings was fifty-four, a political heavyweight in NASA's Exploration Systems Development Directorate who had spent twenty years defending the legacy single-precision navigation architecture developed by prime contractor Axiom-Lockheed.

"Rostova, clean up that NIS trace," Hastings said, his voice flat and dismissive. "The media stream goes live in twelve minutes for the translunar broadcast. I don't want the Administrator seeing caution flags on the public network."

"I can't clean it up, Warren," Elena said, not turning around. Her fingers flew across the mechanical keyboard, dumping the raw optical residuals from the forward navigation cameras. "The optical limb tracker is reporting the Moon's horizon four hundred meters higher than the ephemeris. The laser altimeter is confirming the discrepancy. The spacecraft is physically thirty-eight kilometers closer to the perilune boundary than GEONS thinks it is."

"That's sensor noise," Hastings snapped. "The star tracker baffles are picking up solar glint off the service module solar arrays. The Kalman filter will damp it out once we pass into the lunar shadow."

"It's not glint!" Elena turned, her gray eyes burning. "Look at the covariance matrix. The diagonal elements are shrinking, but the cross-terms are oscillating. The filter has become covariance-starved. It has become overconfident in an incorrect Cartesian trajectory. It's weighting its own internal numerical model ninety-nine to one over live physical measurements!"

### The Singular Tangent

Elena tapped the glass of her display. "The algorithm is calculating the three-body gravitational interaction of Earth, Moon, and *Prometheus* using a single-precision Jacobi-integral approximation in Cartesian coordinates $(x, y, z)$. But near the collinear Lagrange points, the gravitational potentials of Earth and Moon cancel each other out to four decimal places. When you subtract two nearly equal numbers in 32-bit floating point, you suffer catastrophic roundoff cancellation! We are losing sixteen bits of mantissa precision on every integration step!"

"That software was certified across three thousand Monte Carlo runs on the supercomputers at Huntsville," Hastings barked, stepping down to her console. "It passed Phase C Critical Design Review with zero non-conformances. It is flight-proven."

"It was certified on simulated data that assumed Newtonian gravity in flat space!" Elena retorted. "Look at the NIS trend. It is climbing at zero point two per minute. At 16.8, the fault management architecture executes an automated software abort. It trips `PROTECTIVE_SCREENED_COAST`."

"And if it trips," Hastings said coldly, "we execute the contingency burn. We dump the forward hydrazine tanks to balance the mass ratio, drop into manual RCS control, and fire the auxiliary thrusters on time-to-go."

"A blind burn?" Elena stood up, her headset cord pulling taut. "If you fire the thrusters while the state covariance is corrupt, you will vector seventy kilonewtons of thrust along a hallucinated vector! You won't enter Near-Rectilinear Halo Orbit. You will impact the rim of Antoniadi crater at two kilometers per second!"

Her console's encrypted secondary comms channel chimed. A discreet notification flashed in the lower right corner of her private monitor:

`INCOMING ENCRYPTED VOIP: VANCE_R [GILES_VAULT_NODE_01]`

Elena glanced at Hastings. The Flight Director had turned away to confer with the Capcom and the public affairs officer. She reached down, tapped her personal earbud, and clicked the channel open.

"Ryan," she whispered. "Tell me you have something. Houston is sleepwalking off a cliff."

"Elena, do not let Hastings fire the manual RCS," Ryan Vance's voice crackled through the earbud, clear and razor-sharp over the encrypted quantum-keyed link. "The problem isn't roundoff error in your integrator. It's deeper than that."

"I'm seeing a 400-meter position error," Elena said quickly under her breath. "The altimeter and star trackers are disagreeing with the Cartesian state."

"Because Cartesian coordinates do not exist in nature!" Ryan said urgently. "You are flying a three-body problem using coordinates that assume space is an absolute Euclidean box. In a three-body system, the dynamics do not live on $\mathbb{R}^3 \times \mathbb{R}^3 \times \mathbb{R}^3$. They live on the **Montgomery Shape Sphere**!"

### The Spherical Manifold

"The shape sphere?" Elena murmured, her mind racing back to the groundbreaking papers by Richard Montgomery on the three-body problem.

"Yes!" Ryan said. "When three bodies interact gravitationally, you must quotient out translations and rotations. What remains is a three-dimensional space of shapes. If you normalize the moment of inertia, the configuration of the Earth, the Moon, and *Prometheus* is a single point on a two-dimensional sphere:

$$S^2 = \left\{ (u, v, w) \in \mathbb{R}^3 : u^2 + v^2 + w^2 = 1 \right\}$$

"On that sphere," Ryan continued, his voice hammering each word with relentless mathematical proof, "the equator represents collinear configurations where the three bodies lie on a straight line—Euler's configurations. The north and south poles represent Lagrange's equilateral triangle configurations, $L_4$ and $L_5$. And there are three collision points on the equator where two bodies collide."

Elena stared at her blank scratchpad, visualizing the geometry. "And our trajectory?"

"Your trajectory in real physical space is an unknotted geodesic winding across the surface of that sphere!" Ryan explained. "When you use Cartesian coordinates, you are trying to project a spherical Riemannian manifold onto a flat tangent plane with singularity poles. Every time *Prometheus* passes near the collinear axis between the Earth and the Moon, your Cartesian coordinates develop an infinite coordinate shear! That's what is choking your Kalman filter!"

"And the update latency?" Elena asked. "You told me in Tennessee that mass-energy retards network state transitions."

"The Moon's mass concentrates ten to the seventy-second quantum updates per second," Ryan said. "The causal path length between *Prometheus* and the Earth-Moon barycenter is dilated by:

$$\Delta \tau = \int \frac{GM(r)}{c^2 r} dt$$

"Your GEONS filter thinks the clock tick of reality is uniform everywhere. It expects the optical wavefront from the lunar limb to arrive at time $t$. But because of causal impedance, it arrives at $t + 1.54\,\mu\text{s}$. Your single-precision filter interprets that 1.54-microsecond delay as a four-hundred-meter spatial offset! The filter thinks the spacecraft is out of position, tries to correct it with a spurious mathematical innovation, and blows its own covariance to pieces!"

### The Shadow Closes

Elena felt a cold chill run down her spine. "Ryan... the NIS counter just crossed 16.4."

"How long until perilune?" Ryan asked.

"Forty-two minutes," Elena said. "Once we pass behind the Moon, we enter the radio blackout zone. DSN Canberra will lose our downlink. If the filter trips during the occultation, Hastings will order the blind hydrazine dump before we re-emerge."

"I am locking the Giles County Sagnac array onto your S-band transponder," Ryan said. "I am calculating your true geodesic trajectory in Montgomery shape coordinates on our FPGA core. But Hastings has to upload the square-root information filter patch before you hit the shadow!"

Elena looked up at the glass observation booth where Hastings stood, smiling as he briefed the NASA Associate Administrator.

"He won't upload it, Ryan," Elena said, her voice shaking with quiet fury. "Axiom-Lockheed owns the flight software contract. Admitting that Cartesian coordinates are flawed would invalidate their forty-billion-dollar cislunar constellation program. Hastings will kill three astronauts before he admits his software is broken."

"Then don't wait for him," Ryan said. "I am routing our guidance solution to an off-grid receiver. There's a backup."

"What backup?" Elena asked. "There is no other spacecraft in cislunar space!"

"Not yet," Ryan said. "Get your crew ready. We are coming."

Elena cut the link just as Hastings marched back down the riser, clapping his hands together with false bravado.

"Listen up, Flight Dynamics," Hastings announced to the room. "Canberra reports increasing plasma interference from the solar limb, but our nominal burn sequence remains green. Rostova, prep the auto-sequence upload for the AJ10 engine. We take *Prometheus* into orbit on the book."

Elena sat immobile, her fingers hovering above the keyboard. On her screen, the Normalized Innovation Squared ticked upward.

`INNOVATION_NIS: 16.74`  
`INNOVATION_NIS: 16.79`  
`ALARM: THRESHOLD_EXCEEDED`  
`FAULT_TRIPPED: PROTECTIVE_SCREENED_COAST`  
`ENGINE_STATUS: LOCKED`  

A piercing klaxon shrieked across Building 30.
"""

ch3_full = r"""# CHAPTER THREE
## The Expanding Causal Boundary
### The Sagnac Severance

The sound of heavy tires grinding across wet crushed gravel outside the surface shed was the only warning they got.

Dr. Kenji Sato was standing on a stepstool at the liquid nitrogen manifold, using a copper spanner to disconnect the primary boil-off line from the subterranean Sagnac ring, when the headlights flashed through the corrugated metal seams of the blast door. Three black Chevy Suburbans, their undercarriages caked with red Tennessee mud, pulled up to the outer chain-link perimeter gate.

"Ryan," Kenji whispered, his voice tightening as he dropped the spanner into his tool pouch. "We have company. And they didn't bring peer-review forms."

Ryan Vance didn't look up from his workbench. With a pair of ceramic-tipped tweezers, he was carefully disconnecting the twin high-speed serial Low-Voltage Differential Signaling (LVDS) ribbons that linked the cryogenic Sagnac interferometer to the central processing unit. 

He had known this raid was inevitable the moment he patched his terminal into the NASA Johnson Space Center telemetry loop. When a four-hundred-billion-dollar aerospace conglomerate holds the exclusive prime contracts for every military and civilian navigation constellation in Western orbit, the physicist who proves that classical Cartesian coordinates are a fatal fiction isn't treated as an innovator. He is treated as a national security breach.

On the workbench sat the heart of the entire QRC project: a twenty-centimeter cube of gold-plated, milled aluminum containing two Kintex UltraScale+ field-programmable gate arrays, a chip-scale rubidium atomic clock reference, and an isolated gallium-nitride (GaN) power switching stage. 

It was the complete, flight-hardened prototype of the **Square-Root Information Filter (SRIF)** and relational guidance processor—the only hardware on Earth programmed to navigate deep space using Montgomery shape-sphere dynamics and causal impedance metrics.

### The Breach

Above them, the surface shed's heavy steel outer door buckled with a deafening metallic boom. 

*BAM.*

A tactical hydraulic breaching ram.

"Federal marshals!" a voice bellowed through an electric bullhorn, distorted by the torrential rain. "Under Title 50, United States Code, and the International Traffic in Arms Regulations, this facility is under federal impoundment! Power down all transmitters and step away from the equipment!"

"ITAR," Kenji spat, climbing down from the stool. "They're claiming the pulsar clock is an unregistered dual-use inertial guidance weapon."

"It's not marshals leading them," Ryan said, glancing at the security camera feed on his secondary tablet. "Look at the uniforms behind the badges. Black tactical plate carriers, sterile velcro patches, Crye Precision BDUs. That's Axiom Tactical Solutions. Prime contractor private security."

"How much time do we have?" Kenji asked.

"Two minutes before they clear the upper blast airlock," Ryan replied. He clicked the locking latches on the gold-plated FPGA core, lifting the twelve-kilogram unit from its vibration-isolation cradle. He slid it into a ruggedized, foam-lined Pelican 1510 flight case, snapping the four glass-filled nylon latches shut.

"What about the servers?" Kenji asked, pointing at the eight racks of IBM blade servers storing ten years of raw pulsar timing data and the compiled ArgonautOS codebase.

"We don't leave them a single byte," Ryan said.

Kenji smiled grimly. He reached into a fireproof locker beside the liquid nitrogen tanks and pulled out two cylindrical steel canisters with yellow warning bands: military-grade thermite incendiary grenades. He cracked the magnesium ignition strikers and shoved them deep into the cable raceways between the central server racks.

A blinding, violet-white flare hissed to life. Within four seconds, the thermite burned at four thousand degrees Fahrenheit, melting the silicon motherboards, copper bus bars, and aluminum chassis into bubbling, incandescent pools of slag that dripped through the perforated floor plates into the drainage sump.

Above them, boots pounded down the concrete staircase leading into the cavern.

"Down the adit!" Kenji hissed, coughing as acrid white smoke from burning circuit boards began filling the vault.

### The Subterranean Adit

At the rear of the cavern, behind a rusty wire-mesh storage cage, was a narrow wooden portal set into the solid limestone wall. It was the entrance to an abandoned 1880s coal prospecting adit that snaked westward under the ridge for nine hundred yards, terminating in a briar-choked drainage culvert beside State Route 166.

"Kenji, come on!" Ryan yelled, hauling the Pelican case by its top handle.

"I'm right behind you—go!"

Ryan plunged into the darkness of the adit. The floor was shin-deep in freezing mud and mineralized runoff, the ceiling so low he had to bend nearly double. His headlamp flickered against rotting timber shoring and weeping dolomite seams. Behind him, automatic rifle fire cracked through the cavern—the sharp, suppressed *thwip-thwip-thwip* of 5.56 NATO rounds shattering glass vacuum tubes and bouncing off the stone walls.

"Cease fire! Cease fire!" an agent shouted in the vault. "The servers are slagged! Find the hard drives! Where did they go?"

Ryan didn't look back. His boots slipped on the slick shale bed of the subterranean stream. The Pelican case grew heavier with every yard, the twelve kilograms of gold-plated aerospace hardware slamming against his thigh. He focused on the rhythm of his breathing, the cold mud soaking through his trousers, and the mathematical equations running through his mind.

*Forty-two minutes until perilune. Artemis-7 is descending into the dark.*

Every step through the flooded coal shaft felt like wading through molasses. Water seeped over the tops of his hiking boots, numbing his toes. His lungs burned with the damp, sulfurous air of the mine. In his left hand, the Pelican case carried the entire future of relational astrophysics: twenty-seven thousand lines of hand-optimized VHDL, the square-root matrix decomposition algorithms, and the precise mathematical coordinates of the Montgomery shape sphere.

Behind him, Kenji's heavy breathing was punctuated by the occasional splash and curse. 

"They're not following us into the mine," Kenji called out between gasps. "The smoke from the thermite... it's backing up into the adit portal. The draft is blowing carbon monoxide behind us. They'd need rebreathers to make it twenty yards."

"Keep moving," Ryan urged. "The gradient steepens ahead. We're coming up under the western drainage cut."

### The Extraction on Route 166

After seven agonizing minutes of scrambling through the cramped shaft, the sour smell of stagnant coal runoff gave way to the sharp, clean scent of rain and wet cedar. 

Ryan scrambled up a muddy embankment, pushing through a dense tangle of blackberry brambles, and tumbled out onto the shoulder of Route 166.

Rain was pouring in blinding sheets, turning the asphalt into a black mirror.

Tires screeched on the wet pavement. A matte-gray Ford F-350 Super Duty dual-rear-wheel truck slid to a halt beside him, its diesel engine clattering like a freight train. The passenger door swung open.

Behind the wheel was Marcus Thorne.

Thorne was fifty-six, a former Air Force experimental test pilot who had logged twelve hundred hours in the X-37B and the F-22 before being quietly forced out of the astronaut corps for refusing to sign off on Axiom's flawed automated docking algorithms. He wore a greasy flight jacket with the patches ripped off and a baseball cap pulled low over cold, predatory blue eyes.

"Get in, Ryan!" Thorne roared over the thunder. "Throw the box in the footwell!"

Ryan threw the Pelican case into the cab and vaulted onto the bench seat, slamming the door. Thorne dropped the heavy transmission into gear, floored the accelerator, and the eight-ton truck broke traction, fishtailing across the road before rocketing northward into the storm.

"They breached the vault," Ryan said, catching his breath as he wiped freezing rain from his eyes. "Kenji stayed behind to drop the thermite."

"Kenji knows what he's doing," Thorne said grimly, glancing in the rearview mirror. "He has an attorney from Sandia already waiting at the county sheriff's department. They can't hold him without an indictment, and they can't indict him without the hardware."

Thorne tapped the Pelican case resting between Ryan's boots. "Is that the complete flight core?"

"Dual Kintex UltraScale+ FPGAs, rubidium clock, GaN power switches, and the entire ArgonautOS relational guidance stack," Ryan said. "It has the Montgomery shape-sphere solver and the square-root information filter."

"Good," Thorne said, leaning over the steering wheel as the windshield wipers swept furiously against the downpour. "Because we have a four-hour drive to Ohio, and the Air Force just placed the entire Midwest corridor under Class Echo airspace restrictions."

"Plum Brook?" Ryan asked.

"Plum Brook," Thorne confirmed with a grim smile. "The hangar doors are unlocked, the liquid oxygen tanks are pressurized, and *Argonaut* is waiting for her brain."
"""

ch4_full = r"""# CHAPTER FOUR
## The Silicon Horizon
### The Break-in at Plum Brook

The NASA Glenn Research Center's Plum Brook Station in Sandusky, Ohio, sat beneath a low, iron-gray canopy of Lake Erie cloud cover.

Surrounded by six thousand acres of high-security prairie enclosed by triple-strand razor wire, the facility housed the Space Power Facility (SPF)—the largest thermal vacuum chamber in the world. Built during the height of the Apollo program, the chamber was an architectural leviathan: an aluminum vacuum tank one hundred feet in diameter and one hundred and twenty-two feet high, enclosed within an outer concrete containment vessel with walls eight feet thick. It had tested everything from the Mars Pathfinder airbags to the Orion spacecraft service modules.

At 04:30 EST, the perimeter motion sensors on the western rail spur were disabled.

A set of heavy steel bolt-cutters severed the padlock on Gate 7. Marcus Thorne swung the Ford F-350 through the chain-link gap, killing the headlights and rolling on parking lamps across the cracked asphalt of the disused railway yard.

He pulled the truck directly into the auxiliary high-bay transfer airlock behind the SPF dome.

"We have thirty minutes before the automated perimeter sweep cycles back to this quadrant," Marcus said, stepping out into the cavernous concrete bay. He grabbed a heavy canvas mechanic's duffel bag from the truck bed. "Grab the case."

Ryan picked up the Pelican case and followed Marcus through the heavy acoustic personnel door into the central chamber area.

### The Leviathan in the Chamber

The space was immense, bathed in the amber, ghostly glow of high-pressure sodium lamps hanging eighty feet above the concrete floor. The air was dead, cold, and smelled of desiccated rubber seals and turbine lubricating oil.

And there, resting in the center of the vast high bay on an articulated hydraulic integration dolly, was **Argonaut**.

Seeing the spacecraft in person took Ryan's breath away. 

*Argonaut* was not a sleek, PR-approved NASA vehicle. She looked like an angular, predatory bird forged from aerospace-grade titanium and carbon-fiber composite. Designed originally as an uncrewed, high-delta-v technology demonstrator for deep-space autonomous interception, her fuselage was a hexagonal prism six meters long, flanked by two deployable composite solar array wings currently folded flat against her hull.

At her base sat twin fifteen-kilowatt Hall-effect electric propulsion thrusters, ringed by four high-thrust monopropellant hydrazine attitude control thruster pods. Mounted beneath her forward avionics deck was a universal docking mechanism equipped with both an androgynous peripheral attachment collar and an active mechanical capture probe.

And strapped beneath her primary propulsion truss, resting inside an open steel launch cradle, was a twenty-two-foot **Castor 30XL** solid rocket motor—an off-the-shelf, high-thrust orbital upper stage containing twenty-five thousand kilograms of hydroxyl-terminated polybutadiene (HTPB) solid propellant.

"She was supposed to be scrapped three months ago under the Axiom contract consolidation," Marcus said, patting the cold titanium skin of the spacecraft. "The brass said autonomous deep-space interceptors were redundant. They wanted all deep-space logistics centralized on the crewed Gateway architecture."

"Why did you keep her fueled?" Ryan asked, inspecting the braided stainless-steel propellant feedlines.

"Because I knew Hastings's software was going to fail," Marcus said, looking Ryan dead in the eye. "I watched them write the specs in 2024. They cut corners on the floating-point mantissa to save seven million dollars on space-qualified ASIC development. I knew the moment Artemis hit a complex three-body manifold, someone would have to go out there and fish them out."

### The Avionics Graft

Marcus climbed the aluminum staging ladder up to *Argonaut*’s forward avionics bay. He unlatched a composite access panel labeled `AVIONICS_BAY_PRIMARY`.

Inside sat the standard NASA flight computer: a BAE RAD750 single-board computer enclosed in a heavy, radiation-hardened aluminum chassis. Its clock speed was a pedestrian 133 megahertz, running an outdated version of VxWorks.

"Rip it out," Marcus said, handing Ryan a pneumatic socket wrench.

Ryan didn't hesitate. He unscrewed the four Mil-Spec mounting bolts, pulled the locking pins, and yanked the heavy RAD750 chassis out of the mounting rack. He set it on the floor of the bay like a discarded brick.

He popped the latches on the Pelican case.

He lifted the gold-plated QRC Kintex UltraScale+ core. It slid into the empty rack with a satisfying, precision-machined click. Ryan plugged in the primary MIL-STD-1553 bus cables, the high-speed SpaceWire LVDS data harnesses, and the heavy 28-volt DC power leads from the spacecraft's lithium-iron-phosphate battery bank.

He flipped the auxiliary avionics master switch on the diagnostic panel.

A high-pitched turbine whine spun up inside the core as the chip-scale rubidium atomic clock stabilized its vapor cell. On the small maintenance OLED display mounted to the chassis, green text scrolled at lightning speed:

`ARGONAUT_OS_BOOT: OK`  
`FPGA_0: KINTEX_ULTRASCALE_KU115 (ONLINE)`  
`FPGA_1: MONTGOMERY_SHAPE_SOLVER (ONLINE)`  
`ALTIMETER_FUSION: SQUARE_ROOT_FILTER_INITIALIZED`  
`COVARIANCE_INTEGRITY: POSITIVE_DEFINITE_GUARANTEED`  
`TIME_STANDARD: TA_QRC (LUNAR_LATENCY_COMPENSATED)`  
`TARGET_INTERCEPT: ARTEMIS_7 (PROMETHEUS) - NRHO_CORRIDOR`  

"She's alive," Ryan said, exhaling a breath he felt like he had been holding for three years.

### The Roof Blows

Suddenly, an alarm siren began whooping across the high bay. The amber sodium lights switched to pulsating red. 

Over the facility intercom, an automated security broadcast echoed:

`SECURITY BREACH: SECTOR 4 HIGH BAY. ARMED INTRUSION DETECTED. ALL PERSONNEL LOCK DOWN IMMEDIATELY.`

Through the reinforced vision panels of the transfer airlock, Ryan saw three black armored tactical vehicles crash through Gate 7, their high-intensity searchlights sweeping across the concrete floor. Men in black tactical gear poured out of the vehicles, carrying carbines at the low ready.

"They tracked the truck's transponder!" Marcus yelled. He leaped down the ladder, ran to the launch facility master console, and smashed his fist through the glass cover of a large red industrial breaker switch labeled `ROOF_EMERGENCY_VENT_OVERRIDE`.

"Marcus, what are you doing?" Ryan shouted.

"We can't launch through an open runway!" Marcus shouted back over the deafening sirens. "We launch right now, through the roof!"

He pulled the industrial breaker lever down.

With a series of thunderous, concussive explosions, thirty-two linear shaped-charge explosive bolts detonated along the perimeter of the SPF high-bay roof. The massive, thirty-ton retractable roof panels separated from their hydraulic tracks and were violently pushed outward by pneumatic rams, exposing the vast circular opening of the high bay to the dark, rain-swept night sky.

Bullets began pinging off the heavy steel launch cradle below *Argonaut*.

*Spang! Spang! Ricochet!*

"Get into the command module, Ryan!" Marcus roared, shoving Ryan up the access ladder toward *Argonaut*’s pressurized two-man crew capsule. "Now! Now! Now!"

Ryan scrambled through the narrow hatch, pulling the heavy titanium-composite door shut behind him. He threw the three mechanical locking dogs, securing the pressure seal. Marcus tumbled into the left-hand pilot's couch a second later, his flight suit soaked with rain and sweat.

Marcus flipped four guarded toggle switches on the overhead console:

`IGNITION_BUS_ARM: ON`  
`RCS_PURGE: COMPLETE`  
`BOOSTER_ARM: ARMED`  
`GUIDANCE_TRANSFER: QRC_PRIMARY`  

"Trajectory target uploaded," Ryan said from the right couch, his fingers flying across the touch interface. "Montgomery shape-sphere direct-injection solution locked. Boost phase: ninety-four seconds to escape velocity. Intercept perilune in sixty-eight hours."

"Hang on to your teeth, Ryan," Marcus said, grabbing the manual abort handle with both hands. "Castor 30XL solid motors don't have a throttle!"

Marcus twisted the launch key.

Below them, thirty thousand pounds of solid rocket propellant ignited in three milliseconds.

The sound was not a roar; it was a physical blow that compressed their ribcages and drove the breath from their lungs. An incandescent fountain of white-hot exhaust gases slammed into the concrete deflector pit below, blasting forty thousand cubic feet of water into instantaneous steam.

With three point eight gravities of crushing, bone-rattling acceleration, *Argonaut* shot straight up out of the test cradle. 

The spacecraft rocketed through the shattered roof of the Space Power Facility, riding a four-hundred-foot spear of flame into the howling Lake Erie rainstorm. Within six seconds, the facility, the flashing red lights of the tactical vehicles, and the flat Ohio landscape vanished beneath a blinding wall of cloud.

Twenty seconds later, the sky turned from gray to deep indigo, and then to the star-dusted, pitch-black void of space.

*Argonaut* was in flight.
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_01_The_Three_Body_Clock.md"), "w", encoding="utf-8") as f:
    f.write(ch1_full)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_02_The_Montgomery_Shape_Sphere.md"), "w", encoding="utf-8") as f:
    f.write(ch2_full)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_03_The_Expanding_Causal_Boundary.md"), "w", encoding="utf-8") as f:
    f.write(ch3_full)

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_04_The_Silicon_Horizon.md"), "w", encoding="utf-8") as f:
    f.write(ch4_full)

print("Expanded Act I (Chapters 1-4) successfully.")
