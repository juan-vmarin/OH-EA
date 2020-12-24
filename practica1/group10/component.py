import numpy as np
from random import uniform


class Genome(object):
    """Class to represent a genome
    """

    def __init__(self, solution, min_function, bounds):
        """Initialize the bounds, function to minimize and solution if exists

        Args:
            solution ([float,] or numpy.array): Solution to initialize
            min_function: A function to minimize
            bounds: Limits to get solution
        """
        self._solution = solution
        self._min_function = min_function
        self._bounds = bounds
        self._fitness = self._calc_fitness()

    @property
    def solution(self):
        """solution value

        Returns:
            numpy.array: solution
        """
        return self._solution

    @property
    def fitness(self):
        """Get the fitness value of how good is the genome as solution of the problem

        Returns:
            int: Quantification of how good the solution is
        """
        return self._fitness

    @property
    def bounds(self):
        """Get the limits of the solution

        Returns:
            [(float, float),]: Bounds of solution
        """
        return self._bounds

    def _calc_fitness(self):
        """Calculate the fitness

        Returns:
            float: fitness
        """
        return -self._min_function(self._solution.tolist())

    def __setitem__(self, index, value):
        """Set a gen value

        Args:
            index (int): Index
            value (float): Gen
        """
        if value > self._bounds[index][1]:
            value = self._bounds[index][1]
        elif value < self._bounds[index][0]:
            value = self._bounds[index][0]
        self._solution[index] = value
        self._fitness = self._calc_fitness()

    def __getitem__(self, index):
        """Get a gen value

        Args:
            index (int): Index

        Returns:
            [float]: Gen
        """
        return self._solution[index]

    def __len__(self):
        """Length of the solution

        Returns:
            [int]: length
        """
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
    """Class to represent a population of genome
    """

    def __init__(self, min_function, bounds, p_size, random=False):
        """Initialize the bounds, function to minimize, population size

        Args:
            min_function: A function to minimize
            bounds: Limits to get solution
            p_size (int): Population size
            random (bool): True to generate random genomes. Defaults False.
        """
        self._min_function = min_function
        self._bounds = bounds
        self._size = p_size
        if random:
            self._random_genomes()
        else:
            self._genomes = []

    def _random_genomes(self):
        """Generate a random genomes between bounds
        """
        self._genomes = [Genome(np.array([uniform(bound[0], bound[1]) for bound in self._bounds]), self._min_function,
                                self._bounds) for _ in range(self._size)]

    def sort(self, descend=False):
        """Sort the genomes depending on fitness

        Args:
            descend (bool, optional): Descend or ascend sort
        """
        self._genomes.sort(reverse=descend, key=lambda genome: genome.fitness)

    def append(self, genome):
        """Add new genome at the end of the list

        Args:
            genome (component.Genome): New genome
        """
        self._genomes.append(genome)

    @property
    def worst_index(self):
        """Get a worst genome index

        Returns:
            int: Index of the worst genome
        """
        return self._genomes.index(min(self._genomes, key=lambda genome: genome.fitness))

    @property
    def best_index(self):
        """Get the best genome index

        Returns:
            Int: Index of best genome
        """
        return self._genomes.index(max(self._genomes, key=lambda genome: genome.fitness))

    def __setitem__(self, index, genome):
        """Set a genome

        Args:
            index (int): Index
            genome (component.Genome): New Genome
        """
        self._genomes[index] = genome

    def __getitem__(self, index):
        """Get a genome

        Args:
            index (int): Position

        Returns:
            Genome: A genome of the position past as an index
        """
        return self._genomes[index]

    def __delitem__(self, index):
        """Remove a genome

        Args:
            index (int): Index of the gen deleted
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
