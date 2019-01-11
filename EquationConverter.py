class Clause():
    def __init__(self):
        self.array = []
    def Append(self,info):
        self.array.append(info)

class Equation():
    def __init__(self, eqString):
        self.string = eqString
        self.LiteralDictionary = []
        self.ClauseArray = []
    def AddLiteral(self, tup):
        self.LiteralDictionary.append(tup)
    def AddClause(self):
        self.ClauseArray.append(Clause())
    def FindClause(self):
        eqList = list(self.string)
        inc = -1
        docLength = eqList.__len__()
        for x in eqList:
            inc += 1
            if x == "(":
                '''begin clause'''
                self.ClauseArray.append(Clause())
                for y in range(inc,docLength):
                    eq.ClauseArray[eq.ClauseArray.__len__()-1].Append(eqList[y])
                    if(y == ")"):
                        '''end caluse'''
                        break

class Converter():
    def __init__(self, eq):
        self.equation = eq
        self.newEquation = "a"
        self.eqList = list(eq.string)
        self.uniqueLiterals = []
    def findUniques(self):
        for item in self.eqList:
            for i in range(97,123):
                if item is chr(i):
                    self.uniqueLiterals.append(item)
        for currentLiteral in self.uniqueLiterals:
            num = 0
            for literal in self.uniqueLiterals:
                if currentLiteral == literal:
                    num+=1
            for i in range(0,num-1):
                self.uniqueLiterals.remove(currentLiteral)
    def ConvertEquation(self):
        inc2 = -1
        for letter in self.eqList:
            inc2 += 1
            for literal in eq.LiteralDictionary:
                if letter is literal[0]:
                    self.eqList[inc2] = str(literal[1])
        self.newEquation = ''.join(self.eqList)

doc = open("text.txt",'r')
eq = Equation(doc.read())
re = Converter(eq)
eq.FindClause()
re.findUniques()

for i in range(97, 97 + re.uniqueLiterals.__len__()-1):
    value = input("Enter the value of" + " " + chr(i) + " ")
    eq.AddLiteral([chr(i), value])
re.ConvertEquation()
print(re.newEquation)
'''Stuff to do:
    1. Seperate classes into their own files and import them into a main
    2. Find out if there's a way to do a proper incrementing for loop '''