from group10.operator.mutation import UniformMutation
from group10.component import *
import random

def min_func(solution):
    return solution[0] ** 2 + solution[1] ** 2


bounds = [(-2, 2)] * 10
g = Genome(np.array([random.uniform(bound[0], bound[1]) for bound in bounds]), min_func, bounds)
m = UniformMutation()
print(g)
mt = m.apply(g)
print(g == mt)
print(mt)