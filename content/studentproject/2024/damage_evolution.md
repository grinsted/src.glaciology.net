---
title: Ice flow, fractures, and damage
date: 2024-11-17 04:28:00+00:00
author: aslak
banner: /studentproject/2024/crevasse_field2_icebridge.webp
tags:
- crevasse
- damage
- fracture
- continuum mechanics
---

Ice sheet models assume a flow law for solid ice. However, damaged/crevassed ice may will effectively be less viscous than undamaged ice. We need a better way to handle this in ice flow models. 

<!--more-->

Two sub-projects: 
1. Semi-Empirical: Construct a model of sources and sinks to a damage density field. Calibrate it against observations, account for advection. Could potentially us some form of machine learning.  
2. Investigate the impact of newly formed crevasses on the vertically integrated viscosity. Pick area of study with substantial changes in ice flow and crevassing with good observations (e.g. a surging glacier). Invert 2d map plane flow model for viscosity for both before vs. after situation. Relate changes to crevasse density changes. 



builds on
* [damage in PISM](https://www.pism.io/docs/manual/modeling-choices/marine/damage.html)
* An empirical [crevasse failure criterion](/publication/2024-04-26-failure-criterion/)
* [increased crevassing paper](https://www.nature.com/articles/s41561-024-01636-6)