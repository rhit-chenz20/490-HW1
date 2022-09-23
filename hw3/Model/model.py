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
        self.visualizer = Visualizer(self.seed, args.rule, args.width, args.duration)
        self.generations = []
        self.maxDuration = args.duration
        self.durationCount = 0
        self.transientDur = -1
        self.prematureEnd = False
        self.transientDurFound = False
        self.dimen = args.dimension
        rule = format(args.rule, "b")
        if(len(rule)<=8):
            rule = rule[::-1] + "0"*(8-len(rule))
        lam = rule.count("1") / len(rule)
        # print("rule " + str(args.rule) + ": "+rule[::-1] + " with lambda: "+str(lam))
        self.CAs = self.generateRandomStartingState(1, random, args.width,args.height, args.state, rule, args.dimension,args.percentage/100)
        G = ["0"*args.width]*args.height
        if (self.dimen == 1):
            self.visualizer.initVisualizeLive(G)
        else:
            self.visualizer.initLiveConway(G)

    def generateRandomStartingState(self,size,ran, width,height, startingState:str, rule:str, dimension, percentage):
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
        elif (dimension ==2):
            for x in range(size):
                state = []
                for y in range(height):
                    states = [1,0]
                    weights = [percentage, 1-percentage]
                    state.append(random.choices(states,weights,k=width))
                individual = CA(state, ran,rule)
        CAs.append(individual)
        self.generations.append(individual.state)

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
            if (self.dimen == 1):
                self.visualizer.updateLive(self.generations)
            if (self.prematureEnd == True):
                break
        self.end()

    def end(self):
        """
        End the evolution
        """
        print(self.generations)
        if (self.dimen ==1 ):
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
            if (self.dimen == 2):
                self.visualizer.updateLiveConway(ind.state)
            self.generations.append(ind.state)
            ind.step()
        self.durationCount += 1
        data = [self.durationCount]
        data += self.calData()
        # self.writeToFile(self.writer, data)