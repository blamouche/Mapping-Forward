# IBM and NASA Release Open-Source AI Model for Lunar Surface Mapping
**Source**: https://newsroom.ibm.com/2026-09-10-ibm-and-nasa-release-open-source-ai-model-to-support-lunar-exploration
**Date**: 2026-09-12
**Author**: IBM Research / NASA
**Keywords**: IBM, NASA, Lunar Foundation Model, open-source AI, lunar mapping, crater mapping, ice deposits, Hugging Face, Prithvi, remote sensing, geospatial AI

## Elevator pitch
IBM and NASA have released the open-source NASA-IBM Lunar Foundation Model, an AI foundation model trained on decades of lunar observation data that outperforms widely used methods by up to 23% in identifying key geographic features on the Moon's surface, including potential ice deposits, craters, and volcanic formations.

## Takeaways
- The NASA-IBM Lunar Foundation Model is one of the first publicly available foundation models for scientific exploration of the Moon, now available on Hugging Face
- The model exceeds widely used methods by up to 23% in identifying key geographic features including potential ice deposits, craters, and volcanic formations
- It reduced error (RMSE) in identifying areas with high potential for lunar ice up to 22% compared to the SwinV2-B (ImageNet) model
- At context-scale resolution (~100 meters), it outperforms SwinV2-B by nearly 19% using just half the training data
- The model was trained on a unified, machine learning-ready lunar dataset aggregating over 30 spatially-aligned layers from nine instruments across four missions (LRO, GRAIL, SELENE/Kaguya)
- It joins the Prithvi family of open foundation models, spanning geospatial, weather, heliophysics, and now lunar science
- Crater mapping with the model helps NASA select safe landing sites, avoid hazards, and plan long-term lunar infrastructure

## Synthesis
IBM and NASA have jointly released the NASA-IBM Lunar Foundation Model, an open-source AI model designed to transform decades of complex lunar observation data into actionable scientific insights. The model addresses a fundamental challenge: while sensors have generated petabytes of lunar data, scientists previously had to either sift through maps and images manually or rely on low-resolution, task-specific machine learning models.

The foundation model was trained on a groundbreaking dataset aggregating over 30 spatially-aligned layers from nine instruments across four missions, including NASA's Lunar Reconnaissance Orbiter (LRO), the GRAIL mission, and JAXA's SELENE/Kaguya. This multi-modal approach provides a rich view of both the lunar surface and subsurface. A NASA-IBM technical paper demonstrates that the model outperforms state-of-the-art approaches like SwinV2-B by up to 23% in identifying key geographic features, while offering greater efficiency and lower fine-tuning costs.

The model joins the Prithvi family of open foundation models, extending a collaboration between IBM and NASA that already spans geospatial Earth observation, weather forecasting, and heliophysics. By open-sourcing the model, the organizations aim to give the global scientific community access to cutting-edge AI systems for lunar exploration, supporting NASA's plans for a sustained human presence on the Moon.