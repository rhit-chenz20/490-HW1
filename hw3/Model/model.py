import random
import csv
from sre_parse import State
import numpy as np
from Model.visualizer import Visualizer

from .agent import CA

class Model():
    """
    args attributes: width(int), state(str), rule(int), filename, debug, seed, dimension
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
        self.visualizer = Visualizer(self.seed, args.rule, args.width, args.duration)
        self.generations = []
        self.maxDuration = args.duration
        self.durationCount = 0
        rule = format(args.rule, "b")
        if(len(rule)<8):
            rule = rule[::-1] + "0"*(8-len(rule))
        lam = rule.count("0") / len(rule)
        print("rule " + str(args.rule) + ": "+rule[::-1] + " with lambda: "+str(lam))
        self.CAs = self.generateRandomStartingState(1, random, args.width, args.state, rule, args.dimension)
        G = ["0"*args.width]*args.duration
        self.visualizer.initVisualizeLive(G)

    def generateRandomStartingState(self,size,ran, width, startingState:str, rule:str, dimension):
        CAs = []
        if(dimension == 1):
            for x in range(size):
                if(startingState=="-1"):
                    state = ""
                    """
                    Generate random starting state
                    """
                    for z in range(width):
                        state+=str(random.choice([0,1]))

                elif(startingState == "m"):
                    state = ["0"]*width
                    state[int(len(state)/2)] = "1"
                    state = "".join(state)
                else:
                    state = startingState
                
                individual = CA(state, ran, rule)
                CAs.append(individual)
                self.generations.append(individual.state)
        # elif (dimension ==2):


        return CAs

    def calData(self):
        """
        Return the average fitness
        """
        result = [self.durationCount]
        
        return result

    def start(self):
        """
        Start the evolution
        """
        for x in range(self.maxDuration+1):
            self.evolve()
            self.visualizer.updateLive(self.generations)
            # self.visualizer.visualizeLive(self.generations)
            # print(self.generation)
        self.end()

    def end(self):
        """
        End the evolution
        """
        self.visualizer.visualize(self.generations)
        # self.visualizer.showLive()
        self.visualizer.endLive()
        print("End of simulation")

    def evolve(self):
        for ind in self.CAs:
            print(ind)
            self.generations.append(ind.state)
            ind.step()
        self.durationCount += 1
        data = [self.durationCount]
        data += self.calData()
        # self.writeToFile(self.writer, data)