# Field Evaluation of Photogrammetric SLAM for Infrastructure Asset Mapping
**Source**: https://www.geoweeknews.com/articles/field-evaluation-of-photogrammetric-slam-for-infrastructure-asset-mapping/
**Date**: 2026-09-09
**Author**: Wayne Lee and Luke Gervais, BCIT Geomatics (Geo Week News)
**Keywords**: SLAM, photogrammetry, Looq AI, mobile mapping, infrastructure, GIS, Total Station, GNSS RTK, asset management, survey

## Elevator pitch
A field evaluation at BCIT compares Looq AI's handheld photogrammetric mapping platform against Total Station and GNSS RTK survey methods for infrastructure asset mapping, finding that the system can support precision mapping when used with rigorous survey control protocols.

## Takeaways
- Looq AI's Platform combines imagery, GNSS, and inertial sensing to produce georeferenced 3D data
- Evaluation conducted on a 150m x 50m outdoor plaza at BCIT Burnaby campus with ~45-47 manhole/utility features
- Reference framework established via Leica TS13 Robotic Total Station with closed traverse tied to BCIT geodetic network
- Leica GS06 GNSS RTK receiver provided comparison via Leica SmartNet CORS network
- In the no-control test, the Looq dataset exceeded the 50mm tolerance for GIS asset management
- With external ground control alignment, accuracy improved significantly
- Wet surface conditions from post-rain capture did not significantly affect geometry or detection accuracy

## Synthesis
This BCIT study provides a rigorous benchmark of camera-based photogrammetric mobile mapping against traditional survey methods. The Looq AI Platform — a handheld multi-camera system — was tested across multiple conditions: dry vs. wet surfaces, and with vs. without external ground control. The key finding is that while photogrammetric SLAM systems can capture data quickly, achieving professional-grade positioning requires external control alignment, reinforcing a fundamental survey principle.

The study's methodology is notable for its transparency: using UTM Zone 10N coordinates, nearest-neighbor spatial matching, and statistical significance testing at α = 0.05. The 50mm tolerance referenced for GIS asset management provides a practical benchmark. The finding that wet surfaces don't degrade accuracy is encouraging for field operations, but the critical takeaway is that without external control, the system exceeded the 50mm tolerance — a cautionary tale for teams considering AI-enabled reality capture without proper survey protocols.