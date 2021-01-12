from group10.operator import CrossoverOperator
import random
from random import randint
from copy import copy


class BinomialCrossover(CrossoverOperator):
    """A binomial crossover operator
    """

    def __init__(self):
        """
            cr:possibility to crossover to generate
        """
        self.cr = 0.5

    def apply(self, genomes):
        """It represents an operation to cross 2 genomes in a binomial way

        Args:
            genomes (component.Genome): A list of two genomes, genomes[0]: donor vector, genomes[1]:target vector


        Returns:
            Genome: Genome as a result of crossover
        """
        v = copy(genomes[0])
        x = copy(genomes[1])
        for i in range(len(x)):
            rand = random.random()
            rand_int = randint(1, 2)
            if rand <= self.cr or i == rand_int:
                pass
            else:
                v[i] = x[i]

        return v
