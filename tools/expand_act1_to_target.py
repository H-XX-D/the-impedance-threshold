#!/usr/bin/env python3
"""
Deep literary and technical expansion of Act I: Chapters 1-4.
Author: Todd Hendrixx
Expands Chapters 1-4 to ~2,400 words each (~9,600 words total).
"""

import os

MANUSCRIPT_DIR = "/Users/hendrixx./The_Impedance_Threshold/manuscript"

CH1_FULL = r"""# CHAPTER ONE
## The Gridless Sky
### The Appalachian Fog

The Robert C. Byrd radio telescope did not care about the human calendar.

At four o'clock on a freezing November morning in Pocahontas County, West Virginia, the one-hundred-meter paraboloid stood pale and colossal against the Allegheny mountain fog. Its two thousand and four motorized aluminum surface panels drank in the cold 1.4-gigahertz hydrogen line from deep space, tilting slightly on its massive gear ring with a low, hydraulic groan that vibrated through the frozen red-clay soil.

Inside the high-ceilinged control room of the Green Bank Observatory, Dr. Ryan Vance sat hunched over a dual-monitor workstation. A ceramic mug of black diner coffee, long grown lukewarm, rested on a stack of printed radio-astrometry log sheets. He was thirty-seven years old, with dark hair cut short against his collar, the faint squint of an optical interferometrist who had spent too many nights aligning lasers in subterranean vaults, and a stubborn quietness that his former department chair had once described as a refusal to participate in civilized academic consensus.

Across the room, the wall display traced the real-time baseline residuals of PSR J0337+1715—the millisecond pulsar spinning 365 times a second inside a hierarchical triple-star system four thousand two hundred light-years away in the constellation Taurus.

A junior telescope operator in a heavy woolen fleece looked over from the console. "Ryan, drift check is complete. The primary receiver cryostat is sitting at twelve kelvin. Baseline timing jitter is under eight picoseconds across the forty-minute integration. We have thirty seconds left on your scheduled transit window before the scheduled maintenance calibration."

"Hold the raw quadrature baseband stream," Ryan said, his voice flat and concentrated. "Do not let the correlator bin into forty-channel Stokes vectors. I need every individual voltage sample off the front-end analog-to-digital converters."

"That’s four hundred gigabytes every twenty seconds," the operator warned. "The archive system will throw an overrun flag."

"I brought my own NVMe drive array," Ryan replied, gesturing to a ruggedized Pelican case strapped to the bottom shelf of the equipment rack. Four blue status lights blinked in frantic unison. "Let it flag. I’ll clear the incident report with the site director."

For six months, Ryan had fought for these eight observing hours on the Byrd dish. He had not requested the beam time under the institutional auspices of the university’s Department of Astronomy. He had paid the commercial facility access fees out of his own pocket, draining his personal savings and maxing out three credit cards to secure an off-peak observation cycle between international pulsar-timing array runs.

His proposal had been rejected three times by the National Science Foundation review panel. The referee comments, typed in polite, devastating academic jargon, were still burned into his memory:

*The applicant proposes to interpret pulsar timing residuals in hierarchical triples not as an orbital perturbation within general relativity, but as evidence of a non-metric informational impedance limit. The theoretical framework lacks a conventional Lagrangian density, rejects spacetime as a fundamental manifold, and dismisses sixty years of dark matter cosmology without providing a scalar-tensor field alternative. Highly speculative. Unfundable in the current grant cycle.*

Ryan had not bothered to appeal. He had packed his digital storage chassis, driven eight hours through the Shenandoah Valley in his battered all-wheel-drive wagon, and checked in at the Green Bank security gate before midnight.

---

### The Pregeometry Derivation

Through the high observation windows, the massive white steel dish loomed in the mist like the skeleton of a stranded leviathan.

For a century, theoretical physics had operated on a comfortable, unchallenged assumption: that spacetime was an infinitely smooth, four-dimensional geometric fabric. Matter told spacetime how to curve; curved spacetime told matter how to move. When the observations failed to match the geometry—when galactic rotation curves refused to fall off with Keplerian precision, when the cosmic microwave background showed large-scale multipole anomalies, when the three-body gravitational interactions of dense stars showed minute phase leads—the theorists did not question the fabric. They invented invisible furniture to put on it: dark matter halos, quintessence, dark energy, sterile neutrinos, modified Newtonian gravity with adjustable empirical knobs.

Ryan opened his spiral notebook, bound in oil-stained cardboard, its pages filled with dense ink derivations.

"The fabric is an illusion," he whispered to the empty glass of the window.

At the top of the page, he wrote down the fundamental constant that standard textbooks relegated to a footnote:

$$Z_H = \frac{c^3}{G} \approx 4.037 \times 10^{35} \text{ N}$$

The Planck force. The causal impedance of free space. It had the dimensions of pure mechanical tension: kilograms meters per second squared. A force of four hundred billion billion billion billion newtons.

If spacetime were an elastic continuum, it was a continuum so impossibly stiff that an entire star cluster could barely produce a microscopic dimple in its surface. But if spacetime was not a medium at all—if spacetime was merely the statistical residue of causal information exchange—then $Z_H$ was not an elastic constant. It was the transmission channel impedance.

He turned to the Margolus-Levitin theorem of quantum computation.

In 1998, Norman Margolus and Lev Levitin had proven a rigorous mathematical bound from first principles: an ensemble of quantum states cannot evolve from one state to an orthogonal, distinguishable state in a time interval shorter than:

$$\Delta t \ge \frac{\pi \hbar}{2 E}$$

where $E$ is the average energy above the ground state.

The speed of light $c$ was not a speed limit for physical objects traversing an empty theater. The speed of light was the clock rate of causal orthogonalization. When an energy packet moved through space, it did not slide across a pre-existing coordinate grid; it computed the state transition from relation $A$ to relation $B$.

Ryan wrote down the immediate relativistic consequence: the effective index of refraction of the vacuum in the presence of a localized mass $M$:

$$n(r) = 1 + \frac{2GM}{c^2 r}$$

Under standard general relativity, this term appeared as the Shapiro time delay: the time dilation of a radio pulse passing near a massive star, interpreted as the bending of geodesics in Schwarzschild spacetime.

"It isn't geometry bending," Ryan said, tracing his pen along the formula until the paper indented. "It is impedance matching. When relational nodes exchange signals across a region of dense computational load, the channel latency rises. Mass is not something that sits inside space. Mass is the density of relational updates. The more updates you demand per unit volume, the longer each neighboring relation takes to complete its cycle."

---

### The Confrontation

At seven in the morning, the door to the Green Bank control room swung open, letting in a gust of damp mountain air and the smell of wet wool.

Dr. Richard Harrison, the senior observatory liaison and a former member of the NSF astronomy review committee, walked into the room carrying a thermos of coffee. He was in his late fifties, his silver hair neatly combed beneath a fleece-lined cap, his demeanor exuding the calm, unshakeable authority of an administrator who had spent thirty years managing multimillion-dollar radio surveys.

He stood behind Ryan’s chair for nearly two minutes, watching the raw baseband voltage streams waterfall across the monitors in cascading cyan and amber spectra.

"The site engineer called me at home, Ryan," Harrison said quietly. "He told me you were dumping raw digitizer channels at twenty gigabits per second. You're filling the buffer disks meant for the Pulsar Timing Array."

"The PTA correlator throws away seventy percent of the phase microstructure," Ryan said without turning around. "They average over ten-second sub-integrations to find standard pulse arrival times. I need the raw pulse profile down to forty nanoseconds."

"For what? To prove that Einstein was wrong?" Harrison took off his gloves and set his thermos on the corner of the desk. "Ryan, you had a brilliant career ahead of you at the department. Your interferometry work on the Naval Prototype Optical Interferometer was cited eighty times before you turned thirty. But this... this obsession with pregeometry and relational computers. You’re committing professional suicide."

"Look at the screen, Richard," Ryan said, gesturing to the monitor.

Harrison sighed, leaning in reluctantly.

On the secondary display, Ryan had plotted the pulse arrival times for PSR J0337+1715 over the last three observing seasons, subtracted against the standard TEMPO2 ephemeris.

"It’s flat," Harrison said. "The residuals are within twenty nanoseconds. Anne Archibald and the international team already published this in *Nature* back in 2018. They proved the Strong Equivalence Principle holds to one part in a hundred thousand. The pulsar’s gravitational binding energy falls at the exact same rate as the inner white dwarf. It’s the cleanest confirmation of general relativity in history."

"Look at the phase of the triple-body orbital modulation," Ryan insisted. He tapped the lower left quadrant of the graph, where a tiny, rhythmic sinusoidal ripple emerged from the noise floor at the level of 4.2 picoseconds per orbital period. "The standard model explains that ripple by adding an empirical parameter—a small third-order tidal distortion term for the outer white dwarf’s degenerate core. They treat it as an unmeasured parameter and tune the fit."

"Because white dwarfs have finite tidal deformability," Harrison countered. "That is standard stellar astrophysics."

"It's an ad-hoc patch," Ryan said, his voice rising slightly. "They tune the mass-radius relation of the outer star to make the residuals zero. But if you calculate the relational impedance using pure Margolus-Levitin causal limits—zero free parameters, zero adjustable tidal knobs—that exact 4.2-picosecond shift appears naturally. It isn't a physical deformation of the degenerate carbon-oxygen core. It is the transmission impedance between the inner binary’s center of mass and the outer companion. The channel is saturated."

Harrison shook his head slowly, a look of profound disappointment settling over his face.

"You don't have a model, Ryan. You have a philosophical grievance with differential geometry. Spacetime curvature is real. We measure it every day with GPS satellites, with lunar laser ranging, with gravitational wave interferometers. You cannot replace ninety years of mathematical physics with an engineering analogy about transmission lines."

"The GPS satellites use atomic clocks that adjust their frequency because their local causal update rate changes," Ryan replied, standing up to face him. "The lunar laser ranging stations measure a round-trip photon delay. None of them measure a manifold. We measure *events*. We measure the ticks of clocks and the arrival of photons. Every single instrument ever built by human hands measures relational differences between nodes. The manifold is a mathematical fiction we invented to interpolate between points we haven't measured."

Harrison stepped back, crossing his arms.

"Your grant is gone, Ryan. The dean confirmed it yesterday. If you don't return to the department on Monday and resume your undergraduate lectures, the university will declare your faculty line vacant."

Ryan looked at the screen, where the final pulses of PSR J0337+1715 were fading into the morning noise floor as the Byrd dish reached its automated azimuth limit.

"Then declare it vacant," Ryan said.

---

### The Clean Slate

Two hours later, the rain had turned into a steady, gray Appalachian sleet.

Ryan stood beside his wagon in the gravel parking lot of the observatory. The great white dish behind him was already tilting back toward the zenith, stowing for the storm. In the back of the car, four Pelican cases containing forty terabytes of raw baseband voltage data were strapped down beneath heavy tie-down cords, resting next to an optical alignment laser, two toolboxes, and a sleeping bag.

He pulled his collar up against the freezing wind.

For twelve years, he had lived within the warm, subsidized cloisters of academic physics: department seminars, peer review committees, tenure track evaluations, grant renewals, conference dinners where everyone agreed that dark matter would surely be detected in the next generation of liquid xenon detectors.

It was all over.

He had no salary, no institutional affiliation, no lab technicians, and no access to the university's high-performance supercomputing cluster. He had an aging wagon, three thousand dollars left in his checking account, and an unshakeable mathematical proof that the universe was not a continuous geometrical canvas, but a finite network of causal nodes bound by an absolute transmission limit.

He opened the driver’s door, brushed the wet snow from his coat, and climbed inside. The engine turned over with a rough, shuddering clatter before settling into an idle.

He put the car into gear, turned onto Route 28, and drove south into the mountains, leaving the quiet dish behind in the mist.
"""

