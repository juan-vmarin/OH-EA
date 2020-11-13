import copy
from random import uniform
import numpy as np
from group10.component import Population, Genome


def min_func(solution):
    return solution[0] ** 2 + solution[1] ** 2


bounds = [(-2, 2)] * 10
p = Population(min_func, bounds, 9)
p.random_genomes()
print(p)
print(len(p))
p.sort()
# print(p)
print(p.best_index)
print(p.worst_index)
print('for:')
for i in p:
    print(i)

p[1] = p[0]
p[2] = copy.copy(p[3])
print(p[1] is p[0])
print(p[2] is p[3])
print(p)

g = Genome(np.array([uniform(bound[0], bound[1]) for bound in bounds]), min_func, bounds)
g1 = Genome(np.array([uniform(bound[0], bound[1]) for bound in bounds]), min_func, bounds)
print(g.fitness)
print(g1.fitness)
print("==", g == g1)
print("!=", g != g1)
print(">", g > g1)
print("<", g < g1)
print(">=", g >= g1)
print("<=", g <= g1)

print("bounds")
print(g.bounds)
print(g)
print(g.fitness)
print(g[1])
g[0] = 0
print(g[0])
print('For:')
for i in g:
    print(i)
print("Len")
print(len(g))
c = copy.copy(g)
g[1] = 3
print(g)
print(c)
print(c == g)
c[1] = 2
print(c == g)
