---
title: Pypact I
date: "2021-03-27T20:37:24.284Z"
readtime: 6 mins
tags: ['physics', 'fispact', 'FISPACT-II']
---

I'd like to finally spend some time talking about one of my ongoing side projects - pypact. Whilst I have recently been pursuing a variety of different projects (both open and closed source), this one in particularly has taken a fair share of my spare time in the past months. As it happens with everything, this project started out to solve one specific and niche purpose, more as a proof of concept and never intended to go further than that! Something that started out so simple and lightwieght but now seems to have grown arms and legs, with no way of stopping. Actually, it never intended to see the outside world at all, and was purely meant for internal testing only, however fortunately for you (or just the 4 users worldwide) it is an open source project (Apache-2.0). 

OK, so what is pypact? Well if you're not interested in understanding the decay heat in the vacuum vessel of a fusion reactor after 10 years of operation (or nuclear inventory calculations in general) then pypact will be of little interest to you. However, if you are interested in such calculations, and I am hoping you are, then pypact might be a useful library for you. Pypact’s *original aim* was to make FISPACT-II output files easy to parse so that more time can be spent on analysis, and much less time on interrogating the output file (because the output file is an awful thing for a computer to read). No more convoluted scripts, just one simple to use package! If you don't know what FISPACT-II is then I guess you shouldn't have read further than (decay heat in the vacuum vessel .....) but FISPACT-II is an extremely valueable tool to perform such nuclear inventory calculations, amongst other things. Read more on FISPACT-II [here](https://fispact.ukaea.uk/). As I said earlier, however, pypact has evolved beyond its original aim (a simple parser for FISPACT-II), it provides a utility library for FISPACT-II, not just parsing output files, but also writing input files (fluxes, files, inputs), data manipulation, group convert, plotting, and more! Now I am hoping I have got you interested.

Firstly, I should mention it is a pure python library, so if you are not a python enthusiast then I can't really help you there, although Julia bindings would be nice! So unlike FISPACT-II it is not written in Fortran. If you do love python though and love nuclear irradiation, then pypact is for you. Just look at what you can do with a few lines of python and a FISPACT-II output file.

![periodictable](https://github.com/fispact/pypact/blob/master/examples/figures/periodictableanimation.gif) 

![chart of nuclides](https://github.com/fispact/pypact/blob/master/examples/figures/chartofnuclidesanimation.gif)

Of course those animations don't really provide any quantatitive value but can make your presentations look pretty.

Since the documentation for pypact is not great at the current time of writing (check it out [here](https://pypact.readthedocs.io/en/latest/)), I thought this post might help cover some of the basics. With the intention of future posts to show more interesting examples when using pypact.

First, its original purpose - reading a FISPACT-II file.

Let's say you have a FISPACT-II file, named *run1.out* and it looks something like this

```
   TOTAL ACTIVITY EXCLUDING TRITIUM     0.00000E+00 Bq
0  TOTAL ALPHA HEAT PRODUCTION          0.00000E+00 kW
   TOTAL BETA  HEAT PRODUCTION          0.00000E+00 kW
   TOTAL GAMMA HEAT PRODUCTION          0.00000E+00 kW              TOTAL HEAT PRODUCTION 0.00000E+00 kW
0  INITIAL TOTAL MASS OF MATERIAL       1.00000E+00 kg              TOTAL HEAT EX TRITIUM 0.00000E+00 kW
0  TOTAL MASS OF MATERIAL               1.00000E+00 kg
   DEUTERON FLUX DURING INTERVAL        1.00000E+13 d/cm**2/s
0  NUMBER OF FISSIONS                   0.00000E+00                 BURN-UP OF ACTINIDES  0.00000E+00 %



                                               COMPOSITION  OF  MATERIAL  BY  ELEMENT
                                               --------------------------------------
0                                                             BETA                     GAMMA                     ALPHA
                      ATOMS      GRAM-ATOMS     GRAMS      CURIES-MeV      kW        CURIES-MeV      kW        CURIES-MeV      kW

   22       Ti      1.2581E+25   2.0891E+01   1.0000E+03   0.0000E+00   0.0000E+00   0.0000E+00   0.0000E+00   0.0000E+00   0.0000E+00
1 * * * TIME INTERVAL   2 * * * * * * * TIME IS   3.1558E+07 SECS OR  1.0000E+00 YEARS * * * ELAPSED TIME IS   1.000 y   * * * FLUX AMP IS  1.0000E+13 /cm^2/s  * * *
  NUCLIDE        ATOMS         GRAMS        Bq       b-Energy    a-Energy   g-Energy    DOSE RATE   INGESTION  INHALATION   HALF LIFE
                                                        kW          kW         kW         Sv/hr      DOSE(Sv)    DOSE(Sv)    seconds

  H   1    #  2.59134E+21   4.337E-03   0.000E+00   0.000E+00   0.00E+00   0.000E+00   0.000E+00   0.000E+00   0.000E+00     Stable
  H   2    #  2.79642E+20   9.353E-04   0.000E+00   0.000E+00   0.00E+00   0.000E+00   0.000E+00   0.000E+00   0.000E+00     Stable
  H   3       3.87956E+19   1.943E-04   6.911E+10   6.320E-08   0.00E+00   0.000E+00   0.000E+00   2.903E+00   1.797E+01   3.891E+08
  He  3    #  1.37967E+19   6.910E-05   0.000E+00   0.000E+00   0.00E+00   0.000E+00   0.000E+00   0.000E+00   0.000E+00     Stable
  He  4    #  3.87178E+20   2.573E-03   0.000E+00   0.000E+00   0.00E+00   0.000E+00   0.000E+00   0.000E+00   0.000E+00     Stable
  Na 23    #  3.38730E+05   1.293E-17   0.000E+00   0.000E+00   0.00E+00   0.000E+00   0.000E+00   0.000E+00   0.000E+00     Stable
  Mg 24    #  1.84580E+07   7.351E-16   0.000E+00   0.000E+00   0.00E+00   0.000E+00   0.000E+00   0.000E+00   0.000E+00     Stable
  Mg 25    #  2.53133E+08   1.050E-14   0.000E+00   0.000E+00   0.00E+00   0.000E+00   0.000E+00   0.000E+00   0.000E+00     Stable
```
Horrible right?

Well, don't worry about that just simple install pypact by:
```bash
# good to use venvs, of course!
pip3 install pypact
```
and then in a few lines you can print the total decay heat at each timestep by doing the following:

```python
import pypact as pp

filename = "run1.out"

with pp.Reader(filename) as output:
    for inventory in output:
        print(inventory.total_heat) # in kW
```

That's it - 5 lines of code!

We could take this further by only looking at the decay heat of nuclides starting with the letter T, for each timestep in the output. A useless exercise but can show the power of the library.

```python
import pypact as pp

filename = "run1.out"

with pp.Reader(filename) as output:
    for inventory in output:
        heats = [nuclide.heat for nuclide in inventory.nuclides if nuclide.name.startswith('T')]
        print(sum(heats)) # in kW
```

More to examples needed...