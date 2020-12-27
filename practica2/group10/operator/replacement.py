from group10.operator import ReplacementOperator


class ElitistReplacement(ReplacementOperator):
    """A elitist replacement operator
    """

    def apply(self, population_current, population_offspring):
        '''It represents an operation to generate a new population of genomes in a elitist way

        Args:
            population_current (component.Population): The current population of genomes
            population_offspring (component.Population): The population with one genome as result to apply
            selection/crossover/mutation

        Returns:
            Population: New population as a result of the elitist replacement
        '''

        population_current.sort()
        population_offspring.sort(True)
        for i in range(len(population_current)):
            if population_current[i].fitness < population_offspring[0].fitness:
                population_current[i] = population_offspring[0]
                del population_offspring[0]

        return population_current


class Test:
    if __name__ == "__main__":
        # population_current = [2, 4, 7, 6, 5]
        # population_offspring = [9, 10, 2, 22, 4]

        population_current = [2, 4, 5, 6, 7]  # population_current.sort()
        population_offspring = [22, 10, 9, 4, 2]  # population_offspring.sort(True)

        for i in range(len(population_current)):
            if population_current[i] < population_offspring[0]:
                population_current[i] = population_offspring[0]
                del population_offspring[0]
                # population_offspring.__delitem__(0)

        print(population_current)
