from group10.operator import CrossoverOperator
import random
from random import randint
from copy import copy


class BinomialCrossover(CrossoverOperator):
    """A binomial crossover operator
    """

    def __init__(self, cr):
        """
            cr:possibility to crossover to generate
        """
        self.cr = cr

    def apply(self, genome_v, genome_x):

        v = copy(genome_v)
        x = copy(genome_x)
        for i in range(len(x)):
            rand = random.random()
            rand_int = randint(1, 2)
            if rand <= self.cr or i == rand_int:
                pass
            else:
                v[i] = x[i]

        return v
