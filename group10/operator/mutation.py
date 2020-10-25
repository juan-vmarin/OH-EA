from group10.operator import MutationOperator
import random
from copy import copy


class UniformMutation(MutationOperator):
    """A uniform Mutation operator
    """
    def apply(self, genome):
        """it represents an operation to mutate a genome in a uniform way

        Args:
            genome (component.Genome): genome to mutate

        Returns:
            Genome: new genome as result to apply mutation
        """
        index = random.randrange(len(genome))
        genome_copy = copy(genome)
        bound = genome_copy.bounds[index]
        genome_copy[index] = random.uniform(bound[0], bound[1])
        return genome_copy
