---
title: Digitizing pdf figures using inkscape
date: 2015-09-30 00:04:00+00:00
author: aslak
banner: /post/2015/1938hrswlz4vvjpg.jpg
tags:
- Tip
aliases:
- /2015/09/30/digitizing-pdf-figures-using-inkscape/
---

I recommend using [inkscape](https://inkscape.org/en/) if you want to digitize a vector figure from a pdf file. Here's how you do that.
<!--more-->
  1. Open Inkscape.
  2. In [inkscape preferences]-[svg output] disallow "relative coordinates".
  3. Import the pdf into inkscape. Inkscape will let you select which page to import.
  4. Delete all the objects you are not interested in. That is text and virtually everything else except the datapoints.
  5. Save as svg.
  6. Open the svg in a text editor and read the coordinates...

![](/post/2015/svgfig.png)

In the example shown here the path has a set of coordinates and there are some M and C commands. Usually you can just ignore these letters, but if you are curious then you can read more on their meaning [here](http://www.w3schools.com/svg/svg_path.asp). M means moveto, and C means curveto.

When you are done, then you probably want to re-allow "relative coordinates", as it results in smaller files.

**Digitizing non-vector bitmap figures:**

The svg-approach only works with vector graphics. When i need to digitize a bitmap, then I usually use digitize2 in matlab, or [WebPlotDigitizer](http://arohatgi.info/WebPlotDigitizer/) to digitize bitmap figures.