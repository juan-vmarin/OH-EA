from practica1.group10 import CrossoverOperator
from random import random
from copy import copy


class UniformCrossover(CrossoverOperator):
    """A uniform crossover operator
    """

    def __init__(self, prob_cross):
        """Uniform crossover constructor

        Args:
            prob_cross (float): Probability to cross 2 genomes

        """
        self.prob_cross = prob_cross

    @staticmethod
    def _cross_genome(genome_to_cross, genome):
        """Auxiliary static method to cross a genome

        Args:
            genome_to_cross (component.Genome): Genome to be crossed
            genome (component.Genome): Genome to cross
        """
        for i in range(len(genome_to_cross)):
            if genome_to_cross[i] != genome[i]:
                if random() > 0.5:
                    genome_to_cross[i] = genome[i]

    def apply(self, genome_a, genome_b):
        """It represents an operation to cross 2 genomes in a uniform way

        Args:
            genome_a (component.Genome): Genome father a
            genome_b (component.Genome): Genome father a

        Returns:
            Genome: Genome as result to crossover genome father gen
        """
        genome_a_copy = copy(genome_a)
        genome_b_copy = copy(genome_b)
        if random() < self.prob_cross:
            self._cross_genome(genome_a_copy, genome_b)
        if random() < self.prob_cross:
            self._cross_genome(genome_b_copy, genome_a)
        return genome_a_copy, genome_b_copy


