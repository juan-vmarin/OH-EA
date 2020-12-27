from group10.operator.crossover import BinomialCrossover
from group10.operator.replacement import ElitistReplacement
from group10.operator.mutation import DeRandOneMutation
from group10.component import Population
import numpy as np
import random
from benchmarks.functions import ackley


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
        self._crossover = BinomialCrossover()
        self._mutation = DeRandOneMutation(0.9)
        self._replacement = ElitistReplacement()
        self._min_function = min_function
        self._bounds = np.asarray(bounds)
        self._population = Population(min_function, self._bounds, p_size, random=True)

    def run(self, iteration):
        """Resolve the min_function with iteration times

        Args:
            iteration (int): Number of generation
        """
        # i = random.randint(0,self._population.length)
        for i in range(iteration):
            for target in range(len(self._population)):
                genome_target=self._population[target]
                genome_donor = self._mutation.apply(self._population, genome_target)
                print('donor',genome_donor)
                genomes = [genome_donor, genome_target]
                genome_trial = self._crossover.apply(genomes)
                print('trial', genome_trial)
                offspring_population = Population(self._min_function, self._bounds, 1)
                offspring_population.append(genome_trial)
                print('population', offspring_population)
                self._population = self._replacement.apply(self._population, offspring_population)
                print('population', self._population)

    def best(self):
        """Get the best genome of the population

            Returns:
                (component.Genome): the best genome
        """
        return self._population[self._population.best_index]


if __name__ == '__main__':
    ackleybounds = [(-32, 32)] * 10
    ackleyEA = EA(ackley, ackleybounds, 50)
    ackleyEA.run(100000)
    bestGenome = ackleyEA.best()
    print("function ackley")
    print(bestGenome, "\nfitness:", bestGenome.fitness)



    # population = Population(ackley, [(-32, 32)] * 10, 50, random=True)
    # for genome_target in population:
    #     print(genome_target.solution+genome_target.solution)