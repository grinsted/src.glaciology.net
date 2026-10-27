---
title: How much did it snow on Greenland 2000 years ago?
date: 2026-10-26 00:00:00+00:00
author: aslak
banner: snow2016eastgrip.jpg
banner_credit: 'Photo: Aslak Grinsted'
tags:
- accumulation
- greenland
- paleoclimate
- ice cores
- tree rings
- reconstruction
- statistics
draft: true
weight: 10
---

Snowfall is the only source of mass for the Greenland ice sheet, yet we know surprisingly little about how it has varied beyond the last few decades. Regional climate models and in-situ observations give us a detailed picture of accumulation since around 1960, but ice-sheet models and sea-level projections need to know how accumulation behaves on centennial to millennial time scales. Can we reconstruct Greenland accumulation over the past few thousand years?

<!--more-->

We have recently developed a method for combining regional climate model output with millions of accumulation observations from the SUMup database. The method decomposes model accumulation into spatial patterns (EOFs) and their time series (principal components), and calibrates them against observations. This gives bias-corrected, spatially complete accumulation maps, but only for the period covered by the climate models.

To go further back in time, we need to rely on climate proxies. Ice-core records such as δ¹⁸O, and tree-ring records from Greenland and its surroundings, carry information about past climate. The challenge is to translate that information into accumulation: given a set of proxy records, can we reconstruct the time series of the dominant accumulation patterns, and from them, spatially complete accumulation maps for the past few thousand years?

In this project you will develop and test statistical methods for reconstructing past Greenland accumulation. The project combines glaciology, paleoclimate, statistics, and data analysis. It draws on the rich literature on climate field reconstruction, where similar methods have been used to reconstruct past temperature and drought from tree rings and other proxies.

A central challenge is that proxies are noisy, irregularly sampled, and only indirectly related to accumulation. The relationships we calibrate over recent decades may also not hold over millennia. The project therefore focuses both on developing reconstruction methods and on understanding their uncertainties and limitations.

Possible project directions include:

* Developing methods for reconstructing the principal components of accumulation from proxy records.
* Investigating which accumulation patterns can, and cannot, be constrained by the available proxies.
* Selecting and combining predictors from ice cores and tree-ring records.
* Quantifying uncertainty, including proxy noise, dating uncertainty and non-stationarity.
* Comparing approaches from the climate field reconstruction literature, from classical regression to regularized and Bayesian methods.
* Identifying where new proxy records would most improve the reconstruction.

The workflow typically consists of three stages:

1. **Calibration:** Relate proxy records to accumulation patterns over the period covered by climate models and observations.
2. **Validation:** Test the reconstruction against withheld data and against independent long accumulation records from ice cores.
3. **Reconstruction:** Extend the accumulation maps back in time, with uncertainties.

Careful validation is key. Accumulation records from ice cores span centuries to millennia, and provide an independent test of whether the reconstruction captures real variability, and not just noise fitted over the calibration period.

### Methods

* Statistical climate field reconstruction
* EOF and principal component analysis
* Calibration and validation
* Uncertainty quantification
* Python programming
* Paleoclimate data analysis

### Relevant resources

* SUMup surface mass balance database
* Regional climate models (HIRHAM, RACMO) and CARRA reanalysis
* Ice-core δ¹⁸O and accumulation records
* Tree-ring records from Greenland and surroundings

### Builds on
* **Cook, Briffa & Jones (1994):** Spatial regression methods in dendroclimatology, and the calibration/verification statistics used to judge reconstruction skill.
* **Mann, Bradley & Hughes (1998):** Reconstructing the principal components of a climate field from a multiproxy network.
* **Tingley & Huybers (2010):** A Bayesian hierarchical approach to climate field reconstruction in space and time.
* **Wang et al. (2014):** A comparison of modern climate field reconstruction methods, including CCA, RegEM and GraphEM.
* **King et al. (2021):** Climate field reconstruction from a small, highly sensitive tree-ring network, with spatial uncertainty estimates.
* **Lindsey-Clark et al. (2025):** [Greenland Monthly Accumulation Maps (1960–2022): A Statistical Semi-Empirical Bias-Adjustment Model](https://www.glaciology.net/publication/2025/2025-06-22-gris-sumup-rcm-accumulation/).

### Status

This project is reserved for Josephine as part of her PhD. If you are interested in a related topic, come and talk to me.