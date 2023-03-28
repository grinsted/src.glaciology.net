---
title: FEniCS on windows
date: 2022-03-25T05:24:00+00:00
author: aslak
banner: /2022/fenics.png
---
[FEniCS](https://fenicsproject.org/) is a really nice tool for finite element modelling in python. It is difficult to install FEniCS on windows. The official instructions use a docker image. which I think is a bit heavy handed. I therefore installed it in a WSL-Ubuntu (Windows Subsystem for Linux). My experience with that has been friction free, so here are some very brief notes of what I did. 
<!-- more -->

### In windows
* Enable WSL2 and install a Ubuntu image. [see here](https://learn.microsoft.com/en-us/windows/wsl/install)
* Install [VS Code](https://code.visualstudio.com/)

### In VS Code
* Install the "WSL remote" plug-in
* Install the "Python" plugin (the one from microsoft). 

### In your freshly installed ubuntu:
* Install [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) for Linux x86_64 (amd64)
* `mamba install -c conda-forge matplotlib numpy ipykernel fenics`
* `code my_test.ipynb`


### In new VS Code editor window
The final command should open up a new notebook file in a new VS code editor window. In this new VS Code window, test that you can import fenics. 
* Add this line to the my_test.ipynb file `from fenics import *`

# Success!
