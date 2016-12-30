---
title: Comparison of sea level projections
date: 2014-10-23T05:10:00+00:00
author: aslak
layout: post
banner: /2016/02/AR5slprojRCP4.5.png
categories:
  - Debris
tags:
  - IPCC
  - projections
  - RCP
  - review
  - sea level
  - semi-empirical
  - slr
aliases:
  - /2014/10/23/comparison-of-sea-level-projections/
  - /Home/Miscellaneous-Debris/comparisonofsealevelprojections
---
I have been making a nice figure which compares the 21stC sea level projections from the AR5, with previous IPCC reports, Semi empirical models, and an expert elicitation ... I hope this may be useful in presentations for many people (Feel free to use them where ever). See also [this page](/Home/Miscellaneous-Debris/optimisticicesheetprojectionsinar5) for a similar figure for the Ice sheet contribution only.
  
The IPCC FAR,SAR,TAR,AR4 have all been converted to RCP scenarios using conversion factors (see below). All projections have been regularized to 100 years using plain scaling.

![](/2016/02/AR5slprojRCP4.5.png)

!![](/2016/02/AR5slprojRCP8.5.png)
  
 
  
**Legend:**

  * **Extrap**: constant rate of sea level rise at present day trend from [sealevel.colorado.edu](http://sealevel.colorado.edu/). (An absolute lower limit of plausibility IMO)
  * **FAR**: full range of SLR projections from [FAR](http://www.ipcc.ch/ipccreports/far/wg_I/ipcc_far_wg_I_app_01.pdf) (taken from [SAR](http://www.ipcc.ch/ipccreports/sar/wg_I/ipcc_sar_wg_I_full_report.pdf) table 7.8)
  * **SAR**: full range of SLR projections from SAR (taken from [TAR table 11.14](http://www.ipcc.ch/ipccreports/tar/wg1/428.htm#tab1112)). (SARp369: "Excluding the possibility of collapse of the West Antarctic ice sheet").
  * **TAR**: full range of SLR projections from [TAR table 11.14](http://www.ipcc.ch/ipccreports/tar/wg1/428.htm#tab1112). (TAR p.642: "The range of projections given above makes no allowance for icedynamic instability of the WAIS".)
  * **AR4**: SLR projection excluding scaled-up ice sheet discharge. ([AR4 WG1 Table 10.7](http://www.ipcc.ch/publications_and_data/ar4/wg1/en/ch10s10-6-5.html)).
  * **AR4+**: SLR projection including scaled-up ice sheet discharge. ([AR4 WG1 Table 10.7](http://www.ipcc.ch/publications_and_data/ar4/wg1/en/ch10s10-6-5.html)). Context for "larger values cannot be excluded" can be found in the [AR4 SPM](http://www.ipcc.ch/publications_and_data/ar4/wg1/en/spmsspm-projections-of.html).
  * **SEM**: full range of semi-empirical projections in AR5 (from AR5 fig.13.12).
  * **AR5**: "process based" ice sheet projections from AR5 table 13.5. These do not account for a potential [collapse of Antarctic marine based sectors](/Home/Miscellaneous-Debris/ar5sealevelriseuncertaintycommunicationfailure) which may contribute up to several decimetres (indicated with thin shaded line).
  * **Ice sheet experts***. refers to [Bamber and Aspinall (2013) table S1](/Home/Miscellaneous-Debris/icesheetcontributionsfrombamberaspinall) 5-95% plus non ice sheet contributions from AR5 table 13.5. Note BA13 does not refer to a specific scenario (hence the asterisk)
  * **SLR experts** refers to the expert elicitation of [Horton et al. 2013](http://www.sciencedirect.com/science/article/pii/S0277379113004381) ([table 1](http://www.realclimate.org/index.php/archives/2013/11/sea-level-rise-what-the-experts-expect/)). They do not provide RCP45 but only RCP85 and RCP3PD. However both SEMs and AR5 agree that the projection for RCP45 lies at about a third of the way between. So I have used this weighing. Some assumptions on normality and covariance structure were necessary to derive 5-95% confidence intervals from the likely ranges reported in AR5 table 13.5.

"Antarctic collapse" does not literally mean a full collapse, but refers to a marine ice sheet instability. Read AR5 text for more precise meaning. We have also published [an estimate of worst case sea level rise](/Home/PDFs/Announcements/upperlimitforsealevelprojectionsby2100) which you may find here.

**Scenario conversion factors that I have used:**
  
_The aim of the conversion factors is to predict what the old models would give if forced with new scenarios._
  
RCP45/A1B=0.90 & RCP85/A1B=1.20 from AR5 fig 13.10
  
A1B/IS92A=1.20 calculated by forcing a [Jevrejeva model](/Home/PDFs/Announcements/howwillsealevelrespondtochangesinnaturalandanthropogenicforcingsby2100) with [TAR table II.3.11](http://www.ipcc.ch/ipccreports/tar/wg1/551.htm)
  
IS92A/SA90=0.87 calculated by forcing a [Jevrejeva model](/Home/PDFs/Announcements/howwillsealevelrespondtochangesinnaturalandanthropogenicforcingsby2100) with [SAR fig Ax.9](http://www.ipcc.ch/ipccreports/1992%20IPCC%20Supplement/IPCC_Suppl_Report_1992_wg_I/ipcc_wg_I_1992_suppl_report_annex.pdf).
  
Compare TAR II.3.11 with SAR Ax.9. I'd greatly appreciate any comments on how to improve these conversion factors.
  
**My interpretation:**
  
Interestingly sea level projections was coming down (and narrowing) until we started getting worrying records from the ice sheets. By AR4 it became evident that the ice sheets had a far more dynamic behavior than previously thought ([Larsen-B](http://en.wikipedia.org/wiki/Larsen_Ice_Shelf), [Jakobshavn](http://en.wikipedia.org/wiki/Jakobshavn_Glacier), [Helheim](http://en.wikipedia.org/wiki/Helheim_Glacier), [Kangerdlugssuaq](http://www.people.ku.edu/~stearns/leigh/page2/page16/page35/page35.html)). It became clear that the representation of ice physics and marine ice sheet interaction needed to be improved (see [SeaRISE](http://websrv.cs.umt.edu/isis/index.php/SeaRISE_Assessment) & [ice2sea](http://www.ice2sea.eu/)). Since then the evidence for an important dynamic ice sheet contribution has only been strengthening with e.g. [Thwaites](http://en.wikipedia.org/wiki/Thwaites_Glacier) in the Antarctic, and [Petermann](http://en.wikipedia.org/wiki/Petermann_Glacier) in Greenland.

Note: I might update figs with a better representation of the SEM uncertainties. If you have comments then please email or tweet me.
