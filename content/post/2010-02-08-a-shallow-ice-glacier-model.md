---
title: A Shallow Ice Glacier Model
date: 2010-02-08T02:32:00+00:00
author: aslak
banner: /2010/02/sia.jpg
tags:
  - glacier model
  - sia
aliases:
  - /2010/02/08/a-shallow-ice-glacier-model/
  - /Home/Miscellaneous-Debris/ashallowiceglaciermodel
---
I have experiemented with using matlabs built-in ode solvers to integrate a Shallow ice model. Surprisingly the ode solvers are able to take much greater timesteps than what theoretical stability criteria would suggest. I am really impressed by how well it works although I will not recommend using this approach:

  * There is a discontinuity where the height can not go below zero. This is very hard for the ode solvers to deal with.
  * Tiny instabilities result in oscillations (I've set the tolerances such that they are visible in the video). However, this can in practice lead to an accumulation bias due to the altitude-accumulation feedback.

The main advantage of the ode solver approach is that the code can be made extremely short and readable. It could therefore serve as a nice introduction to the Shallow Ice Approximation.
  
{{< youtube JfHs0DjATBY >}}

Mail me if you would like a piece of the code. It is short and easy to read.

brown is the bedrock. It is a modification of matlabs peaks function. transparent white is the glacier surface.
