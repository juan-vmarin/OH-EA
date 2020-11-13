import numpy as np
from random import uniform


class Genome(object):
    """Class to represent a genome
    """

    def __init__(self, solution, min_function, bounds):
        """initialize the bounds, function to minimize and solution if exists

        Args:
            solution ([float,] or np.array, optional): solution to initialize. Defaults to None.
            min_function: a function to minimize
            bounds (np.array): limits to get solution
        """
        self._solution = solution
        self._min_function = min_function
        self._bounds = bounds
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
        """fitness value of how good is the genome as solution of the problem

        Returns:
            int: quantification of how good it is
        """
        return self._fitness

    @property
    def bounds(self):
        """bounds

        Returns:
            [(float, float),]: bounds
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
        if value > self._bounds[index][1]:
            value = self._bounds[index][1]
        elif value < self._bounds[index][0]:
            value = self._bounds[index][0]
        self._solution[index] = value
        self._fitness = self._calc_fitness()

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
        return Genome(np.copy(self._solution), self._min_function, self._bounds)

    def __eq__(self, other):
        return (self._solution == other.solution).all()

    def __ne__(self, other):
        return not (self._solution == other.solution).all()

    def __str__(self):
        return str(self._solution)

    def __cmp__(self, other):
        return self._fitness - other.fitness

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0


class Population(object):
    """class to represent a population of genome
        """

    def __init__(self, min_function, bounds, p_size):
        """initialize the bounds, function to minimize and population size

        Args:
            min_function: a function to minimize
            bounds: limits to get solution
            p_size (int): population size
        """
        self._min_function = min_function
        self._bounds = bounds
        self._size = p_size
        self._genomes = []

    def random_genomes(self):
        """generate a random genomes between bounds
        """
        self._genomes = [Genome(np.array([uniform(bound[0], bound[1]) for bound in self._bounds]), self._min_function,
                                self._bounds) for _ in range(self._size)]

    def sort(self, descend=False):
        """sort the genomes depending on fitness

        Args:
            descend (bool, optional): descend or ascend sort
        """
        self._genomes.sort(reverse=descend, key=lambda genome: genome.fitness)

    def append(self, genome):
        """add new genome at the end

        Args:
            genome (Genome): new genome
        """
        self._genomes.append(genome)

    @property
    def worst_index(self):
        """get a worst genome index

        Returns:
            int: index of the worst genome
        """
        return self._genomes.index(min(self._genomes, key=lambda genome: genome.fitness))

    @property
    def best_index(self):
        """get the best genome index

        Returns:
            int: index of best genome
        """
        return self._genomes.index(max(self._genomes, key=lambda genome: genome.fitness))

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
            index (int): position

        Returns:
            Genome: a genome of the position past as an index
        """
        return self._genomes[index]

    def __delitem__(self, index):
        """remove a genome

        Args:
            index (int): index of the gen deleted
        """
        del self._genomes[index]

    def __iter__(self):
        return self._genomes.__iter__()

    def __next__(self):
        return next(self._genomes)

    def __len__(self):
        return self._size

    def __str__(self):
        return '[' + '\n'.join([str(i) for i in self._genomes]) + ']'
