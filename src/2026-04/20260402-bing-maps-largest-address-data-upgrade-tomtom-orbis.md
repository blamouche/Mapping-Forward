# Bing Maps Receives Its Largest Address Data Upgrade in Years
**Source**: https://www.neowin.net/news/microsofts-bing-maps-receives-its-largest-address-data-upgrade-in-years/
**Date**: April 2, 2026
**Author**: Unknown
**Keywords**: Bing Maps, TomTom Orbis, address data, Microsoft, geospatial, mapping

## Elevator pitch
Microsoft has completed the global rollout of TomTom Orbis Maps address data in Bing Maps, marking the service's largest address data upgrade in years after a nine-month phased deployment.

## Takeaways
- Microsoft completed a nine-month global rollout of TomTom Orbis Maps address data in Bing Maps, starting in Europe in June 2025
- The upgrade brings three key improvements: broader global coverage, higher positional accuracy, and a continuous update model
- TomTom Orbis Maps is built on the Overture Maps Foundation common standard, combining OSM, partner data, sensor observations, and TomTom's own data
- Microsoft used a phased approach — loading and benchmarking data per region before promoting to production — to avoid service degradation
- The improvements apply across Bing Maps, Bing Search, Copilot, and Azure Maps APIs

## Synthesis
Microsoft has completed one of the most significant overhauls to Bing Maps' address data layer in recent history. After nine months of gradual global rollout — beginning in key European markets in June 2025 — the company has fully deployed TomTom Orbis Maps address data worldwide.

The new data layer is built on TomTom Orbis Maps, which follows the common map standard developed by partners of the Overture Maps Foundation. This means the underlying dataset draws from multiple authoritative sources: the Overture Maps Foundation, OpenStreetMap, commercial partner data, sensor-derived observations, and TomTom's proprietary data. This multi-source approach is designed to improve both breadth and freshness of geographic information.

Microsoft cited three core improvements resulting from the upgrade. First, global coverage has expanded — the number of available address points worldwide has grown substantially. Second, positional accuracy has improved, with address points now placed closer to their real-world geographic locations. Third, the system now operates on a continuous update model rather than relying on periodic bulk refreshes, meaning the data is better positioned to reflect real-world changes in near real time.

Rather than replacing the entire address database simultaneously, Microsoft employed a careful phased methodology. For each targeted region, the team loaded and indexed the new TomTom address data, then benchmarked it against the existing dataset across three dimensions: address coverage, query resolution success rate, and positional accuracy. Only when the new data met or exceeded the quality bar did the team promote it to production. Europe was prioritized first, as it offered the greatest improvement in data density and completeness.

The rollout extends beyond Bing Maps proper. Users of Bing Search and Copilot will benefit from improved location-resolution results, and developers using Azure Maps APIs will see enhanced accuracy and completeness in map query responses.

Microsoft indicated that this is only the first phase of the Orbis integration. The company stated it will continue collaborating with TomTom to incorporate additional Orbis data layers and further refine address quality over time.
