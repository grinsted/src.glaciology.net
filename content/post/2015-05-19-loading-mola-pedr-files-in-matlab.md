---
title: Loading MOLA PEDR files in matlab
date: 2015-05-19T06:30:00+00:00
author: aslak
layout: post
banner: /2016/02/marsmola.png
categories:
  - Debris
tags:
  - code
  - Mars
  - Tip
aliases:
  - /2015/05/19/loading-mola-pedr-files-in-matlab/
  - /Home/Miscellaneous-Debris/loadingmolapedrfilesinmatlab
---
I have written a little matlab function to read the MOLA laser altimeter data from the Mars Global Surveyor.  More specifically the so called [Precision Experiment Data Records](http://pds-geosciences.wustl.edu/missions/mgs/pedr.html) (PEDR) records. PEDRs are generated from the raw altimetry profile data with precision orbit corrections applied. They are time-ordered binary tables with attached PDS labels. You can download the MOLA PEDR data [here](ftp://pds-geosciences.wustl.edu/mgs/mgs-m-mola-3-pedr-l1a-v1/mgsl_21xx/data/).
  
Perhaps somebody will find this useful. The function is attached below.
