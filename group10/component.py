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


class Population(object):
    def __init__(self, bounds, size):
        self._genomes = [Genome(bounds) for i in range(size)]
        self._size = size

    def sort(self, reverse=False):
        self._genomes.sort(reverse=reverse, key=lambda genome: genome.fitness)

    def set(self, index, genome):
        self._genomes[index] = genome

    def get(self, index):
        return self._genomes[index]

    def add(self, genome):
        if len(self._genomes) < self._size:
            self._genomes.append(genome)
        else:
            raise Exception("Máximo tamaño de la población es " + self._size)

    def remove(self, index):
        del self._genomes[index]

    @property
    def size(self):
        return self._size
