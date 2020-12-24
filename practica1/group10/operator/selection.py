from practica1.group10 import SelectionOperator
import random


class TournamentSelection(SelectionOperator):
    """A tournament selection operator
    """

    def __init__(self, k):
        """Tournament selection constructor

        Args:
            k (int): number of genomes to be randomly selected

        """
        self.k = k

    def apply(self, population):
        """It represents an operation to select a genome within the population in a tournament selection way

        Args:
            population (component.Population): A population of genomes

        Returns:
            Genome: Genome as result of the selection of the best genome with the best fitness within the population
        """
        selected = random.sample(list(population), self.k)
        return max(selected, key=lambda genome: genome.fitness)
