from group10.operator import ReplacementOperator
from group10.population import Population
import numpy as np

#steady-state
class SteadyStateReplacement(ReplacementOperator):
    def apply(self, population_current, population_offspring):
        population_next=np.copy(population_current)
        population_next.set(population_next.size-1,population_offspring.get(0))
        return population_next