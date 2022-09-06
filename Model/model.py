import statistics
import random
import csv
import numpy as np

from .agent import Genome
from .selection import Selection
from .fitnessFunction import FitnessFunction

class Model():
    """
    args attributes: size, genomeLength, mutationRate, pointRange, pointSize, maxGeneration,
                    elitism, selection, fitnessFunction, filename, topPercent, debug
    """
    def __init__(
        self,
        args
    ):
        self.ran = Randomizer()
        self.population = self.generateIndividuals(args.size, args.fitnessFunction, self.ran, args.genomeLength)
        self.mutationRate = args.mutationRate/self.genome_length
        self.maxGeneration = args.maxGeneration
        self.points = self.generatePoints(args.pointSize, args.pointRange)
        self.generation = 0
        self.maxGen = args.maxGeneration
        self.selection = Selection.get_sel(args.selection,args.topPercent,self.ran, args.elitism)
        self.topPercent = args.topPercent
        self.file = open(args.filename, "w+")
        self.writer = csv.writer(self.file)

        title = ["Generation","Ave_Fitness", "Std_Fitness", "Ave_Threshold", "Std_Threhold"]
        self.writeToFile(self.writer, title)

    def generatePoints(self, size, range):
        """
        Generate random points
        Returns a dictionary with letters as keys and coordinates as values
        """
        pass

    def generateIndividuals(self, size, fitness_function, ran, genomeLength):
        """
        Generate Individuals
        """
        function = FitnessFunction.get_fitness_function(fitness_function)
        population=[]
        for x in range(size):
            genome = []
            for y in range(genomeLength):
                """
                Change it to point letters
                """
                genome.append(ran.ranInt(2))

            individual = Genome(genome, function, ran)
            population.append(individual)
        return population

    def calData(self):
        """
        Return the average fitness
        """
        result = [self.generation]
        fitnesses = []
        self.population.sort(reverse=True)
        for x in range(len(self.population)):
            fitnesses.append(self.population[x].fitness)
        
        # Highest fitness
        result.append(self.population[0].fitness)
        # Average fitness
        result.append(sum(fitnesses) / len(self.population))
        # Lowest fitness
        result.append(self.population[len(self.population)-1].fitness)

        return result

    def writeToFile(self,writer, row):
        """
        Write a row into csv file
        """
        writer.writerow(row)

    def start(self):
        """
        Start the evolution
        """
        for x in range(self.maxGen+1):
            self.evolve()
            self.writeToFile(self.writer,self.calData())

        self.end()

    def end(self):
        """
        End the evolution
        """
        print("End of simulation")
        self.file.close()

    def evolve(self):
        for female in self.population:
            female.step()
        data = [self.generation]
        data += self.calData()
        self.writeToFile(self.writer, data)
        if self.generation < self.maxGen:
            self.reproduce()
            self.generation += 1

    def reproduce(self):
        """
        Generate the next generation
        """
        parent = self.selection.choose_parent(self.population)
        for x in range(len(self.population)):
            index = self.ran.ranInt(len(parent))
            child = Genome(parent[index].genome, parent[index].fitness_function, 
            ran=parent[index].ran,mutationRate=parent[index].mutationRate)
            child.mutate()
        
            self.population[x] = child

    



class Randomizer():
    def norran(self, sigma, mu):
        return np.random.normal(mu, sigma)

    def ranInt(self, size):
        return random.randint(0, size - 1)

    def valmu(self, sigma):
        return np.random.normal(0,sigma)

    def ranMale(self, sigma):
        return np.random.normal(5, sigma)

    def poisson(self, lam):
        return np.random.poisson(lam)
