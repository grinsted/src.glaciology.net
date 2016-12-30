---
title: Scholarfy
date: 2013-06-10T02:17:00+00:00
author: aslak
layout: post
banner: /2013/06/scholarfy.jpg
categories:
  - Debris
aliases:
  - /2013/06/10/scholarfy/
  - /Home/Miscellaneous-Debris/scholarfy
---
I very often want to make a google scholar search using exactly the same search terms that i just had in google. For that i have used the [Scholarfy bookmarklet](http://people.cam.cornell.edu/~jugander/scholarfy.html) (highly recommended). I have updated it to take the search string from the document title instead. This has the advantage that it will work on more sites. E.g. if you click it from [this page](http://onlinelibrary.wiley.com/doi/10.1029/2005JD006494/abstract) then it will make [a sensible google scholar search](http://scholar.google.com/scholar?q=Svalbard%20summer%20melting%2C%20continentality%2C%20and%20sea%20ice%20extent%20from%20the%20Lomonosovfonna%20ice%20core).
  
`javascript:location = 'http://scholar.google.com/scholar?q='+escape(document.title.replace(/\s-\s.*$/g,""));`
  
you can add a bookmark to the above url if you want it. It should work in all browsers.
  
So shortly: Simply replace your bookmark to google scholar with the bookmarklet above.
