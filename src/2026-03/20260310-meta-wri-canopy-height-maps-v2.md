# Mapping the World's Forests with Greater Precision: Introducing Canopy Height Maps v2
**Source**: https://ai.meta.com/blog/world-resources-institute-dino-canopy-height-maps-v2/
**Date**: March 10, 2026
**Author**: Meta AI
**Keywords**: canopy height maps, DINOv3, forest monitoring, satellite imagery, carbon storage, forest restoration, Meta AI, World Resources Institute

## Elevator pitch
Meta and the World Resources Institute release Canopy Height Maps v2, an open-source model using DINOv3 self-supervised vision AI to measure global forest structure with dramatically improved accuracy.

## Takeaways
- CHMv2 improves the R² prediction accuracy metric from 0.53 to 0.86, representing a substantial reliability gain
- The system uses DINOv3, a self-supervised vision model trained on diverse satellite imagery without labeled data
- Key improvements include better measurement of tall trees with reduced bias and a geographically diverse training dataset
- Practical users include Forest Research UK, the European Commission's Joint Research Centre, and US cities for urban cooling planning
- The tool is open-source, enabling broad deployment for forest management, carbon accounting, and biodiversity monitoring

## Synthesis
Meta AI and the World Resources Institute's release of Canopy Height Maps v2 demonstrates how self-supervised vision models can transform scientific measurement at global scale. The core achievement is a near-doubling of prediction accuracy — from R² 0.53 to 0.86 — using a model architecture designed to learn from unlabeled data rather than requiring expensive hand-annotated training sets.

DINOv3's approach is methodologically significant. Rather than learning to recognize forests from labeled examples (this is a 30-meter tree, this is a 5-meter shrub), the model learns robust visual features by analyzing patterns across enormous quantities of satellite imagery without explicit supervision. The result is a feature extractor that understands shadows, textures, and crown shapes well enough to predict canopy height with accuracy approaching that of expensive lidar surveys.

The bias reduction for tall trees addresses a specific failure mode of the previous version. Large, old-growth trees — which store disproportionate amounts of carbon and provide critical biodiversity habitat — were systematically underestimated in CHMv1. Correcting this bias is not merely a statistical improvement; it has direct implications for carbon accounting accuracy and forest management decisions in high-value conservation areas.

The real-world applications cited span governance levels. Forest Research UK is using the tool for national inventory monitoring — a function traditionally requiring expensive field surveys. The European Commission's Joint Research Centre incorporated it into the Global Forest Cover map supporting the 3 Billion Tree Initiative — a policy commitment with significant economic and ecological implications that requires accurate verification data. US cities are applying it to urban heat island analysis, where tree canopy coverage directly affects temperature and energy costs.

The open-source release strategy reflects a deliberate choice to maximize social impact through broad adoption rather than commercial restriction. By making CHMv2 freely available, Meta and WRI enable deployment by national governments, NGOs, and research institutions worldwide — organizations that would not have the resources to develop equivalent tools independently but can apply them immediately at scale.
