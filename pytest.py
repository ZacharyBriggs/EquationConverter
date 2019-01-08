class Clause():
    def __init__(self):
        self.array = []
    def Append(self,info):
        self.array.append(info)

class Equation():
    def __init__(self):
        self.VariableDictionary = dict()
        self.ClauseArray = []
    def AddVariable(self,name, value):
        self.VariableDictionary[name] = value
    def AddCaluse(self):
        self.ClauseArray.append(Clause())





eq = Equation()
eq.AddVariable("a",1)
eq.AddVariable("b",0)
print(eq.VariableDictionary.items())
doc = open("text.txt",'r')
docArray = doc.read()
docLength = docArray.len
inc = -1
for x in docArray:
    inc += 1
    if x == "(":
        '''begin clause'''
        eq.AddCaluse()
        for y in range(x,docLength):
            eq.ClauseArray[eq.ClauseArray.__len__()].Append(docArray[y])
            if(y == ")"):
                '''end caluse'''

        
    print(x)
