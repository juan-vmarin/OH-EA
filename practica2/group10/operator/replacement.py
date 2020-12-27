from group10.operator import ReplacementOperator


class ElitistReplacement(ReplacementOperator):
    """A elitist replacement operator
    """

    def apply(self, population_current, population_offspring):
        """It represents an operation to generate a new population of genomes in a elitist way

        Args:
            population_current (component.Population): The current population of genomes
            population_offspring (component.Population): The population with one genome as result to apply
            selection/crossover/mutation

        Returns:
            Population: New population as a result of the elitist replacement
        """

        population_current[population_current.worst_index] = population_offspring[0]
        return population_current


