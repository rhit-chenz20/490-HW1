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
        self.rule_segs = {"000":1,"001":2,"010":4,"011":8,"100":16,"101":32,"110":64,"111":128}
        self.state = state
        self.ran = ran
        self.rule = rule

    def step(self):
        self.computeNextState()

    def computeNextState(self):
        old = self.state[len(self.state)-1]+self.state[:2]
        binint = int(old,2)
        nextstate = self.rule[binint:binint+1]
        for x in range(1, len(self.state)-1,1):
            cur = self.state[x-1:(x+2)]
            binint = int(cur,2)
            nextstate += self.rule[binint:binint+1]
        old = self.state[len(self.state)-2:]+self.state[:1]
        binint = int(old,2)
        nextstate += self.rule[binint:binint+1]
        self.state = nextstate

    def __repr__(self):
        return self.state
