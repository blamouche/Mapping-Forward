# Why Interoperability Remains a Bottleneck in Geospatial Technology
**Source**: https://www.geoweeknews.com/news/why-interoperability-remains-a-bottleneck-in-geospatial-technology
**Date**: May 20, 2026
**Author**: Abigail Hart
**Keywords**: interoperability, geospatial, data formats, STAC, OGC, ArcGIS, QGIS, cloud-native, open standards

## Elevator pitch
Despite unprecedented geospatial capabilities — daily satellite imagery, AI-powered change detection — interoperability between platforms and data formats remains a critical bottleneck that slows workflows, inflates costs, and delays insights for the organizations that need them most.

## Takeaways
- The geospatial ecosystem is highly fragmented across proprietary platforms (Esri ArcGIS), open-source tools (QGIS), and cloud services (Google Earth Engine, Microsoft Planetary Computer), each with incompatible formats.
- Open standards from the OGC have made genuine progress but adoption is uneven, and newer data types like point clouds and real-time sensor feeds have outpaced standardization.
- Platform lock-in is commercially incentivized, making interoperability a feature gap by design rather than accident.
- The human cost is real: climate scientists and under-resourced organizations can spend more time wrangling data formats than doing actual analysis.
- Cloud-native formats and STAC-compliant catalogs represent meaningful progress, but stronger government mandates and better low-code translation tooling are still needed.

## Synthesis
Abigail Hart's piece for Geo Week News examines why interoperability — the ability of different geospatial software, platforms, and data formats to work together seamlessly — remains stubbornly difficult despite decades of standards work and an explosion in technical capability.

The core problem is fragmentation. The geospatial world is built on accumulated tools and proprietary platforms, each with real strengths but walled off from one another. Esri's ArcGIS dominates enterprise GIS, QGIS leads in open source, and cloud platforms like Google Earth Engine and Microsoft Planetary Computer offer their own ecosystems and services. Drone manufacturers and lidar vendors bundle proprietary formats. Moving data between these environments demands constant conversion, projection reconciliation, and quality checks at every handoff. The result is that organizations maintain parallel workflows, duplicate data, or restrict their analyses to whatever fits within a single platform.

Hart acknowledges that standards work has not been absent. The Open Geospatial Consortium (OGC) has spent decades developing open standards with genuine progress, but adoption is uneven. Newer data types — point clouds, real-time sensor feeds — have outpaced standardization, and proprietary formats rush to fill the gaps. There is also a commercial dimension: platform lock-in is, for many vendors, a feature rather than a bug, as it creates switching costs and customer retention.

The article then shifts to the human cost of this technical friction. A climate scientist combining NOAA oceanographic data with land use records, census demographics, and field observations may be working across five different formats before any analysis can begin. For under-resourced organizations doing climate resilience or environmental justice work, the time spent wrangling data is time not spent engaging with communities. The stakes are not abstract — they translate directly into slower disaster response, delayed climate adaptation planning, and missed opportunities for evidence-based advocacy.

Hart finds reasons for optimism in cloud-native formats and the growing adoption of STAC (SpatioTemporal Asset Catalog) by major data providers including NASA, USGS, and Microsoft. STAC-compliant catalogs make cross-archive discovery increasingly practical. However, she notes that STAC is a metadata standard — it does not solve incompatible processing environments or vector-raster integration challenges.

The article concludes with practical recommendations: stronger government mandates for open-format data delivery in publicly funded projects, greater institutional investment in translation infrastructure, and better low-code tooling that abstracts format complexity for non-specialists without hiding it entirely. The bottom line is that interoperability work generates no headlines compared to new satellites or AI breakthroughs, but it is the connective tissue that determines whether all that capability can actually reach the climate scientist, the emergency manager, or the community organizer trying to understand what rising seas mean for their neighborhood.
