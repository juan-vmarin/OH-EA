from group10.EA import EA
from benchmarks.functions import sphere, ackley, rosenbrock, rastrigin, griewank, schwefel_2_21, schwefel_2_22, schwefel_1_2, extended_f_10,bohachevsky,schaffer

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

griewankbounds = [(-600, 600)] * 10
griewankEA = EA(griewank, griewankbounds, 50)
griewankEA.run(10000)
bestGenome = griewankEA.best()
print("function griewank")
print(bestGenome, "\nfitness:", bestGenome.fitness)

schwefel_2_21bounds = [(-100, 100)] * 10
schwefel_2_21EA = EA(schwefel_2_21, schwefel_2_21bounds, 50)
schwefel_2_21EA.run(10000)
bestGenome = schwefel_2_21EA.best()
print("function schwefel_2_21")
print(bestGenome, "\nfitness:", bestGenome.fitness)

schwefel_2_22bounds = [(-100, 100)] * 10
schwefel_2_22EA = EA(schwefel_2_22, schwefel_2_22bounds, 50)
griewankEA.run(10000)
bestGenome = griewankEA.best()
print("function schwefel_2_22")
print(bestGenome, "\nfitness:", bestGenome.fitness)

schwefel_1_2bounds = [(-500, 500)] * 10
schwefel_1_2EA = EA(schwefel_1_2, schwefel_1_2bounds, 50)
schwefel_1_2EA.run(10000)
bestGenome = schwefel_1_2EA.best()
print("function schwefel_1_2")
print(bestGenome, "\nfitness:", bestGenome.fitness)

extended_f_10bounds = [(-600, 600)] * 10
extended_f_10EA = EA(extended_f_10, extended_f_10bounds, 50)
extended_f_10EA.run(10000)
bestGenome = extended_f_10EA.best()
print("function extended_f_10")
print(bestGenome, "\nfitness:", bestGenome.fitness)

bohachevskybounds = [(-100, 100)] * 10
bohachevskyEA = EA(bohachevsky, bohachevskybounds, 50)
bohachevskyEA.run(10000)
bestGenome = bohachevskyEA.best()
print("function bohachevsky")
print(bestGenome, "\nfitness:", bestGenome.fitness)

schafferbounds = [(-100, 100)] * 10
schafferEA = EA(schaffer, schafferbounds, 50)
schafferEA.run(10000)
bestGenome = schafferEA.best()
print("function schaffer")
print(bestGenome, "\nfitness:", bestGenome.fitness)