from group10.operator.crossover import UniformCrossover
from group10.operator.selection import TournamentSelection
from group10.operator.replacement import SteadyStateReplacement
from group10.operator.mutation import UniformMutation
from group10.component import Population
import numpy as np
import random


class EA(object):
    """Genetic algorithms"""

    def __init__(self, min_function, bounds, p_size):
        # super(EA, self).__init__()
        self._crossover = UniformCrossover()
        self._mutation = UniformMutation()
        self._selection = TournamentSelection()
        self._replacement = SteadyStateReplacement()
        self._min_function = min_function
        self._bounds = np.asarray(bounds)
        self._population = Population(min_function, self._bounds, p_size).random_genomes()

    def run(self, iteration):
        k = random
        for i in range(iteration):
            genome_a = self._selection.apply(self._population, k)
            genome_b = self._selection.apply(self._population, k)
            while genome_a is not genome_b:
                genome_b = self._selection.apply(self._population, k)

            children = self._crossover.apply(genome_a, genome_b)
            child = random.choice(children)
            genome = self._mutation.apply(child)
            offspring_population = Population(self._min_function, self._bounds, 1)
            offspring_population.append(genome)
            self._population = self._replacement.apply(self._population, offspring_population)

        best_genome = self._population[self._population.best_index]

        return best_genome.solution, best_genome.fitness
