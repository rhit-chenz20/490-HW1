import numpy as np
import seaborn as sns
# import sys
import pandas as pd
import matplotlib.pyplot as plt

# get help from https://stackoverflow.com/a/48126960
class Plot():
    def __init__(
        self,
        filenames,
        output,
        debug,
        ):
        self.output = output
        self.debug = debug
        self._setup_filename(filenames)
        # sys.argv

    def _setup_filename(self,filenames):
        """
        Seperating different files based on its filename(might not needed)
        """
        dictionary = {}  
        for x in filenames:  
            li = x.split('_')
            key = x[:x.index(li[len(li)-1])]
            group = dictionary.get(key,[])
            group.append(x)  
            dictionary[key] = group
        ffilenames = dictionary.values()

        self._dataProcessGeno(ffilenames)               
    
    def _dataProcessGeno(self, filenames):
        fit_datas = []
        bests=[]
        worsts=[]
        lasts = []

        for stack1 in filenames:
            fit_data = []
            best_data = []
            worst_data = []
            for file1 in stack1:
                df1 = pd.read_csv(file1, index_col=False).reset_index()
                fit_data.append(df1.filter(items=self.genoNames))
                best_data.append(df1.loc[:, df1.columns!='Generation'].filter(regex="^best_mate"))
                worst_data.append(df1.loc[:, (df1.columns!='Generation') & (df1.index %self.gap == 0)].filter(regex="^worst_mate"))
            fit_datas.append(fit_data) 
            bests.append(best_data)
            worsts.append(worst_data)
            
        for x in range(len(fit_datas)):
            fit_datas[x] = pd.concat(objs=fit_datas[x], ignore_index=True)
            bests[x] = pd.concat(objs=bests[x]).groupby(level=0).mean().T
            worsts[x] = pd.concat(objs = worsts[x]).groupby(level=0).mean().T
            lasts[x] = pd.concat(objs = lasts[x]).groupby(level=0).mean()
            # print(lasts[x])

        self.plot(fit_datas, bests, worsts, lasts)

    def plot(self, thre, thre_conc, lasts):
        labels = ['Average Fitness', 'Sta Dev Fitness', 'Average Threshold', 'Sta Dev Threshold']
        threNames = ["Ave_Fitness", "Std_Fitness", "Ave_Threshold", "Std_Threhold"]
        letters = ['A','B','C','D']

        axd = plt.figure(figsize=(18,8)).subplot_mosaic(
        """
        AB
        CD
        EE
        """,
        )

        color_lines = iter(plt.cm.rainbow(np.linspace(0, 1, len(self.legends))))
        list(map.keys())
        # n sets of data (same length as legends)
        for x in range(len(thre_conc)):
            c_line=next(color_lines)
            
            # four graph
            for y in range(len(threNames)):
                self.lineplot(axd[letters[y]],thre_conc[x],'Generation',threNames[y],"Generation",labels[y],c_line)
                # for z in range(len(thre[0])):
                #     thre[x][z].plot(x='Generation', y=threNames[y], ax=axd[letters[y]], kind='line', c=c_line,label='_nolegend_')
            axd["E"].hist(lasts[x], color=c_line, alpha=0.5)
                
        #         sns.regplot(x=thre_conc[x]['index'],y=thre_conc[x][threNames[y]], lowess=True, 
        #             scatter=False, ax = list(axd.values())[y], color = c_line, ci=95)
                        #     list(axd.values())[y].set(xlabel='Generation', ylabel=self.labels[y])
        #     
        
        list(axd.values())[1].legend(loc='upper left', labels=self.legends,bbox_to_anchor=(1.02, 1))
        axd["E"].set(xlabel='Number of Matings', ylabel="Number of Females")

        identify_axes(axd)
        plt.tight_layout()
        # plt.show() 
        plt.savefig(self.output + ".pdf")

    def lineplot(self, ax, li, x,y,xlabel, ylabel, c):
        sns.lineplot(
            data=li,
            ax=ax,
            x=li[x], y=li[y],
            marker='', color = c
        )
        ax.set(xlabel=xlabel, ylabel=ylabel)
        # ax.legend(loc='upper left', labels=self.legends,bbox_to_anchor=(1.02, 1))

    def plotHeatmap(self, ax, li, title, ylabel):
        sns.heatmap(li, ax =ax, cmap="Greens",vmin=0, vmax=1)
        ax.invert_yaxis()
        ax.set(xlabel='Generation', ylabel=ylabel, title=title)
        c_bar = ax.collections[0].colorbar
        c_bar.set_ticks([0, 0.25, 0.5, 0.75, 1])
        c_bar.set_ticklabels(["0% Female Mate", "25% Female Mate", "50% Female Mate", "75% Female Mate", "100% Female Mate", ])

# https://matplotlib.org/stable/tutorials/provisional/mosaic.html
# Helper function used for visualization in the following examples
def identify_axes(ax_dict, fontsize=48):
    """
    Helper to identify the Axes in the examples below.

    Draws the label in a large font in the center of the Axes.

    Parameters
    ----------
    ax_dict : dict[str, Axes]
        Mapping between the title / label and the Axes.
    fontsize : int, optional
        How big the label should be.
    """
    kw = dict(ha="center", va="center", fontsize=fontsize, color="darkgrey")