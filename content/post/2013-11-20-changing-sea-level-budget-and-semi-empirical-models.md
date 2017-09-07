---
title: Changing Sea level budget and Semi-Empirical models
date: 2013-11-20T01:39:00+00:00
author: aslak
banner: /2013/11/unfair_scale_1_by_rick__hunter.jpg
tags:
  - sea level
  - semi-empirical
  - slr
aliases:
  - /2013/11/20/changing-sea-level-budget-and-semi-empirical-models/
  - /Home/Miscellaneous-Debris/changingbalanceofthebudgetandsemi-empiricalmodels
---
It is expected that the balance of the sea level budget will change in the future as the slow giants of the ice sheets awaken. This has been leveled as a criticism of semi-empirical models. For that reason people sometimes (wrongly) argue that "_the data used to derive the model, do not contain the effect of the processes, which we expect in the future to dominate_". Here I demonstrate that this argument is flawed using an extremely simplified conceptual model.
<!--more-->
Featured image from Ali Almossawi's [Illustrated Book of Bad arguments](https://bookofbadarguments.com/):

## Conceptual Model:

I assume that the contributions from steric, glaciers and icesheets are all responding linearly to global average warming. This is the model:

```
stericRate   = (T-mean(T<sub>1940:1960</sub>))/700
icesheetRate = (T-mean(T<sub>1950:1970</sub>))/300
glacierRate  = (T-mean(T<sub>1880:1900</sub>))/2000
```

where T is global mean temperature in degC. This means that the rate of total sea level rise will also be proportional to warming (see footnote 2). Thus in this idealized world we know that the [Rahmstorf (2007)](http://www.sciencemag.org/content/315/5810/368.short) model is 100% correct.

For convenience I use EC-EARTH model temperatures as T (as they cover both past and future).

Please note this model is not designed to be realistic but just demonstrate that the premise of the argument presented above is flawed.

#### Footnote 1: Why three different baseline temperatures?

In the conceptual model there are three different baseline temperatures / equilibrium temperatures. One might ask how realistic is that.

In the real world the three contributors have different sensitivities and different response times, and the model would only be an approximation. The slow giants of the ice sheets have a long response time compared to the glaciers. This means that at the end of the Little Ice Age then we must expect the glaciers to be much closer to equilibrium than the ice sheets which will still have some memory of the medieval warm period. I.e. we will expect that the glacier equilibrium temperature would be colder than the equilibrium temperature for the ice sheets. This is the motivation for choosing different baseline temps in the model.

We can argue about how much memory each contributor exactly has, but the point is that their response times are different, and in turn that different baselines are to be expected.

**Footnote 2: Equivalence with Rahmstorf 2007:**

GSL_Rate = stericRate + icesheetRate + glacierRate

= (T-T<sub>1</sub>)_a<sub>1 </sub>+ (T-T<sub>2</sub>)_a<sub>2 </sub>+ (T-T<sub>3</sub>)_a<sub>3</sub>

= T_(a<sub>1</sub>+a<sub>2</sub>+a<sub>3</sub>) - T<sub>1</sub>_a<sub>1</sub> - T<sub>2</sub>_a<sub>2</sub> - T<sub>3</sub>_a<sub>3</sub>

= (T-T<sub></sub>)_a

where

  * T<sub>1</sub>=mean(T<sub>1940:1960</sub>)
  * T<sub>2</sub>=mean(T<sub>1950:1970</sub>)
  * T<sub>3</sub>=mean(T<sub>1880:1900</sub>)
  * a<sub>1</sub>=1/700
  * a<sub>2</sub>=1/300
  * a<sub>3</sub>=1/2000
  * a = a<sub>1</sub>+a<sub>2</sub>+a<sub>3</sub>
  * T<sub>0 </sub>= (T<sub>1</sub>*a<sub>1</sub> + T<sub>2</sub>*a<sub>2</sub> + T<sub>3</sub>*a<sub>3</sub>)/a

## Output

The model output shows that the dominating contributor changes between the 20th and 21st centuries and yet we know that in this idealized world the Rahmstorf 2007 model works. This demonstrates that this particular argument against semi-emprical models is fundamentally flawed. Semi empirical models of sea level rise can be perfectly consistent with a shift in dominance.

![](/2016/02/conceptualmodel.png)

*Note only temperature is output from EC-EARTH. The pie charts are based on the conceptual model on this web page.

### No good data on past ice sheet contribution.

Finally, there is very [little data on past ice sheet contributions](/Home/Miscellaneous-Debris/icesheetsandsemi-empiricalmodel), and that is another reason why I have serious problems with the argument "_the data used to derive the model, do not contain the effect of the processes, which we expect in the future to dominate_". To make this argument you have to know know how ice sheets behaved throughout the 19th and 20th centuries. How could they possibly know this?


**Matlab example:**

{{< highlight matlab >}}
T=load('global_tas_Amon_EC-EARTH_rcp45_ave.dat');
t=T(:,1);
T=mean(T(:,2:13),2)-286;
plot(t,T)
stericRate=(T-mean(T(ismember(t,1940:1960))))/700;
icesheetRate=(T-mean(T(ismember(t,1950:1970))))/300;
glacierRate=(T-mean(T(ismember(t,1880:1900))))/2000;
close all
subaxis(2,2,1,1,2,1,'sv',.2)
plot(t,T);
title('EC-EARTH modelled temperature')
subaxis(2,2,1,2)
ix=find(ismember(t,1900:2000));
rates=mean([stericRate(ix) icesheetRate(ix) glacierRate(ix)]);
pie(rates*1e8,{'steric' 'icesheet' 'glaciers'})
title('20th C SLR contributions')
subaxis(2,2,2,2)
ix=find(ismember(t,2000:2100));
rates=mean([stericRate(ix) icesheetRate(ix) glacierRate(ix)])
pie(rates*1e8,{'steric' 'icesheet' 'glaciers'})
title('21st C SLR contributions')
colormap jet

{{< /highlight >}}
