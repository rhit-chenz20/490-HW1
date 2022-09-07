from abc import abstractmethod
import numpy as np

class FitnessFunction():
    def get_fitness_function(num,points):
        return DistanceFitness(points)

    @abstractmethod
    def cal_fitness(self, ind):
        pass

class DistanceFitness(FitnessFunction):
    def __init__(
        self,
        points
    ):
        self.points = points

    def cal_fitness(self, ind):
        totalDistance = 0
        for k in range(len(ind.genome)):
            a = np.array(self.points.get(ind.genome[k]))
            if ((k + 1) == len(ind.genome)):
                b = np.array(self.points.get(ind.genome[0]))
            else:
                b = np.array(self.points.get(ind.genome[k+1]))
            totalDistance += np.linalg.norm(a-b)
        ind.fitness = totalDistance


