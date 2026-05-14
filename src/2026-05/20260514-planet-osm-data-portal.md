# Planet OSM — The OpenStreetMap Data Portal
**Source**: https://planet.openstreetmap.org/
**Date**: May 14, 2026 (continuously updated)
**Author**: OpenStreetMap Foundation
**Keywords**: OpenStreetMap, OSM, planet file, open data, ODbL, PBF, GIS data, weekly export

## Elevator pitch
Planet OSM is the official portal providing weekly complete copies of the entire OpenStreetMap database — a 161 GB XML file covering the world's largest crowdsourced geographic dataset, freely available under the Open Database License.

## Takeaways
- The complete weekly planet file is 161 GB (XML) or 86 GB (PBF format), with a separate 7.8 GB changesets file tracking all modifications.
- The data is now licensed under the Open Data Commons Open Database License (ODbL) 1.0, with older files under CC-BY-SA 2.0.
- Key processing tools include Osmosis for format conversion and Osm2pgsql for importing into PostGIS databases for map rendering.
- Users who don't need the full planet can use country/state extracts from third parties like GeoFabrik and BBBike.
- OSM operates entirely on donations and volunteers; the page actively encourages annual contributions and corporate memberships to sustain infrastructure.

## Synthesis
The Planet OSM page serves as the definitive data distribution point for OpenStreetMap, the crowdsourced geographic database that has become essential infrastructure for countless mapping applications worldwide. Every week, a complete snapshot of all OSM data is published as both a compressed XML file (161 GB) and a Protocol Buffers (PBF) format file (86 GB), along with a separate changesets file (7.8 GB) containing complete metadata for all modifications.

The infrastructure behind this data distribution reflects the scale and maturity of the OSM project. The replication system updates minutely, and the page provides access to historical data, deleted user information, GPS traces, and statistics — a comprehensive archive of the project's evolution. The practical guidance acknowledges that the full planet file is impractically large for many use cases, pointing users to third-party extract services like GeoFabrik.de and BBBike.org that provide country- and state-level subsets with up-to-date worldwide coverage.

The licensing framework has evolved significantly: data published before September 2012 remains under Creative Commons Attribution-ShareAlike 2.0, while all subsequent data uses the Open Data Commons Open Database License 1.0 — a shift that reflected the community's understanding of how geographic data is used in practice. The page also provides clear guidance on tools: Osmosis for general-purpose command-line data conversion, Osm2pgsql for importing into PostGIS databases for rendering, and processed coastline data available separately as a dependency for usable map production.

The sustainability message is notably direct. Despite being free to use, OSM data "is not free to make or host." The page requests annual recurring donations from individual users and directs large businesses generating significant revenue from OSM data to join as corporate members of the OpenStreetMap Foundation. This framing positions Planet OSM not just as a download portal but as a reminder of the volunteer-driven, donation-dependent infrastructure underlying one of the world's most important open data projects.
