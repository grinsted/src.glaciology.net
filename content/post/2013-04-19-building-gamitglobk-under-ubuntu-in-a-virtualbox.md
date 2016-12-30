---
title: Building GAMIT/GLOBK under ubuntu (in a virtualbox)
date: 2013-04-19T04:05:00+00:00
author: aslak
layout: post
banner: /2013/04/storm.jpg
categories:
  - Debris
tags:
  - gps
  - Tip
aliases:
  - /2013/04/19/building-gamitglobk-under-ubuntu-in-a-virtualbox/
  - /Home/Miscellaneous-Debris/buildinggamitunderubuntuinavirtualbox
---
Here's what i did (so far):
  
Install linux in a virtualbox. This is where i want to have my GAMIT installation.

  * Install virtualbox
  * Get an xubuntu/kubuntu/ubuntu image from <http://virtualboxes.org> (see also: <https://www.itefix.no/i2/content/turning-ubuntu-1210-minimal-distribution-virtualbox-simplified-secure-lightweight-gui>)
  * change default username/password.
  * (optional) Compilation of gamit/globk takes quite a lot of memory. It will speed up compilation significantly if more memory is given to the virtual machine. I recommend that you give atleast 1.3Gb while compiling.

inside ubuntu do the following:

  * Get GAMIT sources from MIT (you have to check [here](http://www-gpsg.mit.edu/~simon/gtgk/) on how to get access)
  * Install dependencies 
      * sudo apt-get -y update
      * sudo apt-get -y upgrade
      * sudo apt-get -y install build-essential #will install gcc and g++ and gnu-make
      * sudo apt-get -y install gfortran
      * sudo apt-get -y install csh
      * sudo apt-get -y install tcsh
      * sudo apt-get -y install libx11-dev
  * go to the directory where the source files are located. in my case "~/gg" and execute: 
      * chmod +x install_software
      * ./install_software
  * This extracted all the tar files, but eventually failed for me with an error referring to OS_ID.
  * I then edited ~/gg/gamit/Makefile.config 
      * The line where it says "OS\_ID Linux 0001 3000" i changed to "OS\_ID Linux 0001 4000"
      * If your OS is newer than mine, then you might have to make this number even higher.
      * I also modified it to say "X11LIBPATH /usr/lib/i386-linux-gnu" up in the top somewhere.
  * I then executed the ./install_software again, and it seems to be working as it is currently compiling lots of stuff

Additional installs:

  * install GMT from the ubuntu software center
  * install teqc from <http://www.unavco.org/facility/software/teqc/teqc.html>.
  * If you have javad .jps files, then you might want to install this jps 2 rinex converter (although i believe teqc can do the same),  <http://javad.com/jgnss/products/software/jps2rin.html>

Success. And finally the install script gave these instructions:
  
also ~/gg needs to be linked the gamit.
  
You also need to set up the paths in your .cshrc & .bashrc files
  
Create the gg link in your home directory to the version of
  
gamit/globk you just installed ? (y/n)

add this to .bashrc:
  
export PATH=$PATH:~/gg/com:~/gg/gamit/bin:~/gg/kf/bin
  
add this to .cshrc (but replace XYZ with a 3-letter abbrev. for your institute.)
  
setenv HELP_DIR ~/gg/help/
  
setenv INSTITUTE XYZ

## set path =  ($path ~/gg/gamit/bin ~/gg/kf/bin ~/gg/com)

Track still does not work for me. It just says "KILLED". My current theory is that it is due to not enough mem during compile time. Will try to recompile with more memory.
  
UPDATE: track works after a recompile with more memory to the virtual machine.
  
I also found [these instructions in chinese](http://www.linuxidc.com/Linux/2012-07/65433.htm) (use google translate)
  
One more [link](http://en.cnki.com.cn/Article_en/CJFDTOTAL-QUDW200905015.htm).
