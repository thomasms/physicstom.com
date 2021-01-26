---
title: I don't like ifs
date: "2021-01-13T21:52:24.284Z"
readtime: 8 mins
tags: ["software", "SOLID", "programming"]
---

The `if` statement is fundamental to programming, a core tool in the arsenal of any developer existing today. Hell, I cannot even think of a language that doesn't use them. Well, actually literally after typing that I did a quick bit of research (i.e. Google and Stack Overflow) and came across a few: **Smalltalk**, **Prolog**, and someone mentioned **Haskell**, but I know this not to be true (from the small amount of Haskell I have written - not a lot - I definitely used an if). Given there are over 700, _and counting_, programming languages at the time of writing, almost all of which have an <b><code>if</code></b> construct, then I think you'll all agree it is a 'core', and arguably fundamental, statement. So why do I dislike them?

Let's start by with a standard example (Python code).

```python
def calc_coeff(a, b, c):
    if b == 0:
        return 0
    return (a*6.54 - c)**0.78/b
```

I am sure we have all seen code like this - well not exactly like this contrived example, but similar I am sure - the divide by zero check. I've seen this sort of code everywhere in numerical and scientific based software. Most developers at least check for this in advance but quite often I find this sort of code **running in production without the if there**. When highlighting this to the developer they usually reply with _"Well we never run it with `b=0`, that's just stupid....."_, and my response is _"Is this documented? Is this restricted elsewhere? Is this covered with a unit test?"_. Of course it is not and it is not at all stupid to think of the case when b=0, because if the interface allows it, then someone will do it.

OK, this is not a great defense case so far, the `if` here is very valuable, and I argue is needed in this case (but bear with me). Depending on the requirements it may actually be better to throw an exception here, or log an error, or something else, but returning 0 could be a valid result for `b = 0`, if this is well understood and documented to the caller. Indeed, these types of `if`s can be very useful and sometimes unavoidable. I call these `if`s **`if`s of the first kind** and we can allow them.

Similarly, we have cases of `if`s where we want to do null checking, which follow the same pattern.

```python
def calc_coeff2(obj, b, c):
    if obj is None:
        return 0
    return obj.a*b*2.1/(c-0.8)
```

In this case we want to make sure `obj` exists and has a valid place in memory - in C++ we would do a null pointer check maybe, or in Javascript we want to check the thing is not undefined. Again, for this function it could be a valid case, we don't want to access a null pointer. One complaint with this version is if we designed the function and code architecture better you wouldn't need a null check. Avoid pointers in C++ by convention and only deal with references, for example, is one way around this, but could restrict you later on - pointers have their uses. In the python example we could by design ensure that obj is never `None`, or better, don't pass in the `obj` to the function, just pass in the parameter `a` instead. For one, it is easier to test and makes it clearer to the caller. But this is a seperate discussion, let's get back on track to the really bad `if`s - the ones involving their ugly, dirty siblings: `else` and the dirtiest of all - `else if`!

Let's start with `else`. Well there is rarely a case for them. I argue that this can always be reduced to a simple if by separating the code into a small function. For example, let's say we have the following function.

```python
def my_cool_func(a, b, c):

    d = a*b + c
    e = 5.4*c
    # some more variables and calculations ...

    f = 0.0
    if d < e:
        f = 7.8*a
    else:
        f = 9.6*a*d

    # do something with f
    g = f*7.1

    return g*3.6
```

Whilst this example is rather contrived and abstract, I seen stuff like this running in lots of different code bases, essentially the `else` adds no value to the code and just makes it more complex. What would be better is just to remove the else and initialise `f` with the value in the `else` part. Of course the exception here is if we wanted to condense this onto one line when we initialise `f`. In python (and C++, Javascript, etc) we can use the ternary operator for conciseness, and to me this is the one exception for an `else`. For example, we can use the following simple one liner, which I think is acceptable and easier to read.

```python
f = 7.8*a if d < e else 9.6*a*d
```

Although I do prefer the simpler notation (Javascript):

```javascript
const f = d < e ? 7.8 * a : 9.6 * a * d
```

So, what happens now if we can't do this because the initialisation is conditional or the part in the `else` is a complex calculation which is ultimately not needed? Both valid cases, let's look at the first case first.

```python
def my_cool_func(a, b, c):

    # same as before ...

    f = 0.0
    if d < e:
        f = 7.8*a
    else:
        if b == 0.0:
            f = 1.0
        else:
            f = 9.6*a*d

    # same as before ...

    return g*3.6
```

Now we have an `if` in an `if`, whilst the code looks messy and hard to read (what we want to avoid) it could be a valid case. Maybe `f` really does depend on the other parameters and has a few different cases. Well, in this case it is simple - clean and refactor - make a smaller function to compute `f` first and use this function in the code. It is clear that in the above example, there are three unique cases to cover and probably have some domain knowledge or logically reasoning behind this. Therefore, it seems natural to describe these in separate functions with accurate names of what they do.

