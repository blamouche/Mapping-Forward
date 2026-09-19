# Overture's August Release Shows Open Maps Becoming Data Infrastructure

**Source**: https://geoawesome.com/overture-august-release-open-map-data-infrastructure/
**Date**: 2026-09-18
**Author: Aleks Buczkowski / Geoawesome
**Keywords**: Overture Maps, open data, GeoParquet, PMTiles, data infrastructure, AI agents, schema, conflation, addresses, buildings, transportation

## Elevator pitch
Overture Maps Foundation's August 2026 release (2026-08-19.0) shows open map data evolving into governed, machine-ready infrastructure with 472.8 million address records, schema transitions for AI consumption, and quality controls that prioritize deduplication over raw feature accumulation.

## Takeaways
- Release 2026-08-19.0 uses schema version 1.18.0, distributed via GeoParquet, PMTiles, and cloud-hosted registries
- Approximately 472.8 million candidate address records, with new data from Fresno County, Statistics Canada, Land Information New Zealand, and Italy's ICAR system
- Base dataset: infrastructure features up 1.8% to ~155.5 million, land features up 1.6% to 75.6 million
- Building count fell 0.6% to ~2.53 billion despite millions of new contributions — illustrating that conflation and deduplication matter more than raw accumulation
- Places dataset declined 0.8%, with quality controls removing duplicate/contradictory features
- Transportation: ~497,000 TomTom road segments and ~1.3 million OpenStreetMap segments added, with improvements to surface, class, and access restriction attributes
- Schema transition: deprecated `categories` field replaced by `basic_category` and `taxonomy`, with one transitional release before removal in September
- Base, buildings, divisions, places, and transportation themes are generally available; addresses remain alpha

## Synthesis
The August release marks Overture's maturation from an open data project into governed spatial infrastructure. The counterintuitive finding — fewer buildings and places despite more contributions — demonstrates that quality controls (conflation, deduplication, filtering) are becoming the primary value driver, especially for AI agent consumption where contradictory features cause more harm than missing ones. The schema transition from `categories` to structured `basic_category`/`taxonomy` fields signals Overture's focus on machine-readability.