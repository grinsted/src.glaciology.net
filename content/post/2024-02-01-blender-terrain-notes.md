---
title: Blender terrain workflow notes
date: 2024-02-01T05:24:00+00:00
author: aslak
banner: /2024/blender_egrip.jpg
---

Here are some personal notes for how to make elevation models using Blender. 

* install the BlenderGIS plugin.
* (optional) import geotiff with 
* import using geotiff "DEM as a displacement texture". 
* Scale the model down by a factor 1000. (km to m.) 
the dome at EGRIP).
* Offset the model so that (0,0,0) is a point of interest. E.g. the dome.
* Decide on a vertical scaling
* Tune the models subdiv modifier to have sufficient resolution for the viewport/render. You can use e.g. loop cuts to have non-uniform resolution
* Add a sky texture to the World. That will also be the light source. ( Delete other lights)
* Switch to Cycles renderer
* Place the camera. 
* Add a snow-material to the model (using the shading tab).

In the render above i used a coarse UV sphere for the dome, and a cylinder for the scale bar. The ground-plane was added with a 10km checker board texture.