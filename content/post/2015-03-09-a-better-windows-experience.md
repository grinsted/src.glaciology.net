---
title: A better windows experience
date: 2015-03-09T04:11:00+00:00
author: aslak
banner: /2016/02/Bizcocho_de_chocolate_y_nata.jpg
tags:
  - Tip
aliases:
  - /2015/03/09/a-better-windows-experience/
  - /Home/Miscellaneous-Debris/abetterwindowsexperience
---
### Chocolatey

_update: I'm not currently using it._

[Chocolatey](http://chocolatey.org/) is a package manager sort of like apt-get for windows, or a command-line version of ninite. You can do stuff like:
  
`choco install <packagename>`` `

Usually you have to run choco as an administrator. That means starting the command prompt as an admin. That can get annoying pretty fast, so I recommend installing the sudo package as the next step.
  
`
` 
  
choco install sudo
  
After this you can install a bunch of other stuff using "sudo choco install xxxx" install, without starting an administrative shell.
  
A better terminal, and putty
  
`sudo cinst conemu `
  
I installed putty manually instead of using chocolatey because that makes it easier to get conemu to cooperate with putty.  see also comments [here](https://chocolatey.org/packages/putty)

## SSHFS adds the ability to mount drives over ssh

`sudo cinst win-sshfs`

I recommend installing [FiSSH](https://github.com/tuiSSE/win-sshfs/) instead (a fork of win-sshfs) because it is compatible with pageant. I have not tested if it is better than [this fork](https://github.com/dimov-cz/win-sshfs).

### SublimeText

`sudo cinst SublimeText3`
  
`sudo cinst SublimeText3.powershellalias`

### Python2.xx (& essentials)

For scientific python you might want to try [Anaconda](https://store.continuum.io/cshop/anaconda/) instead of installing python yourself. That is not in the chocolatey.
  
Note this python section is from memory and may not be optimal.
  
`sudo cinst python2`
  
`pip install --upgrade pip`
  
`pip install virtualenv`
  
`pip install virtualenvwrapper-win`
  
If you already have python2, then you might want to remove it first using the control panel.
  
If PIP is not found, then it is most likely a problem with your path.
