from group10.operator.replacement import SteadyStateReplacement
from group10.component import *
import random


def min_func(solution):
    return solution[0] ** 2 + solution[1] ** 2


bounds = [(-2, 2)] * 10
g = Genome(np.array([random.uniform(bound[0], bound[1]) for bound in bounds]), min_func, bounds)
pa = Population(min_func, bounds, 10)
pa.random_genomes()
pb = Population(min_func, bounds, 10)
pb.append(g)
m = SteadyStateReplacement()
print('Population:')
print(pa.worst_index)
print('pa')
print(pa)
print('------------------------')
print('pb')
print(pb)
print('------------------------')
m.apply(pa, pb)
print(pa)