# Brave Place Search API: The Google Maps Alternative That Costs 6–7x Less
**Source**: https://brave.com/blog/place-search-improved/
**Date**: 2026-07-08
**Author**: Brave
**Keywords**: Brave, Place Search API, Google Maps alternative, POI, points of interest, maps API, cost comparison, location search

## Elevator pitch
Brave releases an improved Place Search API with ~200 million POIs worldwide at $5 per 1,000 requests — 6 to 7 times cheaper than Google Maps — while matching or exceeding Google on recall in real-world tests.

## Takeaways
- Single endpoint API accessing ~200 million points of interest worldwide, powering Brave Search's map with over 2.2 billion queries per month
- Flat pricing at $5 per 1,000 requests with all fields included, versus Google's $32–$35 per 1,000 with tiered SKU-based pricing
- Brave leads on recall (7.2 vs 6.8) — returns more places that actually exist; Google leads on precision (8.2 vs 6.2)
- Returns rich data: name, coordinates, address, ratings, hours, photos, price range, categories, distance
- Use cases include "near me" discovery, travel guides, business directories, map dashboards, and geofenced nudges

## Synthesis
Brave's improved Place Search API positions itself as a serious competitor to Google Maps for place discovery, combining competitive quality with dramatically lower costs. The API draws from an index of approximately 200 million points of interest worldwide and serves as the backbone of place search in Brave Search, which handles over 2.2 billion queries monthly.

The pricing gap is significant: Brave charges a flat $5 per 1,000 requests with every field included (ratings, hours, photos), while Google's comparable Text/Nearby Search costs $32–$35 per 1,000 with tiered SKU-based pricing and field masks that can push costs higher. Each Brave plan also includes $5 in free monthly credit.

Quality benchmarks across 1,000 test queries show the two services trading strengths. Brave's overall quality score of 7.3 slightly exceeds Google's 6.4. Brave leads on recall (7.2 vs 6.8), meaning it returns more of the places that actually exist — particularly for ambiguous names and street-level queries. Google maintains an edge on precision (8.2 vs 6.2), floating the most relevant results to the top more reliably for category-based searches like "kebab near me."

The API returns comprehensive metadata per place including coordinates, postal address, ratings, review counts, opening hours, phone, email, timezone, photos, and distance from search center. Developer integration is straightforward with a single REST endpoint, making it suitable for apps and AI agents needing location-aware place discovery without licensing a full maps stack.