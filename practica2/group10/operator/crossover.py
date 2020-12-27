from group10.operator import CrossoverOperator
import random
from random import randint
import numpy


class BinomialCrossover(CrossoverOperator):
    '''A binomial crossover operator
    '''

    def apply(self, genomes, cr=0.1):
        """It represents an operation to cross 2 genomes in a binomial way

        Args:
            genomes (component.Genome): A list of two genomes, genomes[0]: donor vector, genomes[1]:target vector
            cr:possibility to crossover to generate

        Returns:
            Genome: Genome as a result of crossover
        """
        v = genomes[0]
        x = genomes[1]
        # genome_aux = numpy.zeros(len(x))

        for i in range(len(x)):
            rand = random.random()
            rand_int = randint(1, 2)
            if rand <= cr or i == rand_int:
                pass
            elif rand > cr and i != rand_int:
                v[i] = x[i]

        return v


class Test:
    if __name__ == "__main__":
        genomes = [4, 7]
        cr = 0.1
        pass