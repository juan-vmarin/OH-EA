from group10.genome import Genome


class Population(object):
    def __init__(self):
        self.__genomes = []

    def sort(self, reverse=False):
        return self.__genomes.sort(reverse=reverse, key=lambda genome: genome.fitness)

    def set(self, index, genome):
        self.__genomes[index] = genome

    def get(self, index):
        return self.__genomes[index]

    def add(self, genome):
        self.__genomes.append(genome)

    def remove(self, index):
        del self.__genomes[index]
