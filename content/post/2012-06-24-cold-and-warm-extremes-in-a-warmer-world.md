---
title: Cold and Warm Extremes in a warmer world
date: 2012-06-24T20:41:00+00:00
author: aslak
layout: post
banner: /2012/06/squirrelhotday.jpg
categories:
  - Debris
tags:
  - extremes
  - statistics
aliases:
  - /2012/06/24/cold-and-warm-extremes-in-a-warmer-world/
---
Greenhouse gases is warming the world and this will lead to more frequent heat waves all else being equal. You might naively think that this increase in extreme warm spells will be compensated by an similar decrease in the number of cold spells and that the damage on society will be the same. However, that is simply not true statistically even if you assume that the damage from a cold spell is the same as the damage from a warm spell.
  
Let me demonstrate with a simple experiment.
  
Lets say that the "pre-industrial" temperature distribution can be represented by a normal distribution. Events that are more than 2 standard deviations away from the mean we classify as either heat waves or cold waves. We generate 10000 events of pre-industrial temperatures and count the number of warm and cold events. We then proceed to add a mean warming signal and count the number of warm and cold events in this warmed climate. Here's the results:
  
** Heat waves**** Cold waves**** # extremes**** "Pre-industrial" climate**214223437** "warmed" climate**1576101586
  
In the warmer climate we got significantly fewer cold waves (13 compared to 233). However, this decrease was more than compensated by a large increase in the number of heat waves (214 to 1576). The total number of extreme events increased by a factor 3.6. This increase will be greater the further out in the tail you look. It is intuitively clear that it must be so if you imagine the case with extreme warming. You cannot decrease the number of cold waves below zero, but a heat wave will happen virtually every time you roll the dice if you apply sufficient warming. Rahmstorf makes the same argument in the [reply to Hoerling on dot earth](http://dotearth.blogs.nytimes.com/2012/04/10/more-on-extreme-weather-in-a-warming-climate/).
  
Matlab code:

{{< highlight matlab >}}

T=randn(10000,1);
Warm=[sum(T>2) sum(T+1>2)]
Cold=[sum(T<-2) sum(T+1<-2)]
Warm+Cold

{{< /highlight >}}


This post was provoked by some statements by Martin Hoerling in the [dot-earth commentary](http://dotearth.blogs.nytimes.com/2012/04/10/more-on-extreme-weather-in-a-warming-climate/) to Coumou and [Rahmstorf](http://sciences.blogs.liberation.fr/files/10-ans-dextremes-climatiques.pdf)s recent work on climate extremes. In it he said
  
_"Note that the increase in heat waves was largely balanced by a decrease in cold waves". _
  
No evidence is presented for this statement (it is afterall just an interview comment). I can only assume that they observe it is for one of the following reasons:

  * The threshold for warm and cold extremes have been chosen to be something much closer to the mean value.
  * They look at changes over a short time interval where the warming signal is very small compared to weather variability.
  * (... or the shape of the distribution has changed dramatically)

These are probably necessary 'evils' in order to obtain sufficient number of extreme events to do credible statistics. The observational period is short. But these processing choices would also obscure any possibility to detect the distribution changes we are talking about. Therefore, this line of evidence cannot be used to claim that Coumou and Rahmstorf is using "Exaggerated language".
