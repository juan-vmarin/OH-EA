from group10.EA import EA
from benchmarks.functions import sphere, ackley, rosenbrock, rastrigin,griewank

spherebounds = [(-5.12, 5.12)] * 10
sphereEA = EA(sphere, spherebounds, 50)
sphereEA.run(10000)
bestGenome = sphereEA.best()
print("function sphere")
print(bestGenome, "\nfitness:", bestGenome.fitness)

ackleybounds = [(-32, 32)] * 10
ackleyEA = EA(ackley, ackleybounds, 50)
ackleyEA.run(10000)
bestGenome = ackleyEA.best()
print("function ackley")
print(bestGenome, "\nfitness:", bestGenome.fitness)

rosenbrockbounds = [(-5, 10)] * 10
rosenbrockEA = EA(rosenbrock, rosenbrockbounds, 50)
rosenbrockEA.run(10000)
bestGenome = rosenbrockEA.best()
print("function rosenbrock")
print(bestGenome, "\nfitness:", bestGenome.fitness)

rastriginbounds = [(-5.12, 5.12)] * 10
rastriginEA = EA(rastrigin, rastriginbounds, 50)
rastriginEA.run(10000)
bestGenome = rastriginEA.best()
print("function rastrigin")
print(bestGenome, "\nfitness:", bestGenome.fitness)

griewankbounds = [(-5.12, 5.12)] * 10
griewankEA = EA(griewank, griewankbounds, 50)
griewankEA.run(10000)
bestGenome = griewankEA.best()
print("function griewank")
print(bestGenome, "\nfitness:", bestGenome.fitness)