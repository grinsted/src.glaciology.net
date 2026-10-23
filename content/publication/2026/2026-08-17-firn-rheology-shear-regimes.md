---
title: Firn rheology revealed by contrasting shear regimes
date: 2026-08-17 00:00:00+00:00
author: aslak
banner: /publication/2026/toilet_pit.webp
citation: "Grinsted, A., Rathmann, N. M., Freitag, J., Lindsey-Clark, J., Rasmussen, S. O., Nymand, N. F., and Hvidberg, C. S., 2026. Firn rheology revealed by contrasting shear regimes. EGUsphere [preprint]. [10.5194/egusphere-2026-3464](https://doi.org/10.5194/egusphere-2026-3464)"
tags:
- Firn
- densification
- rheology
- NEGIS
- EastGRIP
- shear margin
- ice cores
- Δage
draft: false
---

Two firn cores, 15 km apart, with the same climate but very different ice flow. Together they let us separate how firn responds to shear and to compression, and show that ice dynamics can leave a climate-sized imprint on gas-age proxies.

<!--more-->

Most firn densification models are one-dimensional: snow is buried, the overburden builds up, and the firn compacts. Horizontal flow is assumed not to matter. But in ice streams and shear margins, firn is stretched and sheared as it is buried, and observations have long shown that densification there is faster than overburden alone can explain.

The problem is that a single density profile cannot tell you *why* firn densifies at a given rate. Many combinations of shear and bulk viscosity fit equally well, which is why earlier calibrations of continuum firn rheologies have given inconsistent results.

### A natural experiment at EastGRIP

The Northeast Greenland Ice Stream offers a way around this. The EastGRIP core sits inside the ice stream, while the S5-1 core was drilled in the adjacent shear margin, only about 15 km away. Both sites have essentially the same temperature (around −31 °C) and accumulation, but the horizontal strain rates in the shear margin are several times higher. Any difference between the two density profiles must therefore come from deformation, not climate.

We built a firn model based on the porous-ice rheology of Gagliardini and Meyssonnier (1997), which treats firn as a compressible power-law material that converges to Glen's flow law as it approaches ice density. With horizontal strain rates taken from satellite velocities, the vertical strain rate follows from a cubic equation with a closed-form solution, so the rheology can be dropped straight into existing 1D firn models. We then inverted both profiles for the density-dependent shear enhancement *a(ρ)* and compressibility *b(ρ)*, both with a steady-state model and with a Lagrangian flowline model that tracks each layer along its back-trajectory.

### What we found

* **The overall densification rate is well constrained.** The two cores pin down how fast firn compacts under its own weight, and the answer agrees well with the classic Herron–Langway model. How that compaction splits between squeezing and shearing is harder to determine.
* **Near-surface firn is much softer than standard models assume.** The top few meters compact far faster than commonly used firn rheologies predict. This suggests that a different deformation mechanism, which is not included in the usual flow law, dominates near the surface.
* **Deep firn in the shear margin is surprisingly stiff.** Radar data show that the ice crystals in the shear margin are already strongly aligned at about 24 m depth. This kind of crystal fabric makes the firn resist compaction.
* **Firn changes character as it densifies.** The way firn deforms does not change smoothly with density, but shifts at a few points, which we interpret as transitions between different deformation mechanisms.

The take-home message is that no single flow law describes firn all the way from snow to ice. The fitted parameters are best seen as effective values, and the mismatch tells us where the physics is still missing.

### Implications for ice cores

Because shear directly changes densification rates, changes in ice flow can affect the close-off depth and the gas-age–ice-age difference (Δage), even with no change in climate. In an idealized experiment where a site switches from high to low shear, the close-off depth deepens by about 24 m and Δage changes by roughly 200 years. Through gravitational fractionation, a 20 m shift in close-off depth corresponds to about 0.1 ‰ in δ¹⁵N, which would be read as a 3–5 K temperature change if interpreted purely climatically.

Ice-flow reorganisations have happened in the past, such as the Holocene shutdown of a paleo ice stream in northeast Greenland. Firn-derived proxies may therefore contain a dynamical component, which matters for gas-based chronologies and for comparing the timing of climate events between hemispheres.

### A practical bonus

The paper also includes an analytical approximation for the effective annual rate factor under seasonal temperature cycles. Because of the nonlinear Arrhenius dependence, evaluating the rate factor at the mean annual temperature underestimates densification, which is a common shortcut in steady-state firn models.

Code and data are available on [GitHub](https://github.com/grinsted/grinsted_firn_model-publication-package).

### Abstract

Firn densification is commonly modelled using 1D column approaches that neglect the deformation history associated with ice flow. Here, we present a flowline firn model that explicitly accounts for the accumulation and horizontal strain experienced by firn along its trajectory and use it to infer density-dependent rheology directly from observations.

Applying the method to two ice-core sites in northeast Greenland with contrasting strain regimes, we constrain both the total densification response and its partitioning into shear and volumetric components. While steady-state and flowline inversions agree at large scales, the combined function governing vertical strain is tightly constrained, whereas individual rheological parameters remain poorly identifiable.

The inferred rheology departs markedly from standard formulations, with enhanced near-surface densification, reduced viscous Poisson ratios, and pronounced non-monotonic structure. These behaviours are incompatible with a single power-law rheology and instead require the combined action of multiple deformation mechanisms, including grain-size-dependent creep and evolving anisotropy. The resulting parameters should therefore be interpreted as effective representations of these processes.

These results further imply that firn-derived gas proxies such as Δage and δ¹⁵N may contain a dynamical component linked to horizontal strain, with potential implications for the interpretation of ice-core chronologies.


