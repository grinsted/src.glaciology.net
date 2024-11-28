---
title: 'Persistence Matters: Significance of paleoclimatic reconstruction statistics'
date: 2011-12-24 00:00:00+00:00
author: aslak
citation: 'Macias-Fauria, Grinsted, Helama, Holopainen (2012), Persistence matters:
  Estimation of the statistical significance of paleoclimatic reconstruction statistics
  from autocorrelated time series. Dendrochronologia, 30 (2), doi:10.1016/j.dendro.2011.08.003'
banner: /publication/2011/persistence.jpg
tags:
- climate
- reconstruction
- time series analysis
aliases:
- /2011/12/24/persistence-matters-significance-of-paleoclimatic-reconstruction-statistics/
- /Home/PDFs/Announcements/persistencematterssignificanceofpaleoclimaticreconstructionstatistics
---

Proxy data forms natural time series used to lengthen instrumental climatic records, and may contain a significant portion of autocorrelation. Increased serial correlation limits the number of independent observations, not satisfying the assumptions of conventional statistical methods.  <!--more--> We estimate the significance of calibration and verification statistics used in dendroclimatic reconstructions by combining Monte-Carlo iterations with frequency (Ebisuzaki) or time (Burg) domain time series modelling. Significance tests are presented for Coefficient of Determination (R2), Coefficient of Correlation (r2), Reduction of Error (RE) and Coefficient of Error (CE) for time series ranging from very low to very high autocorrelation. Increased autocorrelation implies higher occurrences of relatively high but spurious reconstruction statistics. Ebisuzaki time series modelling shows greater robustness and its use is recommended over Burg’s method, which penalizes the restriction in the number of autocorrelation coefficients imposed by the Akaike Information Criterion. Positive RE and CE values, traditionally viewed as successful reconstruction statistics, are not necessarily significant and depend on the temporal structure of the time series used. This approach is further implemented successfully to compute confidence intervals based on the temporal structure of the residuals of the transfer function. A Matlab® package and a Windows executable file for non-Matlab® users are provided to perform the described analyses.

**Citation**

Macias-Fauria, Grinsted, Helama, Holopainen (2012), Persistence matters: Estimation of the statistical significance of paleoclimatic reconstruction statistics from autocorrelated time series. Dendrochronologia, 30 (2), doi:[10.1016/j.dendro.2011.08.003](http://dx.doi.org/10.0.3.248/j.dendro.2011.08.003) [pdf](/pdf/Macias-Fauria-Dendrochronologia12-_Persistence.pdf)

**Matlab package:**

[http://oxlel.zoo.ox.ac.uk/reconstats](http://oxlel.zoo.ox.ac.uk/reconstats)

This paper is an advancement because the conventional wisdom in dendroclimatology is that "._.. there is no significance test for CE, any value greater than zero indicates some degree of model skill (Cook et al., 1994)_". (e.g. p272 from [this 2009 book](http://www.springer.com/earth+sciences+and+geography/atmospheric+sciences/book/978-1-4020-4551-6?cm_mmc=Google-_-Book%20Search-_-Springer-_-0)). - Well we provide such a test now, and we show that you commonly need to be more than just positive to beat p=0.05.