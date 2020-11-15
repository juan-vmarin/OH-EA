from group10.EA import EA
from benchmarks.functions import sphere,ackley


bounds = [(-100, 100)] * 10
myEA = EA(sphere, bounds, 50)
myEA.run(10000)
bestGenome = myEA.best()
print("function sphere")
print(bestGenome, "\nfitness:", bestGenome.fitness)



bounds = [(-100, 100)] * 10
myEA = EA(ackley, bounds, 50)
myEA.run(10000)
bestGenome = myEA.best()
print("function ackley")
print(bestGenome, "\nfitness:", bestGenome.fitness)




