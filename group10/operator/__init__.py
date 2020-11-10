from abc import ABC, abstractmethod


class CrossoverOperator(ABC):
    @abstractmethod
    def apply(self, *genomes):
        pass


class MutationOperator(ABC):
    @abstractmethod
    def apply(self, *genomes):
        pass


class SelectionOperator(ABC):
    @abstractmethod
    def apply(self, population, k):
        pass


class ReplacementOperator(ABC):
    @abstractmethod
    def apply(self, *population):
        pass
