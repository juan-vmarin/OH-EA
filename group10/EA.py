from group10.operator.crossover import UniformCrossover
from group10.operator.selection import TournamentSelection
from group10.operator.replacement import SteadyStateReplacement
from group10.operator.mutation import UniformMutation
from group10.component import Population
import numpy as np
import random


class EA(object):
    """Genetic algorithm to obtain the solution that allows us to obtain the minimum value of a function
    """

    def __init__(self, min_function, bounds, p_size):
        """initialize the population and genomes to random value between the bounds, and instantiate operators

        Args:
            min_function (): function to minimize
            bounds ([(float, float),] or numpy array): limits to get solution
            p_size (int): size of the population
        """
        self._crossover = UniformCrossover()
        self._mutation = UniformMutation()
        self._selection = TournamentSelection()
        self._replacement = SteadyStateReplacement()
        self._min_function = min_function
        self._bounds = np.asarray(bounds)
        self._population = Population(min_function, self._bounds, p_size)
        self._population.random_genomes()

    def run(self, iteration):
        """resolve the min_function with iteration times

        Args:
            iteration (int): number of generation

        Returns:
            (solution, fitness): returns the best solution and its fitness value
        """
        for i in range(iteration):
            genome_a = self._selection.apply(self._population)
            genome_b = self._selection.apply(self._population)
            # print(genome_a, genome_b)
            while genome_a is genome_b:
                # print("bucle")
                genome_b = self._selection.apply(self._population)

            children = self._crossover.apply(genome_a, genome_b)
            child = random.choice(children)
            genome = self._mutation.apply(child)
            offspring_population = Population(self._min_function, self._bounds, 1)
            offspring_population.append(genome)
            self._replacement.apply(self._population, offspring_population)

    def best(self):
        return self._population[self._population.best_index]