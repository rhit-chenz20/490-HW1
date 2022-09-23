
import itertools
class CA():
    def __init__(
        self,
        state,
        ran,
        lampda
    ):
        """
        Create a new Female.
        """
        self.state = state
        self.ran = ran
        self.ruleMap = {}
        count = 0
        for perm in itertools.product([0, 1, 2, 3], repeat=5):
            count = count +1
            if (self.allCharactersSame(self.convertTuple(perm))):
                self.ruleMap[self.convertTuple(perm)] = self.convertTuple(perm)[0]
            elif (self.isPlanarRotation(self.convertTuple(perm))):
                self.ruleMap[self.convertTuple(perm)] =  self.ruleMap[self.getPlanarRotation(self.convertTuple(perm))]
            else:
                if (ran.random() < (1-lampda)):
                    self.ruleMap[self.convertTuple(perm)] = "0"
                else:
                    self.ruleMap[self.convertTuple(perm)] = str(ran.choice([1,2,3]))
        print(count)
            
    def isPlanarRotation(self, string):
        for k in range(1, 6):
            if (self.rotate(string, k) in self.ruleMap):
                return True
        return False

    def getPlanarRotation(self, string):
        for k in range(1, 6):
            if (self.rotate(string, k) in self.ruleMap):
                return self.rotate(string, k)

    def rotate(self, strg, n):
        return strg[n:] + strg[:n]
        
    def step(self):
        self.computeNextState()

    def convertTuple(self, tup):
        # initialize an empty string
        string = ''
        for item in tup:
            string = string + str(item)
        return string
    def allCharactersSame(self, s) :
        n = len(s)
        for i in range(1, n) :
            if s[i] != s[0] :
                return False
        return True

    def computeNextState(self):
        helperState = self.state
        helperState = self.state[-2:] + helperState
        helperState = helperState + self.state[:2]
        # helperState2 = helperState
        # for k in range(len(helperState)):
        #     if (int(helperState[k]) > 0):
        #         helperState = helperState[:k] + "1" + helperState[k+1:]
        newState = ""
        for k in range (2, len(self.state) + 2):
            neighborhood = helperState[k-2:k+3]
            newState += str(self.ruleMap[neighborhood])
        # count = 0
        # for k in range (2, len(self.state) + 2):
        #     neighborhood = helperState2[k-2:k+3]
        #     if (self.allCharactersSame(neighborhood)):
        #         newState = newState[:count] + neighborhood[0] + newState[count+1:]
        #     count += 1
        self.state = newState
    
    

    def __repr__(self):
        return self.state
