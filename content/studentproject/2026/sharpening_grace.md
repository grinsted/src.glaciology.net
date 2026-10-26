---
title: "Sharpening GRACE: where on the ice sheet is the mass going?"
date: 2026-10-26 00:00:00+00:00
author: aslak
banner: /studentproject/2026/grace-fo-in-orbit.jpg
tags:
- GRACE
- gravimetry
- inverse modelling
- spherical harmonics
- sea level
- ice sheets
- geophysics
draft: false
weight: 10
---

The GRACE and GRACE-FO satellites weigh the ice sheets from space every month. But they see the world through blurry glasses: the gravity field is only resolved down to a few hundred kilometres, so mass change on the ice sheet smears into the ocean and onto neighbouring land. Can we use physics to sharpen the picture?

<!--more-->

Standard mass-balance products start from monthly solutions of Earth's gravity field in a spherical-harmonic representation (e.g. CSR RL06.2) and infer time series of mass change per ice sheet or drainage basin. Because the spatial resolution is limited, this is an under-determined inverse problem: many different mass-change patterns are consistent with the same gravity observations. How we resolve that ambiguity matters, especially near the coast, where most of the mass loss happens.

In this project you will develop new ways of inverting GRACE data by building in what we already know about how ice sheets gain and lose mass. By constraining the problem with physically motivated assumptions, we may obtain sharper maps, better coastal estimates, and more honest uncertainties.

A central challenge is that every assumption is also a potential source of bias. The project therefore focuses both on developing inversion methods and on testing when, and how badly, each assumption fails.

Possible project directions include:

* Assuming that mass change depends on surface elevation, and differs inside and outside the ice-sheet mask.
* Requiring the ocean's response (the sea-level fingerprint) to be consistent with the inferred ice-sheet mass loss, thereby removing degrees of freedom.
* Assuming that mass change follows spatial patterns (EOFs) learned from other datasets, such as a regional climate model for Greenland or satellite altimetry for Antarctica.
* Unifying these approaches within a Gaussian-process framework, where each assumption becomes a different prior covariance.
* Quantifying leakage, GIA uncertainty, and the trade-off between resolution and noise.

The workflow typically consists of three stages:

1. **Forward modelling:** Convert mass-change fields on the ice sheet and ocean to the spherical-harmonic gravity signal that GRACE would observe.
2. **Synthetic experiments:** Test inversion methods on artificial datasets where the true mass-change pattern is known.
3. **Real-world application:** Apply the methods to GRACE/GRACE-FO data and compare the results with existing mass-balance estimates.

An important advantage of this project is that inversion methods can first be tested in a controlled virtual environment. Mass-change fields from regional climate models and altimetry provide synthetic "ground truth" datasets that allow rigorous validation before moving to real observations. A natural starting point is Greenland, where GIA is relatively small and climate models are excellent, with Antarctica as a more challenging extension.

### Methods

* Inverse modelling
* Spherical harmonics
* Sea-level equation and fingerprints
* Gaussian processes and EOF analysis
* Uncertainty quantification
* Python programming

### Relevant resources

* GRACE/GRACE-FO monthly gravity solutions (CSR RL06.2)
* Mascon products (CSR, JPL, GSFC)
* Regional climate models (MAR, RACMO)
* Altimetry elevation change (CryoSat-2, ICESat-2)
* IMBIE ice-sheet mass balance estimates

### Builds on

* **Wouters et al. (2008):** Forward modelling of GRACE observations to estimate Greenland mass loss with reduced leakage.
* **Harig & Simons (2012):** Slepian-function localization of GRACE data to map where Greenland is losing mass.
* **Rietbroek et al. (2016):** Joint inversion of GRACE and altimetry using sea-level fingerprints to separate the contributions to sea-level rise.