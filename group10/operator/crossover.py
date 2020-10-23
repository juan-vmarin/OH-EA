from group10.operator import CrossoverOperator
from random import random
from copy import copy


class UniformCrossover(CrossoverOperator):
    def apply(self, genome_a, genome_b, prob=0.5):
        genome_a_copy = copy(genome_a)
        genome_b_copy = copy(genome_b)
        for i in range(len(genome_a)):
            if genome_a_copy[i] != genome_b[i]:
                change = random()
                if change > prob:
                    genome_a_copy[i], genome_b_copy[i] = genome_b_copy[i], genome_a_copy[i]
        return genome_a_copy, genome_b_copy
