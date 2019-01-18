from Clause import Clause
class Equation():
    def __init__(self, eqString):
        self.string = eqString
        self.LiteralDictionary = []
        self.ClauseArray = []
        self.findClauses()
        self.findUniques()

    def setLiterals(self, literals):
        self.LiteralDictionary = []
        iterator = 0
        for i in range(97, 97 + literals.__len__()):
            self.LiteralDictionary.append([chr(i), literals[iterator]])
            iterator += 1
        self.LiteralDictionary.sort()

    def addClause(self, clause):
        self.ClauseArray.append(Clause(clause))

    def findClauses(self):
        eqList = list(self.string)
        inc = -1
        docLength = eqList.__len__()
        for x in eqList:
            inc += 1
            if x == "(":
                '''begin clause'''
                clause = []
                for y in range(inc,docLength):
                    clause.append(eqList[y])
                    if(eqList[y] == ")"):
                        '''end caluse'''
                        self.addClause(clause)
                        break

    def findUniques(self):
        for item in list(self.string):
            for i in range(97,123):
                if item is chr(i):
                    self.LiteralDictionary.append(item)
        for currentLiteral in self.LiteralDictionary:
            num = 0
            for literal in self.LiteralDictionary:
                if currentLiteral == literal:
                    num+=1
            for i in range(0,num-1):
                self.LiteralDictionary.remove(currentLiteral)

    def convert(self):
        for clause in self.ClauseArray:
            clause.convert(self.LiteralDictionary)

    def solve(self):
        numT = 0
        for clause in self.ClauseArray:
            if clause.solve():
                numT += 1
        return numT