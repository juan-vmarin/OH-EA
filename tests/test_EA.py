from group10.EA import EA


def f(sol):
    return sum(sol)


print("Test EA")
bounds = [(-10, 10)] * 10
myEA = EA(f, bounds, 50)
myEA.run(100000)
bestGenome = myEA.best()
print(bestGenome, "fitness:", bestGenome.fitness)
