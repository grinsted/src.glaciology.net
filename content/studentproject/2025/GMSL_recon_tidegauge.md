---
title: "Reconstructing global sea level"
date: 2025-04-28 04:28:00+00:00
author: aslak
banner: /studentproject/2025/Isle of the Dead, Port Arthur - hunter et al 2003.webp
weight: 10
tags:
- GMSL
- Reconstruction
- Statistics
- Spherical Harmonics
- Machine Learning
---

Better estimates of historical Global Mean Sea Level (GMSL) can help us understand many components of the climate system. It is a key climate record.

<!--more-->

The GMSL record over the 20th century is based on sparse tide gauge records, and relies on various statistical techniques to extrapolate to the global ocean. This extrapolation introduces uncertainty. Can you do it better than existing techniques?

In this project you will design a new GMSL reconstruction method and put it to the test. Can your statistical method improve our estimates of historical sea level?

Can your method ingest discontinuous data such as [the 1841–42 record at Port Arthur](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2002GL016813) or the measurements made during [James Cook's voyage of the Endeavour in 1769–70](https://hgss.copernicus.org/articles/9/85/2018/)?

**Outcomes:**
* A new reconstruction method
* A new GMSL record
* Improved uncertainties

**Brainstorm:**
* Spherical harmonics
* [Gaussian processes](https://www.youtube.com/watch?v=5ZOPtHKzHrM)

**Builds on:**
* [Hay et al. (2015)](https://www.nature.com/articles/nature14093): probabilistic reanalysis using a Kalman smoother (see also the [2017 erratum](https://doi.org/10.1038/nature24466))
* [Dangendorf et al. (2024)](https://essd.copernicus.org/articles/16/3471/2024/essd-16-3471-2024.pdf)
* [Church and White (2006)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2005GL024826)
* [Kopp et al. (2016)](https://doi.org/10.1073/pnas.1517056113): Common Era sea-level reconstruction
* [Caron et al. (2018)](https://doi.org/10.1002/2017GL076644): probabilistic GIA model

**Data:**
* [PSMSL tide gauges](https://psmsl.org)
* [Satellite altimetry](https://www.aviso.altimetry.fr/en/data/products/ocean-indicators-products/mean-sea-level.html)

**Status:** Benjamin is currently working on this project. He is currently re-implementing the Hay et al. method as a baseline and building his improvements on top of it. If you're interested in a related topic, come and talk to me.