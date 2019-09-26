# -*- coding: utf-8 -*-
"""
The Cube

"""

import numpy as np

scale_factor = (1.0/3.0)
A = np.matrix([[0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0 ],
            [1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0 ],
            [0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0 ],
            [1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0 ],
            [0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0 ],
            [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0 ],
            [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0 ],
            [0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0 ]])
            
        
# Remove the first row and column using the trival solution of n_{1}=0
subA=A
subA = np.delete(subA,0,0)
subA = np.delete(subA,0,1)

I = np.identity(7)
B = (scale_factor*subA - I)

one_vector=-np.matrix([[1,1,1,1,1,1,1]])

sol_vec = B.I*one_vector.T

#n_{1} = 1 + (1/3)(n_{2} + n_{4} + n_{6})
solution = 1.0 + scale_factor*(sol_vec[0] +sol_vec[2] +sol_vec[4])

print(int(solution))

#expected solution
expected_solution=np.matrix([[0.0,7.0,9.0,7.0,9.0,7.0,9.0,10.0]])
print(scale_factor*A*expected_solution.T + 1.0)

n1 = lambda n: 1.0 + scale_factor*(n[0,1] + n[0,3] + n[0,5] )
n2 = lambda n: 1.0 + scale_factor*(n[0,0] + n[0,2] + n[0,6] )
n3 = lambda n: 1.0 + scale_factor*(n[0,1] + n[0,3] + n[0,7] )
n4 = lambda n: 1.0 + scale_factor*(n[0,0] + n[0,2] + n[0,4] )
n5 = lambda n: 1.0 + scale_factor*(n[0,3] + n[0,5] + n[0,7] )
n6 = lambda n: 1.0 + scale_factor*(n[0,0] + n[0,4] + n[0,6] )
n7 = lambda n: 1.0 + scale_factor*(n[0,1] + n[0,5] + n[0,7] )
n8 = lambda n: 1.0 + scale_factor*(n[0,2] + n[0,4] + n[0,6] )

print(n2(expected_solution))