# Fast, accurate water body extraction for Reality Mapping using SAM3
**Source**: https://www.esri.com/arcgis-blog/products/arcgis-pro/3d-gis/fast-accurate-water-body-extraction-for-reality-mapping-using-sam3
**Date**: 2026-04-17
**Author**: Ashleigh Sier
**Keywords**: Esri, reality mapping, SAM3, segmentation, water extraction

## Elevator pitch
Esri shows how foundation-model segmentation can turn water-body extraction from a laborious preprocessing task into a scalable step in reality-mapping production.

## Takeaways
- Esri’s blog post presents water-body extraction as one of the persistent weak points in reality-mapping workflows and positions the SAM3 foundation model as a practical answer.
- The workflow described is relatively straightforward: after image alignment, imagery is exported into an optimized raster format, then processed with the Detect Objects Using Deep Learning tool using a prompt such as “water, lake, river, dam, creek.” SAM3 returns polygon features that can be cleaned via buffering, raster conversion, and polygon simplification.
- What makes the post interesting is its production framing.
- The strategic implication is broader than water polygons.
- Overall, the article illustrates how foundation models are being absorbed into industrial GIS workflows as utility components.

## Synthesis
Esri’s blog post presents water-body extraction as one of the persistent weak points in reality-mapping workflows and positions the SAM3 foundation model as a practical answer. Water is difficult because of reflections, low texture, and seasonal variability, which can produce noise and artifacts in reconstruction. The article argues that natural-language-driven segmentation can simplify this work dramatically compared with older classification pipelines that required training samples, class definitions, and more manual tuning.

The workflow described is relatively straightforward: after image alignment, imagery is exported into an optimized raster format, then processed with the Detect Objects Using Deep Learning tool using a prompt such as “water, lake, river, dam, creek.” SAM3 returns polygon features that can be cleaned via buffering, raster conversion, and polygon simplification. The message is not that post-processing disappears, but that the most tedious and error-prone part of water extraction becomes more automated and more repeatable.

What makes the post interesting is its production framing. Esri is not presenting SAM3 as a demo or research toy. The article specifies dataset size, resolution, GPU hardware, batch size, and runtime on a 50 km² Stuttgart project. The stated ten-hour run on an RTX 4090 is long enough to be realistic, but still framed as operationally acceptable in a weekend production cycle. That makes the piece feel less like a conceptual argument for AI and more like a practical blueprint for imagery teams.

The strategic implication is broader than water polygons. By showing that a foundation model can be inserted into a classic geospatial workflow with limited user friction, Esri is reinforcing a larger shift in GIS tooling: domain operators increasingly guide AI with prompts instead of building bespoke models from scratch. In reality mapping, that means more preprocessing steps can become semi-automated without sacrificing output quality.

Overall, the article illustrates how foundation models are being absorbed into industrial GIS workflows as utility components. The value is not just better segmentation. It is the reduction of manual setup, the improvement of consistency across large project areas, and the ability to turn previously tedious cartographic cleanup into a more scalable production step.
