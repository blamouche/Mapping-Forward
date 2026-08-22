# Use Python in ArcGIS CityEngine and import features from Overture Maps
**Source**: https://www.esri.com/arcgis-blog/products/city-engine/3d-gis/python-arcgis-cityengine-import-from-overture-maps
**Date**: 2026-07-10
**Author**: Simon Haegler and Jen Johnson (Esri)
**Keywords**: ArcGIS CityEngine, Python 3, Overture Maps, GeoParquet, GeoPandas, DuckDB, 3D city modeling

## Elevator pitch
ArcGIS CityEngine 2026.0 introduces a new Python 3 API and environment management, enabling users to import Overture Maps data directly into 3D city models using the broader Python geospatial ecosystem.

## Takeaways
- ArcGIS CityEngine 2026.0 ships with a new Python 3 API that is 1:1 compatible with the existing Jython API, requiring only three migration steps
- A bundled example project demonstrates importing Overture Maps data — the open data mapping initiative backed by Amazon, Microsoft, Meta, and TomTom
- Overture Maps data is available in GeoParquet format, an OGC standard compatible with modern geospatial tools and cloud platforms
- The Python 3 support enables integration with popular libraries like Pandas, GeoPandas, and DuckDB for processing large geospatial datasets
- Environments and packages are automatically installed when importing a project, simplifying collaboration

## Synthesis
Esri's ArcGIS CityEngine 2026.0 release marks a significant modernization step with its introduction of a full Python 3 API and corresponding environment management system. Users can now run Python 3 code in the CityEngine Python editor and interactive console, accessing the complete CityEngine API functionality while leveraging the vast Python package ecosystem from PyPI and Anaconda.

The release includes a practical example project that demonstrates importing data from Overture Maps — the collaborative open data mapping initiative funded by Amazon, Microsoft, Meta, and TomTom, and supported by Esri. Overture Maps data is distributed in GeoParquet format, an Open Geospatial Consortium standard designed for modern geospatial tools and cloud-native workflows.

The Python 3 migration is designed to be smooth: existing Jython scripts need only three changes — switching the project from Jython to Python, updating the import statement from "import scripting" to "import cityengine", and performing standard Python 2-to-3 upgrades. The new API also enables seamless integration with GeoPandas and DuckDB, allowing users to read GeoParquet files directly and process large datasets with spatial SQL in just a few lines of code.

This release reflects the broader industry trend of bridging proprietary GIS platforms with open geospatial data standards and the Python data science ecosystem, making 3D city modeling more accessible and interoperable.