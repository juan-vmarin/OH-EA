from group10.EA import EA
from benchmarks.functions import griewank


bounds = [(-100, 100)] * 10
myEA = EA(griewank, bounds, 50)
myEA.run(10000)
bestGenome = myEA.best()
print(bestGenome, "fitness:", bestGenome.fitness)


