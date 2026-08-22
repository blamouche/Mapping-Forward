# Grounding for the age of AI: Orbis powers the next phase of intelligent tech
**Source**: https://www.tomtom.com/newsroom/behind-the-map/orbis-powers-the-next-phase-of-intelligent-tech/
**Date**: 2026-07-08
**Author**: TomTom Editorial Team
**Keywords**: TomTom Orbis, Overture Maps Foundation, GERS, GEM, Global Entity Matcher, GeoParquet, AI location intelligence, conflation, linear referencing, APIs

## Elevator pitch
TomTom expands its Orbis mapping platform with new data formats, interoperability services, and APIs designed to make location intelligence accessible and AI-consumable, positioning Orbis as a reliable ground truth data layer for AI innovation.

## Takeaways
- TomTom Orbis now supports GeoParquet delivery via Orbis OGP, a cloud-native format directly consumable by AI systems
- The Global Entity Matcher (GEM) automatically aligns external datasets to Overture's shared GERS reference system, significantly reducing conflation effort
- GEM uses linear referencing to treat roads as single entities with overlaid attributes (e.g., speed limits), eliminating the need to break roads into segments
- New APIs are in general availability, streamlining how organizations move location data between analytics environments and applications
- Orbis is developed in collaboration with the Overture Maps Foundation, backed by Meta, Microsoft, and Amazon

## Synthesis
TomTom's latest Orbis expansion represents a significant step in making location intelligence accessible and AI-native. The platform, developed in collaboration with the Overture Maps Foundation, now addresses three key challenges facing organizations: processing growing volumes of location data, connecting datasets from different sources, and building applications from that data.

The new Orbis OGP data format supports GeoParquet delivery, a cloud-native, standardized way to store and query geospatial data designed for complex ecosystems and large-scale data processing. This format is directly consumable by AI systems, enabling organizations to integrate location data into analytics pipelines alongside other datasets. The format aligns with the Overture data model and incorporates stable GERS IDs — unique, persistent identifiers assigned to each real-world entity.

Perhaps the most significant innovation is the Global Entity Matcher (GEM), which addresses the perennial challenge of data conflation. Different data sources normally describe the same real-world road, building, or place using different identifiers, requiring manual matching and merging. GEM automates this by aligning datasets to a shared reference system mapped to stable GERS IDs. Once matched, data enrichment and adding new datasets becomes much simpler. GEM also uses linear referencing, treating each road as a single entity with attributes like speed limits overlaid on it, rather than breaking roads into segments.

The new APIs, now in general availability, complete the picture by making it easier to move location data between analytics environments, integration pipelines, and applications. Together, these developments position TomTom Orbis as a comprehensive, AI-ready mapping platform that provides validated ground truth data to reduce AI hallucinations and ensure accuracy in location-based applications.