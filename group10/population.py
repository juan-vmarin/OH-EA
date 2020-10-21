from group10.genome import Genome
import numpy as np


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
