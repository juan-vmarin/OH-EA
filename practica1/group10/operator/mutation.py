from practica1.group10 import MutationOperator
import random
from copy import copy


class UniformMutation(MutationOperator):
    """A uniform mutation operator
    """

    def __init__(self, prob_mut):
        """Uniform mutation constructor

        Args:
            prob_mut (float): Probability to mutate
        """
        self.prob_mut = prob_mut

    def apply(self, genome):
        """It represents an operation to mutate a genome in a uniform way

        Args:
            genome (component.Genome): Genome to mutate

        Returns:
            Genome: New genome as result to apply mutation
        """
        genome_copy = copy(genome)
        if random.random() < self.prob_mut:
            index = random.randrange(len(genome))
            bound = genome_copy.bounds[index]
            genome_copy[index] = random.uniform(bound[0], bound[1])

        return genome_copy
