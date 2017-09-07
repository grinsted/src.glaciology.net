---
title: Picking a password manager
date: 2016-04-07T06:28:52+00:00
author: aslak
banner: /2016/04/BlascoAB1x-G-e1460011917610.jpg
tags:
  - Tip
aliases:
  - /2016/04/07/picking-a-password-manager/
---
It is difficult to pick a password manager. After many considerations I eventually decided on a keepass2 database. It is a difficult decision because you have to place quite a lot of trust in the solution.
<!--more-->
I want to be able to access my database from every device. I use windows, android, linux, and osx. Additionally I would also like to have a fallback solution for how I could access the db in an environment where I cannot install anything. This means the database has to be hosted/synced to a server or to the cloud. I don't trust the cloud, so it is essential that the decryption takes place client side. Keepass2 allows me to store the database in the cloud (webdav/google drive/dropbox/...).

There are keepass2 clients for all the different platforms. That ticks one box for me. But one thing that makes me uncomfortable is that I have to use a different client for every platform. That is inherently less secure. Can I trust them all? I trust the main Keepass2 project. It is a C#-project, and is primarily designed for windows. It should be possible to run it with mono on linux and osx, but I have not had success with that. Many of the alternative clients for other platforms have a smaller user base, and consequently the code has received less scrutiny. So, that is not an ideal situation. In the end here are the clients that I use, or consider to use:

### Windows

I use [Keepass2](http://keepass.info/) on my windows machine. I use it with two plugins: 1) [keeagent](https://github.com/dlech/KeeAgent) which replaces pageant when i use putty. 2) [keepasshttp](https://github.com/pfn/keepasshttp) for browser integration. I am not totally comfortable with having to trust plugins.

### Android

[Keepass2android](https://play.google.com/store/apps/details?id=keepass2android.keepass2android&hl=en) is good. But do I trust my phone to keep any secrets?

### Online fallback solution

[Keeweb](https://github.com/antelle/keeweb) is a sleek node.js project, and can run both in the browser and on the desktop (it uses electron for that). All the crypto takes place client side. I have a self hosted version that I can use if i have run out of other options.

### OSX

I consider using [MacPass](https://github.com/mstarke/MacPass) which looks good (I don't currently use it) - it has a builtin keepasshttp server which would be convenient for everyday browsing. Some alternatives would be [Keeweb](https://github.com/antelle/keeweb), [Keepass2](http://keepass.info/) (if i can get it to run using mono), and [KeepassX](https://www.keepassx.org/).

### Alternatives

I think [Keepass2](http://keepass.info/) is a great open source solution, but it the sheer number of projects I have to trust for something this critical is somewhat of a problem. I can appreciate why [LastPass($)](https://lastpass.com/) is an attractive solution. [Keeweb](https://github.com/antelle/keeweb) could potentially solve this as it is truly cross platform. [KeepassX](https://www.keepassx.org/) is also multi platform, and is much leaner than the other desktop tools clients on this page. E.g. [Keeweb](https://github.com/antelle/keeweb) uses node.js and electron (which is huge), and [Keepass2](http://keepass.info/) relies on mono/dotnet framework (also huge). [Keeweb](https://github.com/antelle/keeweb) is the only solution which can run in a browser. So if you anyway have to trust it for that, then you might as well trust it for desktop. KeepassX and Keeweb do not support keepasshttp out of the box, which is a no-go for me. Keeweb has it on the todo list though.

For a completely different solution I would probably look at [passwordstore](https://www.passwordstore.org/).

### Backup

A password database contains so much critical info, that it is essential to set up a backup/restore solution for it.

Recently, two family members have been hit by ransomware. This factored heavily into how I have decided to store, and backup my database. I am also concerned with database corruption. I am would not trust e.g. a dropbox mount to be sufficiently safe. I use [rclone](http://rclone.org/) to backup my password database immediately to the cloud on every save. For everything else I use [duplicati2](https://github.com/duplicati/duplicati).
