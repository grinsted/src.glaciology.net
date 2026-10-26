---
title: "Taking giant leaps in time: a differentiable JAX ice-flow model"
date: 2026-10-24
draft: false
banner: /studentproject/2026/Southern_Tip_of_Greenland.jpg
banner_credit: 'Credit: USGS/NASA/Wikimedia Commons'
weight: 10
tags:
- ice-sheet modelling
- numerical methods
- JAX
- differentiable programming
- time stepping
- simulation
---

Ice sheets evolve over centuries to millennia, yet most ice-sheet models are forced to take time steps of only a few years to remain numerically stable. Can we do better? And can we build ice-flow models that are fast, run on GPUs, and are differentiable, so that they can be calibrated with gradients and coupled into modern climate models?

In this computational project, you will develop a compact ice-flow model in JAX, starting from the Shallow Shelf Approximation in a 1D flowline setting and possibly extending to 2D. The model will be verified against analytical solutions and standard benchmarks such as MISMIP and ISMIP-HOM. Using automatic differentiation, you will compute gradients of model output with respect to inputs like basal friction and surface mass balance.

A central question is how to take large time steps without losing accuracy. You will compare different strategies, from the standard sequential approach and recent stabilization schemes, to linearly implicit and fully coupled implicit time stepping, and map out the trade-off between accuracy and computational cost. Depending on your interests, the project can lean towards numerical analysis, high-performance GPU computing, or glaciological applications.

The longer-term goal is a differentiable ice component that can be coupled to atmosphere and ocean models in VerCOR, the JAX-based Earth-system coupler developed at the Niels Bohr Institute. Experience with Python and numerical methods is an advantage.

Curious? Look up: shallow shelf approximation, JAX, Newton–Krylov methods, multigrid, free-surface stabilization algorithm (FSSA), MISMIP+, ISMIP-HOM.

Interesting places to start:

- [A numerical stabilization scheme for the shallow shelf approximation](https://arxiv.org/abs/2510.02943) (Westling Dolling, Henry & Ahlkrona): the Thickness Stabilization Scheme (TSS), which allows much larger stable time steps in SSA models.
- [GLIDE](https://github.com/glide-ism/glide): a GPU-accelerated ice-flow model with multigrid solvers, fully coupled implicit time stepping, and gradients via PyTorch.
- [VerCOR](https://vercor.readthedocs.io/): the JAX-based Earth-system coupler developed at the Niels Bohr Institute.