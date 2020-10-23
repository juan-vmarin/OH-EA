from group10.operator import ReplacementOperator


class SteadyStateReplacement(ReplacementOperator):
    def apply(self, population_current, population_offspring):
        population_current[population_current.worst] = population_offspring[0]
        return population_current
