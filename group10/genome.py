import numpy as np
from random import uniform


class Genome(object):
    def __init__(self, bounds):
        self._solution = np.array([uniform(bounds[0], bounds[1]) for i in bounds], dtype=int)
        self._fitness = self.calculate_fitness()

    @property
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, solution):
        self._solution = np.asarray(solution)
        self._fitness = self.calculate_fitness()

    @property
    def fitness(self):
        return self._fitness
    
    def calculate_fitness(self):
        return ""
