from group10.operator.crossover import UniformCrossover
from group10.operator.selection import TournamentSelection
from group10.operator.replacement import SteadyStateReplacement
from group10.operator.mutation import UniformMutation
from group10.component import Population
import numpy as np


class EA(object):
    """Genetic algorithms"""

    def __init__(self, min_function, bounds, p_size):
        # super(EA, self).__init__()
        self.__crossover = UniformCrossover()
        self.__mutation = UniformMutation()
        self.__selection = TournamentSelection()
        self.__replacement = SteadyStateReplacement()
        self.__min_function = min_function
        self.__bounds = np.asarray(bounds)
        self.__population = Population(min_function, bounds, p_size)

    def run(self, iteration):
        pass
        # for i in range(iteration):
        #     pass
