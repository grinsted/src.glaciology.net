---
title: GDEMv2 geotiff compression
date: 2013-08-10 14:51:00+00:00
author: aslak
banner: /post/2013/n55e012.png
tags:
- Tip
aliases:
- /2013/08/10/gdemv2-geotiff-compression/
- /Home/Miscellaneous-Debris/gdemv2compression
---

There is no good way to download the entire [GDEM](http://asterweb.jpl.nasa.gov/gdem.asp) dataset. It is just lots of manual work. I assume it is because of datavolume that they put artificial restrictions amd annoying hindrances in place.
  <!--more-->
  ![](/post/2013/n55e012.png)
There is 22000 tiles covering 1x1deg. Each tile file is a zip containing two geotiffs. A dem file and a num file. Unzipped then this is about 49Mb (or ~1Tb for all files). Zipped they are about 15Mb (or 330Gb for all).

However the geotiffs appear to be uncompressed tifs. I just downloaded the one covering Copenhagen and tried to use GDAL to compress them with these commands:

> gdal_translate -co "COMPRESS=DEFLATE" -co "predictor=2" -co tiled=yes "ASTGTM2_N55E012_dem.tif" "ASTGTM2_N55E012_dem_small.tif"



> gdal_translate -co "COMPRESS=DEFLATE" -co tiled=yes "ASTGTM2_N55E012_num.tif" "ASTGTM2_N55E012_num_small.tif"

The resulting compressed tifs outperform the zipped files:

  * DEM: Before=24.7Mb  |  CompressedTif=3.14Mb
  * NUM: Before=24.7Mb  |  CompressedTif=1.29Mb
  * Total: Before=49.4Mb | Zipped=5.2Mb  |  CompressedTif=4.4Mb

I also tried with N080W046: ZippedTotal=16.3Mb vs. CompressedTifs=12.3Mb

Anyway I don't understand why they don't distribute compressed geotiffs. It is certainly better than zipping it.

I've also tried the same with the [GIMP Greenland DEM](http://bprc.osu.edu/GDG/gimpdem.php) and it also gives very good compression. Probably a lot better actually because of the smooth topography of the ice sheet.

I used gdal_translate included in [FW_TOOLS](http://fwtools.maptools.org/)