# The decree and the display

*When governments vote on maps and platforms can't comply, the real power has already moved somewhere else.*

In September 2026, 164 countries voted in the United Nations General Assembly to adopt the Equal Earth projection as the organization's standard world map. One voted against — the United States, which called the resolution a "radical ideological project." The vote passed. The world, on paper, had a new view of itself.

Open Google Maps on your phone. Nothing has changed. Greenland still sprawls across the top of the screen, Africa still looks smaller than it is, and the projection that Gerardus Mercator drew in 1569 for navigators still governs what you see. The UN voted, and the maps on a billion screens didn't move.

This is the implementation gap: the space between a political decision about maps and the technical infrastructure that actually puts that decision in front of people. Three stories from this week — the UN projection vote, the renaming of Lake Ontario, and France's ecological routing decree — reveal a structure that few have named but many are running into. Political authority over maps is decoupling from the power to display them. And the power to display them is held by a small number of companies whose architectures were built for a different era.

## The projection problem

The UN's Equal Earth resolution has a sound rationale. The Mercator projection inflates the size of land masses the farther they sit from the equator, making Greenland appear roughly the size of Africa when it is in fact fourteen times smaller. Equal Earth corrects this, preserving area accurately while keeping continents in shapes that look familiar. France has already announced it will switch its official cartography to the Eckert IV projection, another equal-area option, for much the same reason. The colonial legacy of Mercator — which centers Europe and exaggerates the global north — is the explicit target.

But Google Maps runs on a tile architecture built around Web Mercator. The world is pre-rendered in thousands of square image tiles, each aligned to a Mercator grid, cached on servers across the planet, and stitched together on your screen as you pan and zoom. Switching to Equal Earth would mean re-rendering every tile, re-engineering the coordinate system that underpins every search result, every turn-by-turn direction, every business listing pinned to a latitude-longitude pair. It is not a design change. It is a rebuild of the platform's skeleton. As the French publication Clubic reported, the UN resolution will not change Google Maps anytime soon, because the architecture will not allow it.

