import copy
from abc import abstractmethod
from turtle import right

class CA():
    def __init__(
        self,
        state,
        ran,
        rule
    ):
        """
        Create a new Female.
        """
        self.state = state
        self.ran = ran
        self.rule = rule

    def step(self):
        self.computeNextState()

    def computeNextState(self):
        pass

    def __repr__(self):
        result = ''
        for bit in self.state:
            result += bit
        return result
