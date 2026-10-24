---
title: "Can a neural network learn how ice flows?"
date: 2026-10-24
draft: false
banner: /studentproject/2026/robotic_ice_machine.webp
weight: 10
tags:
- machine learning
- deep learning
- ice dynamics
- remote sensing
- Greenland
- Antarctica
---

Satellites now map the surface velocity of the ice sheets in remarkable detail, and we have good maps of ice geometry, surface conditions and climate. Could a neural network learn the relationship between them, and predict how fast the ice flows directly from what we observe?

In this project, you will train a deep neural network, for example a U-Net, to predict observed ice velocities from inputs such as surface elevation, ice thickness, whether the ice is grounded or floating, temperature, melt rates, and perhaps satellite imagery. Velocity products such as ESA's Climate Change Initiative (CCI) and ITS_LIVE, combined with frequently updated surface elevations from satellite altimetry, make it possible to follow how both geometry and flow change through time. Neural networks have been used to emulate ice-flow models, but learning ice flow directly from observations is much less explored.

There are many interesting questions to pursue, and the project can be shaped around your interests. Which inputs actually matter? Has the network learned something resembling physics, or is it reading the answer from clues hidden in the data, such as crevasses in satellite images? Can a network trained on one region or period predict velocities elsewhere, or how flow changes when the geometry changes? A more ambitious direction is to combine the network with a differentiable physics-based ice-flow model, letting the network learn only the parts we cannot observe, such as conditions at the bed.

The ultimate goal is to find out what machine learning can teach us about ice flow, and where physics is still needed. Experience with Python is an advantage; prior machine learning experience is welcome but not required.

Curious? Look up: U-Net, ESA CCI Ice Sheets, ITS_LIVE, CryoSat-2, ICESat-2, BedMachine, Instructed Glacier Model (IGM), physics-informed neural networks.

Interesting places to start:

- [ESA CCI Greenland Ice Sheet](https://climate.esa.int/en/projects/ice-sheets-greenland/) and [ESA CCI Antarctic Ice Sheet](https://climate.esa.int/en/projects/ice-sheets-antarctic/): satellite-derived ice velocities, surface elevation change and more.
- [ITS_LIVE](https://its-live.jpl.nasa.gov/): global satellite-derived glacier and ice-sheet velocities, with annual maps going back decades.
- [BedMachine](https://nsidc.org/data/idbmg4): ice thickness and bed topography for Greenland (an Antarctic version is also available).