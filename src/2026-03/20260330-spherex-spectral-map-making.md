# Spectral Map Making With SPHEREx
**Source**: https://astrobiology.com/2026/03/spectral-map-making-with-spherex.html
**Date**: March 30, 2026
**Author**: Keith Cowing
**Keywords**: SPHEREx, NASA, spectral maps, near-infrared, all-sky survey, galaxy formation, astrobiology

## Elevator pitch
NASA's SPHEREx mission develops innovative spectral map-making techniques for its all-sky near-infrared survey across 102 wavelength channels, enabling investigations of galaxy formation history and galactic dust mapping.

## Takeaways
- SPHEREx is a NASA Explorer spacecraft launched in March 2025 conducting an all-sky near-infrared spectral survey
- The survey spans 0.75 to 5.0 microns with 102 wavelength channels at varying spectral resolution
- Key scientific goals include mapping extragalactic background light and detecting hydrogen recombination lines and PAH emissions
- Output maps are produced in both tangent-plane projection and full-sky HEALPix format
- Public mosaic tools will be made available through NASA/IPAC's Infrared Science Archive (IRSA)

## Synthesis
Astrobiology.com's Keith Cowing reports on the map-making methodology developed for NASA's SPHEREx mission, a wide-field all-sky near-infrared spectrophotometry Explorer satellite launched in March 2025. The research, led by Ari Cukierman and colleagues, addresses the complex computational and methodological challenges of converting raw satellite observations into scientifically usable spectral maps.

SPHEREx (Spectro-Photometer for the History of the Universe, Epoch of Reionization, and Ices Explorer) conducts a comprehensive all-sky survey across 102 wavelength channels spanning 0.75 to 5.0 microns — the near-infrared portion of the electromagnetic spectrum. This wavelength range is particularly valuable for cosmological and astrophysical investigations because it captures light from distant galaxies redshifted out of the visible spectrum and emission from cool stars, dust, and molecules in the Milky Way.

The map-making methodology addresses several categories of technical challenge. Zodiacal light — infrared emission from interplanetary dust in the solar system — creates a bright, spatially variable foreground that must be carefully modeled and subtracted to reveal faint extragalactic signals. Atmospheric emission (though space-based observations largely avoid atmosphere), monitoring of instrument systematics, and signal loss prevention during map projection all require specialized algorithmic treatments.

The scientific ambitions supported by these maps are broad: intensity mapping of the extragalactic background light to investigate the cosmic history of galaxy formation, mapping resolved galaxies and nebulae across the sky, and detecting galactic emission features including hydrogen recombination lines, molecular-hydrogen emission, and polycyclic aromatic hydrocarbon (PAH) spectral features. PAH features are particularly relevant for astrobiology, as these complex organic molecules are widespread in the interstellar medium and represent potential precursors to prebiotic chemistry.

Output maps are produced in two standard formats: tangent-plane projections for local sky regions and full-sky HEALPix format — a widely used pixelization scheme for spherical sky coverage that enables efficient statistical analysis of full-sky datasets. The planned public release through NASA/IPAC's Infrared Science Archive ensures the data will be accessible to the broader astronomical community.
