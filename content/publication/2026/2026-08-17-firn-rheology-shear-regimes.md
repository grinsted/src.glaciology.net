---
title: Firn rheology revealed by contrasting shear regimes
date: 2026-08-17 00:00:00+00:00
author: aslak
banner: /publication/2026/toilet_pit.jpg
banner_credit: "Aslak Grinsted CC-BY SA 3.0"
citation: "Grinsted, A., Rathmann, N. M., Freitag, J., Lindsey-Clark, J., Rasmussen, S. O., Nymand, N. F., and Hvidberg, C. S., 2026. Firn rheology revealed by contrasting shear regimes. EGUsphere [preprint]. doi:10.5194/egusphere-2026-3464"
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

Take two firn cores drilled 15 km apart, at the same temperature and with the same snowfall. If firn densification were only about climate, their density profiles would be identical. They aren't, and the difference tells us something a single core never could.

<!--more-->

### Why one core isn't enough

Most of us model firn as a 1D column. Snow is buried, the overburden builds up, and the firn compacts. Horizontal flow is quietly assumed away. That works well enough on domes and divides, but density profiles from ice streams and shear margins have long shown that firn there densifies faster than overburden alone can explain.

The trouble is working out *why*. A density profile is the integrated result of everything the firn has experienced on its way down, and many combinations of shear viscosity and compressibility reproduce it equally well. That non-uniqueness is a large part of why earlier calibrations of continuum firn rheologies disagree with each other.

What you really want is a controlled experiment: same climate, different deformation.

### A natural experiment at NEGIS

The Northeast Greenland Ice Stream provides one. The EastGRIP core sits inside the ice stream, while S5-1 was drilled in the adjacent shear margin, about 15 km away. Both sites are at around −31 °C with essentially the same accumulation, but the horizontal strain rates in the margin are several times higher. Whatever separates the two density profiles has to come from ice flow.

To use this, we built a firn model on the porous-ice rheology of Gagliardini and Meyssonnier (1997), which treats firn as a compressible power-law material that converges to Glen's flow law as it approaches ice density. Given horizontal strain rates from satellite velocities, the vertical strain rate follows from a cubic equation with a closed-form solution, so the rheology drops straight into existing 1D firn models. We then inverted both profiles for the density-dependent shear enhancement *a(ρ)* and compressibility *b(ρ)*, using both a steady-state model and a Lagrangian flowline model that follows each layer along its back-trajectory.

### What the two cores tell us

The reassuring result first: the total densification response is tightly constrained, and it agrees well with the classic Herron–Langway model. The steady-state and flowline inversions also agree at large scales. The less comfortable result is that even with two contrasting sites, the split between volumetric compaction and shear is poorly identifiable. The combination that governs vertical strain is pinned down; the individual rheological parameters are not.

Beyond that, the inferred rheology looks quite different from standard formulations. The top few meters compact far faster than commonly used rheologies predict, which points to a deformation mechanism the usual flow law leaves out. Deep firn in the shear margin, on the other hand, is surprisingly stiff. Radar data show that the crystal fabric there is already strongly aligned at about 24 m depth, and that fabric resists compaction. We also find reduced viscous Poisson ratios, and a rheology that doesn't evolve smoothly with density but shifts at a few points, which we interpret as transitions between deformation mechanisms.

Taken together, this can't be described by a single power-law rheology. It needs several mechanisms acting together, including grain-size-dependent creep and evolving anisotropy. The fitted parameters are best read as effective values, and where the model struggles is a pointer to where the physics is still missing.

### When ice flow looks like climate

This is where it matters beyond firn modelling. If shear changes densification rates, then changes in ice flow change the close-off depth and Δage, with no change in climate at all. In an idealized experiment where a site switches from high to low shear, the close-off depth deepens by about 24 m and Δage changes by roughly 200 years. Through gravitational fractionation, a 20 m shift in close-off depth corresponds to about 0.1 ‰ in δ¹⁵N, which would be read as a 3–5 K temperature change if interpreted purely climatically.

Ice-flow reorganisations have happened, such as the Holocene shutdown of a paleo ice stream in northeast Greenland. Firn-derived gas proxies may therefore carry a dynamical component, which matters for gas-based chronologies and for comparing the timing of climate events between the hemispheres.

### A small bonus

The paper also includes an analytical approximation for the effective annual rate factor under a seasonal temperature cycle. Because of the nonlinear Arrhenius dependence, evaluating the rate factor at the mean annual temperature underestimates densification, a common shortcut in steady-state firn models that's easy to fix.

### Read more

The preprint is on [EGUsphere](https://doi.org/10.5194/egusphere-2026-3464), and the code and data are on [GitHub](https://github.com/grinsted/grinsted_firn_model-publication-package). Comments and questions are very welcome.



### Abstract

Firn densification is commonly modelled using 1D column approaches that neglect the deformation history associated with ice flow. Here, we present a flowline firn model that explicitly accounts for the accumulation and horizontal strain experienced by firn along its trajectory and use it to infer density-dependent rheology directly from observations.

Applying the method to two ice-core sites in northeast Greenland with contrasting strain regimes, we constrain both the total densification response and its partitioning into shear and volumetric components. While steady-state and flowline inversions agree at large scales, the combined function governing vertical strain is tightly constrained, whereas individual rheological parameters remain poorly identifiable.

The inferred rheology departs markedly from standard formulations, with enhanced near-surface densification, reduced viscous Poisson ratios, and pronounced non-monotonic structure. These behaviours are incompatible with a single power-law rheology and instead require the combined action of multiple deformation mechanisms, including grain-size-dependent creep and evolving anisotropy. The resulting parameters should therefore be interpreted as effective representations of these processes.

These results further imply that firn-derived gas proxies such as Δage and δ¹⁵N may contain a dynamical component linked to horizontal strain, with potential implications for the interpretation of ice-core chronologies.


