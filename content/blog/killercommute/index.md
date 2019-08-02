---
title: Killer Commute
date: "2019-03-23T23:46:21.284Z"
---

My daily commute to work is a beast (small exaggeration). If I haven’t left for work before 7:30, I can expect massive queues of manic commuters all the way along my 4 mile journey. Anytime between 7:30 and 9:00 is gridlock. I’ve experienced this many times and sometimes when I’m very keen, I can make it before 7:30, but this is a very rare occurrence.

Thinking I could use technology to help me, or at least to confirm my suspicions, I used Google maps API to get route times. The results are scarily very accurate. If you want to also use their APIs then check out Google API. Note that you’re limited to 2,500 calls within a 24 hour period, but that is more than enough for some simple experiments.

Now, my commute is only 4 miles, but it can take 30 minutes in heavy traffic. So I queried the route times for a typical work day (Thursday, usually the worst day of the week), and looped in increments of 10 minutes over a 24 hour period. Here is the result.

![New setup](./traffic.png)

Indeed at around 8 in the morning it peaks to 30 minutes, just as I experience.

Now time for bed, if I am going to make it before the 7:30 rush!