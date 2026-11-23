import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

ch2_content = """# CHAPTER TWO
## The Montgomery Shape Sphere
### Covariance Collapse in Houston

The air inside Mission Control at Johnson Space Center tasted of ozone, stale coffee, and collective panic.

Across the front projection wall, the three-body trajectory plot of Artemis-7—the crewed deep-space transport *Prometheus* carrying Elena Rostova, Marcus Thorne, and lunar geologist Chen Wei—was painted in screaming amber. A dotted red vector extended from the vehicle's current position sixty thousand kilometers above the Moon, plunging straight into the basalt wastes of the South Pole-Aitken basin.

"Flight, we have a complete innovation rejection on primary GNC," called the Guidance Officer, his voice cracking beneath the headset. "Star tracker two took a heavy solar proton hit during the coronal burst. When the optical fix came in, the GEONS Extended Kalman Filter computed a negative Normalized Innovation Squared. The covariance matrix lost positive-definiteness. The filter rank collapsed!"

Flight Director Warren Hastings slammed his palm against the mahogany console. "What do you mean, negative NIS? A sum of squares cannot be negative! That is high school linear algebra!"

"In floating-point arithmetic on radiation-hardened RAD750 chips, it can," the Guidance Officer shouted back, pulling up the raw memory dump. "GEONS computes the innovation covariance $S = H P H^T + R$ by direct matrix subtraction. After thirty-six hours of high-gain tracking, the prior covariance $P$ became infinitely overconfident. When the flare shifted the optical limb, the subtraction produced a negative eigenvalue! The filter thought its variance was less than zero. It interpreted reality as a mathematical impossibility, panicked, and threw a critical software fault!"

"And the fail-safe?" Hastings demanded.

"The fail-safe worked exactly as the contractor designed it, Flight," the Systems Officer reported grimly. "The main computer locked out all thruster commands and dropped the ship into `PROTECTIVE_SCREENED_COAST`. The propellant valves are mechanically isolated. The autopilot refuses to fire because it believes firing will corrupt the navigation state further. It's a coast-lock bug!"

On the mission audio loop, Elena Rostova's voice cut through the chaos from four hundred thousand kilometers away:

*"Houston, this is Rostova. I am looking through the forward viewport right now. The Moon is filling ninety degrees of the sky. We have tried the manual GNC override three times. The flight software rejects the joystick input because the safety interlock requires a converged navigation state before opening the bipropellant valves! We are locked out of our own thrusters!"*

"Elena, this is Flight," Hastings said, leaning into his microphone, forcing his voice into an authoritative calm that fooled no one in the room. "We are preparing an emergency ground-commanded hydrazine blowdown. We will fire the auxiliary RCS thrusters via the backup engineering umbilical to push your perilune outward."

*"Negative, Houston!"* Elena fired back instantly. *"If you blow the RCS now without closed-loop attitude stabilization, the ship will tumble uncontrollably in the gravity gradient! You will burn through forty percent of our reserve, and we will miss the lunar capture corridor entirely! We won't crash into the Moon—we'll fly into a dead, hyperbolic orbit into interplanetary space with three days of oxygen!"*

"It's the only procedure authorized in the flight rules, Elena!" Hastings shouted.

*"Then your flight rules are an execution order, Warren!"* Elena snapped. *"Put Ryan Vance on this loop right now!"*

Hastings stiffened, his face reddening. "Dr. Vance is a civilian contractor currently under administrative suspension. His unverified relational navigation theories have not been vetted by NASA Engineering."

*"I don't give a damn about your vetting, Warren!"* Elena's voice was ice. *"Vance warned you three years ago that the Cartesian Kalman filter would suffer covariance starvation in cislunar space! He told you that space is not an empty coordinate box where you can invert matrices with impunity! He built the square-root information filter that prevents negative NIS by construction! Put him on the loop, or I will break the seal on the primary avionics breaker with a fire axe!"*

Before Hastings could respond, a secure audio channel bridged directly into the flight director's console. 

"Warren," Ryan Vance's voice echoed through the speaker, crisp, measured, and completely devoid of fear. "I am looking at your telemetry stream right now. Your Cartesian filter failed because you are trying to describe a three-body chaotic Hamiltonian with two-body osculating ellipses. You are measuring positions against an imaginary origin that doesn't exist."

"Vance," Hastings growled. "You have no operational authority here."

"I have the math that will keep your three astronauts from becoming an aluminum smudge on the far side of the Moon," Ryan replied. "Listen to me carefully. *Prometheus* is caught in the Jacobi manifold between the Earth and the Moon. If you use Montgomery's shape-sphere coordinates, the three-body problem decouples into size and shape:

$$u = \\sqrt{\\frac{m_1 m_2}{m_1 + m_2}}(r_2 - r_1), \\quad v = \\sqrt{\\frac{m_3(m_1 + m_2)}{m_1 + m_2 + m_3}}\\left(r_3 - \\frac{m_1 r_1 + m_2 r_2}{m_1 + m_2}\\right)$$

"On the shape sphere $S^2$," Ryan said, his voice carrying an undeniable commanding clarity, "the collision manifold isn't an infinite plane; it's a closed meridian! You don't need a massive delta-V to escape it. You need a ninety-meter-per-second burn executed at exactly twelve degrees off the Earth-Moon invariant normal! But your ship computer won't let Elena fire that burn because its software is frozen in coast-lock!"

"Then what the hell do you propose we do, Vance?" Hastings asked, the defiance draining from his posture as he stared at the collision clock. "We can't reflash the flight computer from Houston. The solar flare is corrupting the S-band uplink. The packet loss is sixty percent!"

"You can't reflash it from Earth," Ryan said. "Which is why I am bringing the flight core to her myself."
"""

