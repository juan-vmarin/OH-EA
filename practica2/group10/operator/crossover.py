from group10.operator import CrossoverOperator
import random
from random import randint
from copy import copy


class BinomialCrossover(CrossoverOperator):
    """A binomial crossover operator
    """

    def __init__(self,cr):
        """
            cr:possibility to crossover to generate
        """
        self.cr = cr

    def apply(self, genomes):

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
