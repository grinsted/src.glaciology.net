---
title: Ice model emulator
date: 2024-12-12
author: aslak
banner: /studentproject/2024/iceloss_emu_iceclimber.webp
weight: 0
tags:
- ice sheet
- sea level
- emulator
---

State-of-the-art ice-sheet models are computationally expensive to run. A single simulation may require hours to days of computing time, making it difficult to explore uncertainties in future climate forcing, model parameters, and physical assumptions. This is a major obstacle when estimating the possible contribution of ice sheets and glaciers to future sea-level rise.

<!--more-->

The goal of this project is to develop a fast emulator that reproduces the behaviour of a complex ice-sheet model. Once trained on a limited ensemble of model simulations, the emulator can be used to predict ice-sheet evolution under a wide range of future climate scenarios at a fraction of the computational cost.

Unlike purely statistical or ML approaches, the emphasis here is on developing **physically motivated emulators** that incorporate our understanding of glacier and ice-sheet dynamics. The aim is to build simple yet realistic models that capture the essential relationship between climate forcing and ice loss.

Possible approaches include:

* Developing low-order models of ice-sheet mass evolution, for example
  \[
  \frac{dM}{dt} = f(M,T,P,\ldots)
  \]
  where ice loss depends on the current ice mass and climate forcing.
* Using scaling relationships between ice-sheet mass, volume, area, thickness, and length to constrain model behaviour.
* Separating accumulation (snowfall) and ablation (runoff and melt) processes rather than treating climate forcing as a single variable.
* Training and validating emulators against large model intercomparison projects such as ISMIP or GlacierMIP.
* Developing regional emulators for different sectors of Greenland or Antarctica.
* Building glacier-scale emulators and combining them to estimate large-scale ice loss.

The project may involve a combination of:

* Physical modelling.
* Statistical inference and calibration.
* Machine learning.
* Time-series analysis.
* Sea-level projection and uncertainty quantification.

A successful emulator could enable thousands or millions of model evaluations, making it possible to characterize uncertainties that are currently computationally inaccessible with full ice-sheet models.

### Background and inspiration

* Edwards et al. (2021), ice-sheet emulation for sea-level projections:
  https://www.nature.com/articles/s41586-021-03302-y

* Physically informed climate-model emulators:
  https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023MS003899

* Machine-learning emulators for Earth-system applications:
  https://www.nature.com/articles/s43247-021-00289-2

### Students

* Jakob
* Nikolaj
