---
title: Guide to inserting iframes or flash in Google Sites
date: 2010-05-25 02:44:00+00:00
author: aslak
banner: /post/2010/frames.jpg
aliases:
- /2010/05/25/guide-to-inserting-iframes-or-flash-in-google-sites/
- /Home/Miscellaneous-Debris/guide-to-inserting-iframes-or-flash-in-google-sites
---

I receive so many email requests on how to insert flash or iframes in Google Sites. I do not have time to answering them as I should also be working once in a while. So i've decided to write this short guide.
<!--more-->
_Note: this page is outdated, but may still be of some use ..._

The way to insert iframes or html hosted in an iframe (such as flash or ) is by using a custom made Google Gadget. Google Gadgets are small xml files where you place custom html. When you start writing your own gadgets then i urge you to read the [google gadget api reference](http://code.google.com/apis/gadgets/docs/reference.html) rather than asking me. It is really quite simple if you know are comfortable with javascript and xml. -And if you are not then i do not think i could explain it to you anyway. I will just say that you should perhaps avoid UserPrefs for your custom gadgets. Google Sites has some problems with userPrefs, these bugs will probably be ironed out over time though.

Disclaimer:

Nothing here is guaranteed to work. In fact most the xml examples here are mostly untested simplifications of some of my working code. If you want to comment on the examples then please use [this thread](http://groups.google.com/group/sites-help-howtoadmin/browse_thread/thread/b4b007450791550e).

Iframe gadget

The simplest example is to make an iframe gadget where the content is simply some web adress. The xml for such a gadget would look something like this:

{{< highlight xml >}}

<?xml version="1.0" encoding="UTF-8" ?>

<Module>

<ModulePrefs title="Iframe test"
  directory_title="iframe test"
  description="iframe"
  author="name" author_email="testing"
  author_link="http://www.glaciology.net"
  scrolling="true"
  category="funandgames">
</ModulePrefs>
<Content type="url"  href="http://news.google.com/news"/>

</Module>
{{< /highlight >}}

Very simple, right? I am sure that most of the ModulePrefs are not even necessary if you dont want to distribute the gadget.

Inserting the gadget in a Google Sites page.

So, you upload this gadget to a place on the web. And then you insert it on your GS-page [insert]-[more]-[Add by URL...].

Javascript gadget

This xml should display a simple javascript alert box. What it illustrates is that 'everything' is allowed. You can easily modify this gadget to have your own html.


{{< highlight xml >}}

<?xml version="1.0" encoding="UTF-8" ?>
<Module>
<ModulePrefs
author="Aslak Grinsted"  
author_link="http://www.glaciology.net"  
scrolling="false" >

</ModulePrefs>  
<Content type="html"><![CDATA[  
 <h1>testing</h1>
 <script type="text/javascript" language="javascript">
   alert('HELLO!');  
 </script>
]]></Content>
</Module>

{{< /highlight >}}

Where to host the gadget?

If you have a public site then you also want to host it a public place. You'd think a filecabinet or as an attachment on a GS-page would be ideal, but unfortunately there is some weird redirection going on that hinders that. I think they may have fixed that though so you'll have to experiment. I've been using google pages myself, but google is terminating google pages at the end of the year. You may want to host your gadget xml files on [google code.](http://code.google.com/hosting/)

Flash gadget using Googles cache feature

The above example shows that you can easily add your own html. This can ofcourse be used to embed flash or other media. However, google has made it possible to use their servers to [cache the flash](http://code.google.com/apis/gadgets/docs/reference/#gadgets.flash) files and thus reducing the load on the servers where the swf files are hosted. Nice right. You should really check the documentation for it though.

Example:
{{< highlight xml >}}

<?xml version="1.0" encoding="UTF-8" ?>
<Module>
<ModulePrefs
description="last.fm player"
author="xxxx"
scrolling="false"
category="funandgames" >
<Require feature="flash" />
</ModulePrefs>
<Content type="html">
<![CDATA[<div id='swfwrapper'></div><div id='message'></div>
<script type="text/javascript" language="javascript">

function myesc(s){
var r=escape(s);
r=r.replace(/\//gi,'%2F');
r=r.replace(/ /gi,'%2520');
return r;
}
var flashvars = {
lang: "en", FOD: "true", expanded: "true",
autostart: false, lfmMode: "playlist", restype: "url",
url: "lastfm://artist/Van Der Phunck/similarartists"
};
var fv=";
for (var prop in flashvars) {
if (fv) fv=fv+'&'
fv=fv + prop + '=' + myesc(flashvars[prop]);
}
var params= {
wmode: "transparent", bgcolor: "fff", allowFullScreen: "false",
allowNetworking: "all", quality: "high", menu: "true",
flashvars: fv
};
var ok = gadgets.flash.embedFlash('http://cdn.last.fm/webclient/s12n/85/lfmPlayer.swf', 'swfwrapper', 9, params);
if (~ok) {  
document.getElementById('message').innerHTML='Error: Could not embed flash player!';  
}  
</script>]]>  
</Content>
</Module>
{{< /highlight >}}