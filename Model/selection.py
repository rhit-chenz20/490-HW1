from abc import abstractmethod
class Selection():
    def get_sel(num, top, ran, elitism):
        if num == 0 :
            return Top50(top, elitism)
        elif num == 1:
            return Tournament(ran, elitism)

    @abstractmethod
    def choose_parent(self, pop):
        pass

class Top50(Selection):
    def __init__(
        self,
        top_percent,
        elitism
    ):
        """
        top_percent: The percentage of the individuals being selected
        """
        super().__init__()
        self.top = top_percent
        self.elitism = elitism

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
        elitism
    ):
        super().__init__()
        self.ran = ran
        self.elitism = elitism

    def choose_parent(self, pop):
        """
        Use the tournament selection to choose parent
        """
        pop.sort(reverse=True)
        parent = []
        for x in range(int(len(pop)/2)):
            index1 = self.ran.randint(0,len(pop)-1)
            index2 = self.ran.randint(0,len(pop)-1)
            if(index1 == index2):
                index2 = self.ran.randint(0,len(pop)-1)
            if(pop[index1].fitness <= pop[index2].fitness):
                parent.append(pop[index1])
            else:
                parent.append(pop[index2])
        return parent