# -*- coding: utf-8 -*-
"""
Quadratic solver and plotter example

"""

import math
import scipy.optimize as sp
import matplotlib.pyplot as plt
import numpy

def GetRoots(a,b,c):
    # term inside sqrt
    term = b**2 - 4*a*c

    #handle the complex roots
    factor = 1.0
    if term < 0:
        factor = 1j
        term = -term
    
    rootMin = (-b - factor*math.sqrt(term))/(2.0*a)
    rootMax = (-b + factor*math.sqrt(term))/(2.0*a)
    
    return [rootMin,rootMax]
    
# quadratic coefficients and equation
a = 1
b = -50
c = -1
f = lambda x: a*x**2 + b*x + c
g = lambda b: b**2/4.0

#rootsUsingBrent = sp.brentq(f,0.0,Rt*2)
    
#get roots
roots = GetRoots(a,b,c)

# min and max X values
minX = -100
maxX = 100
    
# linear interpolation for plots resolution
resolution = 100

# vectorize function
x = numpy.linspace(minX,maxX,resolution)
y = numpy.vectorize(f)(x)

b = numpy.linspace(minX,maxX,resolution)
c = numpy.vectorize(g)(x)

# plot quadratic function
plt.plot(b,c)
ax = plt.gca()

ax.set_title('a = 1')
ax.set_xlabel('b - coefficient')
ax.set_ylabel('c - coefficient')

ax.fill_between(b, c,2500, facecolor='green', interpolate=True)
ax.fill_between(b, 0,c, facecolor='red', interpolate=True)
ax.text(-50, 2000, 'Complex', style='normal',color='green', fontsize=15,
        bbox={'facecolor':'white', 'alpha':1, 'pad':1.2})
ax.text(-90, 100, 'Real', style='normal',color='red', fontsize=15,
        bbox={'facecolor':'white', 'alpha':1, 'pad':1.2})
ax.text(35, 650, 'Repeated', style='normal',color='blue', fontsize=15,
        bbox={'facecolor':'white', 'alpha':1, 'pad':1.2})
#xmin, xmax = ax.get_xlim()
#ymin, ymax = ax.get_ylim()

#plot roots
#plt.plot([xmin,xmax],[0.0,0.0],'r--')
#plt.plot([roots[0],roots[0]],[ymin,ymax],'g')
#plt.plot([roots[1],roots[1]],[ymin,ymax],'g')

#plt.savefig("root_regions.pdf")
plt.show()

print("Roots are: ", roots[0], " and ", roots[1])