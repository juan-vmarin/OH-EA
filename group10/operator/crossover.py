from group10.operator import CrossoverOperator
from group10.genome import Genome
import numpy as np
import random


class UniformCrossover(CrossoverOperator):
    def apply(self, genome_pairs, prob=0.5):
        genome_a, genome_b = genome_pairs[0], genome_pairs[1]
        solution_size = genome_a.solution.shape[0]
        genome_a_sol = np.copy(genome_a)
        genome_b_sol = np.copy(genome_b)
        equal = genome_a == genome_b
        for i in range(solution_size):
            if not equal[i]:
                change = random.random()
                if change > prob:
                    genome_a_sol[i], genome_b_sol[i] = genome_b_sol[i], genome_a_sol[i]

        return [Genome().solution(genome_a_sol), Genome().solution(genome_b_sol)]