from group10.operator import MutationOperator
import random
from copy import copy


class DeRandOneMutation(MutationOperator):
    """A de/rand/1 mutation operator and A uniform selection operator included
        """

    def __init__(self, f):
        """de/rand/1 mutation constructor and Uniform selection constructor
        Args:
            f (float): mutation factor F
        """
        self._f = f

    def selection(self, population, genomes):
        """It represents an operation to select a genome within the population in a uniform selection way

        Args:
            population (component.Population): A population of genomes
            genomes (component.Genome): Genome target x_i

        Returns:
            Genome: Genome as result of the selection of the random genome within the population which is not the target

        """
        while 1:
            selected = random.choice(list(population))
            if selected not in genomes:
                break
        return selected

    def apply(self, population, genome_target):
        """It represents an operation to mutate a genome with function v= x0 + F(x1-x2)
        and include an operation to select a genome within the population in a uniform selection way


        Args:
            population (component.Population): A population of genomes
            genome_target (component.Genome): Genome target x_i

        Returns:
            Genome: New genome as result to apply mutation
        """

        genomes = [genome_target]
        genome_x0 = self.selection(population, genomes)
        genome_res = copy(genome_x0)
        genomes.append(genome_x0)
        genome_x1 = self.selection(population, genomes)
        genomes.append(genome_x1)
        genome_x2 = self.selection(population, genomes)
        genome_res.solution = genome_x0.solution + self._f * (genome_x1.solution - genome_x2.solution)
        return genome_res
