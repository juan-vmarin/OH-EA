from group10.operator.selection import TournamentSelection
from group10.component import *
import random


def min_func(solution):
    return solution[0] ** 2 + solution[1] ** 2


bounds = [(-2, 2)] * 10
p = Population(min_func, bounds, 10)
p.random_genomes()
m = TournamentSelection()
print(p)
lt = m.apply(p, 1)
print(lt)
for i in lt:
    print(i)

