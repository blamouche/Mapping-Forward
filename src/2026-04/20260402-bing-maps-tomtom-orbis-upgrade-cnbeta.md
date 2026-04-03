# 必应地图迎来最大规模地址数据升级 引入 TomTom Orbis全球数据集
**Source**: https://www.cnbeta.com.tw/articles/tech/1556284.htm
**Date**: April 2, 2026
**Author**: Unknown
**Keywords**: Bing Maps, TomTom Orbis, 地址数据, Microsoft, Overture Maps, Azure Maps, 地图升级

## Elevator pitch
Microsoft completed its largest-ever address data upgrade for Bing Maps, deploying TomTom Orbis Maps data globally over nine months with improvements in coverage, positional accuracy, and continuous real-time updates.

## Takeaways
- Microsoft completed its nine-month global deployment of TomTom Orbis Maps address data in Bing Maps, starting June 2025
- TomTom Orbis Maps integrates data from Overture Maps Foundation, OpenStreetMap, partner data, sensor observations, and TomTom's own data
- The upgrade delivers three main improvements: broader coverage, higher positional accuracy, and a continuous update model
- Microsoft used a staged approach — benchmarking new vs. old data on coverage, query resolution, and accuracy before going live per region
- Improvements extend to Bing Search, Copilot map features, and Azure Maps API results

## Synthesis
Microsoft announced the completion of its largest address data upgrade to Bing Maps in recent years, finalizing the global rollout of TomTom Orbis Maps address data after a nine-month process that began in June 2025. This update represents a significant shift in the underlying data infrastructure powering Microsoft's location services.

TomTom Orbis Maps is built on the common map standard developed in collaboration with the Overture Maps Foundation, a cross-industry initiative. The dataset integrates multiple authoritative sources: Overture Maps Foundation data, OpenStreetMap (OSM), commercial partner data, sensor-derived observations, and TomTom's proprietary geographic data. This multi-source architecture aims to provide both comprehensive coverage and reliable accuracy at a global scale.

Microsoft highlighted three core benefits of the new address layer. First, global coverage has expanded significantly, with a notable increase in the total number of addressable points. Second, positional accuracy has improved, with addresses now placed closer to their true geographic coordinates. Third, the system adopts a continuous update model, ensuring that data reflects real-world changes much faster than previous periodic bulk-refresh approaches.

The implementation followed a carefully staged strategy rather than a single global switch. For each region, Microsoft's team first loaded and indexed the new TomTom address data, then compared it against the existing dataset on three dimensions: address coverage, query parsing success rate, and positional accuracy. Data was only promoted to production when it met or exceeded the established quality standards. Europe was addressed first, given the highest data density and completeness gains there.

The upgraded address data is now live across multiple Microsoft location services, including Bing Maps, Bing Search, and Copilot map features. Azure Maps API users will also benefit from improved accuracy and completeness in map query responses. Microsoft indicated the collaboration with TomTom will continue to integrate additional Orbis data layers and refine address quality further.
