---
title: Monty Hall meets Monte Carlo
date: "2022-04-30T15:47:36.774654"
readtime: 3 mins
tags: ['monte carlo','probability','maths', 'monty hall']
---

We've all heard the famous Monty Hall problem (https://en.wikipedia.org/wiki/Monty_Hall_problem), or at least, some variation of this. You are shown 3 boxes, 1 has a money prize in it while the other two have nothing - nada, zilch. Of course, you need your car fixed so you want the box with the cash in it, so you choose a box, and one third of the time (on average) you win - not great odds, right? But the twist is that after you choose one box, it is not opened, the presenter elimantes one of the remaining two boxes (knowing which one has cash in it), and gives the option to swap or stay with your box with this new knowledge. The question is, is it better to swap or stick with your original box?

The optimal option is indeed to swap, giving you 2/3 chance of wining. This is the counter-intuative result, as naively, and incorrectly, you would think (and as many mathematicians have also reasoned), that it is a 50-50 chance, regardless of this new information - a box without cash was removed. Well this new information does in fact actually swing your odds to 2/3 of winning, by changing boxes.

The purpose of this post is not to show the standard reasonings shown everywhere on the internet, but instead illustrate this result via experiment, i.e. via Monte Carlo simulations. So Monty Hall meets Monte Carlo.

In python we can write a simple function to simulate one game using uniform distribution sampling.
```python

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
```



Note that the rate of not swapping + swapping does not exactly equal 100% because these are two different statistical experiements, one for control and one the result. As we increase the number of trials we do see them converge to close to 100% but ....