```python
def calc_f_critical(a, b, c):
    return 1.0

def calc_f_subcritical(a, b, c):
    return 7.8*a

def calc_f_exceptional(a, b, c):
    d = a*b + c
    return 9.6*a*d
```

Putting this back into the previous big function we have:

```python
def my_cool_func(a, b, c):

    # ...

    f = 0.0
    if d < e:
        f = calc_f_subcritical(a,b,c)
    else:
        if b == 0.0:
            f = calc_f_critical(a,b,c)
        else:
            f = calc_f_exceptional(a,b,c)

    # ...

    return g*3.6
```

which isn't much of an improvement but it is already a bit clearer, and now if I want to change the logic for one calculation I don't have to edit `my_cool_func`. However, this still doesn't address the issue of the `if`s and you may have noticed that we have kept the interface the same for each function, even though most of the don't use `a`, `b`, or `c` in their computation. This however can be used to remove the `if`s.

We can define a mapping between the conditions and the functions which would keep the logic the same but make it much more readable.

```python
f_mappings = [
  {
    "func": calc_f_critical,
    # this is d <e written in terms of a,b,c
    "condition": lambda a,b,c: a*b + c < 5.4*c
  },
  {
    "func": calc_f_subcritical,
    # this is d <e written in terms of a,b,c
    "condition": lambda a,b,c: (a*b + c >= 5.4*c) and (b == 0.0)
  },
  {
    "func": calc_f_exceptional,
    # this is d <e written in terms of a,b,c
    "condition": lambda a,b,c: (a*b + c >= 5.4*c) and (b != 0.0)
  },
]
```

Now at back to the original function we can write it with just one `if`.

```python
def my_cool_func(a, b, c):

    # same as before ...

    funcs = [x['func'] for x in f_mappings if x['condition'](a,b,c)]
    values = [func(a,b,c) for func in funcs]
    # here we assume only one condition is met, take the first
    f = values[0] if len(values) > 0 else 0.0

    # same as before ...

    return g*3.6
```

Now compare this to our starting version with the three conditional cases and the nested `if`s - it is clearly different in terms of readability - which I think is a notable improvement. Additionally, it is a few less lines at the call site (but indeed more code lines overall), however we have now done something very important, we have moved the logic out of `my_cool_func` for different scenarios and into separate identifiable functions. The clear benefits are then modular code, easy to read, and most importantly, easier to extend - what if we want to add a new condition? We change the mappings and add a new condition with its own function. The previous way would mean changing the big nested `if` statement, which in this case is managable, but imagine dealing with lots of these things littered everywhere in your code, and even worse, the same conditions and logic being used in other complicated functions - then you have high technical debt to pay. I don't want to be paying that debt.

OK, so what are the downsides? Of course, I am sure you're all shouting at me "What about performance?".

- We are iterating through the whole list each time,
- We compute `d` and `e` again and again instead of just once
- We pass in `a`, `b`, and `c` and don't even use them sometimes.

All valid concerns, and indeed this approach will not always work, but it is instead showing you how to approach it in a different manner, a more functional viewpoint. There are cases when this could work and workarounds can be applied - cache `d` and `e`, use `*args` and `**kwargs` instead of passing `a`, `b`, and `c`, etc. The idea is to redesign code to keep it extensible but closed for modification, all the time making use of **polymorphism** (polymorphic functions). In the long run, your code base will be easier to maintain and cleaner. Always favour small functions with few (if any) `if`s instead of complex, long functions with nested statements.

Oh, and I am sure you all will have noticed that I still have `if`s in the new code and one `else` but the latter is the one exception I said before (ternary operator) and the other `if`s are of the first kind (the acceptable ones).

_Note: If you are really worried about performance and don't want abstractions and additional function calls bloating out run time, then that is a trade off you need to make. My angle is always readability first and performance second. That doesn't mean write pretty but slow code, it means always think in terms of readability first. You never know before hand where the performance bottlenecks will be and you could waste time trying to optimize a function when it is rarely used. Additionally, with a series of nested conditional statements it could really matter the order in which you define them, which will depend on your requirements and use cases. If you are hitting the last conditional statment 90% of the time, then it is better to reorder to avoid conditional checking everytime._

Also I came across this site https://francescocirillo.com/pages/anti-if-campaign which also shares my hatred for them.

<a href="https://francescocirillo.com/pages/anti-if-campaign">
  <img height="60" width="120"
  src="https://cdn.shopify.com/s/files/1/0257/1675/t/154/assets/banner_ive-joined.gif?v=18014947911647769492"
  alt="I have joined Anti-IF Campaign"></a>

I will make a few other follow posts on this soon, regarding the more obvious and common object orientated approach using polymorphic objects (instead of functions) with a common interface to remove all `if`s in the type of code I see all the time. You'll know the code I am talking about, it starts with `switch` and contains about 10+ `case` statements, or even worse a series of `if else` statements. Stay tuned for the horror!
