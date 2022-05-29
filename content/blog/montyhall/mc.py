"""Monty Hall Monte Carlo"""
import numpy as np
from random import randint
from typing import Optional, Tuple


def one_game(
    swap: Optional[bool] = False, nboxes: Optional[int] = 3
) -> int:
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


def run_simulation(
    trials: int, nboxes: Optional[int] = 3
) -> Tuple[float, float]:
    """
    Runs the MC for N trials with swap and N trials without a swap.
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
    return np.mean(no_swap), np.mean(with_swap)


no_swap, swap = run_simulation(100_000, nboxes=3)
print(f"No swap win rate (%) = {no_swap*100:.2f}")
print(f"With swap win rate (%) = {swap*100:.2f}")