The infrastructure beneath the map — [the part you never see](https://mappingforward.substack.com/p/the-map-is-just-the-surface) — is what actually governs what you see. A projection that survived a 164-to-1 UN vote will keep surviving because the pipes it runs through were poured a decade before anyone voted on them.

## The naming problem

The same week the UN voted, the United States was finishing work on a different kind of cartographic decree. President Trump's executive order renaming Lake Ontario as "Lake America" had worked its way through the US Board on Geographic Names — the obscure federal body that maintains the official inventory of American place names — and emerged as policy. The GNIS database was updated. The federal government's maps changed.

What happened on Google Maps was stranger than nothing. Google announced that it would show "Lake America" to users in the United States, "Lake Ontario" to users in Canada, and both names to everyone else. The same body of water, on the same platform, would carry a different name depending on where you opened the app. MapQuest, the older mapping service, refused the change outright and kept "Lake Ontario" for all users.

The Conversation, covering the renaming, traced the tension between the Board on Geographic Names' bottom-up process — designed to reflect local usage and historical record — and the top-down override of an executive order. But the deeper story is what happened after the decision. Google's country-specific policy means the shared geographic name is now fragmented by audience. There is no single lake. There is the lake Americans see and the lake Canadians see, mediated by a commercial platform making [editorial choices that no government voted on](https://mappingforward.substack.com/p/the-map-is-not-neutral).

A government can change a name in its own databases in days. A platform that serves the entire planet has to decide which version of reality to show to whom — and that decision sits with the company, not with the Board on Geographic Names, the UN, or any legislature.

## The routing problem

France took a different approach to governing maps this summer. A government decree required navigation apps like Waze and Google Maps to calculate routes that minimize emissions rather than travel time — effectively mandating that the fastest way home no longer be the default. Presse-Citron reported that users can still manually switch back to the fastest route, but the algorithmic default was meant to change.

It did, technically. But Le Parisien, drawing on TomTom traffic data, found that the real reason French roads moved more smoothly this summer was not that drivers embraced ecological routing — it was that the spread of such routing across multiple apps distributed traffic more evenly across the network, a side effect of collective behavior rather than individual compliance. And because users can override the green default with two taps, the decree's actual hold on routing is soft. The mandate changes what the app suggests. It does not change what drivers choose. The app, in other words, [is making the decision](https://mappingforward.substack.com/p/the-map-is-now-in-the-drivers-seat) — and the driver can overrule it, which means the decree's authority stops at the phone's surface.

The routing decree reveals the limit of algorithmic governance by fiat. You can order a platform to change its default. You cannot order a person to accept it. The implementation gap, here, runs all the way to the driver's seat.

## Where the gap closes

There is one place this month where political mandates about maps did become infrastructure. In Karnataka, the Indian state government launched a GIS-based application that geo-tags more than 300,000 rural water assets with five-meter accuracy — a working system, deployed, tracking real pipes and real pumps across real villages. In Tamil Nadu, the state government mandated that every urban local body produce legally valid GIS-based Master Plans, and backed the mandate with the surveying, data standards, and institutional scaffolding to make those plans enforceable.

The difference is not ambition. France, the UN, and the United States all issued clear directives. The difference is that the Indian state governments built the thing they decreed. They did not order a foreign platform to change its behavior; they created their own systems, with their own data, on infrastructure they controlled. The implementation gap closes when the authority that issues the mandate is also the authority that builds the pipes.

This is the structural lesson the other three stories circle around. Google's tile architecture, its country-specific naming policy, its routing defaults — these are not bugs. They are the architecture of a platform that was never designed to be governed by external decree. The platform was designed to serve users and advertisers, and it does both with remarkable efficiency.

The commercial layer that sits on top of all this is its own kind of ungoverned decree. Android Police reported this week on Google Maps settings users should turn off — background location tracking, cellular offline downloads, personalized ads generated from location data. Apple Maps, for its part, has been showing unkillable ads that no user voted for and no regulator ordered. The ad layer, the tracking layer, the personalization layer — these exist because the platform's business model requires them, and they persist regardless of what any government decides about projections or place names.

The counterexample to all of this came not from a decree or a business model but from a disaster. When a glacier collapsed in northern Nepal this summer, triggering a debris avalanche and a flash flood that destroyed more than 240 buildings in Syapru Besi and killed over 380 people, the Copernicus Emergency Management Service produced satellite-based flood damage maps within hours. The USGS documented the cascade from glacier collapse to avalanche to flood, tracing a hazard chain that no political body had ordered anyone to map. NBC News used satellite imagery to show the flood path to a public that had no other way to see it.

Here, implementation followed crisis rather than decree. The mapping happened because the infrastructure for rapid response already existed — built and funded by the European Union and the US Geological Survey — and because the need was unambiguous. No one had to vote on whether the flood was worth mapping. The gap between intent and display collapsed because the system was built for exactly this moment.

When the gap between political will and platform capability hardens into the defining feature of cartographic governance, the consequences are concrete. The UN can vote on projections, presidents can rename lakes, ministries can decree ecological routes — and the screens in a billion pockets will reflect none of it, or some of it, or a version of it filtered through commercial decisions no one elected. The maps that govern how people see the world are no longer produced by the institutions that claim authority over them. They are produced by the architectures that deliver them. And those architectures, for now, answer to their own logic.

---

## Sources
1. [Copernicus Emergency Management Service Maps Flood Damages in Northern Nepal](https://eu-space.europa.eu/components/earth-observation-copernicus/image-of-the-day/copernicus-emergency-management-service-maps-flood-damages-northern-nepal)
2. [2026 Nepal Debris Avalanche and Flash Flood](https://www.usgs.gov/programs/landslide-hazards/science/2026-nepal-debris-avalanche-and-flash-flood)
3. [Maps Show How a Glacier Collapse Triggered Deadly Nepal Floods](https://www.nbcnews.com/data-graphics/himalayan-glacier-collapse-nepal-tibet-disaster-rcna594762)
4. [5 Google Maps Settings Drivers Should Enable](https://www.bgr.com/2242473/google-maps-settings-drivers-should-enable/)
5. [You Can Now 'Ask Maps' For Hyper-Specific Travel Advice. But Should You?](https://www.cntraveler.com/story/you-can-now-ask-maps-for-hyper-specific-travel-advice-but-should-you)
6. [Lake Ontario to Lake America: Who Gets to Decide What Goes on Maps?](https://theconversation.com/lake-ontario-to-lake-america-who-gets-to-decide-what-goes-on-maps-290698)
7. [GIS-Based Application Launched for Rural Water Asset Management in Karnataka](https://www.newindianexpress.com/states/karnataka/2026/Aug/28/gis-based-application-launched-for-rural-water-asset-management-in-karnataka)
8. [Tamil Nadu Mandates GIS-Based Master Plans for Urban Local Bodies](https://www.newindianexpress.com/states/tamil-nadu/2026/Aug/27/tn-government-mandates-gis-based-master-plans-for-urban-local-bodies-development-authorities)
9. [Capturing the Dubai Metro Blue Line with Millimeter Accuracy](https://www.geoweeknews.com/articles/capturing-the-dubai-metro-blue-line-with-millimeter-accuracy/)
10. [Waze and Google Maps No Longer Give the Fastest Routes in France](https://www.presse-citron.net/cest-dommage-pourquoi-waze-et-google-maps-ne-donnent-plus-les-trajets-les-plus-rapides-en-france/)
11. [Summer 2026: Why Traffic Was More Fluid on French Roads](https://www.leparisien.fr/societe/moins-de-bouchons-moins-de-galeres-pourquoi-lete-2026-a-ete-plus-fluide-sur-les-routes-francaises-28-08-2026-YKTTWWRHOVBWHBEBCQ33FQWDKY.php)
12. [Why the UN's New World Map Won't Change Google Maps Anytime Soon](https://www.clubic.com/actualite-628429-pourquoi-la-nouvelle-carte-du-monde-adoptee-par-l-onu-ne-va-pas-changer-google-maps-tout-de-suite.html)
13. [Can You Guess the Real Size of Each Country on the New World Map?](https://www.aljazeera.com/news/2026/9/6/can-you-guess-the-real-size-of-each-country-on-the-new-world-map)
14. [3 Hidden Google Maps Settings You Should Turn Off Right Away](https://www.androidpolice.com/hidden-google-maps-settings-turn-off/)
15. [How the GNIS Lake Ontario/Lake America Name Change Will Appear in Google Maps](https://blog.google/products-and-platforms/products/maps/gnis-lake-ontario-lake-america-name-change/)