from group10.operator import ReplacementOperator


class ElitistReplacement(ReplacementOperator):
    """A elitist replacement operator
    """

    def apply(self, population_current, population_offspring, target):
        """It represents an operation to generate a new population of genomes in a elitist way

        Args:
            population_current (component.Population): The current population of genomes
            population_offspring (component.Population): The population with one genome as result to apply
            selection/crossover/mutation
            target: genome target

        Returns:
            Population: New population as a result of the elitist replacement
        """
        if population_current[target] < population_offspring[0]:
            population_current[target] = population_offspring[0]
        return population_current