CH2_FULL = r"""# CHAPTER TWO
## The Weight of Relations
### The Blacksburg Bench

The garage behind Ryan Vance’s rented single-story bungalow on South Main Street in Blacksburg, Virginia, smelled of machine oil, solder rosin, and damp concrete.

Two kerosene space heaters stood at opposite corners of the rectangular bay, their ceramic wicks glowing cherry-red, hissing as they fought off the November chill that seeped under the corrugated garage door. In the center of the room sat two four-by-eight-foot sheets of heavy maple plywood resting across steel sawbucks, forming a makeshift research workbench.

On the table sat a dual-socket AMD EPYC workstation motherboard, mounted directly to a bare sheet of acrylic without a computer case. Three high-speed server fans whined at twelve thousand revolutions per minute, duct-taped to copper heat pipes that dissipated the heat from one hundred and twenty-eight compute cores. Beside it, eight 3.84-terabyte NVMe solid-state drives were plugged into PCIe riser cards, their activity LEDs flashing in frantic green bursts.

This was the Relational Compute Laboratory.

Total capital expenditure: sixteen thousand two hundred dollars. Most of it borrowed from a second mortgage on his late father’s cabin in Giles County.

Ryan Vance stood over the workbench, holding a plastic mug of instant black coffee. On the center monitor, a command terminal was executing a multi-threaded Python and C++ processing script:

```
[QRC-CORE] Loading Archibald 2018 raw pulse times of arrival (TOAs)...
[QRC-CORE] Source: PSR J0337+1715 (Arecibo + GBT + Westerbork)
[QRC-CORE] Total unbinned TOAs: 26,418 points across 1,480 days.
[QRC-CORE] Transforming to Montgomery Shape-Sphere Coordinates...
```

For two weeks following his departure from Green Bank, Ryan had not left the house except to buy groceries and kerosene. He had downloaded the public archives of the Archibald 2018 *Nature* paper, extracting every single recorded pulse arrival time spanning four years of precision radio timing.

The system was unique in the known galaxy.

At its center was a millisecond pulsar, spinning on its axis every 2.73 milliseconds, orbiting a 0.20-solar-mass carbon-oxygen white dwarf every 1.63 days. That tight inner binary was in turn orbited by a second, outer white dwarf of 0.41 solar masses with an orbital period of 327 days.

In standard Newtonian mechanics, the three-body problem was notoriously insoluble in closed form, plagued by chaotic orbital resonance and sensitive dependence on initial conditions. In Einstein’s general relativity, the problem was even more vicious: each body generated a dynamic gravitational field that curved the trajectories of the other two, while the pulsar’s intense internal gravitational binding energy—comprising roughly ten percent of its total rest mass—tested the absolute limits of the Strong Equivalence Principle.

If gravity coupled differently to gravitational self-energy than to ordinary matter, the pulsar’s orbit would show a polarization vector aligned with the outer white dwarf: a Nordtvedt effect that would pull the pulsar off its Keplerian ellipse by tens of meters.

Archibald’s team had found nothing. The limit on the equivalence principle violation had been bounded to less than $2.6 \times 10^{-6}$.

"They proved Einstein was right about equivalence," Ryan murmured, scrolling through the raw residuals. "And in doing so, they blinded themselves to the relational geometry."

---

### The Montgomery Shape Sphere

To compute the three-body interaction without relying on an external, arbitrary Cartesian coordinate grid, Ryan turned to the geometric work of mathematician Richard Montgomery.

In 2002, Montgomery had revolutionized the topology of the three-body problem by projecting the nine degrees of freedom of three masses down to a two-dimensional surface known as the **Shape Sphere**.

Ryan picked up a dry-erase marker and drew a large circle on the garage's whiteboard.

"In standard mechanics," he said aloud, explaining the derivation to the empty room, "you track nine Cartesian coordinates: $(x_1, y_1, z_1)$ for the pulsar, $(x_2, y_2, z_2)$ for the inner white dwarf, and $(x_3, y_3, z_3)$ for the outer companion. You immediately subtract the center of mass, dropping you to six coordinates: the two Jacobi relative vectors $\vec{\rho}_1$ and $\vec{\rho}_2$."

He drew the two vectors: $\vec{\rho}_1$ connecting the pulsar to the inner dwarf, and $\vec{\rho}_2$ connecting their common barycenter to the outer dwarf.

"Then you divide out overall spatial rotation," he continued, drawing a set of curved arrows. "You eliminate the $SO(3)$ symmetry group. What remains is not space. What remains is the pure shape of the triangle formed by the three stars."

The shape of any triangle in the universe could be represented as a single point on the surface of a unit two-sphere:

$$S^2 = \left\{ (w_1, w_2, w_3) \in \mathbb{R}^3 : w_1^2 + w_2^2 + w_3^2 = 1 \right\}$$

- The North Pole of the sphere represented the state where the three bodies formed an equilateral triangle with counterclockwise orientation (Lagrange configuration $L_4$).
- The South Pole represented the equilateral triangle with clockwise orientation ($L_5$).
- The Equator represented all collinear configurations—where the three bodies lined up in a straight line (Euler configurations $L_1, L_2, L_3$).
- Three specific points along the equator represented binary collisions, where two of the bodies occupied the exact same relational node.

"Spacetime does not exist on the shape sphere," Ryan said, his marker squeaking against the whiteboard. "There is no background metric. There is no coordinate time $t$. There is only the continuous evolution of the shape coordinate $\mathbf{w}(s)$, parameterized by relational action $s$."

He stepped back to look at the drawing.

In classical general relativity, calculating the orbital motion of PSR J0337+1715 required solving the Post-Newtonian (PN) field equations up to 3.5PN order—a terrifying expansion involving thousands of tensor terms, retarded potential integrals, and radiating gravitational waves. On a supercomputer, simulating four years of orbit at picosecond precision took forty-eight hours of parallel computation across hundreds of nodes.

Ryan had rewritten the entire three-body equations of motion as a relational state automaton on the Montgomery shape sphere.

Instead of integrating metric perturbations across flat space, his algorithm computed the phase advance along the geodesic of the shape sphere, constrained by the Margolus-Levitin channel impedance:

$$\frac{d^2 \mathbf{w}}{ds^2} + \Gamma^i_{jk} \frac{dw^j}{ds} \frac{dw^k}{ds} = \frac{1}{Z_H} \sum_{a < b} \mathcal{F}_{ab}(\mathbf{w})$$

The right-hand side was not an external force; it was the finite rate of information exchange between the nodes.

He hit Enter on the workstation keyboard.

The 128 cores spiked to 100% utilization. The three server fans screamed, blowing a torrent of warm, dry air across the plywood table. On the monitor, a progress bar began advancing across twenty-six thousand pulse arrival times:

`[SOLVER] Integrating Relational QRC Geodesic...`  
`[SOLVER] Epoch: MJD 55900 to 57380 (1,480 Days)`  
`[SOLVER] CPU Execution Time: 4.12 seconds.`  

Ryan froze.

Four point one two seconds.

The entire four-year observational dataset—which took the university's cluster two full days to process using standard Post-Newtonian approximations—had resolved in four seconds on a sixteen-thousand-dollar desktop rig.

He leaned forward, his heart hammering against his ribs, and opened the residual analysis window.

The post-fit root-mean-square timing residual was **1.14 nanoseconds**.

That was lower than Archibald's published fit (1.30 nanoseconds). And more importantly: Ryan had used **zero empirical parameters**. He had not tuned the tidal deformability of the outer white dwarf. He had not adjusted the quadrupole moment of the inner companion.

The 4.2-picosecond phase shift that institutional cosmology had dismissed as an uninteresting tidal bulge was derived directly from the topology of the shape sphere as the system traversed near the Euler collinear boundary.

"The clock isn't in the sky," Ryan whispered, staring at the green numbers on the screen. "The clock is the network."

---

### The Skeptic’s Visit

At three o'clock that afternoon, a soft knock came at the small wooden side door of the garage.

Ryan walked over, unlocked the deadbolt, and pulled the door inward.

Standing on the stoop, his hands shoved deep into the pockets of a heavy down parka, was Dr. David Chen. David was thirty-six, an assistant professor of gravitational physics at Virginia Tech, and one of the few colleagues who had neither signed the petition to revoke Ryan’s laboratory privileges nor openly mocked his seminar presentations.

"I saw the lights on through the alley," David said, his breath pluming in the cold air. "Can I come in? It's fifteen degrees out here."

"Come in," Ryan said, stepping aside. "Watch your step around the power cables."

David walked into the garage, stamping the slush from his boots onto an old rubber mat. He looked around the space with a mixture of bewilderment and dread: the glowing kerosene heaters, the bare motherboard whirring on the plywood sheets, the whiteboard covered in differential forms and shape-sphere topologies.

"Jesus, Ryan," David said softly. "It looks like the hideout of an ideological bomb-maker."

"I am an ideological bomb-maker," Ryan said, pouring a cup of coffee from a fresh pot and handing it to him. "Have a seat on the crate."

David took the cup, blowing across the steaming surface. "The department held a faculty meeting this morning. Harrison formally submitted the paperwork to declare your position abandoned. They're reassigning your graduate students."

"I don't have any graduate students left," Ryan said. "They all transferred to solid-state optics six months ago when the NSF grant died."

"Ryan, you don't have to do this," David urged, leaning forward on the crate. "I talked to the dean. If you come back, write a standard review paper on laser metrology for LIGO, and agree to shelve this pregeometry manifesto, we can get your line restored under a joint appointment with mechanical engineering. You don't have to freeze in a garage with kerosene fumes."

Ryan didn't answer. He turned to the center monitor, clicked a window, and dragged the residual plot into full-screen view.

"What is that?" David asked, his academic curiosity momentarily overriding his concern.

"That is PSR J0337+1715. Twenty-six thousand unbinned pulse arrival times from Green Bank and Arecibo."

David squinted at the screen. "Okay. That’s the Archibald data. Everyone knows that dataset. What’s the red curve?"

"The red curve is a relational QRC solver. Zero free parameters. Zero post-Newtonian expansions. Executed on those two EPYC processors in four point one seconds."

David frowned, putting his coffee down on the sawbuck. He leaned in until his nose was six inches from the glass. He reached for the mouse, opened the parameter configuration file, and scrolled through the lines of C++ code.

"Where is the quadrupole moment?" David asked. "Where is the tidal Love number $k_2$ for the outer dwarf?"

"There isn't one," Ryan said. "I set it to zero."

"You can't set $k_2$ to zero! A degenerate carbon-oxygen white dwarf has an extended envelope. The tidal gravitational field of the inner binary distorts that envelope! If you don't include the quadrupole potential, your timing residuals should blow up by ten microseconds within sixty days!"

"They don't blow up," Ryan said calmly. "Because the quadrupole potential isn't an internal deformation of the white dwarf. It is the geometric impedance of the shape sphere. When the shape coordinates approach the collinear axis, the transmission rate between the nodes saturates at $Z_H$. What you call a tidal force is simply the latency of the relational updates."

David stared at the screen, his fingers hovering over the keyboard. For five full minutes, the garage was silent except for the roar of the server fans and the hiss of the kerosene wick.

"This is impossible," David whispered. "If this is correct... if you can reproduce the entire three-body post-Newtonian timing ephemeris without metric tensors... then spacetime curvature is an emergent artifact."

"Not an emergent artifact," Ryan corrected. "A low-frequency approximation. Like thermodynamics. When you boil water, you don't calculate the Navier-Stokes equations for the steam by assuming heat is a continuous fluid called caloric. Caloric worked for two hundred years to design steam engines, but it wasn't real. Molecules were real. In gravity, the metric tensor is caloric. The causal relations between nodes are the molecules."

David stood up abruptly, backing away from the table as if the bare motherboard were emitting lethal ionizing radiation.

"Do you know what happens if you publish this?" David's voice cracked. "Every gravitational wave template in the LIGO catalog is built on post-Newtonian expansions. Every black hole merger, every neutron star collision, every cosmological model of the expanding universe rests on the assumption that the metric is fundamental. You're telling the entire global physics community that their fifty-billion-dollar infrastructure is analyzing caloric."

"They are analyzing caloric," Ryan said.

David looked at his former colleague for a long moment. There was no triumph in Ryan Vance’s face; only the grim, exhausted certainty of a man who had looked through a telescope and seen the moons of Jupiter while the cardinals refused to look through the glass.

"They will crush you, Ryan," David said quietly, pulling his gloves back on. "They won't debate you. They will simply ignore you until your savings run out, and then you’ll be an adjunct teaching introductory physics at a community college."

"Then let them try," Ryan said.

David reached the door, paused, and looked back once more at the glowing whiteboard.

"Good luck, Ryan," he said, and closed the door behind him.
"""

