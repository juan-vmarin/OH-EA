from group10.operator import SelectionOperator
import random


class TournamentSelection(SelectionOperator):

    def apply(self, population):
        """It represents an operation to select a genome within the population

        Args:
            population (component.Population): A population of genomes

        Returns:
            Genome: Genome as result of the selection of the best genome with the best fitness within the population
        """
        k = random.randint(1, len(population))
        selected = random.sample(list(population), k)
        return max(selected, key=lambda genome: genome.fitness)
