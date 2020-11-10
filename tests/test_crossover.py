from group10.operator.crossover import UniformCrossover
from group10.component import *
import random


def min_func(solution):
    return solution[0] ** 2 + solution[1] ** 2


bounds = [(-2, 2)] * 10
a = Genome(np.array([random.uniform(bound[0], bound[1]) for bound in bounds]), min_func, bounds)
b = Genome(np.array([random.uniform(bound[0], bound[1]) for bound in bounds]), min_func, bounds)
m = UniformCrossover()
print(a)
print(b)
ca, cb = m.apply(a, b)
print(ca)
print(cb)