ch3_content = """# CHAPTER THREE
## The Expanding Causal Boundary
### The Sagnac Severance

The sound of heavy tires grinding across the gravel road outside the Giles County cavern was the only warning they got.

Sato was at the nitrogen manifold, disconnecting the primary cooling line to the Sagnac ring, when the headlights flashed through the corrugated metal doors of the surface shed. Three black Chevy Suburbans, their grilles caked with Appalachian red mud, pulled up to the perimeter gate.

"Ryan," Sato whispered, dropping the spanner. "Company. And they didn't bring clipboards."

Ryan didn't flinch. He had known this moment was coming the second he tapped into the NASA telemetry feed. When billions of dollars of legacy aerospace contracts depend on selling trillion-dollar satellite constellations based on classical Cartesian grids, the man who proves space is a relational impedance network isn't hailed as a visionary. He is treated as an existential threat to the defense budget.

On his workbench sat the heart of the QRC project: a twenty-centimeter cube of gold-plated aluminum containing two Kintex UltraScale+ FPGAs and an isolated rubidium atomic reference. It was the complete, flight-hardened prototype of the **Square-Root Information Filter (SRIF)** and the **Receding-Horizon Relational Guidance Core**.

"They have federal marshals with them," Sato said, peering through the slit in the reinforced steel blast door. "And two suits from Axiom-Lockheed. They're carrying Pelican cases. They're here to seize the hardware under an ITAR export control order."

"ITAR," Ryan scoffed with bitter contempt, unplugging the primary fiber-optic umbilical. "They classify the geometry of the universe because their own guidance systems can't solve three bodies without crashing."

He slipped the gold-plated cube into a padded carbon-fiber transport case and latched the hermetic seals. 

A sharp, metallic hammering rattled the outer security door. Through the speaker, a voice amplified by a megaphone boomed across the limestone clearing:

*"Dr. Ryan Vance! This is the United States Marshals Service! We have a federal warrant for the immediate impoundment of all cryptographic, guidance, and algorithmic assets associated with Project Relational Causality! Open the doors immediately and step away from the terminals!"*

"Sato," Ryan said calmly. "The thermite charges on the data servers. Fire them."

Sato looked at him, his dark eyes wide. "Ryan, that's ten years of pulsar baseline data—"

"The raw data is already mirrored on the decentralized relay at Green Bank," Ryan said. "What's in these servers is the proprietary military code Axiom wants to patent and lock in a vault for thirty years while astronauts die in cislunar space. Burn it."

Sato didn't hesitate. He pulled the manual safety pins on the two canisters mounted beneath the central server rack and struck the primers.

A blinding, violet-white glare erupted inside the server cabinet. The hiss of burning magnesium and iron oxide was deafening as three thousand degrees of molten slag melted through the hard drives, motherboards, and memory banks, fusing the silicon into a puddle of boiling glass. The fire suppression system roared to life, filling the cavern with dense clouds of white nitrogen fog.

*"Breach the door!"* the megaphone screamed outside.

A loud concussive boom shook the limestone walls as a hydraulic ram buckled the outer security hinges.

"The adit," Ryan said, slinging the carbon-fiber case over his shoulder.

At the rear of the cavern, half-concealed behind a stack of empty liquid helium dewars, lay a low, unmapped drainage adit carved by coal miners eighty years before. It sloped downward through three hundred yards of solid dolomite before opening into an overgrown ravine on the far side of the ridge.

"Go, Ryan," Sato said, grabbing a fire extinguisher and racking the slide on a heavy industrial bolt-gun. "I'll hold the marshals at the blast door. Tell them the smoke is toxic."

"Sato—"

"Elena is eighty hours from impact, Ryan," Sato said, shoving him toward the tunnel opening. "Get to Ohio. Marcus is waiting at Plum Brook."

Ryan locked eyes with his friend for a single, silent second. He gripped the case, ducked beneath the hanging stalactites, and plunged into the pitch-black throat of the drainage tunnel.

Behind him, the heavy blast doors gave way with a screech of tearing steel. Shouts, flashbang grenades, and the hiss of thermite smoke echoed down the stone passage, swallowed by sixty feet of Appalachian limestone.

Thirty minutes later, Ryan emerged from the mountain into the drenched darkness of a Tennessee cedar forest. Cold rain beat against his face. 

Waiting on the logging road, its engine idling silently with dimmed headlights, was Marcus Thorne’s unmarked diesel flatbed truck.

Ryan threw the case into the passenger seat and vaulted inside. Marcus slammed the transmission into gear, spinning tires on wet gravel as they launched north toward Lake Erie.
"""

