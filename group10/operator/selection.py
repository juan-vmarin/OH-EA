from group10.operator import SelectionOperator
import random


class TournamentSelection(SelectionOperator):
    def apply(self, population, k):
        # Creation of the lists
        best = random.choice(population)
        selected = {best}

        # Check k times
        for i in range(k - 1):
            # First case
            rand = random.choice(population)
            while rand in selected:
                rand = random.choice(population)

            if best.fitness < rand.fitness:
                selected.add(best)
                best = rand

            selected.add(rand)

        return best
