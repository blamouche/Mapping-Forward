# The open map stack

*Why the maps under your feet are being rebuilt on shared foundations — and what comes next.*

The news last week felt almost mundane: Microsoft finished updating the address data in Bing Maps. Nine months of phased deployment, one new partner, one cleaner dataset. A routine infrastructure upgrade, buried in a press release.

Except it wasn't routine at all. What Microsoft actually did — quietly, methodically, over three seasons — was migrate one of the world's major map platforms to a new kind of data foundation. One built on open standards, multi-source aggregation, and continuous machine-driven updates. The Bing Maps overhaul is a signal, not an announcement. It marks a moment when the industry's direction of travel became impossible to ignore.

## The infrastructure layer is shifting

TomTom Orbis Maps, the data layer now powering Bing's address search, is a product of the Overture Maps Foundation — a consortium involving Amazon, Meta, Microsoft, and TomTom itself. Overture's bet is that foundational mapping data — addresses, road networks, building footprints, place names — can be produced more efficiently as a shared resource than by each company maintaining proprietary datasets in parallel. The Orbis layer weaves together OpenStreetMap, commercial partner data, TomTom's proprietary sensor observations, and Overture Foundation releases into a single continuously updated dataset.

Microsoft ran the switch carefully. For each region, they benchmarked the new data against the old on three dimensions — address coverage, positional accuracy, and query resolution success — before promoting it to production. Europe came first, in June 2025, where the improvement in data density was greatest. The final global rollout wrapped up in early April 2026. The result flows through Bing Maps, Bing Search, Copilot, and the Azure Maps APIs that thousands of developers build on.

What changes technically is also what changes commercially. Instead of bulk updates pushed out every few months, Bing now runs on a continuous update model. Real-world changes — new streets named, addresses renumbered, buildings demolished — flow through AI-driven pipelines into the live dataset without human-supervised publishing cycles. The map is less a product that ships on a schedule and more a system that learns.

This is not a story about Bing beating Google. It is a story about what replaces the era of proprietary map moats. For twenty years, the dominant narrative in mapping was that whoever built the biggest exclusive dataset would win. Google invested billions in Street View, satellite imagery, and ground truth collection. HERE built partnerships with auto manufacturers. TomTom sold dedicated GPS devices and locked their data behind license fees. The competitive logic was vertical integration: control the data, control the platform.

The Overture model inverts this logic. If enough major players contribute to and consume a shared data layer, the cost of foundational map maintenance is distributed while the competitive surface moves up the stack — to AI features, UX, domain-specific applications. Microsoft doesn't win on maps by owning more addresses than Google. It wins by building Copilot integrations and Azure services on top of a data layer that is good enough, always current, and freely improving.

## Maps as climate infrastructure

While this platform shift dominates the week's industry news, two other stories from the same period are worth sitting with — because they point to a different dimension of mapping's current moment.

In the western United States, wildfire risk maps from the National Interagency Coordination Center now show red spreading across a region from the Southwest into the Rockies, Pacific Northwest, and Northern California. The forecast is built on three simultaneous anomalies: snowpack deficits so severe that the Four Corners region saw its earliest recorded melt date by four to six weeks; temperatures so extreme that Albuquerque hit 90 degrees Fahrenheit in late March — six weeks earlier than any prior recorded date; and drought conditions that have desiccated vegetation across a region that has historically depended on winter moisture as its natural firebreak.

These maps are not decorative. Emergency managers use them to pre-position resources before fire season peaks. Insurance actuaries use them to adjust risk models in real time. State planners use them to decide where to permit new housing and where to restrict it. The information design challenge — converting multi-variable probabilistic forecasts into color gradients that a county official can act on in a budget meeting — is as critical as the underlying modeling.

North Carolina's floodplain mapping story makes the same point from a different angle. The state's new advisory maps for five Eastern river basins use two-dimensional rain-on-grid modeling that follows precipitation across terrain rather than just along stream channels. The results are uncomfortable: a UNC Chapel Hill study found that 43 percent of buildings that flooded at least once between 1996 and 2020 were located outside the official FEMA floodplain. Nearly half of all flood victims were, on paper, in low-risk areas.

This is a measurement problem, not a geological one. Traditional FEMA flood zone maps were built around stream overflow events. They work reasonably well in river valleys. They work poorly in the increasingly common scenario of intense precipitation — the type of rain event that drops six inches in twelve hours over a broad upland — where water flows across the landscape before reaching any channel. The new modeling approach captures this dynamic. It does not change the physics of flooding; it changes which buildings appear on the risk map, which changes which households pay flood insurance premiums, which changes investment decisions and property values and municipal bond ratings.

Maps, in other words, are not neutral documents. They produce the reality they appear to describe.

## The spatial stack gets an upgrade

The Wherobots-and-Felt story from GeoAwesome this week offers a useful architectural diagram for understanding where GIS is heading as an industry.

The traditional spatial stack was built around desktop software — ArcGIS, QGIS — that required installation, licensing, training, and significant technical fluency. Spatial analysis was a specialist discipline. The people who could do it were a small subset of any organization, separated from decision-makers by a skills wall.

What Wherobots and Felt represent is a decomposition of that monolith. Wherobots handles the processing layer: built on Apache Sedona, it scales spatial computation across cloud infrastructure, allowing organizations to run large-scale geospatial analytics without dedicated GIS infrastructure. Felt handles the presentation layer: a browser-based collaborative mapping tool designed for people who need to make and share maps without knowing what a projection system is.

Separately, each solves a narrow problem. Together, they sketch a pattern: separate the concerns, connect with open standards, and let AI do the translation work between them. A data engineer feeds satellite-derived land cover classifications into Wherobots. A policy analyst opens Felt and sees a map. The spatial stack disappears into the background.

