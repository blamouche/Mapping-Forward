# MapTrace: Scalable Data Generation for Route Tracing on Maps
**Source**: https://arxiv.org/abs/2512.19609
**Date**: 2025-12-22
**Author**: Artemis Panagopoulou, Aveek Purohit, Achin Kulshrestha, Soroosh Yazdani, Mohit Goyal
**Keywords**: map understanding, route tracing, synthetic data, multimodal models, spatial reasoning

## Elevator pitch
MapTrace introduces a scalable synthetic-data pipeline for route tracing on maps, showing that fine-grained spatial reasoning in multimodal models can be substantially improved with targeted supervision.

## Takeaways
- The paper targets route tracing on maps, a task where multimodal LLMs often violate path constraints.
- A synthetic data pipeline generates pixel-accurate path annotations from synthetic map imagery.
- The resulting dataset contains roughly 23k paths across about 4k maps.
- Fine-tuning on this dataset improves MapBench performance and reduces path-tracing error.
- The work argues that spatial reasoning deficits can be explicitly trained rather than assumed to emerge.

## Synthesis
MapTrace tackles a persistent weakness in multimodal large language models: fine-grained spatial reasoning on cartographic imagery. The paper focuses on the route‑tracing task, which asks a model to follow a path on a map without breaking connectivity or violating obvious constraints. While humans can quickly interpret these constraints, many models produce plausible yet incorrect traces, suggesting a gap between general visual-language capability and map-specific spatial understanding.

The authors address this by proposing a scalable synthetic data generation pipeline. Instead of relying on costly manual annotation of paths, the pipeline creates synthetic map images and uses pixel-level parsing to automatically generate precise, dense path annotations. This design is significant for two reasons. First, it creates a controllable environment where path geometries, map styles, and complexity can be varied systematically. Second, it bypasses the bottleneck of human labeling, which is particularly expensive for pixel-accurate routing tasks.

Using this pipeline, the authors construct a dataset of around 23,000 path samples across roughly 4,000 synthetic maps. This volume is large enough to support fine‑tuning at scale, but also small enough to be reproducible by other labs. The dataset enables explicit supervision of how a model should trace routes, rather than hoping the model infers routing behavior from natural images or generic diagram tasks. In effect, MapTrace reframes route tracing as a supervised learning problem with domain-specific training signals.

The evaluation uses MapBench, a benchmark for map-based reasoning tasks. The paper reports that fine‑tuning on MapTrace improves route tracing success rates by up to 6.4 points and reduces NDTW (a path‑matching error metric). These gains are presented as evidence that spatial reasoning deficits can be addressed with targeted synthetic supervision. Importantly, the improvements are measured across both open-source and proprietary multimodal models, suggesting that the benefits are not limited to a particular architecture or vendor.

Beyond the headline numbers, the work has broader implications for geospatial AI. Route tracing is a building block for navigation, map digitization, and human‑in‑the‑loop cartography. If models can be trained to respect path connectivity and spatial constraints, they can assist with tasks like extracting routes from scanned maps, validating navigation datasets, or generating synthetic navigation scenarios for simulation. The pipeline’s synthetic nature also allows for domain shifts—testing how models handle different map styles, scales, or symbol conventions.

The paper positions its contribution as a bridge between data scarcity and model capability. It argues that the primary obstacle is not model capacity, but the lack of high-quality, pixel‑accurate supervision for map tasks. By providing a scalable data generator, MapTrace offers a template for other map‑related tasks that suffer from similar annotation bottlenecks. In that sense, the paper is as much about data infrastructure as it is about model performance.

Overall, MapTrace demonstrates that fine‑grained spatial reasoning can be engineered through carefully designed data pipelines. For mapping practitioners, the takeaway is clear: improvements in geospatial AI may hinge less on new architectures and more on domain‑specific datasets that encode the rules and constraints of maps themselves.
