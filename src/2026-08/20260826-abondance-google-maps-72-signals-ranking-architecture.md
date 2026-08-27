# Dans les coulisses de Google Maps : 72 signaux de ranking et l'architecture derrière la recherche locale
**Source**: https://www.abondance.com/20260826-2829709-google-maps-72-signaux-ranking-architecture.html
**Date**: 2026-08-26
**Author**: Olivier De Segonzac (Abondance / Resoneo)
**Keywords**: Google Maps, Geostore, Oyster Rank, local SEO, ranking signals, Knowledge Graph, Webref, GConcepts, retrieval pipeline

## Elevator pitch
A reverse-engineered Google binary exposes Geostore — the system behind Google Maps entities — revealing 72 ranking signals, 793 data providers, and an architecture connecting Maps to the Knowledge Graph and the broader web.

## Takeaways
- Google's Geostore builds a canonical representation of each place from 793 data providers, with conflation mechanisms to resolve conflicting sources — not just a single Google Business Profile listing.
- The Oyster Rank system uses 72 named ranking signals including reviews, query volume, listing impressions, directions requests, Wikipedia signals, and road segment usage (25 are deprecated).
- The 72 signals are not "the Google Maps algorithm" — additional systems handle query understanding, semantic matching, candidate generation, geographic retrieval, and reranking in a multi-stage pipeline.
- Geographic search does not use a fixed radius: the candidate area adapts to query density and the user's environment. Removing geographic weighting shifts median result distance from 6.87 km to over 4,000 km while preserving ranking order, suggesting geography changes retrieval, not just reranking.
- Maps and web search are connected through Knowledge Graph MIDs and the Webref layer, which associates web documents with entities — a store locator page is not just a search result, it is evidence about the entity itself.

## Synthesis
This investigation by Resoneo deconstructs the widely held notion that Google Maps listings are simply the product of a visible algorithm applied to Google Business Profile data. By reverse-engineering a recent Google binary and cross-referencing it with the 2024 Google leak, network traffic from Maps, and other internal components, the authors uncovered the scope of Geostore — Google's internal system for representing geographic entities.

Geostore stores Features (establishments, buildings, roads, cities, even 3D objects) that aggregate identity, geometry, categories, Knowledge Graph references, and ranking information from 793 data source providers. Each attribute of a place — name, phone, category, geometry — can come from a different provider, with mechanisms for priority, trust, and conflation when sources disagree. This explains why corrections made in Google Business Profile sometimes revert: the edit becomes one piece of evidence in a system that may already hold contradictory data from other trusted sources.

The ranking system, called Oyster Rank, contains 72 named signals. While SEOs will naturally focus on this list, the article stresses that these signals feed only one stage of a broader pipeline. A simplified view runs from Geostore entity through query understanding, semantic matching, candidate generation, geography and quality filtering, reranking, and final results. An additional offline scorer runs on the phone itself, using 8 signals across 13 tiers, entirely separate from both Oyster Rank and server-side Places ranking.

The geographic layer proved particularly revealing. Testing showed that the search radius is not fixed — it adapts to query density and the local environment. A search for "pharmacie" in dense Paris yields a much smaller candidate area than the same search in a rural zone. When geographic weighting was removed across 5,083 queries and 86,584 results, median distance jumped from 6.87 km to over 4,000 km, yet the non-geographic ranking remained stable — indicating that geography shapes what is retrieved, not merely how results are sorted.

Perhaps the most strategic finding is the connection between Maps and the web through Knowledge Graph MIDs and the Webref layer. Web documents can be associated with entities, and the system tracks topicality, confidence, and document type (author page, publisher page, reference page). This means a store locator page functions not just as a potential search result but as evidence about the entity it describes — linking local SEO and web SEO in ways the separate interfaces do not suggest. The article also reveals Google's use of GConcepts, a shared semantic vocabulary extending far beyond the visible primary category on a Business Profile, covering cuisines, service modes, attributes, and more.

The authors published an archive of 10,936 Geostore declarations, searchable by message name, field type, documentation, and tag number, enabling the SEO community to trace claims back to source evidence rather than relying on circulating theories.