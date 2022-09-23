class CA():
    def __init__(
        self,
        state,
        ran,
        rule
    ):
        """
        Create a new CA.
        """
        self.state = state
        self.ran = ran
        self.rule = rule

    def step(self):
        self.computeNextState()

    def computeNextState(self):
        if(type(self.state)==str):
            old = self.state[len(self.state)-1]+self.state[:2]
            binint = int(old,2)
            nextstate = self.rule[::-1][binint:binint+1]  
            for x in range(1, len(self.state)-1,1):
                cur = self.state[x-1:(x+2)]
                binint = int(cur,2)
                nextstate += self.rule[binint:binint+1]
            old = self.state[len(self.state)-2:]+self.state[:1]
            binint = int(old,2)
            nextstate += self.rule[binint:binint+1]
            self.state = nextstate
        elif(type(self.state)==list):
            nextstate = [ [ "-1" for i in range(len(self.state[0])) ] for j in range(len(self.state)) ]
            for x in range(len(self.state)):
                for y in range(len(self.state[0])):
                    neighbors =[self.state[(x-1)%len(self.state[0])][(y-1)%len(self.state)],
                    self.state[(x-1)%len(self.state[0])][y],
                    self.state[(x-1)%len(self.state[0])][(y+1)%len(self.state)],
                    self.state[x][(y-1)%len(self.state)],
                    self.state[x][(y+1)%len(self.state)],
                    self.state[(x+1)%len(self.state[0])][(y-1)%len(self.state)],
                    self.state[(x+1)%len(self.state[0])][y],
                    self.state[(x+1)%len(self.state[0])][(y+1)%len(self.state)]]
                    ones=list(filter(lambda x: x==1,neighbors))
                    if(self.state[x][y]==1):
                        if(len(ones)<2 or len(ones)>3): 
                            nextstate[x][y]=0
                        else: nextstate[x][y]=1
                    elif(self.state[x][y]==0):
                        if(len(ones)==3):
                            nextstate[x][y]=1
                        else: nextstate[x][y]=0
            self.state = nextstate

    def __repr__(self):
        if(type(self.state)==str):
            return self.state
        elif(type(self.state)==list):
            result = ""
            for x in range(len(self.state)):
                for y in range(len(self.state[0])):
                    result+=str(self.state[x][y])
                result+="\n"
            return result

