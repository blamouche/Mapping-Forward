# The dashboard is becoming the map

*January’s mapping story wasn’t about prettier tiles; it was about maps turning into operating systems for vehicles, supply chains, and geopolitics.*

For a long time, we talked about maps as if they were screens. You opened an app, you saw a map, you followed a blue line. In January’s reading, that mental model keeps failing. The month is dominated by a different idea: the map is migrating into the machinery of how things move, get built, and get governed.

You can see it in the automotive headlines. HERE argues bluntly that phone-based navigation is ending and that the dashboard will win because it can see what the phone cannot. Its pitch is not primarily cartographic; it is architectural. Cars have sensors. Cars have actuators. Cars have constraints like battery state, traction, and driver-assistance policies. If navigation is supposed to be “right” in that environment, it can’t be a generic overlay. It has to be part of the vehicle’s software stack.

You can see the same migration in open mapping infrastructure. MapLibre’s new MLT vector tile format is framed as performance engineering, but it is really about scale economics. If you can compress six times better and decode faster, you can treat a planet-scale basemap like an ordinary dependency: ship it more widely, cache it more aggressively, render it in more places. Protomaps adding Overture Maps support is about the same thing from the data side: swap out a source dataset without rewriting your styles, and the basemap starts to look like a plug-in component rather than a monolith.

And you can see it in the political and cultural pieces that still orbit mapping. A map of American bases in Europe is a reminder that “where” is still power. A map of Gaza’s hypothetical future under a proposed plan is a reminder that maps can also be propaganda. A rediscovered manuscript on Mercator’s projection is a reminder that the foundations we treat as neutral were built under very specific constraints and incentives.

The obvious conclusion is that mapping is everywhere. The more useful conclusion is sharper: if maps are becoming infrastructure, then the core problem is not features. It is integration. Who controls the data? How fast can it change? What do you trust when layers conflict? What happens when a system uses the map to make decisions, not just to display them?

## The car is turning maps into software

The HERE portfolio at CES 2026 reads less like a product launch and more like a blueprint for the “vehicle OS” era. Hyundai vehicles receiving monthly over-the-air map updates are not a nice-to-have; they are a statement that maps now update like apps. Lucid’s focus on range-aware isolines is not just better routing; it is navigation tied to the physics and economics of electric driving. Qualcomm’s “e-horizon” concept is not a marketing term; it is an admission that autonomy depends on seeing beyond what onboard sensors can reliably perceive, especially when weather and occlusion make the world messy.

Once you accept that, a lot of the rest of the month snaps into place. HERE’s “software-defined vehicle maturity framework” is essentially a roadmap for how a car company becomes a software company. The interesting part is not the labels but the direction of travel: connected, then augmented, then adaptive, then agentic. Each step moves mapping deeper into the system. A connected car needs updates; an augmented car needs feature expansion; an adaptive car needs edge AI that learns patterns; an agentic car needs to coordinate with the broader environment. The map, in this story, isn’t a dataset. It’s a set of promises about what the system can do safely, where, and under which conditions.

That promise shows up in HERE’s January platform release notes in a deceptively mundane way. Experimental layers for “Named Areas” and tile intersections sound like developer conveniences, but they reveal a concern that only infrastructure products have: how do you partition the world so people can process it reliably? Truck routing restrictions, timestamped in RFC 3339, reveal another infrastructure trait: policy changes with time, and systems need to know which policy applied when. Traffic light visualization and route serialization hint at a future where navigation outputs are not ephemeral; they are objects that can be stored, exchanged, audited, and replayed.

The month even contains a quiet warning about how brittle this transition can be. The developer tutorial on adding HERE Maps to a website using AI coding assistants is one of the clearest “ground truth” pieces: AI made the work faster, but it also produced outdated and hallucinated API usage. That is exactly the failure mode you cannot afford when maps become embedded infrastructure. A wrong label on a web map is annoying. A wrong restriction mode in a fleet route or a deprecated rendering style in production can become downtime, or worse.

In other words, January’s vehicle story is not “navigation is smarter.” It is “navigation is no longer a layer.” It is becoming a subsystem.

## The open basemap supply chain is maturing

