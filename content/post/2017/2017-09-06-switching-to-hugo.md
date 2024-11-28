---
title: Migrating to Hugo
date: 2017-09-06 04:20:00+00:00
author: Aslak
banner: /post/2017/hugo.jpg
math: true
tags:
- tips
---

This site is now created using a static site generator called [hugo](https://gohugo.io). I host it on [netlify](https://netlify.com), and the source files are hosted on github. This is a nice setup for academics. So thumbs up from me.  
<!--more-->

Hugo is a static website generator (similar to Jekyll but faster and with fewer dependencies). You write your posts in markdown, and hugo will then render it to static html files using a theme. You can check the markdown source for this page [here](https://raw.githubusercontent.com/grinsted/src.glaciology.net/master/content/post/2017-09-06-switching-to-hugo.md). Static means fast, and easy to find a host. You could put it on github pages, your own web server, and netlify. Static also means that if you are going to host it yourself then it will be easier to keep your server safe from hackers. You will simply have a smaller attack surface.

Netlify is a place that hosts static websites. Once you have set it up then it will detect your commits to the git repo, and automatically compile a new version of the html. You could achieve the same using hugo+travisCI+github pages, but that is much more complicated to setup.

I like this new setup where I just have a bunch of local text files, and a git repo.

I've previously hosted my site on google sites which was nice because it has zero maintenance and high up-time. The drawback is that it has almost no flexibility. I migrated to wordpress hosted on a digital ocean droplet. There is quite a lot of maintenance in keeping all components updated and reasonably secure, installing SSL certificates, managing a database and backups. This new setup is much easier.

## Examples ##

Here are some examples of what you can quite easily do. You can include math such as this: $ x=\sum_{i=1}^{k+1}i $,  using familiar latex syntax. You can also include highlighted code like this:

```python
import matplotlib.pyplot as plt
plt.plot([1,2,3,1])
plt.ylabel('some numbers')
plt.show()
```