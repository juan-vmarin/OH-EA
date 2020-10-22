from group10.operator import SelectionOperator
from group10.population import Population
from group10.genome import Genome
import numpy as np
import random


class TournamentSelection(SelectionOperator):
    def apply(self, population, k):
        # Creation of the lists
        best = random.choice(population)
        selected = []
        selected.append(best)

        # Check k times
        for i in range(k - 1):
            # First case
            rand = random.choice(population)
            while selected.count(rand) > 0:
                rand = random.choice(population)

            # Creo q se puede mejorar esto
            if best.fitness > rand.fitness:
                selected.append(best)
                selected.append(rand)
                best, rand = rand, best
            else:
                selected.append(rand)

        return best
