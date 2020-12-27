from group10.operator import ReplacementOperator


class SteadyStateReplacement(ReplacementOperator):
    """A steady-state replacement operator
    """

    def apply(self, population_current, population_offspring):
        """It represents an operation to generate a new population of genomes in a steady-state way

        Args:
            population_current (component.Population): The current population of genomes
            population_offspring (component.Population): The population with one genome as result to apply selection/crossover/mutation

        Returns:
            Population: New population as result to replace the worst genome of the current population
        """
        population_current[population_current.worst_index] = population_offspring[0]
        return population_current
