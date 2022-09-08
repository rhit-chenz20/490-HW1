import random
import csv

from .agent import Genome
from .selection import Selection
from .fitnessFunction import FitnessFunction

class Model():
    """
    args attributes: size, genomeLength, mutationRate, pointRange, pointSize, maxGeneration,
                    elitism, selection, fitnessFunction, filename, topPercent, debug
    """
    def __init__(
        self,
        args
    ):
        seed = random.randint(0,100000)
        # Sucessful trail's seed
        # seed = 77431
        random.seed(seed)

        self.bestFitness = 1000000
        self.mutationRate = args.mutationRate/args.genomeLength
        self.maxGeneration = args.maxGeneration
        self.generation = 0
        self.elitism = args.elitism
        self.crossover_1 = args.crossover
        self.selection = Selection.get_sel(args.selection,args.topPercent,random)
        self.topPercent = args.topPercent
        self.file = open(args.filename+str(seed)+ '_2.csv', "w+")
        self.writer = csv.writer(self.file)
        title = ["Generation", "Max_Fitness","Ave_Fitness", "Min_Fitness"]
        title_genome = ["Generation"]
        for x in range(args.pointSize):
            title_genome.append(x)
        self.geno_file = open(args.filename+str(seed)+ '_geno.csv', "w+")
        self.geno_writer = csv.writer(self.geno_file)
        self.writeToFile(self.writer, title)
        self.writeToFile(self.geno_writer, title_genome)
        self.points = self.generatePoints(args.pointSize, args.pointRange)
        self.population = self.generateIndividuals(args.size, args.fitnessFunction, random, args.pointSize)

    def generatePoints(self, size, range):
        """
        Generate random points
        Returns a dictionary with letters as keys and coordinates as values
        """
        return {1:[-0.0000000400893815,0.0000000358808126],
        2:[-28.8732862244731230,-0.0000008724121069],
        3:[-79.2915791686897506,21.4033307581457670],
        4:[-14.6577381710829471,43.3895496964974043],
        5:[-64.7472605264735108,-21.8981713360336698],
        6:[-29.0584693142401171,43.2167287683090606],
        7:[-72.0785319657452987,-0.1815834632498404],
        8:[-36.0366489745023770,21.6135482886620949],
        9:[-50.4808382862985496 ,-7.3744722432402208],
        10:[-50.5859026832315024 ,21.5881966132975371],
        11:[-0.1358203773809326,28.7292896751977480],
        12:[-65.0865638413727368,36.0624693073746769],
        13:[-21.4983260706612533,-7.3194159498090388],
        14:[-57.5687244704708050,43.2505562436354225],
        15:[-43.0700258454450875,-14.5548396888330487]}

    def generateIndividuals(self, size, fitness_function, ran, genomeLength):
        """
        Generate Individuals
        """
        function = FitnessFunction.get_fitness_function(fitness_function, self.points)
        population=[]
        for x in range(size):
            genome = []
            for y in range(genomeLength):
                """
                Change it to point letters
                """
                genome.append(y+1)

            random.shuffle(genome)
            individual = Genome(genome, function, ran, self.mutationRate)
            population.append(individual)
        return population

    def calData(self):
        """
        Return the average fitness
        """
        result = [self.generation]
        fitnesses = []
        self.population.sort(reverse=True)
        for x in range(len(self.population)):
            fitnesses.append(self.population[x].fitness)
        
        # Highest fitness
        if (self.population[0].fitness < self.bestFitness):
            self.bestFitness = self.population[0].fitness
            row = [self.generation]
            row.extend(self.population[0].genome)
            self.writeToFile(self.geno_writer, row)
        print("Best Fitness: " + str(self.population[0].fitness) + " at generation " + str(self.generation))
        result.append(self.population[0].fitness)
        # print(self.population[0])
        # print("Best Fitness: " + self.bestFitness + " at generation " + self.generation)
        # Average fitness
        result.append(sum(fitnesses) / len(self.population))
        # Lowest fitness
        result.append(self.population[len(self.population)-1].fitness)

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
        for x in range(self.maxGeneration+1):
            self.evolve()
            # self.writeToFile(self.writer,self.calData())

        self.end()

    def end(self):
        """
        End the evolution
        """
        print("End of simulation")
        self.file.close()

    def evolve(self):
        for ind in self.population:
            ind.step()
        data = [self.generation]
        data += self.calData()
        self.writeToFile(self.writer, data)
        if self.generation < self.maxGeneration:
            self.reproduce()
            self.generation += 1

    def reproduce(self):
        """
        Generate the next generation
        """
        parent = self.selection.choose_parent(self.population)
        # for x in range(self.)
        parent.sort(reverse=True)
        elited = []
        for x in range(min(self.elitism, len(parent))):
            elited.append(parent[x])

        for x in range(0,len(parent)-1,2):
            if(self.crossover_1):
                child1  = Genome(self.crossover(parent[x], parent[x+1]),parent[x].fitness_function, parent[x].ran,parent[x].mutationRate)           
                child2  = Genome(self.crossover(parent[x+1], parent[x]),parent[x].fitness_function, parent[x].ran,parent[x].mutationRate)

            else:
                child1  = Genome(parent[x].genome,parent[x].fitness_function, parent[x].ran,parent[x].mutationRate)           
                child2  = Genome(parent[x+1].genome,parent[x].fitness_function, parent[x].ran,parent[x].mutationRate)     
            child1.mutate()
            child2.mutate()

            self.population[x] = child1
            self.population[x+1] = child2
            self.population[x+(len(parent))] = child1
            self.population[x+1+(len(parent))] = child2
        if (len(parent) % 2 != 0):
            self.population[len(self.population)-1] = Genome(parent[len(parent)-1].genome,parent[len(parent)-1].fitness_function, parent[len(parent)-1].ran,parent[len(parent)-1].mutationRate)   

        random.shuffle(self.population)  
        for x in range(len(elited)):
            self.population[x] = elited[x]

    def crossover(self, genome1, genome2):
        gene1 = genome1.genome
        gene2 = genome2.genome

        start = random.randint(0, len(gene1))
        size = random.randint(0, len(gene1))

        childGenome = [None]*len(gene1)

        for x in range(start, start + size, 1):
            childGenome[x % len(gene1)] = gene1[x % len(gene1)]
        
        i = (start+size) % len(gene1)
        for x in range(len(gene2)):
            if (gene2[x] not in childGenome):
                childGenome[i] = gene2[x]
                i = (i + 1)%len(gene2)

        return childGenome