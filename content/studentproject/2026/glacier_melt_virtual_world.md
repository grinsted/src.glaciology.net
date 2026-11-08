---
title: "Why do simple melt models get mountain glaciers wrong high up?"
date: 2026-11-08
author: aslak
banner: denali_kahiltna.webp
banner_alt: "Aerial view of Denali and the glaciers on its flanks, Alaska"
banner_credit: 'Credit: [ArcticHokie / Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Denali3.jpg), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)'
tags:
- glaciers
- mass balance
- surface energy balance
- machine learning
- climate
- modelling
draft: false
weight: 10
---

Global glacier models calculate melt from air temperature alone, using so-called degree-day models. They work surprisingly well where the ice melts most, but high up on the glacier, where snow accumulates, they get the mass balance wrong, and the error depends on the climate: too much mass on maritime glaciers, too little on dry continental ones. Why?

<!--more-->

Thousands of glaciers worldwide have measured mass-balance profiles, the mass gained or lost at each elevation, collected by the World Glacier Monitoring Service. When we compare them with a degree-day model driven by a global climate reanalysis, the lower parts of the glaciers fit well, but the upper parts do not, and the misfit changes sign between warm, wet and cold, dry climates. Corrections that depend only on elevation, such as more sunshine higher up or a different temperature lapse rate, shift all glaciers the same way and cannot remove it. Something about the climate is missing, but what?

In this project you will find out, choosing one of two routes, or combining them:

* **A virtual world.** Drive a detailed surface energy-balance model, which calculates melt from sunshine, wind, humidity and temperature, with hourly reanalysis data at glaciers from maritime to continental climates. Its mass-balance profiles are then the "truth", and you can ask: does a degree-day model fail on this virtual world in the same way as on the real glaciers? Which process (sublimation in dry air, clouds, wind, rain, the timing of summer snowfall) creates the misfit? Here you know the answer exactly, which is never true for real glaciers.
* **Machine learning.** Train a model to predict the misfit of the degree-day model from everything we know about each glacier and its climate: radiation, humidity, wind, cloudiness, precipitation seasonality, topography. Which predictors matter? Does the model generalise to glaciers in regions it has never seen, or does it only learn regional fingerprints? Interpretable machine learning can point to the physics that the simple model is missing.

The ultimate goal is a better and still simple melt model for global glacier projections, or a clear understanding of why the simple model fails. The project can be shaped as a BSc or MSc project depending on scope. Experience with Python is an advantage; the energy-balance model and the data sets are available.

Curious? Look up: degree-day model, temperature-index melt, surface energy balance, COSIPY, ERA5, CARRA, World Glacier Monitoring Service, OGGM, explainable machine learning.

Interesting places to start:

* [Fluctuations of Glaciers database (WGMS)](https://wgms.ch/data_databaseversions/): mass-balance profiles of glaciers worldwide.
* [ERA5 reanalysis](https://cds.climate.copernicus.eu/): global hourly and monthly climate data since 1940.
* [COSIPY](https://github.com/cryotools/cosipy): an open-source surface energy and mass-balance model for glaciers, written in Python.
* Hock (2003), [Temperature index melt modelling in mountain areas](https://doi.org/10.1016/S0022-1694(03)00257-9), Journal of Hydrology: why degree-day models work, and where they do not.
* [OGGM](https://oggm.org/): the Open Global Glacier Model, a degree-day based global glacier model.
