from abc import abstractmethod
import math

class FitnessFunction():
    def get_fitness_function(num):
        if(num == 0):
            return DistanceFitness()

    @abstractmethod
    def cal_fitness(self, female):
        pass

class DistanceFitness(FitnessFunction):
    def cal_fitness(self, female):
        pass
