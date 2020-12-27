from practica2.group10.component import Population
from practica2.group10.operator import SelectionOperator
import random


class UniformSelection(SelectionOperator):
    """A uniform selection operator
    """

    def __init__(self):
        """Uniform selection constructor

        Args:
            k (int): number of genomes to be randomly selected

        """
        self.k = 1

    def apply(self, population, i):
        """It represents an operation to select a genome within the population in a uniform selection way

        Args:
            population (component.Population): A population of genomes
            i(int): index of the target

        Returns:
            Genome: Genome as result of the selection of the random genome within the population which is not the target
        """
        while 1:
            selected = random.randint(0, len(population) - 1)
            if selected != i:
                break
        print(selected, 'selected')
        return population[selected]

# class test():
#     if __name__ == "__main__":
#         bounds = [(-2, 2)] * 10
#
#         def min_func(solution):
#             return solution[0] ** 2 + solution[1] ** 2
#         p = Population(min_func, bounds, 2)
#         p._random_genomes()
#         # p.random_genomes()
#         for i in p:
#             print(i)
#             for j in i:
#                 print(j)
#         print('............................................................................................')
#         m = UniformSelection()
#         # print(p)
#         lt = m.apply(p,0)
#         print(lt)
#         for i in lt:
#             print(i)
