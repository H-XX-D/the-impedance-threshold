# CHAPTER FIVE
## Flare State
### Translunar Coast & The Blue Marble

The translunar injection burn had been textbook.

At 22:14:08 UTC on November 8, 2026, the four RL10-B-2 cryogenic engines of the Space Launch System Exploration Upper Stage had ignited over the southern Indian Ocean, firing for eight minutes and twenty-two seconds through the orbital darkness. The burn had delivered 3,048.6 meters per second of forward delta-V, accelerating the three-hundred-ton stack through the translunar injection corridor and flinging the Orion spacecraft into the deep cislunar void.

Inside the pressurized command module of Orion, Commander Sarah Ross floated above the forward pilot's station, watching the Earth retreat through the three-pane fused-silica viewports.

The blue marble of the home world was visibly shrinking. Its curved rim was etched with the paper-thin cyan haze of the atmosphere, receding into the velvet blackness by three thousand meters every second. At forty-two years old, Sarah had logged over two thousand hours in carrier-capable strike fighters as a naval test pilot before selection to the astronaut corps. She had the cool, resting pulse of someone who had survived engine flameouts and night deck landings in high sea states, but staring into the cislunar dark, she felt the ancient, biological dread of leaving the protective womb of the home planet.

Her three children were asleep in their beds in Pensacola, Florida. Her husband, an aeronautical engineer at Eglin Air Force Base, had squeezed her hand through the quarantine glass in Houston three days ago and told her not to look at the numbers. But Sarah was an engineer; she always looked at the numbers.

Beside her in the center couch, Pilot David Miller verified the primary flight displays. David was thirty-six, an Air Force colonel with a doctoral degree in astrodynamics from MIT. His wife was seven months pregnant with their first daughter back in Corpus Christi.

"Stage separation confirmed nominal," Miller said, his voice level and methodical. "EUS disposal burn confirmed: the spent stage has entered a heliocentric disposal trajectory. Solar array wings deployed and sun-tracking. All four wings generating twelve point four kilowatts. Reaction control system pressurized to two hundred and eighty bar of gaseous helium. We are coasting."

In the lower equipment bay beneath the flight deck, Mission Specialists Robert Thorne and Dr. Lin Liu were stowing the launch umbilical lines and preparing the autonomous biological radiation experiment racks. Lin Liu, an astrophysicist and cellular biophysicist who had spent five years studying cellular DNA repair mechanisms in low-Earth orbit, was securing the passive thermoluminescent dosimeter badges along the cabin bulkheads.

"Cabin atmosphere is nominal," Liu called up through the access hatch. "Twenty-one percent oxygen, seventy-nine percent nitrogen at ten point two psi. Carbon dioxide scrubbers sitting at zero point two millimeters of mercury. The bio-racks are locked down."

For thirty-six hours, the flight was what NASA flight controllers loved most: completely boring.

The spacecraft was drifting outward along a coasting ellipse toward the Moon, three hundred and ten thousand kilometers from Earth, moving at slightly under one kilometer per second relative to the Earth-Moon barycenter. The cabin hummed with the constant, reassuring drone of cabin avionics fans, the rhythmic clicking of the carbon-dioxide scrubbers, and the low hiss of the air recirculators.

Then, at 14:22 UTC on November 10, the sun decided to remind four human beings that space was not a quiet void.

---

### The Coronal Eruption

Ninety-three million miles away, an immense magnetic knot in active region AR3842—a sunspot complex four times the diameter of Earth—snapped.

The reconnection event released the equivalent of one billion one-megaton hydrogen bombs in less than forty seconds. It was an **X8.4 solar flare**, one of the most violent stellar eruptions recorded in the twenty-first century.

A blinding flash of extreme ultraviolet and soft X-ray radiation washed over the inner solar system at the speed of light, ionizing Earth’s upper ionosphere and causing immediate high-frequency radio blackouts across Europe and North America.

Behind the light came the monster: a coronal mass ejection consisting of billions of tons of magnetized solar plasma, accompanied by a relativistic shockwave that accelerated protons to eighty percent of the speed of light.

Inside the Orion cockpit, the radiation dosimeters did not register a gradual rise. They screamed.

A high-pitched acoustic alarm cut through the ambient avionics hum: *BEEP-BEEP-BEEP-BEEP*.

