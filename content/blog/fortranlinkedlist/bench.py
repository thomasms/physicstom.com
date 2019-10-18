import matplotlib.pyplot as plt


# times ran locally on my machine
# 5 repeated runs

entries = [
    100,
    1000,
    10000,
    100000,
    1000000
]

# times in seconds
int_append = [
    0.000087,
    0.000488,
    0.003520,
    0.033809,
    0.348488,
]

simple_derived_type_append = [
    0.000077,
    0.000742,
    0.006558,
    0.079720,
    0.928221
]

# too slow
int_get = [
    0.000030,
    0.001802,
    0.630823
]

# too slow
derived_get = [
    0.000024,
    0.002417,
    0.971309
]


plt.loglog(entries, int_append, 'k', label="append int")
plt.loglog(entries, simple_derived_type_append, 'r', label="append type")
plt.loglog(entries[:len(int_get)], int_get, 'k:', label="get int")
plt.loglog(entries[:len(derived_get)], derived_get, 'r:', label="get type")
plt.xlabel("number of entries")
plt.ylabel("time taken (s)")
plt.legend()
plt.grid()
plt.show()