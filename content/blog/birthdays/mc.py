import os
from random import randint
import math
import numpy as np
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# gs_font = fm.FontProperties(
#                 fname='/System/Library/Fonts/Supplemental/GillSans.ttc')
thisdir = os.path.dirname(os.path.realpath(__file__))
plt.style.use(os.path.join(thisdir, 'style.mplstyle'))

def generate_birthday():
    """Generate an integer in [1, 365] uniform dist"""
    return randint(1, 365)


def count_until_match():
    birthdays = [generate_birthday()]

    while birthdays[-1] not in birthdays[:-1]:
        birthdays.append(generate_birthday())

    return len(birthdays)

def mc(nsamples=1000):
    return [count_until_match() for _ in range(nsamples)]

def prob_no_match(n):
    """analytical result using integers - python can handle arb large numbers"""
    return math.factorial(n)*math.comb(365,n)/(365**n)

def plot_actual(logy=False, show_match=True, show_no_match=True):
    x = range(1, 366)
    y = [prob_no_match(n) for n in x]
    y2 = [1 - prob_no_match(n) for n in x]

    fig, ax1 = plt.subplots()
    plt.title('Birthday problem')

    if show_no_match:
        ax1.plot(x, y, 'r', lw=2, alpha=0.7, label='no match')
    if show_match:
        ax1.plot(x, y2, 'g', lw=2, alpha=0.7, label='match')
    plt.grid(axis='y', alpha=0.75)

    ax1.set_xlabel('People')
    ax1.set_ylabel('Probability')
    xmax = 100
    ax1.set_xlim(1, xmax)
    ax1.set_ylim(0, 1)
    if logy:
        ax1.set_ylim(1e-150, 10)
        ax1.set_yscale('log')
        ax1.set_xlim(1, 365)
    else:
        n50 = 23
        ax1.axhline(0.5, xmin=n50/xmax, color='k', alpha=0.7, ls='--')
        ax1.axvline(n50, ymax=0.5, color='k', alpha=0.7, ls='--')

    plt.legend()

    return fig, [ax1, ax2]

def plot_mc(x, show_true=False, show_approx=False):
    people = days = np.arange(1, 366)
    xmax = 100

    hist, _ = np.histogram(x, bins=people)
    # these are %
    cumulative = np.cumsum(hist)*100./sum(hist)

    fig, ax1 = plt.subplots()

    n, bins, patches = ax1.hist(x=x, bins=people, color='blue',
                                alpha=0.4, rwidth=0.75, ec='black')
    plt.grid(axis='y', alpha=0.75)

    ax1.set_xlabel('Value')
    ax1.set_ylabel('Count')
    plt.title(f'N={len(x)}')
    ax1.set_xlim(1, xmax)

    maxfreq = n.max()
    ax1.set_ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

    ax2 = ax1.twinx()
    miny2, maxy2 = [0.0, 110.]
    ax2.set_ylim(miny2, maxy2)

    ax2.plot(days[:-1], cumulative, c='green', lw=2, alpha=0.8)
    ax2.set_ylabel('% of people until same birthday')

    def mark_prop_line(pct, colour='red'):
        # index of when we cross pct% chance
        ipeople = next((i for i, c in enumerate(cumulative) if c > pct), -1)
        ax2.axhline(pct, xmin=days[ipeople]/xmax, color=colour, alpha=0.7, ls='--')
        ax2.axvline(days[ipeople], ymax=pct/maxy2, color=colour, alpha=0.7, ls='--')
        plt.text(80, pct+1, f'$p={pct}%$, $\mu={days[ipeople]}$')
    
    mark_prop_line(50, colour='red')
    mark_prop_line(70, colour='orange')
    mark_prop_line(95, colour='yellow')
    mark_prop_line(99, colour='purple')

    if show_true:
        # using approximation of expontential
        approx = (1 - np.exp(-people*people/(2*365)))*100.
        ax2.plot(days, approx, c='pink', lw=1, alpha=0.3)

    if show_approx:
        # using approximation of expontential
        approx = (1 - np.exp(-people*people/(2*365)))*100.
        ax2.plot(days, approx, c='pink', lw=1, alpha=0.3)

    return fig, [ax1, ax2]

N = 1000
values = mc(nsamples=N)

fig, [ax1, ax2] = plot_mc(values)
fig, [ax1, ax2] = plot_actual()
fig, [ax1, ax2] = plot_actual(logy=True, show_match=False)

plt.show()