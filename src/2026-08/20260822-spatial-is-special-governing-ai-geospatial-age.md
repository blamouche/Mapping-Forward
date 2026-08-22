# Spatial Is Special, Governing AI in the Geospatial Age
**Source**: https://www.geoweeknews.com/articles/spatial-is-special-governing-ai-in-the-geospatial-age/
**Date**: August 22, 2026
**Author**: Abigail Hart, Geo Week News
**Keywords**: Overture Maps, AI governance, spatial data, geospatial AI, data provenance, auditability, Amy Rose, conflation, fitness for use

## Elevator pitch
Overture Maps CTO Amy Rose argues that spatial data requires special governance in AI systems — distinct from non-spatial data — because scale, precision, proximity, boundaries, and derived location add complexity layers that most AI users aren't accounting for.

## Takeaways
- Amy Rose, CTO at Overture Maps, reversed her earlier stance that "spatial is not special" when it comes to AI governance
- Spatial data introduces unique governance challenges: scale, precision, proximity, boundaries, and derived location
- The core problem is that users assume AI models have knowledge of the data's provenance, fitness for use, and validity of combining datasets
- A practical governance framework must account for the entire decision chain: data provenance, intended purpose, limitations, license, and access restrictions
- Overture's Global Entity Reference System addresses the "conflation tax" — the cost of reconciling different datasets referencing the same real-world entities

## Synthesis
Amy Rose's evolution from arguing that "spatial is not special" to concluding that "spatial really is special" in the context of AI governance reflects a growing awareness in the geospatial community. While isolating spatial data from mainstream technology limits its reach, treating it like any other dataset in an AI pipeline is a recipe for unreliable results, unintended privacy violations, and decisions no one can audit.

The core governance challenge is that spatial data introduces dimensions absent from tabular data: scale, precision, proximity, boundaries, and derived location. When location data enters an AI system, users make assumptions about fitness for use, data provenance, and the validity of combining different datasets — assumptions that may be incorrect and are often unauditable. Rose offers a concrete example: an organization might legitimately access high-resolution imagery, insurance data, and property records each for separate purposes, but if an AI system cross-references them to identify properties for insurance policy changes, it combines data in ways that violate the terms of each individual access.

A practical governance framework, Rose argues, must go beyond access control to account for the entire decision chain — where data came from, its intended purpose, limitations, license, and access restrictions. Overture Maps is trying to solve part of this through its Global Entity Reference System, which addresses the "conflation tax" — the cost of reconciling different datasets that reference the same real-world entities. The gap between "AI-ready" and "AI-trustworthy" remains stubbornly wide, and closing it requires governance frameworks built specifically for the spatial domain.