# Google Maps Killed The Restaurant Star
**Source**: https://hackaday.com/2026/07/20/google-maps-killed-the-restaurant-star/
**Date**: 2026-07-20
**Author**: Navarre Bartz / Hackaday
**Keywords**: Google Maps, restaurant rankings, machine learning, algorithm bias, prominence, Lauren Leek, Open Food Map, London, digital cartography, algorithmic mapping

## Elevator pitch
A machine learning analysis of Google Maps restaurant rankings in London reveals how the platform's "prominence" algorithm creates vicious cycles for new restaurants, amplifies chain dominance, and embeds socioeconomic patterns into culinary cartography—raising questions about who maps decide to make visible.

## Takeaways
- Lauren Leek built a machine learning model to analyze how Google Maps ranks restaurants, uncovering how "prominence"—the third ranking pillar alongside relevance and proximity—favors chains and high-traffic areas
- New restaurants face a vicious cycle: they can't draw traffic without reviews, but can't get reviews without traffic, making algorithmic visibility a barrier to entry
- Google Maps' ranking algorithm amplifies existing socioeconomic patterns: restaurant diversity correlates with where families settled, which high streets remained affordable, and where displacement occurred before culinary ecosystems could mature
- Leek built a public dashboard and open-source project (Open Food Map on GitHub) that identifies "hidden gems"—restaurants that punch above their Google Maps weight
- The analysis extends beyond food to reveal how algorithmic mapping decisions shape economic visibility, with undisclosed paid placements further complicating the ranking landscape

## Synthesis
On July 20, 2026, Hackaday reported on a data analysis project by Lauren Leek that investigates how Google Maps picks winners and losers in the restaurant scene in London. What began as a machine learning model to determine restaurant recommendations uncovered concerning elements of how Google Maps ranks establishments and, by extension, shapes economic visibility in cities.

Google Maps ranks restaurants using three factors: relevance, proximity, and prominence. While relevance and proximity are fairly straightforward, "prominence" is more opaque. Leek found that "it is not just what people think of a place—it is how often people interact with it, talk about it, and already recognise it." This creates a feedback loop where chains and restaurants in high foot-traffic areas accumulate reviews and visibility, while out-of-the-way establishments struggle to attract the initial traffic needed to build a review base. For new restaurants, this means a vicious cycle: they can't draw traffic without reviews, but can't get reviews without traffic.

The analysis revealed that Google Maps' undisclosed paid placements of restaurants in search results further complicate the landscape, adding a commercial layer atop the algorithmic ranking. This means that visibility on Google Maps is not purely a function of quality or popularity, but also of advertising spend—a factor that advantages well-funded chains over independent establishments.

Zooming out, Leek found larger clusters that revealed deeper socioeconomic patterns. Restaurant diversity, she discovered, "is not just about taste. It is about where families settled, which high streets remained affordable long enough for a second generation to open businesses, and which parts of the city experienced displacement before culinary ecosystems could mature." This insight connects algorithmic mapping to urban geography, showing how Google Maps visibility reflects and reinforces historical patterns of settlement, affordability, and displacement.

Leek built a public dashboard where people can sort restaurants in London, designed to identify hidden gems that punch above their Google Maps weight. The project, Open Food Map, is available on GitHub, allowing others to adapt the analysis for their own cities. The work raises broader questions about the role of algorithmic mapping platforms in shaping economic opportunity and urban visibility.