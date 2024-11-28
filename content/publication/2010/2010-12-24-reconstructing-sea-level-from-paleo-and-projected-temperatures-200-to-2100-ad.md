---
title: Reconstructing sea level from paleo and projected temperatures 200 to 2100
  AD
date: 2010-12-24 00:00:00+00:00
author: aslak
citation: Grinsted, A., J. C. Moore, and S. Jevrejeva (2010), Reconstructing sea level
  from paleo and projected temperatures 200 to 2100 AD, Clim. Dyn., doi:10.1007/s00382-008-0507-2.
banner: /publication/2010/800px-Po_vodam.jpg
tags:
- climate
- global
- hindcast
- historical
- projections
- sea level
- semi-empirical model
- slr
- SRES
- statistical modelling
- time series analysis
aliases:
- /2010/12/24/reconstructing-sea-level-from-paleo-and-projected-temperatures-200-to-2100-ad/
- /Home/PDFs/Announcements/gslprojection
---

Sea level rise of roughly a meter over the next century.
<!--more-->

The press release can be found [here](http://www.eurekalert.org/pub_releases/2009-01/uoc-slr010809.php).

**Abstract**

We use a physically plausible 4 parameter linear response equation to relate 2000 years of global temperatures and sea level. We estimate likelihood distributions of equation parameters using Monte Carlo inversion, which then allows visualization of past and future sea level scenarios. The model has good predictive power when calibrated on the pre-1990 period and validated against the high rates of sea level rise from the satellite altimetry. Future sea level is projected from IPCC temperature scenarios and past sea level from established multi-proxy reconstructions assuming that the established relationship between temperature and sea level holds from 200-2100 A.D. Over the last 2000 years minimum sea level (-19 to -26 cm) occurred around 1730 AD, maximum sea level (12 to 21 cm) around 1150 AD. Sea level 2090-2099 is projected to be 0.9 to 1.3 m for the A1B scenario, with low probability of the rise being within Intergovernmental Panel on Climate Change (IPCC) confidence limits.

_Citation: Grinsted, A., J. C. Moore, and S. Jevrejeva (2010), Reconstructing sea level from paleo and projected temperatures 200 to 2100 AD, Clim. Dyn., [doi:10.1007/s00382-008-0507-2](http://dx.doi.org/10.1007/s00382-008-0507-2)._ [[pdf](/pdf/grinsted-climdyn09-sealevel200to2100ad.pdf)]

**Some of the main results and some comments**

(_Note: when reading the tables and figures in the paper then look at the rows marked 'moberg' as they are our best guess_).

  * We project a sea level rise roughly 3 times higher than the predictions of the IPCC.
  * We are able to calculate a high resolution sea level curve for the past ~2000 years.
  * Even if we stop temperature from rising then sea level will still rise 20-40 cm (see T0 in table 2)
  * To stop sea level from rising then we should lower temperatures by  ~0.6 degrees C (see ΔT|<sub>S=0</sub> in table 1).
  * projected sea level rise for the most optimistic scenario ~80cm (B1 in table 2 - this scenario has a warming of 2degrees by 2100)
  * projected Sea level rise for the most pessimistic scenario ~135cm (A1FI in table 2 - this scenario has a warming of 4.5 degrees by 2100)

This means that no matter what we do to reduce CO2 then we are already committed to a considerable rise in sea level. There is simply so much intertia in the system, because the ice masses and ocean heat have not equilibrated to present surface temperatures. We must therefore adapt (by good infrastructure planning) to higher sea level. Still, we can also see that mitigation is not wasted. -It will be much more expensive to protect against 135cm compared to 80cm. Ofcourse there are also other climate impacts than sea level rise, and so we also have other reasons to reduce CO2.

It sounds very controversial to project such a large rise but it really is not. [Experts have known ](http://www.climatescience.gov/Library/sap/sap3-4/final-report/default.htm)that the IPCC projections were too conservative (including the IPCC authors) and those I have talked to had a feeling that something like 1-1.5 meter of rise was probably more correct (see also [this list ](/Home/Miscellaneous-Debris/recentpapersonsealevel)of recent papers). Now we provide some good solid evidence. Hopefully infrastructure planners will listen and plan accordingly. To be fair to the IPCC numbers then they do explicitly state that their estimates "exclude rapid dynamical changes" in ice sheets[.](/Home/PDFs/Announcements/gslprojection/pressresponse)

**Data and Model results**

  * Observed sea level with uncertainties. [[matlab .mat file](/Home/PDFs/Announcements/gslprojection/gsl-with-montecarloC.mat)].
  * Modelled sea level with uncertainties for all scenarios and experiments. [[matlab .mat file](/Home/PDFs/Announcements/gslprojection/G09-miniresulttable.mat)]
  * Random subsets of the Markov Chain Monte Carlo samples from the model parameter space from each experiment ([Moberg](/Home/PDFs/Announcements/gslprojection/g09-moberg-mcmc-small.txt), [Jones](/Home/PDFs/Announcements/gslprojection/g09-jones-mcmc-small.txt), [Historical](/Home/PDFs/Announcements/gslprojection/g09-obs-mcmc-small.txt)). These can be used to make projections for other temperature scenarios.

**A comment on the discussion at the realclimate blog.**

Stefan Rahmstorf at realclimate posted a blog-criticism of this paper, as he argues it has too low millenium scale sensitivity when compared to [a non-peer reviewed graph with no uncertainties](/Home/Miscellaneous-Debris/relationshipbetweensealevelriseandglobaltemperature). My side of the realclimate story can be found [here](/Home/Miscellaneous-Debris/rahmstorf2007lackofrealism). Please note that our disagreement is very small on projections for the next century though, as we both project roughly 3 times more than IPCC. This result [has since been reproduced and all recent studies seem to agree](/Home/PDFs/Announcements/howwillsealevelrespondtochangesinnaturalandanthropogenicforcingsby2100).