At the same time, the month shows open mapping maturing in a way that looks suspiciously like the early days of open-source software: governance solidifies, formats evolve, and tooling starts to treat data sources as interchangeable.

Overture Maps is still, in many ways, a trust experiment. The foundation appearing on Software Engineering Radio is outreach, but it is also a strategic move: geospatial projects do not win by being correct; they win by being legible to developers. Naming an executive director is not bureaucracy; it is a recognition that shared datasets need real leadership if they are going to survive competing corporate incentives and community expectations.

The technical arc then connects to Protomaps and MapLibre. Protomaps adding Overture support is interesting precisely because it tries to make the swap non-disruptive. The PR emphasizes compatibility with existing MapLibre styles and uses modern data processing primitives like DuckDB over Parquet. This is what “data as infrastructure” looks like in 2026: not a bespoke GIS pipeline, but something closer to the modern analytics stack. The point is not only that Overture data can be used. The point is that it can be used without rewriting everything else.

MapLibre’s MLT format sits one layer lower, but it pushes the same direction. Tile formats are rarely glamorous, yet they determine the economics of every map you have ever scrolled. Compression and decoding speed become strategy when you are serving maps at scale or embedding them in constrained environments like vehicles. MLT’s mention of future support for linear referencing and better 3D capabilities is also telling. It assumes that basemaps are not flat pictures but semantically rich systems that other systems will depend on.

This open supply chain story also has a physical counterpart in the State of the Map 2026 announcement. A community event in Paris might look like calendar filler, but it is one of the places where the messy boundary between volunteer mapping and institutional mapping gets negotiated. OpenStreetMap has always been both a commons and an industrial input. Conferences are where those two identities collide and, sometimes, align.

January’s open mapping signal is therefore not “open is winning.” It is “open is becoming serious.” Governance, formats, and tooling are lining up around the idea that basemaps are components, not artifacts.

## Mapping is also analysis, narrative, and power

If maps are becoming infrastructure for machines, they are also becoming sharper instruments for humans. The month’s analytic and narrative pieces show how easily “mapping” expands beyond roads into decision-making and persuasion.

TomTom’s Traffic Index and Area Analytics are good examples of a shift that is easy to underestimate. Traffic is no longer just something you visualize in red and green. It is a measurable asset that can be exported, compared across custom geographies, and used to justify policy or investment. When a platform offers GeoJSON exports and time-sliced metrics by hour and day, it is not selling a map. It is selling an argument, with data attached.

The broader analytics ecosystem is visible too. CARTO’s roundup of spatial analytics and visualization trends, and Esri’s piece on GIS and AI for urban forestry, are part of the same message: geospatial is increasingly where domain problems get framed. Heat mitigation becomes a mapping problem. Climate resilience becomes a mapping problem. Once those problems are framed spatially, the temptation is to treat the output map as an answer rather than a model with assumptions.

The political cartography in the month is an even clearer warning. A map locating American military bases in Europe is informative, but it is also a way of making a security posture legible. A map describing what would happen to Gaza under a proposed plan is not neutral description; it is a way of normalizing a future. The Iran uprising cartography is a reminder that mapping can also be a tool for documenting, coordinating, and remembering when official narratives are contested.

Even the “non-Earth” pieces fit the month’s theme. A dark matter map from JWST is a demonstration that mapping is, at its core, the discipline of turning an invisible structure into a navigable representation. The rediscovered manuscript shedding light on Mercator’s projection origins is another reminder: the choices that make a map useful are choices that distort. They always have been.

So the month ends with a tension that the geospatial industry often tries to avoid. We want maps to be trusted, but we also want them to be persuasive. We want them to be dynamic, but we also want them to be auditable. We want them to be open, but we also want them to be secure. We want them to be embedded in vehicles, but we also want them to be understandable to humans.

January doesn’t resolve that tension. It does something more useful: it shows where it is going to be fought.

The map is moving into the dashboard, into the supply chain, into the standards body, and into the argument. If you build mapping products, the work ahead is less about adding layers and more about designing contracts: provenance, update cadence, governance, and safety boundaries. If you consume mapping products, the work ahead is less about learning new features and more about learning new questions: who produced this layer, under what incentives, and what happens when it is wrong?

---

