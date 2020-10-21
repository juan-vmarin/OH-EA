from group10.operator.crossover import UniformCrossover
from group10.operator.selection import TournamentSelection
from group10.operator.replacement import SteadyStateReplacement
from group10.operator.mutation import UniformMutation
from group10.population import Population
import numpy as np


class EA(object):
    """Genetic algorithms"""

    def __init__(self, minfun, bounds, psize):
        # super(EA, self).__init__()
        self._crossover = UniformCrossover()
        self._mutation = UniformMutation()
        self._selection = TournamentSelection()
        self._replacement = SteadyStateReplacement()
        self._minfun = minfun
        self._bounds = np.asarray(bounds)
        self._population = Population(bounds, psize)

    def run(self, iteration):
        pass
        # for i in range(iteration):
        #     pass
