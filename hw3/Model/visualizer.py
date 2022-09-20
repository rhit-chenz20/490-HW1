import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import random




class Visualizer():
    
    def visualize(self, stateList):
        data = [[]] * len(stateList)
        for k in range(len(stateList)):
            data[k] = [*stateList[k]]
            data[k] = [int(i) for i in data[k]]
        data = np.array(data)
        # create discrete colormap
        cmap = colors.ListedColormap(['red', 'blue'])
        bounds = [0, data.size,20]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        G = np.zeros((len(stateList),len(stateList[0]),3))

        # Where we set the RGB for each pixel
        G[data>0.5] = [1,0,1]
        G[data<0.5] = [0,1,0]
        fig, ax = plt.subplots()
        ax.imshow(G, cmap="binary",interpolation='nearest')
        # plt.axis('off')
        ax.set_xlabel("Location")
        ax.set_ylabel("Generation")
        xList = range(0, len(stateList[0]))
        yList = range(0, len(stateList))
        plt.xticks(xList)
        plt.yticks(yList)
        plt.show()

stateList = [''] * 20
for k in range (20):
    for j in range (20):
        stateList[k] += str(random.randint(0, 1))
print("Input: ", stateList)
visualizer = Visualizer()
visualizer.visualize(stateList)