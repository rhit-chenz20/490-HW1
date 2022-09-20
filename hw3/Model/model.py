import random
import csv
from sre_parse import State

from Model.visualizer import Visualizer

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
        self.visualizer = Visualizer(self.seed, args.rule)
        self.generations = []
        self.maxDuration = args.duration
        self.durationCount = 0
        rule = format(args.rule, "b")
        if(len(rule)<8):
            rule = rule[::-1] + "0"*(8-len(rule))
        print("rule " + str(args.rule) + ": "+rule[::-1])
        self.file = open(args.filename+"rule_"+str(args.rule) + "_"+str(seed)+ '.csv', "w+")
        self.writer = csv.writer(self.file)
        title = ["Generation", "Max_Fitness","Ave_Fitness", "Min_Fitness"]
        self.writeToFile(self.writer, title)
        self.CAs = self.generateRandomStartingState(1, random, args.width, args.state, rule)

    def generateRandomStartingState(self,size,ran, width, startingState:str, rule:str):
        CAs = []
        for x in range(size):
            state = ""
            if(startingState=="-1"):
                """
                Generate random starting state
                """
                for z in range(width):
                    state+=str(random.choice([0,1]))
            else:
                state = startingState
            
            individual = CA(state, ran, rule)
            CAs.append(individual)
            # self.generations.append(individual.state)
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
            self.visualizer.visualizeLive(self.generations)
            # print(self.generation)
        self.end()

    def end(self):
        """
        End the evolution
        """
        # print("Seed: " + str(self.seed))
        # print("Best Fitness: " + str(self.bestFitness) + " at generation: " + str(self.bestGeneration))
        # print("Approx Best Fitness: " + str(self.approxBestFitness) + " at generation: " + str(self.approxBestGeneration))
        self.visualizer.visualize(self.generations)
        self.visualizer.showLive()
        print("End of simulation")
        self.file.close()

    def evolve(self):
        for ind in self.CAs:
            print(ind)
            self.generations.append(ind.state)
            ind.step()
        self.durationCount += 1
        data = [self.durationCount]
        data += self.calData()
        self.writeToFile(self.writer, data)