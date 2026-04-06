# Mapping Riyadh’s roads in high-resolution
**Source**: https://www.gim-international.com/case-study/mapping-riyadh-s-roads-in-high-resolution
**Date**: 2026-04-03
**Author**: GIM International
**Keywords**: mobile mapping, Riyadh, HD maps, CHCNAV, lidar, digital twin

## Elevator pitch
Hudhud mapped over 23,000 kilometres of Riyadh’s roads with CHCNAV’s mobile mapping system to build a high-resolution basemap for lane-level navigation and future digital twin services.

## Takeaways
- Hudhud surveyed more than 23,000 linear kilometres of roads in Riyadh.
- The project used CHCNAV’s AU20 mobile mapping system with lidar, panoramic imagery, GNSS, IMU, and wheel encoder inputs.
- The resulting dataset is intended for lane-level navigation, ADAS readiness, and broader smart-city use cases.
- Operational constraints included GNSS-degraded urban canyons, heat, and the need for near single-pass capture.
- Hudhud reports a 99.99% acceptance rate and near-zero resurvey rate under its quality-control workflow.

## Synthesis
GIM International presents a case study on Hudhud’s effort to build a high-resolution digital basemap of Riyadh, showing how industrial mobile mapping is being used not just for survey-grade capture but as foundational infrastructure for consumer navigation and future city services. The project covered more than 23,000 linear kilometres of road network across the metropolitan area.

Hudhud’s strategic objective was to create a locally optimized mapping stack instead of relying fully on external providers. The immediate application is its navigation product, which can benefit from lane-level detail, better turn accuracy, and more precise point-of-interest placement. But the article makes clear that the same dataset is also meant to support ADAS and autonomous-driving readiness, logistics optimization, infrastructure inventory, and eventually broader digital twin applications.

The technical architecture is central to the story. CHCNAV’s AU20 combines dual lidar scanners, a 72MP Ladybug panoramic camera, pavement cameras, a tightly coupled GNSS/IMU positioning system, and a DMI wheel encoder. That combination matters because Riyadh poses several operational difficulties: urban canyons introduce multipath and GNSS degradation, tunnels and underpasses interrupt satellite visibility, and sustained heat stresses both hardware and calibration stability. The system was selected to maintain dense, accurate capture at city scale under these conditions.

The article also highlights the production pipeline. CHCNAV’s CoPre preprocessing suite automates parts of the workflow such as filtering moving objects and colorizing lidar point clouds with panoramic imagery. This is important because the economics of HD mapping depend as much on post-processing efficiency as on capture hardware. If a project produces terabytes of data per day but cannot convert them quickly into mapping-ready assets, the operational value drops sharply.

In the end, the case study is a concrete example of how high-definition road mapping is becoming a strategic asset for regional mobility platforms. Rather than treating HD maps as a niche input for autonomous vehicles only, the project shows them as a reusable layer that can support navigation, logistics, smart-city operations, and urban planning at once.
