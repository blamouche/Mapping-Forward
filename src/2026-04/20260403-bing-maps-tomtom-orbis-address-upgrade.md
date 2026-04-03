# Microsoft's Bing Maps Receives Its Largest Address Data Upgrade in Years via TomTom Orbis
**Source**: https://www.neowin.net/news/microsofts-bing-maps-receives-its-largest-address-data-upgrade-in-years/
**Date**: 2026-04-03
**Author**: Neowin Editorial
**Keywords**: Bing Maps, TomTom Orbis, address data, Overture Maps Foundation, Microsoft, Azure Maps

## Elevator pitch
Microsoft has completed a global rollout of TomTom Orbis address data in Bing Maps, delivering its largest address data upgrade in years through a nine-month phased deployment.

## Takeaways
- Microsoft completed the worldwide rollout of TomTom Orbis Maps address data in Bing Maps
- The rollout began in Europe in June 2025 and took nine months to complete globally
- TomTom Orbis uses the Overture Maps Foundation standard, combining OpenStreetMap, partner data, and TomTom proprietary data
- A phased approach ensured quality: each region was validated before going live
- Improvements are visible in Bing Maps, Bing Search, Copilot, and Azure Maps APIs

## Synthesis
Microsoft has finished a major upgrade to Bing Maps' address data layer, completing a nine-month global rollout of TomTom Orbis Maps address information. This represents the most significant address data improvement for Bing Maps in recent years, and reflects the deepening strategic partnership between Microsoft and TomTom that spans Bing Maps, Azure Maps, and Microsoft 365.

TomTom Orbis Maps is built on the Overture Maps Foundation standard — an open mapping initiative backed by Amazon, Meta, Microsoft, and TomTom. The Orbis data layer aggregates multiple sources: OpenStreetMap community data, partner datasets, TomTom's proprietary sensor observations, and Overture Foundation releases. The result is a continuously updated address dataset that goes beyond periodic bulk updates to reflect real-world changes in near-real-time.

The deployment strategy was deliberately phased. Rather than replacing all address data simultaneously, Microsoft's Bing team validated each regional dataset by comparing coverage rates, positional accuracy, and unexpected side effects against the existing baseline. Only regions where the new data met or exceeded the existing quality threshold were migrated to production. This cautious approach minimized service disruption risk for a platform relied upon by millions of Bing users, Azure developers, and Copilot integrations.

The practical benefits for end users include more accurate location results in Bing Search and Maps queries, improved Copilot responses to location-based questions, and enhanced geocoding accuracy for Azure Maps API consumers. Developers building on Azure Maps should see improvements in address search, reverse geocoding, and point-of-interest resolution.

This upgrade is significant from an industry perspective because it illustrates how the Overture Maps Foundation's open data standard is enabling large-scale, production-grade map data improvements at Microsoft scale — validating the commercial viability of community-anchored mapping data models.
