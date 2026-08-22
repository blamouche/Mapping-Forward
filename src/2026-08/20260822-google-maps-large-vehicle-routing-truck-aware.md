# Google Maps Just Launched Truck-Aware Routing That Knows About Low Bridges and Weight Limits
**Source**: https://www.freightwaves.com/news/google-maps-just-launched-truck-aware-routing-that-knows-about-low-bridges-and-weight-limits-here-is-what-it-means-and-what-it-does-not
**Date**: August 22, 2026
**Author**: FreightWaves
**Keywords**: Google Maps, Large Vehicle Routing, truck navigation, fleet management, Routes API, Navigation SDK, low bridges, hazmat restrictions

## Elevator pitch
Google announced the general availability of Large Vehicle Routing (LVR), a version of its mapping technology built specifically for trucks and buses that accounts for height, weight, length, hazmat restrictions, and low bridges — addressing one of the most preventable hazards in trucking through developer APIs rather than a consumer app.

## Takeaways
- LVR is now GA in the US across three Google developer products: Routes API, Route Optimization API, and Navigation SDK
- Operators can specify detailed vehicle profiles including height, weight, length, width, axle count, and hazardous goods classifications
- A large-vehicle-specific ETA model combines observed truck travel speeds with real-time and predictive traffic data
- The Navigation SDK displays truck-aware routes with visual callouts flagging restrictions matched to the vehicle's dimensions
- LVR is a developer tool, not a consumer app — it will reach drivers through fleet management companies, TMS providers, and telematics firms that integrate it

## Synthesis
Google's entry into truck-specific routing marks a significant shift in the mapping landscape. While dedicated trucking navigation products have existed for years, Google brings its enormous road dataset, traffic modeling, and the interface millions of drivers already know to the specific problem of routing large commercial vehicles. The low-clearance problem alone justifies the attention: bridge strikes cause injuries, deaths, expensive infrastructure damage, and enormous liability, with a meaningful share tracing back to drivers following car-oriented navigation tools.

The system lets operators specify detailed vehicle profiles — height, weight, length, width, axle count, and hazmat classifications — and generates routes calculated specifically for those attributes rather than for a generic car. Google also introduced a route token feature ensuring the route planned in the office matches what the driver sees in-cab. A large-vehicle-specific ETA model accounts for the fact that loaded trucks move differently than passenger cars.

The critical caveat is that LVR launched as a set of developer tools, not a free consumer app. Software developers at fleet management companies, TMS providers, and telematics firms will integrate Google's truck-aware routing into the products they sell to carriers. Individual owner-operators will encounter LVR indirectly through their existing navigation or dispatch products. Even the best truck-aware routing depends on the quality and currency of restriction data, and no system replaces a driver's own professional judgment.