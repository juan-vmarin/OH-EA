from group10.operator.crossover import UniformCrossover
from group10.operator.selection import TournamentSelection
from group10.operator.replacement import SteadyStateReplacement
from group10.operator.mutation import UniformMutation
import numpy as np


class EA(object):
    """Genetic algorithms"""

    def __init__(self, minfun, bounds, psize):
        # super(EA, self).__init__()
        self.crossover = UniformCrossover()
        self.mutation = UniformMutation()
        self.selection = TournamentSelection()
        self.replacement = SteadyStateReplacement()
        self.minfun = minfun
        self.bounds = np.asarray(bounds)
        self.solution_size = self.bounds.size
        self.psize = psize

    def run(self, iteration):
        pass
        # for i in range(iteration):
        #     pass