CH3_FULL = r"""# CHAPTER THREE
## Tides in the Granite
### The Giles County Cut

Thirty miles west of Blacksburg, where the Appalachian Valley buckles against the folded sandstone of the Allegheny Front, the Giles County limestone mine plunged twelve hundred meters beneath the mountain.

The air inside the mine did not smell like kerosene or computers. It smelled of pulverized calcium carbonate, damp shale, and an ancient, primeval cold that had remained untouched by sunlight for three hundred million years.

At 02:00 AM on a Tuesday in late November, the commercial quarry operations had ceased. The massive diesel front-end loaders and rock crushers were parked in the staging cavern three levels above, their engines cold. Twelve hundred meters below, at the end of a six-hundred-meter dead-end drift blasted into solid Ordovician limestone, the world was utterly, terrifyingly still.

Ryan Vance sat on an overturned yellow plastic crate beside a heavy aluminum equipment rack. He was wearing steel-toed boots, heavy thermal coveralls, and a miner’s headlamp whose pale LED beam illuminated a sixteen-meter perimeter equilateral triangle resting on six massive granite surface tables.

This was the Giles County Sagnac Vault.

It had taken him four months and every remaining dollar of his savings to assemble. At each vertex of the sixteen-meter triangle sat a super-polished fused-silica mirror with an ultra-low-loss dielectric coating, mounted inside a vacuum-sealed stainless steel chamber pumped down to $10^{-7}$ torr.

A 1550-nanometer distributed feedback diode laser was injected into the cavity through an optical fiber coupler, splitting into two counter-propagating beams of coherent infrared light: one traveling clockwise around the sixteen-meter perimeter, the other counter-clockwise.

When the two beams completed their circuit and interfered on a balanced photodetector, they produced an optical beat note—a Sagnac interference fringe whose frequency was directly proportional to the rotation rate of the Earth:

$$\Delta \Phi = \frac{8 \pi A}{\lambda c} \vec{\Omega} \cdot \hat{n}$$

where $A$ was the enclosed area of the triangle ($110.85\text{ m}^2$), $\lambda$ was the laser wavelength, and $\vec{\Omega}$ was the instantaneous rotation vector of the planet.

Ryan adjusted the polarization paddles on the laser injection rack with a set of plastic alignment tweakers. His breath formed faint white clouds in the headlamp beam.

On the battery-powered oscilloscope resting on a mobile cart, the Sagnac beat frequency was locked at **348.62145 Hertz**.

---

### The Lunar Shear

In classical geophysics, an underground ring laser measured two things: the constant sidereal rotation of the Earth ($7.292 \times 10^{-5}\text{ rad/s}$), and the small, periodic perturbations caused by solid Earth tides—the gravitational pull of the Moon and the Sun flexing the crust of the planet like an elastic rubber ball.

The primary lunar tidal mode was the $O_1$ principal diurnal tide, with a period of 25.819 hours. As the Moon passed overhead, the granite bed of the mine was subjected to a rotational shear strain on the order of twenty-five nanoradians.

To conventional physics, this strain was an elastic response: the Moon’s Newtonian gravity gradient exerted a differential stress across the Earth's diameter, and the elastic rock responded according to Hooke's law and the seismic Love numbers $h_2$ and $l_2$.

Ryan looked at the strip-chart recorder logging the phase difference between the Sagnac beat note and an ultra-stable rubidium atomic frequency standard.

"The granite isn't just stretching," he whispered.

He pulled up the theoretical curve he had derived on his garage workbench three nights earlier.

If the relational quantum clock model was correct, the gravitational interaction between the Moon and the Earth was not transmitted as a classical stress tensor across a continuous solid body. The Moon and the Earth were two dense clusters of causal nodes exchanging quantum relational updates. As the Moon moved through its orbit, the transmission path through the deep mantle and crust experienced a periodic shift in relational impedance:

$$\delta \Omega_{\text{relational}} = \Omega_0 \left( \frac{GM_{\text{moon}}}{c^2 r_{\text{moon}}} \right) \cos(\omega_{O_1} t - \phi_{\text{lag}})$$

In standard Newtonian elasticity, the phase lag $\phi_{\text{lag}}$ between the Moon’s transit and the maximum strain in the rock was caused entirely by seismic anelasticity—viscous friction in the mantle, typically measured at approximately 0.2 degrees.

In relational pregeometry, the phase lag was dictated by the Margolus-Levitin rate limit across the Earth-Moon causal channel:

$$\phi_{\text{lag}} = \arctan\left( \frac{2 \pi}{\omega_{O_1} \tau_{\text{impedance}}} \right)$$

where $\tau_{\text{impedance}} \approx 1.28 \text{ seconds}$—the one-way light travel time between the Earth and the Moon.

Ryan zoomed the oscilloscope display in by a factor of ten.

The Sagnac fringe was tracing a clean, low-frequency sinusoid against the dark grid of the screen. The peak of the $O_1$ lunar tide was arriving right now.

He checked the rubidium clock time: **02:14:38 UTC**.

The astronomical transit of the Moon across the Giles County meridian had occurred at **02:14:36.7 UTC**.

The measured time delay was **1.29 seconds**.

It was not 0.2 degrees of seismic friction. It was an exact, unattenuated light-time latency in the local inertial frame of the ring laser. The bedrock of the mountain was not flexing because a distant mass was pulling on it; the bedrock was flexing because the local rate of causal information exchange was retarding as the Moon’s computational shadow passed through the crust.

"There is no action at a distance," Ryan said, his pencil scratching the observation log with trembling fingers. "And there is no curved space. The granite is an interferometer. The Earth is a node."

---

### The Call from Houston

At 02:45 AM, the harsh, electronic chirp of a satellite phone shattered the subterranean silence.

The sound echoed through the vaulted limestone cut, bouncing off the damp rock faces like a gunshot. Ryan started, nearly dropping his alignment tweakers onto the optical breadboard.

No one had this satellite number.

The phone was a ruggedized Iridium handset he kept in his emergency safety kit, paid for on a prepaid card, registered under his LLC for remote field surveys in the radio-quiet zone. Only two people outside his immediate family knew the number existed. One was David Chen, who was currently asleep in Blacksburg.

The other worked in the Mission Control Center at the Lyndon B. Johnson Space Center in Houston, Texas.

Ryan stepped away from the optical table, wiped his hands on a clean lint-free cloth, and picked up the handset. He pressed the green button and held it to his ear.

"Vance."

For three seconds, there was only the metallic hiss of the low-Earth-orbit satellite constellation bouncing voice packets across polar orbits. Then a woman’s voice came through—brittle, sharp, exhausted, and carrying the distinctive acoustic background roar of a busy flight operations floor.

"Ryan? Is this the private line?"

It was Dr. Elena Rostova.

Elena was forty-one years old, a former flight dynamics officer who had risen through the ranks of NASA's Flight Operations Directorate to become the Mission Director for Artemis-7—the first crewed mission to test the deep-space staging architecture for the proposed Lunar Gateway. She was a brilliant orbital mechanician who had completed her doctorate at Caltech on non-linear three-body trajectory optimization, and she had been Ryan’s closest friend and fiercest intellectual sparring partner when they were both postdocs at Goddard twelve years ago.

"Elena?" Ryan looked at the rock ceiling above him. "It's three in the morning. I'm twelve hundred meters underground in a limestone quarry. Why are you calling on an unlisted satellite link?"

"Because if I call on the NASA voice loop, the telemetry logs become public record under the Freedom of Information Act within twenty-four hours," Elena said, her voice dropping to a low, rapid whisper. "Ryan, listen to me. We have an anomaly on Artemis-7."

Ryan’s grip on the handset tightened. "Artemis-7 is on translunar coast. The public briefing this morning said the spacecraft had completed its translunar injection burn with zero residual delta-V."

"The burn was nominal," Elena interrupted. "The spacecraft is on its trajectory. The crew is fine—four astronauts in the Orion capsule, currently three hundred and ten thousand kilometers out, sixty hours into the coast."

"Then what's the anomaly?"

"The flight navigation computers," Elena said. There was a pause, accompanied by the muffled click of a headset switch on her end. "The primary guidance, navigation, and control system is an architecture built by prime contractors. A triple-redundant, sixty-million-dollar radiation-hardened mainframe running an Extended Kalman Filter in single-precision floating point. Over the last six hours, as the vehicle entered the three-body weak stability boundary between the Earth and the Moon, the covariance matrix began to diverge."

Ryan felt a cold shiver run down his spine that had nothing to do with the mine's temperature.

"The Normalized Innovation Squared," Ryan said quietly. "Is it failing the chi-square gate?"

"It didn't just fail the gate, Ryan," Elena said, her voice trembling with barely suppressed panic. "At 01:15 UTC, the NIS went *negative*. Minus five hundred and three."

"A variance cannot be negative," Ryan said automatically. "A covariance matrix is positive semi-definite by definition. If the NIS is negative, the filter has suffered a numerical rank collapse."

"That’s exactly what the contractor avionics team told me," Elena replied bitterly. "They said it's a floating-point truncation error in the Joseph-form covariance update. They told the Flight Director to cycle power on the navigation computer and reload the state vector from ground tracking."

"Did they?"

"We cycled Computer A at 01:45. Ground tracking at Goldstone took forty minutes to converge an orbit determination solution and uplinked it. Computer A accepted the state vector. Within twelve minutes of re-entering the autonomous star-tracker fusion loop, the NIS collapsed again. Minus four hundred and eighty. Computer B voted to safe the guidance system. Computer C is currently frozen in an infinite matrix inversion loop."

"What is the flight rule?" Ryan asked, his mind racing through the Artemis mission operational requirements.

"Flight Rule 4-Bravo," Elena whispered. "If all three navigation channels lose state confidence within thirty-six hours of perilune, autonomous trajectory correction burns are inhibited. We are thirty-two hours from perilune, Ryan. The spacecraft is currently on a free-return trajectory that has a perilune altitude of minus thirty-eight kilometers."

"Minus thirty-eight?" Ryan felt his breath catch. "That's an impact trajectory."

"It's a direct impact on the farside lunar highlands," Elena confirmed. "If we do not execute Trajectory Correction Burn Number Three at forty-eight hours into the coast, Artemis-7 hits the Moon at two point four kilometers per second. And the Flight Director will not authorize the burn without a certified state vector from the flight computers. The ground DSN stations are swamped by an X-class solar flare that erupted off the eastern limb two hours ago. The radio link is cutting out every twenty minutes."

"Elena..."

"You told me three years ago that standard Kalman filtering would fail at the three-body boundary," Elena said, her voice pleading now. "You told me that floating-point matrix inversion in curved spacetime was mathematically unstable because the background metric assumption breaks down at the Lagrange threshold. I laughed at you, Ryan. I told you that sixty years of Apollo and shuttle avionics proved the Kalman filter was infallible."

She paused, taking a ragged breath.

"You were right. The filter is dying. And I have four human beings on that ship. Do you have a working solver or don't you?"

Ryan looked across the subterranean cavern at his 16-meter Sagnac triangle, where the laser beat note was calmly, flawlessly recording the lunar transit with zero drift.

"I don't have a flight-qualified computer, Elena," Ryan said. "All I have is a four-hundred-dollar development board and an algorithm that doesn't use floating-point matrices."

"Can it run on seven watts?" Elena asked.

"It can run on five," Ryan said.

"Then pack your gear," Elena said. "I am sending a NASA transport jet to Roanoke Regional Airport. You have three hours to get out of that hole."
"""

