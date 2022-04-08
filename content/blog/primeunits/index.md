---
title: Prime units
date: "2022-02-26T17:04:01.227048"
readtime: 3 mins
tags: ['physics','units']
---

Some ideas on a simple and elegant way to handle physical units and dimensionality when writing physics related software.

I am yet to see a complete and elegant treatment of units in software. Boost and other C++ libraries have some great features, but all fall down on angles. You either treat angles as a physical quantity, but then you end up with the mess of taking the sine, cosine, and tangent of an angle, or, you treat it as a dimensionless quantity, but then you end up with the mess of converting or adding other dimensionless quantities. Additionally, things like bytes, decibels and other variables that just don't fit well in the system.

Enter a new way (to the best of my knowledge anyway) - prime units.

Two simple rules:

- Every physical quantity has an associated integer value
- This integer value must be a unique prime number

Then we can use the trick of prime factorisation and take the Highest Common Factor (HCF or GCD) to simplify units.

Let's see an example, in Python.

First we define some basic physical quantities.
```python
# dimensionless must be 1
UDIMLESS = 1

# must be prime
UTIME = 2
ULENGTH = 3
UMASS = 5
UCURRENT = 7
UTEMP = 11
USUBSTANCE = 13
ULUMINOSITY = 17
```

Then we define a basic type for managing values with units, aptly named `UnitValue`.

```python
from collections import namedtuple
# punit tracks the numerator of the unit
# nunit tracks the denominator of the unit
UnitValue = namedtuple('UnitValue', ['value', 'punit', 'nunit'])
```

Add and subtract are simple operations.
```python
def add(a, b):
    assert a.punit == b.punit
    assert a.nunit == b.nunit
    return UnitValue(a.value + b.value, a.punit, a.nunit)

def subtract(a, b):
    return add(a, UnitValue(-b.value, b.punit, b.nunit))
```

Then we use GCD for multiplication and division.
```python
from math import gcd

def multiply(a, b): 
    punit = a.punit*b.punit
    nunit = a.nunit*b.nunit
    hcf = gcd(punit, nunit)
    return UnitValue(a.value*b.value, punit//hcf, nunit//hcf)

def divide(a, b):
    assert b.value != 0
    return multiply(a, UnitValue(1./b.value, b.nunit, b.punit))
```

We can then see this in action.
```python
# Addition
result = add(
    UnitValue(3.5, UTIME, UDIMLESS),
    UnitValue(1.5, UTIME, UDIMLESS))
assert result.value == 5.0
assert result.punit == UTIME
assert result.nunit == UDIMLESS
```

```python
# Subtraction
result = subtract(
    UnitValue(3.5, UCURRENT, UDIMLESS),
    UnitValue(1.5, UCURRENT, UDIMLESS))
assert result.value == 2.0
assert result.punit == UCURRENT
assert result.nunit == UDIMLESS
```

```python
# Multiplication
result = multiply(
    UnitValue(2.0, ULENGTH*UMASS*UMASS, UTIME),
    UnitValue(1.5, UTIME*UTIME*UMASS, ULENGTH*ULENGTH*UMASS*UCURRENT))
assert result.value == 3.0
assert result.punit == UMASS*UMASS*UTIME
assert result.nunit == ULENGTH*UCURRENT
```

Maybe some libraries out there do this already, but I thought it was a nice way to treat units and hadn't seen it implemented. What I like about it is that it is very simple and easy to extend. New unit - just define the next prime. No need to implement the operations, GCD will work it out for you. The algorithm is quite efficient but ideally this should be done at compile time, that way you also benefit from catching unit mismatch at compile time.

Of course, this example is very limited, but the principle can be taken further. Perhaps I have overlooked something, however it may be worth exploring deeper. To me, this seems much more elegant than the seven base units approach (https://en.wikipedia.org/wiki/International_System_of_Quantities). Luminosity and amount of substance just seem like poor choices for "fundamental" units, although I use them here in this demonstration. In this system we are not restricted to these 7 fundamental units, and we can define any units we want.

I made a GitHub gist with the above example, for those interested: https://gist.github.com/thomasms/ec48dafe6abb55eba011de9211d33399.

This idea came about when trying to introduce a flexible and extensible system for handling physical quantities in a control system for a particle accelerator. EPICS (another post on this) was being proposed to handle the networking and communication protocol but they offered no workable solution for managing units, other than simple strings (no thanks). Credit to my manager at the time, Roland Moser, for pointing out the GCD trick here. Perhaps he wrote this up in a paper by now.