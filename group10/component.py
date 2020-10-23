import numpy as np
from random import uniform


class Genome(object):
    def __init__(self, min_function, bounds, solution=None):
        if solution:
            self._solution = solution
        else:
            self._solution = np.array([uniform(bounds[0], bounds[1]) for i in bounds])
        self._bounds = bounds
        self._min_function = min_function
        self._fitness = self.calc_fitness()

    @property
    def solution(self):
        return self._solution

    @property
    def fitness(self):
        return self._fitness

    @property
    def bounds(self):
        return self._bounds

    def calc_fitness(self):
        return -self._min_function(self._solution.tolist())

    def __setitem__(self, index, value):
        self._solution[index] = value

    def __getitem__(self, index):
        return self._solution[index]

    def __len__(self):
        return self._solution.shape[0]

    def __iter__(self):
        return self._solution.__iter__()

    def __next__(self):
        return next(self._solution)

    def __copy__(self):
        return Genome(self._min_function, self._bounds, solution=np.copy(self._solution))

    def __eq__(self, other):
        return self._solution == other.solution

    def __str__(self):
        return str(self._solution)


class Population(object):
    def __init__(self, min_function, bounds, p_size):
        self._min_function = min_function
        self._bounds = bounds
        self._size = p_size
        self._genomes = []

    def random_genomes(self):
        self._genomes = [Genome(self._min_function, self._bounds) for i in range(self._size)]

    def sort(self, descend=False):
        self._genomes.sort(reverse=descend, key=lambda genome: genome.fitness)

    def append(self, genome):
        self._genomes.append(genome)

    @property
    def worst_index(self):
        return min(self._genomes, key=lambda genome: genome.fitness)

    @property
    def best_index(self):
        return max(self._genomes, key=lambda genome: genome.fitness)

    def __setitem__(self, index, genome):
        self._genomes[index] = genome

    def __getitem__(self, index):
        # if index >= self._size:
        #     raise ValueError("El indice se encuentra fuera del rango")
        return self._genomes[index]

    def __delitem__(self, index):
        del self._genomes[index]

    def __iter__(self):
        return self._genomes.__iter__()

    def __next__(self):
        return next(self._genomes)

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._genomes)

