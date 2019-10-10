MIN = 60
HOUR = 60*MIN
DAY = 24*HOUR
WEEK = 7*DAY
MONTH = 365.25*DAY/12

DATA = [
    {
        'year': 2000,
        'price': 87,
        'attendance': 100000,
        # five months?
        'sellouttime': 5*MONTH
    },
    {
        'year': 2002,
        'price': 97,
        'attendance': 140000,
        # two months?
        'sellouttime': 2*MONTH
    },
    {
        'year': 2003,
        'price': 105,
        'attendance': 150000,
        # under 24 hours
        'sellouttime': 18*HOUR
    },
    {
        'year': 2004,
        'price': 112,
        'attendance': 150000,
        # 23 hours?
        'sellouttime': 23*HOUR
    },
    {
        'year': 2005,
        'price': 125,
        'attendance': 153000,
        # 3 hours?
        'sellouttime': 3*HOUR
    },
    {
        'year': 2007,
        'price': 145,
        'attendance': 177500,
        # 1 hour 45 mins
        'sellouttime': 1.75*HOUR
    },
    {
        'year': 2008,
        'price': 155,
        'attendance': 177500,
        # did not sell out - 6 months
        'sellouttime': 6*MONTH
    },
    {
        'year': 2009,
        'price': 175,
        'attendance': 177500,
        'sellouttime': 4*MONTH
    },
    {
        'year': 2010,
        'price': 190,
        'attendance': 177500,
        'sellouttime': 12*HOUR
    },
    {
        'year': 2011,
        'price': 200,
        'attendance': 177500,
        'sellouttime': 4*HOUR
    },
    {
        'year': 2013,
        'price': 210,
        'attendance': 177500,
        'sellouttime': 1.67*HOUR
    },
    {
        'year': 2014,
        'price': 215,
        'attendance': 177500,
        'sellouttime': 1.29*HOUR
    },
    {
        'year': 2015,
        'price': 225,
        'attendance': 177500,
        'sellouttime': 25*MIN
    },
    {
        'year': 2016,
        'price': 233,
        'attendance': 177500,
        'sellouttime': 30*MIN
    },
    {
        'year': 2017,
        'price': 243,
        'attendance': 177500,
        'sellouttime': 50*MIN
    },
    {
        'year': 2019,
        'price': 253,
        'attendance': 177500,
        'sellouttime': 36*MIN
    },
    {
        'year': 2020,
        'price': 270,
        'attendance': 203000,
        'sellouttime': 34*MIN
    },
]

active_years = [entry['year'] for entry in DATA]
actual_years = range(active_years[0], active_years[-1], 1)
missing_years = sorted(list(set(actual_years) - set(active_years)))
missing_year_indices = [actual_years.index(y) for y in missing_years]
print(missing_years)
print(missing_year_indices)

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

times = []
prices = []
sellouttimes = []
for d in DATA:
    times.append(d['year'])
    prices.append(d['price'])
    sellouttimes.append(d['sellouttime'])

# sellout times - show missing years with dash line
f = plt.figure()

# break up into festival and fallow years
# not a good way to do this - can we have an algorithm to do this?
plt.plot(times[:2], sellouttimes[:2], 'k', linestyle=":",
    marker='o', markersize=10, alpha=0.8, label="fallow years", linewidth=4.)
plt.plot(times[1:5], sellouttimes[1:5], 'k', linestyle="-",
    marker='o', markersize=10, label='festival years', alpha=0.8, linewidth=4.)
plt.plot(times[4:6], sellouttimes[4:6], 'k', linestyle=":",
    marker='o', markersize=10, alpha=0.8, linewidth=4.)
plt.plot(times[5:10], sellouttimes[5:10], 'k', linestyle="-",
    marker='o', markersize=10, alpha=0.8, linewidth=4.)
plt.plot(times[9:11], sellouttimes[9:11], 'k', linestyle=":",
    marker='o', markersize=10, alpha=0.8, linewidth=4.)
plt.plot(times[10:15], sellouttimes[10:15], 'k', linestyle="-",
    marker='o', markersize=10, alpha=0.8, linewidth=4.)
plt.plot(times[14:16], sellouttimes[14:16], 'k', linestyle=":",
    marker='o', markersize=10, alpha=0.8, linewidth=4.)
plt.plot(times[15:17], sellouttimes[15:17], 'k', linestyle="-",
    marker='o', markersize=10, alpha=0.8, linewidth=4.)

plt.axhline(y=0.5*HOUR, color='r', alpha=0.3)
plt.text(2011, 0.52*HOUR, "30 mins", fontsize=12)
plt.axhline(y=HOUR, color='r', alpha=0.3)
plt.text(2011, 1.02*HOUR, "1 hour", fontsize=12)
plt.axhline(y=DAY, color='r', alpha=0.3)
plt.text(2011, 1.1*DAY, "1 day", fontsize=12)
plt.axhline(y=MONTH, color='r', alpha=0.3)
plt.text(2011, 1.1*MONTH, "1 month", fontsize=12)
plt.axhline(y=6*MONTH, color='r', alpha=0.3)
plt.text(2011, 6.1*MONTH, "6 months", fontsize=12)
ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.tick_params(axis='both', which='major', labelsize=14)
# ax.tick_params(axis='both', which='minor', labelsize=14)
plt.xlabel('year', fontsize=18)
plt.ylabel('sellout time (s)', fontsize=18)
plt.yscale('log')
plt.legend()

# price
f = plt.figure()
plt.plot(times, prices, 'k', label='£', alpha=0.8, linewidth=4.)
ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.tick_params(axis='both', which='major', labelsize=14)
# ax.tick_params(axis='both', which='minor', labelsize=14)
plt.xlabel('year', fontsize=18)
plt.ylabel('price (£)', fontsize=18)
# plt.yscale('log')
# plt.legend()

plt.show()