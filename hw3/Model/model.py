import random
import csv
from sre_parse import State

from .agent import CA

class Model():
    """
    args attributes: width(int), state(str), rule(int), filename, debug, seed
    """
    def __init__(
        self,
        args
    ):

        if(args.seed==-1):
            seed = random.randint(0,100000)
        else: seed = args.seed
        random.seed(seed)
        self.seed = seed
        self.maxDuration = args.duration
        self.durationCount = 0
        # bitstring representation of given Wolfram’s notation
        rule = format(args.rule, "b")


        # self.approxFound = False
        # self.approxBestFitness = 1000000
        # self.approxBestGeneration = 0
        # self.bestGeneration = 0
        # self.bestFitness = 1000000
        
        self.file = open(args.filename+str(seed)+ '_2.csv', "w+")
        self.writer = csv.writer(self.file)
        title = ["Generation", "Max_Fitness","Ave_Fitness", "Min_Fitness"]
        title_genome = ["Generation"]
        for x in range(args.pointSize):
            title_genome.append(x)
        self.geno_file = open(args.filename+str(seed)+ '_geno.csv', "w+")
        self.geno_writer = csv.writer(self.geno_file)
        self.writeToFile(self.writer, title)
        self.writeToFile(self.geno_writer, title_genome)
        self.CAs = self.generateStartingState(1, random, args.width, args.state, rule)

    def generateStartingState(self,size,ran, width, startingState:str, rule:str):
        CAs = []
        for x in range(size):
            if(startingState==-1):
                """
                TODO: generate random starting state
                """
            else:
                state = []
                for y in range(width):
                    """
                    TODO: generate starting state using given 
                    """
                    state.append(y+1)
                individual = CA(state, ran, rule)
            CAs.append(individual)
        return CAs

    def calData(self):
        """
        Return the average fitness
        """
        result = [self.durationCount]
        # fitnesses = []
        # self.state.sort(reverse=True)
        # for x in range(len(self.state)):
        #     fitnesses.append(self.state[x].fitness)
        
        # # Highest fitness
        # if ((self.state[0].fitness <= (284.38086286247795*1.1)) and not self.approxFound):
        #     self.approxBestFitness = self.state[0].fitness
        #     self.approxBestGeneration = self.generation
        #     self.approxFound = True

        # if (self.state[0].fitness < self.bestFitness):
        #     self.bestGeneration = self.generation
        #     self.bestFitness = self.state[0].fitness
        #     row = [self.generation]
        #     row.extend(self.state[0].genome)
        #     row.append(self.state[0].fitness)
        #     self.writeToFile(self.geno_writer, row)
        #     # print("Best Fitness: " + str(self.population[0].fitness) + " at generation " + str(self.generation))
        # result.append(self.state[0].fitness)
        # # print(self.population[0])
        # # print("Best Fitness: " + self.bestFitness + " at generation " + self.generation)
        # # Average fitness
        # result.append(sum(fitnesses) / len(self.state))
        # # Lowest fitness
        # result.append(self.state[len(self.state)-1].fitness)

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
        for x in range(self.maxDuration+1):
            self.evolve()
            # print(self.generation)
        self.end()

    def end(self):
        """
        End the evolution
        """
        # print("Seed: " + str(self.seed))
        # print("Best Fitness: " + str(self.bestFitness) + " at generation: " + str(self.bestGeneration))
        # print("Approx Best Fitness: " + str(self.approxBestFitness) + " at generation: " + str(self.approxBestGeneration))
        print("End of simulation")
        self.file.close()
        self.geno_file.close()

    def evolve(self):
        if self.durationCount < self.maxDuration:
            for ind in self.CAs:
                print(ind)
                ind.step()
            self.durationCount += 1
        data = [self.durationCount]
        data += self.calData()
        self.writeToFile(self.writer, data)