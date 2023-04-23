"""Monty Hall Monte Carlo"""
import numpy as np
from random import randint
from typing import Optional, Tuple
import matplotlib.pyplot as plt


def one_game(swap: Optional[bool] = False, nboxes: Optional[int] = 3) -> int:
    """
    Swap will remove all but your box and one other box.
    Returns 1 if we win, 0 if we lose.
    """
    chosen_box = randint(1, nboxes)
    money_box = randint(1, nboxes)

    first_pick_correct = money_box == chosen_box

    # RESULT table is XOR operation
    # first_pick_correct, swap, win
    #                  0,    0,   0
    #                  0,    1,   1
    #                  1,    0,   1
    #                  1,    1,   0
    # From the above table it seems to suggest
    # that it should indeed be 50-50, but note
    # that the probability of chosing correctly
    # first is 1/n_boxes!
    return int(first_pick_correct ^ swap)


def run_simulation(trials: int, nboxes: Optional[int] = 3) -> Tuple[float, float]:
    """
    Runs the percent chance of success for N trials with swap and N trials without a swap.
    Returns a tuple of the mean win rates for no_swap and swap, respectively.
    """
    no_swap = np.array(
        [one_game(nboxes=nboxes, swap=False) for _ in range(trials)],
        dtype=float,
    )
    with_swap = np.array(
        [one_game(nboxes=nboxes, swap=True) for _ in range(trials)],
        dtype=float,
    )
    return np.mean(no_swap) * 100, np.mean(with_swap) * 100


trials = [
    10,
    20,
    30,
    40,
    50,
    100,
    200,
    300,
    400,
    500,
    1_000,
    2_000,
    3_000,
    4_000,
    5_000,
    10_000,
    20_000,
    30_000,
    40_000,
    50_000,
    100_000,
    200_000,
    300_000,
    400_000,
    500_000,
    1_000_000,
]
data = [run_simulation(n, nboxes=3) for n in trials]
no_swaps, swaps = map(list, zip(*data))
print(f"No swap win rate (%) = {no_swaps[-1]:.2f}")
print(f"With swap win rate (%) = {swaps[-1]:.2f}")

fig, ax1 = plt.subplots()
plt.grid(axis="y", alpha=0.75)
plt.axhline(200 / 3, color="g", alpha=0.7, ls="--")
plt.axhline(100 / 3, color="r", alpha=0.7, ls="--")
plt.plot(trials, no_swaps, "r", lw=2, alpha=0.7, label="NO SWAP")
plt.plot(trials, swaps, "g", lw=2, alpha=0.7, label="SWAP")
plt.xscale("log")
ax1.set_xlabel("# of trials")
ax1.set_ylabel("% of success")
plt.legend()
plt.show()
