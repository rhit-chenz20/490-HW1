import random
import csv
from sre_parse import State
from tkinter.tix import Tree
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
        self.rule = args.rule
        self.seed = seed
        self.visualizer = Visualizer(self.seed, args.rule, args.width, args.duration, args.lampda)
        self.generations = []
        self.maxDuration = args.duration
        self.durationCount = 0
        self.transientDur = -1
        self.prematureEnd = False
        self.transientDurFound = False
        rule = format(args.rule, "b")
        if(len(rule)<=8):
            rule = rule[::-1] + "0"*(8-len(rule))
        lam = rule.count("1") / len(rule)
        print("rule " + str(args.rule) + ": "+rule[::-1] + " with lambda: "+str(lam))
        self.CAs = self.generateRandomStartingState(1, random, args.width, args.state, rule, args.dimension, args.lampda)
        G = ["0"*args.width]*args.duration
        self.visualizer.initVisualizeLive(G)

    def generateRandomStartingState(self,size,ran, width, startingState:str, rule:str, dimension, lampda):
        CAs = []
        if(dimension == 1):
            for x in range(size):
                if(startingState=="-1"):
                    state = ""
                    """
                    Generate random starting state
                    """
                    for z in range(width):
                        if (random.random() > .5):
                            state+= "0"
                        else:
                            state+= str(random.choice([1,2,3]))
                elif(startingState == "m"):
                    state = ["0"]*width
                    state[int(len(state)/2)] = "1"
                    state = "".join(state)
                else:
                    state = startingState
                
                individual = CA(state, ran, lampda)
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
            if (self.prematureEnd == True):
                break
        self.end()

    def end(self):
        """
        End the evolution
        """
        self.visualizer.visualize(self.generations)
        # self.visualizer.showLive()
        self.visualizer.endLive()
        # print("Transient duration for rule " + str(self.rule) + " is " + str(self.transientDur))
        # print(str(self.transientDur))
        print("End of simulation")

    def evolve(self):
        
        for ind in self.CAs:
            currentState = ind.state
            # if not (self.transientDurFound):
            #     # print(ind)
            # if (len(self.generations) > 1 and currentState in self.generations and not self.transientDurFound):
            #     self.transientDur = self.durationCount
            #     self.transientDurFound = True
            #     self.prematureEnd = True
            # print(ind)
            self.generations.append(ind.state)
            ind.step()
        self.durationCount += 1
        data = [self.durationCount]
        data += self.calData()
        # self.writeToFile(self.writer, data)