## Sources
1. [Seeing Beyond the Sensors: HERE Showcases AI-Powered Map Data with Snapdragon Ride](https://www.here.com/learn/blog/ces-2026-snapdragon-ride)
2. [From Discovery to Action: A New Foundation for Travel](https://overturemaps.org/blog/2025/from-discovery-to-action-a-new-foundation-for-travel/)
3. [The Era of Phone-Based Navigation is Ending. Your Dashboard is Next](https://www.here.com/learn/blog/next-generation-car-navigation)
4. [Overture Maps Explained on Software Engineering Radio](https://overturemaps.org/blog/2025/overture-maps-explained-on-software-engineering-radio/)
5. [Overture Maps Foundation Names William Mortenson as New Executive Director](https://overturemaps.org/announcements/2025/overture-maps-foundation-names-william-mortenson-as-new-executive-director/)
6. [Software-Defined Vehicles: Moving Up the Maturity Framework](https://www.here.com/learn/blog/software-defined-vehicles-maturity-framework)
7. [HERE Just Made the Road to Software-Defined Vehicles a Lot Smoother](https://www.here.com/learn/blog/software-defined-vehicles-solutions)
8. [Location Forecast 2026: Orchestrating Seamless Logistics from Planning to Delivery](https://www.here.com/learn/blog/supply-chain-trends-2026)
9. [TomTom Traffic Index 2025](https://www.tomtom.com/traffic-index/)
10. [Adding HERE Maps to your website in 2026](https://www.here.com/learn/blog/adding-here-maps-to-your-website-in-2026)
11. [HERE at CES 2026: every reveal, announcement and award](https://www.here.com/learn/blog/ces-2026-announcements)
12. [January 2026 Platform Release Notes](https://www.here.com/learn/blog/january-2026-platform-release-notes)
13. [State of the Map 2026 : rendez-vous a Paris !](https://www.openstreetmap.fr/le-state-of-the-map-2026-aura-lieu-a-paris/)
14. [TomTom Area Analytics](https://www.tomtom.com/products/area-analytics/)
15. [5 best spatial analytics and visualizations of 2025](https://carto.com/blog/5-best-spatial-analytics-and-visualizations-of-2025)
16. [Carte : Ou se trouvent les bases militaires americaines en Europe ?](https://www.touteleurope.eu/l-ue-dans-le-monde/carte-ou-se-trouvent-les-bases-militaires-americaines-en-europe/)
17. [The cold war maps that can help us rethink today's Arctic conflict](https://theconversation.com/the-cold-war-maps-that-can-help-us-rethink-todays-arctic-conflict-274058)
18. [Gemini in navigation is now available for walking and cycling in Google Maps](https://blog.google/products-and-platforms/products/maps/gemini-navigation-biking-walking/)
19. [GIS and AI Transform Urban Forestry for Heat Mitigation](https://www.esri.com/about/newsroom/blog/gis-ai-urban-forestry-heat-mitigation)
20. [Iran. Cartographie d'un soulèvement](https://orientxxi.info/Iran-Cartographie-d-un-soulevement)
21. [Webb's biggest dark matter map shows the Universe's invisible scaffolding in stunning detail](https://www.skyatnightmagazine.com/news/james-webb-space-telescope-dark-matter-map)
22. [Un manuscrit decouvert en Espagne eclaire les origines de la projection de Mercator](https://www.courrierinternational.com/article/cartographie-un-manuscrit-decouvert-en-espagne-eclaire-les-origines-de-la-projection-de-mercator_239284)
23. [Map shows what would happen to Gaza under the US master plan](https://www.aljazeera.com/news/2026/1/27/map-shows-what-would-happen-to-gaza-under-the-us-master-plan)
24. [Protomaps Adds Overture Maps Data Source Support](https://github.com/protomaps/basemaps/pull/541)
25. [TomTom Joins Precisely Data Link Program](https://www.precisely.com/press-release/tomtom-joins-precisely-data-link-program-bringing-authoritative-map-and-street-data-to-the-pre%E2%80%91linked-data-ecosystem/)
26. [Announcing MapLibre Tile: a modern and efficient vector tile format](https://maplibre.org/news/2026-01-23-mlt-release/)
