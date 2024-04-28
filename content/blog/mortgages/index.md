---
title: A short post on mortgages and loan calculations
date: "2022-04-30T15:46:41.976657"
readtime: 3 mins
tags: ['mortgage','loan','finance']
---

I always get annoyed when finacial products are sold to you without any explaination of how they come to these magical numbers. When you question the sales person how these figures came out, they always come back blankly with "it's very complicated but our system does it for us". Hogwash. The problem can always be broken down and understood, it is just they are unwilling to explain it, or normally, simply unable to explain it. I bringeth an example on mortgages.

A friend recently asked me to help understand their mortgage proposal from the bank, and I gladly met the challenge. He explained that the bank produced a spreadsheet with monthly payments but no explaination on how this was calculated and he
 wanted to know how it works.

The main reason for this understanding was so that he could play with the rates and principle amounts without everytime having to ask the bank to "simulate" a new proposal.

It was quite easy to do, once I was given the correct information on the rates and understood how payments are fixed per month. Before I explain the process of how this was done, I will present the formula below.

$$
\alpha_{m} = (1 + \alpha_{y})^{\frac{1}{12}} - 1
$$
$$
X_{m} = \frac{P(1+\alpha_{m})^{n}}{\sum_{i}^{n}{(1+\alpha_{m})^{i}}}
$$

Where $X_{m}$ is the monthly payment, $P$ is the loan principle (how much you want to borrow from the bank), $\alpha_{y}$ is the annual interest rate, $\alpha_{m}$ is the monthly interest rate, and $n$ is the number of payment periods.

Below is a python function to compute this for you, with some tricks to deal with rounding.
```python
def get_interest_per_month(interest_rate_per_year: float) -> float:
    interest_rate_per_month = (1.0 + interest_rate_per_year) ** (1.0 / 12.0)
    # we do not consider anything more than 1e-5 for rate
    interest_rate_per_month = round(interest_rate_per_month, 5)
    return interest_rate_per_month - 1


def get_monthly_payment(
    principle: float, interest_rate_per_year: float, period_in_years: int
) -> float:
    """
    Takes the interest rate per year and the number of years and calculates the monthly payment.
    The interest rate is converted to a monthly rate.
    """
    period_in_months = period_in_years * 12
    interest_rate_per_month = get_interest_per_month(interest_rate_per_year) + 1.0
    d = sum(interest_rate_per_month**i for i in range(period_in_months))
    # anything less than a penny is dropped
    return (
        int((principle * (interest_rate_per_month**period_in_months) / d) * 100) / 100
    )
```