import copy
from abc import abstractmethod

class Individual():
    def __init__(
        self,
        genome,
        fitness_function,
        mutationRate
    ):
        """
        Create a new individual.
        """
        self.fitness = 0.0
        self.fitness_function = fitness_function
        self.genome = copy.deepcopy(genome)
        self.mutationRate = mutationRate

    def step(self):
        self.calFitness()

    def calFitness(self):
        self.fitness_function.cal_fitness(self)

    @abstractmethod
    def mutate(self, ran):
        pass

    def __lt__(self, otherF):
        return self.fitness > otherF.fitness

class Genome(Individual):
    def __init__(
        self,
        genome,
        fit,
        ran,
        mutationRate
    ):
        """
        Create a new Female.
        """
        super().__init__(genome,fit,mutationRate)
        self.ran = ran

    def step(self):
        self.calFitness()

    def mutate(self):
        mutationCount = 0
        for x in range(len(self.genome)): 
            if(self.ran.uniform(0,1) <= self.mutationRate):
                mutationCount = mutationCount + 1
                anotherindex = self.ran.randint(0,len(self.genome)-1)
                while(anotherindex==x):
                    anotherindex = self.ran.randint(0,len(self.genome)-1)
                temp = self.genome[x]
                self.genome[x] = self.genome[anotherindex]
                self.genome[anotherindex] = temp
        # print(mutationCount)
    
    def __repr__(self):
        return "".join(str(x)+"," for x in self.genome) + " fitness: "+str(self.fitness)

