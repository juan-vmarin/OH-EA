from group10.EA import EA
from benchmarks.functions import sphere


bounds = [(-100, 100)] * 10
myEA = EA(sphere, bounds, 50)
myEA.run(20000)
bestGenome = myEA.best()
print(bestGenome, "fitness:", bestGenome.fitness)


