# A Tutorial on GeoAI: Designing Footprint Extraction from NAIP Imagery Using U-Net, Grounding DINO, SAM, and Mask R-CNN
**Source**: https://www.marktechpost.com/2026/08/02/a-tutorial-on-geoai-designing-footprint-extraction-from-naip-imagery-using-u-net-grounding-dino-sam-and-mask-r-cnn/
**Date**: 2026-08-02
**Author**: Sana Hassan, MarkTechPost
**Keywords**: GeoAI, building footprint extraction, NAIP imagery, U-Net, ResNet-34, Grounding DINO, SAM, Mask R-CNN, Overture Maps, Microsoft Planetary Computer, deep learning, remote sensing

## Elevator pitch
A comprehensive GeoAI tutorial walks through building a complete pipeline for extracting building footprints from high-resolution NAIP aerial imagery, training a U-Net model, and comparing it with zero-shot segmentation using Grounding DINO and SAM, plus instance segmentation with Mask R-CNN, integrating Overture Maps labels.

## Takeaways
- The tutorial designs a complete GeoAI workflow for extracting building footprints from high-resolution NAIP (National Agriculture Imagery Program) aerial imagery
- Uses a U-Net model with a ResNet-34 encoder for semantic segmentation, with sliding-window inference applied to unseen scenes
- Compares semantic segmentation results with zero-shot segmentation using Grounding DINO and SAM (Segment Anything Model)
- Also compares with a pretrained Mask R-CNN instance segmentation model for benchmarking
- Pipeline includes converting predicted masks into cleaned and regularized building polygons, with IoU and F1 metric evaluation
- Demonstrates extension to real-world areas using NAIP imagery from Microsoft Planetary Computer and building labels from Overture Maps
- Uses the geoai-py library with segmentation-models-pytorch and buildingregulariser packages

## Synthesis
Published on MarkTechPost on August 2, 2026, by Sana Hassan, this tutorial provides a comprehensive, hands-on guide to building footprint extraction from aerial imagery — a fundamental GeoAI task with applications in urban planning, disaster response, and map data creation.

The tutorial covers the complete deep learning pipeline from data preparation through model evaluation. It begins by configuring the geospatial deep learning environment, downloading NAIP raster imagery and vector building labels, and inspecting their spatial properties. The data preparation step generates georeferenced image chips and segmentation masks suitable for training. The primary model architecture is a U-Net with a ResNet-34 encoder, a well-established choice for semantic segmentation tasks that benefits from transfer learning through the pre-trained encoder.

The tutorial goes beyond a single approach by comparing three different AI strategies. The U-Net semantic segmentation approach is the baseline, producing binary masks of building footprints. Grounding DINO combined with SAM offers a zero-shot alternative — Grounding DINO detects buildings from text prompts, and SAM segments them precisely without requiring training data. Mask R-CNN provides instance segmentation, detecting and segmenting individual buildings as distinct objects. This comparison is valuable for practitioners who need to choose the right approach for their use case.

A critical step in the pipeline is converting predicted raster masks into vector polygons suitable for GIS use. The tutorial uses the buildingregulariser package to clean and regularize building polygons, transforming rough segmentation outputs into geometrically clean building footprints. Evaluation uses Intersection over Union (IoU) and F1 metrics, providing standard benchmarks for comparing model performance.

The tutorial's real-world extension is particularly noteworthy. By using NAIP imagery from Microsoft Planetary Computer and building labels from Overture Maps, the pipeline demonstrates how open data infrastructure and deep learning can be combined at scale. The Overture Maps Foundation's building footprint data serves both as training labels and as a validation reference, highlighting the foundation's growing role as a data source for GeoAI research and applications.