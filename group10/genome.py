import numpy as np


class Genome(object):
    def __init__(self, solution, fitness):
        self.solution = np.asarray(solution)
        self.fitness = fitness
