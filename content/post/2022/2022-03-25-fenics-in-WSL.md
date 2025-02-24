---
title: FEniCS on windows
date: 2022-03-25 05:24:00+00:00
author: aslak
banner: /post/2022/fenics.webp
---

[FEniCS](https://fenicsproject.org/) is a really nice tool for finite element modelling in python. It is difficult to install FEniCS on windows. The official instructions use a docker image. which I think is a bit heavy handed. I therefore installed it in a WSL-Ubuntu (Windows Subsystem for Linux). My experience with that has been friction free, so here are some very brief notes of what I did. 
<!-- more -->

### In windows
* Enable WSL [read here](https://learn.microsoft.com/en-us/windows/wsl/install)
* Install an ubuntu/debian image. [ubuntu](https://apps.microsoft.com/detail/9pdxgncfsczv?hl=en-us&gl=US)
* Install [VS Code](https://code.visualstudio.com/)

### In VS Code
* Install the "WSL remote" plug-in
* Install the "Python" plugin (the one from microsoft). 

### In your freshly installed ubuntu:
* Install [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) for Linux x86_64 (amd64)
* `mamba install matplotlib numpy ipykernel fenics`
* `code my_test.ipynb` (you might have to install/enable the VSCODe python plugin for WSL again.)


### In new VS Code editor window
The final command should open up a new notebook file in a new VS code editor window. In this new VS Code window, test that you can import fenics. 
* Add this line to the my_test.ipynb file `from fenics import *`

# Success!