---
title: Citing CMIP data
date: 2013-08-10T04:26:00+00:00
author: aslak
banner: /2013/08/1280px-Citation_needed_stickers.jpeg
aliases:
  - /2013/08/10/citing-cmip-data/
  - /Home/Miscellaneous-Debris/cmip6on-demanddoigeneration
---
It would be nice to have a simple doi-like way of citing CMIP6 datasets and this is being discussed today on twitter. I have not been involved in the discussion before, so I have no idea if my ideas has been proposed before. Anyway here are my thoughts.
<!--more-->

[EDIT: _something has already been proposed and implemented with [Datacite](http://cera-www.dkrz.de/WDCC/CMIP5/Citation.jsp). H/T O.Bothe & B. Lawrence. Consider my proposition below to be a kind of ill-considered wish list._]

[EDIT2: _some infrastructure is already in place using data cite. My ill informed comments here apparently made [Bryan Lawrence grumpy](http://home.badc.rl.ac.uk/lawrence/blog/2013/08/09/on_cmip6_and_dois) :-). Anyway I still think that I have some useful ideas here. But please note that there is already an [existing method](http://cera-www.dkrz.de/WDCC/CMIP5/Citation.jsp) of citing (but it could be better advertised IMO, and is not practical in some cases)._ ]

I think the obvious way would be to simply generate a doi on demand.

In practice all it requires is a central database that holds info on which CMIP datasets correspond to each doi. I would use file hashes (e.g. SHA2) as the primary identifier rather than file names or id's. This is to ensure that the file has not been modified along the way.

The user would simply be supplied with a small script which does the following:

  * all the files matching a file pattern (e.g. *.nc) is being hashed.
  * All hashes is sent to doi-server.
  * doi-server checks that it knows the id of all the files. if not return error.
  * A new doi is generated which links to file collection
  * return new doi

It should also have a web interface where you can put a list of filenames / hashes and it attempts to resolve what datasets you are talking about. This would require an additional manual verification by the user to ensure that the data set version of each file is correct.

When a reader follows a CMIP doi link then they will be confronted with a web page showing exactly which files were in the file collection. This list could link to download archives. It could also highlight if there are new versions available. You could also add features to show if any serious bugs/issues has been found with the data. It could also link to all known citations of the collection.

This could also be implemented to support the existing CMIP ensembles (and other data partners). I think it would be natural to extend it to PMIP and Geomip etc. I think it makes sense to keep it exclusive for these types of climate model outputs rather than making a universal data cite format. This is such a huge collection of data and I think there is added value from supporting only this type of data.

Please follow the more informed discussion over at [Bryans blog](http://home.badc.rl.ac.uk/lawrence/blog/2013/08/09/on_cmip6_and_dois).

**Side benefit: **

Having this would also remove the need to have [a long acknowledgement](http://cmip-pcmdi.llnl.gov/cmip5/citation.html) in every single manuscript using CMIP. The central DOI registry could be used to extract usage statistics at a very detailed level.

**Regarding additional fields: ****Author, Title, Description etc.**

To improve user experience then I would probably not include an author and title of each collection. The data is what it is, and how it is used depends on who is citing the collection. The true author is not who is compiling the selection of datasets, but the modelling groups who made the data. I would not even allow a description because I see it as a potential mess of inconsistent info and spam. I'd much prefer an automatically generated list of known citations.
