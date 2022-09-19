import copy
from abc import abstractmethod
from turtle import right

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

class Tree():
    def __init__(
        self
    ):
        self.root = None

    def insert(self, val):
        if(self.root==None):
            print("root is created")
            self.root = Node(val)
            return
        self.root = self.root.insert(val,BooleanWrapper(False))
    
    def preorder(self):
        return Preorder.preorder_node(self.root)

    # def __str__(self):
    #     pass

class Node():
    def __init__(
        self,
        val,
    ):
        self.value = val
        self.right = None
        self.left = None
        self.terminals = [101, -10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

    # get help from: https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/
    def insert(self, val, bol):
        if (self.is_terminal()):
            return self

        if(not bol.bool):
            if (self.left):
                self.left = self.left.insert(val,bol)
            else:
                self.left = Node(val)
                bol.bool = True

        if(not bol.bool):
            if (self.right != None):
                self.right = self.right.insert(val,bol)
            else:
                self.right = Node(val)
                bol.bool = True
        return self
            
    def __repr__(self):
        return str(self.value)

    def is_terminal(self):
        return (self.value in self.terminals)

class Preorder():   
    def preorder_node(node):
        result = []
        result.append(node)
        if(node.left!=None):
            result.extend(Preorder.preorder_node(node.left))
        
        if(node.right!=None):
            result.extend(Preorder.preorder_node(node.right))

        return result

class BooleanWrapper():
    def __init__(self,bol):
        self.bool =  bol
