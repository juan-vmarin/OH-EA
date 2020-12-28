from group10.operator import CrossoverOperator
import random
from random import randint


class BinomialCrossover(CrossoverOperator):
    """A binomial crossover operator
    """

    def apply(self, genomes, cr=0.5):
        """It represents an operation to cross 2 genomes in a binomial way

        Args:
            genomes (component.Genome): A list of two genomes, genomes[0]: donor vector, genomes[1]:target vector
            cr:possibility to crossover to generate

        Returns:
            Genome: Genome as a result of crossover
        """
        v = genomes[0]
        x = genomes[1]
        for i in range(len(x)):
            rand = random.random()
            rand_int = randint(1, 2)
            if rand <= cr or i == rand_int:
                pass
            else:
                v[i] = x[i]

        return v


