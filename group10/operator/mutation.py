from group10.operator import MutationOperator
import random
from copy import copy


class UniformMutation(MutationOperator):
    def apply(self, genome):
        index = random.randrange(len(genome))
        genome_copy = copy(genome)
        bound = genome_copy.bounds[index]
        genome_copy[index] = random.uniform(bound[0], bound[1])
        return genome_copy
