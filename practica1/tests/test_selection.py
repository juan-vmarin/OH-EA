from practica1.group10 import TournamentSelection
from practica1.group10.component import *


def min_func(solution):
    return solution[0] ** 2 + solution[1] ** 2


bounds = [(-2, 2)] * 10
p = Population(min_func, bounds, 10)
p.random_genomes()
m = TournamentSelection()
# print(p)
lt = m.apply(p)
print(lt)
for i in lt:
    print(i)
