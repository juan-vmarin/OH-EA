from abc import ABC, abstractmethod


class CrossoverOperator(ABC):
    """Crossover Operator abstract class
    """

    @abstractmethod
    def apply(self, *genomes):
        pass


class MutationOperator(ABC):
    """Mutation Operator abstract class
    """

    @abstractmethod
    def apply(self, *genomes):
        pass




class ReplacementOperator(ABC):
    """Replacement Operator abstract class
    """

    @abstractmethod
    def apply(self, *population):
        pass
