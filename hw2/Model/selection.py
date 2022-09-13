from abc import abstractmethod
class Selection():
    def get_sel(num, top, ran, numb):
        if num == 0 :
            return Top50(top, )
        elif num == 1:
            return Tournament(ran, numb)

    @abstractmethod
    def choose_parent(self, pop):
        pass

class Top50(Selection):
    def __init__(
        self,
        top_percent,
        
    ):
        """
        top_percent: The percentage of the individuals being selected
        """
        super().__init__()
        self.top = top_percent
        # self.elitism = elitism

    def choose_parent(self, pop):
        """
        Choose the top ?% of females as the parent
        """
        pop.sort(reverse=True)
        parent = []
        for x in range(int(len(pop)*self.top)):
            parent.append(pop[x])

        return parent


class Tournament(Selection):
    def __init__(
        self,
        ran,
        num
    ):
        super().__init__()
        self.ran = ran
        self.num = num
        # self.elitism = elitism

    def choose_parent(self, pop):
        """
        Use the tournament selection to choose parent
        """
        pop.sort(reverse=True)
        parent = []
        for x in range(int(len(pop)/2)):
            indexes=[]
            while(len(indexes)!= self.num):
                index = self.ran.randint(0,len(pop)-1)
                if(index not in indexes):
                    indexes.append(index)

            parent.append(pop[min(indexes)])
        return parent