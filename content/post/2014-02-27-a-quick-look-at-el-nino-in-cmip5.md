---
title: A quick look at El Niño in CMIP5
date: 2014-02-27T06:54:00+00:00
author: aslak
layout: post
banner: /2014/06/Marine_Fog_Pattern_1.jpg
categories:
  - Debris
tags:
  - ENSO
  - ESM
  - GCM
  - models
aliases:
  - /2014/02/27/a-quick-look-at-el-nino-in-cmip5/
  - /Home/Miscellaneous-Debris/aquicklookatelninoincmip5
---
## Teleconnections

El Nino is not well represented by many climate models.
  
In Nature there is a very high anti correlation between SOI and NINO3.4 in the order of -0.8. I have examined whether that also holds for CMIP5. It does not...

Note: Some runs may have been double counted. However restricting to smaller subsets are qualitatively similar. The few models with positive C are be due to a file mismatch between runs where KNMI-ClimateExplorer did not provide all meta data (I assumed r1i1p1 where this info was missing).
  
(_The models with a correlation coef occasionally greater than -0.5 are: EC-EARTH, **GISS-E2-H**, GISS-E2-R, **IPSL-CM5A-LR**, bcc-csm1-1, FIO-ESM - not all were counted in above histogram_)

Data were downloaded from KNMI climate explorer. Intervals were 1880-present. See also [Guilyardi et al 2012](http://www.gfdl.noaa.gov/~atw/yr/2012/guilyardi_etal_2012_clivex.pdf) and [Coats et al. 2013](http://onlinelibrary.wiley.com/doi/10.1002/grl.50938/abstract): Stationarity of the tropical pacific teleconnection to North America in CMIP5/PMIP3 model simulations

## Power Spectra

The power spectra of Nino3.4 (after removing global warming trend) looks like this.
  
![](/2016/02/cmip5nino34spectrum.png)
  
The model spectra has on average a reasonable shape, but it appears there is a bias towards less variability in modelled nino3.4. There are also models that seem completely off in their shapes.
  
similar for SOI:
  
![](/2016/02/cmip5soispectrum.png)
