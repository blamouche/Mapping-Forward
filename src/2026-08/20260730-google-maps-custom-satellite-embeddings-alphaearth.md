# Introducing Custom Satellite Embeddings, powered by AlphaEarth Foundations
**Source**: https://mapsplatform.google.com/resources/blog/introducing-custom-satellite-embeddings-powered-by-alphaearth-foundations/
**Date**: 2026-07-30
**Author**: Google Maps Platform Team
**Keywords**: satellite embeddings, AlphaEarth, geospatial AI, remote sensing, Earth Engine, Google Maps Platform

## Elevator pitch
Google Maps Platform announces Custom Satellite Embeddings in private preview, enabling organizations to request on-demand, high-frequency geospatial embeddings from the AlphaEarth Foundations model for planetary-scale monitoring.

## Takeaways
- Custom Satellite Embeddings extends Google's annual Satellite Embedding dataset with higher-frequency, on-demand data summaries tailored to specific areas and timeframes (down to 5-day intervals).
- AlphaEarth Foundations synthesizes optical imagery, elevation, radar, and LiDAR into a unified 64-band image representation, reducing manual preprocessing bottlenecks.
- The product targets enterprise use cases: agriculture monitoring, land-use analytics, deforestation tracking, and disaster response.
- Woolpert reports using sub-annual custom embeddings alongside 50cm tasked imagery for crop type determination and government assessment.
- Available via Private Preview sign-up, complementing existing Earth Engine and Google Cloud Storage datasets.

## Synthesis
Google Maps Platform has launched the Private Preview of Custom Satellite Embeddings, building on the AlphaEarth Foundations model originally introduced by Google DeepMind. This new product addresses a key limitation of the existing annual Satellite Embedding dataset: the inability to monitor changes at sub-annual frequencies. By allowing organizations to request custom data summaries at quarterly, monthly, weekly, or even 5-day intervals, Google enables near real-time geospatial monitoring at scale.

The underlying AlphaEarth Foundations model acts as a "virtual satellite" that fuses multiple data sources—optical imagery, elevation models, radar signals, and LiDAR—into a single 64-band representation. This unified embedding simplifies complex remote sensing workflows that traditionally require significant preprocessing, expert tuning, and data integration effort. The embeddings are analysis-ready, meaning downstream machine learning models can consume them directly without extensive feature engineering.

Early customer feedback from Woolpert, a geospatial engineering firm, highlights the agricultural application: combining Google's 10-meter resolution temporal embeddings with freshly tasked 50cm satellite imagery to determine crop types and inform annual assessments for state and local government clients. This demonstrates the practical value of multi-resolution, multi-sensor fusion.

The product fits within Google Maps Platform's broader geospatial AI portfolio, which includes Grounding with Google Maps for LLMs, Maps Agentic UI Toolkit, and the MCP Server for real-time data integration. Custom Satellite Embeddings positions Google as a leader in enterprise geospatial analytics, competing with platforms like Planet Labs and Maxar while leveraging its unique AI-first approach to satellite data abstraction.