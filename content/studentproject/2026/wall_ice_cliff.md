---
title: How long would the Wall stand?
date: 2026-10-23 13:35:00+00:00
author: aslak
banner: /studentproject/2026/ice_wall.jpg
weight: 1
tags:
- ice cliffs
- MICI
- calving
- ice rheology
- geomorphology
- crazy ideas
draft: false
---

In *Game of Thrones*, the Wall is a 200 m tall wall of ice that has stood for thousands of years. Real ice cannot do that. Under its own weight it would creep and slump, and a vertical ice face that tall is thought to be beyond the strength of ice. So how long would the Wall actually stand, and what would be left of it?

<!--more-->

The question turns out to be a clean, idealised version of a real problem in glaciology: the marine ice cliff instability (MICI). If ice shelves collapse, tall ice cliffs may be exposed at the margins of Antarctica. Above a critical height, roughly 100 m above the waterline, these cliffs are expected to fail. If each failure exposes an even taller cliff, retreat could become runaway and contribute substantially to future sea-level rise. Whether this actually happens is still debated.

One thing that may stop it is the debris itself. Calved ice piles up in front of the cliff as icebergs and mélange and pushes back on the ice. Glaciologists describe this as a *back force*. Geomorphologists have studied the same feedback for rock cliffs for more than a century, but describe it in terms of *geometry*: debris falling from a cliff builds a talus slope that gradually buries the face until the cliff is gone. This is the classic Fisher–Lehmann model of cliff retreat.

The Wall is the perfect test case for connecting the two views. It is dry, cold, and sits on land, so all the debris stays where it falls. A real marine cliff is the opposite extreme: debris floats, capsizes and drifts away, unless it gets jammed in a fjord.

The aim of the project is to build a simple, transparent model that bridges glaciological theory and the geomorphological description of cliff burial. Key questions include:

* How fast would a 200 m ice wall slump by viscous flow, and does it fail by brittle collapse first?
* How quickly does the debris from repeated failures bury the cliff, and what is the final stable shape?
* How much back force does a debris apron exert, and how does that compare with the force needed to stop ice-cliff failure?
* What changes when the cliff stands in water: when the debris is buoyant, and when it can be carried away?
* Under what conditions does debris stabilise a cliff, and when does retreat become runaway?

The project can be shaped to suit your interests, and the problem can be attacked at several levels. A natural starting point is scaling arguments based on Glen's flow law and the strength of ice, which can grow into a simple reduced model of cliff failure and debris accumulation. From there, finite-element models can be used to calculate the stress field near the cliff face and how a debris apron alters it, while small 2D discrete-element simulations can show how a pile of ice blocks pushes back on the cliff. Even the simple "falling sand" cellular automata used in games could be a fast way to explore how debris piles up and buries the cliff. A bachelor project could focus on the dry cliff alone, while a master's project could extend it to the marine case.

Relevant resources and background literature:

* [Bassis et al. (2021)](https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/23422/Bassis_2021_Science_Transition_marine_AAM.pdf?sequence=1&isAllowed=y): Transition to marine ice cliff instability controlled by ice thickness gradients and velocity. *Science*. Includes simulations of a dry ice cliff.
* [Crawford et al. (2021)](https://doi.org/10.1038/s41467-021-23070-7): Marine ice-cliff instability modeling shows mixed-mode ice-cliff failure and yields calving rate parameterization. *Nature Communications*.
* [Schlemm et al. (2022)](https://tc.copernicus.org/articles/16/1979/2022/): Stabilizing effect of mélange buttressing on the marine ice-cliff instability of the West Antarctic Ice Sheet. *The Cryosphere*.
* [Cliff burial by talus](https://www.tandfonline.com/doi/pdf/10.1080/00040851.1983.12004329): an analysis of the Fisher–Lehmann model. *Arctic and Alpine Research* (1983).

Software:

* Finite elements: [FEniCSx](https://fenicsproject.org/) or [Firedrake](https://www.firedrakeproject.org/).
* Falling-sand cellular automata: [sandspiel](https://github.com/MaxBittker/sandspiel) (Rust/WebGL, play it online at [sandspiel.club](https://sandspiel.club/)) and a minimal Python example, [falling-simulation](https://github.com/mpioski/falling-simulation).