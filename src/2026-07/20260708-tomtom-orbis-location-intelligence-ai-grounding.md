# Orbis: Making Location Intelligence Accessible — TomTom Grounds AI in Real-World Map Data
**Source**: https://www.tomtom.com/newsroom/behind-the-map/orbis-powers-the-next-phase-of-intelligent-tech
**Date**: 2026-07-08
**Author**: TomTom
**Keywords**: TomTom, Orbis, Overture Maps, GERS, GeoParquet, AI grounding, location intelligence, Global Entity Matcher, GEM, MCP Server, agentic AI

## Elevator pitch
TomTom's Orbis platform evolves into an AI-ready location data layer, adding GeoParquet delivery, stable GERS identifiers, a Global Entity Matcher for dataset conflation, and six GA APIs — positioning validated map data as ground truth for AI agents.

## Takeaways
- Orbis developed with Overture Maps Foundation (Meta, Microsoft, Amazon) — a collaborative, open mapping initiative creating a continuously updated global map
- New GeoParquet delivery format enables cloud-native, standardized geospatial data storage directly consumable by AI analytics pipelines
- Stable Global Entity Reference System (GERS) IDs provide persistent unique identifiers for every real-world entity on the map
- TomTom Global Entity Matcher (GEM) automatically aligns organizations' datasets to the shared GERS reference system, reducing conflation effort
- Six generally available APIs (routing, map display, traffic, geocoding, places search, reverse geocoding) with TomTom MCP Server for agentic access
- Orbis serves as validated ground truth data for AI, reducing hallucinations and improving accuracy in location-dependent applications

## Synthesis
TomTom is positioning Orbis as the foundational ground truth data layer for the age of AI, expanding its mapping platform beyond traditional navigation use cases into AI grounding, cloud analytics, and agentic computing. Developed in collaboration with the Overture Maps Foundation — an open mapping initiative backed by Meta, Microsoft, and Amazon — Orbis brings diverse data sources together into a global, continuously updated map.

A key addition is support for GeoParquet, a cloud-native, standardized format for storing and querying geospatial data. This format is directly consumable by AI systems and analytics pipelines, making Orbis data immediately useful in complex data ecosystems. The platform already offered PBF for open-source tooling and FGDB for ArcGIS workflows, with GeoParquet adding cloud analytics and large-scale data processing capabilities.

The Global Entity Reference System (GERS) provides stable, persistent identifiers assigned to each real-world entity on the map. TomTom's Global Entity Matcher (GEM) leverages GERS to significantly reduce conflation effort — automatically matching an organization's datasets to the shared reference system. Once matched, enrichment and adding new datasets become much simpler, addressing a persistent challenge in geospatial data integration.

A set of six generally available APIs covers routing, map display, traffic, geocoding, places search, and reverse geocoding. The TomTom MCP Server exposes the full API portfolio to AI agents and LLM-based interfaces through a single integration, enabling agents to access validated location data that grounds their results in reality. TomTom's strict validation protocols and diligent data maintenance make Orbis a reliable foundation for AI innovation where accuracy is critical, reducing hallucinations and ensuring performance.