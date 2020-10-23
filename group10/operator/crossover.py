from group10.operator import CrossoverOperator
from random import random
from copy import copy


class UniformCrossover(CrossoverOperator):
    def apply(self, *genome_pairs, prob=0.5):
        if len(genome_pairs) > 2:
            raise ValueError("Hay mas de 2 individuos")
        genome_a, genome_b = genome_pairs[0], genome_pairs[1]
        genome_a_copy = copy(genome_a)
        genome_b_copy = copy(genome_b)
        equal = genome_a == genome_b
        for i in range(len(genome_a)):
            if not equal[i]:
                change = random()
                if change > prob:
                    genome_a_copy[i], genome_b_copy[i] = genome_b_copy[i], genome_a_copy[i]
        return genome_a_copy, genome_b_copy
