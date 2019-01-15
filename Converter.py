class Converter():
    def __init__(self, eq):
        self.equation = eq
        self.newEquation = "a"
        self.eqList = list(eq.string)
        self.uniqueLiterals = []

    def convertEquation(self):
        inc2 = -1
        for letter in self.eqList:
            inc2 += 1
            for literal in self.equation.LiteralDictionary:
                if letter is literal[0]:
                    self.eqList[inc2] = str(literal[1])
        self.newEquation = ''.join(self.eqList)