# Measuring a Bridge That Never Stops Moving: Multimodal Lidar Maps the Cape Fear Memorial Bridge
**Source**: https://www.geoweeknews.com/articles/sponsored/measuring-a-bridge-that-never-stops-moving/
**Date**: 2026-08-25
**Author**: Carla Lauter (Geo Week News)
**Keywords**: lidar, mobile mapping, static scanning, bridge survey, NCDOT, McKim & Creed, centimeter accuracy, digital twin, infrastructure

## Elevator pitch
McKim & Creed delivered a centimeter-accurate 3D survey of a 1969 vertical-lift bridge carrying 65,000 vehicles daily — without a single lane closure — by combining mobile mapping, static lidar, and ground-based survey control.

## Takeaways
- The Cape Fear Memorial Bridge in Wilmington, NC, is a 400-foot vertical-lift span built in 1969, now functionally obsolete with 65,000 daily vehicles and a $1.1 billion replacement in environmental review.
- NCDOT required centimeter-accuracy survey data but prohibited any lane closure, direct deck occupation, or interruption of marine traffic — and the bridge has no shoulder for target placement.
- McKim & Creed combined three data sources: a Riegl VMX-2HA mobile mapping system driven at 45 mph, a Riegl VZ-600i static scanner from ground and elevated positions, and a ground-based control network set entirely off the span.
- Survey control was triangulated from safe ground positions, then propagated to the structure via static scans. Mobile data was adjusted using unconventional vertical features (guardrail faces, light poles) as tie-planes instead of standard flat road surfaces.
- Validation showed mobile and static point clouds aligning at centimeter level; the workflow is repeatable for any structure too dangerous, busy, or sensitive to occupy directly.

## Synthesis
Bridges are among the hardest infrastructure to survey: difficult to access, often vibrating under traffic, and sensitive to lane closures. The Cape Fear Memorial Bridge in Wilmington, North Carolina, added further constraints — it is a 400-foot vertical-lift span (the center deck rises straight up between two towers) built in 1969, carrying more than 65,000 vehicles daily on U.S. Routes 17, 76, and 421. NCDOT deemed it functionally obsolete, with a $1.1 billion replacement in federal environmental review. Before any redesign, NCDOT needed a centimeter-accurate 3D survey — but would not allow a single lane closure, direct deck occupation, or interruption of the bridge's lift cycles for marine traffic.

The solution, engineered by McKim & Creed's geospatial team led by Matt LaLuzerne, combined three coordinated data sources. Mobile mapping used a Riegl VMX-2HA dual-scanner system with integrated GNSS and inertial navigation, collecting at the posted 45 mph in live daytime traffic across multiple passes for redundancy. Static scanning used a Riegl VZ-600i set at ground level below the bridge and from an elevated position with line of sight to the lift towers and truss. The control network was placed entirely off the span — in a parking space beside the tender house and at grade in accessible areas — then triangulated to the scanner positions.

The technical innovation came in the adjustment. Mobile lidar normally relies on flat road surfaces and ground-level targets to correct trajectory drift from GNSS degradation under steel structures. With no targets on the span and GNSS degraded by the truss, the team defined its own planar features — guardrail faces, light poles, and discrete points — and fed them into Riegl's RiPROCESS software as custom tie-planes. This vertical-feature adjustment is unconventional for mobile calibration, which typically uses horizontal surfaces. Cross-section validation showed the mobile data (green) running essentially on top of the static data (purple), confirming centimeter-level accuracy.

The entire process — from pre-approval discussions with NCDOT through fieldwork to deliverable — ran about twelve weeks with a crew of five to six in the field and a similar number processing data. The pre-planning effort was substantial, with plans A, B, and C rehearsed before site mobilization, which is what allowed field operations to run cleanly within the constraints of NCDOT, marine traffic, and bridge tender schedules.

McKim & Creed emphasize that nothing about this workflow is specific to the Cape Fear bridge. The combination of mobile mapping, terrestrial lidar, and off-structure survey control applies to any structure too dangerous, busy, or sensitive to occupy directly — making it a repeatable answer for hard-to-reach infrastructure across the transportation network.