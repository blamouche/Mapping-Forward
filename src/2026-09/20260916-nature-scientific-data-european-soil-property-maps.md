# High-Resolution European Soil Property Maps Based on LUCAS and AlphaEarth Satellite Embeddings
**Source**: https://www.nature.com/articles/s41597-026-08273-1
**Date**: 2026-09-16
**Author**: Nature Scientific Data
**Keywords**: soil property maps, LUCAS, satellite embeddings, machine learning, Random Forest, neural networks, precision agriculture, Europe, 10m resolution

## Elevator pitch
Researchers produced 10-meter resolution soil property maps for all of Europe (EU-27 + UK) using machine learning trained on LUCAS soil datasets with AlphaEarth Foundations satellite embeddings, covering soil texture, pH, bulk density, and coarse fragments — a significant leap from the previous 30–250m resolution.

## Takeaways
- 10 m resolution soil property maps produced for EU-27 + UK, covering clay, silt, sand content, coarse fragments, pH, and bulk density
- Previous European soil maps ranged from 250 m to 30 m resolution depending on the property; this work closes the resolution gap
- Machine learning workflow trained on LUCAS soil datasets using AlphaEarth Foundations satellite embeddings as predictors
- Artificial Neural Networks outperformed Random Forests, with R² values ranging from 0.21 (coarse fragments) to 0.69 (pH)
- Uncertainty estimate maps were produced using Monte Carlo dropout
- Maps support precision agriculture, soil health assessment at field scale, and spatial planning

## Synthesis
A team of researchers has produced the highest-resolution soil property maps currently available for Europe (EU-27 plus the UK), achieving 10-meter resolution for six key soil properties: clay, silt, and sand content (soil texture), coarse fragments, pH, and bulk density. This represents a significant improvement over previously published maps, which ranged from 250 m to 30 m resolution depending on the soil property being mapped.

The maps were produced through a machine-learning workflow that combined LUCAS soil reference datasets with AlphaEarth Foundations satellite embeddings as environmental predictors. The team performed hyperparameter tuning and training on both Random Forests and Artificial Neural Networks, finding that ANN models consistently outperformed RF. The best-performing ANN achieved R² values ranging from 0.21 for coarse fragments (the most difficult property to predict) to 0.69 for pH.

For each soil property, the best ANN hyperparameters were used to generate continuous maps across Europe, accompanied by uncertainty estimate maps derived from Monte Carlo dropout. The generated maps aim to close the resolution gap for European soil data and provide a promising baseline for precision agriculture, field-scale soil health assessment, and spatial planning applications.

Funded through the ML4SoilQA project (part of CNSOIL) by the Austrian Federal Ministry and the EU's Horizon Europe NBSoil project, this work represents a growing trend of combining satellite-derived environmental data with machine learning to produce high-resolution geospatial products that were previously impossible at continental scale.