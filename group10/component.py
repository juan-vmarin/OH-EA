import numpy as np
from random import uniform


class Genome(object):
    """Class to represent a genome
    """
    def __init__(self, min_function, bounds, solution=None):
        """initialize the bounds, function to minimize and solution if exists

        Args:
            min_function: a function to minimize
            bounds (np.array): limits to get solution
            solution ([float,] or np.array, optional): solution to initialize. Defaults to None.
        """
        if solution is not None:
            self._solution = solution
        else:
            self._solution = np.array([uniform(bounds[0], bounds[1]) for i in bounds])
        self._bounds = bounds
        self._min_function = min_function
        self._fitness = self._calc_fitness()

    @property
    def solution(self):
        """solution value

        Returns:
            np.Array:
        """
        return self._solution

    @property
    def fitness(self):
        """fitness value

        Returns:
            int:
        """
        return self._fitness

    @property
    def bounds(self):
        """bounds

        Returns:
            [(float, float),]:
        """
        return self._bounds

    def _calc_fitness(self):
        """calculate the fitness

        Returns:
            float:
        """
        return -self._min_function(self._solution.tolist())

    def __setitem__(self, index, value):
        """set a gen value

        Args:
            index (int): index
            value (float): gen
        """
        self._solution[index] = value

    def __getitem__(self, index):
        """get a gen value

        Args:
            index (int): index

        Returns:
            [float]: gen
        """
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
        return sum(self._solution == other.solution) == self._solution.shape[0]

    def __str__(self):
        return str(self._solution)


class Population(object):
    """class to represent a population of genome
        """

    def __init__(self, min_function, bounds, p_size):
        """initialize the bounds, function to minimize and population size

        Args:
            min_function: a function to minimize
            bounds (np.array): limits to get solution
            p_size (int): population size
        """
        self._min_function = min_function
        self._bounds = bounds
        self._size = p_size
        self._genomes = []

    def random_genomes(self):
        """generate a random genomes between bounds
        """
        self._genomes = [Genome(self._min_function, self._bounds) for i in range(self._size)]

    def sort(self, descend=False):
        """sort the genomes depending on fitness

        Args:
            descend (bool, optional): descend or ascend sort
        """
        self._genomes.sort(reverse=descend, key=lambda genome: genome.fitness)

    def append(self, genome):
        """add new genome to final

        Args:
            genome (Genome): new genome
        """
        self._genomes.append(genome)

    @property
    def worst_index(self):
        """get a worst genome index

        Returns:
            int:
        """
        return min(self._genomes, key=lambda genome: genome.fitness)

    @property
    def best_index(self):
        """get the best genome index

        Returns:
            int:
        """
        return max(self._genomes, key=lambda genome: genome.fitness)

    def __setitem__(self, index, genome):
        """set a genome

        Args:
            index (int): index
            genome (Genome): new Genome
        """
        self._genomes[index] = genome

    def __getitem__(self, index):
        """get a genome

        Args:
            index (int):

        Returns:
            Genome:
        """
        return self._genomes[index]

    def __delitem__(self, index):
        """remove a genome

        Args:
            index (int): index
        """
        del self._genomes[index]

    def __iter__(self):
        return self._genomes.__iter__()

    def __next__(self):
        return next(self._genomes)

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._genomes)

