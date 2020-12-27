from group10.operator import MutationOperator
import random
import numpy

# de/rand/1
class DeRandOneMutation(MutationOperator):
    """A de/rand/1 mutation operator and A uniform selection operator included
        """

    def __init__(self, f):
        """de/rand/1 mutation constructor and Uniform selection constructor
        Args:
            f (float): mutation factor F
            k (float): number of genomes to be randomly selected
        """
        self.k = 1
        self._f = f

    def _selection(self, population, genome_target):
        """It represents an operation to select a genome within the population in a uniform selection way

        Args:
            population (component.Population): A population of genomes
            genome_target (component.Genome): Genome target x_i

        Returns:
            Genome: Genome as result of the selection of the random genome within the population which is not the target

        """
        while 1:
            selected = random.choice(list(population))
            # print(selected, 'selected')
            if genome_target != selected:
                break
        return selected

    def apply(self, population, genome_target):
        """It represents an operation to mutate a genome with function v= x0 + F(x1+x2)
        and include an operation to select a genome within the population in a uniform selection way


        Args:
            population (component.Population): A population of genomes
            genome_target (component.Genome): Genome target x_i

        Returns:
            Genome: New genome as result to apply mutation
        """
        genome_x0 = self._selection(population, genome_target)
        genome_x1 = self._selection(population, genome_target)
        genome_x2 = self._selection(population, genome_target)
        genome_x0 = genome_x0.solution + self._f * (genome_x1.solution + genome_x2.solution)
        # genome_x0 = genome_x0+ self._f * (genome_x1 + genome_x2)
        return genome_x0

        # genome_copy = copy(genome)
        # if random.random() < self.prob_mut:
        #     index = random.randrange(len(genome))
        #     bound = genome_copy.bounds[index]
        #     genome_copy[index] = random.uniform(bound[0], bound[1])
        #
        # return genome_copy
    # if __name__ == "__main__":

# class test():
#     if __name__ == "__main__":
#         m=DeRandOneMutation()
