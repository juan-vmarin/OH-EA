from group10.operator.crossover import BinomialCrossover
from group10.operator.replacement import ElitistReplacement
from group10.operator.mutation import DeRandOneMutation
from group10.component import Population
import numpy as np


class EA(object):
    """Genetic algorithm to obtain the solution that allows us to obtain the minimum value of a function
    """

    def __init__(self, min_function, bounds, p_size):
        """Initialize the population and genomes to random value between the bounds, and instantiate operators

        Args:
            min_function (): function to minimize
            bounds ([(float, float),] or numpy.array): limits to get solution
            p_size (int): size of the population
        """
        self._crossover = BinomialCrossover(0.5)
        self._mutation = DeRandOneMutation(0.8)
        self._replacement = ElitistReplacement()
        self._min_function = min_function
        self._bounds = np.asarray(bounds)
        self._population = Population(min_function, self._bounds, p_size, random=True)

    def run(self, iteration):
        """Resolve the min_function with iteration times

        Args:
            iteration (int): Number of generation
        """

        for i in range(iteration):
            for target in range(self._population.size):
                genome_target = self._population[target]
                genome_donor = self._mutation.apply(self._population, genome_target)
                genomes = [genome_donor, genome_target]
                genome_trial = self._crossover.apply(genomes)
                offspring_population = Population(self._min_function, self._bounds, 1)
                offspring_population.append(genome_trial)
                self._population = self._replacement.apply(self._population, offspring_population, target)

    def best(self):
        """Get the best genome of the population

            Returns:
                (component.Genome): the best genome
        """
        return self._population[self._population.best_index]
