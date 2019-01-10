class Clause():
    def __init__(self):
        self.array = []
    def Append(self,info):
        self.array.append(info)

class Equation():
    def __init__(self):
        self.LiteralDictionary = [("a",1)]
        self.ClauseArray = []
    def AddLiteral(self, tup):
        self.LiteralDictionary.append(tup)
    def AddCaluse(self):
        self.ClauseArray.append(Clause())


eq = Equation()
eq.AddLiteral(("b",1))
eq.AddLiteral(("c",0))
eq.AddLiteral(("d",1))
eq.AddLiteral(("e",0))
eq.AddLiteral(("f",1))
doc = open("text.txt",'r')
docList = list(doc.read())
docLength = docList.__len__()
inc = -1
for x in docList:
    inc += 1
    if x == "(":
        '''begin clause'''
        eq.AddCaluse()
        for y in range(inc,docLength):
            eq.ClauseArray[eq.ClauseArray.__len__()-1].Append(docList[y])
            if(y == ")"):
                '''end caluse'''
                break
inc2 = -1
for letter in docList:
    inc2 += 1
    for literal in eq.LiteralDictionary:
        if letter is literal[0]:
            docList[inc2] = str(literal[1])
newEq = ''.join(docList)
print(newEq)
exit()
'''Stuff to do:
    1. Allow the user to input the values of the literals
    2. Seperate classes into their own files and import them into a main
    3. Find out if there's a way to do a proper incrementing for loop
    4. '''