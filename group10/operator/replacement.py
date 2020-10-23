from group10.operator import ReplacementOperator
from group10.population import Population
import numpy as np

#steady-state
class SteadyStateReplacement(ReplacementOperator):
    def apply(self, population_current, population_offspring):
        population_current[population_current.worst]=population_offspring[0]
        return population_current