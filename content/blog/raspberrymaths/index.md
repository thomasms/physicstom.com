---
title: Raspberry maths
date: "2021-05-25T21:37:24.284Z"
readtime: 6 mins
tags: ['rasberry', 'pi', 'cost']
---

![raspberry](./raspberry.jpeg)

I love raspberries but they are certainly not cheap. While it is not sustainable for me to eat them everyday, the occasional punnet is a nice treat every now and then. The last time I went to buy some (last week) they were 3 EUR a punnet (2.99 EUR to be exact but who counts the pennies?). They usually contain between 15 and 20 raspberries based on some rather rough observation. Given a raspberry efficiency of $ \alpha = 0.85$ I calculate the cost at roughly 0.18 EUR per raspberry, that's not cheap. It may be worth comparing to other fruits to back this claim up but that's maybe for another time. 

You may be wondering what I mean with raspberry efficiency? This strict scientific definition is of course the fraction of non-mouldy and edible raspberries for each punnet. Unless you eat them straight after purchase I can guarantee that you never have $\alpha = 1$. Anyone who has left raspberries in the fridge for a few days will know what I am talking about. Of course I am (very roughly) estimating my efficiency here as an average, that is, 8.5 out of 10 raspberries are good to eat and not mushy or mouldy - I know you can't have half a raspberry but this is on average depending on my eating habits, and depending on how long after purchase I eat them. I could take into account the expontential decay of them as a function of time, but that's just insane!

Recently I find myself buying them quite frequently, once or twice a month perhaps, and definitely much more in season. Let's say on average per month I buy 2 punnets (I am not actually sure if you call them punnets for a collection of raspberries but anyway back to raspberry maths...) that is 24 per year costing me 72 EUR (71.76 EUR to be exact), indeed not a cheap habit, especially for something that leaves me more hungry after eating them. We are assuming that the cost of raspberries are constant and they are inflation proof - something anyone who has been to the supermarket lately can tell me is certainly not the case, but I am not doing a supply chain analysis right now.

Well instead of comparing this to other fruit, why not compare it to another type of raspberry, the non-ediable one, namely the Raspberry Pi.

![raspberrypi](./raspberrypi.jpeg)

After recently purchasing the Raspberry Pi 4 I am leaving it on permanently to run 24/7 and use it for a private server on my home network (amongst other things). But after a few days I began to wonder if I would be in for a nasty shock when I got my next electricity bill, so I decided to do some more raspberry maths. To figure out the cost of running one of these bad boys for a whole year 24/7 we first need to know a few things:

- Cost of one kWh ($\beta_{kWh}$)
- Voltage of the Pi power supply ($V$)
- Current drawn by the Pi ($A$)

The first two we can assume are constant with time, with the first dependent on your provider, and the second fixed at 5.1 V (the same for all Raspbeery Pi versions). The last one, however, will change with time, depending on what we are doing. Since I do not have any way to measure the current I must make some assumptions and use some external data to help me here. Looking at various websites and blog posts of people measuring current as a function of load and idle, I assume that the idle current is 600 mA with more than double that for on-load, at 1400 mA. We denote these as $A_{idle}$ and $A_{load}$ respectively.

Note I turned off the HDMI, Wifi and USB (all of which are controlled with systemd - see [this create post (external)](https://frederik.lindenaar.nl/2018/05/11/raspberry-pi-power-saving-disable-hdmi-port-and-others-the-systemd-way.html) for more details on how to do that). So in actuality my current estimates may be too high, but I'd rather this than estimate it too low.

So we can write the cost of running for a year $\beta_{year}$ with $\lambda_{idle}$ fraction of the time in idle and $\lambda_{load}$ of the time on load as below. Obviously $\lambda_{idle} + \lambda_{load} = 1$. Remember from school physics that power is voltage $\times$ current ($P = VI$).

$$
\beta_{year} = \beta_{kWh}V(\lambda_{idle}A_{idle} +  \lambda_{load}A_{load})\tau \times 10^{-3}
$$

Where $\tau$ is the number of hours in a year ($365 \times 24 = 8760$), since we have our cost in kWh, and the factor $10^{-3}$ is because we want kW not W.

OK so now for some numbers - we know $V, A_{idle}, A_{load}$ and $\tau$ - but we don't know $\beta_{kWh}$ or $\lambda_{idle}$ or $\lambda_{load}$. The last two will be specific to the use case but since my Pi does not actually do much most of the day (bar a few small cron jobs and the odd computation/simulation) I can assume $\lambda_{idle} = 0.95$ and $\lambda_{load} = 0.05$.

Finally, my cost of one kWh is 0.18 EUR so I get the grand cost of 5.15 EUR / year to run it - less than 2 punnets of real raspberries or roughly 29 edible raspberries in total. I think that's pretty cheap. 

To be clear here is the final calculation, with numbers in place of the symbols in the equation above.

$$
\beta_{year} = 0.18 \times 5.1 \times ((0.95 \times 0.6) + (0.05 \times 1.4)) \times 8760 \times 10^{-3}
$$

$$
\beta_{year} = € 5.15
$$

$$
\beta_{year} = 29 \textrm{ Rs}
$$ 

Where, Rs is the number of raspberries.

Feel free to play with the numbers below to see how much it costs you! Move the range bar to the left for more idle and right for more load.
<form oninput="x.value=parseFloat(parseFloat(a.value)*0.44676*(1.4*parseFloat(b.value)+0.6*(100-parseFloat(b.value)))).toFixed(2);r.value=parseFloat(parseFloat(x.value)*5.55).toFixed(0)">

Idle <input type="range" id="b" value="5"> Load 

Cost of one kWh = <input type="number" value="0.18" id="a" name="quantity" min="0" step="0.01"/>

<b>Cost per year</b> = &#8364;<output name="x" for="a b">5.15</output> or <output name="r" for="a b">28.6</output> Rs
</form>

Update: As someone has pointed out, I failed to take into account the cost of the machine itself (about &#8364;80) and the expected life expectancy. Assuming it would last for 5 years then that does indeed put our cost up to about &#8364; 21/22 per year. Still small compared to the equivalent setup on the cloud!
