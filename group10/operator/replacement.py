from group10.operator import ReplacementOperator


class SteadyStateReplacement(ReplacementOperator):
    def apply(self, population_current, population_offspring):
        """it represents an operation to generate a new population of genomes

        Args:
            population_current (component.Population): the current population of genomes
            population_offspring (component.Population): the population from the current population will change
        """
        population_current[population_current.worst_index] = population_offspring[0]
        # return population_current
