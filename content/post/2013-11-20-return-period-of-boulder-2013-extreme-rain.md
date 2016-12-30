---
title: Return period of Boulder 2013 extreme rain
date: 2013-11-20T01:30:00+00:00
author: aslak
layout: post
banner: /2013/11/2013_Colorado_flooding_130918-Z-IT417-012.jpg
categories:
  - Debris
aliases:
  - /2013/11/20/return-period-of-boulder-2013-extreme-rain/
  - /Home/Miscellaneous-Debris/returnperiodofboulder2013extremerain
---
!![](/2016/02/boulder207day20precip2013.png)Several media stories on the Colorado floods talk of it as a 1000-year flood. However, the original source of this claim was talking about a 1000-year precip event (not the same as a flood-event). Pielke Jr discusses this on [his blog](http://rogerpielkejr.blogspot.dk/2013/09/how-fantasy-becomes-fact.html?m=1). The source for the 1000-year return level estimates appears to be this [NOAA](http://hdsc.nws.noaa.gov/hdsc/pfds/pfds_map_cont.html?bkmrk=co) page. We can argue about how solid these very rare return levels are as they obviously must be based on an extrapolation beyond the largest recorded event. Nevertheless out of curiosity I looked up what return period NOAA estimated for the observed rainfalls.
  
I found this map of weekly rain totals and clicked on a gauge in Boulder. It received 12.91 inches over 1 week. Other neighboring gauges experienced similar amounts.
  
I then went to the NOAA [return-period/return level](http://hdsc.nws.noaa.gov/hdsc/pfds/pfds_map_cont.html?bkmrk=co) page and plugged in the lat lon of the station and got this return level plot for 7-day totals:
  
![](/2016/02/7day20return.png)
  
From that return level graph the rainfall appears to be inconsistent with anything less than a 500-year event and the best estimate is that it is more rare than a 1000 year event. But again estimating the return period for this precipitation event is extrapolating far beyond past records and we should take it with a grain of salt. I would not go as far as calling it [pure fantasy](http://rogerpielkejr.blogspot.dk/2013/09/how-fantasy-becomes-fact.html) however.
  
Once the return period estimates are updated with the new observed precipitation extreme then the odds must shorten. Now that we have seen that it can happen then it will no longer seem quite as unlikely that it might happen again.
  
I have also downloaded Boulder precip data from [here](http://www.esrl.noaa.gov/psd/boulder/data.daily.html) and calculated my own empirical return period plot (see below). From this we clearly see that 12.91in is really off the scale. Prior to observing this extreme event you would probably have estimated a 1000 year return period (as indeed NOAA appears to have done). (shading is 1sigma).
  
![](/2016/02/ColoradoPrecip.png)

**Discharge in Boulder creek**
  
![](/2016/02/Colorado2013.png)
  
It would also be interesting to see how the weekly discharge in Boulder Creek compares to the past. At this [station](http://waterdata.usgs.gov/nwis/uv?cb_00060=on&format=gif_default&period=&begin_date=2013-09-11&end_date=2013-09-21&site_no=06730200) I get the weekly discharge (starting the 11th sept 2013) to be: 1.42bn feet<sup>3</sup> = 40M m<sup>3</sup>. A historical record can be found [here](http://waterdata.usgs.gov/co/nwis/dv?cb_00060=on&format=rdb&period=&begin_date=1986-10-01&end_date=2013-09-19&site_no=06730200&referred_module=sw) (since 1986). Taking this record, and stacking into weekly bins and looking at empirical return periods then I get the plot on the right. (shading is 1sigma / 17-83%). There the 2013 event comes out to be a ~25-year event (unsurprisingly since it has been observed once in a record starting in 1986). But you can also notice that the 2013 event does not diverge from a straight line extrapolation of the more common events. I.e. you would/should probably have expected a ~25 year return period prior to the 2013 floods.
  
**Detail**:
  
Why do i look weekly discharge rather than flood levels? The reason is that flood levels and instantaneous discharge are very sensitive to changes in infrastructure and adaptation/protective measures (e.g. flood plains). Weekly discharge is much less sensitive to such changes. Return period confidence intervals have been calculated using the approach described in the supplementary info to [this paper]({{< ref "publication/2013-10-11-homogeneous-record-of-atlantic-hurricane-surge-threat-since-1923.md" >}}).
