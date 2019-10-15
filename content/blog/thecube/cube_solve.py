# -*- coding: utf-8 -*-
"""
The Cube

Number of average steps from node 1 back to node 1
Should be 8!

"""
from math import sqrt
from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

import numpy as np
from numpy.linalg import matrix_power

# matrix of graph of cube
A = np.matrix([[0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0 ],
            [1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0 ],
            [0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0 ],
            [1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0 ],
            [0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0 ],
            [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0 ],
            [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0 ],
            [0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0 ]])
            
# solve it using 8 simulateous equations using 
# n_{1} = average number of steps from one to one
# n_{2} = average number of steps from one to two
# ....
# Since we start at one and must make one step
# The average number of steps from n_{1} will be 
# 1 + the average from adjancent nodes
# 3 options with equal chance means (1/3) from each node
# hence:
# n_{1} = 1 + (1/3)(n_{2} + n_{4} + n_{6})
# similarly this applies for each other node
# n_{2} = 1 + (1/3)(n_{1} + n_{3} + n_{7})
# ....

# Remove the first row and column using the trival solution of n_{1}=0
scale_factor = (1.0/3.0)
subA=A
Bdash = scale_factor*A - np.identity(8)
# print(np.linalg.det(Bdash))
subA = np.delete(subA,0,0)
subA = np.delete(subA,0,1)
# print(subA)

B = (scale_factor*subA - np.identity(7))
print(B)

sol_vec = -B.I*np.ones((7,1))
# values for all other nodes, excluding n_{1}
print(sol_vec)
# we then compute n_{1} by using the solution vector in equation 1
# n_{1} = 1 + (1/3)(n_{2} + n_{4} + n_{6})
# note that index 0 now points to 2, since the first node was removed
# (A-I).I has no inverse -> (A-np.identity(8)).I
solution = 1.0 + scale_factor*(sol_vec[0] +sol_vec[2] +sol_vec[4])
print("First method solution is: {}".format(int(solution)))
print("======================\n")

# Solution 2:
# since n2 = n4 = n6 and n3 = n5 = n7 due to symmetry
# we can reduce matrix to:
A2 =np.matrix([[0., 1., 0., 0.],
                [1./3., 0., 2./3., 0.],
                [0., 2./3., 0., 1./3],
                [0., 0., 1., 0.]])
subA2=A2
subA2 = np.delete(subA2,0,0)
subA2 = np.delete(subA2,0,1)
sol_vec2 = -(subA2 - np.identity(3)).I*np.ones((3,1))
print((subA2 - np.identity(3)).I)
print(sol_vec2)
solution2 = 1 + sol_vec2[0]
print("Second method solution is: {}".format(int(solution2)))
print("======================\n")


# Solution 3:
# Use graph theory
# The matrix represents the graph and the product of
# the matrix on the unit vector for n_{1} = [1, 0, 0,.....]
# gives the number of paths from n_{1} to another node
# number of paths from 1 to another node

def computewalk(mat, nsteps):
    test_vector = np.zeros((8,1))
    test_vector[0] = 1

    full_mat = matrix_power(mat, nsteps)
    # print(full_mat)
    vec = full_mat*test_vector
    prob = vec[0]/sum(vec)
    return prob[0,0], vec

# if we take one step from node 1 we can go to 2, 4, 6 each by one way
# hence we get [0,1,0,1,0,1,0,0]
probs = []
values = []
for i in range(2, 100, 2):
    print("{} step...".format(i))
    prob, vec = computewalk(A, i)
    print(prob, vec[0,0])
    probs.append((i, prob))
    values.append((i, vec[0,0]))

import matplotlib.pyplot as plt

f = plt.figure()
X, Y = map(list, zip(*probs))
plt.plot(X, Y, 'k', alpha=0.7)
f = plt.figure()
X, Y = map(list, zip(*values))
plt.semilogy(X, Y, 'ko', alpha=0.7)
plt.xlabel("number of steps (k)", fontsize=16)
plt.ylabel("number of paths 1 -> 1", fontsize=16)
plt.show()
# we therefore need to sum over all paths that lead to n_{1}
# only even number of steps lead back to one
# 2 steps -> 3 ways (1*3)
# 4 steps -> 21 ways (7*3)
# 6 steps -> 183 ways (61*3)
# 8 steps -> 1641 ways (547*3)
# it is wierd that the number of paths are the product of
# exactly 2 primes (always?) and one is 3 (number of adjacent nodes)
#
# not the case for 10 steps
# 10 steps -> 14763 ways (7*19*37*3)
# 
# Is the probability of the number of steps the inverse of the number of paths?
# It is clear for 2 steps, since 1/3 of the time it must be 2 steps
# but then all the other paths must have prob of 2/3
# 
# the probability should be the number of paths to n_{1}
# divided by the total number of paths from origin in m steps
#
# todo: compute the average based on weighted average
# i.e ave = (2*0.3 + 4*.....)/total number of paths
# total number of paths is infinite though
# we do know that 1 + 2 + 3+ .... = -1/12 although divergent

# extra below work for solution 1

#expected solution
# expected_solution=np.matrix([[0.0,7.0,9.0,7.0,9.0,7.0,9.0,10.0]])
# print(scale_factor*A*expected_solution.T + 1.0)

# n1 = lambda n: 1.0 + scale_factor*(n[0,1] + n[0,3] + n[0,5] )
# n2 = lambda n: 1.0 + scale_factor*(n[0,0] + n[0,2] + n[0,6] )
# n3 = lambda n: 1.0 + scale_factor*(n[0,1] + n[0,3] + n[0,7] )
# n4 = lambda n: 1.0 + scale_factor*(n[0,0] + n[0,2] + n[0,4] )
# n5 = lambda n: 1.0 + scale_factor*(n[0,3] + n[0,5] + n[0,7] )
# n6 = lambda n: 1.0 + scale_factor*(n[0,0] + n[0,4] + n[0,6] )
# n7 = lambda n: 1.0 + scale_factor*(n[0,1] + n[0,5] + n[0,7] )
# n8 = lambda n: 1.0 + scale_factor*(n[0,2] + n[0,4] + n[0,6] )

# print(n2(expected_solution))