CH4_FULL = r"""# CHAPTER FOUR
## The Seven-Watt Partition
### The Roanoke Trade Counter

After hanging up the satellite phone with Elena Rostova, Ryan Vance did not sleep.

He didn't wait for the NASA transport jet to solve his engineering problems. If the last ten years had taught him anything, it was that institutional aerospace spent six months convening safety panels to purchase a ten-thousand-dollar connector while an operational crew suffocated waiting for the paperwork to clear.

He shut down the Giles County Sagnac laser, pumped down the vacuum valves, and secured the subterranean vault. He drove his Subaru out of the limestone cut and headed northeast along Interstate 81 as a freezing mountain rain glazed the asphalt. At six in the morning, an hour before the trade counter officially opened, he was banging on the glass doors of an industrial robotics and automation distributor in an industrial park off Airport Road in Roanoke.

The counter manager, a burly man in an insulated flannel jacket holding a thermos of coffee, unlocked the security deadbolt with a scowl.

"We don't open until seven, buddy."

"I need an edge-AI computing module," Ryan said, stepping into the heated foyer. He pulled his personal credit card from his wallet. "Carrier board, passive heatsink, DC barrel connector, and an FTDI serial breakout. Specifically the **NVIDIA Jetson Orin Nano** development kit."

The manager blinked at him. "The eight-gigabyte model? That’s for warehouse AGVs and computer-vision sorting belts."

"I don't care what it’s for," Ryan said. "Do you have one in inventory?"

The manager tapped the SKU into his terminal. "One unit left on the shelf. Three hundred and ninety-nine dollars plus tax."

"Take the card," Ryan said.

Ten minutes later, Ryan walked back to his car carrying a small cardboard box no larger than a hardcover novel.

Prime aerospace contractors solved flight navigation challenges by spending sixty million dollars on triple-redundant, radiation-hardened BAE RAD750 mainframes housed in milled beryllium-copper conduction enclosures, supported by hundreds of contractor personnel tuning Kalman filter parameters from consoles in Houston.

Ryan Vance had four hundred dollars, an edge-computing board designed to guide automated forklifts through Amazon fulfillment centers, and a strict physical reality: the emergency secondary avionics bay on the Orion capsule had a dedicated auxiliary DC power tap clamped to precisely **seven point two watts**.

If his relational navigation filter could not boot, propagate, fuse optical measurements, and output a valid orbital state vector inside that seven-watt partition, four astronauts were going to vaporize against the basalt cliffs of the lunar farside.

---

### The Architecture of Collapse

Back in his Blacksburg garage, with the kerosene heaters roaring against the dawn chill, Ryan placed the green printed circuit board on an antistatic mat.

The Jetson Orin Nano was an astonishing piece of commercial silicon: a six-core ARM Cortex-A78AE CPU paired with an Ampere-architecture GPU containing 1,024 CUDA cores and 32 Tensor Cores, capable of forty trillion operations per second—provided it was given adequate cooling and twenty-five watts of power.

Ryan flipped the hardware power-selector jumper on the board to **5W Low-Power Mode**.

He clamped the DC input leads to his benchtop linear power supply, wired an oscilloscope current probe across the positive rail, and plugged a USB-serial adapter into his Linux development laptop.

The terminal flashed:

```
[TEGRA-BOOT] NVIDIA Tegra234 (Orin Nano) Initializing...
[TEGRA-BOOT] Cores enabled: 2 of 6 (Cortex-A78AE throttled to 800 MHz)
[TEGRA-BOOT] GPU Tensor Cores: Clock-gated (0 MHz)
[TEGRA-BOOT] Total Board Power Draw: 4.82 Watts.
```

"Four point eight watts," Ryan murmured, checking the digital readout on the power supply. "Two point four watts of thermal headroom for the transceiver."

He created a fresh directory: `cislunar_recovery_bench/`.

To prove beyond any shadow of a doubt why NASA's sixty-million-dollar avionics were collapsing, he spent the next two hours coding an exact replica of the Artemis-7 flight software: a textbook Extended Kalman Filter (EKF) utilizing the standard Joseph-form covariance update:

$$\mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k) \mathbf{P}_{k|k-1} (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k)^T + \mathbf{K}_k \mathbf{R}_k \mathbf{K}_k^T$$

In aerospace textbooks, the Joseph-form update was revered as the gold standard of numerical stability. By squaring the bracketed terms, it guaranteed mathematically that the diagonal elements of the error covariance matrix $\mathbf{P}$—representing the positional and velocity variances $\sigma_x^2, \sigma_y^2, \sigma_z^2$—would remain positive.

He compiled the code in standard IEEE 754 single-precision 32-bit floating-point arithmetic—the exact precision used by the radiation-hardened flight microprocessors on Orion to conserve memory and clock cycles.

He fed the filter the recorded translunar trajectory telemetry from Artemis-7 that Elena had encrypted and uploaded to his secure FTP server at 04:00 AM: seventy-two hours of inertial measurement unit (IMU) delta-velocity pulses, interleaved with optical bearing angles to lunar craters captured by the vehicle's navigation cameras.

He initiated the playback:

```
[EKF-SIM] Replaying Artemis-7 Flight Telemetry (MET 00:00 to 52:00)...
[EKF-SIM] T+12:00:00 - State variance: sigma_r = 14.2 m, sigma_v = 0.012 m/s. Nominal.
[EKF-SIM] T+24:00:00 - State variance: sigma_r = 82.6 m, sigma_v = 0.045 m/s. Nominal.
[EKF-SIM] T+36:00:00 - Weak Stability Boundary Encounter.
```

At hour 38, as the simulated spacecraft crossed the point where Earth's gravitational pull and the Moon's gravitational pull reached parity along the rotating Earth-Moon line, the terminal screen turned red:

```
[EKF-WARN] Innovation Covariance S = H*P*H^T + R condition number: 1.48e+08
[EKF-WARN] Floating-point round-off detected in matrix inversion.
[EKF-FAIL] Diagonal element P[4,4] = -1.842e-04 (Negative Variance!)
[EKF-FAIL] Normalized Innovation Squared (NIS): -503.18
[EKF-FATAL] Chi-Square Gate Failed: Covariance matrix non-positive definite.
[EKF-FATAL] Navigation State INHIBITED. Safe mode triggered.
```

Ryan took off his glasses and rubbed his eyes.

There it was.

In pure mathematics, $\mathbf{P}$ can never have a negative eigenvalue. But in 32-bit floating-point arithmetic, when two nearly equal numbers on the order of $10^5$ are subtracted to update a state variance across a non-linear gravitational saddle point, the least significant bits are truncated. The matrix loses its positive-definite character. A single negative eigenvalue appears.

The filter tries to compute the Kalman gain $\mathbf{K} = \mathbf{P} \mathbf{H}^T \mathbf{S}^{-1}$. Because $\mathbf{S}$ contains the negative variance, the innovation variance turns negative. The Normalized Innovation Squared—which should be a positive scalar drawn from a chi-square distribution—becomes a negative number: **$-503.18$**.

The computer looks at $-503.18$, realizes that a negative probability is a physical impossibility, assumes its sensors have suffered catastrophic hardware destruction, and shuts down the navigation loop to protect the ship.

"You built your filter on caloric," Ryan said to the empty garage. "You assumed space was smooth, so you inverted a metric matrix. And the computer died on a rounding error."

---

### The Integer Guidance Core: SRIF and FixedQP

To replace the failing EKF, Ryan did not try to fix the floating-point math. He threw floating-point math into the trash.

If a flight computer has to operate on seven watts in a high-radiation environment where single-event upsets flip bits in memory registers, floating-point arithmetic is a lethal liability. An exponent bit flip turns a 1.0-meter correction into a ten-billion-kilometer explosion.

Ryan implemented a two-stage relational guidance engine designed entirely around **deterministic integer arithmetic and square-root factorizations**.

#### Stage 1: The Square Root Information Filter (SRIF)

Instead of propagating and updating the covariance matrix $\mathbf{P}$, which had the dimensions of state squared, Ryan used the square root of the information matrix:

$$\mathbf{P}^{-1} = \mathbf{R}^T \mathbf{R}$$

where $\mathbf{R}$ was an upper-triangular matrix.

To update the state with new optical measurements, the algorithm did not perform matrix inversion or Kalman gain division. It constructed a single composite data array combining the prior information square root $\mathbf{R}$, the measurement mapping matrix $\mathbf{H}$, and the measurement residual $\mathbf{z}$:

$$\mathbf{T} = \begin{bmatrix} \mathbf{R} & \mathbf{b} \\ \mathbf{H} & \mathbf{z} \end{bmatrix}$$

Then, Ryan applied a sequence of **Householder orthogonal transformations**—pure geometric reflections that rotated the composite matrix into upper-triangular form:

$$\mathbf{Q} \mathbf{T} = \begin{bmatrix} \mathbf{R}_{\text{new}} & \mathbf{b}_{\text{new}} \\ \mathbf{0} & \mathbf{e} \end{bmatrix}$$

Because $\mathbf{Q}$ was an orthogonal matrix ($\mathbf{Q}^T \mathbf{Q} = \mathbf{I}$), the condition number of the problem was halved. Round-off errors could not produce negative eigenvalues because the covariance matrix was never computed; only its square root $\mathbf{R}_{\text{new}}$ existed.

Even if single-precision floating-point arithmetic were used, the SRIF was mathematically immune to negative-NIS collapse.

#### Stage 2: The FixedQP Integer Guidance Engine

For trajectory optimization and thruster burn execution, Ryan bypassed floating-point quadratic programming altogether.

He wrote **FixedQP**: a 256-iteration active-set quadratic programming solver running entirely in **32-bit fixed-point integer arithmetic** (`int32_t`), with a fixed binary scale factor of $2^{16}$ (Q16.16 format):

- Upper 16 bits: integer part ($-32,768$ to $+32,767$ meters or meters per second).
- Lower 16 bits: fractional part (precision of $1/65,536 \approx 15.25\ \mu\text{m}$).

Every multiplication was executed via a single assembly-level integer multiply-accumulate (`SMULL` on ARM), followed by a deterministic bit-shift:

```cpp
inline int32_t q16_mul(int32_t a, int32_t b) {
    int64_t prod = (int64_t)a * (int64_t)b;
    return (int32_t)(prod >> 16);
}
```

Zero division by zero. Zero NaN propagation. Zero floating-point denormalization stalls.

He compiled the entire package into a bare-metal Linux binary: `argonaut_os_core.elf`.

Total executable binary size: **482 kilobytes**.

He executed the test on the Jetson Orin Nano:

```
[CISLUNAR-OS] Loading FixedQP 32-bit Integer Guidance Core...
[CISLUNAR-OS] Initializing Householder SRIF Information Filter...
[CISLUNAR-OS] Replaying Artemis-7 Telemetry across WSB...
[CISLUNAR-OS] T+36:00:00 - Weak Stability Boundary Encounter.
[CISLUNAR-OS] T+38:00:00 - Householder QR Orthogonalization: COMPLETE.
[CISLUNAR-OS] Information Matrix Condition Number: 1.21e+02 (ROCK SOLID)
[CISLUNAR-OS] State Error: delta_r = 1.18 m, delta_v = 0.0004 m/s.
[CISLUNAR-OS] FixedQP Trajectory Optimization: Converged in 14 iterations (0.82 ms).
[CISLUNAR-OS] Execution Power Draw: 5.14 Watts. PASS.
```

Ryan leaned back in his chair. A slow smile spread across his face for the first time in six months.

The four-hundred-dollar forklift brain had eaten the sixty-million-dollar aerospace anomaly for breakfast, in less than a millisecond, drawing five point one watts.

---

### The Plum Brook Chamber Test

At 08:30 AM, a black government sedan with US Government plates pulled up to the curb of the Blacksburg bungalow. Two men in dark suits stepped out, accompanied by an Air Force captain in flight fatigues.

"Dr. Vance?" the captain asked, saluting crisply. "Captain Miller, Air Mobility Command. Dr. Rostova ordered us to transport you and your hardware to NASA Plum Brook Station immediately."

"Plum Brook?" Ryan picked up his Pelican case containing the Jetson board, a backup unit, two power cables, and a ruggedized terminal laptop. "Why Plum Brook? I thought we were going to Johnson in Houston."

"The Flight Director won't touch uncertified commercial hardware in Mission Control," Miller explained as they loaded the gear into the trunk. "If you want this board anywhere near Artemis-7, you have to prove it can survive flight conditions under the Space Simulation Vacuum Facility at the Neil Armstrong Test Facility in Ohio. Dr. Rostova has booked Chamber B."

Three hours later, a C-21 Learjet touched down at Sandusky, Ohio.

NASA Plum Brook’s Space Power Facility housed the world’s largest thermal vacuum chamber: a cavernous aluminum-ribbed silo capable of simulating the absolute vacuum and cryogenic freeze of deep space.

In the staging bay of Chamber B, a team of NASA avionics qualification technicians stood around a two-meter cylindrical vacuum bell jar.

Elena Rostova was there, wearing a NASA flight jacket over a wrinkled blue blouse, dark circles under her eyes, her smartphone glued to her ear. When she saw Ryan walk through the airlock door, she hung up the phone and walked straight toward him.

"You look terrible, Ryan," she said, her voice hoarse.

"You look worse," Ryan said. "How is Artemis?"

"TCM-3 is scheduled in twenty-one hours," Elena said, her voice dropping. "Computer A failed again twenty minutes ago. Computer B is rejecting ground tracking updates because Canberra DSN lost lock during a solar coronal mass ejection. If we don't have an onboard recovery package certified by eighteen hundred hours today, Flight Director Hayes will call the mission lost and order the crew to prepare for farside impact."

She looked at the Pelican case in Ryan's hand. "Is that it?"

"That's it," Ryan said. He popped the latches and opened the lid.

The NASA qualification lead, a gray-haired engineer named Kowalski with thirty years of shuttle and space station testing experience, looked into the case and let out a dry, incredulous snort.

"An NVIDIA Jetson board?" Kowalski looked at Elena, then at Ryan. "Are you out of your mind? That’s commercial plastic and lead-free solder. It isn't rad-hard. It isn't conformal-coated. The BGA solder balls will crack under thermal shock, and the first solar proton that hits the silicon will latch up the entire memory bus."

"The board doesn't need to survive for ten years on a Mars rover, Mr. Kowalski," Ryan said evenly. "It needs to survive for twenty-one hours. And the code running on it doesn't use floating-point arithmetic. If a proton flips a bit in the data array, the Householder QR transformation projects the error onto the orthogonal residual vector $\mathbf{e}$ and discards it in the next cycle. Put it in the chamber."

Kowalski stared at him for five tense seconds, then waved his arm at the technicians. "Mount it to the cold plate. Wire the auxiliary seven-watt DC bus and pump the chamber down to ten to the minus six."

The technicians bolted the Jetson board to an aluminum bracket inside the bell jar, attached thermocouple probes to the processor heatsink, wired the 5-volt power leads, and sealed the heavy steel dome.

The vacuum pumps began their deafening mechanical whine: *whirrrrr-thump-thump-thump*.

Inside the bell jar, the pressure plummeted through the pascals: $10^1$, $10^{-1}$, $10^{-3}$, $10^{-6}$ torr. Liquid nitrogen was pumped through the thermal shrouds, dropping the chamber wall temperature to minus one hundred and fifty degrees Celsius.

On the test bench monitor, the Jetson Orin Nano booted in the vacuum:

```
[VAC-TEST] Chamber Pressure: 4.2e-06 Torr.
[VAC-TEST] Cold Plate Temp: -142 deg C.
[VAC-TEST] Core Temp: +18 deg C (Self-heating under passive radiation).
[VAC-TEST] Input Voltage: 5.02 V | Current: 1.04 A | Power: 5.22 Watts.
[VAC-TEST] Executing 10,000 Monte Carlo Cislunar Trajectory Recoveries...
```

For two agonizing hours, the qualification team stood around the telemetry screen in dead silence.

Outside in the Ohio afternoon, the winter wind rattled the corrugated steel walls of the test facility. Inside the console room, the green progress bar ticked relentlessly forward:

```
[VAC-TEST] 10,000 / 10,000 Monte Carlo Runs Complete.
[VAC-TEST] Guidance Solutions Converged: 10,000 (100.00%)
[VAC-TEST] Numerical Exceptions / NaN Flags: ZERO.
[VAC-TEST] Negative NIS Occurrences: ZERO.
[VAC-TEST] Maximum Trajectory Discrepancy: 1.42 Meters at Perilune.
[VAC-TEST] Status: QUALIFIED FOR FLIGHT EVALUATION.
```

Kowalski slowly took off his safety glasses, looked at the numbers on the screen, and then looked at Ryan Vance.

"I’ll be damned," Kowalski muttered.

Elena grabbed Ryan’s arm, her fingers digging through his heavy woolen sleeve.

"We have our flight package," Elena said, her eyes burning with fierce determination. "Now we have to convince Hayes to beam it to the ship."
"""

print("Writing expanded Act I chapters...")
for fname, content in [
    ("Chapter_01_The_Gridless_Sky.md", CH1_FULL),
    ("Chapter_02_The_Weight_of_Relations.md", CH2_FULL),
    ("Chapter_03_Tides_in_the_Granite.md", CH3_FULL),
    ("Chapter_04_The_Seven_Watt_Partition.md", CH4_FULL),
]:
    p = os.path.join(MANUSCRIPT_DIR, fname)
    with open(p, "w") as f:
        f.write(content.strip() + "\n")
    words = len(content.split())
    print(f"Updated {fname}: {words} words")
