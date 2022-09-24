from array import array
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random




# class Visualizer():

#     def __init__(self, seedNumber, ruleNumber):
#         self.seedNumber = str(seedNumber)
#         self.ruleNumber = str(ruleNumber)
#         self.livePlot = plt()
    
#     def visualize(self, stateList):
#         data = [[]] * len(stateList)
#         for k in range(len(stateList)):
#             data[k] = [*stateList[k]]
#             data[k] = [int(i) for i in data[k]]
#         data = np.array(data)
#         # create discrete colormap
#         # cmap = colors.ListedColormap(['red', 'blue'])
#         # bounds = [0, data.size,20]
#         # norm = colors.BoundaryNorm(bounds, cmap.N)
#         G = np.zeros((len(stateList),len(stateList[0]),3))

#         # Where we set the RGB for each pixel
#         G[data>0.5] = [1,0,1]
#         G[data<0.5] = [0,1,0]
#         fig, ax = plt.subplots()
#         ax.imshow(G, cmap="binary",interpolation='nearest')
#         # plt.axis('off')
#         # ax.set_xlabel("Location")
#         # ax.set_ylabel("Generation")
#         # xList = range(0, len(stateList[0]))
#         # yList = range(0, len(stateList))
#         # plt.xticks(xList)
#         # plt.yticks(yList)
#         plt.axis("off")
#         plt.savefig("Rule " + self.ruleNumber + "_" + self.seedNumber + ".png")

#     def visualizeLive(self, stateList):
#         data = [[]] * len(stateList)
#         for k in range(len(stateList)):
#             data[k] = [*stateList[k]]
#             data[k] = [int(i) for i in data[k]]
#         data = np.array(data)
#         # create discrete colormap
#         G = np.zeros((len(stateList),len(stateList[0]),3))
#         # Where we set the RGB for each pixel
#         G[data>0.5] = [1,0,1]
#         G[data<0.5] = [0,1,0]
#         self.livePlot.imshow(G, cmap="binary",interpolation='nearest')
#         self.livePlot.axis("off")
#         self.livePlot.pause(0.01)

#     def showLive(self):
#         self.livePlot.close()
#         self.livePlot.show()

class Visualizer():

    def __init__(self, seedNumber, ruleNumber, width, duration):
        self.seedNumber = str(seedNumber)
        self.ruleNumber = str(ruleNumber)
        self.liveFig, self.liveAx = plt.subplots()
        self.bg = None
        self.bits = None
        self.width = width
        self.duration = duration
    
    def visualize(self, stateList):
        # pass
        data = [[]] * len(stateList)
        for k in range(len(stateList)):
            data[k] = [*stateList[k]]
            data[k] = [int(i) for i in data[k]]
        data = np.array(data)
        G = np.zeros((len(stateList),len(stateList[0]),3))
        G[data>0.5] = [0,0,0]
        G[data<0.5] = [1,1,1]
        fig, ax = plt.subplots()
        ax.imshow(G)
        plt.axis("off")
        plt.savefig(r"photos/part1.5/Rule " + self.ruleNumber + "_" + self.seedNumber + ".png")
        plt.close()

    def initVisualizeLive(self, stateList):
        # pass
        data = [[]] * len(stateList)
        for k in range(len(stateList)):
            data[k] = [*stateList[k]]
            data[k] = [int(i) for i in data[k]]
        data = np.array(data)
        G = np.zeros((len(stateList),len(stateList[0]),3))
        G[data>0.5] = [0,0,0]
        G[data<0.5] = [1,1,1]
        self.bits = self.liveAx.imshow(G)
        plt.axis("off")
        plt.show(block=False)
        plt.pause(0.1)
        self.bg = self.liveFig.canvas.copy_from_bbox(self.liveFig.bbox)
        self.liveAx.draw_artist(self.bits)
        self.liveFig.canvas.blit(self.liveFig.bbox)

    def updateLive(self, stateList):
        # pass
        self.liveFig.canvas.restore_region(self.bg)
        data = [[]] * (self.duration+2)
        for k in range(len(stateList)):
            data[k] = [*stateList[k]]
            data[k] = [int(i) for i in data[k]]
        for k in range(len(stateList), len(data)):
            data[k] = [0] * self.width
        data = np.array(data)
        G = np.zeros((self.duration+2,self.width,3))
        G[data>0.5] = [0,0,0]
        G[data<0.5] = [1,1,1]
        self.bits.set_data(G)
        self.liveAx.draw_artist(self.bits)
        self.liveFig.canvas.blit(self.liveFig.bbox)
        self.liveFig.canvas.flush_events()
        plt.pause(.01)

    def initLiveConway(self, stateList):
        data = []
        for k in range(len(stateList)):
            data.append([*stateList[k]])
            data[k] = [int(i) for i in data[k]]
        data = np.array(data)
        G = np.zeros((len(stateList),len(stateList[0]),3))
        G[data>0.5] = [0,0,0]
        G[data<0.5] = [1,1,1]
        self.bits = self.liveAx.imshow(G)
        plt.axis("off")
        plt.show(block=False)
        plt.pause(0.1)
        self.bg = self.liveFig.canvas.copy_from_bbox(self.liveFig.bbox)
        self.liveAx.draw_artist(self.bits)
        self.liveFig.canvas.blit(self.liveFig.bbox)
    
    def updateLiveConway(self, stateList):
        self.liveFig.canvas.restore_region(self.bg)
        data = []
        for k in range(len(stateList)):
            data.append([*stateList[k]])
            data[k] = [int(i) for i in data[k]]
        data = np.array(data)
        G = np.zeros((len(stateList),len(stateList[0]),3))
        G[data>0.5] = [0,0,0]
        G[data<0.5] = [1,1,1]
        self.bits.set_data(G)
        self.liveAx.draw_artist(self.bits)
        self.liveFig.canvas.blit(self.liveFig.bbox)
        self.liveFig.canvas.flush_events()
        plt.pause(.1)
        
    def endLive(self):
        # pass/
        plt.show(block=True)