ch4_content = """# CHAPTER FOUR
## The Silicon Horizon
### The Plum Brook Heist

The Space Power Facility at NASA’s Neil A. Armstrong Test Facility in Sandusky, Ohio, was the only place on Earth where a full-sized interplanetary spacecraft could touch the vacuum of deep space without leaving the ground.

Inside the monolithic aluminum dome—one hundred and twenty-two feet high, with a volume of eight hundred thousand cubic feet—the air had been evacuated down to ten to the minus six torr. The cryogenic cold walls, chilled with liquid nitrogen to eighty Kelvin, sucked the thermal energy out of anything placed at the chamber floor.

Suspended in the center of that vast, echoing cathedral of vacuum was *Argonaut*.

She was not a government flagship. She was a prototype: a lean, predatory wedge of carbon-composite trusswork, twin 15-kilowatt Hall-effect electric thrusters, high-pressure cold-gas reaction wheels, and a central titanium structural cylinder engineered to withstand twenty gravities of translunar injection shock. She had been built under an unclassified DARPA technology demonstrator grant to test autonomous orbital debris interception.

Now, she was the only fueled spacecraft on Earth capable of reaching the Moon in under sixty hours.

"Security has locked down the main gate," Marcus Thorne said, his breath fogging his visor as he worked beneath the unpressurized service scaffolding of the Plum Brook high bay. "Hastings figured out we were coming to Plum Brook twenty minutes ago. The State Highway Patrol is setting up roadblocks along Route 250."

Ryan Vance stood on the work platform sixty feet above the concrete floor, holding the gold-plated QRC guidance core. 

The primary avionics bay on *Argonaut*’s upper truss was open, its wiring harnesses exposed like the nerves of a dissected machine. Classical aerospace engineering called for redundant mil-spec 1553 data buses, quadruple-voted voting computers, and hundreds of pounds of shielding.

Ryan ripped out the primary Cartesian guidance computer—a three-hundred-thousand-dollar RAD750 unit—and dropped it onto the rubber floor mat with a hollow thud.

"What are you doing?" Marcus hissed, staring in disbelief. "You just yanked the primary bus controller!"

"The primary bus controller is programmed with the same EKF code that just killed *Prometheus*," Ryan said, sliding the QRC square-root processor into the mounting rack. He connected the dual high-speed LVDS serial links directly to the thruster driver relays. "We aren't running an EKF. We are running the square-root information filter directly on the raw state vector."

He plugged his ruggedized field terminal into the test port. Lines of green C++ code streamed down the screen:

```
[QRC-INIT]: SQUARE-ROOT MEASUREMENT GATE ENGAGED
[JACOBI-STATE]: 18-STATE RELATIONAL VECTOR CONVERGED
[COVARIANCE-CHECK]: S = r^T * r (POSITIVE DEFINITE BY QR DECOMPOSITION)
[NEGATIVE-NIS]: IMPOSSIBLE BY MATHEMATICAL CONSTRUCTION
[REVERT-OVERRIDE]: ACTIVE // ALL MANUAL CHANNELS OPEN
```

"Look at that, Marcus," Ryan said, pointing at the display. "Because the innovation covariance is factored as $S = r^T r$ using QR decomposition, the eigenvalues of $S$ are the squares of the diagonal elements of $r$. It cannot go negative. A negative NIS is mathematically impossible. Even if a solar flare blindingly whiteouts the star trackers, the filter simply marks the innovation as suspect, drops the measurement weight, and maintains tracking on the relational pulsar prior."

Below them, the heavy blast doors of the high bay shuddered.

The facility emergency alarms began to wail—a rhythmic, deafening siren accompanied by flashing amber strobe lights.

```
SECURITY ALERT // UNAUTHORIZED FACILITY BREACH
HIGH BAY 1 LOCKDOWN INITIATED
STAND CLEAR OF CRYOGENIC VENT LINES
```

"They're inside the building," Marcus said, racking the manual valve on the liquid oxygen transfer line. "Ryan, we don't have a launch window! We don't have orbital clearance from Space Command! If we ignite the solid kick-motor inside this facility, the blast overpressure will blow the roof off the chamber!"

"The chamber is rated for nuclear thermal rocket testing, Marcus," Ryan said, sealing the avionics hatch and tightening the four titanium dog-latches. "The roof will hold. And we don't need a launch window from Space Command. The Earth-Moon three-body problem doesn't give a damn about air traffic control."

Ryan climbed down the scaffolding, pulled the emergency umbilical disconnect, and threw the master breakers for the hangar's overhead crane.

With a deep, hydraulic groan that resonated through the bedrock of Ohio, the ceiling of the Space Power Facility began to split open. The massive, concrete crane doors—weighing four hundred tons each—rolled back, revealing the freezing, star-filled November sky.

Ryan climbed into the pressurized two-man command capsule mounted atop *Argonaut*’s keel, strapping himself into the five-point Nomex harness. He reached across the console and hit the master arm switch for the solid-propellant translunar stage.

On the radio loop, Elena Rostova's telemetry beacon from the lunar farside pulsed across his headphones—a faint, dying heartbeat sixty thousand kilometers out in the black.

"Elena," Ryan spoke into his microphone, his hands steady on the ignition abort lever. "Hold on to your bulkheads. We are inbound."

He punched the master ignition button.

A column of blinding, incandescent orange flame erupted from the floor of the Plum Brook chamber, shaking the shores of Lake Erie with five hundred thousand pounds of thrust as *Argonaut* tore into the night sky.
"""

with open(os.path.join(MANUSCRIPT_DIR, "Chapter_02_The_Montgomery_Shape_Sphere.md"), "w", encoding="utf-8") as f:
    f.write(ch2_content)
with open(os.path.join(MANUSCRIPT_DIR, "Chapter_03_The_Expanding_Causal_Boundary.md"), "w", encoding="utf-8") as f:
    f.write(ch3_content)
with open(os.path.join(MANUSCRIPT_DIR, "Chapter_04_The_Silicon_Horizon.md"), "w", encoding="utf-8") as f:
    f.write(ch4_content)

print("Wrote Chapters 2, 3, 4 successfully.")
