from group10.operator import CrossoverOperator
from random import random
from copy import copy


class UniformCrossover(CrossoverOperator):
    """A uniform crossover operator
    """
    def apply(self, genome_a, genome_b, prob=0.5):
        """It represents an operation to cross 2 genomes in a uniform way

        Args:
            genome_a (component.Genome): Genome father a
            genome_b (component.Genome): Genome father a
            prob (float, optional): Probability to change gen when its different gen. Defaults to 0.5.

        Returns:
            Genome: Genome as result to crossover genome father gen
        """
        genome_a_copy = copy(genome_a)
        genome_b_copy = copy(genome_b)
        for i in range(len(genome_a)):
            if genome_a_copy[i] != genome_b[i]:
                change = random()
                if change > prob:
                    genome_a_copy[i], genome_b_copy[i] = genome_b_copy[i], genome_a_copy[i]
        return genome_a_copy, genome_b_copy
