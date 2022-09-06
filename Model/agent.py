import copy
from abc import abstractmethod

class Individual():
    def __init__(
        self,
        genome,
        fitness_function,
        mutationRate
    ):
        """
        Create a new individual.
        """
        self.fitness = 0.0
        self.fitness_function = fitness_function
        self.genome = copy.deepcopy(genome)
        self.mutationRate = mutationRate

    def step(self):
        self.calFitness()

    def calFitness(self):
        self.fitness_function.cal_fitness(self)

    @abstractmethod
    def mutate(self, ran):
        pass

    def __lt__(self, otherF):
        return self.fitness < otherF.fitness

class Genome(Individual):
    def __init__(
        self,
        genome,
        fit,
        ran,
        mutationRate
    ):
        """
        Create a new Female.
        """
        super().__init__(genome,fit,mutationRate)
        self.ran = ran

    def step(self):
        """
        NOT YET IMPLEMENTED
        """
        self.calFitness()

    def mutate(self):
        """
        NOT YET IMPLEMENTED
        """