The primary caution-and-warning matrix on Ross’s central console lit up in bright amber:

```
[CAUTION] SPE EVENT DETECTED: GOES-19 PROTON FLUX > 10,000 PFU
[CAUTION] ONBOARD DOSIMETER RATE: 14.8 RAD/HR AND CLIMBING
[WARNING] FLIGHT RULE 2-DELTA: CREW RETREAT TO SHELTER REQUIRED
```

"Solar flare," Ross said, her voice dropping into the flat, clipped cadence of a combat test pilot. "Miller, Thorne, Liu—abort scheduled tasks. Helmets on, grab your emergency water jackets. We are moving into the storm shelter."

The crew didn't ask questions. They knew the numbers.

At fourteen rads per hour of unshielded flux, a human being receives a lethal dose of radiation in less than thirty hours. Acute radiation sickness—nausea, intestinal hemorrhage, bone marrow destruction—would begin within six hours.

The four astronauts scrambled down from their flight couches into the central floor well between the equipment lockers. They pulled dense Nomex-and-polyethylene radiation blankets from the stowage bays, stacking the spacecraft’s twenty-liter contingency water containers around them to create a makeshift hydrogen-rich radiation bunker.

They sealed the thermal curtain above their heads, wedging themselves shoulder-to-shoulder in the dark, breathing through their oxygen masks, listening to the metallic creak of the hull as the high-energy proton storm pounded the outer spacecraft skin.

In the dark of the shelter, strange optical phosphenes flickered across their vision: tiny, brilliant flashes of blue-white light caused by relativistic protons slicing through the vitreous humor of their eyeballs and striking their retinas directly.

"Taste that?" Thorne whispered through his comm mic.

"Metallic," Lin Liu said, her teeth clenched. "Like sucking on a copper penny. That’s the ozone and free radicals forming in your saliva from secondary ionization."

---

### The Blinding of the Eyes

Outside the pressurized hull, Orion’s primary sensory systems were fighting for their lives.

To navigate autonomously across cislunar space, the spacecraft relied on two primary optical systems: two high-resolution Star Trackers mounted on the service module, and an Optical Navigation (OpNav) camera mounted on the command module forward bulkhead.

The star trackers were designed to match patterns of distant stars against an onboard catalog of fifteen thousand astronomical coordinates, determining the spacecraft’s three-axis attitude to within two arcseconds.

As the relativistic solar proton storm struck the star tracker CCD sensor chips, the high-energy particles slammed through the protective borosilicate glass windows. Each proton created a miniature shower of secondary ionization electrons in the silicon, producing bright, spurious pixel clusters known as Cherenkov transients.

On the avionics bus, the star tracker software attempted to process the image:

```
[STR-A] Frame 4182: Detected 1,842 bright centroids.
[STR-A] Star Pattern Match: FAILED (Catalog limit: 60 stars).
[STR-A] Noise Rejection Gate: OVERRUN. False Centroids: 98.4%.
[STR-A] Attitude Lock: LOST. Entering Coast-Attitude Mode.
[STR-B] Frame 4182: Sensor Saturated. Latch-up Protection Triggered.
```

Within ninety seconds of the proton front's arrival, both primary star trackers were completely blind.

At the same time, the solar radio burst—a ferocious, broadband blast of synchrotron radio noise generated by relativistic electrons spiraling through the sun's magnetic field—swept across the Earth-Moon axis.

On the Earth's surface, the 70-meter parabolic dish of Deep Space Station 43 at the Canberra Deep Space Communication Complex in Australia was pointed at Artemis-7.

At 14:26 UTC, the signal-to-noise ratio on the spacecraft’s high-gain S-band down-link dropped off a cliff. The carrier lock dropped from plus thirty-two decibels down to minus four decibels, vanishing beneath the deafening solar hiss.

The station operator at Canberra hit his voice switch:

"Houston, Canberra DSN. We have lost RF carrier lock on Artemis-7. Solar radio flux index is sitting at five thousand solar flux units. The S-band transponder is drowned in solar noise. We are blind on ground tracking."

In the dark of the storm shelter, three hundred and ten thousand kilometers from home, Sarah Ross watched a single red LED blinking on her wrist telemetry display:

