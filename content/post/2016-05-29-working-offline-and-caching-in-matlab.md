---
title: Working offline and caching in matlab
date: 2016-05-29T13:48:27+00:00
author: aslak
banner: /2016/05/Tamia_striatus_eating.jpg
tags:
  - matlab
  - tips
aliases:
  - /2016/05/29/working-offline-and-caching-in-matlab/
  - /2015/05/19/loading-mola-pedr-files-in-matlab/
---
I am working with satellite imagery in matlab. This is way too much data for me to keep on my laptop, and so I keep it on a server somewhere. But this has the major drawback that i cannot as easily work on the data when I am out of office. I can mount the server drive over ssh, but it is almost unbearably slow to fetch the data over the net when you are talking about Gb sized images. Instead I have coded a small a local cache system for matlab. It is called cachedcall and can be downloaded from the matlab [fileexchange](http://www.mathworks.com/matlabcentral/fileexchange/49949-cachedcall). It is not specifically aimed at loading files, but can also be used to cache the results of slow computations.

Let's say you have a line of code that looks like this:

{{< highlight matlab >}}
A = load('\\server\file');
{{< /highlight >}}


If you want to use the caching functionality of cachedcall then all you have to do is modify it thus:

{{< highlight matlab >}}
A = cachedcall(@load, {'\\server\file'} );
{{< /highlight >}}

cachedcall will then check if it you have made a call to load with the same input arguments earlier. If it is has a cached result then it will return the cached result. Cachedcall also have functionality for expiring the contents of your cache.

This means that if you have worked on '\\server\file' previously then it will be available later. I use that with when loading satellites of a server using [geoimread](http://www.mathworks.com/matlabcentral/fileexchange/46904-geoimread).

{{< highlight matlab >}}
ROI=[508655 7602045;506038 7595954;495020 7596866;484339 7599034;481306 7600283;475781 7610316;463950 7631832;473202 7659639;496254 7672217;512255 7668650;516136 7650715;517056 7624846;517316 7616226;511634 7606699];
[A,xa,ya,Ia] = cachedcall(@geoimread, {'\\server\path\to\scene\LC82310122013248LGN00_B8.TIF', ROI(:,1), ROI(:,2) } );
{{< /highlight >}}

The great thing is this speeds-up my scripts at work, plus it allows me to continue working on the scripts everywhere else.

 

cachedcall was featured as the file exchange pick of the week: http://blogs.mathworks.com/pick/2015/03/27/cache-your-nuts-to-eat-later/

 

 

 

 
