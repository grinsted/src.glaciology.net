---
title: A sanity check for RCS
date: 2013-07-30 15:05:00+00:00
author: aslak
banner: /post/2013/Forest_in_Yakushima_55.jpg
aliases:
- /2013/07/30/a-sanity-check-for-rcs/
- /Home/Miscellaneous-Debris/asanitycheckforrcsandyamal
---

There has been a lot of [blogging about yamal](http://blogsearch.google.com/blogsearch?hl=en&ie=UTF-8&q=yamal+rcs&btnG=Search+Blogs). Some of it concerns if RCS introduces spurious signals. It is clear that it is very important to try to get an unbiased estimate of the growth curve.
  <!--more-->
Here i have calculated an very simple alternative to RCS. The idea is that if you only use tree rings of a particular age, then you do not need to make any corrections for the growth curve. The procedure:

  * Select a narrow age window. In my case i choose a 10 year wide window.
      * For each tree
          * calculate the log(mean(ringwidth)+0.05). for all the data in the age-window.
          * calculate the average year of growth for that age window.
      * Center the reconstruction for that window.
  * Repeat for different age windows.

The age intervals i chose were: 1-9, 10-19, ... ,390-399. It might be wise to disregard:

  * The youngest time slices where the growth curve signal is strongest.
  * The oldest time slices where there will be so few data that the record will be full of gaps. I am no expert on trees, but i suppose that really old trees can start to behave rather anomalously. For that reason it might be prudent to remove the oldest ring-widths.

I have made several ad-hoc choices here, but this page is only meant to serve as an illustration.

The colored dots show all the ringwidth estimates using this approach. Color shows the central age for the age window i have chosen.

Colored lines is a 50 year smooth of the points for a given age window (note i have not used a very clever interpolation/gapfilling scheme).

The blue line shows 50 year average of all dots.