India's National Geospatial Policy 2022 is trying to do something similar at the national level. The policy removes historical restrictions on geospatial data access — restrictions that had kept mapping data locked behind government agencies for decades on security grounds — and replaces them with open-access platforms (the National Geospatial Data Registry, the Unified Geospatial Interface) that startups, researchers, and local governments can build on. The target: a Digital Elevation Model covering the full country by 2030 and National Digital Twins for major cities by 2035.

The ambition is to make spatial data infrastructure behave like electrical infrastructure: something any business or government can connect to, rather than something each actor must build for themselves.

## The indoor frontier

Market research projections for indoor mapping and 3D wayfinding — both market analysis reports from this week — are worth treating with appropriate skepticism toward the numbers and genuine attention to the underlying trends.

The indoor navigation market is fragmented in ways that outdoor mapping is not. Outside, GPS provides a common positioning foundation. Inside, you need Bluetooth beacons, Wi-Fi fingerprinting, UWB positioning, or LiDAR-scanned floor plans — and there is no single dominant protocol. Google and Apple have indoor maps for major airports and malls. Navvis and IndoorAtlas and Pointr handle specialized enterprise deployments. Siemens integrates spatial intelligence with building management systems.

What is changing is the cost of floor plan creation. LiDAR scanning can now produce detailed 3D models of interior spaces in hours rather than weeks. AI can convert those scans into navigable maps automatically. The bottleneck is shifting from data capture to data standardization — the indoor mapping equivalent of the Overture Maps problem. When floor plan data exists in dozens of incompatible proprietary formats, you cannot build seamless navigation across multiple venues.

The same dynamics apply to TomTom's sustainability pitch and the LOCUS partnership announced this week. TomTom frames location intelligence as environmental infrastructure: eco-routing that smooths traffic reduces fuel burn; EV navigation with charging infrastructure data accelerates electric adoption; traffic analytics enable cities to design lower-emission road networks. These claims are directionally correct. Whether they add up to meaningful scale in the near term depends on how quickly transportation operators actually adopt them — which depends on whether the data is accessible, affordable, and integrated into existing workflows.

## The shape of what's coming

The through-line across a week's worth of mapping news is not any single product launch. It is a structural shift in how map data is produced, maintained, and consumed.

Proprietary data moats are expensive to build and increasingly hard to defend. Open standards — Overture, OpenStreetMap, common API schemas — lower the cost of foundational data for everyone while raising the competitive surface to applications, intelligence, and domain expertise. The winners in the next phase of the mapping industry will not be the organizations with the most exclusive datasets. They will be the ones who build the most useful things on top of shared foundations.

Climate risk mapping, indoor navigation, geospatial policy, logistics intelligence: each of these domains is at a different point in that transition. But each is moving in the same direction — toward maps that are more open, more current, more consequential, and more embedded in the decisions that shape physical environments.

The map is changing. What we do with it is the harder question.

---

## Sources
1. [Get Started with the Google Maps Geocoding API v3](https://developers.google.com/maps/documentation/geocoding/guides-v3/start)
2. [Nordregio Maps: Nordic and Arctic Regional Development Cartography](https://nordregio.org/maps//?selected_tags%5B0%5D=146&view=list)
3. [These Maps Show Exactly Where the West Might Burn This Summer](https://grist.org/extreme-weather/these-maps-show-exactly-where-the-west-might-burn-this-summer/)
4. [New Advisory Floodplain Maps Available for Five Eastern North Carolina River Basins](https://www.deq.nc.gov/news/press-releases/2026/04/01/new-advisory-floodplain-maps-available-five-eastern-north-carolina-river-basins)
5. [Microsoft Bing Maps si aggiorna con i dati TomTom Orbis Maps](https://www.hdblog.it/microsoft/articoli/n653899/microsoft-bing-maps-aggiornamento-tomtom-orbis/)
6. [National Geospatial Policy Strengthening India's Mapping Ecosystem](https://www.usthadian.com/national-geospatial-policy-strengthening-indias-mapping-ecosystem/)
7. [TomTom selected by LOCUS to provide high-precision traffic data](https://www.tomtom.com/newsroom/press-releases/general/160526227876208/tomtom-selected-by-locus-to-provide-high-precision-traffic-data-for-location-intelligence-platform/)
8. [Location data for a greener future](https://www.tomtom.com/newsroom/behind-the-map/location-intelligence-making-a-greener-future)
9. [Microsoft's Bing Maps Receives Its Largest Address Data Upgrade in Years via TomTom Orbis](https://www.neowin.net/news/microsofts-bing-maps-receives-its-largest-address-data-upgrade-in-years/)
10. [Digital Indoor Map Market Is Going to Boom](https://www.openpr.com/news/4452558/digital-indoor-map-market-is-going-to-boom-google-apple)
11. [3D Wayfinding Software Market Is Going to Boom](https://www.openpr.com/news/4452745/3d-wayfinding-software-market-is-going-to-boom-mapbox-pointr)
12. [The AI-Ready Spatial Stack: How Wherobots and Felt Are Redefining GIS](https://geoawesome.com/the-ai-ready-spatial-stack-felt-wherobots/)
13. [Bing Maps Receives Its Largest Address Data Upgrade in Years](https://www.neowin.net/news/microsofts-bing-maps-receives-its-largest-address-data-upgrade-in-years/)
14. [Bing Maps draait nu volledig op TomTom Orbis-adresdata](https://www.ictmagazine.be/nieuws/bing-maps-draait-nu-volledig-op-tomtom-orbis-adresdata/)
15. [必应地图迎来最大规模地址数据升级 引入 TomTom Orbis全球数据集](https://www.cnbeta.com.tw/articles/tech/1556284.htm)
