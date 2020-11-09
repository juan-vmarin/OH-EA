from group10.EA import EA


def min_func(solution):
    return solution[0] ** 2 + solution[1] ** 2


ga = EA(min_func, (-2, 2)*2, 20)
solution, fitness = ga.run(100)
print(f'solution:{solution}, fitness{fitness}')