---
title: Ice flow, fractures, and damage 
date: 2024-11-17T04:28:00+00:00
author: aslak
banner: /2024/crevasse_field2_icebridge.webp
tags:
  - crevasse
  - damage
  - fracture
  - continuum mechanics
---
Ice sheet models assume a flow law for solid ice. However, damaged/crevassed ice may will effectively be less viscous than undamaged ice. We need a better way to handle this in ice flow models. 

<!--more-->

Construct a physically motivated model of crevassing in terms of sources and sinks to a damage density field. Calibrate it against observations. 


builds on
* [damage in PISM](https://www.pism.io/docs/manual/modeling-choices/marine/damage.html)
* An empirical [crevasse failure criterion](/publication/2024-04-26-failure-criterion/)