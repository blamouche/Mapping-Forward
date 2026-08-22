# A Dataset for Multiple Structural Representations of Urban Road Maps Across Chinese Cities
**Source**: https://www.nature.com/articles/s41597-026-07790-3
**Date**: 2026-08-05
**Author**: Hong Zhang, Yu Jin
**Keywords**: urban road networks, graph representations, space syntax, complex network analysis, Chinese cities, OpenStreetMap, GIS, topology, urban morphology

## Elevator pitch
A new open-access dataset published in Scientific Data provides four complementary graph representations of urban road networks across 293 Chinese cities, enabling standardized analysis of geometric, topological, semantic, and cognitive properties for urban morphology and network science research.

## Takeaways
- Dataset covers 293 prefecture-level cities and four provincial-level municipalities in China with multiple structural representations of their road networks
- Provides four complementary graph models: segment-based primal graphs, segment-based dual graphs, stroke-based dual graphs, and mixed dual graphs integrating named streets with strokes
- Validation demonstrates high geometric fidelity (R² = 0.991) and 99% topological connectivity retention after processing
- Available in GIS-compatible Shapefile and GraphML formats for integration with standard spatial analysis tools
- Designed for morphological and structural analysis rather than operational traffic modeling requiring lane capacity or signalisation data
- Addresses a gap in existing datasets which rarely provide standardized multi-representational versions of the same road networks

## Synthesis
Published in Scientific Data on August 5, 2026, by Hong Zhang and Yu Jin, this dataset addresses a critical gap in urban network research: the lack of standardized multi-representational versions of road networks that capture different structural properties. While widely used data sources like OpenStreetMap are organized for general geographic representation and navigation, they require significant processing before supporting systematic urban studies.

The dataset provides four complementary graph models, each capturing different aspects of urban road network structure. Segment-based primal graphs represent the traditional approach where intersections become nodes and road segments become edges. Segment-based dual graphs transform this representation by treating road segments as nodes and intersections as edges, emphasizing connectivity patterns. Stroke-based dual graphs group contiguous road segments into "strokes" — continuous paths that share similar directional properties — creating a representation aligned with human cognitive perception of streets. Mixed dual graphs integrate named streets with strokes, combining semantic information (street names) with geometric continuity.

This multi-representational approach is essential because different research questions require different structural perspectives. Geometric properties (lengths, angles) are captured in primal representations, topological properties (connectivity, centrality) in dual representations, semantic properties (street names, hierarchies) in mixed representations, and cognitive properties (how humans perceive and navigate street networks) in stroke-based representations. The dataset thus supports research across urban morphology, spatial cognition, accessibility analysis, space syntax, and complex network analysis.

The validation results are strong: geometric fidelity achieves R² = 0.991 between processed and original networks, and 99% of original connectivity is retained after topological reconstruction. This demonstrates that the simplification and reconstruction processes preserve the essential structural properties of the original road networks while making them suitable for standardized comparative analysis.

The choice of Chinese cities is significant given China's rapid urbanization and the diversity of urban forms across 297 cities. The dataset enables comparative studies of urban road network structure across different city sizes, planning traditions, and geographic contexts within a standardized framework. The availability in both Shapefile and GraphML formats ensures compatibility with both GIS software and network analysis tools.