`COMM: CARRIER LOST`  
`ATTITUDE: DEGRADED (IMU OPEN LOOP)`  
`RANGE TO PERILUNE: 68,400 KM`  
`TIME TO IMPACT: 28 HOURS 14 MINUTES`  

---

### The Drifting Inertial Platform

Inside the avionics bay, the Honeywell Miniature Inertial Measurement Unit (MIMU) was spinning its three ring-laser gyroscopes.

With the star trackers offline and the ground tracking antennas drowned in solar radio noise, the spacecraft had no external frame of reference. It had become a closed, isolated box drifting through space, forced to infer its orientation and position by integrating the tiny accelerations and angular rates detected by its internal sensors.

In atmospheric flight, a ring-laser gyro is a precision instrument. In deep space, over hours of uncorrected coasting, it is an engine of creeping error.

The gyro drift rate was rated at 0.005 degrees per hour. Over thirty minutes, that error was negligible. Over twenty-four hours, an angular drift of one-tenth of a degree in pointing vector translates into an error of hundreds of kilometers when projecting an orbital trajectory across the cislunar void.

Even worse was the unmodeled acceleration.

As the solar proton storm struck the massive thirty-meter span of Orion’s four solar array wings, the flux of charged particles imparted a continuous, asymmetric mechanical pressure:

$$F_{\text{solar}} \approx 4.8 \times 10^{-5} \text{ Newtons}$$

It was a force no greater than the weight of a postage stamp. But sustained over ten hours against an eighty-ton vehicle, that minute photon and proton pressure produced an unmeasured velocity perturbation of 0.22 meters per second.

In low-Earth orbit, a quarter of a meter per second is an inconsequential drift.

In the chaotic, three-body gravitational landscape of cislunar space—where the gravitational fields of the Earth and the Moon pull against each other along the razor-thin saddle of the Lagrange manifolds—an error of twenty centimeters per second is the difference between a triumphant orbital insertion and a lethal, high-velocity impact on the lunar surface.

---

### The Manual Sextant & The Ghost of Apollo

At 18:00 UTC, Sarah Ross could no longer stay in the floor well.

She pushed back the heavy Nomex blankets, ignoring the sharp prickle of secondary ionization in her skin, and floated up to the command couch.

"Commander, the dosimeter rate is still seven rads an hour," Lin Liu warned from the shelter hatch.

"If we don't know our state vector, the dosimeter doesn't matter," Ross answered. "We hit the lunar crust in twenty-four hours."

She reached above her helmet to the secondary optical alignment hatch—a recessed, five-inch circular quartz viewport equipped with a manual optical reticle and an Apollo-heritage optical alignment sextant. In the 1960s, Jim Lovell and Buzz Aldrin had used optical space sextants to measure the angular separation between stars and lunar landmarks, calculating state vectors with paper charts and pencil.

Sarah pressed her right eye against the rubber eyecup.

The scene through the sextant was a nightmare of chaotic scintillation. The solar proton flux was lighting up the quartz glass with microscopic phosphorescent sparks. Outside, the Moon was a massive, blinding crescent of scarred gray basalt, but the limb of the lunar disk was shimmering with thermal and optical distortion.

"Miller," Ross called out, her fingers adjusting the fine-vernier micrometer drum. "Call out the Apollo benchmark stars. Can you see Acrux or Canopus?"

Miller squinted through the side viewport with handheld binoculars. "Negative. The solar coronal glow is scattering across the entire forward hemisphere. Everything within thirty degrees of the Sun is washed in white flare glare."

Ross tried to align the crosshair with the rim of the crater Copernicus.

Every time Orion’s reaction control thrusters pulsed—tiny, automated firings of cold gaseous nitrogen to keep the vehicle within its deadband attitude limit—the crosshairs in the reticle jumped by forty arcseconds.

In low-Earth orbit, a human navigator can average out ten readings and find an orbital plane within three nautical miles. But here, at the weak stability boundary, an error of forty arcseconds at a distance of sixty thousand kilometers represents an uncertainty of twelve kilometers in position.

And the lunar capture corridor had a total tolerance of less than four kilometers.

Sarah stepped back from the eyepiece, breathing hard. Her right eye burned from the glare.

"Manual sighting cannot solve this," she said, her voice dropping into a flat, grim whisper. "The non-linear gradient is too steep. We are falling down a gravitational funnel, and our eyes are full of static."
