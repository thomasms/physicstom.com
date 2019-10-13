"""
    A Monte Carlo approach to solving the cube problem

    author: Thomas Stainer
    date: 26/09/2019 @ 21:34
"""

import numpy as np
from scipy import stats

showplot = True
NITERS = 10000

# make a graph of a cube with 8 vertices
# we could indeed use a library such as networkx
# but we keep it simple and vanilla for
# educational purposes
CUBEGRAPH = {
    'nodes': [
        1, 2, 3, 4, 5, 6, 7, 8
    ],
    'edges': [
        (1, 2),
        (1, 4),
        (1, 6),
        (2, 3),
        (2, 7),
        (3, 4),
        (3, 8),
        (4, 5),
        (5, 6),
        (5, 8),
        (6, 7),
        (7, 8)
    ]
}

def getadjacent(graph, vertex):
    """
        vertex is the node indexnumber i.e 1, 2, 3, ... or 8
        and returns all adjacent nodes

        For example:
            getadjacent(1) -> [2, 4, 6]
            getadjacent(2) -> [1, 3, 7]
            getadjacent(3) -> [2, 4, 8]
            ....
    """
    nodes = []
    for n1, n2 in graph['edges']:
        if n1 == vertex:
            nodes.append(n2)
        if n2 == vertex:
            nodes.append(n1)
    return sorted(nodes)

def randomstep(graph, start, steps=1):
    """
        Take a random step(s) from a starting node.
        Return the node ending on.

        Since all edges are equal all weights are 1

        This function assumes weight =1, to extend
        we would need to define weights in edge data
    """
    if start < min(graph['nodes']) or start > max(graph['nodes']):
        raise RuntimeError("Invalid node number: {}".format(start))

    if steps == 0:
        return start

    # get all adjacent nodes
    anodes = getadjacent(graph, start)

    # generate a random number drawn from a uniform distribution
    rmin, rmax = 0, 1
    prob = np.random.uniform(rmin, rmax, 1)[0]

    # equal weights
    # this remains unchanged every call, should be moved
    # out but if weights change then code is needed here
    weights = [(rmax-rmin)/len(anodes)]*len(anodes)
    r = rmin
    for w, n in zip(weights, anodes):
        r += w
        if r > prob:
            # use recursion for this problem
            return randomstep(graph, n, steps=steps-1)
    
    return None

def getnumberofsteps(graph, start, end):
    nextnode = start
    count = 0
    while nextnode != end or (count == 0 and nextnode == end):
        nextnode = randomstep(graph, nextnode, steps=1)
        count += 1
    return count

def estimateaveragewalk(graph, start, end, niter=1000, op=np.mean):
    steps = []
    for _ in range(niter):
        steps.append(getnumberofsteps(graph, start, end))
    return op(steps)

for node in CUBEGRAPH['nodes']:
    # 1 -> X 
    # all others are same due to symmetry
    averagesteps = estimateaveragewalk(CUBEGRAPH, 1, node, niter=NITERS)
    mostcommon = estimateaveragewalk(CUBEGRAPH, 1, node, niter=NITERS, op=stats.mode )
    print("1 -> {} = {:.3f} with dominant path of {} step(s)".format(node, averagesteps, mostcommon.mode[0]))

if showplot:
    import matplotlib.pyplot as plt

    # check distribution of final node for 8 steps
    nodes = []
    for _ in range(10000):
        nodes.append(randomstep(CUBEGRAPH, 1, steps=8))

    fig = plt.figure()
    plt.hist(nodes, bins=range(min(CUBEGRAPH['nodes']), max(CUBEGRAPH['nodes'])), 
        facecolor='r', edgecolor='black', linewidth=1.2, alpha=0.4)

    # check distribution of final node for 8 steps
    steps = []
    for _ in range(100000):
        steps.append(getnumberofsteps(CUBEGRAPH, 1, 1))

    fig = plt.figure()
    n, bins, patches = plt.hist(steps, bins=range(0, 100), facecolor='r', 
        edgecolor='black', linewidth=1.2, alpha=0.4)
    plt.xlabel("number of steps 1 -> 1", fontsize=16)
    plt.ylabel("count", fontsize=16)
    plt.yscale('log', nonposy='clip')
    # print(n)

    plt.show()

