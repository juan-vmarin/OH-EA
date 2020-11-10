from group10.operator import SelectionOperator
import random


class TournamentSelection(SelectionOperator):
    def apply(self, population, i=1):
        # Creation of the lists
        best = random.choice(population)
        selected = [best]

        # Check k times
        for _ in range(i):
            # First case
            rand = random.choice(population)
            while rand in selected:
                rand = random.choice(population)

            if best.fitness < rand.fitness:
                selected.append(best)
                best = rand

            selected.append(rand)

        return best
